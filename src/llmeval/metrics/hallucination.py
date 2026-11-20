"""Hallucination risk: how much of the answer is unsupported or contradicted.

The headline baseline is the average unsupported mass of each claim
(1 minus its evidence score). A negation mismatch is treated as a
contradiction and raises that claim's risk. The novel-word rate is reported
beside it: content words in the answer that never appear in the context.
"""

from __future__ import annotations

from llmeval.backends.base import LLMBackend
from llmeval.config import MetricSpec, ScoringConfig
from llmeval.embeddings import HashingEmbedder
from llmeval.metrics.common import (
    best_support,
    call_judge,
    claim_units,
    example_sections,
    finish_metric,
)
from llmeval.models import MetricResult, RagExample
from llmeval.scoring import round4
from llmeval.textutil import content_words, polarity_conflict

_RUBRIC = (
    "Score the fraction of the answer that is not supported by the context. "
    "1 means the answer is unsupported. 0 means it is fully grounded."
)


def _nli_label(claim: str, support: float, evidence: str, threshold: float) -> str:
    if evidence and polarity_conflict(claim, evidence) and support >= 0.2:
        return "contradiction"
    if support >= threshold:
        return "entailment"
    return "neutral"


class HallucinationMetric:
    name = "hallucination"
    higher_is_better = False

    def __init__(
        self,
        embedder: HashingEmbedder,
        backend: LLMBackend,
        spec: MetricSpec,
        scoring: ScoringConfig,
    ) -> None:
        self.embedder = embedder
        self.backend = backend
        self.spec = spec
        self.scoring = scoring

    def compute(self, example: RagExample) -> MetricResult:
        claims = claim_units(example.answer)
        rows: list[dict[str, object]] = []
        risks: list[float] = []
        for claim in claims:
            support, evidence = best_support(claim, example.contexts, self.embedder)
            label = _nli_label(claim, support, evidence, self.spec.support_threshold)
            risk = 1.0 - support
            if label == "contradiction":
                risk = max(risk, 0.85)
            risks.append(risk)
            rows.append(
                {
                    "claim": claim,
                    "support": round4(support),
                    "risk": round4(risk),
                    "label": label,
                }
            )
        baseline = sum(risks) / len(risks) if risks else 0.0
        answer_words = content_words(example.answer)
        context_words = content_words("\n".join(example.contexts))
        if answer_words:
            novel = sorted(answer_words - context_words)
            novel_rate = len(novel) / len(answer_words)
        else:
            novel = []
            novel_rate = 0.0
        judge, reason, error = call_judge(
            self.backend, self.name, _RUBRIC, example_sections(example)
        )
        labels = {
            name: sum(1 for row in rows if row["label"] == name)
            for name in ("entailment", "neutral", "contradiction")
        }
        return finish_metric(
            name=self.name,
            higher_is_better=self.higher_is_better,
            baseline=baseline,
            judge=judge,
            judge_reason=reason,
            judge_error=error,
            spec=self.spec,
            scoring=self.scoring,
            details={
                "claims": rows,
                "labels": labels,
                "novel_word_rate": round4(novel_rate),
                "novel_words": novel[:24],
                "support_threshold": self.spec.support_threshold,
            },
        )
