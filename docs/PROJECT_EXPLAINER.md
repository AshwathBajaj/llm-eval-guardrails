# llmeval, a learning guide

This guide explains the project in plain English. You can read it before an interview and use the model answers at the end. Every number comes from a run of this repository. If a number is from the mock judge, the text says so.

## What the project does

llmeval checks two things.

First, it scores a retrieval-augmented generation answer. Retrieval-augmented generation, or RAG, means the model is given a passage and asked to answer from that passage. The score asks: does the answer stay on the passage, and does the answer address the question?

Second, it checks the user's text against a policy. The policy can block a jailbreak, redact an email address, or flag a toxic reply.

Think of a librarian. The score is the librarian checking that the answer came from the book on the desk. The guardrail is the librarian refusing to hand over a book the library does not lend. The mechanism is code: metric functions for the score, and a YAML file that lists which checks run.

## Architecture

```text
You
  CLI, FastAPI page, or Gradio app
       |
       v
  Pipeline
       |-- metrics: faithfulness, relevance, precision, recall, hallucination
       |        |-- baseline: MiniLM cosine, or an NLI model, or the hashing embedder
       |        |-- judge: mock lexical scorer, or an OpenAI-compatible model
       |-- guardrails: injection, PII, toxicity, topic, JSON schema
       |        |-- injection mode: regex, classifier, or hybrid
       v
  JSON, Markdown, and HTML reports
```

The analogy is an assembly line. The mechanism is `evaluate_examples` in `src/llmeval/pipeline.py`. It builds one embedder, an optional NLI model, the metric objects, and a guardrail engine. Each example goes through every metric, then the question and the answer go through the guardrails. The writers in `src/llmeval/report/render.py` turn that object into files.

## The pieces, one by one

### The example

One row has an id, a question, a list of context passages, an answer, an optional ground-truth answer, and an optional label such as `right` or `hallucinated`. The class is `RagExample` in `src/llmeval/models.py`.

Analogy: a flash card. Mechanism: one JSON object per line in a `.jsonl` file.

### The baseline and the judge

Every metric stores two numbers. The baseline is computed on this machine. The judge is a second opinion from a language-model prompt. In the benchmark, the headline number is the baseline. The judge is the mock, and the report says `mock:mock-judge-v1`. The mock does not call a neural model. It counts word overlap. That is why it is labeled as mocked.

Analogy: a calculator beside a second person with a checklist. Mechanism: `finish_metric` in `src/llmeval/metrics/common.py` keeps both numbers. If the judge returns junk, the baseline remains.

### MiniLM, the NLI model, and the hashing embedder

MiniLM (`all-MiniLM-L6-v2`) turns a sentence into a list of numbers called an embedding. Two sentences about the same thing land closer together. Closeness is cosine similarity, a dot product of two normalized vectors. The code is `SentenceTransformerEmbedder` in `src/llmeval/neural.py`.

The NLI model (`nli-MiniLM2-L6-H768`) reads a passage and a claim and returns three probabilities: contradiction, entailment, and neutral. Entailment means the passage supports the claim. The code is `NLICrossEncoder` in the same file. `best_support` scores the claim against every sentence in the context and keeps the highest entailment probability.

The hashing embedder does not download a model. It hashes words and character groups into 256 buckets. CI and the small demo page use it so tests stay offline. The class is `HashingEmbedder` in `src/llmeval/embeddings.py`.

Analogy: MiniLM is a map of meaning. The hash embedder is a map of spelling. The NLI model is a clerk who says "this sentence follows from that sentence."

### Faithfulness and hallucination

Faithfulness splits the answer into sentences. A sentence passes if its best entailment probability is at least 0.50. The score is the fraction of sentences that pass.

Hallucination is the average of `1 - entailment` for those sentences. Higher means more of the answer is unsupported. A row passes when that average is at or below 0.50.

They are related and they are not the same. Faithfulness is a yes-or-no per sentence. Hallucination is a graded leftover.

### Answer relevance

Relevance ignores whether the answer is true. It asks whether the answer is about the question. On the benchmark this is the MiniLM cosine of the question and the answer. A short correct span can score lower than a long wrong sentence, because the long sentence shares more of the question's meaning. That happened on HaluEval. The section below gives the numbers.

### Context precision and context recall

Precision looks at the retrieved list from the top. A relevant passage in first place scores 1. A relevant passage behind a distractor scores 0.5. The function is `precision_from_relevance` in `src/llmeval/scoring.py`.

