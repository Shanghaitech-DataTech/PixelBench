"""Task specification for the four benchmark task types.

The spec is the *complete* description of a task, including hidden eval
information (reference / target).  The runner splits it into what the
model may see (``public_task`` + ``initial_state`` + visible
reference/mask) and what stays hidden (``hidden_eval``).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np

from pixelbench.core.canvas import PixelCanvas
from pixelbench.core.color import Palette
from pixelbench.core.serialization import from_pixel_json, to_pixel_json

TASK_TYPES = ("agentic_creation", "replication", "restoration", "edit", "animation")


@dataclass
class TaskSpec:
    id: str
    task_type: str
    prompt: str
    width: int
    height: int
    max_colors: int = 16
    transparent_background: bool = True
    initial_palette: List[dict] = field(default_factory=list)
    reference: Optional[PixelCanvas] = None
    mask: Optional[np.ndarray] = None
    reference_visible: bool = False
    # edit tasks: the full input image the model starts from (visible in the
    # canvas; the judge compares against it).  No hidden target image exists
    # yet — judging is instruction-vs-original based.
    base: Optional[PixelCanvas] = None
    # animation: target/reference frame sequence the model must reproduce
    # or continue (frames_visible controls whether they may see them).
    frames: List[PixelCanvas] = field(default_factory=list)
    num_frames: int = 0
    frames_visible: bool = False
    tool_budget: Dict[str, Any] = field(
        default_factory=lambda: {"max_steps": 60, "max_seconds": 600}
    )
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.task_type not in TASK_TYPES:
            raise ValueError(f"unknown task_type {self.task_type!r}; expected one of {TASK_TYPES}")
        if self.width <= 0 or self.height <= 0:
            raise ValueError(f"task {self.id}: bad size {self.width}x{self.height}")
        if self.base is not None and (
            self.base.width != self.width or self.base.height != self.height
        ):
            raise ValueError(
                f"task {self.id}: base canvas {self.base.width}x{self.base.height} "
                f"!= canvas {self.width}x{self.height}"
            )
        if self.task_type == "edit" and self.base is not None:
            from pixelbench.tasks.edit_protocol import crop_edit_input
            original_size = (self.width, self.height)
            self.base, box = crop_edit_input(self.base)
            self.width, self.height = self.base.width, self.base.height
            if original_size != (self.width, self.height):
                self.metadata = dict(self.metadata, input_original_size=list(original_size),
                                     input_crop_box=list(box))
        if self.mask is not None and self.mask.shape != (self.height, self.width):
            raise ValueError(
                f"task {self.id}: mask shape {self.mask.shape} != canvas {self.width}x{self.height}"
            )
        if self.task_type == "animation":
            if not self.num_frames:
                self.num_frames = len(self.frames)
            if self.frames and any(
                f.width != self.width or f.height != self.height for f in self.frames
            ):
                raise ValueError(
                    f"task {self.id}: animation frames must match {self.width}x{self.height}"
                )

    # -- views ---------------------------------------------------------
    def public_task(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "id": self.id,
            "task_type": self.task_type,
            "prompt": self.prompt,
            "width": self.width,
            "height": self.height,
            "constraints": {
                "max_colors": self.max_colors,
                "transparent_background": self.transparent_background,
            },
            "allow_reference": bool(self.reference_visible),
            "tool_budget": dict(self.tool_budget),
        }
        if self.task_type == "edit":
            d["constraints"]["max_colors"] = None
            d["input_size"] = {"width": self.width, "height": self.height}
            d["output_size"] = "agent_defined"
        if self.task_type in ("animation", "edit") or (self.num_frames or 0) > 1:
            # edit tasks always declare num_frames: a single-frame edit would
            # otherwise round-trip through task.json as 0.
            d["num_frames"] = int(self.num_frames or len(self.frames) or 1)
            d["frames_visible"] = bool(self.frames_visible)
        return d

    def initial_state(self) -> Dict[str, Any]:
        """The canvas state handed to the model at episode start."""
        canvas = PixelCanvas(self.width, self.height, transparent_id=0, max_colors=self.max_colors)
        for entry in self.initial_palette:
            canvas.register_color(entry["name"], entry.get("rgba") or entry.get("hex"))
        if self.task_type == "restoration" and self.reference is not None and self.mask is not None:
            canvas = self.reference.copy()
            fill_id = canvas.transparent_id
            canvas.matrix[self.mask] = fill_id
            canvas._version = 0
            canvas._edit_log.clear()
        elif self.task_type == "edit" and self.base is not None:
            # edit tasks: the model starts from the FULL input image
            canvas = self.base.copy()
            canvas._version = 0
            canvas._edit_log.clear()
        meta = {"task_type": self.task_type}
        if self.task_type == "animation" or (self.num_frames or 0) > 1:
            meta["num_frames"] = int(self.num_frames or len(self.frames))
        return to_pixel_json(canvas, id_=self.id, metadata=meta)

    def reference_state(self) -> Optional[Dict[str, Any]]:
        if self.reference is None:
            return None
        return to_pixel_json(self.reference, id_=self.id + "_reference")

    def mask_state(self) -> Optional[Dict[str, Any]]:
        if self.mask is None:
            return None
        box = mask_bbox(self.mask)
        return {
            "width": self.width,
            "height": self.height,
            "box": box,
            "mask": [[int(bool(v)) for v in row] for row in self.mask.tolist()],
        }

    def hidden_eval(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {"task_id": self.id, "task_type": self.task_type}
        if self.reference is not None:
            d["reference"] = to_pixel_json(self.reference, id_=self.id + "_target")
        if self.mask is not None:
            d["mask_box"] = mask_bbox(self.mask)
        # GT frame sequences: animation targets, and (since a multi-frame edit
        # can also carry a hidden target) any task that declares ``frames``.
        if self.frames:
            d["frames"] = [
                to_pixel_json(f, id_=f"{self.id}_target_frame_{i}")
                for i, f in enumerate(self.frames)
            ]
        return d

    # -- disk I/O ------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "id": self.id,
            "task_type": self.task_type,
            "prompt": self.prompt,
            "width": self.width,
            "height": self.height,
            "max_colors": self.max_colors,
            "transparent_background": self.transparent_background,
            "initial_palette": self.initial_palette,
            "reference_visible": self.reference_visible,
            "num_frames": self.num_frames,
            "frames_visible": self.frames_visible,
            "tool_budget": self.tool_budget,
            "metadata": self.metadata,
        }
        if self.reference is not None:
            d["reference"] = to_pixel_json(self.reference, id_=self.id + "_reference")
        if self.base is not None:
            d["base"] = to_pixel_json(self.base, id_=self.id + "_base")
        if self.mask is not None:
            d["mask"] = [[int(bool(v)) for v in row] for row in self.mask.tolist()]
        if self.frames:
            d["frames"] = [
                to_pixel_json(f, id_=f"{self.id}_frame_{i}") for i, f in enumerate(self.frames)
            ]
        return d

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "TaskSpec":
        reference = from_pixel_json(d["reference"]) if d.get("reference") else None
        base = from_pixel_json(d["base"]) if d.get("base") else None
        mask = None
        if d.get("mask"):
            mask = np.array(d["mask"], dtype=bool)
        frames = [from_pixel_json(f) for f in d.get("frames", [])] if d.get("frames") else []
        return cls(
            id=d["id"],
            task_type=d["task_type"],
            prompt=d["prompt"],
            width=int(d["width"]),
            height=int(d["height"]),
            max_colors=int(d.get("max_colors", 16)),
            transparent_background=bool(d.get("transparent_background", True)),
            initial_palette=list(d.get("initial_palette", [])),
            reference=reference,
            mask=mask,
            reference_visible=bool(d.get("reference_visible", False)),
            base=base,
            frames=frames,
            num_frames=int(d.get("num_frames", 0)),
            frames_visible=bool(d.get("frames_visible", False)),
            tool_budget=dict(d.get("tool_budget", {"max_steps": 60, "max_seconds": 600})),
            metadata=dict(d.get("metadata", {})),
        )


def mask_bbox(mask: np.ndarray) -> Optional[List[int]]:
    ys, xs = np.nonzero(mask)
    if len(ys) == 0:
        return None
    return [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]


def _json_default(o: Any) -> Any:
    """Coerce numpy scalars/arrays for JSON serialization."""
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not JSON serializable: {type(o)}")


def _dumps(obj: Any, **kw) -> str:
    return json.dumps(obj, ensure_ascii=False, default=_json_default, **kw)


def save_task_dir(spec: TaskSpec, path: Path) -> None:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    (path / "task.json").write_text(_dumps(spec.public_task(), indent=2))
    (path / "initial.pixel.json").write_text(
        _dumps(spec.initial_state(), indent=2)
    )
    if spec.reference_state() is not None:
        (path / "reference.pixel.json").write_text(
            _dumps(spec.reference_state(), indent=2)
        )
        from pixelbench.core.render import render_png_bytes

        (path / "reference.png").write_bytes(
            render_png_bytes(spec.reference, scale=8)
        )
    if spec.mask_state() is not None:
        (path / "mask.json").write_text(_dumps(spec.mask_state(), indent=2))
        from pixelbench.core.render import render_png_bytes

        mask_canvas = PixelCanvas(spec.width, spec.height)
        mask_canvas.matrix[:] = np.where(spec.mask, 2, 0)
        mask_canvas.register_color("red", "#ff2020")
        (path / "mask.png").write_bytes(render_png_bytes(mask_canvas, scale=8))
    if spec.base is not None:
        from pixelbench.core.render import render_png_bytes

        (path / "base.pixel.json").write_text(
            _dumps(to_pixel_json(spec.base, id_=spec.id + "_base"), indent=2)
        )
        (path / "base.png").write_bytes(render_png_bytes(spec.base, scale=8))
    if spec.frames:
        from pixelbench.core.render import render_png_bytes

        frames_dir = path / "frames"
        frames_dir.mkdir(parents=True, exist_ok=True)
        for i, f in enumerate(spec.frames):
            (frames_dir / f"frame_{i:03d}.pixel.json").write_text(
                _dumps(to_pixel_json(f, id_=f"{spec.id}_frame_{i}"), indent=2)
            )
            (frames_dir / f"frame_{i:03d}.png").write_bytes(render_png_bytes(f, scale=8))
        if spec.frames_visible:
            sheet = None
            from pixelbench.core.render import render_pil
            from PIL import Image as _Image

            n = len(spec.frames)
            cell_w = max(f.width for f in spec.frames) * 8
            cell_h = max(f.height for f in spec.frames) * 8
            import math

            cols = min(n, 8)
            rows = math.ceil(n / cols)
            sheet = _Image.new("RGBA", (cols * cell_w, rows * cell_h), (40, 40, 40, 255))
            for i, f in enumerate(spec.frames):
                frame_img = render_pil(f, scale=8)
                sheet.paste(frame_img, ((i % cols) * cell_w, (i // cols) * cell_h), frame_img)
            sheet.save(path / "frames_contact_sheet.png")
    (path / "hidden_eval.json").write_text(_dumps(spec.hidden_eval(), indent=2))
    (path / "metadata.json").write_text(_dumps(spec.metadata, indent=2))


def load_task_dir(path: Path) -> TaskSpec:
    path = Path(path)
    task_json = json.loads((path / "task.json").read_text())
    initial = json.loads((path / "initial.pixel.json").read_text())
    ref = None
    ref_file = path / "reference.pixel.json"
    if ref_file.exists():
        ref = from_pixel_json(json.loads(ref_file.read_text()))
    mask = None
    mask_file = path / "mask.json"
    if mask_file.exists():
        mask = np.array(json.loads(mask_file.read_text())["mask"], dtype=bool)
    base = None
    base_file = path / "base.pixel.json"
    if base_file.exists():
        base = from_pixel_json(json.loads(base_file.read_text()))
    frames = []
    frames_dir = path / "frames"
    if frames_dir.exists():
        for fp in sorted(frames_dir.glob("frame_*.pixel.json")):
            frames.append(from_pixel_json(json.loads(fp.read_text())))
    return TaskSpec(
        id=task_json["id"],
        task_type=task_json["task_type"],
        prompt=task_json["prompt"],
        width=int(task_json["width"]),
        height=int(task_json["height"]),
        max_colors=int(task_json.get("constraints", {}).get("max_colors", 16) or 0),
        transparent_background=bool(
            task_json.get("constraints", {}).get("transparent_background", True)
        ),
        reference=ref,
        mask=mask,
        reference_visible=bool(task_json.get("allow_reference", False)),
        base=base,
        frames=frames,
        num_frames=int(task_json.get("num_frames", 0)),
        frames_visible=bool(task_json.get("frames_visible", False)),
        tool_budget=dict(task_json.get("tool_budget", {"max_steps": 60, "max_seconds": 600})),
        metadata=(json.loads((path / "metadata.json").read_text())
                  if (path / "metadata.json").exists() else {}),
    )


def load_tasks_from_dir(path) -> List[TaskSpec]:
    """Load every task dir under ``path``.

    Accepts both flat layouts (``<path>/<task_id>/task.json``) and the
    nested layout produced by ``gen-tasks`` (``<path>/<type>/<task_id>/``).
    """
    path = Path(path)
    specs: List[TaskSpec] = []
    candidates = []
    if (path / "task.json").exists():
        candidates.append(path)
    candidates += [p.parent for p in path.glob("*/task.json")]
    candidates += [p.parent for p in path.glob("*/*/task.json")]
    for task_dir in sorted(candidates):
        try:
            specs.append(load_task_dir(task_dir))
        except Exception as e:  # pragma: no cover
            print(f"[pixelbench] skip {task_dir.name}: {e}")
    return specs
