import pytest

from pixelbench.agents.base import AgentResult, Budget
from pixelbench.agents.direct_agent import DirectGenAgent
from pixelbench.agents.mock import MockDirectAgent, MockREPLAgent
from pixelbench.agents.repl_agent import REPLAgent, build_episode_user_content
from pixelbench.tasks.smoke import smoke_tasks

pytest.importorskip("ipykernel")

from tests.conftest import FakeLLM, FakeMessage, image_url_parts, message_has_image, tool_call


def test_mock_direct_agent():
    t = smoke_tasks()[0]
    agent = MockDirectAgent()
    res = agent.run(t, None, Budget())
    assert res.ok and res.final_canvas is not None
    assert res.final_canvas.width == 16


def test_build_sdk_repl_agent_with_llm_config():
    from pixelbench.agents import build_agent

    a = build_agent(
        {
            "type": "sdk-repl",
            "name": "sdk",
            "model": "deepseek-v4-flash",
            "llm": {"base_url": "https://api.deepseek.com", "api_key": "sk-x", "temperature": 0.3},
        }
    )
    assert a.name == "sdk"
    assert a.model == "deepseek-v4-flash"
    assert a.base_url == "https://api.deepseek.com"
    assert a.api_key == "sk-x"
    assert a.temperature == 0.3


def test_mock_repl_agent_agentic(kernel):
    t = smoke_tasks()[2]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=None, seed=0), timeout=60)
    res = MockREPLAgent().run(t, kernel, Budget())
    assert res.ok, res.error
    assert res.final_canvas is not None
    assert res.final_canvas.stats()["used_pixels"] > 0


def test_mock_repl_agent_replication(kernel):
    t = smoke_tasks()[4]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=t.reference_state(), mask_state=None, seed=0), timeout=60)
    res = MockREPLAgent().run(t, kernel, Budget())
    assert res.ok, res.error
    assert (res.final_canvas.matrix == t.reference.matrix).all()


def test_mock_repl_agent_restoration_respects_mask(kernel):
    t = smoke_tasks()[6]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=t.mask_state(), seed=0), timeout=60)
    corrupted = t.reference.copy()
    corrupted.matrix[t.mask] = corrupted.transparent_id
    res = MockREPLAgent().run(t, kernel, Budget())
    assert res.ok, res.error
    # protected region untouched
    assert (res.final_canvas.matrix[~t.mask] == corrupted.matrix[~t.mask]).all()
    # masked region repainted (not transparent everywhere)
    assert res.final_canvas.matrix[t.mask].sum() > 0


# ------------------------------------------------------------ REPLAgent loop
def test_repl_agent_loop_with_fake_llm(kernel):
    t = smoke_tasks()[2]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=None, seed=0), timeout=60)

    def step1(messages, tools):
        return FakeMessage(content=None, tool_calls=[
            tool_call("call_1", "run_code", {"code": "c=input_canvas.copy()\nc.rect(2,2,10,10,'#2b2b2b')\nview(c,scale=8)"})
        ])

    def step2(messages, tools):
        return FakeMessage(content=None, tool_calls=[tool_call("call_2", "run_code", {"code": "finish(c)"})])

    fake = FakeLLM([step1, step2])
    agent = REPLAgent(name="fake-repl", llm=fake)
    res = agent.run(t, kernel, Budget(max_steps=10))
    assert res.ok, res.error
    assert res.steps_used == 2
    assert res.final_canvas is not None
    assert res.final_canvas.stats()["used_pixels"] == 100
    # the render() call produced an image that got injected into the history
    assert message_has_image(fake.calls[0]["messages"]) is False
    assert image_url_parts(fake.calls[1]["messages"]) >= 1


def test_repl_agent_loop_stops_on_finish_from_code(kernel):
    t = smoke_tasks()[2]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=None, seed=0), timeout=60)

    def step1(messages, tools):
        return FakeMessage(content=None, tool_calls=[
            tool_call("c1", "run_code", {"code": "c=input_canvas.copy().set(0,0,'#e0455a')\nfinish(c)"})
        ])

    fake = FakeLLM([step1])
    agent = REPLAgent(name="fake-repl", llm=fake, max_steps=20)
    res = agent.run(t, kernel, Budget(max_steps=20))
    assert res.ok
    assert res.steps_used == 1  # only one code step