HaluEval gives one passage per question, so precision there is only "was this passage about the question." It cannot show ranking. A passage is relevant when its MiniLM cosine with the question is at least 0.35.

Recall looks at the ground-truth answer, not the model's answer, and asks whether the passage supports it.

### The other guardrails

PII detection finds emails, phone numbers with separators, Social Security numbers, and card numbers that pass the Luhn checksum, then replaces them with placeholders. Toxicity is a short word list. Off-topic fires only when the text misses the configured vocabulary and also sits far from the topic descriptions. JSON Schema checks structured output and is off unless a case asks for it. The engine is `GuardrailEngine` in `src/llmeval/guardrails/engine.py`. The strictest triggered action wins: block, then redact, then flag, then allow.

## What changed in this upgrade

### Why the regex failed

The original injection check is a list of regular expressions in `src/llmeval/guardrails/injection.py`. A regular expression is a search pattern. It catches "ignore previous instructions" and "DAN mode". It does not understand a sentence that means the same thing in different words.

On the held-out test set the regex caught 33 attacks and missed 143. It did not flag any of the 176 benign prompts. Precision was 1.0000, because every time it fired it was right. Recall was 0.1875, because it missed most attacks. F1, which balances those two, was 0.3158.

### What a classifier is

A classifier is a model that reads text and returns a probability that the text is an attack. This project fine-tunes MiniLM, the same small transformer used for embeddings. Fine-tuning means the training run updates the model's weights on labeled examples, including a new two-class head (benign versus attack). The code that trains it is `scripts/train_injection_classifier.py`. The saved weights are in `models/injection-minilm/`.

Analogy: a student who studies past exams, then sits a new exam. Mechanism: three epochs of cross-entropy loss on token sequences truncated to 256 tokens, learning rate 0.00002, batch size 16, seed 42.

### Train, validation, and test

The training pool is the train split of two public datasets. Both dataset cards say Apache-2.0.

- `deepset/prompt-injections` train split: 546 rows.
- `jackhhao/jailbreak-classification` train split: 1,044 rows.

After dropping duplicates and any text that also appeared in the test set, 1,571 rows remained. Seven rows were removed because they were leaks into the test set. A stratified 20 percent of the remaining pool is the validation split: 1,256 train rows and 315 validation rows. Stratified means each split keeps a similar mix of attacks and benign prompts.

The test set was not used to train and not used to pick the threshold. It has 352 prompts and is balanced, 176 attacks and 176 benign:

- every row of the deepset test split (116 rows)
- the jailbreak prompts already used by the red team, which are the jailbreak test rows of at most 4,000 characters (236 rows). Twenty-six longer test prompts were skipped, the same rule the red-team file used.

### How the threshold was chosen

The model outputs a probability from 0 to 1. A threshold is the cutoff. At 0.85, a prompt is an attack when the probability is 0.85 or higher.

The cutoff was chosen only on the validation split. The script tried 0.05, 0.10, and so on up to 0.95, and kept the value with the highest F1. If two cutoffs tied on F1, it kept the one with fewer false alarms. The winner was 0.85. On validation that cutoff had precision 0.9786, recall 0.9580, F1 0.9682, and a false-positive rate of 0.0174. Those validation numbers are not the test numbers. The test numbers are in the next section.

### How to read precision, recall, F1, and the false-positive rate

Precision: of the prompts the detector called attacks, what fraction really were attacks. High precision means few false alarms.

Recall: of the real attacks, what fraction the detector caught. High recall means few misses.

F1: the harmonic mean of precision and recall. It is low if either one is low. The regex has perfect precision and weak recall, so its F1 is 0.3158.

False-positive rate: of the benign prompts, what fraction were flagged. This is the cost paid by ordinary users.

A confusion matrix is a four-cell table. Rows are the truth. Columns are the prediction. The cells are true benign, false alarm, missed attack, and caught attack.

### The test results

| Detector | Precision | Recall | F1 | False-positive rate | Mean latency |
| --- | ---: | ---: | ---: | ---: | ---: |
| Regex | 1.0000 | 0.1875 | 0.3158 | 0.0000 | 0.0702 ms |
| Classifier | 0.9938 | 0.9091 | 0.9496 | 0.0057 | 7.2965 ms |
| Hybrid | 0.9938 | 0.9091 | 0.9496 | 0.0057 | 6.0801 ms |

