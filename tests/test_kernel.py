import pytest

from pixelbench.repl.kernel import KernelDied, KernelError, KernelSession

pytest.importorskip("ipykernel")


def test_kernel_start_execute_state_persistence(kernel):
    r = kernel.execute("x = 41", timeout=30)
    assert r.ok
    r = kernel.execute("x + 1", timeout=30)
    assert r.ok
    assert "42" in r.stdout or "42" in r.text


def test_kernel_captures_stdout_and_images(kernel):
    code = (
        "import pixelbench as pb\n"
        "c = pb.PixelCanvas(8, 8)\n"
        "c.register_color('red', '#e0455a')\n"
        "c.paint_circle(4, 4, 3, 'red')\n"
        "print('hello from kernel')\n"
        "c.render(scale=4)\n"
    )
    r = kernel.execute(code, timeout=60)
    assert r.ok
    assert "hello from kernel" in r.stdout
    assert len(r.images) == 1
    assert r.images[0][:8] == b"\x89PNG\r\n\x1a\n"


def test_kernel_error_capture(kernel):
    r = kernel.execute("raise ValueError('boom')", timeout=30)
    assert not r.ok
    assert any(e["ename"] == "ValueError" for e in r.errors)
    assert "boom" in r.combined()


def test_kernel_incomplete_code(kernel):
    r = kernel.execute("for i in range(3):", timeout=30)
    assert not r.ok
    assert any(e["ename"] == "IncompleteCode" for e in r.errors)


def test_kernel_stderr_capture(kernel):
    r = kernel.execute("import sys; print('warn', file=sys.stderr)", timeout=30)
    assert r.ok
    assert "warn" in r.stderr


def test_execute_accepts_code_ending_with_compound_block(kernel):
    """Code that ends with a for/if block must run.

    In interactive mode IPython's is_complete() wants a blank line after a compound statement, so
    `for y in range(h):\n    paint_region(...)` (the natural way to paint row by row) would be judged
    incomplete and dropped. Contract: code that compiles once a newline is appended is executed.
    """
    r = kernel.execute("acc = 0\nfor i in range(3):\n    acc += i", timeout=30)
    assert r.ok, r.combined()
    assert kernel.execute("print(acc)", timeout=30).stdout.strip() == "3"


def test_execute_still_rejects_truly_incomplete_code(kernel):
    r = kernel.execute("for i in range(3):", timeout=30)
    assert not r.ok
    assert any(e.get("ename") == "IncompleteCode" for e in (r.errors or []))


def test_kernel_stdout_not_truncated_by_default(kernel):
    """No truncation by default: a whole canvas view (256x256, about 68k characters) must reach the model.

    A truncated observation forces the model to page through it, so ``kernel.MAX_TEXT`` defaults to None;
    pass a limit explicitly when one is needed.
    """
    r = kernel.execute("print('x' * 20000)", timeout=30)
    assert r.ok
    assert len(r.stdout) >= 20000
    assert "truncated" not in r.stdout


def test_kernel_truncate_opt_in():
    """A length limit can still be requested explicitly (see kernel._truncate)."""
    from pixelbench.repl.kernel import _truncate

    s = _truncate("x" * 20000, 5000)
    assert len(s) < 20000
    assert "truncated" in s


def test_extract_final_canvas(kernel):
    from pixelbench.repl.prelude import build_prelude
    from pixelbench.tasks.specs import TaskSpec
    task = TaskSpec('extract', 'agentic_creation', '', 24, 24)
    assert kernel.execute(build_prelude(task.public_task(), task.initial_state())).ok
    code = (
        "import pixelbench as pb\n"
        "result=input_canvas.copy()\nresult.color('#e0455a',name='red')\n"
        "result.rect(0, 0, 6, 6, 'red')\nfinish(result)\n"
    )
    assert kernel.execute(code, timeout=30).ok
    c = kernel.extract_final_canvas()
    assert c.width == 24 and c.height == 24
    assert c.matrix[3, 3] == c.palette._resolve_id("red")


def test_kernel_dead_raises(kernel):
    with pytest.raises(KernelDied):
        kernel.execute("import os; os._exit(1)", timeout=30)
    assert not kernel.is_alive()


def test_kernel_restart(kernel):
    kernel.execute("x = 5", timeout=30)
    kernel.restart(timeout=60)
    r = kernel.execute("x", timeout=30)
    assert not r.ok  # state gone