def test_repl_agent_vision_off(kernel):
    t = smoke_tasks()[2]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=None, seed=0), timeout=60)

    def step1(messages, tools):
        return FakeMessage(content=None, tool_calls=[
            tool_call("c1", "run_code", {"code": "view(input_canvas,scale=8)"})
        ])

    def step2(messages, tools):
        return FakeMessage(content="done")

    fake = FakeLLM([step1, step2])
    agent = REPLAgent(name="fake-repl", llm=fake, vision=False)
    res = agent.run(t, kernel, Budget(max_steps=10))
    assert res.ok
    # no image_url parts attached when vision is off
    assert image_url_parts(fake.calls[1]["messages"]) == 0


def test_repl_agent_episode_events_bridge(kernel):
    """The web console's observer protocol fires per-step events and can
    abort the run; images from render() are fed back to vision models
    through the SAME shared loop (the fix for the web console)."""
    t = smoke_tasks()[2]
    from pixelbench.repl.prelude import build_prelude
    from pixelbench.agents.repl_agent import EpisodeEvents

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=None, seed=0), timeout=60)

    class Recorder(EpisodeEvents):
        def __init__(self):
            self.events = []
            self.abort_after = None
        def on_llm_response(self, step, content, tool_calls, usage=None):
            self.events.append(("llm", step, content))
        def on_code_call(self, step, tc_id, code):
            self.events.append(("code_call", step, tc_id))
        def on_code_result(self, step, tc_id, code, result, session):
            self.events.append(("code_result", step, tc_id, len(result.images)))
        def on_round_end(self, step):
            self.events.append(("round_end", step))
            return self.abort_after is None or step < self.abort_after
        def on_run_end(self, result):
            self.events.append(("run_end", result.ok))

    def step1(messages, tools):
        return FakeMessage(content="sketching", tool_calls=[
            tool_call("c1", "run_code", {"code": "c=input_canvas.copy().rect(0,0,8,8,'#e0455a')\nview(c,scale=8)"})
        ])

    def step2(messages, tools):
        return FakeMessage(content=None, tool_calls=[tool_call("c2", "run_code", {"code": "finish(c)"})])

    # vision model: render() images must reach the model as image_url parts
    fake = FakeLLM([step1, step2])
    agent = REPLAgent(name="fake-repl", llm=fake, vision=True, max_steps=10)
    rec = Recorder()
    res = agent.run(t, kernel, Budget(max_steps=10), events=rec)
    assert res.ok, res.error
    assert image_url_parts(fake.calls[1]["messages"]) >= 1  # image fed back
    kinds = [e[0] for e in rec.events]
    assert "llm" in kinds and "code_call" in kinds and "code_result" in kinds
    assert ("code_result", 0, "c1", 1) in rec.events  # render produced 1 image
    assert ("round_end", 0) in rec.events
    assert rec.events[-1][0] == "run_end"


def test_repl_agent_events_can_abort_round(kernel):
    """A host returning False from on_round_end stops the episode."""
    t = smoke_tasks()[2]
    from pixelbench.repl.prelude import build_prelude
    from pixelbench.agents.repl_agent import EpisodeEvents

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=None, seed=0), timeout=60)

    class Abort(EpisodeEvents):
        def __init__(self):
            self.rounds = 0
        def on_round_end(self, step):
            self.rounds += 1
            return False  # abort after first round

    def step1(messages, tools):
        return FakeMessage(content=None, tool_calls=[
            tool_call("c1", "run_code", {"code": "register_color('r', '#e0455a')\npaint_rect(0,0,8,8,'r')"})
        ])

    fake = FakeLLM([step1, step1, step1])  # would keep going without abort
    agent = REPLAgent(name="fake-repl", llm=fake, vision=False, max_steps=10)
    ab = Abort()
    res = agent.run(t, kernel, Budget(max_steps=10), events=ab)
    assert ab.rounds == 1
    assert res.final_canvas is not None  # canvas still extracted


def test_repl_agent_reference_image_in_initial_message():
    t = smoke_tasks()[4]
    content = build_episode_user_content(t, reference_png=t.reference.render_png_bytes(scale=8))
    assert any(isinstance(p, dict) and p.get("type") == "image_url" for p in content)


