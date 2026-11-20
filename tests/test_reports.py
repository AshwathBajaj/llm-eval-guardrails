"""The checked-in reports are the output of a real mock-backend run.

If a change moves a score, this test fails until the reports are regenerated.
That keeps the README from drifting away from the code.
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


def test_committed_eval_report_matches_a_fresh_run(monkeypatch):
    monkeypatch.chdir(ROOT)
    config = load_eval_config(ROOT / "configs" / "eval.yaml")
    config.output = OutputConfig()
    dataset = Path(config.dataset)
    report = evaluate_examples(
        load_examples(dataset),
        config,
        dataset_label=display_path(dataset),
    )
    committed = json.loads((ROOT / "examples" / "results" / "eval_report.json").read_text())
    assert report.model_dump() == committed


def test_committed_redteam_report_matches_a_fresh_run():
    _config, cases = load_redteam_config(ROOT / "configs" / "redteam.yaml")
    guard = load_guardrails_config(ROOT / "configs" / "guardrails.yaml")
    report = run_cases(cases, GuardrailEngine(guard))
    committed = json.loads((ROOT / "examples" / "results" / "redteam_report.json").read_text())
    assert report.model_dump() == committed
