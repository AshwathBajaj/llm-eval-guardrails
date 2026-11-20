# llmeval report

- Judge: `mock:mock-judge-v1`
- Baseline: `sentence-transformers:sentence-transformers/all-MiniLM-L6-v2`
- NLI: `cross-encoder:cross-encoder/nli-MiniLM2-L6-H768`
- Dataset: `data/halueval_qa_slice.jsonl`
- Scoring: `baseline`
- Examples: 400

- Dataset name: HaluEval QA
- Source: https://huggingface.co/datasets/pminervini/HaluEval
- License: Apache-2.0
- Slice: first 200 rows of the qa split, each emitted with right_answer and with hallucinated_answer (400 examples)

The headline value follows the scoring setting.
When scoring is baseline, that value is the local model.
The judge column is separate.
The mock judge is a lexical scorer, not a neural LLM.
Hallucination passes when the score is at or below its threshold.
Every other metric passes when the score is at or above its threshold.

## Aggregates

| Metric | Mean | Threshold | Passed | Direction |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5212 | 0.5000 | 210/400 | higher is better |
| answer_relevance | 0.4635 | 0.3000 | 249/400 | higher is better |
| context_precision | 0.9350 | 0.5000 | 374/400 | higher is better |
| context_recall | 0.7400 | 0.5000 | 296/400 | higher is better |
| hallucination | 0.4940 | 0.5000 | 209/400 | lower is better |

## hallucinated (200)

| Metric | Mean | Passed |
| --- | ---: | ---: |
| faithfulness | 0.3025 | 62/200 |
| answer_relevance | 0.6850 | 192/200 |
| context_precision | 0.9350 | 187/200 |
| context_recall | 0.7400 | 148/200 |
| hallucination | 0.6907 | 61/200 |

## right (200)

| Metric | Mean | Passed |
| --- | ---: | ---: |
| faithfulness | 0.7400 | 148/200 |
| answer_relevance | 0.2421 | 57/200 |
| context_precision | 0.9350 | 187/200 |
| context_recall | 0.7400 | 148/200 |
| hallucination | 0.2974 | 148/200 |

## halueval-qa-0000-right

Which magazine was started first Arthur's Magazine or First for Women?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.7987 | 0.7987 | 0.4000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8937 | 0.8937 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0000-hallucinated

Which magazine was started first Arthur's Magazine or First for Women?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.5503 | 0.5503 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9893 | 0.9893 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0001-right

The Oberoi family is part of a hotel company that has a head office in what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1750 | 0.1750 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9698 | 0.9698 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0001-hallucinated

The Oberoi family is part of a hotel company that has a head office in what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.8436 | 0.8436 | 0.3636 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9996 | 0.9996 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0002-right

Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1256 | 0.1256 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1210 | 0.1210 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0002-hallucinated

Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4545 | fail |
| answer_relevance | 0.7500 | 0.7500 | 0.4375 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8169 | 0.8169 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0003-right

What nationality was James Henry Miller's wife?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1061 | 0.1061 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0495 | 0.0495 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0003-hallucinated

What nationality was James Henry Miller's wife?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6000 | pass |
| answer_relevance | 0.9217 | 0.9217 | 0.6667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0706 | 0.0706 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0004-right

Cadmium Chloride is slightly soluble in this chemical, it is also called what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1189 | 0.1189 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.7877 | 0.7877 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0004-hallucinated

Cadmium Chloride is slightly soluble in this chemical, it is also called what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6667 | pass |
| answer_relevance | 0.2086 | 0.2086 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.1093 | 0.1093 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0005-right

Which tennis player won more Grand Slam titles, Henri Leconte or Jonathan Stark?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4221 | 0.4221 | 0.2000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0155 | 0.0155 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0005-hallucinated

Which tennis player won more Grand Slam titles, Henri Leconte or Jonathan Stark?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.8308 | 0.8308 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8873 | 0.8873 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0006-right

Which genus of moth in the world's seventh-largest country contains only one species?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4111 | 0.4111 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0898 | 0.0898 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0006-hallucinated

Which genus of moth in the world's seventh-largest country contains only one species?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8750 | pass |
| answer_relevance | 0.6463 | 0.6463 | 0.2143 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0544 | 0.0544 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0007-right

Who was once considered the best kick boxer in the world, however he has been involved in a number of controversies relating to his "unsportsmanlike conducts" in the sport and crimes of violence outside of the ring.

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1077 | 0.1077 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0379 | 0.0379 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0007-hallucinated

Who was once considered the best kick boxer in the world, however he has been involved in a number of controversies relating to his "unsportsmanlike conducts" in the sport and crimes of violence outside of the ring.

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.5414 | 0.5414 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8021 | 0.8021 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0008-right

The Dutch-Belgian television series that "House of Anubis" was based on first aired in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1455 | 0.1455 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0276 | 0.0276 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0008-hallucinated

The Dutch-Belgian television series that "House of Anubis" was based on first aired in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.7154 | 0.7154 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9981 | 0.9981 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0009-right

What is the length of the track where the 2013 Liqui Moly Bathurst 12 Hour was staged?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4330 | 0.4330 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0186 | 0.0186 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0009-hallucinated

What is the length of the track where the 2013 Liqui Moly Bathurst 12 Hour was staged?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8000 | pass |
| answer_relevance | 0.4728 | 0.4728 | 0.0833 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3559 | 0.3559 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0010-right

Fast Cars, Danger, Fire and Knives includes guest appearances from which hip hop record executive?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1579 | 0.1579 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0134 | 0.0134 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0010-hallucinated

Fast Cars, Danger, Fire and Knives includes guest appearances from which hip hop record executive?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.2000 | fail |
| answer_relevance | 0.6139 | 0.6139 | 0.5714 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9962 | 0.9962 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0011-right

Gunmen from Laredo starred which narrator of "Frontier"?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1266 | 0.1266 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1422 | 0.1422 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0011-hallucinated

Gunmen from Laredo starred which narrator of "Frontier"?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3636 | fail |
| answer_relevance | 0.5068 | 0.5068 | 0.1429 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9952 | 0.9952 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0012-right

Where did the form of music played by Die Rhöner Säuwäntzt originate?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0033 | 0.0033 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2844 | 0.2844 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0012-hallucinated

Where did the form of music played by Die Rhöner Säuwäntzt originate?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4444 | fail |
| answer_relevance | 0.9199 | 0.9199 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.5678 | 0.5678 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0013-right

In which American football game was Malcolm Smith named Most Valuable player?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3968 | 0.3968 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0268 | 0.0268 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0013-hallucinated

In which American football game was Malcolm Smith named Most Valuable player?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.7939 | 0.7939 | 0.4545 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9525 | 0.9525 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0014-right

What U.S Highway gives access to Zilpo Road, and is also known as Midland Trail?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.1456 | 0.1456 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.0702 | 0.0702 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0014-hallucinated

What U.S Highway gives access to Zilpo Road, and is also known as Midland Trail?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3333 | fail |
| answer_relevance | 0.8005 | 0.8005 | 0.5556 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.9980 | 0.9980 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0015-right

The 1988 American comedy film, The Great Outdoors, starred a four-time Academy Award nominee, who received a star on the Hollywood Walk of Fame in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0896 | 0.0896 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0283 | 0.0283 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0015-hallucinated

The 1988 American comedy film, The Great Outdoors, starred a four-time Academy Award nominee, who received a star on the Hollywood Walk of Fame in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5206 | 0.5206 | 0.2000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3284 | 0.3284 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0016-right

What are the names of the current members of  American heavy metal band who wrote the music for  Hurt Locker The Musical?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4631 | 0.4631 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0089 | 0.0089 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0016-hallucinated

What are the names of the current members of  American heavy metal band who wrote the music for  Hurt Locker The Musical?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.3990 | 0.3990 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.6877 | 0.6877 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0017-right

Human Error" is the season finale of the third season of a tv show that aired on what network?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2729 | 0.2729 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1469 | 0.1469 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0017-hallucinated

Human Error" is the season finale of the third season of a tv show that aired on what network?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.8298 | 0.8298 | 0.4167 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9971 | 0.9971 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0018-right

Dua Lipa, an English singer, songwriter and model, the album spawned the number-one single "New Rules" is a song by English singer Dua Lipa from her eponymous debut studio album, released in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0862 | 0.0862 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0334 | 0.0334 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0018-hallucinated

Dua Lipa, an English singer, songwriter and model, the album spawned the number-one single "New Rules" is a song by English singer Dua Lipa from her eponymous debut studio album, released in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.2885 | 0.2885 | 0.1000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9997 | 0.9997 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0019-right

American politician Joe Heck ran unsuccessfully against Democrat Catherine Cortez Masto, a woman who previously served as the 32nd Attorney General of where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1411 | 0.1411 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0736 | 0.0736 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0019-hallucinated

American politician Joe Heck ran unsuccessfully against Democrat Catherine Cortez Masto, a woman who previously served as the 32nd Attorney General of where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.5799 | 0.5799 | 0.2778 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9955 | 0.9955 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0020-right

Which state does the drug stores, of which the CEO is Warren Bryant, are located?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2040 | 0.2040 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2458 | 0.2458 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0020-hallucinated

Which state does the drug stores, of which the CEO is Warren Bryant, are located?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7143 | fail |
| answer_relevance | 0.8735 | 0.8735 | 0.7500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9997 | 0.9997 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0021-right

Which  American politician did Donahue replaced

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0852 | 0.0852 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1425 | 0.1425 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0021-hallucinated

Which  American politician did Donahue replaced

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8000 | pass |
| answer_relevance | 0.5404 | 0.5404 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0112 | 0.0112 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0022-right

Which band was founded first, Hole, the rock band that Courtney Love was a frontwoman of, or The Wolfhounds?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.4993 | 0.4993 | 0.1111 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9828 | 0.9828 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0022-hallucinated

