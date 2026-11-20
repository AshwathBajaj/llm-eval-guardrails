"""Run the checks named in a guardrail policy and pick one decision.

Decision order is block, then redact, then flag, then allow. A clean text
stays allow. Redaction still happens when a later check blocks, so the
output text does not keep a card number just because the prompt was also
an injection.
"""

from __future__ import annotations

from typing import Any

from llmeval.config import GuardrailsConfig
from llmeval.embeddings import TextEmbedder, build_embedder
from llmeval.guardrails.injection import PromptInjectionCheck
from llmeval.guardrails.pii import PIICheck
from llmeval.guardrails.schema import SchemaCheck
from llmeval.guardrails.topic import TopicCheck
from llmeval.guardrails.toxicity import ToxicityCheck
from llmeval.models import Finding, GuardReport
from llmeval.scoring import scrub

_RANK = {"allow": 0, "flag": 1, "redact": 2, "block": 3}


class GuardrailEngine:
    def __init__(self, config: GuardrailsConfig, embedder: TextEmbedder | None = None) -> None:
        self.config = config
        self.embedder = embedder if embedder is not None else build_embedder(config.embedder)
        self._input_injection = self._injection_check(config.input.prompt_injection)
        self._output_injection = self._injection_check(config.output.prompt_injection)
        self._pii = PIICheck()
        self._toxicity = ToxicityCheck()
        topic = config.output.off_topic
        self._topic = TopicCheck(
            self.embedder,
            allowed_topics=topic.allowed_topics,
            in_domain_terms=topic.in_domain_terms,
            min_hits=topic.min_hits,
            similarity_threshold=topic.similarity_threshold,
        )

    def run(
        self,
        text: str,
        stage: str,
        *,
        json_schema: dict[str, Any] | None = None,
    ) -> GuardReport:
        if stage not in {"input", "output"}:
            raise ValueError("stage must be 'input' or 'output'")
        findings = [
            self._finding(stage, name, action, checker.check(text))
            for name, action, checker in self._plan(stage, json_schema)
        ]
        decision = "allow"
        for finding in findings:
            if finding.triggered and _RANK[finding.action] > _RANK[decision]:
                decision = finding.action
        output_text = text
        for finding in findings:
            redacted = finding.details.get("redacted_text")
            if (
                finding.guardrail == "pii"
                and finding.triggered
                and finding.action in {"redact", "block"}
                and isinstance(redacted, str)
            ):
                output_text = redacted
        return GuardReport(
            stage=stage,
            decision=decision,
            text=text,
            output_text=output_text,
            findings=findings,
        )

    def _injection_check(self, policy) -> PromptInjectionCheck:
        return PromptInjectionCheck(
            mode=policy.mode,
            threshold=policy.threshold,
            model_path=policy.model_path,
        )

    def _plan(
        self,
        stage: str,
        json_schema: dict[str, Any] | None,
    ) -> list[tuple[str, str, object]]:
        planned: list[tuple[str, str, object]] = []
        if stage == "input":
            policy = self.config.input
            if policy.prompt_injection.enabled:
                planned.append(
                    ("prompt_injection", policy.prompt_injection.action, self._input_injection)
                )
            if policy.pii.enabled:
                planned.append(("pii", policy.pii.action, self._pii))
            return planned

        policy = self.config.output
        if policy.prompt_injection.enabled:
            planned.append(
                ("prompt_injection", policy.prompt_injection.action, self._output_injection)
            )
        if policy.toxicity.enabled:
            planned.append(("toxicity", policy.toxicity.action, self._toxicity))
        if policy.off_topic.enabled:
            planned.append(("off_topic", policy.off_topic.action, self._topic))
        schema_body = json_schema
        schema_action = "block"
        if schema_body is None and policy.schema_check.enabled:
            schema_body = policy.schema_check.json_schema
            schema_action = policy.schema_check.action
        if schema_body is not None:
            planned.append(("schema", schema_action, SchemaCheck(schema_body)))
        return planned

    def _finding(self, stage: str, name: str, action: str, result: object) -> Finding:
        if not isinstance(result, dict):
            raise TypeError(f"{name} returned a non-dict result")
        return Finding(
            guardrail=name,
            stage=stage,
            action=action,
            triggered=bool(result["triggered"]),
            severity=str(result["severity"]),
            message=str(result["message"]),
            details=scrub(result["details"]),  # type: ignore[arg-type]
        )
