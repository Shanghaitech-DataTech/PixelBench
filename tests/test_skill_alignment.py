"""Drawing semantics, benchmark boundaries, and real-kernel integration."""
import json
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from pixelbench.core.canvas import PixelCanvas
from pixelbench.eval.metrics import edit_metrics, restoration_metrics, palette_discipline
from pixelbench.repl.prelude import build_prelude
from pixelbench.repl.skill_runtime import SkillDrawing
from pixelbench.tasks.specs import TaskSpec


def drawing(tmp_path, size=(4, 4), **kwargs):
    return SkillDrawing(PixelCanvas(*size).to_dict(), {'task_type': 'edit'}, tmp_path, **kwargs)


def rgba(c, x=0, y=0):
    return c.pal.rgba(c.px[y * c.w + x])


def test_layers_replace_vs_source_over_and_shared_palette(tmp_path):
    d = drawing(tmp_path)
    api = d.bindings()
    base = d.input.rect(0, 0, 4, 4, '#ff0000')
    layer = api['new_canvas'](4, 4, name='overlay')
    cid = layer.color('#0000ff80', name='glass')
    assert base.color('glass') == cid
    layer.set(0, 0, 'glass').set(0, 0, 'glass')
    assert rgba(layer) == (0, 0, 255, 128)  # repeat replaces, never accumulates
    merged = api['flatten']([base, layer], name='result')
    assert rgba(merged) == (127, 0, 128, 255)
    assert rgba(merged, 1, 0) == (255, 0, 0, 255)
    assert rgba(base) == (255, 0, 0, 255)
    assert rgba(layer) == (0, 0, 255, 128)
    assert merged.pal is base.pal is layer.pal
    copied = base.copy().blit(layer, 0, 0)
    assert rgba(copied) == rgba(merged)
    assert copied.pal is base.pal
    assert len(d.session.palette.colors) == 4  # no per-pixel duplicate colours
    layer.set(0, 0, None)
    assert rgba(api['flatten']([base, layer])) == (255, 0, 0, 255)


def test_nonzero_transparent_alpha_and_partial_destination(tmp_path):
    d = drawing(tmp_path)
    api = d.bindings()
    base = d.input.set(0, 0, '#ff000080')
    top = api['new_canvas'](4, 4)
    top.set(0, 0, '#0000ff80').set(1, 1, '#abcdef00')
    assert top.stats()['visible_pixels'] == 1
    merged = api['flatten']([base, top])
    assert rgba(merged) == (85, 0, 170, 192)
    assert rgba(merged, 1, 1)[3] == 0
    final = PixelCanvas.from_dict(d.to_dict(top))
    assert final.stats()['used_pixels'] == 1
    assert palette_discipline(final, 1)['used_colors'] == 1


def test_round_undo_preserves_objects_palette_and_layers(tmp_path):
    d = drawing(tmp_path)
    api = d.bindings()
    original = d.input
    d.mark_round()
    original.set(0, 0, '#f00')
    layer = api['new_canvas'](4, 4)
    layer.rect(0, 0, 2, 2, '#0000ff80')
    d.mark_round()
    assert d.undo_round()['restored'] == 1
    assert d.input is original
    assert len(d.session.canvases) == 1
    assert len(original.pal.colors) == 1
    assert rgba(original)[3] == 0
    assert all(v == 0 for v in layer.px)
    original.set(0, 0, '#0f0')  # existing Python references still work
    d.undo_step()
    assert rgba(original)[3] == 0
    assert len(original.pal.colors) == 1


def test_exports_and_layer_state_roundtrip(tmp_path):
    d = drawing(tmp_path)
    api = d.bindings()
    base = d.input.rect(0, 0, 4, 4, '#f00')
    top = api['new_canvas'](4, 4, name='glass').set(1, 1, '#0000ff80')
    composite = api['flatten']([base, top], name='composite')
    files = api['save']('result', composite)
    assert Image.open(files['png']).size == (4, 4)
    assert Image.open(files['png_4x']).size == (16, 16)
    assert Image.open(files['png']).convert('RGBA').getpixel((1, 1)) == (127, 0, 128, 255)
    assert Path(api['export']('layers', [base, top], format='ora')).is_file()
    assert Path(api['export']('layers', [base, top], format='ase')).is_file()
    final = PixelCanvas.from_dict(d.to_dict(d.input))
    assert len(final.copy().to_dict()['drawing_state']['canvases']) == 3
    restored = SkillDrawing(final.to_dict(), {'task_type': 'edit'}, tmp_path / 'again')
    assert restored.to_dict(d.input) == d.to_dict(d.input)
    assert restored.session.canvases[0].pal is restored.session.canvases[1].pal


