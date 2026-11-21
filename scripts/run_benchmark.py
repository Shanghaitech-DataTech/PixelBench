#!/usr/bin/env python3
"""Run one configuration on the PixelBench tasks under the evaluation protocol.

    export PIXELBENCH_BASE_URL=https://...   # any OpenAI-compatible endpoint
    export PIXELBENCH_API_KEY=...
    python scripts/run_benchmark.py --config configs/models/gpt-6-astra.json --out runs/gpt-6-astra
    python scripts/run_benchmark.py --config configs/models/kimi-k3.json --tasks magnifying-glass,knife --out runs/try

The protocol (pixelbench/protocol.py) is applied unchanged: 25 source writes on generation tasks and 15
on editing tasks, 75 minutes per model request, three hours per task, and every program in the sandbox.
A task that hits a failure of the serving infrastructure is run again from the start until it completes;
a task whose model returned no artwork, was cut off, or submitted only transparent frames is rerun once
and the rerun counts.

Output, one directory per task (the layout of data/creations/<config>/ in this release):
    <out>/<task>/frame_000.png ...   the final artwork, one PNG per frame at native size
    <out>/<task>/record.json         outcome, usage and the history of attempts
    <out>/<task>/transcript.json     the transcript of the final attempt
    <out>/<task>/attempts/<k>/       every attempt's program directory (sources, runs, outputs)
A task with a record.json is skipped, so an interrupted run can be resumed with the same command.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pixelbench import protocol as P  # noqa: E402
from pixelbench.agents import build_agent  # noqa: E402
from pixelbench.agents.base import Budget  # noqa: E402
from pixelbench.repl.file_session import FileSession  # noqa: E402
from pixelbench.repl.prelude import build_prelude  # noqa: E402
from pixelbench.tasks.specs import load_task_dir  # noqa: E402

_print = threading.Lock()
STOP = threading.Event()


def log(*a):
    with _print:
        print(*a, flush=True)


def load_env():
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env", override=False)
    except ImportError:
        pass


def tasks(selected):
    index = json.loads((ROOT / "tasks/index.json").read_text())
    out = []
    for t in index:
        if selected and t["id"] not in selected:
            continue
        family = "text2image" if t["family"] == "text2image" else "edit"
        out.append((t["id"], family, ROOT / "tasks" / family / t["id"]))
    return out


def llm_config(cfg, args):
    llm = dict(cfg["llm"])
    llm.update(base_url=args.base_url or os.environ.get("PIXELBENCH_BASE_URL"),
               api_key=os.environ.get(args.api_key_env) or "EMPTY",
               timeout=float(P.REQUEST_LIMIT_S), request_cut_s=float(P.REQUEST_LIMIT_S),
               episode_cut_s=float(P.TASK_LIMIT_S), max_retries=args.max_retries)
    return llm


def episode(cfg, llm, family, task_dir, attempt_dir, sandbox):
    """One attempt at one task. Returns (frames, record, transcript)."""
    spec = load_task_dir(task_dir)
    budget = Budget.from_task(spec)
    assert budget.max_steps == P.WRITE_BUDGET[family], "task budget differs from the protocol"
    agent = build_agent({"type": "file", "name": cfg["id"], "vision": bool(cfg.get("vision", True)),
                         "max_steps": budget.max_steps, "llm": llm})
    session = FileSession(root=attempt_dir, sandbox=sandbox)
    session.start(timeout=90)
    started = time.monotonic()
    try:
        prelude = build_prelude(task=spec.public_task(), initial_state=spec.initial_state(), reference_state=None,
                                mask_state=None, seed=0, surface="full")
        px = spec.width * spec.height
        session.execute_checked(prelude, timeout=60 if px <= 64 * 64 else (180 if px <= 128 * 128 else 300),
                                what="prelude")
        result = agent.run(spec, session, budget, language="en-US")
        submission = dict(result.submission or {})
        frames = list(result.final_frames or [])
        if not frames:
            try:
                frames, meta = session.extract_submission()
                submission = {**submission, **(meta or {})}
            except Exception:  # noqa: BLE001
                frames = []
        if not frames and result.final_canvas is not None:
            frames = [result.final_canvas]
        if not frames:  # no formal submission: recover the artwork from the canvases the program drew
            try:
                recovered = session.extract_final_canvas()
                frames = [recovered] if recovered is not None else []
            except Exception:  # noqa: BLE001
                frames = []
        retry_errors = [r.get("error") for e in result.transcript if e.get("kind") in ("llm_error", "long_request_cut")
                        for r in (e.get("retry_log") or [])]
        termination = submission.get("termination_reason")
        outcome = P.classify(termination, result.error, retry_errors, frames)
        usage = result.usage or {}
        record = {"config": cfg["id"], "task": spec.id, "outcome": outcome, "ok": outcome == P.COMPLETE,
                  "error": result.error, "termination": termination, "submission": submission,
                  "frames": len(frames), "colors": len(frames[-1].palette) if frames else None,
                  "writes": usage.get("mutation_steps"), "model_rounds": usage.get("model_rounds"),
                  "llm_calls": usage.get("llm_calls"), "retries": usage.get("retries"),
                  "prompt_tokens": usage.get("prompt_tokens"), "cached_tokens": usage.get("cached_tokens"),
                  "completion_tokens": usage.get("completion_tokens"), "reasoning_tokens": usage.get("reasoning_tokens"),
                  "seconds": round(time.monotonic() - started, 1), "program_dir": session.root.name}
        return frames, record, result.transcript
    finally:
        session.shutdown()


def run_task(cfg, args, task_id, family, task_dir, out):
    tdir = out / task_id
    if (tdir / "record.json").exists():
        return "skipped"
    history = []
    while not STOP.is_set():
        k = len(history) + 1
        attempt_dir = tdir / "attempts" / f"{k:02d}"
        try:
            frames, record, transcript = episode(cfg, llm_config(cfg, args), family, task_dir, attempt_dir,
                                                 not args.unsafe_no_sandbox)
        except Exception as exc:  # noqa: BLE001 - a harness failure is infrastructure, not a model result
            frames, transcript = [], []
            record = {"config": cfg["id"], "task": task_id, "error": f"{type(exc).__name__}: {exc}",
                      "outcome": P.is_infrastructure_error(str(exc)) or P.INFRASTRUCTURE, "ok": False}
        (attempt_dir / "record.json").parent.mkdir(parents=True, exist_ok=True)
        (attempt_dir / "record.json").write_text(json.dumps(record, ensure_ascii=False, indent=1, default=str))
        (attempt_dir / "transcript.json").write_text(json.dumps(transcript, ensure_ascii=False, indent=1, default=str))
        for i, f in enumerate(frames):
            (attempt_dir / f"frame_{i:03d}.png").write_bytes(f.render_png_bytes(scale=1))
        history.append(record["outcome"])
        action = P.decide(history, args.max_infrastructure_reruns)
        log(f"  {task_id:34s} attempt {k}: {record['outcome']} -> {action}")
        if action == "rerun":
            if record["outcome"] == P.INFRASTRUCTURE:
                time.sleep(min(600, 30 * 2 ** min(sum(o == P.INFRASTRUCTURE for o in history) - 1, 5)))
            continue
        if action == "stop":
            if record["outcome"] == P.FATAL:
                STOP.set()
                log(f"[stop] the endpoint rejected the configuration: {record.get('error')}")
            return "stopped"
        # accept: the last attempt is the result of this task
        for p in attempt_dir.glob("frame_*.png"):
            shutil.copyfile(p, tdir / p.name)
        shutil.copyfile(attempt_dir / "transcript.json", tdir / "transcript.json")
        final = dict(record, attempts=[{"attempt": i + 1, "outcome": o} for i, o in enumerate(history)])
        (tdir / "record.json").write_text(json.dumps(final, ensure_ascii=False, indent=1, default=str))
        return record["outcome"]
    return "stopped"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, help="configs/models/<id>.json")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tasks", default="", help="comma-separated task ids (default: all 100)")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--base-url", default=None, help="default: $PIXELBENCH_BASE_URL")
    ap.add_argument("--api-key-env", default="PIXELBENCH_API_KEY", help="environment variable holding the key")
    ap.add_argument("--max-retries", type=int, default=6, help="retries of one request inside an attempt")
    ap.add_argument("--max-infrastructure-reruns", type=int, default=20)
    ap.add_argument("--unsafe-no-sandbox", action="store_true",
                    help="run model programs without the sandbox (only for platforms without Landlock; "
                         "results are not comparable)")
    args = ap.parse_args()
    load_env()
    cfg = json.loads(Path(args.config).read_text())
    if args.unsafe_no_sandbox:
        log("[warning] the sandbox is OFF: model programs can read the file system and reach the network")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    selected = {t for t in args.tasks.split(",") if t}
    todo = tasks(selected)
    log(f"[pixelbench] {cfg['id']}: {len(todo)} tasks -> {out}")
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        results = list(pool.map(lambda t: run_task(cfg, args, t[0], t[1], t[2], out), todo))
    summary = {k: results.count(k) for k in sorted(set(results))}
    log(f"[pixelbench] done: {summary}")
    return 0 if "stopped" not in summary else 1


if __name__ == "__main__":
    sys.exit(main())