Which band was founded first, Hole, the rock band that Courtney Love was a frontwoman of, or The Wolfhounds?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7500 | pass |
| answer_relevance | 0.8335 | 0.8335 | 0.8889 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.4119 | 0.4119 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0023-right

How old is the female main protagonist of Catching Fire?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3846 | 0.3846 | 0.1429 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0193 | 0.0193 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0023-hallucinated

How old is the female main protagonist of Catching Fire?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.3992 | 0.3992 | 0.1111 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.7199 | 0.7199 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0024-right

Chang Ucchin was born in korea during a time that ended with the conclusion of what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1728 | 0.1728 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0574 | 0.0574 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0024-hallucinated

Chang Ucchin was born in korea during a time that ended with the conclusion of what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.7513 | 0.7513 | 0.3750 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8324 | 0.8324 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0025-right

Who is the director of the 2003 film which has scenes in it filmed at the Quality Cafe in Los Angeles?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1725 | 0.1725 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0953 | 0.0953 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0025-hallucinated

Who is the director of the 2003 film which has scenes in it filmed at the Quality Cafe in Los Angeles?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5556 | fail |
| answer_relevance | 0.7778 | 0.7778 | 0.4615 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9852 | 0.9852 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0026-right

New Faces of 1952 is a musical revue with songs and comedy skits, it helped jump start the career of which young performer, and American actress?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1893 | 0.1893 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9933 | 0.9933 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0026-hallucinated

New Faces of 1952 is a musical revue with songs and comedy skits, it helped jump start the career of which young performer, and American actress?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5385 | fail |
| answer_relevance | 0.6916 | 0.6916 | 0.2083 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9923 | 0.9923 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0027-right

Were Pavel Urysohn and Leonid Levin known for the same type of work?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.0131 | 0.0131 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9990 | 0.9990 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0027-hallucinated

Were Pavel Urysohn and Leonid Levin known for the same type of work?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.5714 | pass |
| answer_relevance | 0.7951 | 0.7951 | 0.4000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.1564 | 0.1564 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0028-right

Are both The New Pornographers and Kings of Leon American rock bands?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.1632 | 0.1632 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9996 | 0.9996 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0028-hallucinated

Are both The New Pornographers and Kings of Leon American rock bands?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.9396 | 0.9396 | 0.8750 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9806 | 0.9806 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0029-right

750 7th Avenue and 101 Park Avenue, are located in which city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3210 | 0.3210 | 0.1111 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2179 | 0.2179 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0029-hallucinated

750 7th Avenue and 101 Park Avenue, are located in which city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.7731 | 0.7731 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9954 | 0.9954 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0030-right

Which actress played the part of fictitious character Kimberly Ann Hart, in the franchise built around a live action superhero television series taking much of its footage from the Japanese tokusatsu 'Super Sentai'?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1376 | 0.1376 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4407 | 0.4407 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0030-hallucinated

Which actress played the part of fictitious character Kimberly Ann Hart, in the franchise built around a live action superhero television series taking much of its footage from the Japanese tokusatsu 'Super Sentai'?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5778 | 0.5778 | 0.0800 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0637 | 0.0637 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0031-right

Who was born first, Pablo Trapero or Aleksander Ford?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.5841 | 0.5841 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9605 | 0.9605 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0031-hallucinated

Who was born first, Pablo Trapero or Aleksander Ford?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.8283 | 0.8283 | 0.6667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9736 | 0.9736 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0032-right

Are Jane and First for Women both women's magazines?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.0978 | 0.0978 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9893 | 0.9893 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0032-hallucinated

Are Jane and First for Women both women's magazines?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8127 | 0.8127 | 0.4286 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.6622 | 0.6622 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0033-right

What profession does Nicholas Ray and Elia Kazan have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.3038 | 0.3038 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9384 | 0.9384 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0033-hallucinated

What profession does Nicholas Ray and Elia Kazan have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7143 | pass |
| answer_relevance | 0.8214 | 0.8214 | 0.4000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.1295 | 0.1295 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0034-right

Where is the company that purchased Aixam based in?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1800 | 0.1800 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0243 | 0.0243 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0034-hallucinated

Where is the company that purchased Aixam based in?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.3118 | 0.3118 | 0.1429 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9992 | 0.9992 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0035-right

Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.3694 | 0.3694 | 0.2222 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.7411 | 0.7411 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0035-hallucinated

Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4386 | 0.4386 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.0895 | 0.0895 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0036-right

Who was inducted into the Rock and Roll Hall of Fame, David Lee Roth or Cia Berg?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.6678 | 0.6678 | 0.3000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9701 | 0.9701 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0036-hallucinated

Who was inducted into the Rock and Roll Hall of Fame, David Lee Roth or Cia Berg?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.8514 | 0.8514 | 0.7000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9406 | 0.9406 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0037-right

Zimbabwe's Guwe Secondary School has a sister school in what New York cunty?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1922 | 0.1922 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6460 | 0.6460 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0037-hallucinated

Zimbabwe's Guwe Secondary School has a sister school in what New York cunty?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6000 | fail |
| answer_relevance | 0.3481 | 0.3481 | 0.1667 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9869 | 0.9869 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0038-right

The Royal Commission into Drug Trafficking (1977–1979) or Woodward Royal Commission was a royal commission initiated by the New South Wales Government to investigate drug trafficking in New South Wales, Australia, especially links between the New South Wales Police and Mafia, The Honoured Society, is a Calabrian 'Ndrangheta criminal confederation, started in Melbourne and currently active in all of which country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1885 | 0.1885 | 0.0345 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6084 | 0.6084 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0038-hallucinated

The Royal Commission into Drug Trafficking (1977–1979) or Woodward Royal Commission was a royal commission initiated by the New South Wales Government to investigate drug trafficking in New South Wales, Australia, especially links between the New South Wales Police and Mafia, The Honoured Society, is a Calabrian 'Ndrangheta criminal confederation, started in Melbourne and currently active in all of which country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.9091 | fail |
| answer_relevance | 0.5038 | 0.5038 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9768 | 0.9768 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0039-right

The 337th Flight Test Squadron (337 FLTS) was most recently part of the 46th Test Wing and based at McClellan Air Force Base, a former United States Air Force base located in the North Highlands area of Sacramento County, in which US state?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2018 | 0.2018 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0418 | 0.0418 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0039-hallucinated

The 337th Flight Test Squadron (337 FLTS) was most recently part of the 46th Test Wing and based at McClellan Air Force Base, a former United States Air Force base located in the North Highlands area of Sacramento County, in which US state?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.9444 | pass |
| answer_relevance | 0.9196 | 0.9196 | 0.5926 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0133 | 0.0133 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0040-right

The axial turbojet Pirna 014 was designed by engineers from this German aircraft and aircraft engine manufacturer based in which city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0226 | 0.0226 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0380 | 0.0380 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0040-hallucinated

The axial turbojet Pirna 014 was designed by engineers from this German aircraft and aircraft engine manufacturer based in which city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.6027 | 0.6027 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9768 | 0.9768 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0041-right

Which faith is designated to the University of Providence, private university accredited by the NW association of Schools and Colleges and located in a third largest city in Montana after being passed by Missoula?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3233 | 0.3233 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0629 | 0.0629 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0041-hallucinated

Which faith is designated to the University of Providence, private university accredited by the NW association of Schools and Colleges and located in a third largest city in Montana after being passed by Missoula?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.7074 | 0.7074 | 0.1765 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9989 | 0.9989 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0042-right

Pauline Henry was known as the vocalist of a very popular cover song. Which album was this song from?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | -0.0229 | -0.0229 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0423 | 0.0423 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0042-hallucinated

Pauline Henry was known as the vocalist of a very popular cover song. Which album was this song from?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7143 | fail |
| answer_relevance | 0.3484 | 0.3484 | 0.0714 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9981 | 0.9981 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0043-right

Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2571 | 0.2571 | 0.1000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.7893 | 0.7893 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0043-hallucinated

Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.2857 | fail |
| answer_relevance | 0.9000 | 0.9000 | 0.6000 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9987 | 0.9987 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0044-right

What American country music singer-songwriter, born in May of 1942, sang a duet with her ex-husband the same year that he released the song "The Battle?"

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2883 | 0.2883 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0474 | 0.0474 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0044-hallucinated

What American country music singer-songwriter, born in May of 1942, sang a duet with her ex-husband the same year that he released the song "The Battle?"

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8333 | pass |
| answer_relevance | 0.5276 | 0.5276 | 0.2273 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0136 | 0.0136 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0045-right

Who was born first, Francis Nethersole or Elizabeth Stuart?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.6772 | 0.6772 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.5834 | 0.5834 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0045-hallucinated

Who was born first, Francis Nethersole or Elizabeth Stuart?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8336 | 0.8336 | 0.6667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9890 | 0.9890 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0046-right

What does the Hacker-Pschorr Brewery have to limit in order to comply with German regulations?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3102 | 0.3102 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1101 | 0.1101 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0046-hallucinated

What does the Hacker-Pschorr Brewery have to limit in order to comply with German regulations?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7143 | pass |
| answer_relevance | 0.7664 | 0.7664 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0830 | 0.0830 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0047-right

Don Barry Mason was the founder of the Psychedelic Shamanistic Institute (PSI), which other member that's Welsh, that died on 10 April 2016?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2273 | 0.2273 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2849 | 0.2849 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0047-hallucinated

Don Barry Mason was the founder of the Psychedelic Shamanistic Institute (PSI), which other member that's Welsh, that died on 10 April 2016?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.5913 | 0.5913 | 0.2143 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9967 | 0.9967 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0048-right

What male actor starred in The Messenger?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2241 | 0.2241 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1950 | 0.1950 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0048-hallucinated

What male actor starred in The Messenger?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.7479 | 0.7479 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9996 | 0.9996 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0049-right

Are Gin and tonic and Paloma both cocktails based on tequila?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.0282 | 0.0282 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9990 | 0.9990 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0049-hallucinated