Regex confusion matrix: 176 true benign, 0 false alarms, 143 missed attacks, 33 caught attacks.

Classifier and hybrid: 175 true benign, 1 false alarm, 16 missed attacks, 160 caught attacks.

![Confusion matrices](docs/images/injection_confusion.png)

Hybrid means the regex runs first. If it matches, the prompt is blocked and the classifier is not called. If it does not match, the classifier decides. On this test set the regex never caught an attack the classifier missed, so precision, recall, and F1 are the same as the classifier. Hybrid is slightly faster, 6.0801 ms versus 7.2965 ms per prompt, because some prompts stop at the regex. The regex itself is 0.0702 ms. Latency is the mean per prompt after one warmup call, measured on this test set.

The practical reading: the regex is safe and narrow. The classifier catches most of the attacks the regex misses, at the cost of one benign prompt in 176 and about 7 milliseconds. Hybrid keeps the regex as a fast, exact backstop.

The guardrail YAML key is `mode`, with values `regex`, `classifier`, or `hybrid`. The default is `regex`, so the older red-team report and the CI tests stay on the pattern list.

### The HaluEval scores, so the two parts of the project stay distinct

These numbers are from `configs/eval.benchmark.yaml` on the first 200 HaluEval QA rows, each scored twice (400 examples). The baseline is MiniLM plus the NLI model. The judge is the mock and is not mixed into these means. HaluEval's card says Apache-2.0.

| Metric | All 400 | Right (200) | Hallucinated (200) |
| --- | ---: | ---: | ---: |
| Faithfulness | 0.5212 | 0.7400 | 0.3025 |
| Hallucination | 0.4940 | 0.2974 | 0.6907 |
| Answer relevance | 0.4635 | 0.2421 | 0.6850 |
| Context precision | 0.9350 | 0.9350 | 0.9350 |
| Context recall | 0.7400 | 0.7400 | 0.7400 |

Right answers pass the faithfulness line 148 of 200 times. Hallucinated answers pass it 62 of 200 times. Relevance is higher for hallucinated answers because those answers are full sentences and many right answers are short spans. Precision and recall match across the two groups because both copies share the passage and the ground truth.

## How the demo works, and how to deploy it

`app.py` is a Gradio app. Gradio is a small web form in front of a Python function. The function calls the same metric classes and the same injection check as the CLI.

On screen you get:

- Faithfulness baseline from the NLI model, with the pass line at 0.50.
- The mock judge's number, labeled as lexical and not a neural model.
- Relevance baseline from MiniLM cosine, with the pass line at 0.30.
- Three injection verdicts on the question: regex, classifier, and hybrid, each with a reason. The classifier reason includes the attack probability.

Run it locally:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python app.py
```

Then open `http://127.0.0.1:7860`. Two buttons load a grounded HaluEval example and a short jailbreak the regex misses.

![The Gradio demo](docs/images/demo.png)

This copy was not uploaded to Hugging Face, because there is no token here. To deploy it:

1. Create a Space at https://huggingface.co/new-space and choose the Gradio SDK.
2. Push this repository to the Space. Include `app.py`, `requirements.txt`, `src/`, and `models/injection-minilm/`.
3. Keep the YAML block at the top of `README.md`. It sets `sdk: gradio`, `sdk_version: 5.49.1`, and `app_file: app.py`.
4. Leave the Space on CPU. The first boot downloads MiniLM and the NLI model. The injection weights are already in the repository.
5. Open the Space URL when the logs say the app is running.

## Glossary

**Attack.** A prompt labeled as an injection or a jailbreak. The positive class in the detector.

**Baseline.** The score computed on this machine, without calling a paid API.

**Benign.** A prompt that is not an attack. The negative class.

**Classifier.** A model that maps text to a class probability.

**Confusion matrix.** The four counts: true benign, false alarm, missed attack, caught attack.

**Cosine similarity.** How aligned two embedding vectors are. 1 means the same direction.

**Embedding.** A list of numbers that stands for a piece of text.

**Entailment.** The NLI decision that the passage supports the claim.

**F1.** The harmonic mean of precision and recall.

**False-positive rate.** False alarms divided by all benign prompts.

**Fine-tuning.** Continuing training of an existing model on a new labeled set.

**Ground truth.** The reference answer, used by context recall. It is not the model's answer.

