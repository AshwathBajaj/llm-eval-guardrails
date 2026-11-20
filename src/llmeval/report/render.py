"""JSON, Markdown, and HTML renderers for eval and red-team reports."""

from __future__ import annotations

import json
from importlib.resources import files
from pathlib import Path

from jinja2 import Environment, select_autoescape
from pydantic import BaseModel

from llmeval.models import EvaluationReport, ExampleReport, RedTeamReport


def dump_json(model: BaseModel) -> str:
    payload = model.model_dump()
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def _cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_eval_markdown(report: EvaluationReport) -> str:
    lines = [
        "# llmeval report",
        "",
        f"- Judge: `{report.backend}`",
        f"- Baseline: `{report.baseline_model}`",
        f"- NLI: `{report.nli_model or 'none'}`",
        f"- Dataset: `{report.dataset}`",
        f"- Scoring: `{report.scoring}`",
        f"- Examples: {report.example_count}",
        "",
    ]
    if report.dataset_info:
        info = report.dataset_info
        lines.extend(
            [
                f"- Dataset name: {info.get('name', '')}",
                f"- Source: {info.get('source', '')}",
                f"- License: {info.get('license', '')}",
                f"- Slice: {info.get('slice', '')}",
                "",
            ]
        )
    lines.extend(
        [
            "The headline value follows the scoring setting.",
            "When scoring is baseline, that value is the local model.",
            "The judge column is separate.",
            "The mock judge is a lexical scorer, not a neural LLM.",
            "Hallucination passes when the score is at or below its threshold.",
            "Every other metric passes when the score is at or above its threshold.",
            "",
            "## Aggregates",
            "",
            "| Metric | Mean | Threshold | Passed | Direction |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for aggregate in report.aggregates:
        direction = "higher is better" if aggregate.higher_is_better else "lower is better"
        total = aggregate.passed + aggregate.failed
        lines.append(
            f"| {_cell(aggregate.name)} | {aggregate.mean:.4f} | {aggregate.threshold:.4f} "
            f"| {aggregate.passed}/{total} | {direction} |"
        )
    for group in report.groups:
        lines.extend(["", f"## {group.label} ({group.example_count})", ""])
        lines.append("| Metric | Mean | Passed |")
        lines.append("| --- | ---: | ---: |")
        for aggregate in group.aggregates:
            total = aggregate.passed + aggregate.failed
            lines.append(
                f"| {_cell(aggregate.name)} | {aggregate.mean:.4f} | {aggregate.passed}/{total} |"
            )
    for example in report.examples:
        lines.extend(["", f"## {example.id}", "", _cell(example.question), ""])
        lines.append("| Metric | Value | Baseline | Judge | Passed |")
        lines.append("| --- | ---: | ---: | ---: | --- |")
        for metric in example.metrics:
            judge = "" if metric.judge is None else f"{metric.judge:.4f}"
            baseline = "" if metric.baseline is None else f"{metric.baseline:.4f}"
            lines.append(
                f"| {_cell(metric.name)} | {metric.value:.4f} | {baseline} | {judge} "
                f"| {'pass' if metric.passed else 'fail'} |"
            )
        reason = _first_reason(example)
        if reason:
            lines.extend(["", f"Judge note: {_cell(reason)}"])
        if example.input_guard is not None:
            lines.append(f"Input guard: {example.input_guard.decision}.")
        if example.output_guard is not None:
            lines.append(f"Output guard: {example.output_guard.decision}.")
    lines.append("")
    return "\n".join(lines)


def render_redteam_markdown(report: RedTeamReport) -> str:
    lines = [
        "# llmeval red team",
        "",
        f"- Cases: {report.total}",
        f"- Passed: {report.passed}",
        f"- Failed: {report.failed}",
        f"- Pass rate: {report.pass_rate:.4f}",
        "",
        "A case passes when the guardrail decision matches the expected decision.",
        "Benign cases are expected to be allowed, so blocking everything does not score 100%.",
        "",
        "## By source",
        "",
        "| Source | Passed | Pass rate |",
        "| --- | ---: | ---: |",
    ]
    for source in report.by_source:
        lines.append(
            f"| {_cell(source.source)} | {source.passed}/{source.total} | {source.pass_rate:.4f} |"
        )
    lines.extend(
        [
            "",
            "## By category",
            "",
            "| Category | Passed | Pass rate |",
            "| --- | ---: | ---: |",
        ]
    )
    for category in report.by_category:
        lines.append(
            f"| {_cell(category.category)} | {category.passed}/{category.total} "
            f"| {category.pass_rate:.4f} |"
        )
    lines.extend(["", "## Cases", ""])
    lines.append("| Id | Category | Expect | Decision | Result |")
    lines.append("| --- | --- | --- | --- | --- |")
    for case in report.cases:
        lines.append(
            f"| {_cell(case.id)} | {_cell(case.category)} | {case.expect} | {case.decision} "
            f"| {'pass' if case.passed else 'fail'} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_eval_html(report: EvaluationReport) -> str:
    return _template("eval.html").render(report=report)


def render_redteam_html(report: RedTeamReport) -> str:
    return _template("redteam.html").render(report=report)


def _template(name: str):
    environment = Environment(autoescape=select_autoescape(["html"]))
    return environment.from_string(_template_text(name))


def _template_text(name: str) -> str:
    resource = files("llmeval.report").joinpath(name)
    try:
        return resource.read_text(encoding="utf-8")
    except OSError:
        return (Path(__file__).resolve().parent / name).read_text(encoding="utf-8")


def _first_reason(example: ExampleReport) -> str:
    for metric in example.metrics:
        reason = metric.details.get("judge_reason")
        if isinstance(reason, str) and reason:
            return reason
    return ""
