"""Lexicon baseline for obvious abuse.

A word list catches clear insults and threats and misses implication, sarcasm,
and anything outside the list. Production traffic should add a classifier.
The list is short on purpose: it is a baseline you can read, not a blocklist
of slurs.
"""

from __future__ import annotations

import re

_PHRASES = (
    "kill yourself",
    "worthless idiot",
    "shut up",
    "piece of trash",
    "go die",
    "i hate you",
)
_WORDS = ("idiot", "moron", "dumbass", "worthless")


def find_toxicity(text: str) -> list[str]:
    lowered = text.lower()
    hits: list[str] = []
    for phrase in _PHRASES:
        if phrase in lowered:
            hits.append(phrase)
    for word in _WORDS:
        if re.search(rf"\b{re.escape(word)}\b", lowered):
            hits.append(word)
    # A phrase and the words inside it both match. Report each once, phrases first.
    seen: list[str] = []
    for hit in hits:
        if hit not in seen:
            seen.append(hit)
    return seen


class ToxicityCheck:
    name = "toxicity"

    def check(self, text: str) -> dict[str, object]:
        hits = find_toxicity(text)
        triggered = bool(hits)
        if triggered:
            message = "toxic language matched the lexicon"
            severity = "high"
        else:
            message = "no toxic language matched"
            severity = "none"
        return {
            "triggered": triggered,
            "severity": severity,
            "message": message,
            "details": {"matches": hits},
        }
