"""Shared pytest fixtures and fake LLM."""
from __future__ import annotations

import base64
import copy
import json
from types import SimpleNamespace
from typing import Any, Dict, List, Optional

import pytest

from pixelbench.repl.kernel import KernelSession


@pytest.fixture(scope="function")
def kernel():
    """A fresh, ready kernel per test (module-scope would be faster but
    leak state between tests)."""
    s = KernelSession()
    s.start(timeout=90)
    yield s
    s.shutdown()


class FakeMessage:
    def __init__(self, content: Optional[str] = None, tool_calls: Optional[List[dict]] = None) -> None:
        self.content = content
        self.tool_calls = tool_calls


class FakeLLM:
    """Scripted chat-completions fake.

    ``script`` is a list of callables ``(messages, tools) -> FakeMessage``
    consumed one per chat() call.  All calls are recorded on
    ``self.calls`` so tests can assert on the conversation history
    (including injected images).
    """

    def __init__(self, script: List[Any]) -> None:
        self.script = list(script)
        self.calls: List[dict] = []
        self.model = "fake-llm"

    def chat(self, messages, tools=None, response_format=None):
        # deep-copy: the agent mutates the message list in place after the call
        self.calls.append(
            {
                "messages": copy.deepcopy(messages),
                "tools": copy.deepcopy(tools),
                "response_format": response_format,
            }
        )
        if not self.script:
            return SimpleNamespace(choices=[SimpleNamespace(message=FakeMessage(content="done"))])
        step = self.script.pop(0)
        msg = step(messages, tools) if callable(step) else step
        return SimpleNamespace(choices=[SimpleNamespace(message=msg)])


def tool_call(id_: str, name: str, arguments: dict) -> dict:
    return {"id": id_, "type": "function", "function": {"name": name, "arguments": json.dumps(arguments)}}


def message_has_image(messages: List[dict]) -> bool:
    for m in messages:
        content = m.get("content")
        if isinstance(content, list):
            for part in content:
                if isinstance(part, dict) and part.get("type") == "image_url":
                    return True
    return False


def image_url_parts(messages: List[dict]) -> int:
    n = 0
    for m in messages:
        content = m.get("content")
        if isinstance(content, list):
            n += sum(1 for p in content if isinstance(p, dict) and p.get("type") == "image_url")
    return n
