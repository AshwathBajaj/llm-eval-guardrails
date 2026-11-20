"""Text embedders.

``HashingEmbedder`` is the offline baseline used by tests and CI. It needs no
download. ``build_embedder`` can also construct a sentence-transformers model
when the config asks for one. That import happens inside the function so the
default install stays free of torch.
"""

from __future__ import annotations

import hashlib
import math
from typing import Protocol

from llmeval.config import EmbedderConfig
from llmeval.textutil import tokenize


class TextEmbedder(Protocol):
    name: str
    semantic: bool

    def cosine(self, left: str, right: str) -> float: ...


class EntailmentModel(Protocol):
    name: str

    def score_many(self, pairs: list[tuple[str, str]]) -> list[dict[str, float]]: ...


def _bucket(feature: str, dim: int) -> tuple[int, float]:
    digest = hashlib.sha256(feature.encode("utf-8")).digest()
    index = int.from_bytes(digest[:4], "little") % dim
    sign = 1.0 if digest[4] % 2 == 0 else -1.0
    return index, sign


class HashingEmbedder:
    semantic = False

    def __init__(self, dim: int = 256) -> None:
        if dim < 16:
            raise ValueError("embedder dim must be at least 16")
        self.dim = dim
        self.name = f"hashing-{dim}"

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


def build_embedder(config: EmbedderConfig) -> TextEmbedder:
    if config.type == "hash":
        return HashingEmbedder(dim=config.dim)
    if config.type == "sentence-transformers":
        from llmeval.neural import SentenceTransformerEmbedder

        return SentenceTransformerEmbedder(
            config.model,
            cache_dir=config.cache_dir,
            device=config.device,
        )
    raise ValueError(f"unknown embedder type: {config.type}")
