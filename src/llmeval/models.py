"""Result objects written to reports and returned by the demo API."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class RagExample(BaseModel):
    id: str
    question: str
    contexts: list[str]
    answer: str
    ground_truth: str | None = None


class MetricResult(BaseModel):
    name: str
    value: float
    higher_is_better: bool
    baseline: float | None = None
    judge: float | None = None
    threshold: float
    passed: bool
    details: dict[str, Any] = Field(default_factory=dict)


class Finding(BaseModel):
    guardrail: str
    stage: str
    action: str
    triggered: bool
    severity: str
    message: str
    details: dict[str, Any] = Field(default_factory=dict)


class GuardReport(BaseModel):
    stage: str
    decision: str
    text: str
    output_text: str
    findings: list[Finding]


class ExampleReport(BaseModel):
    id: str
    question: str
    metrics: list[MetricResult]
    input_guard: GuardReport | None = None
    output_guard: GuardReport | None = None


class AggregateResult(BaseModel):
    name: str
    mean: float
    higher_is_better: bool
    passed: int
    failed: int
    threshold: float


class EvaluationReport(BaseModel):
    project: str = "llmeval"
    version: str
    backend: str
    dataset: str
    scoring: str
    example_count: int
    aggregates: list[AggregateResult]
    examples: list[ExampleReport]


class RedTeamCaseResult(BaseModel):
    id: str
    category: str
    stage: str
    expect: str
    decision: str
    passed: bool
    text: str
    output_text: str
    findings: list[Finding]


class CategorySummary(BaseModel):
    category: str
    total: int
    passed: int
    failed: int
    pass_rate: float


class RedTeamReport(BaseModel):
    project: str = "llmeval"
    version: str
    total: int
    passed: int
    failed: int
    pass_rate: float
    by_category: list[CategorySummary]
    cases: list[RedTeamCaseResult]