def test_skill_shapes_fonts_and_snapshot(tmp_path):
    d = drawing(tmp_path, (32, 32))
    c = d.input
    assert c.rect(0, 0, 3, 3, '#f00') is c
    assert rgba(c, 1, 1) == (255, 0, 0, 255)
    c.snapshot('a').clear().restore('a')
    assert rgba(c, 1, 1) == (255, 0, 0, 255)
    c.path('M 8 8 Q 16 0 24 8 L 24 24 L 8 24 Z', '#0f0')
    assert rgba(c, 16, 16) == (0, 255, 0, 255)
    c.clear().text(0, 0, '中', '#fff')
    assert c.stats()['visible_pixels'] > 0
    for size in ('8px', '10px', '12px'):
        c.clear().text(0, 0, '中', '#fff', font=size)
        assert c.stats()['visible_pixels'] > 0
    assert '0' in c.matrix_text(indices=True)


def test_implicit_bindings_removed(tmp_path):
    d = drawing(tmp_path)
    api = d.bindings()
    assert 'current' not in api and 'set_pixel' not in api and 'register_canvas' not in api
    with pytest.raises(TypeError):
        api['view']()
    with pytest.raises(TypeError):
        api['save']('bad')


def test_rgba_scoring_ignores_id_remapping_but_detects_palette_edits():
    ref = PixelCanvas(2, 2)
    ref.register_color('red', '#ff000080')
    ref.paint_rect(0, 0, 2, 2, 'red')
    pred = PixelCanvas(2, 2)
    pred.register_color('unused', '#000')
    pred.register_color('same_red', '#ff000080')
    pred.paint_rect(0, 0, 2, 2, 'same_red')
    mask = np.array([[True, False], [False, False]])
    assert edit_metrics(pred, ref)['changed_px'] == 0
    metrics = restoration_metrics(pred, ref, mask, ref)
    assert metrics['region_accuracy'] == metrics['seam_accuracy'] == 1
    assert metrics['protected_change_rate'] == 0
    pred = ref.copy()
    pred.replace_color('red', '#ff000040')  # same ID, different actual alpha
    assert edit_metrics(pred, ref)['changed_px'] == 4
    assert restoration_metrics(pred, ref, mask, ref)['protected_change_rate'] == 1


def test_real_kernel_keeps_state_errors_images_and_layers(kernel, tmp_path):
    task = TaskSpec('edit-test', 'edit', 'Add translucent blue', 4, 4)
    obs = tmp_path / 'observations'
    prelude = build_prelude(task.public_task(), task.initial_state(), observer_dir=str(obs))
    assert kernel.execute(prelude).ok
    first = kernel.execute("counter=41\nbase=input_canvas.rect(0,0,4,4,'#f00')\ntop=new_canvas(4,4,name='top')\ntop.set(0,0,'#0000ff80')\nview(top,size=64)")
    assert first.ok, first.combined()
    assert len(first.images) == 1
    failed = kernel.execute("top.set(1,1,'#fff')\nraise ValueError('keep ipykernel semantics')")
    assert not failed.ok
    again = kernel.execute("print(counter+1)\nundo_round()\nresult=flatten([base,top])\nfinish(result)")
    assert again.ok, again.combined()
    assert '42' in again.stdout
    final = kernel.extract_final_canvas()
    assert final.render(scale=1).getpixel((0, 0)) == (127, 0, 128, 255)
    assert final.render(scale=1).getpixel((1, 1)) == (255, 0, 0, 255)
    assert len(final.to_dict()['drawing_state']['canvases']) == 3
    events = [json.loads(line) for line in (obs / 'calls.jsonl').read_text().splitlines()]
    assert {'rect', 'new_canvas', 'set', 'flatten'} <= {e['op'] for e in events}
    assert list((obs / 'frames').glob('*.png'))


