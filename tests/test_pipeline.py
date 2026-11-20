from pathlib import Path

import pytest

from llmeval.config import load_eval_config, normalize_metrics
from llmeval.pipeline import evaluate_examples, load_examples, run_evaluation

ROOT = Path(__file__).resolve().parents[1]


def test_unknown_metric_is_rejected():
    with pytest.raises(ValueError, match="unknown metric"):
        normalize_metrics({"bleu": {}})


def test_pipeline_separates_a_copied_answer_from_an_unrelated_one():
    from llmeval.models import RagExample

    config = load_eval_config(ROOT / "configs" / "eval.yaml")
    context = "The index stores embeddings so nearest-neighbor search can retrieve passages."
    examples = [
        RagExample(
            id="copied",
            question="What does the index store?",
            contexts=[context],
            answer=context,
            ground_truth=context,
        ),
        RagExample(
            id="unrelated",
            question="What does the index store?",
            contexts=[context],
            answer="Preheat the oven and cream the butter with sugar.",
            ground_truth=context,
        ),
    ]
    report = evaluate_examples(examples, config, dataset_label="inline")
    by_id = {example.id: example for example in report.examples}

    def value(example_id: str, metric_name: str) -> float:
        example = by_id[example_id]
        return next(metric.value for metric in example.metrics if metric.name == metric_name)

    assert value("copied", "faithfulness") > value("unrelated", "faithfulness")
    assert value("copied", "hallucination") < value("unrelated", "hallucination")


def test_run_evaluation_writes_reports(tmp_path):
    # Use the real config but redirect outputs so the test does not depend on the worktree.
    source = (ROOT / "configs" / "eval.yaml").read_text(encoding="utf-8")
    config_path = tmp_path / "eval.yaml"
    config_path.write_text(
        source.replace("../examples/results/offline_eval_report", "report"),
        encoding="utf-8",
    )
    # dataset and guardrails paths are relative to the config file. Point them back at the repo.
    text = config_path.read_text(encoding="utf-8")
    text = text.replace("../data/sample_rag.jsonl", str(ROOT / "data" / "sample_rag.jsonl"))
    guardrails = ROOT / "configs" / "guardrails.yaml"
    text = text.replace("guardrails: guardrails.yaml", f"guardrails: {guardrails}")
    config_path.write_text(text, encoding="utf-8")
    report, written = run_evaluation(config_path)
    assert report.example_count == len(load_examples(ROOT / "data" / "sample_rag.jsonl"))
    names = {path.name for path in written}
    assert names == {"report.json", "report.md", "report.html"}
    assert (tmp_path / "report.md").read_text(encoding="utf-8").startswith("# llmeval report")
