"""Automatic hard metrics per task type.

These are deterministic, cheap and do not depend on any LLM.  They cover:
- validity & palette discipline
- replication: pixel accuracy, content IoU, palette recall
- restoration: region accuracy/IoU, seam continuity, protected-region error
- agentic: coverage, color usage, tool usage statistics
"""
from __future__ import annotations

from typing import Any, Dict, List

import numpy as np

from pixelbench.core.canvas import PixelCanvas
from pixelbench.tasks.specs import TaskSpec


def validate_canvas(canvas: PixelCanvas) -> Dict[str, Any]:
    errors: List[str] = []
    m = canvas.matrix
    ids = set(canvas.palette.ids())
    for v in np.unique(m):
        if int(v) not in ids:
            errors.append(f"cell value {int(v)} not in palette")
    if m.shape != (canvas.height, canvas.width):
        errors.append(f"matrix shape {m.shape} != {canvas.height}x{canvas.width}")
    return {"valid": not errors, "errors": errors}


def palette_discipline(canvas: PixelCanvas, max_colors: int) -> Dict[str, Any]:
    used = sorted({int(v) for v in np.unique(canvas.matrix) if int(v) != canvas.transparent_id})
    if hasattr(canvas, "_drawing_state"):
        used = [cid for cid in used if canvas.palette[cid].rgba[3] > 0]
    return {
        "used_colors": len(used),
        "max_colors": max_colors,
        "ok": len(used) <= max_colors,
        "names": [canvas.palette[cid].name for cid in used],
    }


def pixel_accuracy(pred: PixelCanvas, ref: PixelCanvas) -> float:
    if pred.matrix.shape != ref.matrix.shape:
        return 0.0
    return float((pred.matrix == ref.matrix).mean())


def _macro_f1(pred: PixelCanvas, ref: PixelCanvas) -> Dict[str, float]:
    """Per-color (non-transparent) macro precision/recall/F1."""
    ids = sorted({int(v) for v in np.unique(ref.matrix) if int(v) != ref.transparent_id})
    precs, recs = [], []
    for cid in ids:
        ref_mask = ref.matrix == cid
        pred_mask = pred.matrix == cid
        inter = float((ref_mask & pred_mask).sum())
        precs.append(inter / float(pred_mask.sum()) if pred_mask.sum() else 1.0)
        recs.append(inter / float(ref_mask.sum()) if ref_mask.sum() else 1.0)
    p = float(np.mean(precs)) if precs else 1.0
    r = float(np.mean(recs)) if recs else 1.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0
    return {"macro_precision": round(p, 4), "macro_recall": round(r, 4), "macro_f1": round(f1, 4)}


def replication_metrics(pred: PixelCanvas, ref: PixelCanvas) -> Dict[str, Any]:
    acc = pixel_accuracy(pred, ref)
    content = ref.matrix != ref.transparent_id
    pred_content = pred.matrix != pred.transparent_id
    inter = float(((pred.matrix == ref.matrix) & content).sum())
    union = float((content | pred_content).sum())
    iou = inter / union if union else 1.0
    ref_ids = sorted({int(v) for v in np.unique(ref.matrix) if int(v) != ref.transparent_id})
    pred_ids = sorted({int(v) for v in np.unique(pred.matrix) if int(v) != pred.transparent_id})
    pal_recall = len(set(ref_ids) & set(pred_ids)) / len(ref_ids) if ref_ids else 1.0
    f1 = _macro_f1(pred, ref)
    return {
        "pixel_accuracy": round(acc, 4),
        "content_iou": round(iou, 4),
        "palette_recall": round(pal_recall, 4),
        **f1,
        "ref_colors": len(ref_ids),
        "pred_colors": len(pred_ids),
    }


def _rgba_pixels(canvas: PixelCanvas) -> np.ndarray:
    """Colour identity is RGBA, independent of palette numbering/aliases.

    Hidden RGB at alpha zero has no visual meaning and is canonicalised.
    """
    out = np.zeros((*canvas.matrix.shape, 4), dtype=np.uint8)
    for color in canvas.palette:
        if color.rgba[3]:
            out[canvas.matrix == color.id] = color.rgba
    return out


