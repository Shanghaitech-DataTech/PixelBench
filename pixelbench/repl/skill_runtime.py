"""Astra's drawing API hosted in the existing persistent ipykernel.

All task types use this adapter. The engine is synchronized with the installed explicit-canvas skill; Session._api supplies drawing operations, never replay/step.
"""
from __future__ import annotations

import copy
import functools
from pathlib import Path

import numpy as np

from pixelbench._vendor.astra_pixelart.canvas import Canvas, Palette
from pixelbench._vendor.astra_pixelart.session import Session
from pixelbench._vendor.astra_pixelart.selection import Selection
from pixelbench.core.canvas import PixelCanvas
from pixelbench.core.color import Color, Palette as BenchPalette
from pixelbench.tasks.edit_protocol import validate_edit_size

DRAWING_METHODS = frozenset({
    'color', 'set', 'rect', 'line', 'circle', 'ellipse', 'poly', 'path',
    'text', 'fill_at', 'clear', 'blit', 'mirror', 'shift', 'outline',
    'dither', 'snapshot', 'restore', 'copy',
})


def uses_skill(task, surface='full'):
    kind = task.get('task_type') if isinstance(task, dict) else task.task_type
    return surface in ('full', 'redraw')


class TrackedCanvas(Canvas):
    """Observe engine calls without changing their rasterisation or return values."""

    def _clipped(self, x, y):
        # Print once per canvas per execution, including in tight pixel loops.
        # stderr is returned to the agent by both file and kernel sessions.
        if self.__dict__.get('_clipping_warned'):
            return
        self._clipping_warned = True
        import sys
        print(f"WARNING: canvas {self.name!r} ({self.w}x{self.h}): pixel ({x}, {y}) "
              "is outside the canvas and was clipped. Execution continues. "
              "Check the preview; if unintended, create a larger canvas and blit your work "
              "onto it with an appropriate offset. Further clipping warnings for this "
              "canvas are suppressed in this execution.", file=sys.stderr)

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        owner = super().__getattribute__('__dict__').get('_owner')
        if owner and name == 'select':
            return functools.partial(owner.recipe, attr)
        if owner and name in DRAWING_METHODS:
            if owner.task.get('surface') == 'redraw' and name not in ('color', 'copy'):
                raise ValueError('use redraw(canvas, rows) to replace the complete pixel matrix on this surface')
            return functools.partial(owner.call, name, attr)
        if owner and name in ('get', 'matrix_text'):
            return functools.partial(owner.look, name, attr)
        if owner and name in ('stats', 'stats_text', 'palette', 'color_name', 'to_rgba', 'to_indexed'):
            return functools.partial(owner.read, attr)
        return attr


class TrackedSelection(Selection):
    """Immutable recipes are reads; preview/paste participate in drawing undo."""

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        owner = super().__getattribute__('__dict__').get('_owner')
        if owner and name in ('resize', 'flip', 'rotate'):
            return functools.partial(owner.recipe, attr)
        if owner and name in ('preview', 'copy_to', 'move_to'):
            return functools.partial(owner.selection_call, name, attr)
        return attr


