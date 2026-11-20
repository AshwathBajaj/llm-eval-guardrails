"""Validate model output against a JSON Schema.

Fenced ```json blocks are unwrapped first, which is how chat models usually
return structured output.
"""

from __future__ import annotations

import json
import re
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL | re.IGNORECASE)


def parse_json_payload(text: str) -> tuple[Any | None, str | None]:
    raw = text.strip()
    fenced = _FENCE.search(raw)
    if fenced:
        raw = fenced.group(1).strip()
    try:
        return json.loads(raw), None
    except json.JSONDecodeError as exc:
        return None, f"invalid json: {exc.msg}"


class SchemaCheck:
    name = "schema"

    def __init__(self, json_schema: dict[str, Any]) -> None:
        try:
            Draft202012Validator.check_schema(json_schema)
        except SchemaError as exc:
            raise ValueError(f"invalid json schema: {exc.message}") from exc
        self.json_schema = json_schema
        self.validator = Draft202012Validator(json_schema)

    def check(self, text: str) -> dict[str, object]:
        payload, error = parse_json_payload(text)
        if error:
            return {
                "triggered": True,
                "severity": "high",
                "message": error,
                "details": {"errors": [error]},
            }
        errors = sorted(self.validator.iter_errors(payload), key=lambda item: list(item.path))
        if not errors:
            return {
                "triggered": False,
                "severity": "none",
                "message": "json matches the schema",
                "details": {"errors": []},
            }
        messages = [item.message for item in errors]
        return {
            "triggered": True,
            "severity": "high",
            "message": messages[0],
            "details": {"errors": messages},
        }
