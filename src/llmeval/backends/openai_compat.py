"""Client for any server that speaks the OpenAI chat completions API.

That includes the OpenAI API itself, Azure-style gateways, vLLM, and Ollama's
OpenAI-compatible endpoint. The toolkit only depends on the chat completions
shape, not on a vendor SDK.
"""

from __future__ import annotations

import os
from typing import Any

import httpx

from llmeval.backends.base import BackendError, LLMBackend
from llmeval.config import BackendConfig


class OpenAICompatibleBackend:
    def __init__(
        self,
        *,
        base_url: str,
        model: str,
        api_key: str,
        timeout: float = 60.0,
    ) -> None:
        if not base_url.strip():
            raise ValueError("base_url is required")
        self.name = f"openai:{model}"
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key = api_key
        self.timeout = timeout

    def complete(self, prompt: str, *, temperature: float = 0.0) -> str:
        if not self.api_key:
            raise BackendError(
                "API key is empty. Set the environment variable named in the config."
            )
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "temperature": temperature,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a careful evaluation judge. Reply with JSON only.",
                },
                {"role": "user", "content": prompt},
            ],
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(url, headers=headers, json=payload)
                response.raise_for_status()
                body: dict[str, Any] = response.json()
        except httpx.HTTPError as exc:
            raise BackendError(f"backend request failed: {exc}") from exc
        except ValueError as exc:
            raise BackendError("backend did not return JSON") from exc
        return _message_text(body)


def _message_text(body: dict[str, Any]) -> str:
    try:
        content = body["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise BackendError("backend response is missing choices[0].message.content") from exc
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for part in content:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict) and part.get("type") == "text":
                parts.append(str(part.get("text", "")))
        if parts:
            return "".join(parts)
    raise BackendError("backend returned an unexpected message content")


def build_backend(config: BackendConfig) -> LLMBackend:
    if config.type == "mock":
        from llmeval.backends.mock import MockBackend

        return MockBackend(model=config.model)
    if config.type == "openai":
        api_key = os.environ.get(config.api_key_env, "")
        return OpenAICompatibleBackend(
            base_url=config.base_url,
            model=config.model,
            api_key=api_key,
            timeout=config.timeout_seconds,
        )
    raise ValueError(f"unknown backend type: {config.type}")
