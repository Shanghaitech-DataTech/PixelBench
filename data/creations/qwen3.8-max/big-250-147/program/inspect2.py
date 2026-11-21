from pixelbench_api import *
from collections import Counter, defaultdict

W, H = 250, 147
cnt = Counter()
bbox = defaultdict(lambda: [999, 999, -1, -1])
grid = {}
for y in range(H):
    for x in range(W):
        i = input_canvas.get(x, y)
        cnt[i] += 1
        b = bbox[i]
        b[0] = min(b[0], x); b[1] = min(b[1], y)
        b[2] = max(b[2], x); b[3] = max(b[3], y)
        grid[(x, y)] = i

pal = {p['index']: tuple(p['rgba']) for p in input_canvas.palette()}
for i, c in cnt.most_common(60):
    r, g, b_, a = pal[i]
    x0, y0, x1, y1 = bbox[i]
    print(f"idx={i:3d} rgba=({r:3d},{g:3d},{b_:3d}) n={c:5d} bbox=({x0:3d},{y0:3d})-({x1:3d},{y1:3d})")

# vertical profile at a few columns: print color index runs
for x in [10, 60, 117, 175, 230]:
    runs = []
    prev = None
    for y in range(H):
        i = grid[(x, y)]
        if i != prev:
            runs.append((y, i))
            prev = i
    print("col", x, runs[:40])
