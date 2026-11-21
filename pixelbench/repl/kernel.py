"""Persistent ipykernel subprocess session.

Each benchmark episode owns one :class:`KernelSession`: a real Python
kernel launched as a subprocess (jupyter_client + ipykernel) that keeps
the canvas state alive across every ``run_code`` step.  The kernel
imports ``pixelbench`` via ``PYTHONPATH`` so the same code runs inside
and outside the sandbox.

If a kernel dies (the model runs something fatal), the harness decides
whether to restart it; the episode is marked failed otherwise.
"""
from __future__ import annotations

import base64
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from queue import Empty
from threading import Lock
from typing import Dict, List, Optional

import pixelbench

# --- fixed-port allocator -------------------------------------------------
# jupyter_client probes free ports before binding; under concurrent kernel
# startup two kernels can grab the same port (ZMQ "Address already in use").
# We hand out disjoint 5-port blocks per kernel to make concurrency safe.
_PORT_LOCK = Lock()
_PORT_BASE = 46000  # pick a range unlikely to collide with anything else
_PORT_NEXT = 0
_PORT_COUNT = 5  # shell, iopub, stdin, hb, control


def _alloc_ports() -> List[int]:
    global _PORT_NEXT
    with _PORT_LOCK:
        base = _PORT_BASE + _PORT_NEXT * _PORT_COUNT
        _PORT_NEXT += 1
        return list(range(base, base + _PORT_COUNT))

PACKAGE_ROOT = Path(pixelbench.__file__).resolve().parent.parent

# Length cap for a single step's stdout/stderr. None = no truncation: canvas views (e.g.
# color_as='char') must reach the model in full; a truncated observation forces the model
# to re-read it page by page, which wastes even more steps.
# To restore a cap, set this to an integer (e.g. 6000).
MAX_TEXT: Optional[int] = None
FINISH_SENTINEL = "PIXELBENCH_FINISHED"
FINAL_MARKER = "PIXELBENCH_FINAL:"


class KernelError(RuntimeError):
    pass


class KernelTimeout(KernelError):
    pass


class KernelDied(KernelError):
    pass


@dataclass
class KernelResult:
    """Outputs of one kernel execution."""

    ok: bool = True
    stdout: str = ""
    stderr: str = ""
    text: str = ""
    images: List[bytes] = field(default_factory=list)  # PNG bytes
    errors: List[dict] = field(default_factory=list)
    timed_out: bool = False
    submitted: Optional[bool] = None

    @property
    def finished(self) -> bool:
        return self.submitted if self.submitted is not None else FINISH_SENTINEL in self.stdout

    def combined(self) -> str:
        parts = []
        if self.stdout:
            parts.append(self.stdout.rstrip())
        if self.stderr:
            parts.append("STDERR:\n" + self.stderr.rstrip())
        for e in self.errors:
            parts.append(f"{e.get('ename','Error')}: {e.get('evalue','')}")
        return "\n".join(parts)

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "text": self.text,
            "n_images": len(self.images),
            "errors": self.errors,
            "timed_out": self.timed_out,
            "finished": self.finished,
        }


def _truncate(s: str, limit: Optional[int] = None) -> str:
    """Length cap. The default None means no truncation (see the note on MAX_TEXT)."""
    if limit is None:
        limit = MAX_TEXT
    if limit is None or len(s) <= limit:
        return s
    return s[:limit] + f"\n...[truncated {len(s) - limit} chars]"