def _aligned_rgba(canvases):
    """Align native pixels at top-left, with transparent padding, never resize."""
    w, h = max(c.width for c in canvases), max(c.height for c in canvases)
    arrays = []
    for c in canvases:
        a = np.zeros((h, w, 4), dtype=np.uint8)
        a[:c.height, :c.width] = _rgba_pixels(c)
        arrays.append(a)
    return arrays


def edit_metrics(pred: PixelCanvas, base: PixelCanvas) -> Dict[str, Any]:
    """Edit hard metrics vs. the original input image.

    Without a hidden "after" target, the objective signal is *how much* the
    agent changed and *where*: a focused edit should leave most of the
    canvas untouched and reuse the original palette.  (Whether the change
    is the right one is judged by the LLM judge against the instruction.)
    """
    p, b = _aligned_rgba([pred, base])
    changed = np.any(p != b, axis=-1)
    changed_px = int(changed.sum())
    # Blank extra margins must not inflate preservation ratios.
    domain = p[..., 3] > 0
    domain[:base.height, :base.width] = True
    total = int(domain.sum())
    bbox = None
    if changed_px:
        ys, xs = np.nonzero(changed)
        bbox = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
    base_colors = {base.palette[int(v)].rgba for v in np.unique(base.matrix)
                   if base.palette[int(v)].rgba[3] > 0}
    new_colors = sorted(int(v) for v in np.unique(pred.matrix)
                        if pred.palette[int(v)].rgba[3] > 0
                        and pred.palette[int(v)].rgba not in base_colors)
    return {
        "input_size": [base.width, base.height],
        "output_size": [pred.width, pred.height],
        "size_changed": (pred.width, pred.height) != (base.width, base.height),
        "alignment": "top_left_transparent_padding",
        "compared_px": total,
        "changed_px": changed_px,
        "changed_ratio": round(changed_px / total, 4) if total else 0.0,
        "unchanged_ratio": round(1.0 - changed_px / total, 4) if total else 1.0,
        "bbox": bbox,
        "new_colors": new_colors,
    }


def _dilate(mask: np.ndarray, radius: int = 1) -> np.ndarray:
    p = np.pad(mask, radius, constant_values=False)
    out = np.zeros_like(mask)
    h, w = mask.shape
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            out |= p[radius + dy : radius + dy + h, radius + dx : radius + dx + w]
    return out


def restoration_metrics(pred: PixelCanvas, target: PixelCanvas, mask: np.ndarray, corrupted: PixelCanvas) -> Dict[str, Any]:
    if pred.matrix.shape != target.matrix.shape or pred.matrix.shape != corrupted.matrix.shape:
        return {"error": "shape mismatch"}
    m = mask
    p_rgba, t_rgba = _rgba_pixels(pred), _rgba_pixels(target)
    equal = np.all(p_rgba == t_rgba, axis=-1)
    region_acc = float(equal[m].mean()) if m.any() else 1.0
    t_content = t_rgba[m, 3] > 0
    p_content = p_rgba[m, 3] > 0
    inter = float((t_content & p_content).sum())
    union = float((t_content | p_content).sum())
    region_iou = inter / union if union else 1.0
    boundary = _dilate(m, 1) & ~m
    seam_acc = float(equal[boundary].mean()) if boundary.any() else 1.0
    changed = np.any(p_rgba != _rgba_pixels(corrupted), axis=-1)
    protected_changed = changed & ~m
    protected_frac = float(protected_changed.sum()) / float((~m).sum()) if (~m).any() else 0.0
    mask_frac = float(m.sum()) / m.size
    return {
        "region_accuracy": round(region_acc, 4),
        "region_iou": round(region_iou, 4),
        "seam_accuracy": round(seam_acc, 4),
        "protected_change_rate": round(protected_frac, 4),
        "mask_fraction": round(mask_frac, 4),
    }


