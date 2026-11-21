"""Edit input cropping, independent output dimensions and runtime-only limits."""
import json
from pathlib import Path

import numpy as np
import pytest

from pixelbench.core.canvas import PixelCanvas
from pixelbench.tasks.specs import TaskSpec, save_task_dir, load_task_dir
from pixelbench.tasks.edit_protocol import crop_edit_input
from pixelbench.repl.prelude import build_prelude
from pixelbench.repl.skill_runtime import SkillDrawing
from pixelbench.repl.skill_docs import skill_user_content, skill_system_prompt, skill_tool_docs
from pixelbench.agents.repl_agent import build_episode_user_content
from pixelbench.eval.metrics import compute_metrics, edit_metrics, animation_metrics
from pixelbench.agents.base import AgentResult


def input_canvas():
    c = PixelCanvas(8, 6)
    hidden = c.register_color('hidden', (12, 34, 56, 0))
    c.matrix[:] = hidden
    c.register_color('glass', (12, 34, 56, 128))
    c.register_color('ink', (0, 0, 0, 255))
    c.set_pixel(2, 1, 'glass')
    c.set_pixel(4, 3, 'ink')
    return c


def task():
    return TaskSpec('edit-variable', 'edit', 'Modify the sprite.', 8, 6, base=input_canvas())


def pixels(c):
    return np.asarray(c.render(scale=1).convert('RGBA'))


def test_trim_transparent_border_by_alpha_and_preserve_holes():
    base = input_canvas()
    before = pixels(base)
    cropped, box = crop_edit_input(base)
    assert box == (2, 1, 5, 4)
    assert (cropped.width, cropped.height) == (3, 3)
    assert np.array_equal(pixels(cropped), before[1:4, 2:5])
    assert np.array_equal(pixels(base), before)
    assert pixels(cropped)[1, 1, 3] == 0
    assert pixels(cropped)[0, 0, 3] == 128
    assert pixels(cropped)[2, 2].tolist() == [0, 0, 0, 255]
    # Opaque white borders are real pixels, not blank margins.
    white = PixelCanvas(4, 4)
    white.register_color('white', '#fff')
    white.paint_rect(0, 0, 4, 4, 'white')
    assert crop_edit_input(white)[1] == (0, 0, 4, 4)
    assert crop_edit_input(PixelCanvas(4, 3))[0].matrix.shape == (3, 4)


def test_task_dimensions_and_saved_inputs_use_trimmed_size(tmp_path):
    t = task()
    assert (t.width, t.height) == (3, 3)
    assert t.public_task()['input_size'] == {'width': 3, 'height': 3}
    assert t.public_task()['output_size'] == 'agent_defined'
    assert t.metadata['input_crop_box'] == [2, 1, 5, 4]
    initial = PixelCanvas.from_dict(t.initial_state())
    assert initial.matrix.shape == (3, 3)
    save_task_dir(t, tmp_path)
    reloaded = load_task_dir(tmp_path)
    assert (reloaded.width, reloaded.height) == (3, 3)
    assert reloaded.metadata['input_original_size'] == [8, 6]
    assert np.array_equal(pixels(reloaded.base), pixels(t.base))
    restore = TaskSpec('restore', 'restoration', '', 8, 6, reference=input_canvas(), mask=np.zeros((6, 8), bool))
    assert (restore.width, restore.height) == (8, 6)


def test_agent_prompts_show_input_size_not_output_size_or_limit():
    t = task()
    for content in (skill_user_content(t), build_episode_user_content(t)):
        text = '\n'.join(p.get('text', '') for p in content)
        assert 'Input image: 3x3 px.' in text
        assert 'Required output' not in text
        assert 'new_canvas(w,h)' in text
        assert 'input_canvas.copy' in text
        assert 'twice' not in text and '6x6' not in text and 'two times' not in text
    assert "dimensions and final" not in skill_system_prompt()
    assert 'edit limit' not in skill_tool_docs()
    restore = TaskSpec('restore', 'restoration', '', 8, 6)
    assert 'Required output: 8x6 px.' in skill_user_content(restore)[0]['text']


def test_runtime_dimension_guard_before_mutation_and_exact_copy_registration(tmp_path):
    from pixelbench._vendor.astra_pixelart.canvas import Canvas
    t = task()
    d = SkillDrawing(t.initial_state(), t.public_task(), tmp_path)
    api = d.bindings()
    before = d.to_dict(d.input)
    marks = len(d.calls)
    # invalid dimensions still fail before any mutation
    for w, h in ((0, 2), (2.1, 2), (True, 2), (-1, 5), (99999, 99999)):
        with pytest.raises(ValueError):
            api['new_canvas'](w, h)
        assert d.to_dict(d.input) == before and len(d.calls) == marks
    # an output larger than the input is allowed: growing the canvas to make
    # room for the edit is a normal move, with no cap relative to the input
    d._check_edit_size(7, 2)
    d._check_edit_size(2, 7)
    d._check_edit_size(1000, 1000)
    # every rejected call above left the workspace untouched
    assert d.to_dict(d.input) == before and len(d.calls) == marks
    # flattening a canvas larger than the input is allowed too
    flat = api['flatten']([Canvas(7, 2)])
    assert (flat.w, flat.h) == (7, 2)
    c = api['new_canvas'](6, 5, name='large')
    assert c in d.session.canvases
    # undo both canvas-creating calls (flatten + new_canvas) and the workspace
    # is back to the initial input
    d.undo_step()
    d.undo_step()
    assert d.to_dict(d.input) == before
    copied = api['input_canvas'].copy(name='output')
    assert copied is not api['input_canvas']
    assert copied.px == api['input_canvas'].px
    copied.set(0, 0, '#fff')
    assert copied.px != api['input_canvas'].px
    small = api['new_canvas'](2, 2)  # smaller is valid too
    assert small.w == 2


