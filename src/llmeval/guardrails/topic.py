"""Off-topic check for output that leaves the configured domain.

Two signals have to miss before the check fires. The primary one is a count of
in-domain content words, with a light prefix match so "retriever" and
"retrieves" agree. The secondary one is cosine similarity against the allowed
topic descriptions. A recipe fails both. An answer that uses the domain
vocabulary passes even if the hashing embedder is unsure.
"""

from __future__ import annotations

from llmeval.embeddings import TextEmbedder
from llmeval.scoring import round4
from llmeval.textutil import content_words


def _in_domain(token: str, terms: set[str]) -> bool:
    if token in terms:
        return True
    if len(token) < 5:
        return False
    for term in terms:
        if len(term) < 5:
            continue
        if token.startswith(term) or term.startswith(token):
            return True
    return False


def domain_hits(text: str, terms: list[str]) -> list[str]:
    vocabulary = {term.lower() for term in terms}
    hits = [token for token in sorted(content_words(text)) if _in_domain(token, vocabulary)]
    return hits


class TopicCheck:
    name = "off_topic"

    def __init__(
        self,
        embedder: TextEmbedder,
        *,
        allowed_topics: list[str],
        in_domain_terms: list[str],
        min_hits: int = 1,
        similarity_threshold: float = 0.22,
    ) -> None:
        self.embedder = embedder
        self.allowed_topics = allowed_topics
        self.in_domain_terms = in_domain_terms
        self.min_hits = min_hits
        self.similarity_threshold = similarity_threshold

    def check(self, text: str) -> dict[str, object]:
        if not self.allowed_topics and not self.in_domain_terms:
            return {
                "triggered": False,
                "severity": "none",
                "message": "off-topic check has no topics or terms configured",
                "details": {"hits": [], "similarity": 0.0},
            }
        hits = domain_hits(text, self.in_domain_terms)
        if self.allowed_topics and text.strip():
            similarity = max(self.embedder.cosine(text, topic) for topic in self.allowed_topics)
        else:
            similarity = 0.0
        on_topic = len(hits) >= self.min_hits or (
            bool(self.allowed_topics) and similarity >= self.similarity_threshold
        )
        triggered = not on_topic
        if triggered:
            message = "text is outside the configured topics"
            severity = "medium"
        else:
            message = "text is inside the configured topics"
            severity = "none"
        return {
            "triggered": triggered,
            "severity": severity,
            "message": message,
            "details": {
                "hits": hits,
                "hit_count": len(hits),
                "similarity": round4(similarity),
                "min_hits": self.min_hits,
                "similarity_threshold": self.similarity_threshold,
            },
        }
