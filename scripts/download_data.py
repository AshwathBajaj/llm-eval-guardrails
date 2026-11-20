"""Download the public slices llmeval evaluates, and cache them on disk.

The committed files are the slices this repo scores. Re-running the script
refreshes them from Hugging Face. CI does not run this script.

Datasets, all Apache-2.0 on the Hugging Face card we download:

- pminervini/HaluEval, config qa. A mirror of the HaluEval QA split
  (Li et al., 2023). The first 200 rows become 400 examples: one with
  right_answer and one with hallucinated_answer. The first 4 rows are also
  written to data/sample_rag.jsonl for offline CI.
- deepset/prompt-injections, test split. label 1 is an injection.
- jackhhao/jailbreak-classification, test split. type jailbreak or benign.

Curated cases in data/redteam_curated.yaml are kept and written out together
with the public cases.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache" / "hf"
SOURCE_ROWS = 200
SAMPLE_ROWS = 4
MAX_PROMPT_CHARS = 4000

HALUEVAL = "pminervini/HaluEval"
INJECTIONS = "deepset/prompt-injections"
JAILBREAKS = "jackhhao/jailbreak-classification"


def main() -> None:
    from datasets import load_dataset

    qa = load_dataset(HALUEVAL, "qa", split="data", cache_dir=str(CACHE))
    examples = _halueval_examples(qa.select(range(SOURCE_ROWS)))
    _write_jsonl(ROOT / "data" / "halueval_qa_slice.jsonl", examples)
    _write_jsonl(ROOT / "data" / "sample_rag.jsonl", examples[: SAMPLE_ROWS * 2])
    print(f"halueval examples {len(examples)} sample {SAMPLE_ROWS * 2}")

    injections = load_dataset(INJECTIONS, split="test", cache_dir=str(CACHE))
    jailbreaks = load_dataset(JAILBREAKS, split="test", cache_dir=str(CACHE))
    print("deepset label counts", _counts(injections, "label"))
    print("jailbreak type counts", _counts(jailbreaks, "type"))
    _print_injections(injections)

    curated = yaml.safe_load((ROOT / "data" / "redteam_curated.yaml").read_text(encoding="utf-8"))
    cases = list(curated["cases"])
    cases.extend(_injection_cases(injections))
    cases.extend(_jailbreak_cases(jailbreaks))
    payload = {
        "cases": cases,
    }
    text = yaml.safe_dump(payload, allow_unicode=True, sort_keys=False, width=1000)
    (ROOT / "data" / "redteam_cases.yaml").write_text(text, encoding="utf-8")
    print(f"redteam cases {len(cases)}")


def _halueval_examples(rows) -> list[dict[str, object]]:
    examples: list[dict[str, object]] = []
    for index, row in enumerate(rows):
        knowledge = str(row["knowledge"]).strip()
        question = str(row["question"]).strip()
        right = str(row["right_answer"]).strip()
        hallucinated = str(row["hallucinated_answer"]).strip()
        shared = {
            "question": question,
            "contexts": [knowledge],
            "ground_truth": right,
        }
        examples.append(
            {
                **shared,
                "id": f"halueval-qa-{index:04d}-right",
                "answer": right,
                "label": "right",
            }
        )
        examples.append(
            {
                **shared,
                "id": f"halueval-qa-{index:04d}-hallucinated",
                "answer": hallucinated,
                "label": "hallucinated",
            }
        )
    return examples


def _injection_cases(rows) -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []
    for index, row in enumerate(rows):
        text = str(row["text"]).strip()
        if not text or len(text) > MAX_PROMPT_CHARS:
            continue
        label = int(row["label"])
        cases.append(
            {
                "id": f"deepset-test-{index:04d}",
                "category": "prompt_injection" if label == 1 else "benign",
                "stage": "input",
                "text": text,
                "expect": "block" if label == 1 else "allow",
                "source": "deepset/prompt-injections",
            }
        )
    return cases


def _jailbreak_cases(rows) -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []
    kept = 0
    for index, row in enumerate(rows):
        kind = str(row["type"]).strip().lower()
        if kind not in {"jailbreak", "benign"}:
            continue
        text = str(row["prompt"]).strip()
        if not text or len(text) > MAX_PROMPT_CHARS:
            continue
        cases.append(
            {
                "id": f"jailbreak-test-{index:04d}",
                "category": "prompt_injection" if kind == "jailbreak" else "benign",
                "stage": "input",
                "text": text,
                "expect": "block" if kind == "jailbreak" else "allow",
                "source": "jackhhao/jailbreak-classification",
            }
        )
        kept += 1
    print(f"jailbreak cases kept {kept}")
    return cases


def _counts(rows, column: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        key = str(row[column])
        counts[key] = counts.get(key, 0) + 1
    return counts


def _print_injections(rows) -> None:
    shown = 0
    for row in rows:
        if int(row["label"]) != 1:
            continue
        print("injection example:", str(row["text"])[:180].replace("\n", " "))
        shown += 1
        if shown == 2:
            return


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    path.write_text(body, encoding="utf-8")


if __name__ == "__main__":
    main()
