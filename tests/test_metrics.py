import json

from llmeval.backends.mock import MockBackend
from llmeval.config import MetricSpec, ScoringConfig, default_eval_config
from llmeval.embeddings import HashingEmbedder
from llmeval.metrics.context import ContextPrecisionMetric, ContextRecallMetric
from llmeval.metrics.faithfulness import FaithfulnessMetric
from llmeval.metrics.hallucination import HallucinationMetric
from llmeval.metrics.relevance import AnswerRelevanceMetric
from llmeval.models import RagExample
from llmeval.prompts import judge_prompt


def _spec(**overrides):
    data = {"threshold": 0.5, "support_threshold": 0.55, "relevance_threshold": 0.28}
    data.update(overrides)
    return MetricSpec(**data)


def _metric_args():
    return HashingEmbedder(), MockBackend(), ScoringConfig()


def test_copied_answer_is_more_faithful_than_an_invented_one():
    embedder, backend, scoring = _metric_args()
    metric = FaithfulnessMetric(embedder, backend, _spec(threshold=0.6), scoring)
    context = "The index stores embeddings so nearest-neighbor search can retrieve passages."
    grounded = RagExample(
        id="g",
        question="What does the index store?",
        contexts=[context],
        answer=context,
        ground_truth=context,
    )
    invented = RagExample(
        id="i",
        question="What does the index store?",
        contexts=[context],
        answer="Purple octopuses juggle quartz teacups on Mars.",
        ground_truth=context,
    )
    good = metric.compute(grounded)
    bad = metric.compute(invented)
    assert good.value > 0.8
    assert bad.value < 0.3
    assert good.judge is not None and good.judge > bad.judge


def test_negated_claim_is_not_treated_as_support():
    embedder, backend, scoring = _metric_args()
    metric = FaithfulnessMetric(embedder, backend, _spec(), scoring)
    example = RagExample(
        id="neg",
        question="Does the index store embeddings?",
        contexts=["The index stores embeddings."],
        answer="The index does not store embeddings.",
        ground_truth="The index stores embeddings.",
    )
    result = metric.compute(example)
    assert result.details["claims"][0]["supported"] is False
    assert result.baseline < 0.5


def test_relevance_prefers_an_answer_about_the_question():
    embedder, backend, scoring = _metric_args()
    metric = AnswerRelevanceMetric(embedder, backend, _spec(threshold=0.35), scoring)
    on_topic = RagExample(
        id="on",
        question="How does cosine similarity compare embeddings?",
        contexts=["unused"],
        answer="Cosine similarity compares embeddings by the angle between their vectors.",
    )
    off_topic = RagExample(
        id="off",
        question="How does cosine similarity compare embeddings?",
        contexts=["unused"],
        answer="Preheat the oven and cream the butter with sugar.",
    )
    assert metric.compute(on_topic).value > metric.compute(off_topic).value


def test_distractor_ranked_first_lowers_context_precision():
    embedder, backend, scoring = _metric_args()
    metric = ContextPrecisionMetric(embedder, backend, _spec(relevance_threshold=0.28), scoring)
    question = "What is a vector index used for?"
    relevant = "A vector index stores embeddings so nearest-neighbor search can retrieve passages."
    distractor = "Bananas are rich in potassium and grow in tropical climates."
    good = metric.compute(
        RagExample(id="good", question=question, contexts=[relevant, distractor], answer=relevant)
    )
    bad = metric.compute(
        RagExample(id="bad", question=question, contexts=[distractor, relevant], answer=relevant)
    )
    assert good.baseline > bad.baseline
    assert good.details["contexts"][0]["relevant"] is True
    assert bad.details["contexts"][0]["relevant"] is False


def test_recall_is_higher_when_the_ground_truth_is_in_the_context():
    embedder, backend, scoring = _metric_args()
    metric = ContextRecallMetric(embedder, backend, _spec(), scoring)
    truth = "A RAG system has a retriever and a generator."
    covered = metric.compute(
        RagExample(
            id="covered",
            question="What is RAG?",
            contexts=[truth],
            answer=truth,
            ground_truth=truth,
        )
    )
    missing = metric.compute(
        RagExample(
            id="missing",
            question="What is RAG?",
            contexts=["Language models predict the next token."],
            answer=truth,
            ground_truth=truth,
        )
    )
    absent = metric.compute(
        RagExample(id="absent", question="What is RAG?", contexts=[truth], answer=truth)
    )
    assert covered.baseline > missing.baseline
    assert absent.baseline == 0.0
    assert "missing" in absent.details["note"]


def test_hallucination_flags_a_contradiction_and_an_unrelated_answer():
    embedder, backend, _scoring = _metric_args()
    scoring = ScoringConfig(decision="baseline")
    metric = HallucinationMetric(embedder, backend, _spec(threshold=0.45), scoring)
    context = "The index stores embeddings."
    copied = metric.compute(
        RagExample(
            id="c",
            question="What does the index store?",
            contexts=[context],
            answer=context,
        )
    )
    contradicted = metric.compute(
        RagExample(
            id="n",
            question="What does the index store?",
            contexts=[context],
            answer="The index does not store embeddings.",
        )
    )
    assert copied.baseline < contradicted.baseline
    assert contradicted.details["labels"]["contradiction"] == 1
    assert copied.passed
    assert contradicted.passed is False


def test_bad_judge_json_falls_back_to_the_baseline():
    class BadBackend:
        name = "bad"

        def complete(self, prompt: str, *, temperature: float = 0.0) -> str:
            del prompt, temperature
            return "not json"

    embedder = HashingEmbedder()
    metric = FaithfulnessMetric(
        embedder,
        BadBackend(),
        _spec(),
        ScoringConfig(decision="blend", blend_judge_weight=0.5),
    )
    context = "The index stores embeddings."
    result = metric.compute(
        RagExample(id="x", question="What is stored?", contexts=[context], answer=context)
    )
    assert result.judge is None
    assert result.value == result.baseline
    assert "judge_error" in result.details


def test_blend_uses_the_judge_weight():
    class FixedBackend:
        name = "fixed"

        def complete(self, prompt: str, *, temperature: float = 0.0) -> str:
            del prompt, temperature
            return json.dumps({"score": 1.0, "reason": "fixed"})

    metric = FaithfulnessMetric(
        HashingEmbedder(),
        FixedBackend(),
        _spec(),
        ScoringConfig(decision="blend", blend_judge_weight=0.5),
    )
    result = metric.compute(
        RagExample(
            id="x",
            question="What is stored?",
            contexts=["The index stores embeddings."],
            answer="Purple octopuses juggle quartz teacups.",
        )
    )
    assert result.judge == 1.0
    assert result.baseline < 0.2
    assert result.value == round((result.baseline + 1.0) / 2, 4)


def test_default_config_enables_the_five_metrics():
    config = default_eval_config()
    assert set(config.metrics) == {
        "faithfulness",
        "answer_relevance",
        "context_precision",
        "context_recall",
        "hallucination",
    }


def test_parse_judge_output_accepts_json_inside_prose():
    from llmeval.prompts import parse_judge_output

    parsed = parse_judge_output('Here you go {"score": 0.25, "reason": "partial"} thanks')
    assert parsed.score == 0.25
    # The prompt helper stays importable for callers that build prompts in tests.
    assert "Task:" in judge_prompt("hallucination", {"ANSWER": "x"}, "rubric")
