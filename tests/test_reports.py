"""Offline reports are regenerated in CI. The benchmark report is not.

The benchmark file is the neural-baseline run on the HaluEval slice. CI does
not download those weights, so this test only checks that the committed file
is labeled as that run and that the right-answer group is more faithful than
the hallucinated group. The numbers themselves are whatever that run produced.
"""

import json
from pathlib import Path

from llmeval.config import (
    OutputConfig,
    load_eval_config,
    load_guardrails_config,
    load_redteam_config,
)
from llmeval.guardrails import GuardrailEngine
from llmeval.pipeline import display_path, evaluate_examples, load_examples
from llmeval.redteam import run_cases

ROOT = Path(__file__).resolve().parents[1]


def test_offline_eval_report_matches_a_fresh_run(monkeypatch):
    monkeypatch.chdir(ROOT)
    config = load_eval_config(ROOT / "configs" / "eval.yaml")
    config.output = OutputConfig()
    dataset = Path(config.dataset)
    report = evaluate_examples(
        load_examples(dataset),
        config,
        dataset_label=display_path(dataset),
    )
    path = ROOT / "examples" / "results" / "offline_eval_report.json"
    committed = json.loads(path.read_text(encoding="utf-8"))
    assert report.model_dump() == committed


def test_committed_sample_is_a_halueval_slice():
    rows = load_examples(ROOT / "data" / "sample_rag.jsonl")
    assert len(rows) == 8
    assert {row.label for row in rows} == {"right", "hallucinated"}
    assert all(row.id.startswith("halueval-qa-") for row in rows)
    assert all(row.contexts and row.ground_truth for row in rows)


def test_benchmark_report_is_the_neural_baseline():
    path = ROOT / "examples" / "results" / "eval_report.json"
    report = json.loads(path.read_text(encoding="utf-8"))
    assert "all-MiniLM-L6-v2" in report["baseline_model"]
    assert report["nli_model"] is not None
    assert "nli-MiniLM2-L6-H768" in report["nli_model"]
    assert report["backend"].startswith("mock:")
    assert report["scoring"] == "baseline"
    assert report["example_count"] == 400
    assert report["dataset_info"]["license"] == "Apache-2.0"
    groups = {group["label"]: group for group in report["groups"]}
    assert groups["right"]["example_count"] == 200
    assert groups["hallucinated"]["example_count"] == 200

    def mean(label: str, metric: str) -> float:
        aggregates = groups[label]["aggregates"]
        return next(item["mean"] for item in aggregates if item["name"] == metric)

    assert mean("right", "faithfulness") > mean("hallucinated", "faithfulness")
    assert mean("right", "hallucination") < mean("hallucinated", "hallucination")


def test_committed_redteam_report_matches_a_fresh_run():
    _config, cases = load_redteam_config(ROOT / "configs" / "redteam.yaml")
    guard = load_guardrails_config(ROOT / "configs" / "guardrails.yaml")
    report = run_cases(cases, GuardrailEngine(guard))
    path = ROOT / "examples" / "results" / "redteam_report.json"
    committed = json.loads(path.read_text(encoding="utf-8"))
    assert report.model_dump() == committed
