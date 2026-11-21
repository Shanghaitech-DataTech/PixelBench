import json

import httpx
import openai
import pytest

from pixelbench.agents.chat import LLMClient, LLMError


@pytest.mark.parametrize('stream', [False, True])
def test_reasoning_tool_and_image_roundtrip(stream):
    """Exercise actual SDK serialization and parsing across two model turns."""
    requests = []
    reasoning = {'id': 'rs_1', 'type': 'reasoning', 'summary': [],
                 'encrypted_content': 'opaque-state'}
    call = {'id': 'fc_1', 'type': 'function_call', 'call_id': 'call_1',
            'name': 'run', 'arguments': '{"path":"main.py"}', 'status': 'completed'}

    def handle(req):
        body = json.loads(req.content)
        requests.append(body)
        assert body['reasoning'] == {'effort': 'high'}
        assert 'reasoning_effort' not in body
        assert body['store'] is False
        assert 'reasoning.encrypted_content' in body['include']
        assert 'temperature' not in body
        output = [reasoning, call] if len(requests) == 1 else [
            {'id': 'msg_1', 'type': 'message', 'role': 'assistant', 'status': 'completed',
             'content': [{'type': 'output_text', 'text': 'done', 'annotations': []}]}]
        response = {'id': 'resp_1', 'object': 'response', 'created_at': 1,
                    'model': 'gpt-6-astra', 'status': 'completed', 'output': output,
                    'reasoning': {'effort': 'high'},
                    'usage': {'input_tokens': 50, 'output_tokens': 30, 'total_tokens': 80,
                              'input_tokens_details': {'cached_tokens': 0},
                              'output_tokens_details': {'reasoning_tokens': 20}}}
        if stream:
            event = {'type': 'response.completed', 'sequence_number': 1, 'response': response}
            return httpx.Response(200, text='data: ' + json.dumps(event) + '\n\n',
                                  headers={'content-type': 'text/event-stream'})
        return httpx.Response(200, json=response)

    client = LLMClient('gpt-6-astra', api_key='test', api_format='responses',
                       temperature=None, stream=stream, extra_body={'reasoning_effort': 'high'})
    client.client = openai.OpenAI(api_key='test', base_url='https://test.invalid/v1',
                                 http_client=httpx.Client(transport=httpx.MockTransport(handle)))
    messages = [{'role': 'user', 'content': 'Draw.'}]
    first = client.chat(messages)
    assert first.usage.completion_tokens == 30
    assert first.raw_usage['output_tokens_details']['reasoning_tokens'] == 20
    messages.extend([
        {'role': 'assistant', 'content': '',
         'tool_calls': [t.model_dump() for t in first.choices[0].message.tool_calls],
         '_responses_output': first.choices[0].message.responses_output},
        {'role': 'tool', 'tool_call_id': 'call_1', 'content': 'ok'},
        {'role': 'user', 'content': [{'type': 'image_url', 'image_url': {
            'url': 'data:image/png;base64,AAAA', 'detail': 'high'}}]},
    ])
    second = client.chat(messages)
    assert second.choices[0].message.content == 'done'
    assert requests[1]['input'][1:3] == [reasoning, call]
    assert requests[1]['input'][3]['type'] == 'function_call_output'
    assert requests[1]['input'][4]['content'][0]['detail'] == 'high'
    assert second.request_metadata['reasoning_items'] == 1
    assert second.request_metadata['input_images'] == 1
    assert 'test' not in json.dumps(second.raw_usage)


def test_developer_instruction_role_is_preserved():
    from pixelbench.agents.chat import _to_responses_input
    from pixelbench.agents import build_agent

    agent = build_agent({'type': 'file', 'name': 'aligned', 'vision': True,
                         'instruction_role': 'developer',
                         'llm': {'api_key': 'test', 'api_format': 'responses',
                                 'model': 'gpt-6-astra', 'extra_body': {'reasoning_effort': 'high'}}})
    assert agent.instruction_role == 'developer'
    assert agent.llm.extra_body['reasoning_effort'] == 'high'
    items = _to_responses_input([{'role': 'developer', 'content': 'API reference'},
                                {'role': 'user', 'content': 'Draw.'}])
    assert items[0] == {'role': 'developer', 'content': 'API reference'}


def test_truncated_stream_is_retried_without_executing_partial_tool():
    count = 0

    def handle(req):
        nonlocal count
        count += 1
        return httpx.Response(200, text='data: {"type":"response.created","sequence_number":0}\n\n',
                              headers={'content-type': 'text/event-stream'})

    client = LLMClient('gpt-6-astra', api_key='test', api_format='responses', stream=True,
                       max_retries=1, retry_backoff=0)
    client.client = openai.OpenAI(api_key='test', http_client=httpx.Client(transport=httpx.MockTransport(handle)))
    with pytest.raises(LLMError, match='terminal response'):
        client.chat([{'role': 'user', 'content': 'draw'}])
    assert count == 2



