"""Explicit submissions and deterministic, reference-free recovery of unfinished work."""
from __future__ import annotations

import copy
import hashlib
import json
import re

from pixelbench._vendor.astra_pixelart.canvas import Canvas
from pixelbench.tasks.edit_protocol import validate_edit_size


class Submission:
    def __init__(self, drawing, namespace):
        self.drawing = drawing
        self.namespace = namespace
        self.accepted = None
        self.attempt = []

    @property
    def expected(self):
        return max(1, int(self.drawing.task.get('num_frames') or 1))

    def validate(self, c):
        if not isinstance(c, Canvas):
            raise TypeError('finish expects a Canvas or a nonempty list of Canvas objects')
        owner = getattr(c, '_owner', None)
        if owner is not self.drawing:
            raise ValueError('submit a canvas created or loaded in this drawing session')
        task = self.drawing.task
        if task.get('task_type') == 'edit':
            validate_edit_size(c.w, c.h)
        elif (c.w, c.h) != (task['width'], task['height']):
            raise ValueError(f'output must be {task["width"]}x{task["height"]}, got {c.w}x{c.h}')
        if len(c.px) != c.w * c.h or any(type(i) is not int or not 0 <= i < len(c.pal.colors) for i in c.px):
            raise ValueError('canvas has invalid pixel indices or dimensions')
        if task.get('task_type') != 'edit':
            limit = int((task.get('constraints') or {}).get('max_colors') or 0)
            colors = {c.pal.rgba(i) for i in c.px if c.pal.rgba(i)[3] > 0}
            if limit and len(colors) > limit:
                raise ValueError(f'canvas uses {len(colors)} visible colors; limit is {limit}')

    def validate_sequence(self, items):
        """Only canvas geometry is structural; content extent is unrestricted."""
        if len(items) < 2:
            return
        shapes = [(c.w, c.h) for c in items]
        if len(set(shapes)) > 1:
            raise ValueError('every frame of one sequence must use the same canvas size; '
                             'choose any suitable size, independent of the input size')

    def finish(self, value):
        if self.accepted is not None:
            raise RuntimeError('a submission has already been accepted')
        items = value if isinstance(value, list) else [value]
        if not items or any(not isinstance(c, Canvas) for c in items):
            raise TypeError('finish expects a Canvas or a nonempty flat list of Canvas objects')
        self.attempt = [c for c in items if getattr(c, '_owner', None) is self.drawing]
        for c in items:
            self.validate(c)
        self.validate_sequence(items)
        # Atomic acceptance: conversion and validation precede publishing the result.
        payload = self.pack(items, 'explicit', 'finish', [])
        self.accepted = copy.deepcopy(payload)
        self.drawing.checkpoint()
        from pixelbench.repl.kernel import FINISH_SENTINEL
        print(f'Declared {len(items)} output canvas(es).' if self.drawing.file_mode else FINISH_SENTINEL)
        return f'declared {len(items)} canvas(es)'

    def pack(self, items, source, reason, candidates):
        outputs, manifest = [], []
        for c in items:
            out = self.drawing.to_dict(c)
            outputs.append(out)
            manifest.append({'canvas_id': self.drawing.canvas_id(c), 'name': c.name,
                             'size': [c.w, c.h],
                             'rgba_sha256': hashlib.sha256(bytes(c.to_rgba()[2])).hexdigest()})
        return {'outputs': outputs, 'submission': {'source': source, 'reason': reason,
                'expected_count': self.expected, 'actual_count': len(items),
                'count_match': len(items) == self.expected, 'items': manifest,
                'candidates': candidates,
                'modified_content': any(self.drawing.meta[id(c)].get('modified', 0) > 0
                                        for c in items)}}

    def extract(self):
        if self.accepted is not None:
            return copy.deepcopy(self.accepted)
        d = self.drawing
        # Raw pixel-list changes are legal Python too; observe them at each checkpoint.
        for c in d.known:
            try:
                fingerprint = hashlib.sha256(bytes(c.to_rgba()[2])).hexdigest()
            except (TypeError, ValueError, IndexError):
                continue
            meta = d.meta[id(c)]
            if meta.get('rgba_hash') != fingerprint:
                if not meta.get('modified'):
                    d.version += 1
                    meta['modified'] = d.version
                meta['rgba_hash'] = fingerprint
        # Inspect only plain user containers. Never eval expressions or traverse arbitrary objects.
        aliases, groups = {}, []
        def visit(value, path, depth=0):
            if isinstance(value, Canvas) and getattr(value, '_owner', None) is d:
                aliases.setdefault(id(value), []).append(path)
            elif type(value) in (list, tuple) and depth < 2:
                if value and all(isinstance(c, Canvas) and getattr(c, '_owner', None) is d for c in value):
                    groups.append((path, list(value)))
                for i, v in enumerate(value[:256]):
                    visit(v, f'{path}[{i}]', depth + 1)
            elif type(value) is dict and depth < 2:
                for k, v in list(value.items())[:256]:
                    visit(v, f'{path}[{str(k)[:64]}]', depth + 1)
        for name, value in list(self.namespace.items()):
            if not name.startswith('_') and name not in ('In', 'Out', 'reference', 'reference_frames'):
                visit(value, name)
        rows, usable = [], []
        for c in list(d.known):
            meta = d.meta[id(c)]
            if meta.get('role') in ('reference', 'undone'):
                continue
            errors = []
            try:
                self.validate(c)
            except (ValueError, TypeError, IndexError) as e:
                errors.append(str(e))
            # Even invalid-size/color outputs are kept as progress, with validity recorded.
            try:
                visible = sum(c.pal.rgba(i)[3] > 0 for i in c.px)
                d.to_pixel_canvas(c)
            except (ValueError, TypeError, IndexError):
                continue
            names = aliases.get(id(c), []) + [c.name or '']
            final_name = any(re.search(r'(^|[_.\[])\b(final|result|output|frames|animation)\b', n.lower()) for n in names)
            scratch = any(re.search(r'(^|[_.])(?:scratch|temp|preview|draft)(?:\b|_)', n.lower()) for n in names)
            score = (not errors, meta.get('role') != 'input' or meta.get('modified', 0) > 0,
                     not scratch and meta.get('role') != 'preview', bool(final_name),
                     bool(meta.get('saved')), not meta.get('consumed', False), bool(visible),
                     meta.get('modified', 0), meta.get('created', 0))
            row = {'canvas_id': d.canvas_id(c), 'name': c.name, 'aliases': aliases.get(id(c), []),
                   'score': list(score), 'validation_errors': errors, 'visible_pixels': visible}
            rows.append(row)
            usable.append((c, score))
        by_id = {id(c): score for c, score in usable}
        choices = []
        if self.attempt:
            groups.append(('last_finish_attempt', self.attempt))
        for name, items in groups:
            if not all(id(c) in by_id for c in items):
                continue
            # Explicit lists preserve order, including repeated references (valid hold frames).
            hint = name == 'last_finish_attempt' or bool(re.search(r'final|result|output|frames|animation', name.lower()))
            quality = min(by_id[id(c)][:3] for c in items)
            choices.append(((quality, len(items) == self.expected, hint, -abs(len(items)-self.expected),
                             max(by_id[id(c)][-2] for c in items), name), name, items))
        if self.attempt and all(id(c) in by_id for c in self.attempt):
            return self.pack(self.attempt, 'recovered', 'last_finish_attempt', rows)
        if choices and self.expected > 1:
            _, name, items = max(choices, key=lambda x: x[0])
            # Preserve a recognized list rather than silently padding or truncating it.
            return self.pack(items, 'recovered', f'ordered candidate list: {name}', rows)
        ranked = sorted(usable, key=lambda x: x[1], reverse=True)
        # Prefer output candidates; only use the untouched input if there is nothing else.
        preferred = [(c,s) for c,s in ranked if s[1] and s[2]]
        if preferred:
            ranked = preferred
        selected = [c for c, _ in ranked[:self.expected]]
        if self.expected > 1:
            # Numbered frame names take precedence; otherwise creation order is reproducible.
            def order(c):
                names = aliases.get(id(c), []) + [c.name or '']
                nums = [int(m.group(1)) for n in names if (m := re.search(r'(?:frame|f|image|img)[_ -]?(\d+)$', n, re.I))]
                return (0, min(nums)) if nums else (1, d.meta[id(c)]['created'])
            selected.sort(key=order)
        return self.pack(selected, 'recovered' if selected else 'missing',
                         'ranked workspace candidates; frame number then creation order', rows)
