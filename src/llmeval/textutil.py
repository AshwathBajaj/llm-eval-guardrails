"""Small text helpers shared by the metrics, the mock judge, and the guardrails."""

from __future__ import annotations

import re

_TOKEN = re.compile(r"[a-z0-9]+", re.IGNORECASE)
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_BULLET = re.compile(r"^(?:[-*]|\d+[.)])\s+")

# Closed-class words. They dominate overlap scores and say little about grounding.
_STOPWORD_TEXT = """
a an the of to and or in on for with without from by as at is are was were be been
being it this that these those into over under than then so if not no yes do does
did doing can could should would will just about above below between within using
use used its their his her our your you we they them i me my which what who whom
when where why how all any each few more most other some such only own same too
very also per via across after before during while because both
"""
STOPWORDS = frozenset(_STOPWORD_TEXT.split())

# Polarity cues used by the lightweight entailment check. "no" is intentionally
# absent: it shows up in titles and lists and creates false contradictions.
NEGATION = re.compile(r"\b(?:not|never|cannot|without)\b|n't\b", re.IGNORECASE)


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in _TOKEN.finditer(text)]


def content_words(text: str) -> set[str]:
    return {token for token in tokenize(text) if token not in STOPWORDS and len(token) > 2}


def sentences(text: str) -> list[str]:
    """Split prose into sentences.

    This is a regex segmenter. Abbreviations such as "Dr." can split early;
    the sample data and tests avoid that case.
    """
    chunks: list[str] = []
    for raw_line in text.splitlines():
        line = _BULLET.sub("", raw_line.strip())
        if not line:
            continue
        chunks.extend(part.strip() for part in _SENTENCE_SPLIT.split(line) if part.strip())
    return chunks


def token_f1(left: str, right: str) -> float:
    left_words = content_words(left)
    right_words = content_words(right)
    if not left_words or not right_words:
        return 0.0
    overlap = len(left_words & right_words)
    if overlap == 0:
        return 0.0
    precision = overlap / len(left_words)
    recall = overlap / len(right_words)
    return 2 * precision * recall / (precision + recall)


def jaccard(left: str, right: str) -> float:
    left_words = content_words(left)
    right_words = content_words(right)
    if not left_words and not right_words:
        return 1.0
    if not left_words or not right_words:
        return 0.0
    return len(left_words & right_words) / len(left_words | right_words)


def has_negation(text: str) -> bool:
    return NEGATION.search(text) is not None


def polarity_conflict(claim: str, evidence: str) -> bool:
    """True when one side is negated and the other is not."""
    return has_negation(claim) != has_negation(evidence)
