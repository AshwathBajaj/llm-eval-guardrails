"""Streamlit demo for Streamlit Community Cloud.

Same checks as the Gradio app: NLI faithfulness, MiniLM relevance, the mock
judge, and regex / classifier / hybrid injection verdicts. Models load once
per process through st.cache_resource. Thread counts are capped so the free
1 GB instance has a better chance of staying up.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import json
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from app import (  # noqa: E402
    GROUNDED_ANSWER,
    GROUNDED_CONTEXT,
    GROUNDED_QUESTION,
    JAILBREAK_QUESTION,
    _verdict,
)

from llmeval.backends import build_backend  # noqa: E402
from llmeval.config import (  # noqa: E402
    BackendConfig,
    EmbedderConfig,
    MetricSpec,
    NLIConfig,
    ScoringConfig,
)
from llmeval.embeddings import build_embedder  # noqa: E402
from llmeval.guardrails.injection import PromptInjectionCheck  # noqa: E402
from llmeval.metrics.faithfulness import FaithfulnessMetric  # noqa: E402
from llmeval.metrics.relevance import AnswerRelevanceMetric  # noqa: E402
from llmeval.models import RagExample  # noqa: E402
from llmeval.neural import build_nli  # noqa: E402


def _hallucinated_answer() -> str:
    path = ROOT / "data" / "sample_rag.jsonl"
    with path.open(encoding="utf-8") as handle:
        next(handle)
        row = json.loads(next(handle))
    return str(row["answer"])


HALLUCINATED_ANSWER = _hallucinated_answer()


@st.cache_resource
def load_models() -> dict[str, object]:
    import torch

    torch.set_num_threads(1)
    embedder = build_embedder(EmbedderConfig(type="sentence-transformers", device="cpu"))
    nli = build_nli(NLIConfig(enabled=True, device="cpu"))
    backend = build_backend(BackendConfig())
    scoring = ScoringConfig(decision="baseline")
    return {
        "faith": FaithfulnessMetric(
            embedder,
            backend,
            MetricSpec(threshold=0.5, support_threshold=0.5),
            scoring,
            nli,
        ),
        "relevance": AnswerRelevanceMetric(
            embedder,
            backend,
            MetricSpec(threshold=0.3),
            scoring,
            None,
        ),
        "regex": PromptInjectionCheck(mode="regex"),
        "classifier": PromptInjectionCheck(mode="classifier"),
        "hybrid": PromptInjectionCheck(mode="hybrid"),
    }


def score(question: str, context: str, answer: str) -> dict[str, object] | None:
    question = question.strip()
    context = context.strip()
    answer = answer.strip()
    if not question or not context or not answer:
        return None
    runtime = load_models()
    example = RagExample(
        id="demo",
        question=question,
        contexts=[context],
        answer=answer,
        ground_truth=answer,
    )
    return {
        "faith": runtime["faith"].compute(example),  # type: ignore[attr-defined]
        "relevance": runtime["relevance"].compute(example),  # type: ignore[attr-defined]
        "regex": runtime["regex"].check(question),  # type: ignore[attr-defined]
        "classifier": runtime["classifier"].check(question),  # type: ignore[attr-defined]
        "hybrid": runtime["hybrid"].check(question),  # type: ignore[attr-defined]
    }


def _set_example(question: str, context: str, answer: str) -> None:
    st.session_state["question"] = question
    st.session_state["context"] = context
    st.session_state["answer"] = answer
    st.session_state["result"] = None


def main() -> None:
    st.set_page_config(page_title="llmeval", layout="centered")
    st.title("llmeval")
    st.caption(
        "Faithfulness is an NLI score. Relevance is a MiniLM cosine. "
        "The mock judge is a word-overlap scorer, not a neural model."
    )
    if "question" not in st.session_state:
        _set_example(GROUNDED_QUESTION, GROUNDED_CONTEXT, GROUNDED_ANSWER)

    left, middle, right = st.columns(3)
    if left.button("Grounded example", use_container_width=True):
        _set_example(GROUNDED_QUESTION, GROUNDED_CONTEXT, GROUNDED_ANSWER)
    if middle.button("Hallucinated example", use_container_width=True):
        _set_example(GROUNDED_QUESTION, GROUNDED_CONTEXT, HALLUCINATED_ANSWER)
    if right.button("Jailbreak example", use_container_width=True):
        _set_example(JAILBREAK_QUESTION, GROUNDED_CONTEXT, GROUNDED_ANSWER)

    question = st.text_area("Question", key="question", height=100)
    context = st.text_area("Context", key="context", height=140)
    answer = st.text_area("Answer", key="answer", height=80)
    if st.button("Score", type="primary"):
        st.session_state["result"] = score(question, context, answer)

    result = st.session_state.get("result")
    if result is None:
        return
    faith = result["faith"]
    relevance = result["relevance"]
    one, two = st.columns(2)
    one.metric("Faithfulness (NLI baseline)", f"{faith.baseline:.4f}")
    two.metric("Relevance (MiniLM cosine)", f"{relevance.baseline:.4f}")
    st.write(
        f"Mock judge, lexical, not a neural model. "
        f"Faithfulness: {faith.judge}. Relevance: {relevance.judge}."
    )
    st.subheader("Injection check on the question")
    for label, key in (
        ("Regex", "regex"),
        ("Classifier", "classifier"),
        ("Hybrid (regex or classifier)", "hybrid"),
    ):
        verdict = _verdict(result[key])
        if verdict.startswith("block"):
            st.error(f"{label}: {verdict}")
        else:
            st.success(f"{label}: {verdict}")


if __name__ == "__main__":
    main()
