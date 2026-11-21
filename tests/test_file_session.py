import json
import time

import pytest

from pixelbench.agents.base import Budget
from pixelbench.agents.repl_agent import REPLAgent
from pixelbench.repl.file_session import FileSession
from pixelbench.repl.prelude import build_prelude
from pixelbench.tasks.specs import TaskSpec
from tests.conftest import FakeLLM, FakeMessage, tool_call


def setup(tmp_path, count=1, width=4, height=4):
    task = TaskSpec('files', 'agentic_creation', 'draw', width, height, num_frames=count)
    session = FileSession(tmp_path)
    session.execute_checked(build_prelude(task.public_task(), task.initial_state()), what='prelude')
    return task, session


def pixel(session, x=0, y=0):
    return session.extract_submission()[0][0].render(scale=1).getpixel((x, y))


def test_preview_then_edit_helper_and_submit_fresh(tmp_path):
    _, s = setup(tmp_path)
    s.write_file('art/helper.py', "from pixelbench_api import new_canvas\ndef draw():\n return new_canvas(4,4).set(0,0,'#f00')")
    s.write_file('art/main.py', "from helper import draw\nassert 'stale' not in globals()\nstale=1\nc=draw()\nview(c)\nfinish(c)\nc.clear()")
    r = s.run('art/main.py')
    assert r.ok and not r.finished and len(r.images) == 1
    assert pixel(s) == (255,0,0,255)
    assert s.extract_submission()[1]['source'] == 'recovered'
    s.edit_file('art/helper.py', '#f00', '#00f')
    assert not s.extract_submission()[1]['source_matches_workspace']
    r = s.run('art/main.py', submit=True)
    assert r.ok and r.finished, r.combined()
    assert pixel(s) == (0,0,255,255)
    assert s.extract_submission()[1]['source'] == 'explicit'
    assert s.extract_submission()[1]['source_matches_workspace']
    snapshots = sorted((s.root / 'runs').glob('*/source/art/helper.py'))
    assert '#f00' in snapshots[0].read_text() and '#00f' in snapshots[1].read_text()


def test_failed_submit_and_timeout_preserve_preview(tmp_path):
    _, s = setup(tmp_path)
    s.write_file('main.py', "c=new_canvas(4,4).set(0,0,'#f00')\nfinish(c)")
    assert s.run().ok
    s.write_file('main.py', "c=new_canvas(4,4).set(0,0,'#00f')\nfinish(c)\nraise RuntimeError('after finish')")
    r = s.run(submit=True)
    assert not r.ok and not r.finished
    latest = json.loads(s.latest_checkpoint_path.read_text())
    assert latest['submission']['source'] == 'recovered'
    assert latest['submission']['accepted'] is False
    assert pixel(s) == (255,0,0,255)
    s.write_file('main.py', 'while True: pass')
    r = s.run(submit=True, timeout=1)
    assert r.timed_out and not r.finished and s.is_alive()
    assert pixel(s) == (255,0,0,255)
    assert not s.extract_submission()[1]['source_matches_workspace']


def test_counts_retry_and_heuristic_order_blank(tmp_path):
    _, s = setup(tmp_path, count=2)
    code = "a=new_canvas(4,4).set(0,0,'#f00')\nb=new_canvas(4,4)\nresults=[b,a]"
    s.write_file('main.py', code)
    r = s.run(submit=True)
    assert not r.ok and not r.finished
    outputs, meta = s.extract_submission()
    assert len(outputs) == 2 and outputs[0].stats()['used_pixels'] == 0
    s.write_file('main.py', code + '\nfinish(a)')
    assert s.run(submit=True).finished
    assert len(s.extract_final_frames()) == 1
    assert not s.extract_submission()[1]['count_match']
    s.write_file('main.py', code + '\nfinish(results)')
    assert s.run(submit=True).finished


def test_last_round_file_loop(tmp_path, monkeypatch):
    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND', 'off')
    task, s = setup(tmp_path)
    llm = FakeLLM([
        FakeMessage(tool_calls=[tool_call('w','write_file',{'path':'main.py','content':'finish(input_canvas)'}),
                                tool_call('p','run',{'path':'main.py'})]),
        FakeMessage(tool_calls=[tool_call('s','run',{'path':'main.py','submit':True})]),
    ])
    result = REPLAgent(llm=llm).run(task, s, Budget(max_steps=2))
    assert result.ok and result.submission['source'] == 'explicit'
    assert len(llm.calls) == 2
    assert 'LAST ROUND' in str(llm.calls[-1]['messages'])
    assert [t['function']['name'] for t in llm.calls[0]['tools']] == ['write_file','edit_file','read_file','list_files','run']