class SkillDrawing:
    """Explicit canvas workspace, undo, observations and submission checkpoints."""

    def __init__(self, initial, task, root, look_budget=None):
        import os
        self.file_mode = os.environ.get('PIXELBENCH_FILE_MODE') == '1'
        self.session = Session(root)
        self.api = self.session._api()
        self.task = task
        self.observer = None
        self.active = True
        self.depth = 0
        self.version = 0
        self.calls = []
        self.rounds = []
        self.known = []
        self.events = []
        self._seq = 0
        self.meta = {}
        self.look_budget = look_budget
        self.looks_used = int(os.environ.get('PIXELBENCH_LOOKS_USED', '0')) if self.file_mode else 0
        self.submission = None
        self.checkpoint_path = None
        # Import without quantising; preserve RGBA and every original name.
        src = PixelCanvas.from_dict(initial)
        self.input_size = (src.width, src.height)
        c = self.api['new_canvas'](src.width, src.height, name='input')
        remap = {}
        for color in src.palette:
            remap[color.id] = self.session.palette.register(color.rgba, color.name)
        c.px = [remap[int(v)] for v in src.matrix.flat]
        self.adopt(c)
        self.input = c
        self.meta[id(c)]['role'] = 'input'
        if initial.get('drawing_state'):
            state = initial['drawing_state']
            self.known = []
            self.meta = {}
            self.session.palette = Palette.from_dict(state['palette'])
            self.session.canvases = [self.adopt(Canvas.from_dict(row, self.session.palette))
                                     for row in state['canvases']]
            self.input = self.session.canvases[0]
            self.input_size = (self.input.w, self.input.h)

    def adopt(self, value):
        if isinstance(value, Selection):
            value.__class__ = TrackedSelection
            value._owner = self
        if isinstance(value, Canvas):
            if value.pal is not self.session.palette:
                mapping = [self.session.palette.register(rgba) for rgba in value.pal.colors]
                value.px[:] = [mapping[int(v)] for v in value.px]
                value.pal = self.session.palette
            value.__class__ = TrackedCanvas
            value._owner = self
            if not any(c is value for c in self.known):
                self.known.append(value)
                import hashlib
                self.meta[id(value)] = {'created': len(self.known), 'modified': 0, 'role': 'canvas',
                                        'rgba_hash': hashlib.sha256(bytes(Canvas.to_rgba(value)[2])).hexdigest()}
        return value

    def canvas_id(self, c):
        return f"canvas_{self.meta[id(c)]['created']:04d}"

    def __call__(self, ref):
        return self.api['canvas'](ref)

    def _check_edit_size(self, width, height):
        """Guard canvas dimensions (edit tasks only).

        There is no longer a cap relative to the input size: an edit output may
        be any size, so growing the canvas to make room for the edit is allowed.
        Only the technical crash guard in ``validate_edit_size`` remains.
        """
        if self.task.get('task_type') == 'edit':
            validate_edit_size(width, height)

    def new_canvas(self, w, h, background=None, name=None):
        self._check_edit_size(w, h)
        return self.call('new_canvas', self.api['new_canvas'], w, h, background, name)

    def load(self, path, name=None, add=True):
        # Read into an isolated palette first: rejected loads must not mutate
        # the current canvas, registered layers, or shared drawing palette.
        c = Session(self.session.root)._api()['load'](path, name=name, add=False)
        if add:
            self._check_edit_size(c.w, c.h)
        def load():
            return self.api['load'](path, name=name, add=add)
        return self.call('load', load)

    def flatten(self, layers, name=None, background=None):
        layers = list(layers)
        for ref in layers:
            c = ref if isinstance(ref, Canvas) else (
                self.session.canvases[ref] if isinstance(ref, int) else
                next(c for c in self.session.canvases if c.name == ref))
            self._check_edit_size(c.w, c.h)
        return self.call('flatten', self.api['flatten'], layers, name=name, background=background)

    def state(self):
        """Portable drawing state, independent of Python object identities."""
        return {
            'engine': 'astra-pixel-art-0.6.0',
            'palette': self.session.palette.to_dict(),
            'canvases': [c.to_dict() for c in self.known if self.meta[id(c)].get('role') != 'undone'],
            'canvas_ids': [self.canvas_id(c) for c in self.known if self.meta[id(c)].get('role') != 'undone'],
            'registered_ids': [self.canvas_id(c) for c in self.session.canvases],
        }

    def to_pixel_canvas(self, c):
        pal = BenchPalette()
        # One canonical name per id; all aliases survive in drawing_state.
        for i, rgba in enumerate(c.pal.colors):
            label = c.pal.label(i)
            while label in pal.names():
                label += f'_{i}'
            pal._add(Color(i, label, tuple(rgba)))
        out = PixelCanvas(c.w, c.h, palette=pal)
        out.matrix = np.asarray(c.px, dtype=np.int32).reshape(c.h, c.w).copy()
        out._alpha_visibility = True
        out._version = self.version
        out._edit_log = list(self.events)
        return out

    def to_dict(self, c):
        out = self.to_pixel_canvas(c).to_dict()
        if not self.file_mode:
            out['drawing_state'] = self.state()
        return out

    def _snapshot(self):
        self._seq += 1
        return {
            'seq': self._seq,
            'palette': copy.deepcopy(self.session.palette.to_dict()),
            'layers': list(self.session.canvases),
            'meta': copy.deepcopy(self.meta),
            'canvases': [(c, list(c.px), c.name, copy.deepcopy(c._snapshots)) for c in self.known],
            'events': len(self.events),
        }

    def _restore(self, mark):
        restored = Palette.from_dict(mark['palette'])
        self.session.palette.__dict__.update(restored.__dict__)
        self.session.canvases[:] = mark['layers']
        for key, value in mark['meta'].items():
            self.meta[key] = copy.deepcopy(value)
        kept = []
        for c, pixels, name, snapshots in mark['canvases']:
            c.px[:] = pixels
            c.name = name
            c._snapshots = copy.deepcopy(snapshots)
            c.pal = self.session.palette
            kept.append(c)
        # A Python variable may still reference a layer created after the mark.
        # Keep it valid but empty, with the restored palette, after undo.
        for c in self.known:
            if not any(c is old for old in kept):
                c.px[:] = [0] * (c.w * c.h)
                c.pal = self.session.palette
                c._snapshots.clear()
                self.meta[id(c)].update(role="undone", modified=0)
        del self.events[mark['events']:]
        self.version += 1

    def mark_round(self):
        if self.active:
            self.rounds.append(self._snapshot())
            self.rounds[:] = self.rounds[-200:]

    def mark_call(self):
        # Calls are tracked here, not by the legacy SessionTools wrapper.
        pass

    def call(self, op, fn, *args, **kwargs):
        if self.depth:
            return fn(*args, **kwargs)
        if self.file_mode:
            self.depth += 1
            try:
                result = fn(*args, **kwargs)
                if isinstance(result, (Canvas, Selection)) and getattr(result, '_owner', None) is not self:
                    self.adopt(result)
                if op == 'flatten':
                    for ref in args[0]:
                        source = self.api['canvas'](ref)
                        if id(source) in self.meta:
                            self.meta[id(source)]['consumed'] = True
                if op == 'selection_preview' and isinstance(result, Canvas):
                    self.meta[id(result)]['role'] = 'preview'
                self.version += 1
                target = getattr(fn, '__self__', None)
                if isinstance(target, Canvas) and id(target) in self.meta:
                    self.meta[id(target)]['modified'] = self.version
                return result
            finally:
                self.depth -= 1
        before = {id(c): (c, self.to_pixel_canvas(c)) for c in self.known}
        if self.active:
            self.calls.append(self._snapshot())
            self.calls[:] = self.calls[-200:]
        self.depth += 1
        result = None
        try:
            result = self.adopt(fn(*args, **kwargs))
            if op == 'flatten':
                for ref in args[0]:
                    source = self.api['canvas'](ref)
                    if id(source) in self.meta:
                        self.meta[id(source)]['consumed'] = True
            if op == 'selection_preview' and isinstance(result, Canvas):
                self.meta[id(result)]['role'] = 'preview'
            return result
        finally:
            self.depth -= 1
            self.version += 1
            touched = []
            for c in self.known:
                after = self.to_pixel_canvas(c)
                old = before.get(id(c))
                previous = old[1] if old else PixelCanvas(c.w, c.h)
                old_rgba = np.asarray([color.rgba for color in previous.palette], dtype=np.uint8)[previous.matrix]
                new_rgba = np.asarray([color.rgba for color in after.palette], dtype=np.uint8)[after.matrix]
                changed = int(np.any(old_rgba != new_rgba, axis=2).sum())
                if changed or (old is None and c is result):
                    self.meta[id(c)]['modified'] = self.version
                    if self.meta[id(c)].get('role') == 'undone':
                        self.meta[id(c)]['role'] = 'canvas'
                    touched.append(self.canvas_id(c))
                    if self.observer and self.active:
                        self.observer.observe_canvas(op, c, previous, after, changed)
            self.events.append({'op': op, 'args': {}, 'canvas_ids': touched, 'version': self.version})
            if self.observer and self.active and not touched:
                self.observer.observe_workspace(op)

    def undo_step(self):
        if not self.calls:
            return {'op': 'undo_step', 'restored': 0}
        mark = self.calls.pop()
        self._restore(mark)
        self.rounds[:] = [m for m in self.rounds if m['seq'] <= mark['seq']]
        self._record_undo('undo_step')
        return {'op': 'undo_step', 'restored': 1}

    def undo_round(self):
        if len(self.rounds) < 2:
            return {'op': 'undo_round', 'restored': 0}
        mark = self.rounds[-2]
        self.rounds.pop()
        self._restore(mark)
        self.calls[:] = [m for m in self.calls if m['seq'] < mark['seq']]
        self._record_undo('undo_round')
        return {'op': 'undo_round', 'restored': 1}

    def _record_undo(self, op):
        self.events.append({'op': op, 'args': {}, 'changed': 0, 'version': self.version})
        if self.observer and self.active:
            self.observer.observe_workspace(op)

    def undo(self, n=1):
        for _ in range(n):
            self.undo_step()
        return {'op': 'undo', 'steps': n}

    def look(self, name, fn, *args, **kwargs):
        if self.look_budget is not None and self.looks_used >= int(self.look_budget):
            return '[observation disabled] Observation budget exhausted; finish(canvas) when ready.'
        self.looks_used += 1
        return fn(*args, **kwargs)

    def selection_call(self, name, fn, *args, **kwargs):
        if name in ('copy_to', 'move_to'):
            target = kwargs.get('canvas', args[2] if len(args) > 2 else None)
            if isinstance(target, Canvas):
                self.adopt(target)
        return self.call('selection_' + name, fn, *args, **kwargs)

    def recipe(self, fn, *args, **kwargs):
        return self.adopt(fn(*args, **kwargs))

    def read(self, fn, *args, **kwargs):
        return fn(*args, **kwargs)

    def view(self, canvas, **kwargs):
        from IPython.display import Image, display
        def show():
            target = self.api['canvas'](canvas)
            path = self.api['view'](canvas=target, **kwargs)
            display(Image(filename=path))
            return path
        return self.look('view', show)

    def save(self, name, canvas, **kwargs):
        c = self.api['canvas'](canvas)
        result = self.api['save'](name, c, **kwargs)
        if id(c) in self.meta:
            self.meta[id(c)]['saved'] = self.version + 1
        return result

    def redraw(self, canvas, rows):
        def apply():
            if len(rows) != canvas.h or any(len(row) != canvas.w for row in rows):
                raise ValueError('redraw requires exactly canvas.h rows of canvas.w colors')
            pixels = [canvas.pal.index_of(v) for row in rows for v in row]
            canvas.px[:] = pixels
            return canvas
        return self.call('redraw', apply)

    def bindings(self):
        return dict(new_canvas=self.new_canvas, canvas=self.__call__, canvases=self.api['canvases'],
                    flatten=self.flatten, load=self.load, save=self.save, export=self.api['export'],
                    view=self.view, Canvas=lambda *a, **kw: self.adopt(Canvas(*a, **kw)),
                    input_canvas=self.input, undo=self.undo, undo_step=self.undo_step,
                    undo_round=self.undo_round, redraw=self.redraw)

    def checkpoint(self):
        if not self.checkpoint_path or self.submission is None:
            return
        import json, os
        path = Path(self.checkpoint_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = self.submission.extract()
        payload['workspace'] = self.state()
        payload['looks_used'] = self.looks_used
        temporary = path.with_suffix('.tmp')
        temporary.write_text(json.dumps(payload), encoding='utf-8')
        os.replace(temporary, path)


def install(namespace, task, initial, mask_state, observer_dir, look_budget,
            reference_state=None, frames_state=None):
    import os, tempfile
    from pixelbench.repl.submission import Submission
    root = Path(observer_dir).parent / 'pixelart' if observer_dir else Path(tempfile.mkdtemp(prefix='pixelbench-skill-'))
    if os.environ.get('PIXELBENCH_FILE_MODE') == '1':
        root = Path(os.environ['PIXELBENCH_RUN_ROOT'])
    drawing = SkillDrawing(initial, task, root, look_budget)
    namespace.update(drawing.bindings())
    namespace.update(_pb_skill=drawing, np=np, reference=None, reference_frames=None,
                     mask=np.array(mask_state['mask'], dtype=bool) if mask_state else None)
    def import_reference(row):
        src = PixelCanvas.from_dict(row)
        c = Canvas(src.width, src.height, palette=drawing.session.palette, name='reference')
        mapping = {color.id: c.pal.register(color.rgba, color.name) for color in src.palette}
        c.px = [mapping[int(v)] for v in src.matrix.flat]
        drawing.adopt(c)
        drawing.meta[id(c)]['role'] = 'reference'
        return c
    if reference_state is not None:
        namespace['reference'] = import_reference(reference_state)
    if task.get('frames_visible') and frames_state:
        namespace['reference_frames'] = [import_reference(row) for row in frames_state]
    submission = Submission(drawing, namespace)
    drawing.submission = submission
    namespace['finish'] = submission.finish
    namespace['_pb_submission'] = submission
    def retired_finish_frame(*args, **kwargs):
        raise RuntimeError('finish_frame was removed; keep editable Canvas objects and finish([f1, f2, ...]) together')
    namespace['finish_frame'] = retired_finish_frame
    if observer_dir:
        from pixelbench.repl.observer import WorkspaceObserver
        drawing.observer = WorkspaceObserver(observer_dir, drawing)
        if drawing.file_mode:
            index = int(os.environ.get('PIXELBENCH_RUN_INDEX', '0'))
            drawing.observer.turn_index = index
            drawing.observer.call_index = index
            drawing.observer._turn_start_call = index
    namespace['_pb_obs'] = drawing.observer
    def set_active(value):
        drawing.active = bool(value)
        if drawing.observer:
            drawing.observer.set_active(value)
    namespace['_pb_obs_set_active'] = set_active
    drawing.checkpoint_path = os.environ.get('PIXELBENCH_CHECKPOINT')
    def post_execute():
        if drawing.active:
            drawing.checkpoint()
            if drawing.observer:
                drawing.observer.on_execute_done()
    from IPython import get_ipython
    shell = get_ipython()
    if shell is not None and not drawing.file_mode:
        shell.events.register('pre_execute', drawing.mark_round)
        shell.events.register('post_execute', post_execute)
    drawing.checkpoint()
    print('Explicit canvas workspace ready. Use view(canvas) and finish(canvas or ordered_list).')
