"""Build the setup code injected into a fresh kernel per episode.

The prelude reconstructs the canvas (and, depending on the task,
reference / mask objects) from JSON, creates the :class:`SessionTools`
and binds every tool as a top-level function so the model can write
short, natural drawing code.
"""
from __future__ import annotations

import json
from typing import Any, Dict, Optional


def _embed(obj: Any) -> str:
    """Embed a JSON-serializable object as a valid Python literal in code.

    The literal is emitted multi-line (one element per line) on purpose:
    ipykernel/IPython crashes on a single line that is very long (a
    ~200KB+ one-line dict literal kills the kernel during AST handling),
    while the same content split across many short lines runs fine.
    ``repr``-based output is valid Python for JSON-native types; we keep
    bools as ``True``/``False`` to stay valid Python (json.dumps emits
    ``true``/``false`` which is *not* valid Python).
    """
    import json as _json

    _json.dumps(obj)  # validate JSON-serializability
    if isinstance(obj, dict):
        parts = ["{"]
        for k, v in obj.items():
            parts.append(f"{k!r}: {_embed(v)},")
        parts.append("}")
        return "\n".join(parts)
    if isinstance(obj, list):
        parts = ["["]
        for v in obj:
            parts.append(f"{_embed(v)},")
        parts.append("]")
        return "\n".join(parts)
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return repr(obj)
    raise TypeError(f"cannot embed {type(obj).__name__}")


def build_prelude(
    task: Dict[str, Any],
    initial_state: Dict[str, Any],
    reference_state: Optional[Dict[str, Any]] = None,
    mask_state: Optional[Dict[str, Any]] = None,
    frames_state: Optional[List[Dict[str, Any]]] = None,
    seed: int = 0,
    observer_dir: Optional[str] = None,
    surface: str = "full",
    look_budget: Optional[int] = None,
) -> str:
    """Return the setup code string for one episode kernel.

    ``observer_dir`` (optional): when given, the drawing process is
    observed at call granularity (per tool call diff images) and turn
    granularity (per executed block canvas frames); see
    :mod:`pixelbench.repl.observer`.  The harness disarms the observer
    before extraction with ``_pb_obs_set_active(False)``.

    ``surface``: which tool surface to bind as top-level names — ``"full"``
    (all tools) or ``"redraw"`` (only full-canvas redraw + palette +
    full-canvas observation; see :data:`pixelbench.repl.tools.SURFACES`).
    """
    if surface not in ('full', 'redraw'):
        raise ValueError(f'unknown tool surface {surface!r}')
    return "\n".join([
        "from pixelbench.repl.skill_runtime import install as _pb_install_skill",
        f"_task = {_embed(dict(task, surface=surface))}",
        f"_initial = {_embed(initial_state)}",
        f"_mask_state = {_embed(mask_state)}",
        f"_visible_reference = {_embed(reference_state if task.get('task_type') != 'restoration' else None)}",
        f"_visible_frames = {_embed(frames_state if task.get('frames_visible') else None)}",
        f"_pb_install_skill(globals(), _task, _initial, _mask_state, {_embed(observer_dir)}, {_embed(look_budget)}, _visible_reference, _visible_frames)",
        f"np.random.seed({int(seed)})",
        f"import random; random.seed({int(seed)})",
    ])


def finalize_snippet() -> str:
    from pixelbench.repl.kernel import FINAL_MARKER
    return f"import json; print('{FINAL_MARKER}' + json.dumps(_pb_submission.extract()))"