def test_agent_preserves_native_reasoning_and_preview_for_next_request(tmp_path, monkeypatch):
    from pixelbench.agents.chat import _to_responses_input

    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND', 'off')
    task, session = setup(tmp_path)
    first = FakeMessage(tool_calls=[
        tool_call('w', 'write_file', {'path': 'main.py', 'content': 'view(input_canvas)\nfinish(input_canvas)'}),
        tool_call('p', 'run', {'path': 'main.py'}),
    ])
    reasoning = {'type': 'reasoning', 'id': 'rs_1', 'summary': [], 'encrypted_content': 'opaque-state'}
    first.responses_output = [reasoning] + [
        {'type': 'function_call', 'call_id': tc['id'], **tc['function']}
        for tc in first.tool_calls
    ]

    def submit(messages, tools):
        items = _to_responses_input(messages)
        assert reasoning in items
        assert [x['call_id'] for x in items if x.get('type') == 'function_call'] == ['w', 'p']
        assert [x['call_id'] for x in items if x.get('type') == 'function_call_output'] == ['w', 'p']
        assert any(part.get('type') == 'input_image' for item in items
                   if isinstance(item.get('content'), list) for part in item['content'])
        return FakeMessage(tool_calls=[tool_call('s', 'run', {'path': 'main.py', 'submit': True})])

    result = REPLAgent(llm=FakeLLM([first, submit])).run(task, session, Budget(max_steps=3))
    assert result.ok and result.submission['source'] == 'explicit'


def test_large_pixel_loop_has_no_per_operation_snapshots(tmp_path):
    _, s = setup(tmp_path, width=200, height=250)
    s.write_file('main.py', """
def forbidden(*args, **kwargs):
    raise AssertionError('per-operation full conversion or snapshot')
_pb_skill._snapshot = forbidden
original = _pb_skill.to_pixel_canvas
_pb_skill.to_pixel_canvas = forbidden
c = new_canvas(200,250)
for y in range(250):
    for x in range(200):
        c.set(x,y,'#f00')
assert not _pb_skill.events and not _pb_skill.calls
_pb_skill.to_pixel_canvas = original
finish(c)
""")
    r = s.run(submit=True, timeout=15)
    assert r.ok and r.finished, r.combined()
    assert s.extract_final_canvas().stats()['used_pixels'] == 50000


def test_source_paths_and_unique_edits(tmp_path):
    _, s = setup(tmp_path)
    for path in ('../escape.py','/tmp/escape.py'):
        with pytest.raises(ValueError):
            s.write_file(path, 'bad')
    s.write_file('main.py','aa aa')
    with pytest.raises(ValueError):
        s.edit_file('main.py','aa','b')


def test_sdk_file_tools_and_preview_does_not_stop(tmp_path, monkeypatch):
    import asyncio
    from types import SimpleNamespace
    agents = pytest.importorskip('agents')
    from pixelbench.agents.sdk_adapter import AgentsSdkReplAgent
    task, s = setup(tmp_path, count=2)
    adapter = AgentsSdkReplAgent()
    def fake_run(agent, input, run_config, max_turns, hooks):
        assert [t.name for t in agent.tools] == ['write_file','edit_file','read_file','list_files','run']
        items = []
        asyncio.run(hooks.on_llm_start(None, agent, None, items))
        adapter._write_file('main.py', 'a=new_canvas(4,4)\nfinish([a,a.copy()])')
        adapter._run_file()
        assert not asyncio.run(agent.tool_use_behavior(None, [])).is_final_output
        asyncio.run(hooks.on_llm_start(None, agent, None, items))
        assert 'LAST ROUND' in items[-1]['content'] and 'submit=True' in items[-1]['content']
        adapter._run_file(submit=True)
        assert asyncio.run(agent.tool_use_behavior(None, [])).is_final_output
        return SimpleNamespace(final_output='submitted')
    monkeypatch.setattr(agents.Runner, 'run_sync', fake_run)
    result = adapter.run(task, s, Budget(max_steps=2))
    assert result.ok and result.submission['source'] == 'explicit', result.transcript