def _crop_sequence(frames):
    """Remove one shared empty border per sequence, preserving relative motion."""
    if not frames:
        return frames
    boxes = []
    for f in frames:
        ys, xs = np.nonzero(_rgba_pixels(f)[..., 3])
        if len(xs):
            boxes.append((int(xs.min()), int(ys.min()), int(xs.max())+1, int(ys.max())+1))
    if not boxes:
        return frames
    x0, y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
    x1, y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
    out = []
    for f in frames:
        c = PixelCanvas(x1-x0, y1-y0, palette=f.palette.copy(), transparent_id=f.transparent_id)
        right, bottom = min(x1, f.width), min(y1, f.height)
        if right > x0 and bottom > y0:
            c.matrix[:bottom-y0, :right-x0] = f.matrix[y0:bottom, x0:right]
        out.append(c)
    return out


def animation_metrics(pred_frames: List[PixelCanvas], ref_frames: List[PixelCanvas], *, rgba: bool = False, variable_size: bool = False) -> Dict[str, Any]:
    """Per-frame fidelity + inter-frame consistency for animation tasks.

    - frame_pixel_accuracy / frame_content_iou: mean replication fidelity
      over aligned frames.
    - diff_agreement: IoU between predicted and reference per-pixel "what
      changed between adjacent frames" masks (motion correctness).
    - static_consistency: fraction of pixels that stay static in the
      reference that also stay static in the prediction (no spurious motion).
    - frame_count_match: whether the model produced the expected number.
    """
    if variable_size:
        rgba = True
        pred_frames, ref_frames = _crop_sequence(pred_frames), _crop_sequence(ref_frames)
    n = min(len(pred_frames), len(ref_frames))
    if n == 0:
        return {"frame_count": len(pred_frames), "frame_count_match": False}
    accs, ious, pal_recalls = [], [], []
    for i in range(n):
        p, r = pred_frames[i], ref_frames[i]
        if not variable_size and p.matrix.shape != r.matrix.shape:
            accs.append(0.0); ious.append(0.0); pal_recalls.append(0.0)
            continue
        if rgba:
            p_values, r_values = (_aligned_rgba([p, r]) if variable_size else (_rgba_pixels(p), _rgba_pixels(r)))
            equal = np.all(p_values == r_values, axis=-1)
            content, p_content = r_values[..., 3] > 0, p_values[..., 3] > 0
        else:
            equal = p.matrix == r.matrix
            content, p_content = r.matrix != r.transparent_id, p.matrix != p.transparent_id
        if variable_size:
            domain = p_content.copy()
            domain[:r.height, :r.width] = True
            accs.append(float(equal[domain].mean()) if domain.any() else 1.0)
        else:
            accs.append(float(equal.mean()))
        inter = float((equal & content).sum())
        union = float((content | p_content).sum())
        ious.append(inter / union if union else 1.0)
        ref_ids = sorted({int(v) for v in np.unique(r.matrix) if int(v) != r.transparent_id})
        pred_ids = sorted({int(v) for v in np.unique(p.matrix) if int(v) != p.transparent_id})
        if rgba:
            ref_colors = {r.palette[int(v)].rgba for v in np.unique(r.matrix) if r.palette[int(v)].rgba[3]}
            pred_colors = {p.palette[int(v)].rgba for v in np.unique(p.matrix) if p.palette[int(v)].rgba[3]}
            pal_recalls.append(len(ref_colors & pred_colors) / len(ref_colors) if ref_colors else 1.0)
        else:
            pal_recalls.append(len(set(ref_ids) & set(pred_ids)) / len(ref_ids) if ref_ids else 1.0)

    # inter-frame motion agreement (aligned pairs)
    diff_ious, static_ok = [], []
    for i in range(n - 1):
        p0, p1 = pred_frames[i], pred_frames[i + 1]
        r0, r1 = ref_frames[i], ref_frames[i + 1]
        if not variable_size and (p0.matrix.shape != p1.matrix.shape or p0.matrix.shape != r0.matrix.shape
                or r0.matrix.shape != r1.matrix.shape):
            continue
        if variable_size:
            a, b, c, d = _aligned_rgba([p0, p1, r0, r1])
            p_diff, r_diff = np.any(a != b, axis=-1), np.any(c != d, axis=-1)
        else:
            p_diff = (np.any(_rgba_pixels(p0) != _rgba_pixels(p1), axis=-1)
                      if rgba else p0.matrix != p1.matrix)
            r_diff = (np.any(_rgba_pixels(r0) != _rgba_pixels(r1), axis=-1)
                      if rgba else r0.matrix != r1.matrix)
        inter = float((p_diff & r_diff).sum())
        union = float((p_diff | r_diff).sum())
        diff_ious.append(inter / union if union else 1.0)
        r_static = ~r_diff
        if variable_size:
            domain = (a[..., 3] > 0) | (b[..., 3] > 0)
            domain[:r0.height, :r0.width] = True
            domain[:r1.height, :r1.width] = True
            r_static &= domain
        if r_static.any():
            static_ok.append(float((~p_diff & r_static).sum()) / float(r_static.sum()))
    m = {
        "frame_count": len(pred_frames),
        "frame_count_match": len(pred_frames) == len(ref_frames),
        "frame_pixel_accuracy": round(float(np.mean(accs)), 4) if accs else 0.0,
        "frame_content_iou": round(float(np.mean(ious)), 4) if ious else 0.0,
        "frame_palette_recall": round(float(np.mean(pal_recalls)), 4) if pal_recalls else 0.0,
        "diff_agreement": round(float(np.mean(diff_ious)), 4) if diff_ious else 0.0,
        "static_consistency": round(float(np.mean(static_ok)), 4) if static_ok else 0.0,
        "frames_aligned": n,
        **({"alignment": "sequence_content_bbox_transparent_padding"} if variable_size else {}),
    }
    return m


