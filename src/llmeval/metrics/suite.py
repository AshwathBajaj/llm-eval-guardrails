"""Build the metric objects selected in an eval config."""

from __future__ import annotations

from llmeval.backends.base import LLMBackend
from llmeval.config import METRIC_ORDER, EvalConfig
from llmeval.embeddings import EntailmentModel, TextEmbedder
from llmeval.metrics.context import ContextPrecisionMetric, ContextRecallMetric
from llmeval.metrics.faithfulness import FaithfulnessMetric
from llmeval.metrics.hallucination import HallucinationMetric
from llmeval.metrics.relevance import AnswerRelevanceMetric

Metric = (
    FaithfulnessMetric
    | AnswerRelevanceMetric
    | ContextPrecisionMetric
    | ContextRecallMetric
    | HallucinationMetric
)

_BUILDERS = {
    "faithfulness": FaithfulnessMetric,
    "answer_relevance": AnswerRelevanceMetric,
    "context_precision": ContextPrecisionMetric,
    "context_recall": ContextRecallMetric,
    "hallucination": HallucinationMetric,
}


def build_metrics(
    config: EvalConfig,
    embedder: TextEmbedder,
    backend: LLMBackend,
    nli: EntailmentModel | None = None,
) -> list[Metric]:
    metrics: list[Metric] = []
    for name in METRIC_ORDER:
        spec = config.metrics.get(name)
        if spec is None or not spec.enabled:
            continue
        builder = _BUILDERS[name]
        metrics.append(builder(embedder, backend, spec, config.scoring, nli))
    return metrics
