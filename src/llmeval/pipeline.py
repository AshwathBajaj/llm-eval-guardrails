"""Load a dataset, score it, optionally guard it, and write the report."""

from __future__ import annotations

import json
from pathlib import Path

from pydantic import ValidationError

from llmeval import __version__
from llmeval.backends import build_backend
from llmeval.config import (
    METRIC_ORDER,
    EvalConfig,
    GuardrailsConfig,
    OutputConfig,
    load_eval_config,
    load_guardrails_config,
    load_redteam_config,
)
from llmeval.embeddings import HashingEmbedder
from llmeval.guardrails import GuardrailEngine
from llmeval.metrics import build_metrics
from llmeval.models import (
    AggregateResult,
    EvaluationReport,
    ExampleReport,
    GuardReport,
    RagExample,
    RedTeamReport,
)
from llmeval.redteam import run_cases
from llmeval.report import (
    dump_json,
    render_eval_html,
    render_eval_markdown,
    render_redteam_html,
    render_redteam_markdown,
)
from llmeval.scoring import round4, scoring_label


def display_path(path: Path) -> str:
    """Prefer a path relative to the working directory so reports stay portable."""
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(resolved)


def load_examples(path: Path) -> list[RagExample]:
    if not path.is_file():
        raise FileNotFoundError(f"dataset not found: {path}")
    examples: list[RagExample] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            payload = json.loads(line)
            examples.append(RagExample.model_validate(payload))
        except (json.JSONDecodeError, ValidationError) as exc:
            raise ValueError(f"{path}:{line_no}: {exc}") from exc
    if not examples:
        raise ValueError(f"dataset is empty: {path}")
    return examples


def evaluate_examples(
    examples: list[RagExample],
    config: EvalConfig,
    *,
    dataset_label: str,
) -> EvaluationReport:
    backend = build_backend(config.backend)
    embedder = HashingEmbedder(config.embedder.dim)
    metrics = build_metrics(config, embedder, backend)
    engine: GuardrailEngine | None = None
    if config.guardrails:
        engine = GuardrailEngine(load_guardrails_config(Path(config.guardrails)), embedder)
    example_reports: list[ExampleReport] = []
    for example in examples:
        example_reports.append(
            ExampleReport(
                id=example.id,
                question=example.question,
                metrics=[metric.compute(example) for metric in metrics],
                input_guard=engine.run(example.question, "input") if engine else None,
                output_guard=engine.run(example.answer, "output") if engine else None,
            )
        )
    return EvaluationReport(
        version=__version__,
        backend=backend.name,
        dataset=dataset_label,
        scoring=scoring_label(config.scoring),
        example_count=len(example_reports),
        aggregates=_aggregates(example_reports),
        examples=example_reports,
    )


def run_evaluation(config_path: Path) -> tuple[EvaluationReport, list[Path]]:
    config = load_eval_config(config_path)
    if not config.dataset:
        raise ValueError("eval config is missing dataset")
    dataset = Path(config.dataset)
    examples = load_examples(dataset)
    report = evaluate_examples(examples, config, dataset_label=display_path(dataset))
    written = write_evaluation(report, config.output)
    return report, written


def run_redteam(config_path: Path) -> tuple[RedTeamReport, list[Path]]:
    config, cases = load_redteam_config(config_path)
    guard_config = load_guardrails_config(Path(config.guardrails))
    report = run_cases(cases, GuardrailEngine(guard_config))
    written = write_redteam(report, config.output)
    return report, written


def run_guard(config_path: Path, text: str, stage: str) -> tuple[GuardrailsConfig, GuardReport]:
    config = load_guardrails_config(config_path)
    report = GuardrailEngine(config).run(text, stage)
    return config, report


def write_evaluation(report: EvaluationReport, output: OutputConfig) -> list[Path]:
    return _write_trio(
        output,
        dump_json(report),
        render_eval_markdown(report),
        render_eval_html(report),
    )


def write_redteam(report: RedTeamReport, output: OutputConfig) -> list[Path]:
    return _write_trio(
        output,
        dump_json(report),
        render_redteam_markdown(report),
        render_redteam_html(report),
    )


def _write_trio(output: OutputConfig, json_text: str, markdown: str, html: str) -> list[Path]:
    written: list[Path] = []
    for path_value, text in (
        (output.json_path, json_text),
        (output.markdown_path, markdown),
        (output.html_path, html),
    ):
        if not path_value:
            continue
        path = Path(path_value)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        written.append(path)
    return written


def _aggregates(examples: list[ExampleReport]) -> list[AggregateResult]:
    aggregates: list[AggregateResult] = []
    for name in METRIC_ORDER:
        values: list[float] = []
        passed = 0
        failed = 0
        higher = True
        threshold = 0.0
        seen = False
        for example in examples:
            for metric in example.metrics:
                if metric.name != name:
                    continue
                seen = True
                values.append(metric.value)
                higher = metric.higher_is_better
                threshold = metric.threshold
                if metric.passed:
                    passed += 1
                else:
                    failed += 1
        if not seen:
            continue
        aggregates.append(
            AggregateResult(
                name=name,
                mean=round4(sum(values) / len(values)),
                higher_is_better=higher,
                passed=passed,
                failed=failed,
                threshold=threshold,
            )
        )
    return aggregates
