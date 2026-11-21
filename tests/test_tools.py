import pytest

from pixelbench.repl.kernel import FINISH_SENTINEL
from pixelbench.repl.prelude import build_prelude
from pixelbench.tasks.smoke import smoke_tasks

pytest.importorskip("ipykernel")


def _agentic_task():
    return smoke_tasks()[2]  # agentic_0001 (32x32 mushroom)


def _replication_task():
    return smoke_tasks()[4]  # replicate_0001 (potion)


def _restoration_task():
    return smoke_tasks()[6]  # restore_0001 (chest)


def _run_prelude(kernel, task, ref_visible=False, mask=False):
    code = build_prelude(
        task=task.public_task(),
        initial_state=task.initial_state(),
        reference_state=task.reference_state() if ref_visible else None,
        mask_state=task.mask_state() if mask else None,
        seed=0,
    )
    r = kernel.execute(code, timeout=60)
    assert r.ok, r.combined()
    return r


def test_prelude_agentic(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    r = kernel.execute("input_canvas.stats_text()", timeout=30)
    assert r.ok
    assert "32x32" in (r.stdout + r.text)
    # tools bound as top-level functions
    r = kernel.execute("print(callable(input_canvas.color), callable(view), callable(input_canvas.select))", timeout=30)
    assert "True True True" in r.stdout


def test_register_color_returns_id(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    r = kernel.execute("cid = input_canvas.color('#3f9b4f',name='leaf'); print(cid)", timeout=30)
    assert r.ok
    assert "1" in r.stdout


def test_render_produces_image(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    r = kernel.execute("view(input_canvas,scale=8)", timeout=30)
    assert r.ok
    assert len(r.images) == 1


def test_observe_region_image_mode(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    r = kernel.execute("input_canvas.rect(0,0,8,8,'#f00')\nview(input_canvas.select(0,0,8,8).preview())", timeout=30)
    assert r.ok
    assert len(r.images) == 1



def test_finish_sentinel(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    r = kernel.execute("finish(input_canvas)", timeout=30)
    assert r.ok
    assert FINISH_SENTINEL in r.stdout


def test_replication_reference_available(kernel):
    t = _replication_task()
    _run_prelude(kernel, t, ref_visible=True)
    r = kernel.execute("print(reference is not None, callable(reference.matrix_text))", timeout=30)
    assert "True True" in r.stdout
    # Viewing a reference is explicit, like every other canvas.
    assert len(kernel.execute("view(reference)").images) == 1
    # no official diff tool
    r = kernel.execute("print('compare_to_reference' in globals())", timeout=30)
    assert "False" in r.stdout


def test_restoration_mask_available(kernel):
    t = _restoration_task()
    _run_prelude(kernel, t, mask=True)
    r = kernel.execute("import numpy as np; print(mask.dtype, mask.shape)", timeout=30)
    assert "bool" in r.stdout and "(32, 32)" in r.stdout
    # reference must NOT be visible for restoration
    r = kernel.execute("print(reference is None)", timeout=30)
    assert "True" in r.stdout


def test_tools_help_removed(kernel):
    # the in-kernel help()/help_pixelbench surface was removed: tool docs
    # now live in the run_code description (see tool_docs() in tools.py)
    t = _agentic_task()
    _run_prelude(kernel, t)
    r = kernel.execute("print('tools' in globals(), 'help_pixelbench' in globals())", timeout=30)
    assert r.ok
    assert "False False" in r.stdout


def test_implicit_observation_tools_removed(kernel):
    _run_prelude(kernel, _agentic_task())
    r = kernel.execute("print('render' in globals(), 'observe_canvas' in globals())")
    assert r.ok and 'False False' in r.stdout


def _run_legacy_data_tools(kernel):
    # The old standalone data helpers remain usable via explicit construction,
    # but are deliberately absent from the agent prelude.
    result = kernel.execute("""
from pixelbench.core.canvas import PixelCanvas
from pixelbench.repl.tools import SessionTools, SURFACES
canvas = PixelCanvas(32,32)
tools = SessionTools(canvas)
for name in SURFACES['full']:
    globals()[name] = getattr(tools,name)
""")
    assert result.ok, result.combined()


def test_mix_shade_color_tools(kernel):
    t = _agentic_task()
    _run_legacy_data_tools(kernel)
    r = kernel.execute(
        "red = register_color('red', '#ff0000')\n"
        "blue = register_color('blue', '#0000ff')\n"
        "mid = mix_colors('purple', red, blue, 0.5)\n"
        "print('mid', mid, canvas.palette[mid].to_hex())\n"
        "light = shade_color('pink', red, 0.5)\n"
        "dark = shade_color('darkred', red, -0.5)\n"
        "print('shades', light, dark, canvas.palette[light].to_hex(), canvas.palette[dark].to_hex())\n",
        timeout=60,
    )
    assert r.ok, r.combined()
    # #ff0000 mixed with #0000ff at t=0.5 -> #800080
    assert "mid" in r.stdout and "#800080" in r.stdout
    # half-light toward white -> #ff8080; half-dark toward black -> #800000
    assert "#ff8080" in r.stdout
    assert "#800000" in r.stdout


def test_mix_shade_color_undoable(kernel):
    t = _agentic_task()
    _run_legacy_data_tools(kernel)
    r = kernel.execute(
        "red = register_color('red', '#ff0000')\n"
        "blue = register_color('blue', '#0000ff')\n"
        "p = mix_colors('purple', red, blue, 0.5)\n"
        "print('purple' in list_palette())\n"
        "undo_step()\n"
        "print('purple' in list_palette())\n",
        timeout=60,
    )
    assert r.ok, r.combined()
    assert "True" in r.stdout and "False" in r.stdout


# ----------------------------------------------------------------------
# undo_step / undo_round as model-callable tools
# ----------------------------------------------------------------------
def test_undo_step_tool(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    # one round: register + two calls; undo_step() reverts the last call
    r = kernel.execute(
        "red = input_canvas.color('#e0455a',name='red')\n"
        "input_canvas.rect(0,0,4,4,red)\n"
        "input_canvas.rect(10,10,4,4,red)\n"
        "out = undo_step()\n"
        "print(out)\n"
        "print(input_canvas.get(1,1) == red, input_canvas.get(12,12) == 0)\n",
        timeout=60,
    )
    assert r.ok, r.combined()
    assert "undo_step" in r.stdout
    # first rect kept, second rect reverted
    assert "True True" in r.stdout


def test_undo_step_nothing_to_undo_tool(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    r = kernel.execute("print(undo_step())", timeout=60)
    assert r.ok
    assert "undo_step" in r.stdout and "0" in r.stdout


def test_explicit_transparent_erase(kernel):
    _run_prelude(kernel, _agentic_task())
    r=kernel.execute("input_canvas.rect(0,0,3,3,'#f00')\ninput_canvas.set(2,1,None).set(1,2,'transparent')\nprint(input_canvas.get(1,1)!=0, input_canvas.get(2,1)==0, input_canvas.get(2,2)!=0)")
    assert r.ok, r.combined()
    assert 'True True True' in r.stdout


def test_undo_round_tool(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    # round 1
    r = kernel.execute("red = input_canvas.color('#e0455a',name='red')\ninput_canvas.rect(0,0,4,4,red)", timeout=60)
    assert r.ok, r.combined()
    # round 2
    r = kernel.execute("input_canvas.rect(10,10,4,4,red)", timeout=60)
    assert r.ok, r.combined()
    # round 3: undo_round() reverts round 2 only
    r = kernel.execute(
        "out = undo_round()\n"
        "print(out)\n"
        "print(input_canvas.get(1,1) == red, input_canvas.get(12,12) == 0)\n",
        timeout=60,
    )
    assert r.ok, r.combined()
    assert "undo_round" in r.stdout
    assert "True True" in r.stdout


def test_undo_round_walks_back_tool(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    kernel.execute("red = input_canvas.color('#e0455a',name='red')\ninput_canvas.rect(0,0,4,4,red)", timeout=60)  # round 1
    kernel.execute("input_canvas.rect(10,10,4,4,red)", timeout=60)  # round 2
    r = kernel.execute(
        "undo_round()\n"
        "undo_round()\n"
        "print(input_canvas.get(1,1) == 0, input_canvas.get(12,12) == 0)\n",
        timeout=60,
    )
    assert r.ok, r.combined()
    # both rounds reverted back to the initial (empty) canvas
    assert "True True" in r.stdout


def test_undo_round_reverts_palette_tool(kernel):
    t = _agentic_task()
    _run_prelude(kernel, t)
    kernel.execute("input_canvas.color('#3f9b4f',name='leaf')", timeout=60)  # round 1 (palette-only)
    r = kernel.execute("out = undo_round()\nprint(out)", timeout=60)
    assert r.ok
    r = kernel.execute("print('leaf' in input_canvas.pal.names)", timeout=60)
    assert "False" in r.stdout  # palette registration from round 1 reverted
