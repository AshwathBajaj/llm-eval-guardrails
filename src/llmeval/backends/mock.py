"""Offline judge.

The mock does not sample and does not invent a score. For judge prompts it
recomputes a lexical score from the sections in the prompt. For any other
prompt it returns a short, refusal-biased completion so the demo can run
with no API key. Those lexical scores are deliberately not the same formula
as the embedding baseline, so the two columns in a report can disagree.
"""

from __future__ import annotations

import json

from llmeval.guardrails.injection import find_injections
from llmeval.prompts import parse_judge_prompt
from llmeval.scoring import precision_from_relevance, round4
from llmeval.textutil import content_words, jaccard, sentences

_REFUSAL = "I can't help with that request. Ask a question about the documents you provided."
_SAFE_ANSWER = (
    "Retrieval-augmented generation uses a retriever to fetch passages and a "
    "generator to answer from those passages."
)


def _coverage(claim: str, context_words: set[str]) -> float:
    words = content_words(claim)
    if not words:
        return 0.0
    return len(words & context_words) / len(words)


def _contexts(sections: dict[str, str]) -> list[str]:
    raw = sections.get("CONTEXTS", "")
    return [part.strip() for part in raw.split("\n---\n") if part.strip()]


class MockBackend:
    def __init__(self, model: str = "mock-judge-v1") -> None:
        self.name = f"mock:{model}"
        self.model = model

    def complete(self, prompt: str, *, temperature: float = 0.0) -> str:
        del temperature  # the mock is deterministic on purpose
        task, sections = parse_judge_prompt(prompt)
        if task:
            score, reason = self._judge(task, sections)
            return json.dumps({"score": round4(score), "reason": reason})
        if find_injections(prompt):
            return _REFUSAL
        return _SAFE_ANSWER

    def _judge(self, task: str, sections: dict[str, str]) -> tuple[float, str]:
        contexts = _contexts(sections)
        context_words = content_words("\n".join(contexts))
        answer = sections.get("ANSWER", "")
        question = sections.get("QUESTION", "")
        ground_truth = sections.get("GROUND_TRUTH", "")

        if task == "faithfulness":
            claims = sentences(answer) or ([answer] if answer.strip() else [])
            if not claims:
                return 0.0, "The answer was empty."
            covered = [_coverage(claim, context_words) for claim in claims]
            score = sum(covered) / len(covered)
            return score, f"Mean lexical coverage across {len(claims)} claim(s)."

        if task == "hallucination":
            claims = sentences(answer) or ([answer] if answer.strip() else [])
            if not claims:
                return 0.0, "The answer was empty."
            unsupported = sum(1 for claim in claims if _coverage(claim, context_words) < 0.5)
            return unsupported / len(claims), (
                f"{unsupported} of {len(claims)} claim(s) had lexical coverage under 0.5."
            )

        if task == "answer_relevance":
            return jaccard(question, answer), "Jaccard overlap between question and answer."

        if task == "context_precision":
            question_words = content_words(question)
            flags: list[bool] = []
            for context in contexts:
                shared = question_words & content_words(context)
                flags.append(bool(question_words) and len(shared) / len(question_words) >= 0.34)
            score = precision_from_relevance(flags)
            return score, "Lexical context precision, relevant items first."

        if task == "context_recall":
            statements = sentences(ground_truth) or ([ground_truth] if ground_truth.strip() else [])
            if not statements or not contexts:
                return 0.0, "Ground truth or context was missing."
            covered = sum(
                1 for statement in statements if _coverage(statement, context_words) >= 0.5
            )
            return covered / len(statements), (
                f"{covered} of {len(statements)} ground-truth sentence(s) were covered."
            )

        return 0.0, f"No lexical judge is defined for task '{task}'."
