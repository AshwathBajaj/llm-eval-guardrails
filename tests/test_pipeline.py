from pathlib import Path

import pytest

from llmeval.config import load_eval_config, normalize_metrics
from llmeval.pipeline import evaluate_examples, load_examples, run_evaluation

ROOT = Path(__file__).resolve().parents[1]


def test_unknown_metric_is_rejected():
    with pytest.raises(ValueError, match="unknown metric"):
        normalize_metrics({"bleu": {}})


def test_sample_dataset_orders_the_obvious_cases():
    config = load_eval_config(ROOT / "configs" / "eval.yaml")
    examples = load_examples(ROOT / "data" / "sample_rag.jsonl")
    report = evaluate_examples(examples, config, dataset_label="sample")
    by_id = {example.id: example for example in report.examples}

    def value(example_id, metric_name):
        example = by_id[example_id]
        return next(metric.value for metric in example.metrics if metric.name == metric_name)

    assert value("grounded-rag", "faithfulness") > value("mixed-claim", "faithfulness")
    assert value("mixed-claim", "faithfulness") > value("off-topic-answer", "faithfulness")
    assert value("grounded-rag", "hallucination") < value("off-topic-answer", "hallucination")
    grounded_precision = value("grounded-rag", "context_precision")
    distractor_precision = value("distractor-first", "context_precision")
    assert grounded_precision > distractor_precision
    assert value("grounded-rag", "context_recall") > value("missing-context", "context_recall")
    assert value("grounded-rag", "answer_relevance") > value("off-topic-answer", "answer_relevance")
    assert by_id["off-topic-answer"].output_guard is not None
    assert by_id["off-topic-answer"].output_guard.decision == "block"
    assert by_id["grounded-rag"].output_guard.decision == "allow"


def test_run_evaluation_writes_reports(tmp_path):
    # Use the real config but redirect outputs so the test does not depend on the worktree.
    source = (ROOT / "configs" / "eval.yaml").read_text(encoding="utf-8")
    config_path = tmp_path / "eval.yaml"
    config_path.write_text(
        source.replace("../examples/results/eval_report", "report"),
        encoding="utf-8",
    )
    # dataset and guardrails paths are relative to the config file. Point them back at the repo.
    text = config_path.read_text(encoding="utf-8")
    text = text.replace("../data/sample_rag.jsonl", str(ROOT / "data" / "sample_rag.jsonl"))
    guardrails = ROOT / "configs" / "guardrails.yaml"
    text = text.replace("guardrails: guardrails.yaml", f"guardrails: {guardrails}")
    config_path.write_text(text, encoding="utf-8")
    report, written = run_evaluation(config_path)
    assert report.example_count == 6
    names = {path.name for path in written}
    assert names == {"report.json", "report.md", "report.html"}
    assert (tmp_path / "report.md").read_text(encoding="utf-8").startswith("# llmeval report")
