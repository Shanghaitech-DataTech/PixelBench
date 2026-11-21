"""LLM-as-Judge scoring of pixel-art quality.

The judge receives rendered images (final at several scales, plus
reference / corrupted / mask when relevant), the prompt and the rubric,
and returns per-dimension 1..5 scores with reasons.  A deterministic
:class:`MockJudge` is provided for offline tests and CI.
"""
from __future__ import annotations

import base64
import json
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import numpy as np

from pixelbench.agents.chat import LLMClient
from pixelbench.core.canvas import PixelCanvas
from pixelbench.eval.preprocess import judge_image
from pixelbench.tasks.specs import TaskSpec

COMMON_DIMS = [
    ("prompt_alignment", "Does the art match the requested subject, size and constraints?"),
    ("pixel_art_authenticity", "Does it look like genuine pixel art (clean pixel clusters, limited palette) rather than a blurred low-res image?"),
    ("readability", "Is the subject recognizable at native resolution?"),
    ("composition", "Proportions, pose, silhouette and overall balance."),
    ("palette_quality", "Deliberate color choices, shading and contrast."),
    ("asset_usability", "Could it be used directly as a game asset (clean edges, no stray noisy pixels, consistent style)?"),
]
REPLICATION_DIMS = COMMON_DIMS + [("fidelity", "How closely it matches the reference in structure, colors and details.")]
RESTORATION_DIMS = COMMON_DIMS + [("seamless_repair", "Does the repaired region blend with the untouched surroundings without seams or artifacts?")]
EDIT_DIMS = COMMON_DIMS + [
    ("instruction_following", "Does the result apply the requested edit to the correct object/region with the correct change?"),
    ("minimal_edit", "Does everything the instruction did not ask to change stay exactly the same as the original?"),
]


@dataclass
class EpisodeView:
    task: TaskSpec
    agent_name: str
    final_canvas: Optional[PixelCanvas] = None
    reference: Optional[PixelCanvas] = None
    corrupted: Optional[PixelCanvas] = None
    mask: Optional[np.ndarray] = None
    original: Optional[PixelCanvas] = None
    metrics: Dict[str, Any] = field(default_factory=dict)
    final_frames: List[PixelCanvas] = field(default_factory=list)


def dims_for(task_type: str) -> List[tuple]:
    if task_type == "replication":
        return REPLICATION_DIMS
    if task_type == "restoration":
        return RESTORATION_DIMS
    if task_type == "edit":
        return EDIT_DIMS
    return COMMON_DIMS


class Judge(ABC):
    @abstractmethod
    def score(self, episode: EpisodeView) -> Dict[str, Any]: ...


def _clamp5(x: float) -> float:
    return round(max(1.0, min(5.0, x)), 2)


class MockJudge(Judge):
    """Deterministic heuristic judge: maps hard metrics to rubric scores.

    Only used for tests / demos; the real benchmark uses :class:`LLMJudge`
    (or a human-calibrated model judge).
    """

    def score(self, episode: EpisodeView) -> Dict[str, Any]:
        dims: Dict[str, dict] = {}
        ttype = episode.task.task_type
        m = episode.metrics
        if ttype == "replication":
            rep = m.get("replication", {})
            acc = rep.get("pixel_accuracy", 0.0)
            dims["fidelity"] = {"score": _clamp5(1 + 4 * acc), "reason": f"pixel_accuracy={acc}"}
            dims["pixel_art_authenticity"] = {
                "score": _clamp5(2 + 3 * rep.get("palette_recall", 0.0)),
                "reason": "palette_recall heuristic",
            }
            dims["prompt_alignment"] = {"score": _clamp5(1 + 4 * acc), "reason": "mock heuristic"}
        elif ttype == "restoration":
            res = m.get("restoration", {})
            dims["seamless_repair"] = {
                "score": _clamp5(1 + 4 * res.get("region_accuracy", 0.0)),
                "reason": "region_accuracy heuristic",
            }
            dims["prompt_alignment"] = {
                "score": _clamp5(5 - 4 * res.get("protected_change_rate", 1.0)),
                "reason": "protected_change_rate heuristic",
            }
            dims["pixel_art_authenticity"] = {"score": 3.0, "reason": "mock heuristic"}
        elif ttype == "edit":
            # edit has no hidden target image; mock judge scores on the
            # fraction of the canvas the agent actually changed (rough
            # proxy for a focused edit) + agentic coverage
            ag = m.get("agentic", {})
            changed = m.get("edit", {}).get("changed_px", 0)
            total = episode.task.width * episode.task.height
            focus = 1.0 - min(1.0, (changed or 0) / max(1, total))
            dims["instruction_following"] = {
                "score": _clamp5(1 + 4 * ag.get("coverage_pct", 0.0) / 100.0),
                "reason": "coverage heuristic",
            }
            dims["minimal_edit"] = {"score": _clamp5(1 + 4 * focus), "reason": f"changed {changed}/{total} px"}
            dims["prompt_alignment"] = {"score": _clamp5(1 + 4 * ag.get("coverage_pct", 0.0) / 100.0), "reason": "mock heuristic"}
            dims["pixel_art_authenticity"] = {"score": 3.0, "reason": "mock heuristic"}
        else:
            ag = m.get("agentic", {})
            coverage = ag.get("coverage_pct", 0.0) / 100.0
            dims["prompt_alignment"] = {"score": _clamp5(1 + 4 * coverage), "reason": "coverage heuristic"}
            dims["pixel_art_authenticity"] = {
                "score": _clamp5(2 + 2 * min(1.0, coverage + 0.2)),
                "reason": "mock heuristic",
            }
        for name, _desc in dims_for(ttype):
            dims.setdefault(name, {"score": 3.0, "reason": "mock judge: no visual signal"})
        scores = [d["score"] for d in dims.values()]
        return {"dims": dims, "overall": round(float(np.mean(scores)), 2), "judge": "mock"}