def test_full_agent_uses_skill_docs_and_feedback(kernel, tmp_path, monkeypatch):
    from pixelbench.agents.repl_agent import REPLAgent
    from pixelbench.agents.base import Budget
    from tests.conftest import FakeLLM, FakeMessage, tool_call, message_has_image
    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND', 'off')
    task = TaskSpec('edit-test', 'edit', 'Add red', 4, 4)
    assert kernel.execute(build_prelude(task.public_task(), task.initial_state())).ok
    llm = FakeLLM([
        FakeMessage(tool_calls=[tool_call('a', 'run_code', {'code': "input_canvas.set(0,0,'#f00')\nview(input_canvas,size=32)"})]),
        FakeMessage(tool_calls=[tool_call('b', 'run_code', {'code': 'finish(input_canvas)'})]),
    ])
    result = REPLAgent(llm=llm).run(task, kernel, Budget(max_steps=2))
    assert result.ok
    assert 'flatten' in llm.calls[0]['tools'][0]['function']['description']
    assert message_has_image(llm.calls[1]['messages'])
    assert result.final_canvas.render(scale=1).getpixel((0, 0)) == (255, 0, 0, 255)


def test_all_tasks_use_explicit_canvas_surface():
    for kind, surface in [('agentic_creation', 'full'), ('restoration', 'redraw')]:
        task = TaskSpec('legacy', kind, '', 4, 4)
        code = build_prelude(task.public_task(), task.initial_state(), surface=surface)
        assert '_pb_install_skill' in code
        assert 'SessionTools' not in code


def test_foreign_palette_composition_and_shape_rejection(tmp_path):
    from pixelbench._vendor.astra_pixelart.canvas import Canvas
    d = drawing(tmp_path)
    base = d.input.rect(0, 0, 4, 4, '#f00')
    foreign = Canvas(4, 4).set(0, 0, '#0000ff80')
    result = d.bindings()['flatten']([base, foreign])
    assert rgba(result) == (127, 0, 128, 255)
    with pytest.raises(ValueError, match='same size'):
        d.bindings()['flatten']([base, Canvas(3, 3)])


def test_skill_preview_is_not_submitted_and_text_look_budget(tmp_path):
    d = drawing(tmp_path, look_budget=1)
    c = d.input.set(0, 0, '#f00')
    assert isinstance(c.get(0, 0), int)
    assert 'observation disabled' in c.matrix_text()
    assert 'observation disabled' in d.view(c,size=64)
    files = d.api['save']('native', c)
    assert Image.open(files['png']).size == (4, 4)
    assert len(d.to_dict(d.input)['canvas']) == 4


def test_edit_multiframe_metric_uses_actual_colours():
    from pixelbench.eval.metrics import animation_metrics, compute_metrics
    from pixelbench.agents.base import AgentResult
    base = PixelCanvas(2, 2)
    base.register_color('red', '#f00')
    base.paint_rect(0, 0, 2, 2, 'red')
    changed = base.copy()
    changed.replace_color('red', '#00f')
    # Palette-only edits change every visible pixel although IDs stay fixed.
    pred = changed.copy()
    task = TaskSpec('frames', 'edit', '', 2, 2, base=base, frames=[base, changed], num_frames=2)
    result = AgentResult(ok=True, final_canvas=pred, final_frames=[base, changed])
    metrics = compute_metrics(task, pred, result)
    assert metrics['edit_frames']['frame_pixel_accuracy'] == 1
    assert metrics['edit_frames']['diff_agreement'] == 1
    assert animation_metrics([base, base], [base, changed], rgba=True)['diff_agreement'] == 0
    assert compute_metrics(task, PixelCanvas(5, 3))['validity']['valid'] is False


