"""Score a curated set of adversarial cases against a guardrail policy.

A case passes when the engine's decision equals the expected decision.
Allow-cases are part of the set on purpose: a policy that blocks every
string would fail them. Pass rate is therefore not "attacks blocked".
"""

from __future__ import annotations

from llmeval import __version__
from llmeval.config import RedTeamCase
from llmeval.guardrails.engine import GuardrailEngine
from llmeval.models import CategorySummary, RedTeamCaseResult, RedTeamReport, SourceSummary
from llmeval.scoring import round4


def run_cases(cases: list[RedTeamCase], engine: GuardrailEngine) -> RedTeamReport:
    results: list[RedTeamCaseResult] = []
    for case in cases:
        report = engine.run(case.text, case.stage, json_schema=case.json_schema)
        results.append(
            RedTeamCaseResult(
                id=case.id,
                category=case.category,
                source=case.source,
                stage=case.stage,
                expect=case.expect,
                decision=report.decision,
                passed=report.decision == case.expect,
                text=case.text,
                output_text=report.output_text,
                findings=report.findings,
            )
        )
    passed = sum(1 for result in results if result.passed)
    total = len(results)
    return RedTeamReport(
        version=__version__,
        total=total,
        passed=passed,
        failed=total - passed,
        pass_rate=round4(passed / total) if total else 0.0,
        by_category=_categories(results),
        by_source=_sources(results),
        cases=results,
    )


def _categories(results: list[RedTeamCaseResult]) -> list[CategorySummary]:
    names = sorted({result.category for result in results})
    summaries: list[CategorySummary] = []
    for name in names:
        rows = [result for result in results if result.category == name]
        passed = sum(1 for row in rows if row.passed)
        total = len(rows)
        summaries.append(
            CategorySummary(
                category=name,
                total=total,
                passed=passed,
                failed=total - passed,
                pass_rate=round4(passed / total) if total else 0.0,
            )
        )
    return summaries


def _sources(results: list[RedTeamCaseResult]) -> list[SourceSummary]:
    names = sorted({result.source for result in results})
    summaries: list[SourceSummary] = []
    for name in names:
        rows = [result for result in results if result.source == name]
        passed = sum(1 for row in rows if row.passed)
        total = len(rows)
        summaries.append(
            SourceSummary(
                source=name,
                total=total,
                passed=passed,
                failed=total - passed,
                pass_rate=round4(passed / total) if total else 0.0,
            )
        )
    return summaries