Are Gin and tonic and Paloma both cocktails based on tequila?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8333 | pass |
| answer_relevance | 0.9427 | 0.9427 | 1.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.4368 | 0.4368 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0050-right

Who is older Glenn Hughes or Ross Lynch?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.6926 | 0.6926 | 0.4000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6487 | 0.6487 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0050-hallucinated

Who is older Glenn Hughes or Ross Lynch?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.7653 | 0.7653 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6035 | 0.6035 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0051-right

In what year was the creator of the current arrangement of the "Simpson's Theme" born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1353 | 0.1353 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0604 | 0.0604 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0051-hallucinated

In what year was the creator of the current arrangement of the "Simpson's Theme" born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7143 | pass |
| answer_relevance | 0.9493 | 0.9493 | 0.7500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0312 | 0.0312 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0052-right

The Southern Railway runs from Vienna to Graz and the border with Slovenia at Spielfeld via the first mountain railway built in Europe to use what kind of track?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.3972 | 0.3972 | 0.0625 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.5382 | 0.5382 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0052-hallucinated

The Southern Railway runs from Vienna to Graz and the border with Slovenia at Spielfeld via the first mountain railway built in Europe to use what kind of track?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.5848 | 0.5848 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9785 | 0.9785 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0053-right

In what show did Cynthia Nixon receive the 2004 Primetime Emmy Award for Outstanding Supporting Actress in a Comedy Series and a Screen Actors Guild Award for her performance?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1524 | 0.1524 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0427 | 0.0427 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0053-hallucinated

In what show did Cynthia Nixon receive the 2004 Primetime Emmy Award for Outstanding Supporting Actress in a Comedy Series and a Screen Actors Guild Award for her performance?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4286 | fail |
| answer_relevance | 0.7096 | 0.7096 | 0.1429 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9935 | 0.9935 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0054-right

Lee Jun-fan played what character in "The Green Hornet" television series?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2977 | 0.2977 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0418 | 0.0418 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0054-hallucinated

Lee Jun-fan played what character in "The Green Hornet" television series?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7778 | pass |
| answer_relevance | 0.8055 | 0.8055 | 0.6364 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4197 | 0.4197 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0055-right

The 1895/96 Football League season was the eighth in Football League history with Everton, their Goodison Park home, is a football stadium located in Walton, Liverpool, in which country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2182 | 0.2182 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6861 | 0.6861 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0055-hallucinated

The 1895/96 Football League season was the eighth in Football League history with Everton, their Goodison Park home, is a football stadium located in Walton, Liverpool, in which country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7273 | fail |
| answer_relevance | 0.8681 | 0.8681 | 0.5294 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9565 | 0.9565 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0056-right

A Head Full of Dreams Tour is the seventh tour by Coldplay, and which had it's first show at a stadium that is known as Estadio Unico and is owned by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1063 | 0.1063 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0114 | 0.0114 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0056-hallucinated

A Head Full of Dreams Tour is the seventh tour by Coldplay, and which had it's first show at a stadium that is known as Estadio Unico and is owned by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7333 | fail |
| answer_relevance | 0.7673 | 0.7673 | 0.4500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9970 | 0.9970 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0057-right

Roger Avary (born August 23, 1965) is a Canadian film and television producer, screenwriter and director in the American mass media industry, he wrote the screenplay for Beowulf, a 2007 British-American 3D motion capture epic fantasy film, directed by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2013 | 0.2013 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0159 | 0.0159 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0057-hallucinated

Roger Avary (born August 23, 1965) is a Canadian film and television producer, screenwriter and director in the American mass media industry, he wrote the screenplay for Beowulf, a 2007 British-American 3D motion capture epic fantasy film, directed by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.6506 | 0.6506 | 0.0741 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.6243 | 0.6243 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0058-right

The American Pre-Code comedy film featuring an American actress, dancer, and singer, widely known for performing in films and RKO's musical films, was released in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2206 | 0.2206 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0241 | 0.0241 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0058-hallucinated

The American Pre-Code comedy film featuring an American actress, dancer, and singer, widely known for performing in films and RKO's musical films, was released in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3333 | fail |
| answer_relevance | 0.3822 | 0.3822 | 0.1111 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9983 | 0.9983 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0059-right

An edited version of "Just the Two of Us" reached number two on the "Billboard" Hot 100 behind a song written and composed by Donna Weiss and Jackie DeShannon which spend how many weeks at No. 1 on the "Billboard" hot 100?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2345 | 0.2345 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8822 | 0.8822 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0059-hallucinated

An edited version of "Just the Two of Us" reached number two on the "Billboard" Hot 100 behind a song written and composed by Donna Weiss and Jackie DeShannon which spend how many weeks at No. 1 on the "Billboard" hot 100?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.5000 | 0.8333 | pass |
| answer_relevance | 0.7857 | 0.7857 | 0.2727 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.4985 | 0.4985 | 0.0000 | pass |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0060-right

Which band has more members, Saint Motel or Curve?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5766 | 0.5766 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0450 | 0.0450 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0060-hallucinated

Which band has more members, Saint Motel or Curve?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3333 | fail |
| answer_relevance | 0.4365 | 0.4365 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9997 | 0.9997 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0061-right

"Funnybot" is the second episode of the fifteenth season of which American animated television series, created by Trey Parker and Matt Stone?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.3214 | 0.3214 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9883 | 0.9883 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0061-hallucinated

"Funnybot" is the second episode of the fifteenth season of which American animated television series, created by Trey Parker and Matt Stone?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.7165 | 0.7165 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9993 | 0.9993 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0062-right

Which private research university is located in Chestnut Hill, Massachusetts Boston College or Stanford University?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.6222 | 0.6222 | 0.2000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9925 | 0.9925 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0062-hallucinated

Which private research university is located in Chestnut Hill, Massachusetts Boston College or Stanford University?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6667 | pass |
| answer_relevance | 0.7374 | 0.7374 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.1043 | 0.1043 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0063-right

What American stage, film, and television actor  who also appeared in a large number of musicals, played Samson in the 1949 film "Samson and Delilah".

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1494 | 0.1494 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4631 | 0.4631 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0063-hallucinated

What American stage, film, and television actor  who also appeared in a large number of musicals, played Samson in the 1949 film "Samson and Delilah".

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.8423 | 0.8423 | 0.3529 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9991 | 0.9991 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0064-right

Iqaluit Airport and Canadian North are based out of what country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4007 | 0.4007 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0529 | 0.0529 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0064-hallucinated

Iqaluit Airport and Canadian North are based out of what country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6000 | pass |
| answer_relevance | 0.6283 | 0.6283 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0675 | 0.0675 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0065-right

In what political party was the man who officially opened he Royal Spa Centre in 1972?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1574 | 0.1574 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1303 | 0.1303 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0065-hallucinated

In what political party was the man who officially opened he Royal Spa Centre in 1972?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5556 | fail |
| answer_relevance | 0.9095 | 0.9095 | 0.6364 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9986 | 0.9986 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0066-right

Which Oscar-nominated film was written by the screenwriter who wrote a 1991 romantic drama based upon a screenplay by Sooni Taraporevala?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1507 | 0.1507 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9074 | 0.9074 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0066-hallucinated

Which Oscar-nominated film was written by the screenwriter who wrote a 1991 romantic drama based upon a screenplay by Sooni Taraporevala?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | -0.0252 | -0.0252 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9931 | 0.9931 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0067-right

Are both Tim McIlrath and Spike Slawson American punk rock musicians?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.2043 | 0.2043 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9567 | 0.9567 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0067-hallucinated

Are both Tim McIlrath and Spike Slawson American punk rock musicians?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7273 | fail |
| answer_relevance | 0.9159 | 0.9159 | 0.7273 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9882 | 0.9882 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0068-right

The Golden Globe Award winner for best actor from "Roseanne" starred along what actress in Gigantic?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2326 | 0.2326 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3109 | 0.3109 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0068-hallucinated

The Golden Globe Award winner for best actor from "Roseanne" starred along what actress in Gigantic?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7500 | pass |
| answer_relevance | 0.4808 | 0.4808 | 0.1538 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0627 | 0.0627 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0069-right

The expert mentor to the celebrities that perform on "Splash!" won the 2009 FINA World Championionship in the individual event at what age?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.2479 | 0.2479 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.2041 | 0.2041 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0069-hallucinated

The expert mentor to the celebrities that perform on "Splash!" won the 2009 FINA World Championionship in the individual event at what age?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8462 | fail |
| answer_relevance | 0.9680 | 0.9680 | 1.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.9952 | 0.9952 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0070-right

Still Da Baddest is the fourth studio album by American rapper Trina, following the poor chart performance, "I Got a Thang for You" featuring which American singer/songwriter, record producer, business woman, and television personality, and was born in Oakland, California?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2366 | 0.2366 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0687 | 0.0687 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0070-hallucinated

Still Da Baddest is the fourth studio album by American rapper Trina, following the poor chart performance, "I Got a Thang for You" featuring which American singer/songwriter, record producer, business woman, and television personality, and was born in Oakland, California?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.5191 | 0.5191 | 0.0714 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9988 | 0.9988 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0071-right

What profession does Am Rong and Alexandre Rockwell have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3560 | 0.3560 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1206 | 0.1206 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0071-hallucinated

What profession does Am Rong and Alexandre Rockwell have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.2500 | fail |
| answer_relevance | 0.8306 | 0.8306 | 0.6667 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9717 | 0.9717 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0072-right

El Nuevo Cojo and Golf Magazine are both special interest publications but which one is owned by Time Inc?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5928 | 0.5928 | 0.1667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0271 | 0.0271 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0072-hallucinated

El Nuevo Cojo and Golf Magazine are both special interest publications but which one is owned by Time Inc?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6593 | 0.6593 | 0.3846 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1711 | 0.1711 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0073-right

