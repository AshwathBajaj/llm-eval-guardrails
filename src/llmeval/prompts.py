"""Judge prompt format shared by the metrics and the mock backend.

The mock backend parses this format back out. Keeping one writer and one
reader is what makes the offline demo agree with the real judge path.
"""

from __future__ import annotations

import json
import re

from pydantic import BaseModel, ValidationError

_TASK = re.compile(r"^Task:\s*(.+)$", re.MULTILINE)


class JudgeOutput(BaseModel):
    score: float
    reason: str = ""


class JudgeParseError(ValueError):
    """The judge replied, but not with a usable score."""


def judge_prompt(task: str, sections: dict[str, str], rubric: str) -> str:
    lines = [
        "You are a strict evaluation judge.",
        f"Task: {task}",
        "Return JSON only with keys score (float from 0 to 1) and reason (a short string).",
        f"Rubric: {rubric}",
        "",
    ]
    for key, value in sections.items():
        lines.append(f"## {key}")
        lines.append(value.strip())
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parse_judge_prompt(prompt: str) -> tuple[str, dict[str, str]]:
    """Return the task name and ``##`` sections. Task is empty when absent."""
    task_match = _TASK.search(prompt)
    task = task_match.group(1).strip() if task_match else ""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in prompt.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return task, {key: "\n".join(lines).strip() for key, lines in sections.items()}


def parse_judge_output(raw: str) -> JudgeOutput:
    text = raw.strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match is None:
            raise JudgeParseError("judge did not return JSON") from None
        try:
            payload = json.loads(match.group(0))
        except json.JSONDecodeError as exc:
            raise JudgeParseError("judge returned malformed JSON") from exc
    try:
        parsed = JudgeOutput.model_validate(payload)
    except ValidationError as exc:
        raise JudgeParseError("judge JSON is missing a numeric score") from exc
    if not 0.0 <= parsed.score <= 1.0:
        raise JudgeParseError("judge score is outside 0 to 1")
    return parsed