class KernelSession:
    def __init__(
        self,
        kernel_name: str = "pixelbench",
        cwd: Optional[str] = None,
        pythonpath_extra: Optional[List[str]] = None,
        env: Optional[Dict[str, str]] = None,
    ) -> None:
        self.kernel_name = kernel_name
        self.cwd = cwd
        self.pythonpath_extra = pythonpath_extra or []
        self.env = env or {}
        self.km = None
        self.kc = None
        self._started = False
        import tempfile
        self.checkpoint_path = Path(tempfile.mkdtemp(prefix='pixelbench-checkpoint-')) / 'workspace.json'

    # -- lifecycle -----------------------------------------------------
    def _ensure_kernelspec(self) -> None:
        try:
            from jupyter_client.kernelspec import KernelSpecManager

            ksm = KernelSpecManager()
            if self.kernel_name in ksm.find_kernel_specs():
                return
        except Exception:
            pass
        try:
            from ipykernel.kernelspec import install

            install(user=True, kernel_name=self.kernel_name, display_name=f"PixelBench ({self.kernel_name})")
        except Exception as e:  # pragma: no cover
            raise KernelError(f"could not register kernelspec {self.kernel_name!r}: {e}")

    def start(self, timeout: float = 60.0) -> None:
        if self._started:
            return
        self._ensure_kernelspec()
        env = dict(os.environ)
        paths = [str(PACKAGE_ROOT)] + [str(p) for p in self.pythonpath_extra]
        if env.get("PYTHONPATH"):
            paths.append(env["PYTHONPATH"])
        env["PYTHONPATH"] = os.pathsep.join(paths)
        env.update(self.env)
        env['PIXELBENCH_CHECKPOINT'] = str(self.checkpoint_path)
        self.checkpoint_path.unlink(missing_ok=True)

        from jupyter_client import KernelManager

        self.km = KernelManager(kernel_name=self.kernel_name)
        ports = _alloc_ports()
        self.km.shell_port, self.km.iopub_port = ports[0], ports[1]
        self.km.stdin_port, self.km.hb_port = ports[2], ports[3]
        self.km.control_port = ports[4]
        try:
            self.km.start_kernel(cwd=self.cwd, env=env)
        except Exception as e:  # pragma: no cover
            self.km = None
            raise KernelError(f"failed to start kernel {self.kernel_name!r}: {e}")
        self.kc = self.km.client()
        self.kc.start_channels()
        try:
            self.kc.wait_for_ready(timeout=timeout)
        except Exception as e:  # pragma: no cover
            self.shutdown()
            raise KernelError(f"kernel did not become ready: {e}")
        self._started = True
        # warm import so failures surface early
        r = self.execute("import pixelbench, numpy, PIL", timeout=30.0)
        if not r.ok:
            self.shutdown()
            raise KernelError(
                "kernel cannot import pixelbench: " + (r.combined() or "unknown error")
            )

    def is_alive(self) -> bool:
        return self._started and self.km is not None and self.km.is_alive()

    def restart(self, timeout: float = 60.0) -> None:
        self.shutdown()
        self.start(timeout=timeout)

    def shutdown(self) -> None:
        self._started = False
        if self.kc is not None:
            try:
                self.kc.stop_channels()
            except Exception:
                pass
            self.kc = None
        if self.km is not None:
            try:
                self.km.shutdown_kernel(now=True)
            except Exception:
                try:
                    self.km.cleanup_resources()
                except Exception:
                    pass
            self.km = None

    # -- execution ------------------------------------------------------
    def execute(self, code: str, timeout: float = 120.0, truncate: bool = True) -> KernelResult:
        if not self.is_alive():
            raise KernelDied("kernel is not running")
        # Reject incomplete Python without executing it (clearer than a SyntaxError).
        #
        # But in interactive mode IPython's is_complete() only accepts a **compound statement
        # followed by a blank line**: `for y in range(h):\n    paint(...)` counts as incomplete
        # until a blank line is added. Models most naturally end drawing code with exactly such
        # a loop (paint_region row by row); such code used to be rejected as "incomplete", so
        # models kept retrying or fell back to analysis (in one run the capybara task was
        # rejected 9 times). So first try appending a newline, and report an error only if the
        # code is still incomplete (the body really is missing).
        if self._code_is_incomplete(code):
            if not self._code_is_incomplete(code + "\n"):
                code = code + "\n"
            else:
                res = KernelResult(ok=False)
                res.errors.append(
                    {
                        "ename": "IncompleteCode",
                        "evalue": (
                            "the submitted code is incomplete Python; send a complete code "
                            "block (if it ends with a for/if/def block, close the block with a "
                            "blank line)"
                        ),
                        "traceback": [],
                    }
                )
                return res
        try:
            msg_id = self.kc.execute(code, allow_stdin=False)
        except Exception as e:  # pragma: no cover
            raise KernelDied(f"failed to send code to kernel: {e}")
        return self._collect(msg_id, timeout, truncate=truncate)

    def _code_is_incomplete(self, code: str) -> bool:
        """Ask the kernel whether ``code`` is complete; returns True for
        incomplete blocks (a trailing ``for x in y:`` etc.)."""
        try:
            req_id = self.kc.is_complete(code)
            deadline = time.monotonic() + 10.0
            while time.monotonic() < deadline:
                reply = self.kc.get_shell_msg(timeout=1.0)
                if reply.get("parent_header", {}).get("msg_id") == req_id:
                    return reply.get("content", {}).get("status") == "incomplete"
        except Exception:  # pragma: no cover - kernel or channel issues
            pass
        return False

    def execute_checked(self, code: str, timeout: float = 120.0, what: str = "code", truncate: bool = True) -> KernelResult:
        r = self.execute(code, timeout=timeout, truncate=truncate)
        if not r.ok:
            raise KernelError(f"kernel execution failed during {what}:\n{r.combined()}")
        return r

    def _collect(self, msg_id: str, timeout: float, truncate: bool = True) -> KernelResult:
        res = KernelResult()
        deadline = time.monotonic() + timeout

        def _remaining() -> float:
            return deadline - time.monotonic()

        # 1) wait for the shell (execute_reply) message — catches
        #    'incomplete' / 'aborted' states that never emit iopub output.
        shell = None
        while True:
            if _remaining() <= 0:
                res.timed_out = True
                res.ok = False
                return res
            try:
                shell = self.kc.get_shell_msg(timeout=min(_remaining(), 5.0))
                break
            except Empty:
                if not self.is_alive():
                    raise KernelDied("kernel process died during execution")
                continue
            except Exception:  # pragma: no cover
                raise KernelDied("error while reading kernel messages")

        status = (shell.get("content") or {}).get("status", "ok")
        if status == "incomplete":
            res.ok = False
            res.errors.append(
                {
                    "ename": "IncompleteCode",
                    "evalue": "the submitted code is incomplete Python; send a complete code block",
                    "traceback": [],
                }
            )
            return res
        if status == "aborted":
            res.ok = False
            res.errors.append({"ename": "Aborted", "evalue": "execution aborted", "traceback": []})
            return res

        # 2) drain iopub messages until the idle status
        while True:
            if _remaining() <= 0:
                res.timed_out = True
                res.ok = False
                return res
            try:
                msg = self.kc.get_iopub_msg(timeout=min(_remaining(), 5.0))
            except Empty:
                if not self.is_alive():
                    raise KernelDied("kernel process died during execution")
                continue
            except Exception:  # pragma: no cover
                raise KernelDied("error while reading kernel messages")
            if msg.get("parent_header", {}).get("msg_id") != msg_id:
                continue
            mtype = msg.get("msg_type", "")
            content = msg.get("content", {})
            if mtype == "status":
                if content.get("execution_state") == "idle":
                    break
            elif mtype == "stream":
                text = content.get("text", "")
                if content.get("name") == "stderr":
                    res.stderr += text
                else:
                    res.stdout += text
            elif mtype in ("display_data", "execute_result"):
                data = content.get("data", {})
                if "text/plain" in data:
                    res.text += data["text/plain"] + "\n"
                if "image/png" in data:
                    # the Jupyter protocol delivers image/png as base64 text
                    res.images.append(base64.b64decode(data["image/png"]))
            elif mtype == "error":
                res.errors.append(
                    {
                        "ename": content.get("ename", "Error"),
                        "evalue": content.get("evalue", ""),
                        "traceback": content.get("traceback", []),
                    }
                )
        if status == "error" and not res.errors:
            res.errors.append(
                {"ename": "Error", "evalue": "execution failed (see traceback)", "traceback": []}
            )
        # The durable submission record is authoritative; stdout alone is not a submission.
        if self.checkpoint_path.is_file():
            try:
                import json
                checkpoint = json.loads(self.checkpoint_path.read_text())
                res.submitted = checkpoint.get('submission', {}).get('source') == 'explicit'
            except (OSError, ValueError):
                res.submitted = False
        res.ok = not res.errors and not res.timed_out
        if truncate:
            res.stdout = _truncate(res.stdout)
            res.stderr = _truncate(res.stderr)
            res.text = _truncate(res.text)
        return res

    # -- convenience ----------------------------------------------------
    def extract_submission(self, timeout: float = 30.0):
        """One extraction path for explicit submissions and unfinished-work recovery.

        A dead kernel uses the last atomic, per-cell checkpoint. No GT is consulted.
        """
        import json
        from pixelbench.core.canvas import PixelCanvas
        payload = None
        error = None
        if self.is_alive():
            try:
                self.execute("_pb_obs_set_active(False)", timeout=10.0)
                code = f"import json; print('{FINAL_MARKER}' + json.dumps(_pb_submission.extract()))"
                r = self.execute_checked(code, timeout=timeout, what='submission extraction', truncate=False)
                for line in r.stdout.splitlines():
                    if line.startswith(FINAL_MARKER):
                        payload = json.loads(line[len(FINAL_MARKER):])
                        break
            except Exception as exc:
                error = str(exc)
        if payload is None and self.checkpoint_path.is_file():
            payload = json.loads(self.checkpoint_path.read_text())
            payload['submission']['checkpoint_recovery'] = True
            if error:
                payload['submission']['extraction_error'] = error
        if payload is None:
            raise KernelError('no submission or workspace checkpoint available')
        return [PixelCanvas.from_dict(row) for row in payload['outputs']], payload['submission']

    def extract_final_canvas(self, timeout: float = 30.0):
        """Compatibility accessor for old report consumers; never selects a canvas."""
        outputs, _ = self.extract_submission(timeout)
        return outputs[-1] if outputs else None

    def extract_final_frames(self, timeout: float = 30.0):
        return self.extract_submission(timeout)[0]