Who funds the bowling team that includes the school bus driver for Springfield Elementary School?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.5000 | pass |
| answer_relevance | 0.1485 | 0.1485 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.5000 | pass |
| hallucination | 0.0925 | 0.0925 | 0.5000 | pass |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0073-hallucinated

Who funds the bowling team that includes the school bus driver for Springfield Elementary School?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.5412 | 0.5412 | 0.1818 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.5000 | pass |
| hallucination | 0.9787 | 0.9787 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0074-right

What city are George Washington University Hospital and MedStar Washington Hospital Center located in?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5453 | 0.5453 | 0.1250 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0202 | 0.0202 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0074-hallucinated

What city are George Washington University Hospital and MedStar Washington Hospital Center located in?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7778 | fail |
| answer_relevance | 0.9473 | 0.9473 | 0.7000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9978 | 0.9978 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0075-right

what is the connection between Peter O'Meara and Norman Dike?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1703 | 0.1703 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0326 | 0.0326 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0075-hallucinated

what is the connection between Peter O'Meara and Norman Dike?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.7995 | 0.7995 | 0.5714 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9246 | 0.9246 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0076-right

What author has contributed to such works as "New Statesmen", "The Nation", and "The Atlantic", among others, while also being being associated with Dysteleology?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2219 | 0.2219 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2809 | 0.2809 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0076-hallucinated

What author has contributed to such works as "New Statesmen", "The Nation", and "The Atlantic", among others, while also being being associated with Dysteleology?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.5000 | pass |
| answer_relevance | 0.2738 | 0.2738 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0761 | 0.0761 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0077-right

Who developed the prototype pacemaker used by the 34th President of the USA?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1124 | 0.1124 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0178 | 0.0178 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0077-hallucinated

Who developed the prototype pacemaker used by the 34th President of the USA?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.3060 | 0.3060 | 0.0769 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9933 | 0.9933 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0078-right

Which publishing company has published Bizarre and a sister publication devoted to the anomalous phenomena popularised by Charles Fort?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3735 | 0.3735 | 0.0714 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0887 | 0.0887 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0078-hallucinated

Which publishing company has published Bizarre and a sister publication devoted to the anomalous phenomena popularised by Charles Fort?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.9286 | pass |
| answer_relevance | 0.8921 | 0.8921 | 0.8000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0668 | 0.0668 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0079-right

Who performed the lead single on the album Friends in Low Places, No Fences, that reached #1 on Billboard?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3024 | 0.3024 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0182 | 0.0182 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0079-hallucinated

Who performed the lead single on the album Friends in Low Places, No Fences, that reached #1 on Billboard?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6913 | 0.6913 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0072 | 0.0072 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0080-right

Hate to Feel is the tenth track on what Alice in Chains' album that peaked as number six on the Billboard 200?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1173 | 0.1173 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1733 | 0.1733 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0080-hallucinated

Hate to Feel is the tenth track on what Alice in Chains' album that peaked as number six on the Billboard 200?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8217 | 0.8217 | 0.2941 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9259 | 0.9259 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0081-right

The lead singer and guitarist in the Portland, Oregon rock band consisting of John Gourley, Zach Carothers, Kyle O'Quin, Jason Sechrist and Eric Howk, goes by what alias?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1975 | 0.1975 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4468 | 0.4468 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0081-hallucinated

The lead singer and guitarist in the Portland, Oregon rock band consisting of John Gourley, Zach Carothers, Kyle O'Quin, Jason Sechrist and Eric Howk, goes by what alias?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3333 | fail |
| answer_relevance | 0.3569 | 0.3569 | 0.0455 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9967 | 0.9967 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0082-right

What year was the winner of the 2016 Marrakesh ePrix born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2974 | 0.2974 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2859 | 0.2859 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0082-hallucinated

What year was the winner of the 2016 Marrakesh ePrix born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3362 | 0.3362 | 0.1111 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0114 | 0.0114 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0083-right

South Korean actor Kim Yool-ho starred in what 2016 movie directed by Yeon Sang-ho Yeon Sang-ho and starring actors Gong Yoo, Jung Yu-mi, and Ma Dong-seok?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2308 | 0.2308 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1795 | 0.1795 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0083-hallucinated

South Korean actor Kim Yool-ho starred in what 2016 movie directed by Yeon Sang-ho Yeon Sang-ho and starring actors Gong Yoo, Jung Yu-mi, and Ma Dong-seok?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7222 | fail |
| answer_relevance | 0.8495 | 0.8495 | 0.6364 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.7985 | 0.7985 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0084-right

According to the 2006 census what is the population of the city in which James Iroha Uchechukwu was born ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0297 | 0.0297 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0257 | 0.0257 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0084-hallucinated

According to the 2006 census what is the population of the city in which James Iroha Uchechukwu was born ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3333 | fail |
| answer_relevance | 0.9081 | 0.9081 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.7128 | 0.7128 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0085-right

What actor in the film D.C. Cab also had a role in the TV series Barney Miller?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1220 | 0.1220 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0200 | 0.0200 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0085-hallucinated

What actor in the film D.C. Cab also had a role in the TV series Barney Miller?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.6098 | 0.6098 | 0.2000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8472 | 0.8472 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0086-right

Which industry do Richard Hawley and Chicago's Catherine belong to?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.0691 | 0.0691 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.7519 | 0.7519 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0086-hallucinated

Which industry do Richard Hawley and Chicago's Catherine belong to?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.6184 | 0.6184 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9997 | 0.9997 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0087-right

Are Pam Veasey and Jon Jost both American?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.1288 | 0.1288 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9983 | 0.9983 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0087-hallucinated

Are Pam Veasey and Jon Jost both American?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5714 | fail |
| answer_relevance | 0.8518 | 0.8518 | 0.7143 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9815 | 0.9815 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0088-right

Maurice Hines and his brother were famous for what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6690 | 0.6690 | 0.1667 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0486 | 0.0486 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0088-hallucinated

Maurice Hines and his brother were famous for what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4286 | fail |
| answer_relevance | 0.9199 | 0.9199 | 0.5714 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9909 | 0.9909 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0089-right

Are the New Orleans Outfall Canals the same length as the Augusta Canal?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.1018 | 0.1018 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.4859 | 0.4859 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0089-hallucinated

Are the New Orleans Outfall Canals the same length as the Augusta Canal?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.8008 | 0.8008 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.9964 | 0.9964 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0090-right

In which stadium do the teams owned by Myra Kraft's husband play?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4076 | 0.4076 | 0.1250 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0190 | 0.0190 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0090-hallucinated

In which stadium do the teams owned by Myra Kraft's husband play?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6667 | pass |
| answer_relevance | 0.8286 | 0.8286 | 0.6250 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1790 | 0.1790 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0091-right

What southern California based band covered Blue Öyster Cult's Godzilla?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1588 | 0.1588 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9674 | 0.9674 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0091-hallucinated

What southern California based band covered Blue Öyster Cult's Godzilla?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4286 | fail |
| answer_relevance | 0.7267 | 0.7267 | 0.4545 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9974 | 0.9974 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0092-right

The Swedish-British entertainment studio executive and film executive producer, who was the Executive producer for a 2016 American action thriller film directed by Babak Najafi, currently serve?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2376 | 0.2376 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0335 | 0.0335 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0092-hallucinated

The Swedish-British entertainment studio executive and film executive producer, who was the Executive producer for a 2016 American action thriller film directed by Babak Najafi, currently serve?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6000 | fail |
| answer_relevance | 0.5093 | 0.5093 | 0.1818 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9432 | 0.9432 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0093-right

an Emmy Award winner and two-time Tony Award winner, was on the episode 15 of the third season of "Chuck". what is her name ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1260 | 0.1260 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3331 | 0.3331 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0093-hallucinated

an Emmy Award winner and two-time Tony Award winner, was on the episode 15 of the third season of "Chuck". what is her name ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4444 | fail |
| answer_relevance | 0.7371 | 0.7371 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9974 | 0.9974 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0094-right

What is the current name of the Atlanta Mansion built for the daughter of the 41st Mayor of Atlanta, Georgia?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2116 | 0.2116 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.7015 | 0.7015 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0094-hallucinated

What is the current name of the Atlanta Mansion built for the daughter of the 41st Mayor of Atlanta, Georgia?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.5818 | 0.5818 | 0.1538 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9950 | 0.9950 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0095-right

Who invented the type of script used in autographs?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1078 | 0.1078 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0263 | 0.0263 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0095-hallucinated

Who invented the type of script used in autographs?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.4347 | 0.4347 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9973 | 0.9973 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0096-right

Approximately what percentage of the global population is made up of the ethnic group Princess Fragrant was produced to improve relations with?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.1958 | 0.1958 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.4096 | 0.4096 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0096-hallucinated

Approximately what percentage of the global population is made up of the ethnic group Princess Fragrant was produced to improve relations with?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.2911 | 0.2911 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.2986 | 0.2986 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0097-right

The Boren-McCurdy proposals were partially brought about by which Oklahoma politician in 1992?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3312 | 0.3312 | 0.1000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0344 | 0.0344 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0097-hallucinated

The Boren-McCurdy proposals were partially brought about by which Oklahoma politician in 1992?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5714 | fail |
| answer_relevance | 0.5052 | 0.5052 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9987 | 0.9987 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0098-right

The Thoen Stone is on display at a museum in what county?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3056 | 0.3056 | 0.1667 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1609 | 0.1609 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0098-hallucinated

The Thoen Stone is on display at a museum in what county?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.7930 | 0.7930 | 0.2500 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9938 | 0.9938 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0099-right

Is Children's National Medical Center or MedStar Washington Hospital Center the largest private hospital in Washington, D.C.?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.7562 | 0.7562 | 0.4444 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0178 | 0.0178 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0099-hallucinated

Is Children's National Medical Center or MedStar Washington Hospital Center the largest private hospital in Washington, D.C.?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.7610 | 0.7610 | 0.4545 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0419 | 0.0419 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0100-right

