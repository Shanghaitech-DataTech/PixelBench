#!/usr/bin/env python3
"""Direct-answer baseline: the model writes the artwork as a character grid in ONE answer.

No tools, no code execution, no observation and no second turn. The model receives the task
statement (and, for editing tasks, the input image encoded in the same text format) and answers
with a palette plus one code per pixel. The answer is parsed, rendered and stored in the layout of
data/creations/<config>/, so the judge scores it exactly like an agent's artwork.

    python scripts/run_direct.py --config configs/models/gpt-6-astra.json --out runs/gpt-6-astra.direct

Budget: one request of at most 131,072 tokens (reasoning included) and 60 minutes. An answer cut by
the token budget, a request past the time limit, or an answer that cannot be parsed into the required
number of frames counts as no valid answer (scored 0). Small grid slips are repaired and counted (see
parse_answer); larger ones invalidate the frame.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import re
import sys
import threading
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pixelbench.agents.chat import LLMClient, LLMError  # noqa: E402
from pixelbench.core.canvas import PixelCanvas  # noqa: E402
from pixelbench.tasks.specs import TaskSpec, load_task_dir  # noqa: E402

# One-character pixel codes: printable ASCII without whitespace, the transparent '.', and
# characters that tend to be escaped or read as markup.
SYMBOLS = [c for c in map(chr, range(33, 127)) if c not in ".#<>\"'\\`"]
ALNUM = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"]
MAX_TOKENS = 131072
PARSER_VERSION = 2
WALL_S = 3600.0

SYSTEM = """You are a pixel artist. In this task you draw by writing the image directly as text: there are no tools, no code execution and no second turn. Your single answer is parsed into the final artwork.

Answer format (exactly these markers, each on its own line):

PALETTE
<code> <colour>
...
END PALETTE
FRAME 1 <width>x<height>
<row 1>
...
<row height>
END FRAME

