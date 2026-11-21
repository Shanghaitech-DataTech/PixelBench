"""Agent protocols, budgets and result types."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from pixelbench.core.canvas import PixelCanvas
from pixelbench.repl.kernel import KernelSession
from pixelbench.tasks.specs import TaskSpec


@dataclass
class Budget:
    max_steps: int = 40
    max_seconds: float = 600.0
    max_code_seconds: float = 120.0

    @classmethod
    def from_task(cls, spec: TaskSpec, fallback: "Budget" | None = None) -> "Budget":
        tb = spec.tool_budget or {}
        fb = fallback or cls()
        return cls(
            max_steps=int(tb.get("max_steps", fb.max_steps)),
            max_seconds=float(tb.get("max_seconds", fb.max_seconds)),
            max_code_seconds=float(tb.get("max_code_seconds", fb.max_code_seconds)),
        )


@dataclass
class AgentResult:
    ok: bool = True
    final_canvas: Optional[PixelCanvas] = None
    final_frames: List[PixelCanvas] = field(default_factory=list)
    transcript: List[Dict[str, Any]] = field(default_factory=list)
    error: Optional[str] = None
    steps_used: int = 0
    submission: Dict[str, Any] = field(default_factory=dict)
    usage: Optional[Dict[str, int]] = None  # cumulative token usage across LLM steps


class Agent(ABC):
    """One evaluatable model configuration."""

    name: str = "agent"
    requires_repl: bool = False

    @abstractmethod
    def run(self, task: TaskSpec, session: Optional[KernelSession], budget: Budget) -> AgentResult:
        """Run one episode.

        For REPL tasks the harness already injected the prelude into
        ``session`` (canvas, tools, reference/mask variables).
        ``final_canvas`` must be set on the result.
        """
