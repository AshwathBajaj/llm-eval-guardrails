"""Fine-tuned MiniLM prompt-injection classifier.

The weights are produced by scripts/train_injection_classifier.py. Loading
this module does not import torch. The model is loaded only when a check
actually uses classifier or hybrid mode.
"""

from __future__ import annotations

import json
from pathlib import Path


class InjectionClassifier:
    def __init__(self, model_dir: Path) -> None:
        try:
            import torch
            from transformers import AutoModelForSequenceClassification, AutoTokenizer
        except ImportError as exc:
            raise RuntimeError(
                "The injection classifier needs torch and transformers. "
                'Install the neural extra: pip install -e ".[neural]"'
            ) from exc
        self.model_dir = model_dir
        meta_path = model_dir / "threshold.json"
        if not meta_path.is_file():
            raise FileNotFoundError(f"classifier metadata not found: {meta_path}")
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        self.threshold = float(meta["threshold"])
        self.method = str(meta["method"])
        self.max_length = int(meta.get("max_length", 256))
        self._torch = torch
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_dir)
        self.model.eval()

    def probability(self, text: str) -> float:
        encoded = self.tokenizer(
            text,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )
        with self._torch.no_grad():
            logits = self.model(**encoded).logits
            prob = self._torch.softmax(logits, dim=-1)[0, 1]
        return float(prob)


def default_model_dir() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "models" / "injection-minilm"
        if (candidate / "threshold.json").is_file():
            return candidate
    return here.parents[3] / "models" / "injection-minilm"
