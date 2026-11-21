"""Consistency of the released tasks, artworks and judge records (a sample; scripts/run_judge.py --verify checks all)."""
import importlib.util
import json
import random
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
pytestmark = pytest.mark.skipif(not (DATA / "judge/final_protocol.jsonl").exists(), reason="release data not present")


def run_judge():
    spec = importlib.util.spec_from_file_location("run_judge", ROOT / "scripts/run_judge.py")
    module = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, ["run_judge.py"]
    try:
        spec.loader.exec_module(module)
    finally:
        sys.argv = argv
    return module


def test_task_set():
    index = json.loads((ROOT / "tasks/index.json").read_text())
    assert len(index) == 100
    assert sum(t["family"] == "text2image" for t in index) == 75
    assert sum(t["development_subset"] for t in index) == 23


def test_every_main_artwork_is_scored():
    rows = [json.loads(line) for line in (DATA / "judge/final_protocol.jsonl").read_text().splitlines() if line]
    configs = [c["id"] for c in json.loads((DATA / "configs.json").read_text()) if c["role"] == "main"]
    scored = {(r["config"], r["task"]) for r in rows if r["score"] is not None}
    assert len(configs) == 12
    assert all((c, t["id"]) in scored for c in configs for t in json.loads((ROOT / "tasks/index.json").read_text()))


def test_judge_inputs_rebuild_from_release():
    J = run_judge()
    tasks = J.load_tasks()
    rows = [json.loads(line) for line in (DATA / "judge/final_protocol.jsonl").read_text().splitlines() if line]
    for r in random.Random(0).sample(rows, 40):
        t = tasks[r["task"]]
        text, _slots, images = t.build(t.candidate_frames(DATA / "creations" / r["config"] / r["task"]), r["protocol"])
        assert text == r["message"]
        assert {k: J.pixels(v) for k, v in images.items()} == r["image_pixels"]
