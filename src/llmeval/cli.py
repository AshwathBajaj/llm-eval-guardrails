"""Command line for evaluation, guardrails, the red team, and the demo server."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Annotated

import typer
from pydantic import ValidationError

from llmeval import __version__
from llmeval.pipeline import run_evaluation, run_guard, run_redteam

app = typer.Typer(add_completion=False, no_args_is_help=True)

EvalConfigPath = Annotated[
    Path,
    typer.Option(
        "--config",
        "-c",
        exists=True,
        dir_okay=False,
        readable=True,
        help="Path to an eval YAML file.",
    ),
]
GuardConfigPath = Annotated[
    Path,
    typer.Option(
        "--config",
        "-c",
        exists=True,
        dir_okay=False,
        readable=True,
        help="Path to a guardrails YAML file.",
    ),
]
RedTeamConfigPath = Annotated[
    Path,
    typer.Option(
        "--config",
        "-c",
        exists=True,
        dir_okay=False,
        readable=True,
        help="Path to a red-team YAML file.",
    ),
]


def _version(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=_version,
            is_eager=True,
            help="Print the version and exit.",
        ),
    ] = False,
) -> None:
    """Evaluate RAG outputs and apply LLM guardrails."""


@app.command()
def run(config: EvalConfigPath) -> None:
    """Score a JSONL dataset and write JSON, Markdown, and HTML reports."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    try:
        report, written = run_evaluation(config)
    except (FileNotFoundError, ValueError, ValidationError) as exc:
        _fail(exc)
        return
    nli = report.nli_model or "none"
    typer.echo(
        f"llmeval {report.version}  judge={report.backend}  "
        f"baseline={report.baseline_model}  nli={nli}  examples={report.example_count}"
    )
    for group in report.groups:
        typer.echo(f"  {group.label}: {group.example_count}")
    typer.echo(f"{'metric':<22}{'mean':>10}{'passed':>12}")
    for aggregate in report.aggregates:
        total = aggregate.passed + aggregate.failed
        typer.echo(f"{aggregate.name:<22}{aggregate.mean:10.4f}{aggregate.passed:>7}/{total}")
    for path in written:
        typer.echo(f"wrote {path}")


@app.command()
def guard(
    config: GuardConfigPath,
    text: Annotated[str | None, typer.Option("--text", help="Text to check.")] = None,
    file: Annotated[
        Path | None,
        typer.Option("--file", help="Read the text from this file."),
    ] = None,
    stage: Annotated[str, typer.Option("--stage", help="input or output.")] = "input",
) -> None:
    """Run input or output guardrails on one piece of text."""
    if (text is None) == (file is None):
        _fail(ValueError("pass exactly one of --text or --file"))
        return
    try:
        if text is None:
            assert file is not None
            payload = file.read_text(encoding="utf-8")
        else:
            payload = text
        _config, report = run_guard(config, payload, stage)
    except (FileNotFoundError, ValueError, ValidationError, OSError) as exc:
        _fail(exc)
        return
    typer.echo(f"decision: {report.decision}")
    if report.output_text != report.text:
        typer.echo(f"output: {report.output_text}")
    for finding in report.findings:
        if not finding.triggered:
            continue
        typer.echo(
            f"- {finding.guardrail} ({finding.action}, {finding.severity}): {finding.message}"
        )


@app.command()
def redteam(
    config: RedTeamConfigPath,
    fail_under: Annotated[
        float | None,
        typer.Option("--fail-under", help="Exit 1 if the pass rate is below this value."),
    ] = None,
) -> None:
    """Run the curated adversarial cases and report pass/fail."""
    try:
        report, written = run_redteam(config)
    except (FileNotFoundError, ValueError, ValidationError) as exc:
        _fail(exc)
        return
    typer.echo(f"pass rate {report.pass_rate:.4f}  ({report.passed}/{report.total})")
    for category in report.by_category:
        typer.echo(f"  {category.category:<22}{category.passed}/{category.total}")
    for case in report.cases:
        if not case.passed:
            typer.echo(f"  miss {case.id}: expected {case.expect}, got {case.decision}")
    for path in written:
        typer.echo(f"wrote {path}")
    if fail_under is not None and report.pass_rate < fail_under:
        raise typer.Exit(code=1)


@app.command()
def serve(
    host: Annotated[str, typer.Option("--host")] = "127.0.0.1",
    port: Annotated[int, typer.Option("--port")] = 8000,
    config_dir: Annotated[
        Path,
        typer.Option("--config-dir", help="Directory of YAML configs."),
    ] = Path("configs"),
) -> None:
    """Start the local FastAPI demo. It uses the mock backend."""
    import uvicorn

    from llmeval.demo.app import create_app

    uvicorn.run(create_app(config_dir.resolve()), host=host, port=port)


def _fail(exc: Exception) -> None:
    typer.echo(str(exc), err=True)
    raise typer.Exit(code=1)