Prince William, Duke of Gloucester and Prince George of Denmark, were eventually monarchs of which Kingdom?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2216 | 0.2216 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.5846 | 0.5846 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0100-hallucinated

Prince William, Duke of Gloucester and Prince George of Denmark, were eventually monarchs of which Kingdom?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.6737 | 0.6737 | 0.7000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9993 | 0.9993 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0101-right

The airline operating in Whitehorse, Yukon handled how many passengers in 2012?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1815 | 0.1815 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0257 | 0.0257 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0101-hallucinated

The airline operating in Whitehorse, Yukon handled how many passengers in 2012?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7143 | pass |
| answer_relevance | 0.4959 | 0.4959 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3032 | 0.3032 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0102-right

What State has a Disney Resort & Spa that is a beachside hotel, resort and vacation destination offering complimentary children's activities and programs and that Djuan Rivers was a General Manager at?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4733 | 0.4733 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0629 | 0.0629 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0102-hallucinated

What State has a Disney Resort & Spa that is a beachside hotel, resort and vacation destination offering complimentary children's activities and programs and that Djuan Rivers was a General Manager at?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.5184 | 0.5184 | 0.2105 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9890 | 0.9890 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0103-right

Are Wenling and Xinzheng both in China?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.0924 | 0.0924 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9900 | 0.9900 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0103-hallucinated

Are Wenling and Xinzheng both in China?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.5000 | 0.7500 | pass |
| answer_relevance | 0.9145 | 0.9145 | 0.7500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.5149 | 0.5149 | 0.0000 | fail |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0104-right

What is the birth date of the coach of the 2014-15 Michigan Wolverines men's basketball team?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2620 | 0.2620 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0957 | 0.0957 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0104-hallucinated

What is the birth date of the coach of the 2014-15 Michigan Wolverines men's basketball team?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8000 | fail |
| answer_relevance | 0.8585 | 0.8585 | 0.5833 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.6405 | 0.6405 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0105-right

Which organization presents the award in which Chris Noonan was nominated for his work in "Babe?"

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2013 | 0.2013 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0478 | 0.0478 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0105-hallucinated

Which organization presents the award in which Chris Noonan was nominated for his work in "Babe?"

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.9160 | 0.9160 | 0.5455 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9973 | 0.9973 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0106-right

Where is the base of one of the three main British intelligence agencies?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1724 | 0.1724 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1632 | 0.1632 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0106-hallucinated

Where is the base of one of the three main British intelligence agencies?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6250 | pass |
| answer_relevance | 0.7079 | 0.7079 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0182 | 0.0182 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0107-right

When a Man Falls in Love, is a 2013 South Korean television series, starring Song Seung-heon, Shin Se-kyung, Chae Jung-an, and which South Korean actor, born on ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0641 | 0.0641 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0687 | 0.0687 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0107-hallucinated

When a Man Falls in Love, is a 2013 South Korean television series, starring Song Seung-heon, Shin Se-kyung, Chae Jung-an, and which South Korean actor, born on ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8462 | pass |
| answer_relevance | 0.6930 | 0.6930 | 0.2917 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0718 | 0.0718 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0108-right

What retailer is the second-largest in the United States and has a commercial featuring the American artist who was 1st runner-up in the 2005 USA Weekend Magazine's songwriting competition?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3911 | 0.3911 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0908 | 0.0908 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0108-hallucinated

What retailer is the second-largest in the United States and has a commercial featuring the American artist who was 1st runner-up in the 2005 USA Weekend Magazine's songwriting competition?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8889 | fail |
| answer_relevance | 0.7337 | 0.7337 | 0.8000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9533 | 0.9533 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0109-right

Which English actor of stage, film and television from the 1978 BBC drama "Pennies From Heaven" appeared in the 2006 BBC Four television play "Kenneth Williams: Fantabulosa!?"

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0467 | 0.0467 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0168 | 0.0168 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0109-hallucinated

Which English actor of stage, film and television from the 1978 BBC drama "Pennies From Heaven" appeared in the 2006 BBC Four television play "Kenneth Williams: Fantabulosa!?"

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8301 | 0.8301 | 0.3158 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9997 | 0.9997 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0110-right

Who hosted both Miss USA 1968 and The Price Is Right?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2344 | 0.2344 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0200 | 0.0200 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0110-hallucinated

Who hosted both Miss USA 1968 and The Price Is Right?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6277 | 0.6277 | 0.4000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0356 | 0.0356 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0111-right

What video game published by Sierra Entertainment includes an antagonist figure who's mystery is the core of the series?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.0476 | 0.0476 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.0235 | 0.0235 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0111-hallucinated

What video game published by Sierra Entertainment includes an antagonist figure who's mystery is the core of the series?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1651 | 0.1651 | 0.0769 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.6737 | 0.6737 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0112-right

Close to the Enemy starred the English actor known as Ash Morgan in what BBC series?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1057 | 0.1057 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8775 | 0.8775 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0112-hallucinated

Close to the Enemy starred the English actor known as Ash Morgan in what BBC series?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.5212 | 0.5212 | 0.4667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9745 | 0.9745 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0113-right

The Bass Rock Lighthouse was next to what Castle?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4189 | 0.4189 | 0.1667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4106 | 0.4106 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0113-hallucinated

The Bass Rock Lighthouse was next to what Castle?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.8627 | 0.8627 | 0.8333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9940 | 0.9940 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0114-right

Gülhane Park and Zografeion Lyceum, are located in which country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0973 | 0.0973 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2253 | 0.2253 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0114-hallucinated

Gülhane Park and Zografeion Lyceum, are located in which country?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.9367 | 0.9367 | 0.7143 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9860 | 0.9860 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0115-right

What is the name of the movie in which Edwin Brown plays a man that executed at least 400 people, including William Joyce and John Amery?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1254 | 0.1254 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0969 | 0.0969 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0115-hallucinated

What is the name of the movie in which Edwin Brown plays a man that executed at least 400 people, including William Joyce and John Amery?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.4440 | 0.4440 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9580 | 0.9580 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0116-right

What genre of music is the solo artist that contributed to Real Damage a variant of?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4151 | 0.4151 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2946 | 0.2946 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0116-hallucinated

What genre of music is the solo artist that contributed to Real Damage a variant of?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8639 | 0.8639 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8054 | 0.8054 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0117-right

Jake David Shapiro was best know for being the screenwriter of a film directed by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1723 | 0.1723 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0183 | 0.0183 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0117-hallucinated

Jake David Shapiro was best know for being the screenwriter of a film directed by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6000 | fail |
| answer_relevance | 0.9096 | 0.9096 | 0.6364 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9968 | 0.9968 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0118-right

What book contains a poem which, along with "Beowulf" and the "Anglo-Saxon Chronicle", preserves a legendary list of the kings of the Angles?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3409 | 0.3409 | 0.0714 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0218 | 0.0218 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0118-hallucinated

What book contains a poem which, along with "Beowulf" and the "Anglo-Saxon Chronicle", preserves a legendary list of the kings of the Angles?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.4507 | 0.4507 | 0.2143 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9972 | 0.9972 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0119-right

Norbert Holm was arrested and later demoted because of his Chief of Operations association with a military theorist popularly known as what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0279 | 0.0279 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0320 | 0.0320 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0119-hallucinated

Norbert Holm was arrested and later demoted because of his Chief of Operations association with a military theorist popularly known as what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.9000 | pass |
| answer_relevance | 0.9308 | 0.9308 | 0.6923 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2839 | 0.2839 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0120-right

What state does Sang-Wook Cheong work as a materials scientist?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2778 | 0.2778 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1303 | 0.1303 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0120-hallucinated

What state does Sang-Wook Cheong work as a materials scientist?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7143 | fail |
| answer_relevance | 0.8804 | 0.8804 | 0.5556 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9981 | 0.9981 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0121-right

What type of vegetation does Kniphofia and Baptisia have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3954 | 0.3954 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0198 | 0.0198 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0121-hallucinated

What type of vegetation does Kniphofia and Baptisia have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.8053 | 0.8053 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9278 | 0.9278 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0122-right

Californian rock band Lit recorded A Place in the Sun in 1995, but what's their best known song?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0756 | 0.0756 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0449 | 0.0449 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0122-hallucinated

Californian rock band Lit recorded A Place in the Sun in 1995, but what's their best known song?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3333 | fail |
| answer_relevance | 0.5555 | 0.5555 | 0.0588 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9989 | 0.9989 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0123-right

Gary Harrison, began his career in the 1970s and has written over how many major-label recorded songs including several number-one hits, another artist who have recorded his work include Bryan White, an American country music artist?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.0309 | 0.0309 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9893 | 0.9893 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0123-hallucinated

Gary Harrison, began his career in the 1970s and has written over how many major-label recorded songs including several number-one hits, another artist who have recorded his work include Bryan White, an American country music artist?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7778 | pass |
| answer_relevance | 0.7609 | 0.7609 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.3567 | 0.3567 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0124-right

The 1976 German Grand Prix was won by a driver who retired in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2698 | 0.2698 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0217 | 0.0217 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0124-hallucinated

The 1976 German Grand Prix was won by a driver who retired in what year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.2500 | fail |
| answer_relevance | 0.9531 | 0.9531 | 0.7778 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9933 | 0.9933 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0125-right

What event at the Asian Junior Athletics Championships has men and women competing at the same time?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2273 | 0.2273 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0354 | 0.0354 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0125-hallucinated

What event at the Asian Junior Athletics Championships has men and women competing at the same time?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.4000 | pass |
| answer_relevance | 0.7138 | 0.7138 | 0.1538 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0630 | 0.0630 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0126-right

Which 1999 French Open - Women's Doubles runner-up was born in Russia on 7 June 1981?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3204 | 0.3204 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1597 | 0.1597 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0126-hallucinated

