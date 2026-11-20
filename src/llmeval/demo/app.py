"""Local demo API. Evaluation always goes through the configured backend.

The shipped configs use the mock backend, so the page runs without an API key.
"""

from __future__ import annotations

from importlib.resources import files
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, ValidationError

from llmeval import __version__
from llmeval.config import (
    default_eval_config,
    load_eval_config,
    load_guardrails_config,
    load_redteam_config,
)
from llmeval.guardrails import GuardrailEngine
from llmeval.models import RagExample
from llmeval.pipeline import evaluate_examples, run_guard
from llmeval.redteam import run_cases


class EvalIn(BaseModel):
    id: str = "ad-hoc"
    question: str = Field(min_length=1)
    contexts: list[str] = Field(min_length=1)
    answer: str = Field(min_length=1)
    ground_truth: str | None = None


class GuardIn(BaseModel):
    text: str = Field(min_length=1)
    stage: str = "input"


def _page() -> str:
    resource = files("llmeval.demo").joinpath("index.html")
    try:
        return resource.read_text(encoding="utf-8")
    except OSError:
        return Path(__file__).with_name("index.html").read_text(encoding="utf-8")


def create_app(config_dir: Path | None = None) -> FastAPI:
    directory = config_dir or Path("configs")
    api = FastAPI(title="llmeval", version=__version__)
    page = _page()

    @api.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "version": __version__, "backend": "mock"}

    @api.get("/", response_class=HTMLResponse)
    def index() -> str:
        return page

    @api.post("/api/evaluate")
    def evaluate(body: EvalIn) -> dict[str, object]:
        config_path = directory / "eval.yaml"
        try:
            if config_path.is_file():
                config = load_eval_config(config_path)
            else:
                config = default_eval_config()
            config.output.json_path = None
            config.output.markdown_path = None
            config.output.html_path = None
            example = RagExample(
                id=body.id,
                question=body.question,
                contexts=[context for context in body.contexts if context.strip()],
                answer=body.answer,
                ground_truth=body.ground_truth,
            )
            if not example.contexts:
                raise HTTPException(status_code=422, detail="contexts must include one passage")
            report = evaluate_examples([example], config, dataset_label="ad-hoc")
        except HTTPException:
            raise
        except (FileNotFoundError, ValueError, ValidationError) as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return report.model_dump()

    @api.post("/api/guard")
    def guard(body: GuardIn) -> dict[str, object]:
        config_path = directory / "guardrails.yaml"
        if body.stage not in {"input", "output"}:
            raise HTTPException(status_code=422, detail="stage must be input or output")
        if not config_path.is_file():
            raise HTTPException(status_code=400, detail=f"config not found: {config_path}")
        try:
            _config, report = run_guard(config_path, body.text, body.stage)
        except (FileNotFoundError, ValueError, ValidationError) as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return report.model_dump()

    @api.post("/api/redteam")
    def redteam() -> dict[str, object]:
        config_path = directory / "redteam.yaml"
        if not config_path.is_file():
            raise HTTPException(status_code=400, detail=f"config not found: {config_path}")
        try:
            config, cases = load_redteam_config(config_path)
            guard = load_guardrails_config(Path(config.guardrails))
            report = run_cases(cases, GuardrailEngine(guard))
        except (FileNotFoundError, ValueError, ValidationError) as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return report.model_dump()

    return api


app = create_app()
