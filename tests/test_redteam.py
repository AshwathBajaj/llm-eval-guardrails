from pathlib import Path

from llmeval.config import load_guardrails_config, load_redteam_config
from llmeval.guardrails import GuardrailEngine
from llmeval.redteam import run_cases

ROOT = Path(__file__).resolve().parents[1]


def test_curated_suite_catches_known_attacks_and_allows_benign_text():
    _config, cases = load_redteam_config(ROOT / "configs" / "redteam.yaml")
    guard = load_guardrails_config(ROOT / "configs" / "guardrails.yaml")
    report = run_cases(cases, GuardrailEngine(guard))
    by_id = {case.id: case for case in report.cases}

    assert by_id["inj-ignore"].passed
    assert by_id["inj-ignore"].decision == "block"
    assert by_id["benign-ignore-word"].decision == "allow"
    assert by_id["benign-rag"].passed
    assert by_id["pii-email"].decision == "redact"
    assert "[EMAIL]" in by_id["pii-email"].output_text
    assert by_id["tox-insult"].decision == "block"
    assert by_id["tox-clean"].decision == "allow"
    assert by_id["topic-recipe"].decision == "block"
    assert by_id["topic-rag"].decision == "allow"
    assert by_id["schema-bad"].decision == "block"
    assert by_id["schema-ok"].decision == "allow"
    # A paraphrase with the same intent is a known miss. The suite records it.
    assert by_id["inj-paraphrase"].passed is False
    assert by_id["inj-paraphrase"].decision == "allow"
    assert report.failed >= 1
    assert report.pass_rate == round(report.passed / report.total, 4)
    assert report.pass_rate < 1.0
