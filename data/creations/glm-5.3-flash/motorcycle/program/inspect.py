import math
import numpy as np

src = open('main.py').read()
parts = src.split('# ============')
c = new_canvas(128, 128, background=None, name="dbg")
ns = {'math': math, 'new_canvas': new_canvas, 'c': c}
snaps = []
for i, ch in enumerate(parts):
    body = ch.strip().split('\n', 1)
    body = body[1] if len(body) > 1 else ''
    exec('import math\n' + body, ns)
    w, h, idx, pal = c.to_indexed()
    snaps.append(idx.copy())

w, h, idx, pal = c.to_indexed()
idx = np.frombuffer(bytes(idx), dtype=np.uint8).reshape(h, w).copy()
snaps = [np.frombuffer(bytes(s), dtype=np.uint8).reshape(h, w).copy() for s in snaps]
    tgt = idx[y, x]
    if tgt == 0:
        return f'({x},{y}) transparent'
    for i in range(len(snaps) - 1, -1, -1):
        if snaps[i][y, x] == tgt:
            head = parts[i].strip().splitlines()[0][:60] if parts[i].strip() else '(init)'
            return f'({x},{y}) idx={tgt} {pal[tgt]["name"]} <- part {i}: {head}'
    return f'({x},{y}) idx={tgt} {pal[tgt]["name"]} unknown'

for pt in [(100,64),(100,63),(102,65),(96,64),(110,64),(90,65),(85,65),(80,65),(82,64),(86,64),(91,64),(78,66),(105,66)]:
    print(who(*pt))
