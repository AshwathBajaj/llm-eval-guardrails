"""Faithfulness: how much of the answer is supported by the retrieved context."""

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

_RUBRIC = (
    "Score the fraction of answer sentences supported by the context. "
    "1 means every sentence is supported. 0 means none are."
)


class FaithfulnessMetric:
    name = "faithfulness"
    higher_is_better = True

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
        for claim in claims:
            support, _evidence = best_support(claim, example.contexts, self.embedder)
            rows.append(
                {
                    "claim": claim,
                    "support": round4(support),
                    "supported": support >= self.spec.support_threshold,
                }
            )
        baseline = sum(1 for row in rows if row["supported"]) / len(rows) if rows else 0.0
        judge, reason, error = call_judge(
            self.backend, self.name, _RUBRIC, example_sections(example)
        )
        return finish_metric(
            name=self.name,
            higher_is_better=self.higher_is_better,
            baseline=baseline,
            judge=judge,
            judge_reason=reason,
            judge_error=error,
            spec=self.spec,
            scoring=self.scoring,
            details={"claims": rows, "support_threshold": self.spec.support_threshold},
        )
