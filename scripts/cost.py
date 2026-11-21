#!/usr/bin/env python3
"""Per-task tokens, time and list-price cost of every configuration (Appendix J.3) from the released records.

    python scripts/cost.py               # the twelve configurations of the main table
    python scripts/cost.py --all         # also every variant (reasoning effort, runs 2 and 3, ...)

Each model call is priced on its own with data/cost/prices.json. Output includes reasoning; minutes are the median
wall-clock time per task.
"""
from __future__ import annotations

import argparse
import json
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def task_cost(calls, price):
    total, prev = 0.0, 0
    cached_sum = 0
    for p, c, o, _r in calls:
        if price.get("estimate_cache"):
            c, prev = min(p, prev), p
        rate = price
        lc = price.get("long_context")
        if lc and p > lc["above_prompt_tokens"]:
            rate = lc
        total += ((p - c) * rate["input"] + c * rate["cached_input"] + o * rate["output"]) / 1e6
        cached_sum += c
    return total, cached_sum


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    prices = json.loads((DATA / "cost/prices.json").read_text())["models"]
    configs = json.loads((DATA / "configs.json").read_text())
    index = json.loads((ROOT / "tasks/index.json").read_text())
    fam = {t["id"]: ("gen" if t["family"] == "text2image" else "edit") for t in index}
    rows = []
    for cfg in configs:
        if cfg["role"] != "main" and not a.all:
            continue
        cid = cfg["id"]
        price = prices[cfg.get("base", cid)]
        cells = []
        for t in fam:
            rec_path = DATA / "creations" / cid / t / "record.json"
            if not rec_path.exists():
                continue
            r = json.loads(rec_path.read_text())
            calls = r.get("calls_usage") or []
            cost, cached = task_cost(calls, price)
            cells.append({"fam": fam[t], "calls": len(calls), "writes": r.get("writes") or 0,
                          "prompt": sum(c[0] for c in calls), "cached": cached, "output": sum(c[2] for c in calls),
                          "reasoning": sum(c[3] for c in calls), "minutes": (r.get("seconds") or 0) / 60, "cost": cost})
        for g in ("all",):
            cs = [c for c in cells if g == "all" or c["fam"] == g]
            m = lambda k: st.mean(c[k] for c in cs)
            rows.append((cid, len(cs), m("calls"), m("writes"), m("prompt") / 1e3,
                         sum(c["cached"] for c in cs) / max(1, sum(c["prompt"] for c in cs)), m("output") / 1e3,
                         st.median(c["minutes"] for c in cs), round(m("cost"), 3)))  # cents rounded as in the paper
    print(f"{'configuration':34s} {'tasks':>5s} {'calls':>6s} {'writes':>6s} {'input k':>8s} {'cached':>7s} "
          f"{'output k':>8s} {'minutes':>7s} {'cost':>7s}")
    for cid, n, calls, writes, inp, cached, out, mins, cost in rows:
        print(f"{cid:34s} {n:5d} {calls:6.1f} {writes:6.1f} {inp:8.0f} {cached:7.0%} {out:8.1f} {mins:7.1f} ${cost:6.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