def test_redraw_file_surface_and_prompt(tmp_path, monkeypatch):
    from pixelbench.agents.direct_agent import DirectGenAgent
    task = TaskSpec('direct-files','agentic_creation','draw',4,4)
    s = FileSession(tmp_path)
    s.execute_checked(build_prelude(task.public_task(),task.initial_state(),surface='redraw'),what='prelude')
    s.write_file('main.py', "c=new_canvas(4,4)\nc.set(0,0,'#f00')\nfinish(c)")
    assert not s.run(submit=True).ok
    llm = FakeLLM([FakeMessage(tool_calls=[
        tool_call('w','write_file',{'path':'main.py','content':"c=new_canvas(4,4)\nredraw(c,[['#f00']*4 for _ in range(4)])\nfinish(c)"}),
        tool_call('r','run',{'path':'main.py','submit':True}),
    ])])
    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND','off')
    result = DirectGenAgent(llm=llm).run(task,s,Budget(max_steps=1))
    assert result.ok and result.submission['source'] == 'explicit'
    assert 'persistent Python REPL' not in llm.calls[0]['messages'][0]['content']


def test_user_files_cannot_shadow_runtime_dependencies(tmp_path):
    _, s = setup(tmp_path)
    for name in ('inspect', 'json', 'numpy', 'random'):
        s.write_file(name + '.py', "raise AssertionError('user module imported during bootstrap')")
    s.write_file('helper.py', "def draw(c):\n return c.set(0,0,'#f00')")
    s.write_file('inspect.py', 'import inspect, json, numpy, random\nfrom helper import draw\nassert hasattr(inspect, "cleandoc")\nview(input_canvas)\nfinish(draw(input_canvas.copy()))')
    r = s.run('inspect.py', submit=True)
    assert r.ok and r.finished and len(r.images) == 1, r.combined()
    assert pixel(s) == (255,0,0,255)


def test_edit_accepts_colors_count_and_motion_extent(tmp_path):
    from pixelbench.core.canvas import PixelCanvas
    from pixelbench.repl.skill_docs import skill_user_content
    base = PixelCanvas(16,16)
    task = TaskSpec('edit-free','edit','draw',16,16,base=base,num_frames=3,max_colors=1)
    assert task.public_task()['constraints']['max_colors'] is None
    assert 'limit per image' not in str(skill_user_content(task))
    s = FileSession(tmp_path)
    s.execute_checked(build_prelude(task.public_task(),task.initial_state()),what='prelude')
    s.write_file('main.py', "a=new_canvas(40,40).rect(0,0,8,8,'#f00')\nb=a.copy().rect(0,0,30,30,'#0f0').set(39,39,'#00f')\nfinish([b,a])")
    r = s.run(submit=True)
    assert r.ok and r.finished, r.combined()
    outputs, meta = s.extract_submission()
    assert len(outputs) == 2 and not meta['count_match']
    assert outputs[0].render(scale=1).getpixel((39,39)) == (0,0,255,255)


def test_failed_output_attempt_beats_successful_inspection(tmp_path):
    _, s = setup(tmp_path, count=2)
    s.write_file('look.py', 'view(input_canvas)')
    assert s.run('look.py').ok
    s.write_file('main.py', "a=input_canvas.copy().set(0,0,'#f00')\nb=a.copy().set(1,0,'#00f')\nfinish([b,a])\nraise RuntimeError('after declaration')")
    assert not s.run(submit=True).finished
    assert len(s.extract_final_frames()) == 2
    assert pixel(s,1,0) == (0,0,255,255)
    assert s.run('look.py').ok
    assert len(s.extract_final_frames()) == 2  # Later inspection cannot erase progress.
    assert s.extract_submission()[1]['source'] == 'recovered'


