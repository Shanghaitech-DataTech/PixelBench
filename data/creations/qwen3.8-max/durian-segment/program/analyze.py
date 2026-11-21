from pixelbench_api import *
from collections import deque

w, h = input_canvas.stats()['size']
FLESH = {7, 8}

grid = {}
for y in range(h):
    for x in range(w):
        grid[(x, y)] = input_canvas.get(x, y)

seen = set()
comps = []
for y in range(h):
    for x in range(w):
        p = (x, y)
        if p in seen or grid[p] not in FLESH:
            continue
        comp = [p]
        seen.add(p)
        q = deque([p])
        while q:
            cx, cy = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                np_ = (cx + dx, cy + dy)
                if np_ in seen:
                    continue
                v = grid.get(np_, 1)
                if v in FLESH:
                    seen.add(np_)
                    comp.append(np_)
                    q.append(np_)
        comps.append(comp)

comps.sort(key=len, reverse=True)
for i, c in enumerate(comps[:8]):
    xs = [p[0] for p in c]
    ys = [p[1] for p in c]
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)
    print(f'comp {i}: size={len(c)} bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)}) centroid=({cx:.1f},{cy:.1f})')

# visualise the three biggest components
letters = 'abcde'
vis = [['.'] * w for _ in range(h)]
for i, c in enumerate(comps[:5]):
    for (x, y) in c:
        vis[y][x] = letters[i]
for y in range(h):
    print(f'{y:2d} ' + ''.join(vis[y]))
