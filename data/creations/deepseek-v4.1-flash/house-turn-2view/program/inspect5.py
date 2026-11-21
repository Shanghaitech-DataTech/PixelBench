c = input_canvas
W, H = 112, 157
g = [[c.get(x, y) for x in range(W)] for y in range(H)]

# connected components per exact color index
from collections import deque
seen = [[False] * W for _ in range(H)]
comps = []
for y in range(H):
    for x in range(W):
        if seen[y][x]:
            continue
        col = g[y][x]
        if col == 0:
            seen[y][x] = True
            continue
        q = deque([(x, y)])
        seen[y][x] = True
        pix = []
        while q:
            cx, cy = q.popleft()
            pix.append((cx, cy))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < W and 0 <= ny < H and not seen[ny][nx] and g[ny][nx] == col:
                    seen[ny][nx] = True
                    q.append((nx, ny))
        xs = [p[0] for p in pix]
        ys = [p[1] for p in pix]
        comps.append((len(pix), col, min(xs), min(ys), max(xs), max(ys)))
comps.sort(reverse=True)
print('area color  bbox(x0,y0,x1,y1)')
for comp in comps[:45]:
    print('%5d  c%-3d  (%3d,%3d)-(%3d,%3d)  %dx%d' % (comp[0], comp[1], comp[2], comp[3], comp[4], comp[5], comp[4]-comp[2]+1, comp[5]-comp[3]+1))