def test_request_failure_survives_recovery_and_is_durable(tmp_path, monkeypatch):
    task, s = setup(tmp_path)
    s.write_file('main.py', "finish(input_canvas.copy().set(0,0,'#f00'))")
    s.run()
    def fail(messages, tools):
        raise RuntimeError('endpoint unavailable test')
    llm = FakeLLM([fail])
    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND','off')
    result = REPLAgent(llm=llm).run(task,s,Budget(max_steps=2))
    assert not result.ok
    assert 'endpoint unavailable test' in result.error
    assert result.final_canvas is not None
    rows = [json.loads(line) for line in (s.root/'events.jsonl').read_text().splitlines()]
    assert any(r['kind']=='llm_request' for r in rows)
    assert any(r['kind']=='llm_error' and 'endpoint unavailable test' in r['content'] for r in rows)
    assert result.submission['termination_reason']=='llm_error'


def test_empty_response_retries_keep_images_and_round_budget(tmp_path, monkeypatch):
    task, s = setup(tmp_path)
    llm = FakeLLM([
        FakeMessage(tool_calls=[tool_call('w','write_file',{'path':'main.py','content':'view(input_canvas)\nfinish(input_canvas)'}),
                               tool_call('r','run',{'path':'main.py'})]),
        FakeMessage(content=''),
        FakeMessage(tool_calls=[tool_call('s','run',{'path':'main.py','submit':True})]),
    ])
    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND','off')
    result = REPLAgent(llm=llm).run(task,s,Budget(max_steps=2))
    assert result.submission['source']=='explicit'
    assert llm.calls[1]['messages']==llm.calls[2]['messages']
    assert 'image_url' in str(llm.calls[2]['messages'])
    assert 'LAST ROUND' in str(llm.calls[2]['messages'])


@pytest.mark.parametrize('operation', [
    "c.set(-1, 0, '#f00')",
    "c.rect(3, 3, 2, 2, '#f00')",
    "c.poly([(2, 2), (6, 2), (6, 6)], '#f00')",
    "c.path('M 2 2 L 6 2 L 6 6 Z', '#f00')",
    "c.blit(new_canvas(2, 2).rect(0, 0, 2, 2, '#ff000088'), 3, 3)",
    "c.set(3, 3, '#f00'); c.shift(1, 1)",
    "c.select(0, 0, 2, 2).copy_to(3, 3, c)",
])
def test_clipping_warns_but_continues_and_submits(tmp_path, operation):
    _, s = setup(tmp_path)
    s.write_file('main.py', "c=new_canvas(4,4,name='output')\n" + operation +
                 "\nc.set(0,0,'#00f')\nfinish(c)")
    result = s.run(submit=True)
    assert result.ok and result.finished, result.combined()
    assert 'WARNING: canvas' in result.stderr
    assert "'output' (4x4)" in result.stderr
    assert 'clipped' in result.stderr
    assert pixel(s) == (0, 0, 255, 255)


def test_clipping_warning_bounded_and_transparent_blit_quiet(tmp_path):
    _, s = setup(tmp_path)
    s.write_file('main.py', "c=new_canvas(4,4)\nc.blit(new_canvas(20,20),-10,-10)\nc.set(3,3,'#f00')\nfinish(c)")
    result = s.run()
    assert result.ok and 'WARNING' not in result.stderr
    s.write_file('main.py', "c=new_canvas(4,4)\nfor x in range(1000): c.set(-1,x,'#f00')\nfinish(c)")
    result = s.run(submit=True)
    assert result.ok and result.finished
    assert result.stderr.count('WARNING: canvas') == 1


def test_write_budget_blocks_extra_edit_but_allows_later_submit(tmp_path, monkeypatch):
    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND', 'off')
    task, s = setup(tmp_path)
    llm = FakeLLM([
        FakeMessage(tool_calls=[tool_call('w', 'write_file', {'path': 'main.py', 'content': "finish(input_canvas.copy().set(0,0,'#f00'))"})]),
        FakeMessage(tool_calls=[tool_call('p', 'run', {'path': 'main.py'})]),
        FakeMessage(tool_calls=[tool_call('extra', 'write_file', {'path': 'main.py', 'content': 'raise RuntimeError()'})]),
        FakeMessage(tool_calls=[tool_call('s', 'run', {'path': 'main.py', 'submit': True})]),
    ])
    result = REPLAgent(llm=llm).run(task, s, Budget(max_steps=1))
    assert result.submission['source'] == 'explicit'
    assert result.steps_used == 1
    assert pixel(s) == (255, 0, 0, 255)
    assert any(r['kind'] == 'write_budget_exhausted' for r in result.transcript)
