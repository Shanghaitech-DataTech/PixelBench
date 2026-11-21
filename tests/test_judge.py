from pixelbench.eval.judge import (
    EpisodeView,
    MockJudge,
    _parse_judge_json,
    dims_for,
)
from pixelbench.tasks.smoke import smoke_tasks


def test_dims_for():
    common = dims_for("agentic_creation")
    assert "prompt_alignment" in [d for d, _ in common]
    assert "fidelity" not in [d for d, _ in common]
    assert "fidelity" in [d for d, _ in dims_for("replication")]
    assert "seamless_repair" in [d for d, _ in dims_for("restoration")]


def test_mock_judge_deterministic():
    t = smoke_tasks()[4]
    judge = MockJudge()
    ep = EpisodeView(task=t, agent_name="mock-repl", final_canvas=t.reference.copy(),
                     reference=t.reference, metrics={"replication": {"pixel_accuracy": 1.0, "palette_recall": 1.0}})
    a = judge.score(ep)
    b = judge.score(ep)
    assert a == b
    assert a["dims"]["fidelity"]["score"] == 5.0
    assert 1.0 <= a["overall"] <= 5.0
    # all rubric dims present with 1..5 scores
    for name, _ in dims_for("replication"):
        assert name in a["dims"]
        assert 1.0 <= a["dims"][name]["score"] <= 5.0


def test_mock_judge_restoration_scores_protected_change():
    t = smoke_tasks()[6]
    judge = MockJudge()
    ep = EpisodeView(task=t, agent_name="a", final_canvas=t.reference.copy(),
                     metrics={"restoration": {"region_accuracy": 0.9, "protected_change_rate": 0.0}})
    s = judge.score(ep)
    assert s["dims"]["seamless_repair"]["score"] > 4.0
    ep2 = EpisodeView(task=t, agent_name="a", final_canvas=t.reference.copy(),
                      metrics={"restoration": {"region_accuracy": 0.2, "protected_change_rate": 0.8}})
    s2 = judge.score(ep2)
    assert s2["dims"]["seamless_repair"]["score"] < s["dims"]["seamless_repair"]["score"]


def test_parse_judge_json_variants():
    assert _parse_judge_json('{"scores": {"a": {"score": 4, "reason": "ok"}}}')["scores"]["a"]["score"] == 4
    assert _parse_judge_json('```json\n{"overall": 3}\n```')["overall"] == 3
    assert _parse_judge_json("garbage") == {}
