"""YAML configuration for evaluation runs, guardrails, and the red-team suite."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

Action = Literal["allow", "flag", "redact", "block"]
BackendKind = Literal["mock", "openai"]
ScoreDecision = Literal["baseline", "judge", "blend"]
Stage = Literal["input", "output"]

METRIC_ORDER = (
    "faithfulness",
    "answer_relevance",
    "context_precision",
    "context_recall",
    "hallucination",
)

# Defaults are also written out in configs/eval.yaml. Keep the two in sync.
METRIC_DEFAULTS: dict[str, dict[str, float]] = {
    "faithfulness": {"threshold": 0.60, "support_threshold": 0.55},
    "answer_relevance": {"threshold": 0.35},
    "context_precision": {"threshold": 0.50, "relevance_threshold": 0.18},
    "context_recall": {"threshold": 0.50, "support_threshold": 0.55},
    "hallucination": {"threshold": 0.45, "support_threshold": 0.55},
}


class BackendConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: BackendKind = "mock"
    model: str = "mock-judge-v1"
    base_url: str = "https://api.openai.com/v1"
    api_key_env: str = "OPENAI_API_KEY"
    timeout_seconds: float = 60.0


class EmbedderConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["hash", "sentence-transformers"] = "hash"
    dim: int = 256
    model: str = "sentence-transformers/all-MiniLM-L6-v2"
    cache_dir: str | None = None
    device: str = "cpu"


class NLIConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = False
    model: str = "cross-encoder/nli-MiniLM2-L6-H768"
    cache_dir: str | None = None
    device: str = "cpu"


class DatasetInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    source: str
    license: str
    slice: str


class ScoringConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    decision: ScoreDecision = "blend"
    blend_judge_weight: float = 0.5


class MetricSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = True
    threshold: float = 0.5
    support_threshold: float = 0.55
    relevance_threshold: float = 0.18


class OutputConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    json_path: str | None = None
    markdown_path: str | None = None
    html_path: str | None = None


class EvalConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    backend: BackendConfig = Field(default_factory=BackendConfig)
    dataset: str | None = None
    embedder: EmbedderConfig = Field(default_factory=EmbedderConfig)
    nli: NLIConfig = Field(default_factory=NLIConfig)
    dataset_info: DatasetInfo | None = None
    scoring: ScoringConfig = Field(default_factory=ScoringConfig)
    metrics: dict[str, MetricSpec] = Field(default_factory=dict)
    guardrails: str | None = None
    output: OutputConfig = Field(default_factory=OutputConfig)


class InjectionConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = True
    action: Action = "block"


class PIIConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = True
    action: Action = "redact"


class ToxicityConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = True
    action: Action = "block"


class TopicConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = True
    action: Action = "block"
    allowed_topics: list[str] = Field(default_factory=list)
    in_domain_terms: list[str] = Field(default_factory=list)
    min_hits: int = 1
    similarity_threshold: float = 0.22


class SchemaConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = False
    action: Action = "block"
    json_schema: dict[str, Any] | None = None


class InputPolicy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    prompt_injection: InjectionConfig = Field(default_factory=InjectionConfig)
    pii: PIIConfig = Field(default_factory=PIIConfig)


class OutputPolicy(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    prompt_injection: InjectionConfig = Field(
        default_factory=lambda: InjectionConfig(enabled=False)
    )
    toxicity: ToxicityConfig = Field(default_factory=ToxicityConfig)
    off_topic: TopicConfig = Field(default_factory=TopicConfig)
    schema_check: SchemaConfig = Field(default_factory=SchemaConfig, alias="schema")


class GuardrailsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    embedder: EmbedderConfig = Field(default_factory=EmbedderConfig)
    input: InputPolicy = Field(default_factory=InputPolicy)
    output: OutputPolicy = Field(default_factory=OutputPolicy)


class RedTeamCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    category: str
    stage: Stage
    text: str
    expect: Action
    json_schema: dict[str, Any] | None = None
    source: str = "curated"


class RedTeamFile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    guardrails: str
    cases: str
    output: OutputConfig = Field(default_factory=OutputConfig)


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"config not found: {path}")
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return loaded


def _resolve(value: str | None, base: Path) -> str | None:
    if value is None:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = (base / path).resolve()
    return str(path)


def normalize_metrics(raw: dict[str, Any] | None) -> dict[str, Any]:
    """Fill per-metric defaults without clobbering values the file set on purpose."""
    source: dict[str, Any] = raw if raw else {name: {} for name in METRIC_ORDER}
    unknown = sorted(set(source) - set(METRIC_ORDER))
    if unknown:
        known = ", ".join(METRIC_ORDER)
        raise ValueError(f"unknown metric(s): {', '.join(unknown)}. Known metrics: {known}")
    normalized: dict[str, Any] = {}
    for name, spec in source.items():
        if spec is None:
            spec = {}
        if not isinstance(spec, dict):
            raise ValueError(f"metric '{name}' must be a mapping")
        merged: dict[str, Any] = {"enabled": True}
        merged.update(METRIC_DEFAULTS[name])
        merged.update(spec)
        normalized[name] = merged
    return normalized


def default_eval_config() -> EvalConfig:
    return EvalConfig.model_validate({"metrics": normalize_metrics(None)})


def load_eval_config(path: Path) -> EvalConfig:
    raw = read_yaml(path)
    raw["metrics"] = normalize_metrics(raw.get("metrics"))
    config = EvalConfig.model_validate(raw)
    base = path.parent
    config.dataset = _resolve(config.dataset, base)
    config.guardrails = _resolve(config.guardrails, base)
    config.output.json_path = _resolve(config.output.json_path, base)
    config.output.markdown_path = _resolve(config.output.markdown_path, base)
    config.output.html_path = _resolve(config.output.html_path, base)
    return config


def load_guardrails_config(path: Path) -> GuardrailsConfig:
    return GuardrailsConfig.model_validate(read_yaml(path))


def load_redteam_config(path: Path) -> tuple[RedTeamFile, list[RedTeamCase]]:
    raw = read_yaml(path)
    config = RedTeamFile.model_validate(raw)
    base = path.parent
    config.guardrails = _resolve(config.guardrails, base) or config.guardrails
    config.cases = _resolve(config.cases, base) or config.cases
    config.output.json_path = _resolve(config.output.json_path, base)
    config.output.markdown_path = _resolve(config.output.markdown_path, base)
    config.output.html_path = _resolve(config.output.html_path, base)
    cases_raw = read_yaml(Path(config.cases))
    rows = cases_raw.get("cases")
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"{config.cases} must contain a non-empty 'cases' list")
    cases = [RedTeamCase.model_validate(row) for row in rows]
    return config, cases
