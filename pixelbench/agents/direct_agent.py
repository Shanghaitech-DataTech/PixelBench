"""File-driven generation restricted to full-matrix redraw(canvas, rows)."""
from __future__ import annotations

from typing import Optional

from pixelbench.agents.chat import LLMClient
from pixelbench.agents.repl_agent import REDRAW_SYSTEM_PROMPT, REPLAgent

SYSTEM_PROMPT = REDRAW_SYSTEM_PROMPT


class DirectGenAgent(REPLAgent):
    """A REPL agent restricted to full-canvas redraws.

    A one-shot generation is just this agent finishing after a single
    redraw round; nothing is lost by unifying with the REPL loop.
    """

    def __init__(
        self,
        name: str = "direct",
        llm: Optional[LLMClient] = None,
        system_prompt: Optional[str] = None,
        vision: bool = True,
        max_steps: Optional[int] = None,
    ) -> None:
        super().__init__(
            name=name,
            llm=llm,
            system_prompt=system_prompt,
            vision=vision,
            max_steps=max_steps,
            surface="redraw",
        )