def test_load_larger_than_input_is_allowed(tmp_path):
    from PIL import Image
    t = task()
    d = SkillDrawing(t.initial_state(), t.public_task(), tmp_path)
    image = tmp_path/'large.png'
    Image.new('RGBA', (7, 2), (255, 0, 0, 255)).save(image)
    loaded = d.bindings()['load'](str(image))
    assert loaded.w == 7 and loaded.h == 2
    preview = d.bindings()['load'](str(image), add=False)
    assert preview.w == 7 and len(d.session.canvases) == 2
    d._check_edit_size(preview.w, preview.h)


@pytest.mark.parametrize('surface', ['full', 'redraw'])
def test_real_kernel_runtime_error_recovery_and_chosen_final_size(kernel, tmp_path, surface):
    t = task()
    obs = tmp_path/surface
    result = kernel.execute(build_prelude(t.public_task(), t.initial_state(), surface=surface, observer_dir=str(obs)))
    assert result.ok, result.combined()
    result = kernel.execute('sentinel=42\nnew_canvas(0,3)')
    assert not result.ok and 'positive integers' in result.combined()
    # a canvas larger than the input is no longer an error: the cap relative to
    # the input is gone, so this only has to not break the session
    result = kernel.execute('big=new_canvas(7,3)')
    assert result.ok, result.combined()
    result = kernel.execute("out=input_canvas.copy()\nassert sentinel==42\nout=new_canvas(5,4)\nout.set(4,3,'#ff0000')\nfinish(out)" if surface == 'full' else
                            "out=new_canvas(5,4)\nassert sentinel==42\nredraw(out,[['#ff0000']*5 for _ in range(4)])\nfinish(out)")
    assert result.ok, result.combined()
    final = kernel.extract_final_canvas()
    assert (final.width, final.height) == (5, 4)
    assert final.render(scale=1).getpixel((4, 3)) == (255, 0, 0, 255)
    assert compute_metrics(t, final)['validity']['valid']
    events = [json.loads(line) for line in (obs/'calls.jsonl').read_text().splitlines()]
    assert 'new_canvas' in {e['op'] for e in events}


def test_edit_explicit_frames_keep_chosen_dimensions(kernel):
    t = task()
    t.num_frames = 2
    result = kernel.execute(build_prelude(t.public_task(), t.initial_state()))
    assert result.ok, result.combined()
    result = kernel.execute("f1=new_canvas(5,4).set(1,1,'#f00')\nf2=f1.copy().set(2,1,'#0f0')\nfinish([f1,f2])")
    assert result.ok, result.combined()
    frames = kernel.extract_final_frames()
    assert len(frames) == 2
    assert [(f.width, f.height) for f in frames] == [(5, 4), (5, 4)]


def test_no_fixed_output_size_and_sequence_structure_is_the_remaining_rule():
    t = task()
    # any size the agent chooses is valid, above or below the input size
    for canvas in (PixelCanvas(6, 6), PixelCanvas(1, 2), PixelCanvas(7, 3), PixelCanvas(900, 900)):
        assert compute_metrics(t, canvas)['validity']['valid'], canvas.shape if hasattr(canvas, 'shape') else canvas
    # multi-frame outputs must at least share one canvas geometry
    t.num_frames = 2
    result = AgentResult(ok=True, final_frames=[PixelCanvas(3, 3), PixelCanvas(3, 7)])
    m = compute_metrics(t, PixelCanvas(3, 3), result)
    assert not m['validity']['valid']
    assert any('same canvas size' in e for e in m['validity']['errors']), m['validity']['errors']
    restore = TaskSpec('restore', 'restoration', '', 3, 3)
    assert not compute_metrics(restore, PixelCanvas(4, 3))['validity']['valid']


def test_blank_padding_does_not_inflate_edit_preservation():
    base = task().base
    larger = PixelCanvas(6, 5, palette=base.palette.copy())
    larger.matrix[:3, :3] = base.matrix
    same = edit_metrics(larger, base)
    assert same['changed_px'] == 0 and same['compared_px'] == 9
    larger.set_pixel(5, 4, 'ink')
    changed = edit_metrics(larger, base)
    assert changed['changed_px'] == 1 and changed['compared_px'] == 10
    assert changed['changed_ratio'] == 0.1
    smaller = PixelCanvas(1, 1, palette=base.palette.copy(), initial=base.matrix[:1, :1])
    assert edit_metrics(smaller, base)['changed_px'] == 1


def test_edit_sequence_ignores_common_empty_border_but_keeps_motion():
    first, second = task().base, task().base.copy()
    second.set_pixel(1, 0, 'ink')
    pred = []
    for frame in (first, second):
        larger = PixelCanvas(6, 5, palette=frame.palette.copy())
        larger.matrix[1:4, 2:5] = frame.matrix
        pred.append(larger)
    metrics = animation_metrics(pred, [first, second], rgba=True, variable_size=True)
    assert metrics['frame_pixel_accuracy'] == metrics['diff_agreement'] == 1
    bad = animation_metrics([pred[0], pred[0]], [first, second], rgba=True, variable_size=True)
    assert bad['diff_agreement'] == 0