def agentic_metrics(
    canvas: PixelCanvas,
    transcript: List[dict],
    obs_calls: Optional[List[dict]] = None,
) -> Dict[str, Any]:
    """Agentic tool-use statistics.

    Prefers the painting-process observer's call log (``obs_calls``, one
    dict per tool call) because it records *every* model call — including
    palette registration — and survives canvas serialization.  Falls back
    to the canvas edit log when no observer data is available (observe
    off, or in-memory canvases in tests).
    """
    st = canvas.stats()
    steps = len([t for t in transcript if t.get("kind") == "code"])
    if obs_calls is not None:
        ops = [{"op": c.get("op", "?"), "changed": int(c.get("changed", 0) or 0)} for c in obs_calls]
    else:
        ops = canvas._edit_log
    tool_types = sorted({o["op"] for o in ops})
    total_changed = sum(int(o.get("changed", 0)) for o in ops)
    undo_count = sum(1 for o in ops if o["op"] in ("undo", "undo_step", "undo_round"))
    return {
        "coverage_pct": round(st["coverage_pct"], 2),
        "used_colors": st["used_colors"],
        "steps": steps,
        "tool_calls": len(ops),
        "tool_diversity": len(tool_types),
        "tool_types": tool_types,
        "total_changed_px": total_changed,
        "undo_count": undo_count,
    }


def freeform_multiframe_metrics(pred_frames: List[PixelCanvas], expected: int = 0) -> Dict[str, Any]:
    """Lightweight metrics for free-creation multi-frame tasks (no reference).

    Used by text2pixelart tasks with ``num_frames > 1``: the model invents
    the frames (e.g. a slash or explosion effect), so there is no hidden
    target to compare against.  We still measure structural sanity:

    - frame_count / frame_count_match: expected vs produced frames
    - frame_coverage: mean non-transparent pixel fraction per frame
    - inter_frame_diff: fraction of pixels that change between adjacent
      frames (motion; 0 = identical frames, which usually means the agent
      did not actually animate)
    """
    if not pred_frames:
        return {"frame_count": 0, "frame_count_match": False}
    covs, diffs = [], []
    for f in pred_frames:
        total = f.matrix.size
        non_empty = int((f.matrix != f.transparent_id).sum())
        covs.append(non_empty / total if total else 0.0)
    for i in range(len(pred_frames) - 1):
        p0, p1 = pred_frames[i], pred_frames[i + 1]
        if p0.matrix.shape != p1.matrix.shape:
            diffs.append(0.0)
            continue
        diffs.append(float((p0.matrix != p1.matrix).mean()))
    return {
        "frame_count": len(pred_frames),
        "frame_count_match": bool(expected) and len(pred_frames) == int(expected),
        "frame_coverage": round(float(np.mean(covs)), 4) if covs else 0.0,
        "inter_frame_diff": round(float(np.mean(diffs)), 4) if diffs else 0.0,
    }


