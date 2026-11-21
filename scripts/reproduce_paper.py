#!/usr/bin/env python3
"""Recompute the paper's main numbers from the released data (no model calls).

    python scripts/reproduce_paper.py            # prints a report and writes results/paper_numbers.json

Conventions: per-task Kendall tau_b; tasks weighted equally; 95% intervals from 10,000 bootstrap resamples
of tasks (seed 20260923); the judge's agreement is with the mean rank of the ten raters (the consensus),
and leave-one-out compares the judge and each rater with the consensus of the other nine.
"""
from __future__ import annotations

import itertools
import json
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import kendalltau, rankdata, spearmanr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
B, SEED = 10_000, 20260923
MAIN = ["gpt-6-astra", "claude-opus-5", "gemini-3.8-flash", "qwen3.8-max", "gpt-5.6-sol", "deepseek-v4.1-flash",
        "glm-5.3-flash", "kimi-k3", "gemini-3.1-pro-preview", "deepseek-v4-pro", "deepseek-v4-flash-0731",
        "qwen3.5-397b-a17b"]


def jsonl(name):
    return [json.loads(line) for line in (DATA / name).read_text().splitlines() if line]


def tau(a, b):
    return float(kendalltau(a, b).statistic)


def boot(v):
    v = np.asarray(v, float)
    d = v[np.random.default_rng(SEED).integers(0, len(v), size=(B, len(v)))].mean(1)
    return [float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))]


def sm(v):
    return {"mean": float(np.mean(v)), "ci": boot(v), "n": len(v)}


def fmt(s, digits=3):
    return f"{s['mean']:.{digits}f} [{s['ci'][0]:.{digits}f}, {s['ci'][1]:.{digits}f}]"


# ---------------------------------------------------------------------------------------------- data
INDEX = json.loads((ROOT / "tasks/index.json").read_text())
TASKS = [t["id"] for t in INDEX]
FAM = {t["id"]: t["family"] for t in INDEX}
SIDE = {t["id"]: max(t["canvas"]) for t in INDEX}
GEN = [t for t in TASKS if FAM[t] == "text2image"]
EDIT = [t for t in TASKS if FAM[t] != "text2image"]
GROUPS = {"all": TASKS, "gen": GEN, "edit": EDIT}
DEV = {t["id"] for t in INDEX if t.get("development_subset")}

SCORE = {}  # (protocol, config, task) -> judge score
for r in jsonl("judge/final_protocol.jsonl") + jsonl("judge/protocol_versions.jsonl"):
    SCORE[r["protocol"], r["config"], r["task"]] = r["score"]
RATERS = [json.loads(p.read_text()) for p in sorted((DATA / "human").glob("R*.json"))]
N = len(RATERS)
H = {t: np.array([[r["tasks"][t]["ranking"].index(m) + 1 for m in MAIN] for r in RATERS], float) for t in TASKS}
REF = [i for i, r in enumerate(RATERS) if r["reference_mode"] == "with_reference"]
NOREF = [i for i, r in enumerate(RATERS) if r["reference_mode"] == "without_reference"]


def jvec(t, protocol="e3_reference", scores=None):
    src = scores if scores is not None else {m: SCORE[protocol, m, t] for m in MAIN}
    return [src[m] for m in MAIN] if scores is None else [scores[t, m] for m in MAIN]


def boards(ts, scores=None):
    sc = (lambda t: jvec(t)) if scores is None else (lambda t: [scores[t, m] for m in MAIN])
    score = {m: float(np.mean([sc(t)[k] for t in ts])) for k, m in enumerate(MAIN)}
    jrank = {m: float(np.mean([rankdata([-x for x in sc(t)])[k] for t in ts])) for k, m in enumerate(MAIN)}
    hrank = {m: float(np.mean([H[t][:, k].mean() for t in ts])) for k, m in enumerate(MAIN)}
    return score, jrank, hrank