def test_restoration_kernel_mask_hidden_reference_and_multiframe(kernel):
    from pixelbench.eval.metrics import restoration_metrics
    base = PixelCanvas(4, 4)
    base.register_color('red', '#f00')
    base.paint_rect(0, 0, 4, 4, 'red')
    mask = np.zeros((4, 4), dtype=bool)
    mask[1, 1] = True
    task = TaskSpec('restore', 'restoration', '', 4, 4, reference=base, mask=mask, num_frames=2)
    result = kernel.execute(build_prelude(task.public_task(), task.initial_state(), mask_state=task.mask_state()))
    assert result.ok, result.combined()
    result = kernel.execute("assert reference is None\nassert mask[1,1]\nf1=input_canvas.copy().set(1,1,'red')\nf2=f1.copy().set(0,0,'#fff')\nfinish([f1,f2])")
    assert result.ok, result.combined()
    frames = kernel.extract_final_frames()
    assert len(frames) == 2
    damaged = PixelCanvas.from_dict(task.initial_state())
    scores = restoration_metrics(frames[0], base, mask, damaged)
    assert scores['region_accuracy'] == 1
    assert scores['protected_change_rate'] == 0
    assert 'drawing_state' in frames[0].to_dict()


def test_selection_recipe_is_read_paste_is_undoable(tmp_path):
    d = drawing(tmp_path, (8, 4), look_budget=0)
    c = d.input.set(0, 0, '#ff000080').set(1, 0, '#0f0')
    before = d.to_dict(d.input)
    calls = len(d.calls)
    s = c.select(0, 0, 2, 1)
    transformed = s.flip().resize(4, 2).rotate(90)
    assert transformed.size == (2, 4)
    assert len(d.calls) == calls  # no checkpoint or look charge for recipes
    assert d.to_dict(d.input) == before
    transformed.copy_to(4, 0, c)
    assert rgba(c, 4, 0) == (0, 255, 0, 255)
    assert rgba(c, 4, 3) == (255, 0, 0, 128)
    assert len(d.calls) == calls + 1
    assert d.events[-1]['op'] == 'selection_copy_to'
    d.undo_step()
    assert d.to_dict(d.input) == before
    # Selecting sees legacy matrix writes too.
    c.set(0, 0, '#0f0')
    s = c.select(0, 0, 1, 1)
    s.copy_to(7, 3, c)
    assert rgba(c, 7, 3) == (0, 255, 0, 255)


def test_selection_move_undo_restores_both_layers_and_blended_palette(tmp_path):
    d = drawing(tmp_path)
    a = d.input.set(0, 0, '#0000ff80')
    b = d.bindings()['new_canvas'](4, 4, background='#f00')
    before = d.to_dict(d.input)
    source_pixels = list(a.px)
    d.mark_round()
    a.select(0, 0, 1, 1).move_to(1, 1, canvas=b, mode='over')
    assert rgba(a)[3] == 0
    assert rgba(b, 1, 1) == (127, 0, 128, 255)
    assert len(b.pal.colors) == len(before['drawing_state']['palette']['colors']) + 1
    d.mark_round()
    d.undo_round()
    assert b in d.session.canvases
    assert a.px == source_pixels
    assert d.to_dict(d.input) == before


def test_selection_snapshot_after_undo_and_detached_preview(tmp_path):
    d = drawing(tmp_path)
    c = d.input.set(0, 0, '#0000ff80')
    s = c.select(0, 0, 1, 1)
    d.undo_step()  # snapshot retains RGBA after its palette entry disappears
    assert len(c.pal.colors) == 1
    p = s.preview()
    assert p.pal is c.pal and rgba(p) == (0, 0, 255, 128)
    assert d.input is c and len(d.session.canvases) == 1
    assert len(c.pal.colors) == 2
    d.undo_step()  # preview's colour registration and detached pixels roll back
    assert len(c.pal.colors) == 1 and rgba(p)[3] == 0
    s.copy_to(2, 2, c)
    assert rgba(c, 2, 2) == (0, 0, 255, 128)
    assert d.events[-1]['op'] == 'selection_copy_to'
    p = s.preview()
    p.set(0, 0, '#fff')
    assert rgba(c, 2, 2) == (0, 0, 255, 128)


