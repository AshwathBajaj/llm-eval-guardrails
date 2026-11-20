"""Pattern detector for prompt injection and jailbreak phrasing.

The patterns look for instructions that try to override the system prompt,
switch the model into an unrestricted role, or smuggle a fake system turn.
They are a high-precision baseline. Spacing characters out, encoding the
request, or describing the attack in other words will get past them. The red
team suite includes one case like that so the report does not pretend the
detector is complete.
"""

from __future__ import annotations

import re

Pattern = tuple[str, re.Pattern[str], str]

PATTERNS: tuple[Pattern, ...] = (
    (
        "ignore_instructions",
        re.compile(
            r"\bignore\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+"
            r"(?:instructions|prompts|rules|directions)\b",
            re.IGNORECASE,
        ),
        "high",
    ),
    (
        "disregard_rules",
        re.compile(
            r"\bdisregard\s+(?:all|any|your|the)?\s*(?:\w+\s+){0,4}"
            r"(?:rules|guidelines|instructions|policies)\b",
            re.IGNORECASE,
        ),
        "high",
    ),
    (
        "forget_instructions",
        re.compile(
            r"\bforget\s+everything\s+(?:you\s+were\s+told|above|before)\b",
            re.IGNORECASE,
        ),
        "high",
    ),
    (
        "reveal_prompt",
        re.compile(
            r"\b(?:reveal|print|dump|leak|repeat|show)\b(?:\s+\w+){0,5}\s+"
            r"\b(?:system\s+prompt|hidden\s+instructions|initial\s+prompt)\b",
            re.IGNORECASE,
        ),
        "high",
    ),
    (
        "developer_mode",
        re.compile(
            r"\b(?:dan|developer)\s+mode\b|\bdo anything now\b|\bjailbreak\b",
            re.IGNORECASE,
        ),
        "high",
    ),
    (
        "role_override",
        re.compile(
            r"\byou are now\b(?:\s+\w+){0,4}\s+\b(?:unfiltered|unrestricted|dan)\b",
            re.IGNORECASE,
        ),
        "high",
    ),
    (
        "bypass_safety",
        re.compile(
            r"\bbypass\b(?:\s+\w+){0,4}\s+\b(?:safety|guardrails|filters|restrictions|policy)\b",
            re.IGNORECASE,
        ),
        "high",
    ),
    (
        "fake_system_turn",
        re.compile(r"<\s*/?\s*(?:system|im_start|im_end)\s*>", re.IGNORECASE),
        "high",
    ),
)

_SEVERITY_RANK = {"none": 0, "low": 1, "medium": 2, "high": 3}


def find_injections(text: str) -> list[dict[str, str]]:
    matches: list[dict[str, str]] = []
    for name, pattern, severity in PATTERNS:
        found = pattern.search(text)
        if found:
            matches.append({"rule": name, "severity": severity, "span": found.group(0)})
    return matches


def highest_severity(matches: list[dict[str, str]]) -> str:
    if not matches:
        return "none"
    return max(matches, key=lambda match: _SEVERITY_RANK[match["severity"]])["severity"]


class PromptInjectionCheck:
    name = "prompt_injection"

    def check(self, text: str) -> dict[str, object]:
        matches = find_injections(text)
        triggered = bool(matches)
        if triggered:
            message = "prompt injection pattern matched"
        else:
            message = "no injection pattern matched"
        return {
            "triggered": triggered,
            "severity": highest_severity(matches),
            "message": message,
            "details": {"matches": matches},
        }
