"""Score blending and the context-precision formula.

Kept free of backend imports so the mock judge and the metrics can share it.
"""

from __future__ import annotations

from llmeval.config import ScoringConfig


def round4(value: float) -> float:
    return round(float(value), 4)


def scrub(value: object) -> object:
    """Round floats so a second run writes the same JSON."""
    if isinstance(value, float):
        return round4(value)
    if isinstance(value, dict):
        return {str(key): scrub(item) for key, item in value.items()}
    if isinstance(value, list):
        return [scrub(item) for item in value]
    return value


def combine_scores(baseline: float, judge: float | None, scoring: ScoringConfig) -> float:
    """Pick the number that pass/fail will use.

    A missing judge always falls back to the baseline. That keeps a bad
    response from the model from erasing a score we could compute locally.
    """
    if judge is None or scoring.decision == "baseline":
        return baseline
    if scoring.decision == "judge":
        return judge
    weight = min(max(scoring.blend_judge_weight, 0.0), 1.0)
    return weight * judge + (1.0 - weight) * baseline


def precision_from_relevance(relevant: list[bool]) -> float:
    """RAGAS-style context precision.

    For each relevant item at rank k, add Precision@k (relevant items in the
    first k positions, divided by k). Divide by the number of relevant items.
    Irrelevant items do not add a term, but they lower Precision@k for anything
    ranked after them. No relevant items yields 0.
    """
    relevant_total = sum(1 for flag in relevant if flag)
    if relevant_total == 0:
        return 0.0
    hits = 0
    weighted = 0.0
    for rank, flag in enumerate(relevant, start=1):
        if not flag:
            continue
        hits += 1
        weighted += hits / rank
    return weighted / relevant_total


def scoring_label(scoring: ScoringConfig) -> str:
    if scoring.decision == "blend":
        return f"blend(judge={scoring.blend_judge_weight:.2f})"
    return scoring.decision
