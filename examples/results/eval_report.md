# llmeval report

- Backend: `mock:mock-judge-v1`
- Dataset: `data/sample_rag.jsonl`
- Scoring: `blend(judge=0.50)`
- Examples: 6

Pass/fail uses the blended score unless the config says otherwise.
Hallucination passes when the score is at or below its threshold.
Every other metric passes when the score is at or above its threshold.

## Aggregates

| Metric | Mean | Threshold | Passed | Direction |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.6000 | 2/6 | higher is better |
| answer_relevance | 0.4224 | 0.3500 | 4/6 | higher is better |
| context_precision | 0.6250 | 0.5000 | 4/6 | higher is better |
| context_recall | 0.8333 | 0.5000 | 5/6 | higher is better |
| hallucination | 0.4820 | 0.4500 | 2/6 | lower is better |

## grounded-rag

What is retrieval-augmented generation?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6154 | 1.0000 | 0.2308 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0000 | 0.0000 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## mixed-claim

When was the transformer architecture introduced?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.5000 | 0.5000 | fail |
| answer_relevance | 0.6250 | 1.0000 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4657 | 0.4314 | 0.5000 | fail |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## off-topic-answer

How does cosine similarity measure the closeness of two embeddings?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.0414 | 0.0829 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9369 | 0.8737 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## distractor-first

What is a vector index used for?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5909 | 1.0000 | 0.1818 | pass |
| context_precision | 0.5000 | 0.5000 | 0.5000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0000 | 0.0000 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## missing-context

What two components make up a retrieval-augmented generation system?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.5056 | 0.6111 | 0.4000 | pass |
| context_precision | 0.0000 | 0.0000 | 0.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 1.0000 | 1.0000 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## partial-extra

Why do RAG evaluations report faithfulness?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.5000 | 0.5000 | fail |
| answer_relevance | 0.1562 | 0.2500 | 0.0625 | fail |
| context_precision | 0.2500 | 0.5000 | 0.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4891 | 0.4783 | 0.5000 | fail |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.