**Hybrid.** Regex first. If the regex does not match, the classifier decides. A block from either one blocks the prompt.

**Mock judge.** A word-overlap scorer that pretends to be a language-model judge so tests run with no API key. It is not a neural model.

**NLI.** Natural language inference. A model that compares a premise and a hypothesis.

**Precision.** Caught attacks divided by everything the detector called an attack.

**Recall.** Caught attacks divided by all real attacks.

**Regex.** A text pattern. Fast and exact, and blind to paraphrases.

**Threshold.** The probability cutoff. Here it is 0.85, chosen on the validation split.

**Validation split.** Labeled data used to choose the cutoff, and not used as the final test.

## Interview questions

### What does this project do?

It scores RAG answers for grounding and relevance, and it checks prompts against a written policy. The scoring baseline on the benchmark is a local MiniLM embedder plus a small NLI model. The injection policy can be a regex, a fine-tuned MiniLM classifier, or both.

### Why keep a mock judge if you have real models?

The mock lets every test and the red-team report run with no API key and no GPU. The benchmark file records `baseline_model` and `nli_model` so a reader can see that the headline score is not the mock. The mock column is still stored, and it is labeled `mock:mock-judge-v1`.

### Why did the regex get a perfect precision and a weak recall?

Because it only fires on a short list of phrases. On 176 held-out attacks it caught 33 and missed 143. It flagged 0 of 176 benign prompts. Precision 1.0000, recall 0.1875, F1 0.3158. A paraphrase of "ignore the instructions" walks past it.

### What did you train, and on what license?

A sequence classifier starting from `sentence-transformers/all-MiniLM-L6-v2`, which is Apache-2.0. The labels come from the train splits of `deepset/prompt-injections` and `jackhhao/jailbreak-classification`, both Apache-2.0 on the dataset cards. Three epochs, seed 42.

### How did you keep the test honest?

The test set is the deepset test split plus the jailbreak prompts already in the red-team file. Those strings were removed from training if they also appeared there. Seven leaks were removed. The threshold was chosen by a sweep on the validation split only. The test set was scored once after that.

### Why is the threshold 0.85 and not 0.50?

Because 0.85 had the best F1 on the validation split. The sweep was 0.05 through 0.95. Ties would have gone to the lower false-positive rate. On the test set, which did not pick this cutoff, precision is 0.9938, recall is 0.9091, and the false-positive rate is 0.0057.

### Why did hybrid not beat the classifier on F1?

On this test set every attack the regex caught, the classifier also caught. Hybrid recall stays 0.9091. Hybrid is still useful: the regex is an exact, readable backstop, and the measured latency dropped from 7.2965 ms to 6.0801 ms because some prompts never reach the model.

### Why is relevance higher for hallucinated HaluEval answers?

The right answers are often a few words. The hallucinated answers are sentences that talk about the question. MiniLM cosine rewards that. The group means are 0.2421 and 0.6850. Faithfulness is the metric that moves the right way: 0.7400 versus 0.3025.

### Where does this sit in a real RAG product?

Run the input guardrail before the model call. After retrieval, context precision can reject a bad passage. After generation, faithfulness decides whether to show the answer. The red team runs in CI against the policy file. I would not block users on a threshold that was fit on the same rows I am reporting. The 0.85 cutoff was fit on validation, then reported on test, which is the right order, and it is still one dataset pair, not every attack style.

### What would you do next?

Add attack styles that were not in these two datasets, and do not edit the regex until that new set looks good. Add a benchmark with several ranked passages so context precision is a ranking score. Fit the next threshold on a fresh validation split.

## Limitations

The classifier sees at most 256 tokens. A long jailbreak can hide the attack past the cutoff. Twenty-six jailbreak test prompts longer than 4,000 characters were not in the red-team file and were not in this test set.

Hybrid did not raise F1 on this particular test. It is a safety net, not a free accuracy gain.

The threshold and the epoch choice both looked at the validation split. The test set was untouched, but the validation F1 of 0.9682 is not a test score and should not be quoted as one.

HaluEval has one passage per question, so the precision number 0.9350 is not evidence about ranking.

Relevance cosine is not a truth score. The HaluEval table shows that clearly.

The mock judge is a lexicon. Quoting it as model quality would be wrong. The reports label it.

The regex list and the toxicity list are short on purpose. They miss paraphrases and implied abuse.

The demo was run locally. It was not deployed to Hugging Face Spaces, because this environment has no token.
