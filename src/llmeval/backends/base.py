"""Backend interface. Anything with ``name`` and ``complete`` can be a judge."""

from __future__ import annotations

from typing import Protocol


class BackendError(RuntimeError):
    """The model could not be called, or the response was not usable."""


class LLMBackend(Protocol):
    name: str

    def complete(self, prompt: str, *, temperature: float = 0.0) -> str:
        """Return the model text for a single user prompt."""
