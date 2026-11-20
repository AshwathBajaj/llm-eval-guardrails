"""Fine-tune MiniLM to detect prompt injection and jailbreak prompts.

Training data is the deepset/prompt-injections train split and the
jackhhao/jailbreak-classification train split. Both cards say Apache-2.0.
A stratified 20% of that pool is the validation split. The threshold is
chosen only on validation, by the highest F1.

The test set is never used for training or for the threshold:
- the full deepset test split
- the jailbreak prompts already shipped in data/redteam_cases.yaml
  (the held-out jailbreak test rows the red team uses)

Texts are normalized and dropped from training if the same text is in the test set.
"""

from __future__ import annotations

import json
import random
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import torch
import yaml
from datasets import load_dataset
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

ROOT = Path(__file__).resolve().parents[1]
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
OUT_DIR = ROOT / "models" / "injection-minilm"
RESULTS = ROOT / "examples" / "results" / "injection_detector.json"
PLOT = ROOT / "docs" / "images" / "injection_confusion.png"
SEED = 42
EPOCHS = 3
BATCH = 16
MAX_LEN = 256
LR = 2e-5


def norm(text: str) -> str:
    return " ".join(text.lower().split())


def load_rows() -> tuple[list[tuple[str, int]], list[tuple[str, int]], dict[str, int]]:
    cache = str(ROOT / ".cache" / "hf")
    deep_train = load_dataset("deepset/prompt-injections", split="train", cache_dir=cache)
    deep_test = load_dataset("deepset/prompt-injections", split="test", cache_dir=cache)
    jail_train = load_dataset("jackhhao/jailbreak-classification", split="train", cache_dir=cache)
    jail_test = load_dataset("jackhhao/jailbreak-classification", split="test", cache_dir=cache)

    redteam = yaml.safe_load((ROOT / "data" / "redteam_cases.yaml").read_text(encoding="utf-8"))
    redteam_jail = {
        norm(str(case["text"]))
        for case in redteam["cases"]
        if case.get("source") == "jackhhao/jailbreak-classification"
    }

    test: list[tuple[str, int]] = []
    for row in deep_test:
        test.append((str(row["text"]), int(row["label"])))
    kept_jail_test = 0
    skipped_long = 0
    for row in jail_test:
        text = str(row["prompt"])
        if len(text) > 4000:
            skipped_long += 1
            continue
        if norm(text) not in redteam_jail:
            continue
        label = 1 if str(row["type"]).strip().lower() == "jailbreak" else 0
        test.append((text, label))
        kept_jail_test += 1

    test_keys = {norm(text) for text, _label in test}
    pool: list[tuple[str, int]] = []
    for row in deep_train:
        pool.append((str(row["text"]), int(row["label"])))
    for row in jail_train:
        kind = str(row["type"]).strip().lower()
        if kind not in {"jailbreak", "benign"}:
            continue
        pool.append((str(row["prompt"]), 1 if kind == "jailbreak" else 0))

    leaked = 0
    seen: set[str] = set()
    train_pool: list[tuple[str, int]] = []
    for text, label in pool:
        key = norm(text)
        if key in test_keys:
            leaked += 1
            continue
        if key in seen:
            continue
        seen.add(key)
        train_pool.append((text, label))

    stats = {
        "deepset_train_rows": len(deep_train),
        "deepset_test_rows": len(deep_test),
        "jailbreak_train_rows": len(jail_train),
        "jailbreak_test_rows": len(jail_test),
        "redteam_jailbreak_rows": len(redteam_jail),
        "jailbreak_test_rows_over_4000_chars_skipped": skipped_long,
        "jailbreak_test_rows_in_eval": kept_jail_test,
        "train_rows_removed_as_test_leaks": leaked,
        "train_pool_after_dedupe": len(train_pool),
        "test_rows": len(test),
    }
    return train_pool, test, stats


def stratified_split(
    rows: list[tuple[str, int]], val_fraction: float = 0.2
) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
    by_label: dict[int, list[tuple[str, int]]] = {0: [], 1: []}
    for row in rows:
        by_label[row[1]].append(row)
    rng = random.Random(SEED)
    train: list[tuple[str, int]] = []
    val: list[tuple[str, int]] = []
    for _label, group in by_label.items():
        rng.shuffle(group)
        cut = max(1, int(round(len(group) * val_fraction)))
        val.extend(group[:cut])
        train.extend(group[cut:])
    rng.shuffle(train)
    rng.shuffle(val)
    return train, val


