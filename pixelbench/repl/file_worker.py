"""One execution, one process. No persistent Python state or per-op snapshots."""
import json
import os
import traceback
import random
import sys
import types
from pathlib import Path


def main():
    directory = Path(sys.argv[1]).resolve()
    config = json.loads((directory / 'config.json').read_text())
    namespace = {'__name__': '__main__'}
    random.seed(0)
    exec(config['prelude'], namespace)
    drawing = namespace['_pb_skill']
    image_dir = directory / 'images'
    image_dir.mkdir()
    def view(canvas, **kwargs):
        def show():
            path = drawing.api['view'](canvas=canvas, **kwargs)
            target = image_dir / f'{len(list(image_dir.glob("*.png"))):04d}.png'
            target.write_bytes(Path(path).read_bytes())
            return str(target)
        return drawing.look('view', show)
    namespace['view'] = view
    for key in ('undo', 'undo_step', 'undo_round', 'finish_frame'):
        namespace.pop(key, None)
    module = types.ModuleType('pixelbench_api')
    module.__dict__.update({k: v for k, v in namespace.items() if not k.startswith('_')})
    sys.modules['pixelbench_api'] = module
    sys.path.append(config['source'])
    os.chdir(config['source'])
    # Confine the process before any agent code runs: own run directory only, no network, no exec.
    if config.get('sandbox', True):
        from pixelbench.repl import sandbox
        observer_dir = getattr(drawing.observer, 'out_dir', None) if drawing.observer else None
        sandbox.lock(directory, extra_write=[str(observer_dir)] if observer_dir else [])
    try:
        if config['path']:
            path = Path(config['source']) / config['path']
            namespace['__file__'] = str(path)
            sys.path.append(str(path.parent))
            exec(compile(path.read_text(), str(path), 'exec'), namespace)
    finally:
        # A serialization/observer failure must not obscure the original program exception.
        failed = sys.exc_info()[0] is not None
        try:
            drawing.checkpoint()
        except Exception:
            if not failed:
                raise
            traceback.print_exc()

        if drawing.observer:
            try:
                drawing.observer.source_code = path.read_text() if config['path'] else None
                drawing.observer.observe_workspace('program_run')
                drawing.observer.on_execute_done()
            except Exception:
                # Observation is auxiliary and cannot invalidate a program's outputs.
                traceback.print_exc()
            finally:
                drawing.observer.close()



if __name__ == '__main__':
    main()