def _frame_box(canvas: PixelCanvas):
    """Visible-pixel bounding box of a canvas (``None`` when fully transparent)."""
    from pixelbench.tasks.edit_protocol import visible_box

    alpha = np.asarray([color.rgba[3] for color in canvas.palette], dtype=np.uint8)
    flat = alpha[canvas.matrix.reshape(-1)]
    return visible_box(canvas.width, canvas.height, lambda i: bool(flat[i]))


def compute_metrics(task: TaskSpec, canvas: PixelCanvas, result=None, obs_calls: Optional[List[dict]] = None) -> Dict[str, Any]:
    outputs = list(getattr(result, 'final_frames', None) or [canvas])
    errors = []
    palettes = []
    expected = max(1, task.num_frames or 1)
    shapes = []
    boxes = []
    for i, output in enumerate(outputs):
        errors.extend(f'output {i+1}: {e}' for e in validate_canvas(output)['errors'])
        palettes.append(palette_discipline(output, task.max_colors))
        if task.task_type == 'edit':
            # no size cap on edit output: any canvas the agent chooses is valid,
            # only the technical crash guard applies
            from pixelbench.tasks.edit_protocol import validate_edit_size
            try:
                validate_edit_size(output.width, output.height)
            except ValueError as error:
                errors.append(f'output {i+1}: {error}')
        elif (output.width, output.height) != (task.width, task.height):
            errors.append(f'output {i+1}: size {output.width}x{output.height} != task {task.width}x{task.height}')
        shapes.append((output.width, output.height))
        boxes.append(_frame_box(output))
    if task.task_type == 'edit':
        # one sequence must share a geometry and keep the subject at one scale
        from pixelbench.tasks.edit_protocol import sequence_errors
        errors.extend(f'sequence: {e}' for e in sequence_errors(shapes, boxes))
    if len(outputs) != expected:
        errors.append(f'expected {expected} outputs, got {len(outputs)}')
    metrics = {'validity': {'valid': not errors, 'errors': errors},
               'palette': palettes[-1], 'output_palettes': palettes,
               'submission': {**(getattr(result, 'submission', None) or {}),
                              'expected_count': expected, 'actual_count': len(outputs),
                              'count_match': len(outputs) == expected}}
    transcript = (result.transcript if result is not None else [])
    if task.task_type == "replication" and task.reference is not None:
        metrics["replication"] = replication_metrics(canvas, task.reference)
    elif task.task_type == "restoration" and task.reference is not None and task.mask is not None:
        corrupted = task.reference.copy()
        corrupted.matrix[task.mask] = corrupted.transparent_id
        metrics["restoration"] = restoration_metrics(canvas, task.reference, task.mask, corrupted)
    elif task.task_type == "edit" and task.base is not None:
        # hard metric for edit: how much of the canvas the agent actually
        # touched (focused edits change little) — the instruction-fidelity
        # judgement itself stays with the LLM judge (no hidden target).
        metrics["edit"] = edit_metrics(canvas, task.base)
        if task.frames:
            # Multi-frame edit WITH a hidden target sequence (e.g. "draw this
            # character turned +/-45 and from behind"): score the produced
            # frames against the GT frames, frame by frame.  Additive — the
            # edit metric above and the judge are unchanged.
            pred_frames = (
                result.final_frames if result is not None and result.final_frames else [canvas]
            )
            metrics["edit_frames"] = animation_metrics(pred_frames, task.frames, rgba=True, variable_size=True)
    elif task.task_type == "animation" and task.frames:
        pred_frames = (result.final_frames if result is not None and result.final_frames else [canvas])
        metrics["animation"] = animation_metrics(pred_frames, task.frames, rgba=True)
    elif (task.num_frames or 0) > 1:
        # text2pixelart multi-frame: free creation, structural sanity only
        pred_frames = (result.final_frames if result is not None and result.final_frames else [canvas])
        metrics["multiframe"] = freeform_multiframe_metrics(pred_frames, expected=task.num_frames)
    if task.task_type in ("agentic_creation", "replication", "restoration", "edit", "animation"):
        metrics["agentic"] = agentic_metrics(canvas, transcript, obs_calls=obs_calls)
    return metrics
