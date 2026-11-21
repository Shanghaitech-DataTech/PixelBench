"""Deterministic mock agents for tests and the demo run.

These agents exercise the full harness (kernel, prelude, tools, metrics,
judge) without any LLM, so tests are fast, offline and reproducible.
"""
from __future__ import annotations

from typing import List, Optional

from pixelbench.agents.base import Agent, AgentResult, Budget
from pixelbench.core.canvas import PixelCanvas
from pixelbench.repl.kernel import KernelSession
from pixelbench.tasks.generators import AssetLibrary
from pixelbench.tasks.specs import TaskSpec


def default_demo_script(task: TaskSpec) -> List[str]:
    """A small deterministic drawing script that works on any canvas.

    Each element is one complete Python cell (multiline strings are
    allowed) so it can be executed as-is by the kernel.
    """
    n = max(1, task.num_frames or 1)
    if task.task_type == 'replication':
        return ["result = reference.copy(name='result')\nview(result)\nfinish(result)"]
    if task.frames_visible and task.frames:
        return ["results = [c.copy() for c in reference_frames]\nfinish(results)"]
    start = "result = input_canvas.copy(name='result')\n"
    if task.task_type == 'restoration':
        code = start + "for y, x in zip(*np.where(mask)):\n    result.set(int(x), int(y), '#8a8a8a')\n"
    elif task.task_type == 'edit':
        code = start + "used = [v for v in result.px if result.pal.rgba(v)[3]]\nif used:\n    target = max(set(used), key=used.count)\n    new = result.color('#39398a')\n    result.px[:] = [new if v == target else v for v in result.px]\n"
    else:
        code = start + "result.rect(1,1,max(1,result.w-2),max(1,result.h-2),'#e0455a')\n"
    code += "view(result)\n"
    code += "finish(result)" if n == 1 else f"results = [result.copy(name=f'frame{{i+1}}') for i in range({n})]\nfinish(results)"
    return [code]


class MockREPLAgent(Agent):
    """Executes a fixed Python script in the session (no LLM)."""

    requires_repl = True

    def __init__(self, name: str = "mock-repl", script: Optional[List[str]] = None) -> None:
        self.name = name
        self.script = script

    def run(self, task: TaskSpec, session: Optional[KernelSession], budget: Budget) -> AgentResult:
        if session is None:
            return AgentResult(ok=False, error="MockREPLAgent requires a kernel session")
        script = self.script if self.script is not None else default_demo_script(task)
        transcript = []
        ok = True
        error = None
        if hasattr(session, 'write_file'):
            session.write_file('main.py', '\n'.join(script))
            r = session.run('main.py', submit=True, timeout=budget.max_code_seconds)
            outputs, submission = session.extract_submission()
            return AgentResult(ok=r.ok and bool(outputs), final_canvas=outputs[-1] if outputs else None,
                               final_frames=outputs, submission=submission,
                               transcript=[{'kind': 'code', 'code': '\n'.join(script), 'output': r.to_dict()}],
                               error=None if r.ok else r.combined(), steps_used=1)
        for i, code in enumerate(script):
            r = session.execute(code, timeout=budget.max_code_seconds)
            transcript.append({"step": i, "kind": "code", "code": code, "output": r.to_dict()})
            if not r.ok:
                ok = False
                error = r.combined() or "script step failed"
                break
            if r.finished:
                break
        try:
            outputs, submission = session.extract_submission()
        except Exception as e:
            outputs, submission = [], {'source': 'missing'}
            ok, error = False, str(e)
        return AgentResult(ok=ok and bool(outputs), final_canvas=outputs[-1] if outputs else None,
                           final_frames=outputs, submission=submission, transcript=transcript,
                           error=error, steps_used=len(transcript))


class MockDirectAgent(Agent):
    """Returns a library-generated pixel art (no LLM)."""

    requires_repl = False

    def __init__(self, name: str = "mock-direct", fallback_kind: str = "heart") -> None:
        self.name = name
        self.fallback_kind = fallback_kind
        self.lib = AssetLibrary(seed=0)

    def run(self, task: TaskSpec, session: Optional[KernelSession], budget: Budget) -> AgentResult:
        kind = task.metadata.get("asset") or self.fallback_kind
        try:
            canvas = self.lib.generate(kind, task.width, task.height, seed=hash(task.id) % 1000)
        except ValueError:
            canvas = self.lib.generate(self.fallback_kind, task.width, task.height)
        return AgentResult(
            ok=True,
            final_canvas=canvas,
            transcript=[{"kind": "direct", "asset": kind}],
            steps_used=1,
        )
