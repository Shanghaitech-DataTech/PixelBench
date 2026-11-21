"""Run report: per-episode records, aggregation, artifacts on disk."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
from PIL import Image, ImageDraw


@dataclass
class EpisodeRecord:
    task_id: str
    task_type: str
    agent: str
    ok: bool
    steps: int = 0
    error: Optional[str] = None
    metrics: Dict[str, Any] = field(default_factory=dict)
    judge: Optional[Dict[str, Any]] = None
    images: Dict[str, bytes] = field(default_factory=dict)
    transcript: List[Dict[str, Any]] = field(default_factory=list)
    submission: Dict[str, Any] = field(default_factory=dict)
    episode_dir: Optional[str] = None  # set when observations are enabled

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "agent": self.agent,
            "ok": self.ok,
            "steps": self.steps,
            "error": self.error,
            "metrics": self.metrics,
            "submission": self.submission,
            "judge": self.judge,
            "images": {k: f"{k}.png" for k in self.images},
            "trace": "trace.jsonl",
        }


def save_episode(out_dir: Path, rec: EpisodeRecord) -> None:
    """Persist one episode's artifacts (final images, record.json,
    trace.jsonl, process viewer) under ``out_dir/episodes/``.

    Used both by :meth:`RunReport.save` and directly by the runner right
    after each episode finishes, so an interrupted run still keeps the
    episodes that completed.
    """
    out_dir = Path(out_dir)
    episodes_dir = out_dir / "episodes"
    episodes_dir.mkdir(parents=True, exist_ok=True)
    d = Path(rec.episode_dir) if rec.episode_dir else episodes_dir / f"{rec.task_id}__{rec.agent}"
    d.mkdir(parents=True, exist_ok=True)
    for name, png in rec.images.items():
        (d / f"{name}.png").write_bytes(png)
    payload = rec.to_dict()
    if rec.episode_dir is not None:
        # observations were written live by the kernel during the run
        from pixelbench.observe import collect_observation_stats

        stats = collect_observation_stats(Path(rec.episode_dir))
        if stats:
            payload["observations"] = stats
    (d / "record.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    if rec.transcript:
        with (d / "trace.jsonl").open("w", encoding="utf-8") as fh:
            for step in rec.transcript:
                fh.write(json.dumps(step, ensure_ascii=False, default=str) + "\n")
    if rec.episode_dir is not None:
        from pixelbench.observe import write_process_viewer

        write_process_viewer(d)


class RunReport:
    def __init__(self, run_id: str, records: List[EpisodeRecord], config: Optional[dict] = None) -> None:
        self.run_id = run_id
        self.records = records
        self.config = config or {}
        self.out_dir: Optional[Path] = None

    # -- aggregation ---------------------------------------------------
    def summary(self) -> Dict[str, Any]:
        types = sorted({r.task_type for r in self.records})
        agents = sorted({r.agent for r in self.records})
        out: Dict[str, Any] = {"run_id": self.run_id}
        for t in types:
            out[t] = {}
            for a in agents:
                recs = [r for r in self.records if r.task_type == t and r.agent == a]
                if not recs:
                    continue
                entry: Dict[str, Any] = {"n": len(recs), "ok": sum(1 for r in recs if r.ok)}
                # collect scalar metric paths
                scalars: Dict[str, List[float]] = {}
                for r in recs:
                    _collect_scalars(r.metrics, scalars)
                entry["metrics"] = {k: round(float(np.mean(v)), 4) for k, v in scalars.items() if v}
                if any(r.judge for r in recs):
                    judge_dims: Dict[str, List[float]] = {}
                    for r in recs:
                        if r.judge:
                            for name, d in (r.judge.get("dims") or {}).items():
                                judge_dims.setdefault(name, []).append(float(d["score"]))
                    entry["judge"] = {k: round(float(np.mean(v)), 4) for k, v in judge_dims.items() if v}
                out[t][a] = entry
        return out

    # -- disk ----------------------------------------------------------
    def save(self, out_dir: Path) -> Path:
        out_dir = Path(out_dir)
        self.out_dir = out_dir
        episodes_dir = out_dir / "episodes"
        episodes_dir.mkdir(parents=True, exist_ok=True)
        for rec in self.records:
            save_episode(out_dir, rec)
        summary = self.summary()
        (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
        (out_dir / "summary.md").write_text(self._markdown(summary), encoding="utf-8")
        self._contact_sheet(out_dir)
        self._gallery(out_dir)
        return out_dir

    def _gallery(self, out_dir: Path) -> None:
        """Simple run-level gallery linking each episode's process viewer."""
        cards = []
        for rec in self.records:
            d = Path(rec.episode_dir) if rec.episode_dir else out_dir / "episodes" / f"{rec.task_id}__{rec.agent}"
            figs = "".join(
                f'<figure><img src="episodes/{d.name}/{n}.png"><figcaption>{n}.png</figcaption></figure>'
                for n in ("reference", "corrupted", "final", "final_1x")
                if (d / f"{n}.png").is_file()
            )
            viewer = ""
            if (d / "process.html").is_file():
                viewer = f' · <a href="episodes/{d.name}/process.html" style="color:#7bd">process viewer</a>'
            cards.append(
                f'<div class="card"><h3>{rec.task_id} <span class="tag">{rec.agent}</span>'
                f'{" <span style=\"color:#f79\">FAIL</span>" if not rec.ok else ""}{viewer}</h3>'
                f'<div class="imgs">{figs}</div></div>'
            )
        html = (
            "<!DOCTYPE html><html><head><meta charset=\"utf-8\">"
            "<title>PixelBench outputs</title><style>"
            "body{background:#1c1c22;color:#ddd;font-family:system-ui,sans-serif;margin:24px}"
            "h1{font-size:20px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}"
            ".card{background:#26262e;border-radius:10px;padding:14px}h3{margin:0 0 10px;font-size:14px}"
            ".tag{color:#7bd;font-weight:normal}.imgs{display:flex;flex-wrap:wrap;gap:12px}"
            "figure{margin:0}img{image-rendering:pixelated;background:repeating-conic-gradient(#3a3a44 0% 25%,#2a2a32 0% 50%) 0 0/16px 16px;border-radius:6px;border:1px solid #444;max-width:220px}"
            "figcaption{font-size:11px;color:#889;margin-top:4px;text-align:center}"
            "</style></head><body>"
            f"<h1>PixelBench run — {out_dir.name}</h1>"
            f'<p style="font-size:12px;color:#889"><a href="summary.md" style="color:#7bd">summary.md</a> · '
            f'<a href="summary.json" style="color:#7bd">summary.json</a> · '
            f'<a href="contact_sheet.png" style="color:#7bd">contact_sheet.png</a></p>'
            f'<div class="grid">{"".join(cards)}</div></body></html>'
        )
        (out_dir / "gallery.html").write_text(html, encoding="utf-8")

    def _markdown(self, summary: dict) -> str:
        lines = [f"# PixelBench run `{self.run_id}`", ""]
        for t, agents in summary.items():
            if t == "run_id":
                continue
            lines.append(f"## {t}")
            lines.append("")
            lines.append("| agent | n | ok | metrics | judge |")
            lines.append("|---|---|---|---|---|")
            for a, entry in agents.items():
                m = ", ".join(f"{k}={v}" for k, v in entry.get("metrics", {}).items())
                # runs without a judge ("judge": {"type": "none"}) show a placeholder in the judge column
                j = ", ".join(f"{k}={v}" for k, v in entry.get("judge", {}).items()) or "—"
                lines.append(f"| {a} | {entry['n']} | {entry['ok']} | {m} | {j} |")
            lines.append("")
        return "\n".join(lines)

    def _contact_sheet(self, out_dir: Path) -> None:
        """Grid: rows = agents, cols = tasks; each cell shows final.png."""
        agents = sorted({r.agent for r in self.records})
        tasks = sorted({r.task_id for r in self.records})
        cell = 64 * 4 + 24  # 64px max dimension @4x + label
        pad = 6
        label_h = 16
        img = Image.new("RGB", (len(tasks) * cell + pad, len(agents) * (cell + label_h) + pad), (30, 30, 34))
        draw = ImageDraw.Draw(img)
        lookup = {(r.task_id, r.agent): r for r in self.records}
        for ai, a in enumerate(agents):
            draw.text((pad, pad + ai * (cell + label_h) + 2), a, fill=(200, 200, 210))
            for ti, t in enumerate(tasks):
                x0 = pad + ti * cell
                y0 = pad + ai * (cell + label_h) + label_h
                draw.text((x0 + 2, y0 - label_h + 2), t, fill=(160, 160, 170))
                rec = lookup.get((t, a))
                thumb = None
                if rec and rec.images.get("final"):
                    thumb = Image.open(__import__("io").BytesIO(rec.images["final"]))
                    thumb = thumb.convert("RGBA")
                    bg = Image.new("RGBA", thumb.size, (30, 30, 34))
                    bg.alpha_composite(thumb)
                    thumb = bg.convert("RGB")
                    thumb.thumbnail((cell - pad * 2, cell - pad * 2), Image.NEAREST)
                if thumb:
                    img.paste(thumb, (x0 + pad, y0 + pad))
                else:
                    draw.rectangle([x0 + pad, y0 + pad, x0 + cell - pad, y0 + cell - pad], outline=(120, 60, 60))
        img.save(out_dir / "contact_sheet.png")


def _collect_scalars(d: dict, out: Dict[str, List[float]], prefix: str = "") -> None:
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            _collect_scalars(v, out, key)
        elif isinstance(v, (int, float)) and not isinstance(v, bool):
            out.setdefault(key, []).append(float(v))