- Each pixel is written as a code of exactly {w} character(s). Every row is the concatenation of the codes of its pixels from left to right, with no spaces or separators, so a row has width x {w} characters. Write rows from top to bottom.
- {transparent} is reserved for a fully transparent pixel and needs no palette line. Every other code used in a frame must be declared in the palette as "<code> #RRGGBB" (or #RRGGBBAA for partial alpha).
- {codes}
- For several frames, write FRAME 1, FRAME 2, ... in order, each with its own rows and END FRAME. All frames share the one palette.
- Anything outside the PALETTE and FRAME blocks is ignored. Write the complete grid; do not abbreviate, elide or describe rows."""


def code_width(n_colors: int) -> int:
    return 1 if n_colors <= len(SYMBOLS) else 2


def codes_note(w: int) -> str:
    if w == 1:
        return "Codes are single printable ASCII characters other than whitespace and . # < > \" ' \\ `."
    return "Codes are two characters, each a letter or digit (A-Z, a-z, 0-9), for example Aa or 7Q."


def encode_canvas(c: PixelCanvas, w: int) -> Tuple[str, Dict[int, str]]:
    """Palette + rows for an input image, in the answer format."""
    ids = [int(i) for i in np.unique(c.matrix) if int(i) != c.transparent_id]
    pool = SYMBOLS if w == 1 else [a + b for a in ALNUM for b in ALNUM]
    code = {c.transparent_id: "." * w}
    lines = ["PALETTE"]
    for k, cid in enumerate(ids):
        code[cid] = pool[k]
        lines.append(f"{pool[k]} {c.palette[cid].to_hex()}")
    lines.append("END PALETTE")
    lines.append(f"FRAME 1 {c.width}x{c.height}")
    lines += ["".join(code[int(v)] for v in row) for row in c.matrix]
    lines.append("END FRAME")
    return "\n".join(lines), code


def user_text(task: TaskSpec, w: int, input_block: Optional[str]) -> str:
    n = max(1, task.num_frames or 1)
    parts = [task.prompt, "", f"Task: {task.id} ({task.task_type})."]
    if task.task_type == "edit":
        parts += [f"Input image: {task.width}x{task.height} px, given below in the answer format.",
                  "You may register any colours you need.",
                  "If the edit or motion needs a different canvas size, choose it: declare your size in each FRAME line. "
                  "All output frames should share the same size. The artwork and its parts may move as the action requires.",
                  f"Output exactly {n} frame(s) in task order. The input image is not automatically included: if the task "
                  "specifies the original image as frame 1, write that frame explicitly within this total.",
                  "", "INPUT IMAGE", input_block, "END INPUT IMAGE"]
    else:
        parts += [f"Required output: {task.width}x{task.height} px (exactly {task.height} rows of {task.width} pixels).",
                  f"Final visible-colour limit: {task.max_colors}; fully transparent pixels are free.",
                  f"Output exactly {n} frame(s)."]
    parts += ["", f"Pixel codes are {w} character(s) wide. Answer now in the required format."]
    return "\n".join(parts)


_HEX = re.compile(r"^#?([0-9a-fA-F]{6})([0-9a-fA-F]{2})?$")


def parse_answer(text: str, w: int, n_frames: int, size: Optional[Tuple[int, int]]) -> dict:
    """Parse palette and frames; repair small slips and count them.

    Parser v2. The palette block ends at END PALETTE or, if that marker is
    missing, at the first FRAME line. A row is repairable when its length is within
    max(2, 5%) of the width (padded with transparency or truncated). A frame is invalid when
    its row count differs from the height by more than max(2, 5%), when more than 20% of its
    rows are beyond that length tolerance, or when more than 5% of its pixels use undeclared
    codes (made transparent otherwise). v1 required END PALETTE and counted any length slip
    toward the 20%.
    """
    text = text.replace("\r", "")
    pal_m = list(re.finditer(r"^PALETTE\s*$(.*?)^(?:END PALETTE\s*$|(?=FRAME\s+\d))", text, re.S | re.M))
    if not pal_m:
        return {"ok": False, "reason": "no_palette"}
    palette: Dict[str, Tuple[int, int, int, int]] = {}
    for line in pal_m[-1].group(1).splitlines():
        bits = line.strip().split()
        if len(bits) < 2 or len(bits[0]) != w:
            continue
        m = _HEX.match(bits[1])
        if m:
            rgb = m.group(1)
            a = int(m.group(2), 16) if m.group(2) else 255
            palette[bits[0]] = (int(rgb[0:2], 16), int(rgb[2:4], 16), int(rgb[4:6], 16), a)
    frames_m = list(re.finditer(r"^FRAME\s+(\d+)\s+(\d+)\s*[xX]\s*(\d+)\s*$(.*?)^END FRAME\s*$", text, re.S | re.M))
    if len(frames_m) < n_frames:
        return {"ok": False, "reason": f"frames {len(frames_m)}/{n_frames}", "palette_size": len(palette)}
    frames, diags = [], []
    for fm in frames_m[:n_frames]:
        W, H = int(fm.group(2)), int(fm.group(3))
        if size is not None:
            W, H = size
        rows = [r.strip() for r in fm.group(4).splitlines() if r.strip()]
        d = {"declared": [int(fm.group(2)), int(fm.group(3))], "size": [W, H], "rows": len(rows)}
        if abs(len(rows) - H) > max(2, 0.05 * H):
            return {"ok": False, "reason": f"row count {len(rows)} vs {H}", "palette_size": len(palette), "diags": diags + [d]}
        tol = max(2, 0.05 * W) * w
        bad_len = sum(1 for r in rows[:H] if len(r) != W * w)
        far = sum(1 for r in rows[:H] if abs(len(r) - W * w) > tol)
        if far > 0.2 * H:
            return {"ok": False, "reason": f"{far}/{H} rows beyond length tolerance", "palette_size": len(palette), "diags": diags + [d]}
        grid, unknown = [], 0
        for r in (rows + ["." * (W * w)] * H)[:H]:
            r = (r + "." * (W * w))[:W * w]
            cells = [r[i:i + w] for i in range(0, W * w, w)]
            unknown += sum(1 for c in cells if c != "." * w and c not in palette)
            grid.append(cells)
        if unknown > 0.05 * W * H:
            return {"ok": False, "reason": f"{unknown} undeclared pixels", "palette_size": len(palette), "diags": diags + [d]}
        d.update(rows_wrong_length=bad_len, rows_beyond_tolerance=far, rows_missing=max(0, H - len(rows)), rows_extra=max(0, len(rows) - H),
                 undeclared_pixels=unknown)
        frames.append(grid)
        diags.append(d)
    return {"ok": True, "palette": palette, "frames": frames, "diags": diags}


def to_canvas(grid: List[List[str]], palette: Dict[str, Tuple[int, int, int, int]], w: int) -> PixelCanvas:
    H, W = len(grid), len(grid[0])
    c = PixelCanvas(W, H)
    ids = {"." * w: c.transparent_id}
    for code, rgba in palette.items():
        if rgba[3] == 0:
            ids[code] = c.transparent_id
            continue
        ids[code] = c.register_color(f"q{len(ids)}", rgba)
    c.matrix[:] = np.array([[ids.get(x, c.transparent_id) for x in row] for row in grid], dtype=np.int32)
    return c


_lock = threading.Lock()


def log(*a) -> None:
    with _lock:
        print(*a, flush=True)


def run_cell(task: TaskSpec, cfg: dict, llm_cfg: dict, tdir: Path) -> dict:
    tdir.mkdir(parents=True, exist_ok=True)
    if task.task_type == "edit":
        base = task.base
        w = code_width(len([i for i in np.unique(base.matrix) if int(i) != base.transparent_id]))
        block, _ = encode_canvas(base, w)
    else:
        w = code_width(task.max_colors)
        block = None
    messages = [{"role": "system", "content": SYSTEM.format(w=w, transparent="." * w, codes=codes_note(w))},
                {"role": "user", "content": user_text(task, w, block)}]
    llm = LLMClient.from_config({**llm_cfg, "max_tokens": MAX_TOKENS, "timeout": WALL_S, "request_cut_s": WALL_S})
    started = time.time()
    info: dict = {"config": cfg["id"], "task": task.id, "code_width": w, "max_tokens": MAX_TOKENS, "time_limit_s": WALL_S}
    (tdir / "messages.json").write_text(json.dumps(messages, ensure_ascii=False, indent=1))
    try:
        resp = llm.chat(messages)
    except LLMError as e:
        info.update(ok=False, error=f"{type(e).__name__}: {e}", termination=(
            "time_limit" if "exceeded" in str(e) else "llm_error"), seconds=round(time.time() - started, 1))
        return info
    choice = resp.choices[0]
    content = choice.message.content or ""
    reasoning = (getattr(resp, "reasoning", None) or {}).get("content") or ""
    raw = getattr(resp, "raw_usage", None) or {}
    det = raw.get("completion_tokens_details") or {}
    info.update(prompt_tokens=raw.get("prompt_tokens"), completion_tokens=raw.get("completion_tokens"),
                reasoning_tokens=det.get("reasoning_tokens") or 0, finish_reason=choice.finish_reason,
                seconds=round(time.time() - started, 1))
    (tdir / "answer.json").write_text(json.dumps({"content": content, "reasoning": reasoning,
                                                  "finish_reason": choice.finish_reason}, ensure_ascii=False, indent=1))
    return finish_cell(task, tdir, content, choice.finish_reason, w, info)


def finish_cell(task: TaskSpec, tdir: Path, content: str, finish_reason: Optional[str], w: int, info: dict) -> dict:
    """Turn a saved answer into the task result."""
    n = max(1, task.num_frames or 1)
    size = None if task.task_type == "edit" else (task.width, task.height)
    info["parser_version"] = PARSER_VERSION
    if finish_reason == "length":
        info.update(ok=False, error="token budget exhausted before the answer ended", termination="token_budget")
        return info
    parsed = parse_answer(content, w, n, size)
    info["parse"] = {k: v for k, v in parsed.items() if k not in ("palette", "frames")}
    if not parsed["ok"]:
        info.update(ok=False, error=f"unparseable answer: {parsed['reason']}", termination="format")
        return info
    frames = [to_canvas(g, parsed["palette"], w) for g in parsed["frames"]]
    visible = len({c for g in parsed["frames"] for row in g for c in row if c != "." * w and c in parsed["palette"]})
    info["colors"] = visible
    if task.task_type != "edit":
        info["color_limit_exceeded"] = visible > task.max_colors
    for i, f in enumerate(frames):
        (tdir / f"frame_{i:03d}.png").write_bytes(f.render_png_bytes(scale=1))
    info.update(ok=True, error=None, termination="answered", frames=len(frames))
    return info


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, help="configs/models/<id>.json")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tasks", default="", help="comma-separated task ids (default: all 100)")
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--base-url", default=None, help="default: $PIXELBENCH_BASE_URL")
    ap.add_argument("--api-key-env", default="PIXELBENCH_API_KEY")
    a = ap.parse_args()
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env", override=False)
    except ImportError:
        pass
    cfg = json.loads(Path(a.config).read_text())
    llm_cfg = {**cfg["llm"], "base_url": a.base_url or os.environ.get("PIXELBENCH_BASE_URL"),
               "api_key": os.environ.get(a.api_key_env) or "EMPTY"}
    selected = {t for t in a.tasks.split(",") if t}
    index = json.loads((ROOT / "tasks/index.json").read_text())
    tasks = [load_task_dir(ROOT / "tasks" / ("text2image" if t["family"] == "text2image" else "edit") / t["id"])
             for t in index if not selected or t["id"] in selected]
    out = Path(a.out)
    jobs = [t for t in tasks if not (out / t.id / "record.json").exists()]
    log(f"[direct] {cfg['id']}: {len(jobs)} tasks -> {out}")

    def one(task):
        try:
            info = run_cell(task, cfg, llm_cfg, out / task.id)
        except Exception as e:  # noqa: BLE001
            info = {"config": cfg["id"], "task": task.id, "ok": False, "error": f"{type(e).__name__}: {e}"}
        (out / task.id).mkdir(parents=True, exist_ok=True)
        (out / task.id / "record.json").write_text(json.dumps(info, ensure_ascii=False, indent=1, default=str))
        log(f"  {'OK ' if info.get('ok') else 'FAIL'} {task.id:34s} {info.get('termination')} "
            f"{'' if info.get('ok') else (info.get('error') or '')[:120]}")
        return info.get("ok")

    with cf.ThreadPoolExecutor(a.concurrency) as ex:
        ok = sum(1 for r in ex.map(one, jobs) if r)
    log(f"[direct] done: {ok}/{len(jobs)} valid answers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
