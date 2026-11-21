"""Benchmark run configuration (JSON)."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from pixelbench.tasks.specs import TaskSpec, load_tasks_from_dir


_ENV_LOADED = False


def _load_repo_env() -> None:
    """Load the repo-root ``.env`` once (same behaviour as ``webapp/server.py``).

    The CLI has always advertised ``.env`` as the place real-model keys come
    from, but only the web app actually loaded it — so a config using
    ``"api_key": "${PIXELBENCH_API_KEY}"`` resolved to an empty string under
    ``python -m pixelbench run``, and :class:`LLMClient` then sent the
    placeholder ``"not-needed"`` as the key (surfacing as
    ``401 Authentication Fails, Your api key: ****eded is invalid``).
    """
    global _ENV_LOADED
    if _ENV_LOADED:
        return
    _ENV_LOADED = True
    try:  # dotenv is optional
        from dotenv import load_dotenv

        load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=False)
    except Exception:  # pragma: no cover - dotenv missing
        pass


def _interpolate_env(obj: Any) -> Any:
    """Replace ``${ENV_VAR}`` string values with their environment value.

    Lets configs carry API keys without hardcoding them, e.g.
    ``"api_key": "${PIXELBENCH_API_KEY}"``.
    """
    _load_repo_env()
    if isinstance(obj, dict):
        return {k: _interpolate_env(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_interpolate_env(v) for v in obj]
    if isinstance(obj, str) and obj.startswith("${") and obj.endswith("}"):
        return os.environ.get(obj[2:-1], "")
    return obj

DEFAULT_CONFIG: Dict[str, Any] = {
    "tasks": "smoke",
    "agents": [{"type": "mock-repl", "name": "mock-repl"}],
    "judge": {"type": "mock"},
    "out_dir": "outputs",
    "seed": 0,
    "observe": True,
}


@dataclass
class BenchmarkConfig:
    tasks: Any = "smoke"  # "smoke" | {"types": [...]} | path to task dir
    agents: List[dict] = field(default_factory=lambda: [{"type": "mock-repl", "name": "mock-repl"}])
    judge: dict = field(default_factory=lambda: {"type": "mock"})
    out_dir: str = "outputs"
    seed: int = 0
    max_tasks: Optional[int] = None
    observe: bool = True  # record the painting process (frames/diffs + viewer)

    def to_dict(self) -> dict:
        return {
            "tasks": self.tasks,
            "agents": self.agents,
            "judge": self.judge,
            "out_dir": self.out_dir,
            "seed": self.seed,
            "max_tasks": self.max_tasks,
            "observe": self.observe,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "BenchmarkConfig":
        d = _interpolate_env(d)
        return cls(
            tasks=d.get("tasks", "smoke"),
            agents=[dict(a) for a in d.get("agents", [{"type": "mock-repl", "name": "mock-repl"}])],
            judge=dict(d.get("judge", {"type": "mock"})),
            out_dir=d.get("out_dir", "outputs"),
            seed=int(d.get("seed", 0)),
            max_tasks=d.get("max_tasks"),
            observe=bool(d.get("observe", True)),
        )

    @classmethod
    def from_json(cls, path: str) -> "BenchmarkConfig":
        return cls.from_dict(json.loads(Path(path).read_text()))

    def load_tasks(self) -> List[TaskSpec]:
        t = self.tasks
        if isinstance(t, str) and t == "smoke":
            from pixelbench.tasks.smoke import smoke_tasks

            specs = smoke_tasks()
        elif isinstance(t, str):
            specs = load_tasks_from_dir(t)
        elif isinstance(t, dict):
            from pixelbench.tasks.smoke import smoke_tasks

            specs = smoke_tasks()
            types = set(t.get("types", []))
            sizes = set(t.get("sizes", []))
            if types or sizes:
                specs = [
                    s
                    for s in specs
                    if (not types or s.task_type in types) and (not sizes or s.width in sizes or s.height in sizes)
                ]
        else:
            raise ValueError(f"cannot interpret tasks config {t!r}")
        if self.max_tasks:
            specs = specs[: self.max_tasks]
        return specs
