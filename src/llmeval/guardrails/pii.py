"""Detect and redact common PII with patterns, plus a Luhn check for card numbers.

The sample data uses reserved example addresses, 555 numbers, and the public
Visa test PAN. Matches are replaced with placeholders. The raw value is not
copied into the finding details.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_EMAIL = re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")
_SSN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
_PHONE = re.compile(r"(?<!\d)(?:\+?1[-.\s])?(?:\(\d{3}\)|\d{3})[-.\s]\d{3}[-.\s]\d{4}(?!\d)")
_CARD = re.compile(r"\b(?:\d[ -]?){13,19}\b")

_PRIORITY = {"SSN": 4, "CREDIT_CARD": 3, "EMAIL": 2, "PHONE": 1}


@dataclass(frozen=True)
class PiiSpan:
    start: int
    end: int
    label: str
    replacement: str


def luhn_ok(digits: str) -> bool:
    total = 0
    double = False
    for char in reversed(digits):
        digit = int(char)
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        double = not double
    return total % 10 == 0


def _card_span(match: re.Match[str]) -> PiiSpan | None:
    digits = re.sub(r"\D", "", match.group(0))
    if not 13 <= len(digits) <= 19 or not luhn_ok(digits):
        return None
    return PiiSpan(match.start(), match.end(), "CREDIT_CARD", "[CREDIT_CARD]")


def find_pii(text: str) -> list[PiiSpan]:
    spans: list[PiiSpan] = []
    for match in _SSN.finditer(text):
        spans.append(PiiSpan(match.start(), match.end(), "SSN", "[SSN]"))
    for match in _EMAIL.finditer(text):
        spans.append(PiiSpan(match.start(), match.end(), "EMAIL", "[EMAIL]"))
    for match in _PHONE.finditer(text):
        spans.append(PiiSpan(match.start(), match.end(), "PHONE", "[PHONE]"))
    for match in _CARD.finditer(text):
        span = _card_span(match)
        if span is not None:
            spans.append(span)
    return _resolve_overlaps(spans)


def _resolve_overlaps(spans: list[PiiSpan]) -> list[PiiSpan]:
    ordered = sorted(
        spans,
        key=lambda span: (-_PRIORITY[span.label], -(span.end - span.start), span.start),
    )
    kept: list[PiiSpan] = []
    for span in ordered:
        overlaps = any(span.start < other.end and other.start < span.end for other in kept)
        if not overlaps:
            kept.append(span)
    return sorted(kept, key=lambda span: span.start)


def redact(text: str, spans: list[PiiSpan]) -> str:
    updated = text
    for span in sorted(spans, key=lambda item: item.start, reverse=True):
        updated = updated[: span.start] + span.replacement + updated[span.end :]
    return updated


class PIICheck:
    name = "pii"

    def check(self, text: str) -> dict[str, object]:
        spans = find_pii(text)
        labels = sorted({span.label for span in spans})
        high = bool({"SSN", "CREDIT_CARD"} & set(labels))
        if not spans:
            severity = "none"
            message = "no pii detected"
        elif high:
            severity = "high"
            message = f"found {len(spans)} pii span(s)"
        else:
            severity = "medium"
            message = f"found {len(spans)} pii span(s)"
        return {
            "triggered": bool(spans),
            "severity": severity,
            "message": message,
            "details": {
                "labels": labels,
                "count": len(spans),
                "redacted_text": redact(text, spans),
            },
        }
