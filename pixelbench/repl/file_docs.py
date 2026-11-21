"""Tools and instructions for the source-file protocol."""
from pathlib import Path


def file_api_reference():
    """Pinned Skill API, with its CLI-only execution semantics removed."""
    text = (Path(__file__).resolve().parents[1] / '_vendor/astra_pixelart/api.md').read_text()
    text = text.split('## Canvases\n', 1)[1].split('## How a step is executed\n', 1)[0]
    text = text.replace(
        'Across\nsteps, drop the step with `pixelart undo` instead — or, better, repair the step\n'
        'in place, as described under [How a step is executed](#how-a-step-is-executed).',
        'Across runs, edit the source and rerun; in-memory snapshots are rebuilt by the program.')
    text = text.replace(
        'Coordinates outside the canvas are clipped in silence: no error, just a shape\n'
        'that is partly or entirely missing.',
        'Coordinates outside the canvas clip and produce a non-blocking warning; '
        'the rest of the program continues.')
    text = text.replace('in either of two built-in fonts.', 'in one of four built-in fonts.')
    return '## Canvases\n' + text


def file_tools(vision=True, surface='full'):
    specs = [
        ('write_file', 'Create or replace a UTF-8 source file.', {'path': 'string', 'content': 'string'}, ['path', 'content']),
        ('edit_file', 'Replace one exact, unique occurrence of old text with new text.', {'path': 'string', 'old': 'string', 'new': 'string'}, ['path', 'old', 'new']),
        ('read_file', 'Read a source file.', {'path': 'string'}, ['path']),
        ('list_files', 'List source files.', {}, []),
        ('run', 'Execute a Python file in a fresh process. submit=false previews; submit=true ends the episode only if the whole program succeeds and calls finish with valid outputs.', {'path': 'string', 'submit': 'boolean'}, ['path']),
    ]
    tools = [{'type': 'function', 'function': {'name': name, 'description': desc,
             'parameters': {'type': 'object', 'properties': {k: {'type': v} for k,v in props.items()},
                            'required': required, 'additionalProperties': False}}}
            for name, desc, props, required in specs]
    return tools


def file_prompt(vision=True, surface='full'):
    workflow = '''You are using Astra Pixel Art 0.6.0. Read the supplied API reference before drawing. It is the Skill's full API documentation; the execution and submission adaptations for this environment are below.

Workflow:
1. Read the API. All documented drawing objects are preloaded in the main Python file; helper modules can import them from pixelbench_api.
2. Draw in source steps. Use write_file(path, content), edit_file(path, old, new), read_file(path), and list_files(). run(path="main.py") executes your current program from the original task input in a fresh process. Source files persist; Python variables and canvas mutations are reconstructed by running the source. You can extend or edit that source between runs.
3. Look at the result. '''
    workflow += ('''Put view(canvas) in the program and run it to receive the PNG directly in your next observation. view returns a path as well; no separate image-opening tool is needed. Saved images alone are not observations.
''' if vision else '''No images are shown to you. Print c.stats_text() and c.matrix_text(region=...) for text observations. A view or save call does not give you visual feedback.
''')
    workflow += '''Edit the source and rerun as needed. save(name, canvas) exports native and 4x PNGs plus reloadable state; it does not submit.
4. Submit. In the program call finish(canvas) or finish([c1,c2,...]) to freeze the intended outputs in order. run(path="main.py", submit=True) ends the episode only when the whole program succeeds and declares its outputs with finish. In a preview run, finish declares outputs but leaves the episode open. Exceptions invalidate a submitting run. Only explicitly supplied canvases are submitted; independent working canvases are allowed. Use flatten explicitly when combining them into an output.

Environment:
- input_canvas is the task input (blank for creation). For an exact independently editable input copy use input_canvas.copy(name="output").
- reference and reference_frames are available only when supplied by the task. mask, when supplied, is a boolean NumPy array indexed mask[y,x].
- For Edit tasks the stated dimensions describe the input; output dimensions are agent-defined. Other tasks specify their required canvas size. Output count follows the task. All requested outputs must be constructed in one run; separate preview runs do not accumulate frames. Copies have independent pixels and share the palette.
- Coordinates outside a canvas clip and produce a non-blocking warning. There is no selected/default canvas, no run_code tool, and no CLI exec/undo session. Repair the source and rerun after an error.
- File tools in one response execute in order. On the last allowed source edit, save your changes and run with submit=True.

API reference (drawing and export semantics):
'''
    if surface == 'redraw':
        workflow += 'This surface requires redraw(canvas, rows) for all pixel changes; partial drawing methods in the reference below are disabled. rows must be the complete height-by-width matrix of colors.\n'
    return workflow + file_api_reference()


def file_submission_instructions(task, last_round=False):
    """Task-specific output contract shared by both model loops."""
    count = max(1, task.num_frames or 1)
    call = 'finish(result)' if count == 1 else 'finish([' + ', '.join(f'f{i}' for i in range(1, count + 1)) + '])'
    text = (
        f'This task requires exactly {count} output canvas(es) TOTAL, in the order described by the task. '
        f'The program must construct the outputs and end its drawing work with {call}. '
    )
    if count > 1:
        text += (
        'The input image is not automatically included: if the task specifies the original image as frame 1, '
        'include that frame explicitly in the submitted list, within this total. '
        'Create all frames in the same program execution; separate runs do not accumulate frames. '
        'Do not submit only the last frame or a contact sheet in place of the individual frames. '
        )
    text += (
        'When ready, call run(path="main.py", submit=True) '
        '(or use your actual program path). Viewing, saving, or a final text reply does not submit the work.'
    )
    if last_round:
        text = ('This is your LAST ROUND for editing source. You have at most ONE source edit left. After that you can still run the file; run calls do not consume the source edit budget. ' + text +
                ' Make your final source edit if needed, then run it with submit=True, even if the artwork is incomplete. '
                'Prioritize having a draft of every requested frame over polishing only one frame.')
    return text