Which 1999 French Open - Women's Doubles runner-up was born in Russia on 7 June 1981?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.4096 | 0.4096 | 0.0833 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8217 | 0.8217 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0127-right

What is the length of the River which has Wild Horse Creek as a tributary ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2747 | 0.2747 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0464 | 0.0464 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0127-hallucinated

What is the length of the River which has Wild Horse Creek as a tributary ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7143 | pass |
| answer_relevance | 0.8249 | 0.8249 | 0.4000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2327 | 0.2327 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0128-right

Are Manhattan West and Singer Building both projects in New York?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.1590 | 0.1590 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.5402 | 0.5402 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0128-hallucinated

Are Manhattan West and Singer Building both projects in New York?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.7296 | 0.7296 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.2822 | 0.2822 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0129-right

Who is the American internet entrepreneur who founded the company featured on 24 Hours on Craigslist?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.4431 | 0.4431 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6030 | 0.6030 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0129-hallucinated

Who is the American internet entrepreneur who founded the company featured on 24 Hours on Craigslist?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.7029 | 0.7029 | 0.0909 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9980 | 0.9980 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0130-right

Between two tennis players Kim Clijsters and Mary Pierce, who is older?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.5274 | 0.5274 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9933 | 0.9933 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0130-hallucinated

Between two tennis players Kim Clijsters and Mary Pierce, who is older?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.5000 | pass |
| answer_relevance | 0.6703 | 0.6703 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.3005 | 0.3005 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0131-right

Which American college that has sent students to Centre for Medieval and Renaissance Studies was founded in 1874?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.5000 | pass |
| answer_relevance | 0.4502 | 0.4502 | 0.0833 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.5000 | pass |
| hallucination | 0.0382 | 0.0382 | 0.5000 | pass |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0131-hallucinated

Which American college that has sent students to Centre for Medieval and Renaissance Studies was founded in 1874?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5577 | 0.5577 | 0.2308 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.5000 | pass |
| hallucination | 0.1354 | 0.1354 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0132-right

Hot Coffee, Mississippi sometimes shares a zipcode with a nearby city with what population at the 2010 census?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0763 | 0.0763 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0142 | 0.0142 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0132-hallucinated

Hot Coffee, Mississippi sometimes shares a zipcode with a nearby city with what population at the 2010 census?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.4019 | 0.4019 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.6705 | 0.6705 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0133-right

Jo Ann Terry won the 80m hurdles event at what Sao Paulo-based event from 1963?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.0295 | 0.0295 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6300 | 0.6300 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0133-hallucinated

Jo Ann Terry won the 80m hurdles event at what Sao Paulo-based event from 1963?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6364 | fail |
| answer_relevance | 0.8969 | 0.8969 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9219 | 0.9219 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0134-right

Pearl Lowe and Alison Goldfrapp, is of which nationality?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.0959 | 0.0959 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9057 | 0.9057 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0134-hallucinated

Pearl Lowe and Alison Goldfrapp, is of which nationality?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.9287 | 0.9287 | 0.8333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9586 | 0.9586 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0135-right

Which British company whose majority of its business interests are in Asia was related to the London Based Trading house Matheson & Company?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2230 | 0.2230 | 0.0714 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8217 | 0.8217 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0135-hallucinated

Which British company whose majority of its business interests are in Asia was related to the London Based Trading house Matheson & Company?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.4976 | 0.4976 | 0.1333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8796 | 0.8796 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0136-right

What man, also known as mi Sde-Or, created a military self-defense system developed for the Israel Defense Forces?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2457 | 0.2457 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3195 | 0.3195 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0136-hallucinated

What man, also known as mi Sde-Or, created a military self-defense system developed for the Israel Defense Forces?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.9091 | pass |
| answer_relevance | 0.6201 | 0.6201 | 0.3750 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0276 | 0.0276 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0137-right

Do musicians Robert Fleischman and Jimmy Barnes have the same nationality?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.0775 | 0.0775 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9992 | 0.9992 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0137-hallucinated

Do musicians Robert Fleischman and Jimmy Barnes have the same nationality?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6667 | pass |
| answer_relevance | 0.8728 | 0.8728 | 0.4444 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.3983 | 0.3983 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0138-right

What is the name of this American multinational corporation that provides IT services, headquartered in New Jersey, that acquired Mirabeau?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0814 | 0.0814 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0329 | 0.0329 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0138-hallucinated

What is the name of this American multinational corporation that provides IT services, headquartered in New Jersey, that acquired Mirabeau?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.8562 | 0.8562 | 0.9167 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9982 | 0.9982 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0139-right

When was Fannie Lee Chaney's son born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.3354 | 0.3354 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9814 | 0.9814 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0139-hallucinated

When was Fannie Lee Chaney's son born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7273 | fail |
| answer_relevance | 0.7917 | 0.7917 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9585 | 0.9585 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0140-right

The Canada Memorial in Green Park, London, United Kingdom, commemorates members of the Canadian Forces killed during the First and Second World Wars, the memorial was the result of lobbying and fund raising, much of it in Canada, by the former Canadian media tycoon Conrad Moffat Black, his title is what, of this British former newspaper publisher and author?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2920 | 0.2920 | 0.0294 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6396 | 0.6396 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0140-hallucinated

The Canada Memorial in Green Park, London, United Kingdom, commemorates members of the Canadian Forces killed during the First and Second World Wars, the memorial was the result of lobbying and fund raising, much of it in Canada, by the former Canadian media tycoon Conrad Moffat Black, his title is what, of this British former newspaper publisher and author?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.5034 | 0.5034 | 0.1250 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.5773 | 0.5773 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0141-right

WNP-3 and WNP-5 were constructed by the agency formed in which year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1096 | 0.1096 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4388 | 0.4388 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0141-hallucinated

WNP-3 and WNP-5 were constructed by the agency formed in which year?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.2500 | fail |
| answer_relevance | 0.8621 | 0.8621 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9971 | 0.9971 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0142-right

he Central Harbourfront is a waterfront site it is the result of Central and Wan Chai Reclamation, and it sits to the east of the International Finance Centre (IFC), a skyscraper and an integrated commercial development on the waterfront of the Central District, of which territory?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2981 | 0.2981 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0338 | 0.0338 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0142-hallucinated

he Central Harbourfront is a waterfront site it is the result of Central and Wan Chai Reclamation, and it sits to the east of the International Finance Centre (IFC), a skyscraper and an integrated commercial development on the waterfront of the Central District, of which territory?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.5968 | 0.5968 | 0.0870 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9997 | 0.9997 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0143-right

What city does Bundestag and Reichstag building have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.5455 | 0.5455 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0251 | 0.0251 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0143-hallucinated

What city does Bundestag and Reichstag building have in common?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4286 | fail |
| answer_relevance | 0.9212 | 0.9212 | 0.3000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.7476 | 0.7476 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0144-right

Which musician, Edwyn Collins or Jimmie Ross, played the bass guitar?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.5795 | 0.5795 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8003 | 0.8003 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0144-hallucinated

Which musician, Edwyn Collins or Jimmie Ross, played the bass guitar?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.2000 | pass |
| answer_relevance | 0.7167 | 0.7167 | 0.3000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.0558 | 0.0558 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0145-right

what is the 3112 acre Pennsylvania state park that took over 11,000 to make due to the wave action of lake Erie called?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2118 | 0.2118 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1406 | 0.1406 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0145-hallucinated

what is the 3112 acre Pennsylvania state park that took over 11,000 to make due to the wave action of lake Erie called?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7500 | pass |
| answer_relevance | 0.8504 | 0.8504 | 0.7647 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0463 | 0.0463 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0146-right

Teri W. Odom is a member of a scientific journal first published in 2007 by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3160 | 0.3160 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0469 | 0.0469 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0146-hallucinated

Teri W. Odom is a member of a scientific journal first published in 2007 by who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.8470 | 0.8470 | 0.3529 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0244 | 0.0244 | 0.0000 | pass |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0147-right

What forensic psychiatrist consulted on numbers cases including one for a contract killer associated with the DeCavalcante crime family?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0326 | 0.0326 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0116 | 0.0116 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0147-hallucinated

What forensic psychiatrist consulted on numbers cases including one for a contract killer associated with the DeCavalcante crime family?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.3021 | 0.3021 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9070 | 0.9070 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0148-right

Which American singer-songwriter known as "the Caruso of Rock", recorded on the Monument Records label and had hits such as "Pretty One," and "Uptown"?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3046 | 0.3046 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0139 | 0.0139 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0148-hallucinated

Which American singer-songwriter known as "the Caruso of Rock", recorded on the Monument Records label and had hits such as "Pretty One," and "Uptown"?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7143 | fail |
| answer_relevance | 0.5565 | 0.5565 | 0.2222 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9954 | 0.9954 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0149-right

The central character of "The Adventures of Brer Rabbit" was later adapted into which 1946 Walt Disney Company motion picture film?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0890 | 0.0890 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0237 | 0.0237 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0149-hallucinated

The central character of "The Adventures of Brer Rabbit" was later adapted into which 1946 Walt Disney Company motion picture film?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8000 | fail |
| answer_relevance | 0.6878 | 0.6878 | 0.2667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9766 | 0.9766 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0150-right

Abraham Weinberg was a suspect in the killing of which Irish-American hitman?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1725 | 0.1725 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.2236 | 0.2236 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0150-hallucinated

Abraham Weinberg was a suspect in the killing of which Irish-American hitman?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.6000 | pass |
| answer_relevance | 0.6631 | 0.6631 | 0.2000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0193 | 0.0193 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0151-right

Benjamin Halfpenny was a footballer for a club that plays its home matches where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2291 | 0.2291 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0307 | 0.0307 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0151-hallucinated

Benjamin Halfpenny was a footballer for a club that plays its home matches where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.8897 | 0.8897 | 0.5556 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0310 | 0.0310 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0152-right