def loo_block(ts, vec):
    agree = [tau(vec(t), -H[t].mean(0)) for t in ts]
    jl = [np.mean([tau(vec(t), -np.delete(H[t], i, 0).mean(0)) for i in range(N)]) for t in ts]
    hl = [np.mean([tau(H[t][i], np.delete(H[t], i, 0).mean(0)) for i in range(N)]) for t in ts]
    per = [float(np.mean([tau(H[t][i], np.delete(H[t], i, 0).mean(0)) for t in ts])) for i in range(N)]
    return {"agreement": sm(agree), "judge_loo": sm(jl), "human_loo": sm(hl), "judge_minus_rater": sm(np.subtract(jl, hl)),
            "rater_loo_range": [min(per), max(per)], "raters_below_judge": int(sum(x < np.mean(jl) for x in per))}


def main():
    out, lines = {}, []
    say = lines.append
    # ------------------------------------------------------------------ Table 2
    say("Table 2  leaderboard (judge score; mean within-task rank of the judge and of the ten raters)")
    out["leaderboard"] = {}
    for g, ts in GROUPS.items():
        score, jrank, hrank = boards(ts)
        rho = spearmanr([score[m] for m in MAIN], [-hrank[m] for m in MAIN]).statistic
        out["leaderboard"][g] = {"score": score, "judge_rank": jrank, "human_rank": hrank, "rho_score_vs_human": float(rho)}
    lb = out["leaderboard"]
    for m in sorted(MAIN, key=lambda m: -lb["all"]["score"][m]):
        say(f"  {m:24s} " + "  ".join(f"{lb[g]['score'][m]:6.2f} {lb[g]['judge_rank'][m]:5.2f} {lb[g]['human_rank'][m]:5.2f}"
                                      for g in GROUPS))
    say(f"  Spearman rho, judge score vs human rank: all {lb['all']['rho_score_vs_human']:.3f}")
    # ------------------------------------------------------------------ Section 5: agreement and leave-one-out
    out["agreement"] = {g: loo_block(ts, jvec) for g, ts in GROUPS.items()}
    a = out["agreement"]
    say("\nSection 5.3  judge agreement with the ten-rater consensus (Kendall tau_b per task)")
    for g in GROUPS:
        say(f"  {g:5s} agreement {fmt(a[g]['agreement'])}  judge LOO {fmt(a[g]['judge_loo'])}  "
            f"raters LOO {a[g]['rater_loo_range'][0]:.3f}-{a[g]['rater_loo_range'][1]:.3f}  "
            f"raters below judge {a[g]['raters_below_judge']}")
    out["outside_development_subset"] = sm([tau(jvec(t), -H[t].mean(0)) for t in TASKS if t not in DEV])
    say(f"  outside the 23-task development subset: {fmt(out['outside_development_subset'])}")
    # ------------------------------------------------------------------ protocol versions
    say("\nProtocol versions on the same artworks (agreement, all 100 tasks)")
    out["protocol_versions"] = {}
    for p in ("e0_base", "e1_margin", "e2_rubric", "e3_reference"):
        v = sm([tau(jvec(t, p), -H[t].mean(0)) for t in TASKS])
        vr = sm([tau(jvec(t, p), -H[t][REF].mean(0)) for t in TASKS])
        vn = sm([tau(jvec(t, p), -H[t][NOREF].mean(0)) for t in TASKS])
        out["protocol_versions"][p] = {"all_raters": v, "with_reference_raters": vr, "without_reference_raters": vn}
        say(f"  {p:13s} {fmt(v)}   vs raters with reference {vr['mean']:.3f}, without {vn['mean']:.3f}")
    # ------------------------------------------------------------------ Appendix D: repeat scoring
    rep = defaultdict(dict)
    first = {}
    for r in jsonl("judge/repeat_passes.jsonl"):
        rep[r["task"], r["config"]][r["pass"]] = r["score"]
        first[r["task"], r["config"]] = r["first_pass_score"]
    arts = sorted(rep)
    passes = np.array([[rep[k][p] for p in (1, 2, 3)] for k in arts], float)
    sds = passes.std(1, ddof=1)
    pairs = np.abs(np.concatenate([passes[:, 0] - passes[:, 1], passes[:, 0] - passes[:, 2], passes[:, 1] - passes[:, 2]]))
    out["repeat"] = {"artworks": len(arts), "pass_means": passes.mean(0).tolist(),
                     "three_pass_minus_first": float(passes.mean(1).mean() - np.mean([first[k] for k in arts])),
                     "sd_mean": float(sds.mean()), "sd_median": float(np.median(sds)),
                     "within_2": float(np.mean(pairs <= 2)), "within_5": float(np.mean(pairs <= 5))}
    say(f"\nAppendix D  repeat scoring of {len(arts)} artworks: pass means "
        + ", ".join(f"{x:.1f}" for x in out['repeat']['pass_means'])
        + f"; per-artwork SD mean {out['repeat']['sd_mean']:.2f}, median {out['repeat']['sd_median']:.2f}; "
          f"pairs within 2 points {out['repeat']['within_2']:.1%}, within 5 {out['repeat']['within_5']:.1%}")
    # ------------------------------------------------------------------ Appendix F: other judge models
    other = defaultdict(dict)
    for r in jsonl("judge/other_judges.jsonl"):
        if r["score"] is not None:
            other[r["judge"]][r["task"], r["config"]] = r["score"]
    out["other_judges"] = {}
    say("\nAppendix F  other judge models (same protocol and inputs)")
    for judge, sc in other.items():
        ts = [t for t in TASKS if all((t, m) in sc for m in MAIN)]
        vec = lambda t, sc=sc: [sc[t, m] for m in MAIN]
        res = {"tasks": len(ts)}
        for g, gt in GROUPS.items():
            tj = [t for t in gt if t in ts]
            b = loo_block(tj, vec)
            astra = [tau(jvec(t), -H[t].mean(0)) for t in tj]
            mine = [tau(vec(t), -H[t].mean(0)) for t in tj]
            res[g] = {"agreement": b["agreement"], "judge_loo": b["judge_loo"], "raters_below_judge": b["raters_below_judge"],
                      "astra_minus_this": sm(np.subtract(astra, mine))}
        score, _, hrank = boards(ts, sc)
        astra_score, _, _ = boards(ts)
        res["rho_vs_human"] = float(spearmanr([score[m] for m in MAIN], [-hrank[m] for m in MAIN]).statistic)
        res["rho_vs_astra_judge"] = float(spearmanr([score[m] for m in MAIN], [astra_score[m] for m in MAIN]).statistic)
        res["first"] = max(MAIN, key=score.get)
        out["other_judges"][judge] = res
        say(f"  {judge:20s} tasks {len(ts)}  agreement {fmt(res['all']['agreement'])}  "
            f"Astra minus it {fmt(res['all']['astra_minus_this'])}  rho vs human {res['rho_vs_human']:.3f}  first: {res['first']}")
    # ------------------------------------------------------------------ Appendix I: raters
    pos = [np.mean([tau([r["tasks"][t]["initial_order"].index(m) for m in MAIN], H[t][i]) for t in TASKS])
           for i, r in enumerate(RATERS)]
    secs = [r["tasks"][t]["seconds"] or 0 for r in RATERS for t in TASKS]
    hb = lambda idx, ts: [np.mean([H[t][idx, k].mean() for t in ts]) for k in range(len(MAIN))]
    out["raters"] = {"initial_order_tau_mean": float(np.mean(pos)), "initial_order_tau_range": [min(pos), max(pos)],
                     "median_seconds": float(np.median(secs)),
                     "reference_split_rho_all": float(spearmanr(hb(REF, TASKS), hb(NOREF, TASKS)).statistic),
                     "reference_split_rho_gen": float(spearmanr(hb(REF, GEN), hb(NOREF, GEN)).statistic)}
    say(f"\nAppendix I  initial order vs final rank tau {np.mean(pos):.3f} ({min(pos):.3f}-{max(pos):.3f}); "
        f"median {np.median(secs):.0f} s per task; with vs without reference rho "
        f"{out['raters']['reference_split_rho_all']:.3f} (all), {out['raters']['reference_split_rho_gen']:.3f} (generation)")
    # ------------------------------------------------------------------ Appendix J: analyses scored by the judge
    def mean_of(cfg, ts, zero_missing=False):
        vals = []
        for t in ts:
            s = SCORE.get(("e3_reference", cfg, t))
            if s is None and zero_missing:
                s = 0.0
            if s is not None:
                vals.append(s)
        return float(np.mean(vals)) if vals else None

    def boot_py(d):
        """The effort tables' interval: tasks in alphabetical order, random.Random(seed).choices, sorted means."""
        rng = random.Random(SEED)
        m = sorted(statistics.mean(rng.choices(d, k=len(d))) for _ in range(B))
        return [m[int(.025 * B)], m[int(.975 * B)]]

    say("\nAppendix J  analyses scored by the judge (mean judge score: all / generation / editing)")
    out["variants"] = {}
    alpha = sorted(TASKS)
    # -------- Table 8: repeated creation
    runs = {"gpt-6-astra": ["gpt-6-astra", "gpt-6-astra@run2", "gpt-6-astra@run3"],
            "gpt-5.6-sol": ["gpt-5.6-sol", "gpt-5.6-sol@run2", "gpt-5.6-sol@run3"],
            "deepseek-v4-flash-0731": ["deepseek-v4-flash-0731", "deepseek-v4-flash-0731@run2", "deepseek-v4-flash-0731@run3"]}
    rep_var = float(np.mean(passes.var(1, ddof=1)))  # the judge's repeat-scoring variance (Appendix D)
    out["repeat"]["pooled_sd"] = float(np.sqrt(rep_var))
    say(f"  repeated creation (judge repeat-scoring pooled SD {np.sqrt(rep_var):.2f} removed from the creation SD)")
    rc = {}
    for base, cfgs in runs.items():
        means = [mean_of(c, TASKS) for c in cfgs]
        v = [np.var([SCORE["e3_reference", c, t] for c in cfgs], ddof=1) for t in alpha]
        rho = [spearmanr([SCORE["e3_reference", a, t] for t in alpha], [SCORE["e3_reference", b, t] for t in alpha]).statistic
               for a, b in itertools.combinations(cfgs, 2)]
        rc[base] = {"run_means": means, "gen": [mean_of(c, GEN) for c in cfgs], "edit": [mean_of(c, EDIT) for c in cfgs],
                    "sd_of_means": float(np.std(means, ddof=1)), "per_task_sd": float(np.sqrt(np.mean(v))),
                    "creation_sd": float(np.sqrt(max(np.mean(v) - rep_var, 0))), "rho_range": [float(min(rho)), float(max(rho))]}
        say(f"    {base:24s} runs " + " / ".join(f"{x:.2f}" for x in means)
            + f"  SD of means {rc[base]['sd_of_means']:.2f}  per-task SD {rc[base]['per_task_sd']:.2f}"
              f"  creation SD {rc[base]['creation_sd']:.2f}  rho {min(rho):.2f}-{max(rho):.2f}")
    rng = np.random.default_rng(SEED)  # tasks x runs, one shared generator in this pair order
    gaps = {}
    for a, b in itertools.combinations(runs, 2):
        sa = np.array([[SCORE["e3_reference", c, t] for c in runs[a]] for t in alpha])
        sb = np.array([[SCORE["e3_reference", c, t] for c in runs[b]] for t in alpha])
        draws = []
        for _ in range(B):
            ti = rng.integers(0, len(alpha), len(alpha))
            ra = rng.integers(0, sa.shape[1], len(alpha))
            rb = rng.integers(0, sb.shape[1], len(alpha))
            draws.append(sa[ti, ra].mean() - sb[ti, rb].mean())
        gaps[f"{a} - {b}"] = {"mean": float(sa.mean() - sb.mean()),
                              "ci": [float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))]}
        say(f"    {a} - {b}: {gaps[f'{a} - {b}']['mean']:+.2f} [{gaps[f'{a} - {b}']['ci'][0]:+.2f}, {gaps[f'{a} - {b}']['ci'][1]:+.2f}]")
    out["repeated_creation"] = {"configs": rc, "paired_differences": gaps}
    # -------- Table 9: reasoning effort
    say("  reasoning effort (difference from the level of the main table, 95% interval)")
    studies = {"gpt-6-astra": ["gpt-6-astra@effort-low", "gpt-6-astra@effort-medium", "gpt-6-astra", "gpt-6-astra@effort-xhigh"],
               "deepseek-v4-flash-0731": ["deepseek-v4-flash-0731@effort-none", "deepseek-v4-flash-0731@effort-low",
                                          "deepseek-v4-flash-0731", "deepseek-v4-flash-0731@effort-max"],
               "glm-5.3-flash": ["glm-5.3-flash@effort-low", "glm-5.3-flash@effort-high", "glm-5.3-flash"]}
    for base, cfgs in studies.items():
        for c in cfgs:
            row = {g: mean_of(c, ts) for g, ts in GROUPS.items()}
            if c != base:
                d = [SCORE["e3_reference", c, t] - SCORE["e3_reference", base, t] for t in alpha]
                row["delta"] = {"mean": statistics.mean(d), "ci": boot_py(d)}
            out["variants"][c] = row
            delta = (f"  delta {row['delta']['mean']:+.1f} [{row['delta']['ci'][0]:+.1f}, {row['delta']['ci'][1]:+.1f}]"
                     if "delta" in row else "")
            say(f"    {c:36s} {row['all']:6.2f} {row['gen']:6.2f} {row['edit']:6.2f}{delta}")
    # -------- image observation
    for c in ("gpt-6-astra", "gpt-6-astra@no-vision"):
        out["variants"].setdefault(c, {g: mean_of(c, ts) for g, ts in GROUPS.items()})
    nv = out["variants"]["gpt-6-astra@no-vision"]
    say(f"  without image observation: generation {nv['gen']:.1f}, editing {nv['edit']:.1f} "
        f"(with it: {out['variants']['gpt-6-astra']['gen']:.1f}, {out['variants']['gpt-6-astra']['edit']:.1f})")
    say("  direct answering (tasks without a valid answer score 0)")
    for c in ("gpt-6-astra@direct", "deepseek-v4-flash-0731@direct"):
        answered = sum(SCORE.get(("e3_reference", c, t)) is not None for t in TASKS)
        bands = {"<=32": [t for t in GEN if SIDE[t] <= 32], "33-64": [t for t in GEN if 32 < SIDE[t] <= 64],
                 ">64": [t for t in GEN if SIDE[t] > 64]}
        row = {"answered": answered, **{g: mean_of(c, ts, zero_missing=True) for g, ts in GROUPS.items()},
               **{f"gen{b}": mean_of(c, ts, zero_missing=True) for b, ts in bands.items()}}
        out["variants"][c] = row
        say(f"    {c:36s} answered {answered}/100  all {row['all']:.1f}  gen {row['gen']:.1f}  edit {row['edit']:.1f}  "
            + "  ".join(f"gen{b} {row['gen' + b]:.1f}" for b in bands))
    res = ROOT / "results"
    res.mkdir(exist_ok=True)
    (res / "paper_numbers.json").write_text(json.dumps(out, indent=1))
    print("\n".join(lines))
    print(f"\nwritten {res / 'paper_numbers.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
