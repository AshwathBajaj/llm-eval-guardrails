import pytest

from llmeval.embeddings import HashingEmbedder
from llmeval.scoring import precision_from_relevance


def test_identical_text_has_cosine_near_one():
    embedder = HashingEmbedder(dim=128)
    text = "A retriever fetches passages for the generator."
    assert embedder.cosine(text, text) == pytest.approx(1.0)


def test_unrelated_text_is_less_similar_than_a_paraphrase_with_shared_words():
    embedder = HashingEmbedder()
    question = "What is a vector index used for?"
    related = "A vector index stores embeddings so search can retrieve related passages."
    unrelated = "Bananas are rich in potassium and grow in tropical climates."
    assert embedder.cosine(question, related) > embedder.cosine(question, unrelated)


def test_empty_text_has_zero_cosine():
    embedder = HashingEmbedder()
    assert embedder.cosine("", "retrieval augmented generation") == 0.0


def test_context_precision_penalizes_a_distractor_ranked_first():
    assert precision_from_relevance([True, False]) == 1.0
    assert precision_from_relevance([False, True]) == 0.5
    assert precision_from_relevance([False, False]) == 0.0
    assert precision_from_relevance([]) == 0.0