JUDGE_SYSTEM_PROMPT = """You are an expert judge for pixel-art quality in a game-asset benchmark.
Score each dimension from 1 (very poor) to 5 (excellent) and give a one-sentence reason.
Respond with ONLY a JSON object: {"scores": {"<dim>": {"score": <1-5>, "reason": "<text>"}}, "overall": <1-5>}
"""


def _png_part(png: bytes, caption: str) -> dict:
    return {
        "type": "text",
        "text": caption,
    }, {
        "type": "image_url",
        "image_url": {"url": f"data:image/png;base64,{base64.b64encode(judge_image(png)).decode()}"},
    }


class LLMJudge(Judge):
    def __init__(self, llm: Optional[LLMClient] = None, model: Optional[str] = None, temperature: float = 0.2) -> None:
        if llm is None:
            llm = LLMClient.from_config({"model": model or "gpt-4o", "temperature": temperature})
        self.llm = llm

    def score(self, episode: EpisodeView) -> Dict[str, Any]:
        dims = dims_for(episode.task.task_type)
        parts: List[dict] = []
        parts.append(
            {
                "type": "text",
                "text": (
                    f"Task: {episode.task.task_type} | Agent: {episode.agent_name}\n"
                    f"Prompt: {episode.task.prompt}\n" +
                    (f"Input size: {episode.task.width}x{episode.task.height}; max colors {episode.task.max_colors}. "
                     "Output canvas dimensions are agent-chosen. Do not penalize different canvas dimensions "
                     "or transparent margins by themselves; judge requested changes and preservation of "
                     "unrelated content.\n"
                     if episode.task.task_type == "edit" else
                     f"Size: {episode.task.width}x{episode.task.height}, max colors {episode.task.max_colors}\n") +
                    f"Dimensions to score: {[d for d, _ in dims]}\n"
                    "Images: [final render at 8x, native 1x]"
                ),
            }
        )
        if len(episode.final_frames) > 1:
            labels = episode.task.metadata.get('frame_order') or []
            for i, canvas in enumerate(episode.final_frames):
                label = labels[i] if isinstance(labels, list) and i < len(labels) else ''
                parts.extend(_png_part(canvas.render_png_bytes(scale=8), f'output {i+1}/{len(episode.final_frames)} {label} (8x)'))
                parts.extend(_png_part(canvas.render_png_bytes(scale=1), f'output {i+1} (1x)'))
        elif episode.final_canvas is not None:
            parts.extend(_png_part(episode.final_canvas.render_png_bytes(scale=8), "final (8x)"))
            parts.extend(_png_part(episode.final_canvas.render_png_bytes(scale=1), "final (1x)"))
        if episode.reference is not None:
            parts.extend(_png_part(episode.reference.render_png_bytes(scale=8), "reference (8x)"))
        if episode.original is not None:
            parts.extend(_png_part(episode.original.render_png_bytes(scale=8), "original input (8x)"))
        if episode.corrupted is not None:
            parts.extend(_png_part(episode.corrupted.render_png_bytes(scale=8), "corrupted input"))
        if episode.mask is not None:
            parts.append(
                {
                    "type": "text",
                    "text": (
                        f"Editable mask covers {float(episode.mask.mean()) * 100:.1f}% of the canvas; "
                        "pixels outside the mask must not change."
                    ),
                }
            )
        resp = self.llm.chat(
            [
                {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
                {"role": "user", "content": parts},
            ],
            response_format={"type": "json_object"},
        )
        text = resp.choices[0].message.content or "{}"
        data = _parse_judge_json(text)
        parsed = data.get("scores", data)
        out_dims: Dict[str, dict] = {}
        for name, _ in dims:
            entry = parsed.get(name) or {}
            if isinstance(entry, (int, float)):
                out_dims[name] = {"score": _clamp5(float(entry)), "reason": ""}
            else:
                out_dims[name] = {"score": _clamp5(float(entry.get("score", 3))), "reason": str(entry.get("reason", ""))}
        overall = data.get("overall")
        return {
            "dims": out_dims,
            "overall": _clamp5(float(overall)) if overall is not None else round(float(np.mean([d["score"] for d in out_dims.values()])), 2),
            "judge": self.llm.model,
            "raw": text,
        }


def _parse_judge_json(text: str) -> dict:
    text = (text or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE).strip()
    candidates = [text]
    # models sometimes drop a trailing brace (e.g. "...overall: 4}" with
    # the outer object unclosed)
    diff = text.count("{") - text.count("}")
    if diff > 0:
        candidates.append(text + "}" * diff)
    for cand in candidates:
        try:
            return json.loads(cand)
        except json.JSONDecodeError:
            pass
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return {}


class NullJudge(Judge):
    """Explicitly "no judge": calls no LLM and returns None.

    Useful for task types such as restore that **have ground truth and can be scored with
    deterministic metrics**: it saves the LLM cost and keeps the judge's subjective noise
    out of the scores. Configure it with ``"judge": {"type": "none"}``.
    """

    def score(self, episode: EpisodeView) -> None:  # noqa: D102
        return None


def build_judge(cfg: dict) -> Optional[Judge]:
    """None means this run uses no judge (deterministic metrics only)."""
    if cfg.get("type") in ("none", "null"):
        return None
    if cfg.get("type") == "mock":
        return MockJudge()
    return LLMJudge(llm=LLMClient.from_config(cfg.get("llm", cfg)) if cfg.get("llm") or cfg.get("model") else None, model=cfg.get("model"))