The 2000–01 NBA season was the Jazz's 27th season in the National Basketball Association, and 22nd season in Salt Lake City, Utah, after the retirement of Jeff Hornacek, the Jazz signed free agents John Starks, and who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.3128 | 0.3128 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9964 | 0.9964 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0152-hallucinated

The 2000–01 NBA season was the Jazz's 27th season in the National Basketball Association, and 22nd season in Salt Lake City, Utah, after the retirement of Jeff Hornacek, the Jazz signed free agents John Starks, and who?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.6038 | 0.6038 | 0.1364 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9997 | 0.9997 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0153-right

What was population of the city where the Dutch retired footballer Foeke Booy born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | -0.0014 | -0.0014 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0259 | 0.0259 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0153-hallucinated

What was population of the city where the Dutch retired footballer Foeke Booy born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7500 | pass |
| answer_relevance | 0.3293 | 0.3293 | 0.0909 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0474 | 0.0474 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0154-right

In what year was the company that co-developed and distributed the BlackBerry DTEK60 founded?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0721 | 0.0721 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0194 | 0.0194 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0154-hallucinated

In what year was the company that co-developed and distributed the BlackBerry DTEK60 founded?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6250 | fail |
| answer_relevance | 0.9693 | 0.9693 | 0.6667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9902 | 0.9902 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0155-right

Who chaired the ceremony in which the film written by Canet and Philippe Lefebvre won the award for Best Film?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1349 | 0.1349 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0173 | 0.0173 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0155-hallucinated

Who chaired the ceremony in which the film written by Canet and Philippe Lefebvre won the award for Best Film?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.2000 | fail |
| answer_relevance | 0.3909 | 0.3909 | 0.0714 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9960 | 0.9960 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0156-right

Mookychick is an independent daily online magazine and community with more than 100,000 readers a month and over 5,000 forum members, content includes analysis of current sociopolitical events, social and cultural trends, alternative fashion, movies, books, music and arts and crafts from a feminist perspective, in contrast with feminist publications and communities such as which women's lifestyle magazine that is published six times a year, and is published by Debbie Stoller and Laurie Henzel?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0782 | 0.0782 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4573 | 0.4573 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0156-hallucinated

Mookychick is an independent daily online magazine and community with more than 100,000 readers a month and over 5,000 forum members, content includes analysis of current sociopolitical events, social and cultural trends, alternative fashion, movies, books, music and arts and crafts from a feminist perspective, in contrast with feminist publications and communities such as which women's lifestyle magazine that is published six times a year, and is published by Debbie Stoller and Laurie Henzel?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.7391 | 0.7391 | 0.0426 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.5616 | 0.5616 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0157-right

Der Mond was composed by the man who was best known for what cantata?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1964 | 0.1964 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3003 | 0.3003 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0157-hallucinated

Der Mond was composed by the man who was best known for what cantata?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8000 | pass |
| answer_relevance | 0.6671 | 0.6671 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0112 | 0.0112 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0158-right

Mackenzie Davis appeared in the 2013 Canadian romantic comedy film directed by whom?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1016 | 0.1016 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0258 | 0.0258 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0158-hallucinated

Mackenzie Davis appeared in the 2013 Canadian romantic comedy film directed by whom?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8058 | 0.8058 | 0.5455 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9948 | 0.9948 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0159-right

The Developing Communities Project's first executive director was which former President?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0519 | 0.0519 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0425 | 0.0425 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0159-hallucinated

The Developing Communities Project's first executive director was which former President?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5556 | fail |
| answer_relevance | 0.7280 | 0.7280 | 0.5455 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9985 | 0.9985 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0160-right

Jane's Addiction and Weeping Willows, play which genre of music?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2654 | 0.2654 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9991 | 0.9991 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0160-hallucinated

Jane's Addiction and Weeping Willows, play which genre of music?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5714 | fail |
| answer_relevance | 0.9367 | 0.9367 | 0.5556 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8131 | 0.8131 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0161-right

Throne of Glass is a young adult high fantasy novel series, by which bestselling American fantasy author?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0466 | 0.0466 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0775 | 0.0775 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0161-hallucinated

Throne of Glass is a young adult high fantasy novel series, by which bestselling American fantasy author?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8462 | fail |
| answer_relevance | 0.8319 | 0.8319 | 0.8462 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9975 | 0.9975 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0162-right

The largest ship in the "Imperator" class ocean liners had how many gross register tons?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0622 | 0.0622 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0147 | 0.0147 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0162-hallucinated

The largest ship in the "Imperator" class ocean liners had how many gross register tons?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.4444 | pass |
| answer_relevance | 0.8689 | 0.8689 | 0.6667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0919 | 0.0919 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0163-right

Axle Whitehead was a part of an American comedy-drama television series that is a remake of the British series with the same name set in what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | -0.0266 | -0.0266 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1355 | 0.1355 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0163-hallucinated

Axle Whitehead was a part of an American comedy-drama television series that is a remake of the British series with the same name set in what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8462 | pass |
| answer_relevance | 0.9689 | 0.9689 | 0.7333 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0385 | 0.0385 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0164-right

Were both Joseph Roth and Cid Corman authors?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.0245 | 0.0245 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.9635 | 0.9635 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0164-hallucinated

Were both Joseph Roth and Cid Corman authors?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8000 | pass |
| answer_relevance | 0.9206 | 0.9206 | 0.6667 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 0.0000 | fail |
| hallucination | 0.0580 | 0.0580 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0165-right

What was the event that Afghanistan competed in for the first time in 2017 officially known as?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2054 | 0.2054 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0387 | 0.0387 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0165-hallucinated

What was the event that Afghanistan competed in for the first time in 2017 officially known as?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.7071 | 0.7071 | 0.2727 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0140 | 0.0140 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0166-right

Who was the director of the 2001 American romantic comedy film written by Marc Klein in which Lucy Gordon had a small role?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0734 | 0.0734 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0509 | 0.0509 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0166-hallucinated

Who was the director of the 2001 American romantic comedy film written by Marc Klein in which Lucy Gordon had a small role?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.2500 | fail |
| answer_relevance | 0.3201 | 0.3201 | 0.0588 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9996 | 0.9996 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0167-right

What hamlet and census designated place was the location of the only pay-per-view Bunkhouse Stampede?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2781 | 0.2781 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0105 | 0.0105 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0167-hallucinated

What hamlet and census designated place was the location of the only pay-per-view Bunkhouse Stampede?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.8571 | pass |
| answer_relevance | 0.6005 | 0.6005 | 0.1429 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1834 | 0.1834 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0168-right

La Barredora was a gang that declared war on the leader of the cartel based where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2664 | 0.2664 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1768 | 0.1768 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0168-hallucinated

La Barredora was a gang that declared war on the leader of the cartel based where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6250 | fail |
| answer_relevance | 0.8817 | 0.8817 | 0.8750 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9430 | 0.9430 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0169-right

What year did the chairman of the Jenkins Commission die?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.1995 | 0.1995 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9439 | 0.9439 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0169-hallucinated

What year did the chairman of the Jenkins Commission die?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.6033 | 0.6033 | 0.1250 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9978 | 0.9978 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0170-right

Who was born first, Odysseas Elytis or Cornel West?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.5986 | 0.5986 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9319 | 0.9319 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0170-hallucinated

Who was born first, Odysseas Elytis or Cornel West?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.7049 | 0.7049 | 0.4286 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.8351 | 0.8351 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0171-right

"Let Me Out" is a song released as the fifth single from what band's fifth studio album "Humanz" which was recorded in London, Paris, New York City, Chicago, and Jamaica ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2802 | 0.2802 | 0.0455 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0218 | 0.0218 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0171-hallucinated

"Let Me Out" is a song released as the fifth single from what band's fifth studio album "Humanz" which was recorded in London, Paris, New York City, Chicago, and Jamaica ?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6250 | fail |
| answer_relevance | 0.6869 | 0.6869 | 0.1818 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9968 | 0.9968 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0172-right

Up to how far off can the Deal Timeball be from Coordinated Universal Time?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.0891 | 0.0891 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.2156 | 0.2156 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0172-hallucinated

Up to how far off can the Deal Timeball be from Coordinated Universal Time?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8774 | 0.8774 | 0.8571 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.8784 | 0.8784 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0173-right

Superheaven and Oceansize, are bands of which shared genre?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.3166 | 0.3166 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9989 | 0.9989 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0173-hallucinated

Superheaven and Oceansize, are bands of which shared genre?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.6610 | 0.6610 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.5809 | 0.5809 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0174-right

What nationality was a  historical drama film directed by?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1605 | 0.1605 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0145 | 0.0145 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0174-hallucinated

What nationality was a  historical drama film directed by?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.5650 | 0.5650 | 0.5714 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9994 | 0.9994 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0175-right

Who has more scope of profession, Richard Ford or Robert E. Howard?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6140 | 0.6140 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1940 | 0.1940 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0175-hallucinated

Who has more scope of profession, Richard Ford or Robert E. Howard?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.6396 | 0.6396 | 0.2222 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9825 | 0.9825 | 0.0000 | fail |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0176-right

The American Aircraft Penetrator was modified from a helicopter produced by what nation's military?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1627 | 0.1627 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1291 | 0.1291 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0176-hallucinated

The American Aircraft Penetrator was modified from a helicopter produced by what nation's military?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.6644 | 0.6644 | 0.3333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9955 | 0.9955 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0177-right

Canton Road Station was a planned railway station on the Kowloon Southern Link of West Rail Line, that was to run beneath a large shopping mall located where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.2625 | 0.2625 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.6559 | 0.6559 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0177-hallucinated

Canton Road Station was a planned railway station on the Kowloon Southern Link of West Rail Line, that was to run beneath a large shopping mall located where?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8750 | fail |
| answer_relevance | 0.5600 | 0.5600 | 0.1905 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9436 | 0.9436 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0178-right