@pytest.mark.parametrize('model', ['gpt-6-astra', 'gemini-3.8-flash'])
def test_edit_file_loop_through_responses_sdk(model, tmp_path, monkeypatch):
    """Actual SDK + real source execution: alpha, resized frames and image feedback."""
    from pixelbench.agents import build_agent
    from pixelbench.agents.base import Budget
    from pixelbench.repl.file_session import FileSession
    from pixelbench.repl.prelude import build_prelude
    from tests.test_edit_canvas_protocol import input_canvas, pixels
    from pixelbench.tasks.specs import TaskSpec
    import numpy as np

    monkeypatch.setenv('PIXELBENCH_TRACE_BACKEND', 'off')
    task = TaskSpec('edit-responses', 'edit', 'Submit original, expanded edit, and a second edit.',
                    8, 6, base=input_canvas(), num_frames=3)
    session = FileSession(tmp_path)
    session.execute_checked(build_prelude(task.public_task(), task.initial_state()), what='prelude')
    code = """a=new_canvas(9,8,name='original').blit(input_canvas,0,0)
b=a.copy(name='expanded')
b.set(8,7,'#ff0000')
c=b.copy(name='variant').set(8,7,'#0000ff')
view(b)
finish([a,b,c])
b.clear()
"""
    requests = []
    reasoning = {'type': 'reasoning', 'id': 'rs_edit', 'summary': [], 'encrypted_content': 'opaque'}

    def call(cid, name, args):
        return {'type': 'function_call', 'id': 'fc_' + cid, 'call_id': cid,
                'name': name, 'arguments': json.dumps(args), 'status': 'completed'}

    def handle(req):
        body = json.loads(req.content)
        requests.append(body)
        assert req.url.path == '/v1/responses'
        assert body['input'][0]['role'] == 'developer'
        assert isinstance(body['input'][0]['content'], str)
        assert body['stream'] and 'temperature' not in body
        assert ('reasoning' in body) == (model == 'gpt-6-astra')
        assert {t['name'] for t in body['tools']} == {'write_file','read_file','edit_file','list_files','run'}
        if len(requests) == 1:
            output = [reasoning, call('w1','write_file',{'path':'main.py','content':'view(input_canvas)'}),
                      call('p1','run',{'path':'main.py'})]
        else:
            assert reasoning in body['input']
            assert any(p.get('type') == 'input_image' for m in body['input']
                       if isinstance(m.get('content'), list) for p in m['content'])
            assert any(m.get('type') == 'function_call_output' and m['call_id'] == 'p1'
                       for m in body['input'])
            output = ([call('w2','write_file',{'path':'main.py','content':code}),
                       call('p2','run',{'path':'main.py'})] if len(requests) == 2 else
                      [call('s','run',{'path':'main.py','submit':True})])
        response = {'id':'resp_edit', 'object':'response', 'created_at':1, 'model':model,
                    'status':'completed', 'output':output,
                    'usage':{'input_tokens':10,'output_tokens':10,'total_tokens':20}}
        return httpx.Response(200, text='data: '+json.dumps({'type':'response.completed',
                              'sequence_number':1,'response':response})+'\n\n',
                              headers={'content-type':'text/event-stream'})

    agent = build_agent({'type':'file','vision':True,'llm':{'model':model,'api_key':'test','base_url':'https://test.invalid/v1','api_format':'responses','extra_body':({'reasoning_effort':'high'} if model=='gpt-6-astra' else {})}})
    agent.llm.client = openai.OpenAI(api_key='test',base_url='https://test.invalid/v1',
        http_client=httpx.Client(transport=httpx.MockTransport(handle)))
    try:
        result = agent.run(task,session,Budget(max_steps=8))
        assert result.ok, result.error
        assert len(requests) == 3
        frames, meta = session.extract_submission()
        assert meta['source'] == 'explicit' and meta['accepted'] and meta['source_matches_workspace']
        assert len(frames) == 3 and meta['count_match']
        assert [(c.width,c.height) for c in frames] == [(9,8),(9,8),(9,8)]
        expected = pixels(task.base)
        visible = expected[:,:,3] > 0
        for frame in frames:
            actual = pixels(frame)[:3,:3]
            assert np.array_equal(actual[visible],expected[visible])
            assert np.array_equal(actual[:,:,3],expected[:,:,3])
        assert pixels(frames[1])[7,8].tolist() == [255,0,0,255]
        assert pixels(frames[2])[7,8].tolist() == [0,0,255,255]
        assert pixels(frames[1])[0,0,3] == 128
        assert pixels(frames[2])[1,1,3] == 0
    finally:
        session.shutdown()
