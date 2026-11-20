"""Context precision and context recall."""

from __future__ import annotations

from llmeval.backends.base import LLMBackend
from llmeval.config import MetricSpec, ScoringConfig
from llmeval.embeddings import EntailmentModel, TextEmbedder
from llmeval.metrics.common import (
    best_support,
    call_judge,
    claim_units,
    example_sections,
    finish_metric,
)
from llmeval.models import MetricResult, RagExample
from llmeval.scoring import precision_from_relevance, round4

_PRECISION_RUBRIC = (
    "Score whether retrieved contexts are about the question, with relevant "
    "contexts ranked first. 1 is perfect precision. 0 means nothing relevant."
)
_RECALL_RUBRIC = (
    "Score whether the contexts contain the information in the ground truth. "
    "1 means every ground-truth statement is covered. 0 means none are."
)


class ContextPrecisionMetric:
    name = "context_precision"
    higher_is_better = True

    def __init__(
        self,
        embedder: TextEmbedder,
        backend: LLMBackend,
        spec: MetricSpec,
        scoring: ScoringConfig,
        nli: EntailmentModel | None = None,
    ) -> None:
        self.embedder = embedder
        self.backend = backend
        self.spec = spec
        self.scoring = scoring
        self.nli = nli

    def compute(self, example: RagExample) -> MetricResult:
        rows: list[dict[str, object]] = []
        flags: list[bool] = []
        for rank, context in enumerate(example.contexts, start=1):
            if example.question:
                similarity = self.embedder.cosine(example.question, context)
            else:
                similarity = 0.0
            relevant = similarity >= self.spec.relevance_threshold
            flags.append(relevant)
            rows.append(
                {
                    "rank": rank,
                    "relevant": relevant,
                    "similarity": round4(similarity),
                }
            )
        baseline = precision_from_relevance(flags)
        judge, reason, error = call_judge(
            self.backend, self.name, _PRECISION_RUBRIC, example_sections(example)
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
            details={
                "contexts": rows,
                "relevance_threshold": self.spec.relevance_threshold,
            },
        )


class ContextRecallMetric:
    name = "context_recall"
    higher_is_better = True

    def __init__(
        self,
        embedder: TextEmbedder,
        backend: LLMBackend,
        spec: MetricSpec,
        scoring: ScoringConfig,
        nli: EntailmentModel | None = None,
    ) -> None:
        self.embedder = embedder
        self.backend = backend
        self.spec = spec
        self.scoring = scoring
        self.nli = nli

    def compute(self, example: RagExample) -> MetricResult:
        note = None
        rows: list[dict[str, object]] = []
        if not example.ground_truth or not example.ground_truth.strip():
            baseline = 0.0
            note = "ground_truth is missing, so recall is 0."
        else:
            statements = claim_units(example.ground_truth)
            for statement in statements:
                support, _evidence, _probs = best_support(
                    statement, example.contexts, self.embedder, self.nli
                )
                rows.append(
                    {
                        "statement": statement,
                        "support": round4(support),
                        "covered": support >= self.spec.support_threshold,
                    }
                )
            baseline = sum(1 for row in rows if row["covered"]) / len(rows) if rows else 0.0
        judge, reason, error = call_judge(
            self.backend, self.name, _RECALL_RUBRIC, example_sections(example)
        )
        details: dict[str, object] = {
            "statements": rows,
            "support_threshold": self.spec.support_threshold,
        }
        if note:
            details["note"] = note
        return finish_metric(
            name=self.name,
            higher_is_better=self.higher_is_better,
            baseline=baseline,
            judge=judge,
            judge_reason=reason,
            judge_error=error,
            spec=self.spec,
            scoring=self.scoring,
            details=details,
        )
