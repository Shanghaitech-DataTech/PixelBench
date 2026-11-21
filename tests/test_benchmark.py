import json
from pathlib import Path

import pytest

from pixelbench.agents.mock import MockDirectAgent, MockREPLAgent
from pixelbench.config import BenchmarkConfig
from pixelbench.eval.judge import MockJudge
from pixelbench.runner import BenchmarkRunner
from pixelbench.tasks.smoke import smoke_tasks

pytest.importorskip("ipykernel")


def test_runner_end_to_end(tmp_path):
    tasks = smoke_tasks()[:4]  # 4 agentic (text2image) tasks
    agents = [MockDirectAgent(name="mock-direct"), MockREPLAgent(name="mock-repl")]
    report = BenchmarkRunner(tasks, agents, MockJudge(), out_dir=str(tmp_path / "out"), seed=0).run()
    assert len(report.records) == 8
    assert all(r.ok for r in report.records), [r.error for r in report.records if not r.ok]
    summary = report.summary()
    assert "agentic_creation" in summary
    # artifacts written
    out = tmp_path / "out"
    assert (out / "summary.json").exists()
    assert (out / "summary.md").exists()
    assert (out / "contact_sheet.png").exists()
    assert (out / "episodes" / "agentic_0001__mock-repl" / "final.png").exists()


def test_runner_observation_artifacts(tmp_path):
    tasks = smoke_tasks()[2:4]  # 2 agentic (REPL)
    agents = [MockREPLAgent(name="mock-repl")]
    report = BenchmarkRunner(tasks, agents, MockJudge(), out_dir=str(tmp_path / "out_obs"), seed=0).run()
    assert all(r.ok for r in report.records), [r.error for r in report.records if not r.ok]
    ep = tmp_path / "out_obs" / "episodes" / "agentic_0001__mock-repl"
    # record.json carries observation stats
    rec = json.loads((ep / "record.json").read_text(encoding="utf-8"))
    obs = rec["observations"]
    assert obs["turns"] >= 1 and obs["calls"] >= 1
    assert obs["viewer"] == "process.html"
    # kernel-side logs + frames/diffs written
    assert (ep / "observations" / "turns.jsonl").is_file()
    assert (ep / "observations" / "calls.jsonl").is_file()
    assert len(list((ep / "observations" / "frames").glob("*.png"))) >= 1
    # process viewer generated with embedded frame references
    assert (ep / "process.html").is_file()
    assert "frames/turn" in (ep / "process.html").read_text(encoding="utf-8")


def test_runner_observe_disabled(tmp_path):
    tasks = smoke_tasks()[2:3]
    agents = [MockREPLAgent(name="mock-repl")]
    report = BenchmarkRunner(tasks, agents, MockJudge(), out_dir=str(tmp_path / "out_noobs"), seed=0, observe=False).run()
    ep = tmp_path / "out_noobs" / "episodes" / "agentic_0001__mock-repl"
    rec = json.loads((ep / "record.json").read_text(encoding="utf-8"))
    assert "observations" not in rec
    assert not (ep / "process.html").exists()


def test_runner_replication_and_restoration(tmp_path):
    tasks = smoke_tasks()[4:]  # 2 replication + 2 restoration
    agents = [MockREPLAgent(name="mock-repl")]
    report = BenchmarkRunner(tasks, agents, MockJudge(), out_dir=str(tmp_path / "out2"), seed=0).run()
    assert all(r.ok for r in report.records), [r.error for r in report.records if not r.ok]
    rep = [r for r in report.records if r.task_type == "replication"]
    res = [r for r in report.records if r.task_type == "restoration"]
    assert all(r.metrics["replication"]["pixel_accuracy"] == 1.0 for r in rep)
    assert all(r.metrics["restoration"]["protected_change_rate"] == 0.0 for r in res)
    assert all(r.judge is not None and "overall" in r.judge for r in report.records)


def test_rerun_overwrites_episode_observations(tmp_path):
    # re-running into the same out_dir must not append to the previous
    # run's observer logs (calls.jsonl / turns.jsonl are append-mode)
    tasks = smoke_tasks()[2:3]
    agents = [MockREPLAgent(name="mock-repl")]
    out = str(tmp_path / "out")
    BenchmarkRunner(tasks, agents, MockJudge(), out_dir=out, seed=0).run()
    ep = Path(out) / "episodes" / "agentic_0001__mock-repl"
    n1 = len((ep / "observations" / "calls.jsonl").read_text(encoding="utf-8").splitlines())
    assert n1 >= 1
    BenchmarkRunner(tasks, agents, MockJudge(), out_dir=out, seed=0).run()
    n2 = len((ep / "observations" / "calls.jsonl").read_text(encoding="utf-8").splitlines())
    assert n2 == n1  # second run replaced the episode dir
    rec = json.loads((ep / "record.json").read_text(encoding="utf-8"))
    assert rec["observations"]["calls"] == n2  # stats not inflated by stale rows


def test_runner_tolerates_agent_failure(tmp_path):
    class BrokenAgent(MockREPLAgent):
        def run(self, task, session, budget):
            raise RuntimeError("agent crashed")

    tasks = smoke_tasks()[2:3]
    report = BenchmarkRunner(tasks, [BrokenAgent(name="broken")], MockJudge(), out_dir=str(tmp_path / "out3")).run()
    rec = report.records[0]
    assert rec.ok is False
    assert "agent crashed" in rec.error


def test_config_smoke_roundtrip(tmp_path):
    cfg = BenchmarkConfig.from_dict({"tasks": "smoke", "agents": [{"type": "mock-repl", "name": "m"}], "judge": {"type": "mock"}, "out_dir": "o"})
    cfg.to_dict()
    tasks = cfg.load_tasks()
    assert len(tasks) == 10
    filtered = BenchmarkConfig.from_dict({"tasks": {"types": ["agentic_creation"]}})
    assert all(t.task_type == "agentic_creation" for t in filtered.load_tasks())
    p = tmp_path / "cfg.json"
    p.write_text(json.dumps(cfg.to_dict()))
    cfg2 = BenchmarkConfig.from_json(str(p))
    assert cfg2.out_dir == "o"


def test_config_env_interpolation(tmp_path, monkeypatch):
    monkeypatch.setenv("PIXELBENCH_API_KEY", "sk-test-123")
    p = tmp_path / "cfg.json"
    p.write_text(
        json.dumps(
            {
                "tasks": "smoke",
                "agents": [
                    {
                        "type": "sdk-repl",
                        "name": "s",
                        "model": "m",
                        "llm": {"base_url": "https://api.example.com/v1", "api_key": "${PIXELBENCH_API_KEY}"},
                    }
                ],
                "judge": {"type": "mock"},
            }
        )
    )
    cfg = BenchmarkConfig.from_json(str(p))
    assert cfg.agents[0]["llm"]["api_key"] == "sk-test-123"
    assert cfg.agents[0]["llm"]["base_url"] == "https://api.example.com/v1"


def test_run_missing_config_returns_error(capsys):
    from pixelbench.cli import main

    rc = main(["run", "--config", "/nonexistent/config.json"])
    assert rc == 1
    assert "config file not found" in capsys.readouterr().err
