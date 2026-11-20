"""Local CPU models for the non-LLM baseline.

Imported only when a config selects them. The hash embedder remains the
default so tests and CI never download weights.
"""

from __future__ import annotations

import logging

from llmeval.config import NLIConfig

logger = logging.getLogger(__name__)

_MISSING = (
    'sentence-transformers is not installed. Install the neural extra: pip install -e ".[neural]"'
)


class SentenceTransformerEmbedder:
    """Bi-encoder. Vectors are L2-normalized, so cosine is a dot product."""

    semantic = True

    def __init__(self, model_name: str, *, cache_dir: str | None, device: str) -> None:
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise RuntimeError(_MISSING) from exc
        self.name = f"sentence-transformers:{model_name}"
        self.model_name = model_name
        logger.info("loading embedder %s on %s", model_name, device)
        self.model = SentenceTransformer(model_name, cache_folder=cache_dir, device=device)
        self._cache: dict[str, list[float]] = {}

    def embed(self, text: str) -> list[float]:
        cached = self._cache.get(text)
        if cached is not None:
            return cached
        vector = self.model.encode(text, normalize_embeddings=True, show_progress_bar=False)
        stored = [float(value) for value in vector]
        self._cache[text] = stored
        return stored

    def cosine(self, left: str, right: str) -> float:
        left_vector = self.embed(left)
        right_vector = self.embed(right)
        return float(sum(a * b for a, b in zip(left_vector, right_vector, strict=True)))


class NLICrossEncoder:
    """Three-way NLI. ``score_many`` returns entailment, contradiction, neutral."""

    def __init__(self, model_name: str, *, cache_dir: str | None, device: str) -> None:
        try:
            from sentence_transformers import CrossEncoder
        except ImportError as exc:
            raise RuntimeError(_MISSING) from exc
        del cache_dir  # CrossEncoder uses the Hugging Face cache, not this folder.
        self.name = f"cross-encoder:{model_name}"
        self.model_name = model_name
        logger.info("loading nli model %s on %s", model_name, device)
        self.model = CrossEncoder(model_name, device=device, max_length=256)
        id2label = self.model.model.config.id2label
        labels: list[str] = []
        for index in range(len(id2label)):
            label = id2label.get(index, id2label.get(str(index)))
            if not isinstance(label, str):
                raise RuntimeError(f"{model_name} has no label for class {index}")
            labels.append(label)
        if "entailment" not in labels:
            raise RuntimeError(f"{model_name} has no entailment label: {labels}")
        self.labels = labels

    def score_many(self, pairs: list[tuple[str, str]]) -> list[dict[str, float]]:
        if not pairs:
            return []
        raw = self.model.predict(
            list(pairs),
            batch_size=32,
            show_progress_bar=False,
            apply_softmax=True,
        )
        scored: list[dict[str, float]] = []
        for row in raw:
            scored.append({label: float(row[index]) for index, label in enumerate(self.labels)})
        return scored


def build_nli(config: NLIConfig) -> NLICrossEncoder | None:
    if not config.enabled:
        return None
    return NLICrossEncoder(config.model, cache_dir=config.cache_dir, device=config.device)
