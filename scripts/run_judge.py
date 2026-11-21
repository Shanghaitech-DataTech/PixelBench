#!/usr/bin/env python3
"""Score artworks with the frozen PixelBench judge protocol, or verify this release against it.

    # Rebuild every judge input of the evaluation (prompt text and images) from the released tasks and
    # artworks and compare them with the released judge records. No model is called.
    python scripts/run_judge.py --verify

    # Score new artworks (e.g. the output directory of run_benchmark.py) under the final protocol.
    export PIXELBENCH_JUDGE_BASE_URL=https://...  PIXELBENCH_JUDGE_API_KEY=...
    python scripts/run_judge.py --creations runs/my-model --config-id my-model --out runs/my-model.judge.jsonl

The prompt builder and the image pipeline are pixelbench/eval/judge_protocol.py. The final protocol is
version e3_reference: rubric, 1/16 transparent margin and the task's reference image. Judge settings are
configs/judge.json: GPT-6 Astra at reasoning effort xhigh, temperature 0.2, at most four attempts, and
only a bare number from 0 to 100 counts as a score.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pixelbench.eval.judge_protocol import (EXPERIMENT_BY_KEY, JUDGE_SIZE, TILED_CATEGORY, build_message,  # noqa: E402
                                            compose_native, encode, fit_longest, grid_shape)

# English subject names of tasks/index.json -> the protocol's category keys
CATEGORY = {"characters": "人物类", "creatures": "生物类", "scenes": "场景类", "objects": "物品类",
            "icons": "UI类", "materials": "材质类", "effects": "特效类"}
SHUFFLE_SEED = 20260922


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pixels(png: bytes) -> str:
    """Hash of the decoded RGBA pixels: independent of the PNG encoder that wrote the file."""
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    return sha(f"{im.width}x{im.height}:".encode() + im.tobytes())


class Task:
    def __init__(self, row: dict):
        self.row = row
        self.id = row["id"]
        self.family = row["family"]
        self.dir = ROOT / "tasks" / ("text2image" if self.family == "text2image" else "edit") / self.id
        spec = json.loads((self.dir / "task.json").read_text())
        self.prompt = spec["prompt"]
        self.width, self.height = spec["width"], spec["height"]
        self.size = row.get("judge_size") or f"{self.width}x{self.height}"
        self.max_colors = row.get("max_colors")
        self.category = CATEGORY.get(row.get("subject")) if self.family == "text2image" else None
        self.n_frames = row.get("frames") or 1
        self.first_is_original = bool(row.get("first_frame_is_original"))
        self.reference_kind = "gt" if row.get("reference") == "source frames" else "gptimage"
        shown = self.n_frames - 1 if self.first_is_original else self.n_frames
        self.shape = grid_shape(shown, self.width, self.height)

    def candidate_frames(self, directory: Path):
        frames = [Image.open(p).convert("RGBA") for p in sorted(directory.glob("frame_*.png"))]
        if self.first_is_original and len(frames) > 1:
            frames = frames[1:]
        return frames

    def build(self, frames, experiment_key: str):
        """(message text, [(slot, caption)], {slot: png bytes}) of one judge call."""
        e = EXPERIMENT_BY_KEY[experiment_key]
        images = {}
        native, shape = compose_native(frames, margin=e.margin, tile=self.category == TILED_CATEGORY, shape=self.shape)
        images["candidate"] = encode(fit_longest(native, JUDGE_SIZE))
        if self.family != "text2image":
            original = Image.open(self.dir / "original.png").convert("RGBA")
            images["original"] = encode(fit_longest(compose_native([original], margin=e.margin, tile=False)[0],
                                                    JUDGE_SIZE))
        kind = self.reference_kind if e.reference else None
        if kind:
            images["reference"] = (self.dir / "reference.png").read_bytes()  # stored exactly as the judge saw it
        message = build_message(family=self.family, experiment=e, prompt=self.prompt, size=self.size,
                                max_colors=self.max_colors, category=self.category, width=self.width,
                                height=self.height, n_frames=len(frames), frame_shape=shape, reference_kind=kind,
                                total_frames=self.n_frames if self.first_is_original else None)
        return message.text, list(message.slots), images


def load_tasks():
    return {r["id"]: Task(r) for r in json.loads((ROOT / "tasks/index.json").read_text())}


def payload(text, slots, images, judge):
    content = [{"type": "text", "text": text}]
    for kind, caption in slots:
        content.append({"type": "text", "text": caption})
        content.append({"type": "image_url", "image_url": {
            "url": "data:image/png;base64," + base64.b64encode(images[kind]).decode()}})
    body = {"model": judge["model"], "temperature": judge["temperature"],
            "messages": [{"role": "user", "content": content}]}
    if judge.get("reasoning_effort"):
        body["reasoning_effort"] = judge["reasoning_effort"]
    return body


def strict_score(raw):
    """Only a bare number counts; anything else is a failed attempt, never a guess."""
    if not isinstance(raw, str) or not re.fullmatch(r"\s*\d+(?:\.\d+)?\s*", raw):
        return None
    value = float(raw)
    return value if 0 <= value <= 100 else None


# ---------------------------------------------------------------------------------------------- verify
def verify(args) -> int:
    tasks = load_tasks()
    rows = []
    for name in ("final_protocol.jsonl", "protocol_versions.jsonl"):
        rows += [json.loads(line) for line in (ROOT / "data/judge" / name).read_text().splitlines() if line]
    bad = checked = 0
    for r in rows:
        t = tasks[r["task"]]
        frames = t.candidate_frames(ROOT / "data/creations" / r["config"] / r["task"])
        text, _slots, images = t.build(frames, r["protocol"])
        problems = []
        if r.get("message") is not None and text != r["message"]:
            problems.append("prompt text")
        for kind, digest in (r.get("image_pixels") or {}).items():
            if pixels(images[kind]) != digest:
                problems.append(f"{kind} image")
        if set(images) != set(r.get("images") or {}):
            problems.append("image slots")
        checked += 1
        if problems:
            bad += 1
            if bad <= 20:
                print(f"  mismatch {r['config']}/{r['task']}/{r['protocol']}: {', '.join(problems)}")
    print(f"verified {checked} judge calls: {checked - bad} identical, {bad} different")
    return 1 if bad else 0


# ----------------------------------------------------------------------------------------------- score
def score(args) -> int:
    judge = json.loads((ROOT / "configs/judge.json").read_text())
    base = (args.base_url or os.environ.get("PIXELBENCH_JUDGE_BASE_URL") or "").rstrip("/")
    key = os.environ.get(args.api_key_env)
    if not base or not key:
        sys.exit("set PIXELBENCH_JUDGE_BASE_URL and PIXELBENCH_JUDGE_API_KEY (or --base-url / --api-key-env)")
    endpoint = base + ("/chat/completions" if base.endswith("/v1") else "/v1/chat/completions")
    import requests

    tasks = load_tasks()
    creations = Path(args.creations)
    todo = [t for t in tasks if (creations / t / "frame_000.png").exists()]
    random.Random(SHUFFLE_SEED).shuffle(todo)
    out = Path(args.out)
    done = {json.loads(line)["task"] for line in out.read_text().splitlines() if line} if out.exists() else set()

    def one(task_id):
        t = tasks[task_id]
        text, slots, images = t.build(t.candidate_frames(creations / task_id), "e3_reference")
        body = payload(text, slots, images, judge)
        row = {"task": task_id, "config": args.config_id, "protocol": "e3_reference", "score": None, "raw": None,
               "images": {k: sha(v) for k, v in images.items()}, "attempts": 0}
        for attempt in range(judge["max_attempts"]):
            row["attempts"] = attempt + 1
            try:
                resp = requests.post(endpoint, headers={"Authorization": "Bearer " + key}, json=body, timeout=(20, 600))
                if resp.status_code in (401, 402, 403):
                    raise SystemExit(f"judge endpoint refused the key: HTTP {resp.status_code}")
                resp.raise_for_status()
                raw = resp.json()["choices"][0]["message"].get("content")
                row["raw"] = raw
                row["score"] = strict_score(raw)
                if row["score"] is not None:
                    break
            except SystemExit:
                raise
            except Exception as exc:  # noqa: BLE001
                row["error"] = f"{type(exc).__name__}"
            time.sleep(min(8, 2 * (attempt + 1)))
        return row

    with ThreadPoolExecutor(max_workers=args.concurrency) as pool, out.open("a") as fh:
        for row in pool.map(one, [t for t in todo if t not in done]):
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            fh.flush()
    print(f"scored -> {out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verify", action="store_true", help="rebuild and compare every judge input of the release")
    ap.add_argument("--creations", help="directory with <task>/frame_000.png ... (e.g. a run_benchmark.py output)")
    ap.add_argument("--config-id", default="candidate")
    ap.add_argument("--out", default=None)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--base-url", default=None)
    ap.add_argument("--api-key-env", default="PIXELBENCH_JUDGE_API_KEY")
    args = ap.parse_args()
    if args.verify:
        return verify(args)
    if not args.creations or not args.out:
        ap.error("--creations and --out are required for scoring")
    return score(args)


if __name__ == "__main__":
    sys.exit(main())