What South Korean sitcom starred a South Korean singer and actress who began her music career at the age of 15?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1667 | 0.1667 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0331 | 0.0331 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0178-hallucinated

What South Korean sitcom starred a South Korean singer and actress who began her music career at the age of 15?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4238 | 0.4238 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0101 | 0.0101 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0179-right

Ghostbusters is a song written and recorded by Ray Parker Jr. as the theme song for a movie starring a Canadian-American actor who was an original member of the Not Ready for Prime Time Players on what show?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2231 | 0.2231 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0256 | 0.0256 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0179-hallucinated

Ghostbusters is a song written and recorded by Ray Parker Jr. as the theme song for a movie starring a Canadian-American actor who was an original member of the Not Ready for Prime Time Players on what show?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.5000 | 0.5000 | 0.9286 | pass |
| answer_relevance | 0.9444 | 0.9444 | 0.9000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.4720 | 0.4720 | 0.0000 | pass |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0180-right

Gelatine was an airship piloted on September 19, 1905 by a pioneer American aviator and what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2336 | 0.2336 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1215 | 0.1215 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0180-hallucinated

Gelatine was an airship piloted on September 19, 1905 by a pioneer American aviator and what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8889 | fail |
| answer_relevance | 0.9463 | 0.9463 | 0.8889 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9496 | 0.9496 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0181-right

Which movie was released first, The Hunchback of Notre Dame or Saludos Amigos?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.5123 | 0.5123 | 0.2500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9827 | 0.9827 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0181-hallucinated

Which movie was released first, The Hunchback of Notre Dame or Saludos Amigos?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8000 | fail |
| answer_relevance | 0.7607 | 0.7607 | 0.6250 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9964 | 0.9964 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0182-right

In what country did the repression of citizens by a dictator during the period of 1973 to 1990 occur?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2193 | 0.2193 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0240 | 0.0240 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0182-hallucinated

In what country did the repression of citizens by a dictator during the period of 1973 to 1990 occur?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.3750 | fail |
| answer_relevance | 0.8525 | 0.8525 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9976 | 0.9976 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0183-right

The mother of the vice chair of Hillary Clinton's 2016 campaign for President is the director of what institue?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2270 | 0.2270 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0201 | 0.0201 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0183-hallucinated

The mother of the vice chair of Hillary Clinton's 2016 campaign for President is the director of what institue?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6559 | 0.6559 | 0.2857 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0456 | 0.0456 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0184-right

Michael Ralph DeVito (born June 10, 1984) is a former American football defensive end, he  the National Football League (NFL), DeVito attended high school at Nauset Regional High School an NEASC accredited high school located in North Eastham, in which state?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1586 | 0.1586 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0478 | 0.0478 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0184-hallucinated

Michael Ralph DeVito (born June 10, 1984) is a former American football defensive end, he  the National Football League (NFL), DeVito attended high school at Nauset Regional High School an NEASC accredited high school located in North Eastham, in which state?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8000 | fail |
| answer_relevance | 0.7123 | 0.7123 | 0.1538 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9993 | 0.9993 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0185-right

"Apocalypic" is a song sung by Lizzy Hale from which group?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4144 | 0.4144 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0528 | 0.0528 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0185-hallucinated

"Apocalypic" is a song sung by Lizzy Hale from which group?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.6512 | 0.6512 | 0.3750 | pass |
| context_precision | 1.0000 | 1.0000 | 0.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9992 | 0.9992 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0186-right

Ted Sutton plays Sergeant Cunningham in a2002 film that stars Mel Gibson as what character?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3992 | 0.3992 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0251 | 0.0251 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0186-hallucinated

Ted Sutton plays Sergeant Cunningham in a2002 film that stars Mel Gibson as what character?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5455 | fail |
| answer_relevance | 0.8737 | 0.8737 | 0.6923 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9923 | 0.9923 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0187-right

Who is the former professional tennis player from Italy, Chris Evert or Mara Santangelo?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.6770 | 0.6770 | 0.2222 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3294 | 0.3294 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0187-hallucinated

Who is the former professional tennis player from Italy, Chris Evert or Mara Santangelo?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.8251 | 0.8251 | 0.5000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.8554 | 0.8554 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0188-right

Who directed a film that included Sarah Manninen?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2861 | 0.2861 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0456 | 0.0456 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0188-hallucinated

Who directed a film that included Sarah Manninen?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.4284 | 0.4284 | 0.1250 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0095 | 0.0095 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0189-right

The republic with the smallest population of all the members of the Council of Europe is one of few places in Europe where a species of beetle cannot be found, that wew originally described in 1809 by whom?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1679 | 0.1679 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0305 | 0.0305 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0189-hallucinated

The republic with the smallest population of all the members of the Council of Europe is one of few places in Europe where a species of beetle cannot be found, that wew originally described in 1809 by whom?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5714 | fail |
| answer_relevance | 0.6843 | 0.6843 | 0.3636 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9880 | 0.9880 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0190-right

At the 2011 census, what was he population of the city where Kerry Saxby-Junna was born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | -0.0142 | -0.0142 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0218 | 0.0218 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0190-hallucinated

At the 2011 census, what was he population of the city where Kerry Saxby-Junna was born?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.4000 | fail |
| answer_relevance | 0.7049 | 0.7049 | 0.5000 | pass |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9955 | 0.9955 | 1.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0191-right

How many German scientists, engineers, and technicians, were recruited in post-Nazi Germany as a result of the clandestine operation where Arthur Rudolph became one of the main developers of the U.S. ?space program

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.0946 | 0.0946 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0134 | 0.0134 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0191-hallucinated

How many German scientists, engineers, and technicians, were recruited in post-Nazi Germany as a result of the clandestine operation where Arthur Rudolph became one of the main developers of the U.S. ?space program

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8000 | fail |
| answer_relevance | 0.6672 | 0.6672 | 0.1364 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.7752 | 0.7752 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0192-right

Marion is approximately 50 mi north of a city that is the third-most populous what in the U.S.?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3520 | 0.3520 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0318 | 0.0318 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0192-hallucinated

Marion is approximately 50 mi north of a city that is the third-most populous what in the U.S.?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.7500 | fail |
| answer_relevance | 0.9081 | 0.9081 | 0.7500 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9955 | 0.9955 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0193-right

Jayantabhai Ki Luv Story includes a lead role for the film actress and model who is a native of what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.1858 | 0.1858 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0800 | 0.0800 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0193-hallucinated

Jayantabhai Ki Luv Story includes a lead role for the film actress and model who is a native of what city?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.3365 | 0.3365 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0895 | 0.0895 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0194-right

Which is currently more valuable, Temagami-Lorrain Mine or Meadowbank Gold Mine?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 1.0000 | fail |
| answer_relevance | 0.7410 | 0.7410 | 0.4286 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9675 | 0.9675 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0194-hallucinated

Which is currently more valuable, Temagami-Lorrain Mine or Meadowbank Gold Mine?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.5000 | fail |
| answer_relevance | 0.8115 | 0.8115 | 0.4167 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 0.0000 | 0.0000 | 1.0000 | fail |
| hallucination | 0.9982 | 0.9982 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0195-right

St James Street appears as a segment of Whitecross Street on the 1610 map of the Monmouth by an English historian best known as a mapmaker of what perior?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2459 | 0.2459 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0375 | 0.0375 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0195-hallucinated

St James Street appears as a segment of Whitecross Street on the 1610 map of the Monmouth by an English historian best known as a mapmaker of what perior?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.2039 | 0.2039 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.3482 | 0.3482 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0196-right

The Pineground Bridge formerly carried Depot Road over the Suncook River into a town with a population of what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | -0.0546 | -0.0546 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0144 | 0.0144 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0196-hallucinated

The Pineground Bridge formerly carried Depot Road over the Suncook River into a town with a population of what?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.8333 | fail |
| answer_relevance | 0.9312 | 0.9312 | 0.8333 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9631 | 0.9631 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0197-right

Which city is the American rock band, that released their album on March 19, 2012, from?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2311 | 0.2311 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.0681 | 0.0681 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0197-hallucinated

Which city is the American rock band, that released their album on March 19, 2012, from?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.6667 | fail |
| answer_relevance | 0.1541 | 0.1541 | 0.0000 | fail |
| context_precision | 0.0000 | 0.0000 | 1.0000 | fail |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9984 | 0.9984 | 0.0000 | fail |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0198-right

The Rossendale Free Press serves the town how far north of Manchester?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.0000 | pass |
| answer_relevance | 0.2477 | 0.2477 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.0309 | 0.0309 | 1.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0198-hallucinated

The Rossendale Free Press serves the town how far north of Manchester?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 0.7500 | pass |
| answer_relevance | 0.9171 | 0.9171 | 0.6000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 0.0000 | pass |
| hallucination | 0.0332 | 0.0332 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0199-right

Which american president's father was a farmer and he was a former US representative from NY?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 1.0000 | 1.0000 | 1.0000 | pass |
| answer_relevance | 0.2237 | 0.2237 | 0.0000 | fail |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.1034 | 0.1034 | 0.0000 | pass |

Judge note: Mean lexical coverage across 1 claim(s).
Input guard: allow.
Output guard: allow.

## halueval-qa-0199-hallucinated

Which american president's father was a farmer and he was a former US representative from NY?

| Metric | Value | Baseline | Judge | Passed |
| --- | ---: | ---: | ---: | --- |
| faithfulness | 0.0000 | 0.0000 | 0.0000 | fail |
| answer_relevance | 0.4194 | 0.4194 | 0.0000 | pass |
| context_precision | 1.0000 | 1.0000 | 1.0000 | pass |
| context_recall | 1.0000 | 1.0000 | 1.0000 | pass |
| hallucination | 0.9708 | 0.9708 | 1.0000 | fail |

Judge note: Mean lexical coverage across 2 claim(s).
Input guard: allow.
Output guard: allow.
