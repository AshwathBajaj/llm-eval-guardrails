"""Deterministic feature-hashing embedder.

Word unigrams and character trigrams are hashed into a fixed vector. Cosine
similarity is then reproducible and needs no model download. The vectors are
a lexical baseline, not a neural encoder: a paraphrase that shares no content
words will look unrelated. Swap this class for a neural embedder by keeping
the ``embed`` and ``cosine`` methods.
"""

from __future__ import annotations

import hashlib
import math

from llmeval.textutil import tokenize


def _bucket(feature: str, dim: int) -> tuple[int, float]:
    digest = hashlib.sha256(feature.encode("utf-8")).digest()
    index = int.from_bytes(digest[:4], "little") % dim
    sign = 1.0 if digest[4] % 2 == 0 else -1.0
    return index, sign


class HashingEmbedder:
    def __init__(self, dim: int = 256) -> None:
        if dim < 16:
            raise ValueError("embedder dim must be at least 16")
        self.dim = dim

    def embed(self, text: str) -> list[float]:
        vector = [0.0] * self.dim
        tokens = tokenize(text)
        if not tokens:
            return vector
        features = [f"w:{token}" for token in tokens]
        compact = " ".join(tokens)
        padded = f"  {compact}  "
        features.extend(f"c:{padded[index : index + 3]}" for index in range(len(padded) - 2))
        for feature in features:
            index, sign = _bucket(feature, self.dim)
            vector[index] += sign
        norm = math.sqrt(sum(value * value for value in vector))
        if norm == 0.0:
            return vector
        return [value / norm for value in vector]

    def cosine(self, left: str, right: str) -> float:
        left_vector = self.embed(left)
        right_vector = self.embed(right)
        return float(sum(a * b for a, b in zip(left_vector, right_vector, strict=True)))