def test_selection_stale_move_rejected_without_erasure(tmp_path):
    from pixelbench._vendor.astra_pixelart.canvas import CanvasError
    d = drawing(tmp_path)
    c = d.input.set(0, 0, '#f00')
    s = c.select(0, 0, 1, 1)
    c.set(0, 0, '#0f0')
    before = d.to_dict(d.input)
    with pytest.raises(CanvasError, match='source has changed'):
        s.move_to(1, 1, c)
    assert d.to_dict(d.input) == before
    s.copy_to(1, 1, c)  # copying deliberately retains old snapshot
    assert rgba(c, 1, 1) == (255, 0, 0, 255)


def test_selection_real_kernel_cross_block_preview_undo_and_events(kernel, tmp_path):
    task = TaskSpec('selection-edit', 'edit', 'Move selected pixels', 8, 8)
    obs = tmp_path / 'selection-observations'
    result = kernel.execute(build_prelude(task.public_task(), task.initial_state(), observer_dir=str(obs)))
    assert result.ok, result.combined()
    result = kernel.execute("c=input_canvas\nc.set(0,0,'#ff000080').set(1,0,'#0f0')\ns=c.select(0,0,2,1)")
    assert result.ok, result.combined()
    result = kernel.execute("t=s.rotate(90)\nview(canvas=t.preview(),size=64)\nt.move_to(3,2,c)")
    assert result.ok, result.combined()
    assert len(result.images) == 1
    result = kernel.execute("undo_round()\nassert c.pal.rgba(c.px[0]) == (255,0,0,128)\nassert c.pal.rgba(c.px[2*c.w+3])[3] == 0\ns.rotate(30,'rotsprite').copy_to(5,5,c)\nundo_step()\ns.flip().copy_to(4,4,c)\nraise ValueError('keep executed writes')")
    assert not result.ok
    result = kernel.execute("assert c.pal.rgba(c.px[4*c.w+4]) == (0,255,0,255)\nfinish(c)")
    assert result.ok, result.combined()
    final = kernel.extract_final_canvas()
    im = final.render(scale=1)
    assert im.size == (8, 8)
    assert im.getpixel((0, 0)) == (255, 0, 0, 128)
    assert im.getpixel((4, 4)) == (0, 255, 0, 255)
    assert im.getpixel((5, 4)) == (255, 0, 0, 128)
    assert len(final.to_dict()['drawing_state']['canvases']) == 1
    events = [json.loads(line) for line in (obs / 'calls.jsonl').read_text().splitlines()]
    assert {'selection_preview', 'selection_move_to', 'selection_copy_to', 'undo_step', 'undo_round'} <= {e['op'] for e in events}


def test_pinned_selection_engine_hashes_and_model_surface():
    import hashlib
    from pixelbench._vendor import astra_pixelart
    from pixelbench.repl.skill_docs import skill_tool_docs
    root = Path(astra_pixelart.__file__).parent
    manifest = json.loads((root / 'UPSTREAM.json').read_text())
    assert manifest['version'] == astra_pixelart.__version__ == '0.6.0'
    assert 'selection.py' in manifest['files']
    for name, expected in manifest['files'].items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected, name
    docs = skill_tool_docs()
    for method in ('select', 'flip', 'resize', 'rotate', 'preview', 'copy_to', 'move_to'):
        assert method + '(' in docs
    assert 'rotsprite' in docs


def test_selection_paste_to_standalone_canvas_can_undo(tmp_path):
    from pixelbench._vendor.astra_pixelart.canvas import Canvas
    d = drawing(tmp_path)
    c = d.input.set(0, 0, '#0000ff80')
    foreign = Canvas(2, 2, background='#f00')
    c.select(0, 0, 1, 1).move_to(0, 0, foreign, mode='over')
    assert rgba(foreign) == (127, 0, 128, 255)
    assert rgba(c)[3] == 0
    d.undo_step()
    assert rgba(foreign) == (255, 0, 0, 255)
    assert rgba(c) == (0, 0, 255, 128)
    assert foreign.pal is c.pal
    assert (127, 0, 128, 255) not in c.pal.colors
