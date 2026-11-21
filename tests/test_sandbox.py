"""Model programs run in the sandbox by default: no files outside the run directory, no network, no exec."""
import pytest

from pixelbench.repl import sandbox
from pixelbench.repl.file_session import FileSession
from pixelbench.repl.prelude import build_prelude
from pixelbench.tasks.specs import TaskSpec

pytestmark = pytest.mark.skipif(sandbox.landlock_abi() < 1, reason="Landlock is not available on this kernel")

PROBE = """
import os, socket, subprocess
results = {}
try:
    open(SECRET).read(); results['read_outside'] = 'allowed'
except OSError:
    results['read_outside'] = 'denied'
try:
    socket.socket(socket.AF_INET, socket.SOCK_STREAM); results['socket'] = 'allowed'
except OSError:
    results['socket'] = 'denied'
try:
    subprocess.run(['true'], check=False); results['exec'] = 'allowed'
except OSError:
    results['exec'] = 'denied'
print(results)
finish(new_canvas(4, 4).set(0, 0, '#f00'))
"""


def run_probe(tmp_path, sandboxed):
    secret = tmp_path / "secret.txt"
    secret.write_text("hidden")
    task = TaskSpec("probe", "agentic_creation", "draw", 4, 4)
    session = FileSession(tmp_path / "runs", sandbox=sandboxed)
    session.execute_checked(build_prelude(task.public_task(), task.initial_state()), what="prelude")
    session.write_file("main.py", f"SECRET = {str(secret)!r}\n" + PROBE)
    result = session.run("main.py", submit=True)
    assert result.ok, result.combined()
    return result.stdout


def test_sandbox_is_on_by_default(tmp_path):
    out = run_probe(tmp_path, sandboxed=True)
    assert "'read_outside': 'denied'" in out
    assert "'socket': 'denied'" in out
    assert "'exec': 'denied'" in out


def test_explicit_opt_out(tmp_path):
    out = run_probe(tmp_path, sandboxed=False)
    assert "'read_outside': 'allowed'" in out
