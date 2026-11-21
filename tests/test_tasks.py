import numpy as np
import pytest

from pixelbench.tasks.generators import ASSET_KINDS, AssetLibrary
from pixelbench.tasks.masks import blob_mask, mask_bbox, rect_mask
from pixelbench.tasks.smoke import smoke_tasks
from pixelbench.tasks.specs import TaskSpec, load_task_dir, save_task_dir


def test_smoke_tasks_cover_all_types_and_sizes():
    tasks = smoke_tasks()
    types = {t.task_type for t in tasks}
    assert types == {"agentic_creation", "replication", "restoration", "edit"}
    sizes = {(t.width, t.height) for t in tasks}
    assert (16, 16) in sizes and (48, 48) in sizes
    for t in tasks:
        assert t.max_colors > 0
        if t.task_type in ("replication", "restoration"):
            assert t.reference is not None
        if t.task_type == "restoration":
            assert t.mask is not None and t.mask.shape == (t.height, t.width)
        if t.task_type == "edit":
            assert t.base is not None and (t.base.width, t.base.height) == (t.width, t.height)


def test_task_initial_state():
    t = smoke_tasks()[2]
    s = t.initial_state()
    assert s["width"] == t.width and s["height"] == t.height
    assert s["canvas"] == [[0] * t.width for _ in range(t.height)]


def test_restoration_initial_state_is_corrupted():
    t = smoke_tasks()[6]
    s = t.initial_state()
    arr = np.array(s["canvas"])
    assert arr[t.mask].sum() == 0  # masked region erased
    assert arr[~t.mask].sum() > 0  # protected region intact


def test_hidden_eval_does_not_leak_reference_for_restoration():
    t = smoke_tasks()[6]
    pub = t.public_task()
    assert pub.get("allow_reference") is False
    hidden = t.hidden_eval()
    assert "reference" in hidden  # only the evaluator sees it


def test_save_load_task_dir(tmp_path):
    t = smoke_tasks()[4]
    save_task_dir(t, tmp_path / t.task_type / t.id)
    t2 = load_task_dir(tmp_path / t.task_type / t.id)
    assert t2.id == t.id
    assert t2.task_type == t.task_type
    assert t2.width == t.width and t2.height == t.height
    assert t2.reference is not None
    assert t2.reference.matrix.tolist() == t.reference.matrix.tolist()
    assert (tmp_path / t.task_type / t.id / "task.json").exists()
    assert (tmp_path / t.task_type / t.id / "reference.png").exists()
    assert (tmp_path / t.task_type / t.id / "hidden_eval.json").exists()


def test_save_load_restoration_dir(tmp_path):
    t = smoke_tasks()[6]
    save_task_dir(t, tmp_path / "r")
    t2 = load_task_dir(tmp_path / "r")
    assert t2.mask is not None
    assert np.array_equal(t2.mask, t.mask)


def test_edit_initial_state_is_full_base():
    t = next(x for x in smoke_tasks() if x.id == "edit_0001")
    s = t.initial_state()
    assert s["width"] == t.width and s["height"] == t.height
    arr = np.array(s["canvas"])
    base_arr = np.array(t.base.matrix)
    assert arr.shape == base_arr.shape
    assert (arr != t.base.transparent_id).sum() > 0  # starts from a real image
    assert np.array_equal(arr, base_arr)  # full original, nothing erased


def test_edit_public_task_does_not_leak_base_path_or_target():
    t = next(x for x in smoke_tasks() if x.id == "edit_0001")
    pub = t.public_task()
    assert pub.get("allow_reference") is False
    assert "base" not in pub  # the input image is the canvas itself, no hidden blob
    hidden = t.hidden_eval()
    assert "base" not in hidden  # base is visible input, not hidden eval


def test_save_load_edit_dir(tmp_path):
    t = next(x for x in smoke_tasks() if x.id == "edit_0002")
    save_task_dir(t, tmp_path / "edit")
    assert (tmp_path / "edit" / "base.pixel.json").exists()
    assert (tmp_path / "edit" / "base.png").exists()
    t2 = load_task_dir(tmp_path / "edit")
    assert t2.task_type == "edit"
    assert t2.base is not None
    assert np.array_equal(np.array(t2.base.matrix), np.array(t.base.matrix))
    assert np.array_equal(np.array(t2.initial_state()["canvas"]), np.array(t.base.matrix))


def test_load_tasks_from_dir_nested(tmp_path):
    from pixelbench.tasks.specs import load_tasks_from_dir

    for t in smoke_tasks()[:4]:
        save_task_dir(t, tmp_path / "tasks" / t.task_type / t.id)
    specs = load_tasks_from_dir(tmp_path / "tasks")
    assert len(specs) == 4
    assert {s.id for s in specs} == {t.id for t in smoke_tasks()[:4]}


def test_asset_library_deterministic():
    lib = AssetLibrary(seed=5)
    a = lib.generate("heart", 24, 24, seed=1)
    b = lib.generate("heart", 24, 24, seed=1)
    assert a.matrix.tolist() == b.matrix.tolist()
    assert len(a.palette) >= 2
    assert set(lib.list_kinds()) == set(ASSET_KINDS)
    with pytest.raises(ValueError):
        lib.generate("banana", 8, 8)


def test_masks():
    m = rect_mask(16, 16, (4, 4, 8, 8))
    assert m[4:12, 4:12].all() and not m[0, 0]
    assert mask_bbox(m) == [4, 4, 11, 11]
    b = blob_mask(32, 32, 16, 16, 8, seed=3)
    assert b.any() and b.sum() > 0
    assert b.shape == (32, 32)


def test_mae_style_masks_large_coverage():
    from pixelbench.tasks.masks import large_blob_mask, mae_mask, scattered_mask

    for w, h in [(64, 64), (128, 128), (90, 90), (32, 25)]:
        m = mae_mask(w, h, mask_ratio=0.75, patch_size=16, seed=3)
        assert m.shape == (h, w) and m.dtype == bool
        assert 0.6 < m.mean() < 0.9, (w, h, m.mean())

        b = large_blob_mask(w, h, frac=0.5, seed=3)
        assert b.shape == (h, w) and 0.25 < b.mean() < 0.75

        s = scattered_mask(w, h, n_regions=6, total_frac=0.5, seed=3)
        assert s.shape == (h, w) and 0.25 < s.mean() < 0.75

    # deterministic for a fixed seed
    a = mae_mask(64, 64, seed=9)
    b = mae_mask(64, 64, seed=9)
    assert np.array_equal(a, b)
