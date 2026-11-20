# llmeval report

- Judge: `mock:mock-judge-v1`
- Baseline: `hashing-256`
- NLI: `none`
- Dataset: `data/sample_rag.jsonl`
- Scoring: `blend(judge=0.50)`
- Examples: 8

- Dataset name: HaluEval QA tiny slice
- Source: https://huggingface.co/datasets/pminervini/HaluEval
- License: Apache-2.0
- Slice: first 4 rows of the qa split, right answer and hallucinated answer

The headline value follows the scoring setting.
When scoring is baseline, that value is the local model.
The judge column is separate.
The mock judge is a lexical scorer, not a neural LLM.
Hallucination passes when the score is at or below its threshold.
Every other metric passes when the score is at or above its threshold.

## Aggregates

| Metric | Mean | Threshold | Passed | Direction |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.3992 | 0.6000 | 0/8 | higher is better |
| answer_relevance | 0.3645 | 0.3500 | 5/8 | higher is better |
| context_precision | 0.8750 | 0.5000 | 8/8 | higher is better |
| context_recall | 0.5000 | 0.5000 | 8/8 | higher is better |
| hallucination | 0.4299 | 0.4500 | 7/8 | lower is better |

## hallucinated (4)

| Metric | Mean | Passed |
| --- | ---: | ---: |
| faithfulness | 0.2985 | 0/4 |
| answer_relevance | 0.5735 | 4/4 |
| context_precision | 0.8750 | 4/4 |
| context_recall | 0.5000 | 4/4 |
| hallucination | 0.4795 | 3/4 |

## right (4)

| Metric | Mean | Passed |
| --- | ---: | ---: |
| faithfulness | 0.5000 | 0/4 |
| answer_relevance | 0.1556 | 1/4 |
| context_precision | 0.8750 | 4/4 |
| context_recall | 0.5000 | 4/4 |
| hallucination | 0.3803 | 4/4 |

## halueval-qa-0000-right

Which magazine was started first Arthur's Magazine or First for Women?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.5280 | 0.6559 | 0.4000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.3413 | 0.6827 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## halueval-qa-0000-hallucinated

Which magazine was started first Arthur's Magazine or First for Women?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.3333 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.6405 | 0.6810 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.3891 | 0.7782 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## halueval-qa-0001-right

The Oberoi family is part of a hotel company that has a head office in what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.0000 | 0.0000 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.4295 | 0.8589 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## halueval-qa-0001-hallucinated

The Oberoi family is part of a hotel company that has a head office in what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.3333 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.4096 | 0.4556 | 0.3636 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.2692 | 0.5383 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## halueval-qa-0002-right

Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.0000 | 0.0000 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.3891 | 0.7782 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## halueval-qa-0002-hallucinated

Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.2273 | 0.0000 | 0.4545 | fail |
| answer_relevance | 0.5104 | 0.5833 | 0.4375 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.8531 | 0.7061 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## halueval-qa-0003-right

What nationality was James Henry Miller's wife?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.0942 | 0.1884 | 0.0000 | fail |
| context_precision | 0.5000 | 0.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.3612 | 0.7224 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.

## halueval-qa-0003-hallucinated

What nationality was James Henry Miller's wife?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.3000 | 0.0000 | 0.6000 | fail |
| answer_relevance | 0.7333 | 0.8000 | 0.6667 | pass |
| context_precision | 0.5000 | 0.0000 | 1.0000 | pass |
| context_recall | 0.5000 | 0.0000 | 1.0000 | pass |
| hallucination | 0.4067 | 0.8135 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: block.