def test_direct_agent_redraw_loop_with_fake_llm(kernel):
    t = smoke_tasks()[0]  # direct_0001 (16x16 heart)
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(
        build_prelude(
            task=t.public_task(), initial_state=t.initial_state(),
            reference_state=None, mask_state=None, seed=0, surface="redraw",
        ),
        timeout=60,
    )

    def step1(messages, tools):
        rows = [["red" if (i + j) % 3 == 0 else "transparent" for i in range(16)] for j in range(16)]
        code = "c=input_canvas.copy()\nc.color('#e0455a', name='red')\nredraw(c," + repr(rows) + ")\nview(c,scale=8)"
        return FakeMessage(content=None, tool_calls=[tool_call("c1", "run_code", {"code": code})])

    def step2(messages, tools):
        return FakeMessage(content=None, tool_calls=[tool_call("c2", "run_code", {"code": "finish(c)"})])

    fake = FakeLLM([step1, step2])
    agent = DirectGenAgent(name="fake-direct", llm=fake)
    res = agent.run(t, kernel, Budget(max_steps=10))
    assert res.ok, res.error
    assert res.steps_used == 2
    assert res.final_canvas is not None
    assert res.final_canvas.stats()["used_pixels"] > 0
    # the render() image was injected back into the conversation history
    assert image_url_parts(fake.calls[1]["messages"]) >= 1


def test_redraw_surface_binds_only_redraw_tools(kernel):
    t = smoke_tasks()[0]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(
        build_prelude(
            task=t.public_task(), initial_state=t.initial_state(),
            reference_state=None, mask_state=None, seed=0, surface="redraw",
        ),
        timeout=60,
    )
    r = kernel.execute(
        "print(callable(redraw), callable(input_canvas.color), callable(view), callable(input_canvas.matrix_text))\n"
        "try:\n"
        "    set_pixel\n"
        "    print('LEAK')\n"
        "except NameError:\n"
        "    print('locked')\n",
        timeout=30,
    )
    assert r.ok, r.combined()
    assert "True True True True" in r.stdout
    assert "locked" in r.stdout


def test_run_code_docs_differ_by_vision():
    from pixelbench.agents.repl_agent import run_code_tool

    for surface in ("full", "redraw"):
        vis = run_code_tool(surface, vision=True)["function"]["description"]
        text = run_code_tool(surface, vision=False)["function"]["description"]
        # multimodal docs announce the model type and the image modes
        assert "multimodal model" in vis
        assert "image" in vis
        assert "view(canvas" in vis
        # text-only docs hide every vision option: no 'render(' tool, no
        # 'fed to your vision', no observe_region(mode='image')
        assert "render(" not in text
        assert "fed to your vision" not in text
        assert "mode='image'" not in text
        assert "multimodal" not in text
    # mode semantics are spelled out
    full = run_code_tool("full", vision=False)["function"]["description"]
    assert "matrix_text" in full
    assert "stats_text" in full
    assert "canvas_chars" not in full  # char-art REPL tool removed
    assert "ascii" not in full  # luminance ascii channel removed


def test_build_agent_requires_vision_registration():
    from pixelbench.agents import build_agent

    # a repl agent without an explicit vision flag is rejected: every
    # evaluated model must register whether it is multimodal
    with pytest.raises(ValueError, match="must register its vision capability"):
        build_agent(
            {
                "type": "repl",
                "name": "no-vision",
                "llm": {"base_url": "http://localhost:9", "api_key": "sk-x"},
            }
        )
    for flag in (True, False):
        a = build_agent(
            {
                "type": "repl",
                "name": "reg",
                "vision": flag,
                "llm": {"base_url": "http://localhost:9", "api_key": "sk-x"},
            }
        )
        assert a.vision is flag


def test_system_prompt_matches_vision():
    from pixelbench.agents.repl_agent import REPLAgent

    vis = REPLAgent(name="v", llm=None)
    assert "multimodal" in vis.system_prompt
    text = REPLAgent(name="t", llm=None, vision=False)
    assert "text-only" in text.system_prompt
    assert "multimodal" not in text.system_prompt
    redraw_text = REPLAgent(name="rt", llm=None, surface="redraw", vision=False)
    assert "text-only" in redraw_text.system_prompt