class TextSet(Dataset):
    def __init__(self, rows: list[tuple[str, int]]) -> None:
        self.rows = rows

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, index: int) -> tuple[str, int]:
        return self.rows[index]


def collate(tokenizer, batch: list[tuple[str, int]]) -> dict[str, torch.Tensor]:
    texts = [item[0] for item in batch]
    labels = torch.tensor([item[1] for item in batch], dtype=torch.long)
    encoded = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=MAX_LEN,
        return_tensors="pt",
    )
    encoded["labels"] = labels
    return encoded


@torch.no_grad()
def predict_proba(model, tokenizer, texts: list[str]) -> list[float]:
    model.eval()
    probs: list[float] = []
    for start in range(0, len(texts), 32):
        chunk = texts[start : start + 32]
        encoded = tokenizer(
            chunk,
            padding=True,
            truncation=True,
            max_length=MAX_LEN,
            return_tensors="pt",
        )
        logits = model(**encoded).logits
        positive = torch.softmax(logits, dim=-1)[:, 1]
        probs.extend(float(value) for value in positive)
    return probs


def scores_at(labels: list[int], probs: list[float], threshold: float) -> dict[str, float]:
    tp = fp = tn = fn = 0
    for label, prob in zip(labels, probs, strict=True):
        pred = prob >= threshold
        if label == 1 and pred:
            tp += 1
        elif label == 0 and pred:
            fp += 1
        elif label == 0 and not pred:
            tn += 1
        else:
            fn += 1
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    fpr = fp / (fp + tn) if fp + tn else 0.0
    return {
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "false_positive_rate": round(fpr, 4),
    }


def best_threshold(labels: list[int], probs: list[float]) -> tuple[float, dict[str, float]]:
    best_t = 0.5
    best = scores_at(labels, probs, best_t)
    for step in range(1, 20):
        threshold = step / 20
        current = scores_at(labels, probs, threshold)
        better_f1 = current["f1"] > best["f1"]
        tie_lower_fpr = (
            current["f1"] == best["f1"]
            and current["false_positive_rate"] < best["false_positive_rate"]
        )
        if better_f1 or tie_lower_fpr:
            best_t = threshold
            best = current
    return best_t, best


def regex_flags(texts: list[str]) -> list[int]:
    from llmeval.guardrails.injection import find_injections

    return [1 if find_injections(text) else 0 for text in texts]


def metrics_from_flags(labels: list[int], flags: list[int]) -> dict[str, float]:
    probs = [1.0 if flag else 0.0 for flag in flags]
    return scores_at(labels, probs, 0.5)


