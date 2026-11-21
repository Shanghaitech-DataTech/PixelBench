"""The PixelBench creation protocol: budgets, time limits, and the rerun rule.

Budgets and limits
    A model may write or edit its program source at most 25 times on a generation task and 15 times on
    an editing task; running a program does not count. A single model request is cut after 75 minutes
    and a task after three hours; a cut episode keeps its intermediate result. Every program run is
    limited to 120 seconds and executes in the sandbox of ``pixelbench.repl.sandbox``.

Rerun rule
    * A failure of the serving infrastructure (a 5xx or 429 response, an exhausted quota, a dropped
      connection) says nothing about the model: the task is run again from the start until it completes.
    * When the model itself returned no artwork, was cut off by one of the time limits, or submitted only
      fully transparent frames, the task is rerun once with the same configuration, and the rerun counts.
    * Anything else is final.
"""
from __future__ import annotations

import re
from typing import Iterable, Optional, Sequence

WRITE_BUDGET = {"text2image": 25, "edit": 15}
REQUEST_LIMIT_S = 75 * 60
TASK_LIMIT_S = 3 * 60 * 60
PROGRAM_LIMIT_S = 120

COMPLETE = "complete"
MODEL_FAILURE = "model_failure"
INFRASTRUCTURE = "infrastructure"
FATAL = "fatal"  # the configuration itself is wrong (e.g. a rejected key): stop instead of rerunning

CUT_REASONS = ("long_request_cut", "episode_time_cut")
_STATUS = re.compile(r"(?:Error code|status(?:_code)?|HTTP)[:= ]+(\d{3})", re.I)
_INFRA_TEXT = ("connection", "timed out", "timeout", "temporarily", "overloaded", "rate limit", "quota",
               "insufficient", "exhausted", "unavailable", "bad gateway", "reset by peer", "remote end closed")


def write_budget(task_type: str) -> int:
    return WRITE_BUDGET["text2image" if task_type in ("agentic_creation", "text2image", "creation") else "edit"]


def _status(text: str) -> Optional[int]:
    m = _STATUS.search(text or "")
    return int(m.group(1)) if m else None


def is_infrastructure_error(error: Optional[str], retry_errors: Iterable[str] = ()) -> Optional[str]:
    """``INFRASTRUCTURE``, ``FATAL`` or None for the terminal error of an episode and its failed attempts."""
    texts = [t for t in (error, *retry_errors) if t]
    if not texts:
        return None
    statuses = [s for s in (_status(t) for t in texts) if s]
    if any(s in (401, 403) for s in statuses):
        return FATAL
    if any(s >= 500 or s in (402, 408, 409, 429) for s in statuses):
        return INFRASTRUCTURE
    low = " ".join(texts).lower()
    if any(k in low for k in _INFRA_TEXT):
        return INFRASTRUCTURE
    return None


def fully_transparent(frame) -> bool:
    """True when every pixel of a PixelCanvas (or a PIL image) has alpha 0."""
    if not hasattr(frame, "getchannel"):
        import io

        from PIL import Image
        frame = Image.open(io.BytesIO(frame.render_png_bytes(scale=1)))
    return frame.convert("RGBA").getchannel("A").getextrema()[1] == 0


def classify(termination: Optional[str], error: Optional[str], retry_errors: Iterable[str],
             frames: Sequence) -> str:
    """Outcome of one attempt at a task."""
    if termination == "llm_error":
        infra = is_infrastructure_error(error, retry_errors)
        if infra:
            return infra
    if termination in CUT_REASONS:
        return MODEL_FAILURE
    if not frames:
        return MODEL_FAILURE
    if all(fully_transparent(f) for f in frames):
        return MODEL_FAILURE
    return COMPLETE


def decide(outcomes: Sequence[str], max_infrastructure_reruns: int = 20) -> str:
    """What to do after the attempts so far: "rerun", "accept" (the last attempt is final) or "stop"."""
    if not outcomes:
        return "rerun"
    last = outcomes[-1]
    if last == FATAL:
        return "stop"
    if last == INFRASTRUCTURE:
        infra = sum(1 for o in outcomes if o == INFRASTRUCTURE)
        return "rerun" if infra <= max_infrastructure_reruns else "stop"
    model_attempts = [o for o in outcomes if o != INFRASTRUCTURE]
    if last == MODEL_FAILURE and len(model_attempts) == 1:
        return "rerun"  # one rerun, and the rerun counts
    return "accept"