def test_step_budget_announced_once(kernel):
    # the total step budget is announced up front, but tool results no
    # longer carry a per-step [step k/N] prefix
    t = smoke_tasks()[2]
    from pixelbench.repl.prelude import build_prelude

    kernel.execute(build_prelude(task=t.public_task(), initial_state=t.initial_state(), reference_state=None, mask_state=None, seed=0), timeout=60)

    def step1(messages, tools):
        return FakeMessage(content=None, tool_calls=[tool_call("c1", "run_code", {"code": "c=input_canvas.copy()\nc.color('#e0455a',name='red')"})])

    def step2(messages, tools):
        return FakeMessage(content=None, tool_calls=[tool_call("c2", "run_code", {"code": "finish(c)"})])

    fake = FakeLLM([step1, step2])
    agent = REPLAgent(name="fake-repl", llm=fake)
    res = agent.run(t, kernel, Budget(max_steps=10))
    assert res.ok
    # the initial user content announces the total budget
    first_user = fake.calls[0]["messages"][-1]
    text = " ".join(p["text"] for p in first_user["content"] if isinstance(p, dict) and p.get("type") == "text")
    assert "at most 10 model rounds" in text
    # tool results are plain (no per-step prefix)
    for call in fake.calls[1:]:
        for m in call["messages"]:
            if m["role"] == "tool":
                assert not str(m["content"]).startswith("[step")
                assert "[step" not in str(m["content"])


# ------------------------------------------------------------ Responses API
def test_llm_client_api_format_validation():
    from pixelbench.agents.chat import LLMClient

    for bad in ("bogus", "", None):
        with pytest.raises(ValueError):
            LLMClient(model="gpt-5.5", base_url="http://localhost:9", api_key="sk-x", api_format=bad)


def test_to_responses_input_converts_message_shapes():
    from pixelbench.agents.chat import _to_responses_input, _to_responses_tools

    messages = [
        {"role": "system", "content": "be terse"},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "look at this"},
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,AAAA"}},
            ],
        },
        {
            "role": "assistant",
            "content": "",
            "tool_calls": [
                {
                    "id": "call_1",
                    "type": "function",
                    "function": {"name": "echo", "arguments": '{"text":"hi"}'},
                }
            ],
        },
        {"role": "tool", "tool_call_id": "call_1", "content": "echo: hi"},
    ]
    items = _to_responses_input(messages)
    assert items[0] == {"role": "system", "content": [{"type": "input_text", "text": "be terse"}]}
    assert items[1]["content"][0] == {"type": "input_text", "text": "look at this"}
    assert items[1]["content"][1] == {"type": "input_image", "image_url": "data:image/png;base64,AAAA"}
    assert items[2] == {
        "call_id": "call_1",
        "type": "function_call",
        "name": "echo",
        "arguments": '{"text":"hi"}',
    }
    assert items[3] == {"type": "function_call_output", "call_id": "call_1", "output": "echo: hi"}

    tools = [
        {
            "type": "function",
            "function": {
                "name": "echo",
                "description": "echo text",
                "parameters": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]},
            },
        }
    ]
    converted = _to_responses_tools(tools)
    assert converted[0]["type"] == "function"
    assert converted[0]["name"] == "echo"
    assert converted[0]["parameters"]["properties"]["text"]["type"] == "string"
    assert converted[0]["strict"] is False


def test_responses_output_normalized_to_completions_shape():
    from pixelbench.agents.chat import _MessageShim, _ResponseShim, _ToolCallShim

    msg = _MessageShim(
        "all good",
        tool_calls=[
            _ToolCallShim("call_9", "run_code", '{"code":"x=1"}'),
        ],
    )
    resp = _ResponseShim(msg)
    assert resp.choices[0].message.content == "all good"
    tc = resp.choices[0].message.tool_calls[0]
    assert tc.id == "call_9"
    assert tc.function.name == "run_code"
    assert tc.function.arguments == '{"code":"x=1"}'
    dumped = tc.model_dump()
    assert dumped["id"] == "call_9"
    assert dumped["function"]["name"] == "run_code"


def test_should_fallback_to_responses():
    from pixelbench.agents.chat import LLMError, _should_fallback_to_responses

    assert _should_fallback_to_responses(LLMError("must use the Responses API"))
    assert not _should_fallback_to_responses(LLMError("connection refused"))
    e = LLMError("404: model not found")
    e.status_code = 404
    assert _should_fallback_to_responses(e)