def plot_matrices(labels: list[int], systems: dict[str, list[int]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6))
    for ax, (name, flags) in zip(axes, systems.items(), strict=True):
        matrix = scores_at(labels, [1.0 if flag else 0.0 for flag in flags], 0.5)
        grid = [[matrix["tn"], matrix["fp"]], [matrix["fn"], matrix["tp"]]]
        ax.imshow(grid, cmap="Blues")
        ax.set_xticks([0, 1], ["benign", "attack"])
        ax.set_yticks([0, 1], ["benign", "attack"])
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        ax.set_title(name)
        for row in range(2):
            for col in range(2):
                ax.text(col, row, str(grid[row][col]), ha="center", va="center", color="black")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def main() -> None:
    random.seed(SEED)
    torch.manual_seed(SEED)
    pool, test, stats = load_rows()
    train, val = stratified_split(pool)
    print("stats", json.dumps(stats))
    print("train", len(train), Counter(label for _t, label in train))
    print("val", len(val), Counter(label for _t, label in val))
    print("test", len(test), Counter(label for _t, label in test))

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)
    counts = Counter(label for _t, label in train)
    weights = torch.tensor(
        [len(train) / (2 * counts[0]), len(train) / (2 * counts[1])],
        dtype=torch.float,
    )
    criterion = torch.nn.CrossEntropyLoss(weight=weights)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR)
    loader = DataLoader(
        TextSet(train),
        batch_size=BATCH,
        shuffle=True,
        collate_fn=lambda batch: collate(tokenizer, batch),
    )

    best_state = None
    best_val_f1 = -1.0
    history = []
    for epoch in range(1, EPOCHS + 1):
        model.train()
        total = 0.0
        for batch in loader:
            labels = batch.pop("labels")
            logits = model(**batch).logits
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            total += float(loss) * labels.size(0)
        val_probs = predict_proba(model, tokenizer, [text for text, _label in val])
        val_labels = [label for _text, label in val]
        val_scores = scores_at(val_labels, val_probs, 0.5)
        history.append({"epoch": epoch, "train_loss": round(total / len(train), 4), **val_scores})
        print("epoch", epoch, history[-1])
        if val_scores["f1"] > best_val_f1:
            best_val_f1 = val_scores["f1"]
            best_state = {
                key: value.detach().cpu().clone() for key, value in model.state_dict().items()
            }

    if best_state is None:
        raise RuntimeError("training produced no checkpoint")
    model.load_state_dict(best_state)
    val_probs = predict_proba(model, tokenizer, [text for text, _label in val])
    val_labels = [label for _text, label in val]
    threshold, val_at_threshold = best_threshold(val_labels, val_probs)
    print("chosen threshold", threshold, val_at_threshold)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(OUT_DIR)
    tokenizer.save_pretrained(OUT_DIR)
    (OUT_DIR / "threshold.json").write_text(
        json.dumps(
            {
                "threshold": threshold,
                "method": "fine-tuned MiniLM sequence classifier",
                "base_model": MODEL_NAME,
                "epochs": EPOCHS,
                "seed": SEED,
                "max_length": MAX_LEN,
                "validation_metrics_at_threshold": val_at_threshold,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    test_texts = [text for text, _label in test]
    test_labels = [label for _text, label in test]
    import time

    t0 = time.perf_counter()
    regex = regex_flags(test_texts)
    regex_s = time.perf_counter() - t0

    t1 = time.perf_counter()
    probs = predict_proba(model, tokenizer, test_texts)
    clf_s = time.perf_counter() - t1
    clf_flags = [1 if prob >= threshold else 0 for prob in probs]

    from llmeval.guardrails.injection import find_injections

    t3 = time.perf_counter()
    hybrid_live: list[int] = []
    for text in test_texts:
        if find_injections(text):
            hybrid_live.append(1)
            continue
        encoded = tokenizer(text, truncation=True, max_length=MAX_LEN, return_tensors="pt")
        with torch.no_grad():
            logit = model(**encoded).logits
            prob = float(torch.softmax(logit, dim=-1)[0, 1])
        hybrid_live.append(1 if prob >= threshold else 0)
    hybrid_s = time.perf_counter() - t3

    n = len(test_texts)
    table = {
        "regex": {
            **metrics_from_flags(test_labels, regex),
            "mean_latency_ms": round(regex_s / n * 1000, 4),
        },
        "classifier": {
            **metrics_from_flags(test_labels, clf_flags),
            "mean_latency_ms": round(clf_s / n * 1000, 4),
        },
        "hybrid": {
            **metrics_from_flags(test_labels, hybrid_live),
            "mean_latency_ms": round(hybrid_s / n * 1000, 4),
        },
    }
    # The batched classifier latency is the fair model number. Hybrid uses the
    # per-prompt path so the table matches the guardrail implementation.
    print(json.dumps(table, indent=2))
    plot_matrices(
        test_labels,
        {"regex": regex, "classifier": clf_flags, "hybrid": hybrid_live},
        PLOT,
    )
    payload = {
        "base_model": MODEL_NAME,
        "method": "fine-tuned MiniLM sequence classifier",
        "licenses": {
            "deepset/prompt-injections": "Apache-2.0",
            "jackhhao/jailbreak-classification": "Apache-2.0",
            "sentence-transformers/all-MiniLM-L6-v2": "Apache-2.0",
        },
        "threshold_rule": (
            "On the validation split only, sweep 0.05, 0.10, ... 0.95 and keep "
            "the threshold with the highest F1. Ties go to the lower false-positive rate."
        ),
        "threshold": threshold,
        "validation_at_threshold": val_at_threshold,
        "history": history,
        "split_sizes": {
            "train": len(train),
            "validation": len(val),
            "test": len(test),
            **stats,
        },
        "test_label_counts": dict(Counter(str(label) for label in test_labels)),
        "test_metrics": table,
        "plot": str(PLOT.relative_to(ROOT)),
    }
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print("wrote", RESULTS)
    print("wrote", PLOT)


if __name__ == "__main__":
    main()
