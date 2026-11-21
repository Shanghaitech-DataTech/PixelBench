"""Versioned source workspaces and fresh-process drawing executions."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile

from pixelbench.core.canvas import PixelCanvas
from pixelbench.repl.kernel import KernelResult


class FileSession:
    def __init__(self, root=None, sandbox=True, **kwargs):
        # Every program runs in the sandbox (repl/sandbox.py) unless the caller explicitly opts out.
        self.sandbox = bool(sandbox)
        if root is not None:
            Path(root).mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix='program-', dir=root)).resolve()
        self.source = self.root / 'source'
        self.source.mkdir(parents=True, exist_ok=True)
        self.checkpoint_path = self.root / 'workspace.json'
        self.latest_checkpoint_path = self.root / 'latest-workspace.json'
        self.prelude = ''
        self.runs = []
        self.best = None
        self.accepted = None
        self.looks_used = 0

    def start(self, **kwargs):
        return self

    def shutdown(self):
        pass  # Artifacts intentionally survive for audit/reproduction.

    def is_alive(self):
        return True

    def path(self, name):
        path = (self.source / name).resolve()
        if not path.is_relative_to(self.source) or path == self.source:
            raise ValueError('file path must be inside the source workspace')
        return path

    def write_file(self, path, content):
        target = self.path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        return f'Wrote {path}'

    def edit_file(self, path, old, new):
        target = self.path(path)
        content = target.read_text()
        if not old or content.count(old) != 1:
            raise ValueError('old text must match exactly once')
        target.write_text(content.replace(old, new, 1))
        return f'Edited {path}'

    def read_file(self, path):
        return self.path(path).read_text()

    def list_files(self):
        return '\n'.join(str(p.relative_to(self.source)) for p in sorted(self.source.rglob('*')) if p.is_file())

    def execute_checked(self, code, timeout=60, what='code'):
        if what != 'prelude':
            raise ValueError('FileSession executes files via run(path, submit=False)')
        self.prelude = code
        result = self._run(None, False, timeout)
        if not result.ok:
            raise RuntimeError(result.combined())
        return result

    def dispatch(self, name, args, timeout):
        try:
            if name == 'run':
                return self.run(args.get('path', 'main.py'), args.get('submit', False), timeout)
            if name not in ('write_file', 'read_file', 'edit_file', 'list_files'):
                raise ValueError('Use file tools and run(path, submit=True) to submit')
            return KernelResult(stdout=str(getattr(self, name)(**args)), submitted=False)
        except Exception as exc:
            return KernelResult(ok=False, stderr=f'{type(exc).__name__}: {exc}', submitted=False)

    def run(self, path='main.py', submit=False, timeout=60):
        target = self.path(path)
        target.read_text()  # validate before snapshot
        return self._run(str(target.relative_to(self.source)), submit, timeout)

    def _run(self, path, submit, timeout):
        run_id = f'run_{len(self.runs):04d}'
        directory = self.root / 'runs' / run_id
        sources = directory / 'source'
        shutil.copytree(self.source, sources, ignore=shutil.ignore_patterns('__pycache__'))
        hashes = {str(p.relative_to(sources)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(sources.rglob('*')) if p.is_file()}
        working = directory / 'work'
        shutil.copytree(sources, working)
        config = {'prelude': self.prelude, 'path': path, 'source': str(working), 'sandbox': self.sandbox}
        (directory / 'config.json').write_text(json.dumps(config))
        # Minimal environment: no API keys, proxies or user paths leak into agent code.
        (directory / 'tmp').mkdir(parents=True, exist_ok=True)
        base_env = {k: os.environ[k] for k in ('PATH', 'LANG', 'LC_ALL', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS',
                                               'MKL_NUM_THREADS', 'PYTHONUSERBASE') if k in os.environ}
        env = dict(base_env, HOME=str(directory), TMPDIR=str(directory / 'tmp'), PIXELBENCH_FILE_MODE='1',
                   PIXELBENCH_CHECKPOINT=str(directory / 'workspace.json'),
                   PIXELBENCH_RUN_ROOT=str(directory / 'artifacts'),
                   PIXELBENCH_RUN_INDEX=str(len(self.runs)),
                   PIXELBENCH_LOOKS_USED=str(self.looks_used))
        package = str(Path(__file__).resolve().parents[2])
        env['PYTHONPATH'] = package
        env['PYTHONSAFEPATH'] = '1'
        proc = subprocess.Popen([sys.executable, '-m', 'pixelbench.repl.file_worker', str(directory)],
                                cwd=directory, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                start_new_session=True)
        timed_out = False
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = proc.communicate()
        except BaseException:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            proc.communicate()
            raise
        ok = proc.returncode == 0 and not timed_out
        payload = None
        checkpoint = directory / 'workspace.json'
        if checkpoint.exists():
            payload = json.loads(checkpoint.read_text())
            self.looks_used = max(self.looks_used, payload.get('looks_used', 0))
        declared = bool(payload and payload['submission']['source'] == 'explicit')
        accepted = bool(path and submit and ok and declared)
        record = {'run_id': run_id, 'source_hashes': hashes, 'path': path,
                  'ok': ok and (not submit or declared), 'execution_ok': ok,
                  'submission_valid': declared, 'submit_requested': submit, 'accepted': accepted, 'timed_out': timed_out}
        self.runs.append(record)
        (directory / 'result.json').write_text(json.dumps(record, indent=2))
        (directory / 'stdout.txt').write_bytes(stdout)
        (directory / 'stderr.txt').write_bytes(stderr + (b'\nSubmission rejected: program must call finish(canvas_or_list).'
                                                        if submit and ok and not declared else b''))
        if payload:
            payload['submission']['output_attempt'] = payload['submission'].get('reason') == 'last_finish_attempt'
            payload['submission'].update(record, protocol='file-v1')
            if accepted:
                self.accepted = payload
            else:
                reason = ('successful_preview' if declared else 'run_boundary_recovery') if ok else 'incomplete_run'
                payload['submission'].update(source='recovered', reason=reason)
                if path:
                    # Explicit output intent outranks guesses; inspection never replaces drawing progress.
                    rank = (4 if declared and ok else 3 if declared or payload['submission'].get('output_attempt')
                            else 2 if payload['submission'].get('modified_content') else 1)
                    payload['submission']['recovery_rank'] = rank
                    if self.best is None or rank >= self.best['submission'].get('recovery_rank', 0):
                        self.best = payload
            temporary = self.latest_checkpoint_path.with_suffix('.tmp')
            temporary.write_text(json.dumps(payload))
            temporary.replace(self.latest_checkpoint_path)
            chosen = self.accepted or self.best or payload
            checkpoint.write_text(json.dumps(payload))
            temporary = self.checkpoint_path.with_suffix('.tmp')
            temporary.write_text(json.dumps(chosen))
            temporary.replace(self.checkpoint_path)
        if submit and ok and not declared:
            ok = False
            stderr += b'\nSubmission rejected: program must call finish(canvas_or_list).'
        images = [p.read_bytes() for p in sorted((directory / 'images').glob('*.png'))]
        return KernelResult(ok=ok, stdout=stdout.decode(errors='replace'), stderr=stderr.decode(errors='replace'),
                            images=images, timed_out=timed_out, submitted=accepted)

    def extract_submission(self):
        payload = self.accepted or self.best
        if not payload:
            return [], {'source': 'missing', 'protocol': 'file-v1'}
        meta = dict(payload['submission'])
        hashes = {str(p.relative_to(self.source)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in self.source.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        meta['source_matches_workspace'] = hashes == meta.get('source_hashes')
        meta['artifacts_dir'] = str(self.root)
        return [PixelCanvas.from_dict(c) for c in payload['outputs']], meta

    def extract_final_canvas(self):
        outputs, _ = self.extract_submission()
        return outputs[-1] if outputs else None

    def extract_final_frames(self):
        return self.extract_submission()[0]
