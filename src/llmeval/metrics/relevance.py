"""Answer relevance: does the answer address the question that was asked?

The baseline is the better of two signals. Question coverage is the fraction of
the question's content words that appear in the answer, so a long grounded
answer is not punished for extra words. Cosine similarity is the embedding
signal and can carry a short paraphrase that coverage misses. The lexical
judge uses Jaccard, which does punish extra words, so the two columns differ.
"""

from __future__ import annotations

from llmeval.backends.base import LLMBackend
from llmeval.config import MetricSpec, ScoringConfig
from llmeval.embeddings import EntailmentModel, TextEmbedder
from llmeval.metrics.common import call_judge, example_sections, finish_metric
from llmeval.models import MetricResult, RagExample
from llmeval.scoring import round4
from llmeval.textutil import content_words, token_f1

_RUBRIC = (
    "Score how directly the answer addresses the question. "
    "1 is a direct answer. 0 is off-topic or empty. Ignore factual correctness."
)


class AnswerRelevanceMetric:
    name = "answer_relevance"
    higher_is_better = True

    def __init__(
        self,
        embedder: TextEmbedder,
        backend: LLMBackend,
        spec: MetricSpec,
        scoring: ScoringConfig,
        nli: EntailmentModel | None = None,
    ) -> None:
        del nli
        self.embedder = embedder
        self.backend = backend
        self.spec = spec
        self.scoring = scoring

    def compute(self, example: RagExample) -> MetricResult:
        if not example.answer.strip() or not example.question.strip():
            coverage = 0.0
            cosine = 0.0
            lexical = 0.0
        else:
            question_words = content_words(example.question)
            if question_words:
                overlap = question_words & content_words(example.answer)
                coverage = len(overlap) / len(question_words)
            else:
                coverage = 0.0
            cosine = self.embedder.cosine(example.question, example.answer)
            lexical = token_f1(example.question, example.answer)
        baseline = cosine if self.embedder.semantic else max(coverage, cosine)
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
            details={
                "question_coverage": round4(coverage),
                "cosine": round4(cosine),
                "token_f1": round4(lexical),
            },
        )
