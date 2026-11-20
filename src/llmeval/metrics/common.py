"""Shared claim-support score and the judge call used by every metric."""

from __future__ import annotations

from llmeval.backends.base import BackendError, LLMBackend
from llmeval.config import MetricSpec, ScoringConfig
from llmeval.embeddings import HashingEmbedder
from llmeval.models import MetricResult, RagExample
from llmeval.prompts import JudgeParseError, judge_prompt, parse_judge_output
from llmeval.scoring import combine_scores, round4, scrub
from llmeval.textutil import polarity_conflict, sentences, token_f1


def example_sections(example: RagExample) -> dict[str, str]:
    sections = {
        "QUESTION": example.question,
        "CONTEXTS": "\n---\n".join(example.contexts),
        "ANSWER": example.answer,
    }
    if example.ground_truth:
        sections["GROUND_TRUTH"] = example.ground_truth
    return sections


def claim_units(text: str) -> list[str]:
    return sentences(text) or ([text] if text.strip() else [])


def best_support(claim: str, contexts: list[str], embedder: HashingEmbedder) -> tuple[float, str]:
    """Best evidence score for one claim, and the passage that produced it.

    The score blends cosine similarity with token F1 so a high trigram-only
    cosine cannot, on its own, mark an unrelated sentence as supported.
    A negation mismatch caps the score: "does not store" is not support for
    "stores", even when the other words match. Polarity is judged against the
    matched sentence, not the whole context, so a "not" in a different passage
    does not poison a supported claim.
    """
    if not claim.strip() or not contexts:
        return 0.0, ""
    best = 0.0
    best_unit = ""
    for context in contexts:
        units = sentences(context) or [context]
        if context not in units:
            units.append(context)
        for unit in units:
            lexical = token_f1(claim, unit)
            blended = 0.5 * embedder.cosine(claim, unit) + 0.5 * lexical
            if blended >= 0.35 and polarity_conflict(claim, unit):
                blended = min(blended, 0.2)
            if blended > best:
                best = blended
                best_unit = unit
    return best, best_unit


def call_judge(
    backend: LLMBackend,
    task: str,
    rubric: str,
    sections: dict[str, str],
) -> tuple[float | None, str | None, str | None]:
    """Return ``(score, reason, error)``. A bad reply does not raise."""
    prompt = judge_prompt(task, sections, rubric)
    try:
        raw = backend.complete(prompt, temperature=0.0)
        parsed = parse_judge_output(raw)
    except (BackendError, JudgeParseError) as exc:
        return None, None, str(exc)
    return parsed.score, parsed.reason, None


def finish_metric(
    *,
    name: str,
    higher_is_better: bool,
    baseline: float,
    judge: float | None,
    judge_reason: str | None,
    judge_error: str | None,
    spec: MetricSpec,
    scoring: ScoringConfig,
    details: dict[str, object],
) -> MetricResult:
    value = combine_scores(baseline, judge, scoring)
    if higher_is_better:
        passed = value >= spec.threshold
    if not higher_is_better:
        passed = value <= spec.threshold
    if judge_reason:
        details["judge_reason"] = judge_reason
    if judge_error:
        details["judge_error"] = judge_error
    return MetricResult(
        name=name,
        value=round4(value),
        higher_is_better=higher_is_better,
        baseline=round4(baseline),
        judge=None if judge is None else round4(judge),
        threshold=spec.threshold,
        passed=passed,
        details=scrub(details),  # type: ignore[arg-type]
    )
