from collections import deque

out = input_canvas.copy(name="output")

FLESH = {6, 7, 8}          # cream #fbf4c9, gold #ffc830, yellow #ffda45
CREASE = {4}               # #e08c37 crease line
BLACK, CLEAR = 2, 1

RIND_LIT = out.color("#ef9d0e", "rind_lit")      # lit rim of the rind wall
RIND_MID = out.color("#e08c37", "rind_mid")      # rind body
RIND_DARK = out.color("#be6f48", "rind_dark")    # cavity floor
RIND_DEEP = out.color("#a65537", "rind_deep")    # shadow under the overhang
RIND_PIT = out.color("#7a3c28", "rind_pit")      # deepest crease at the back

# x of the crease separating the bottom lobe from the middle lobe, per row
cutx = {33: 20, 34: 20, 35: 24, 36: 24, 37: 25, 38: 25, 39: 25, 40: 25,
        41: 25, 42: 27, 43: 27, 44: 29, 45: 28, 46: 29, 47: 32, 48: 32,
        49: 33, 50: 34, 51: 34, 52: 35, 53: 35}

region = set()
for y, cx in cutx.items():
    for x in range(cx):
        if out.get(x, y) in FLESH:
            region.add((x, y))

N8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def bfs(seeds):
    dist = {p: 1 for p in seeds}
    q = deque(seeds)
    while q:
        x, y = q.popleft()
        for dx, dy in N8:
            p = (x + dx, y + dy)
            if p in region and p not in dist:
                dist[p] = dist[(x, y)] + 1
                q.append(p)
    return dist


# classify the region border: silhouette side vs. the cut edge where the
# remaining flesh overhangs the hollow
outer_seeds, cut_seeds = [], []
for (x, y) in region:
    touch_out = touch_cut = False
    for dx, dy in N8:
        nx, ny = x + dx, y + dy
        if (nx, ny) in region:
            continue
        if not (0 <= nx < 64 and 0 <= ny < 64):
            touch_out = True
            continue
        i = out.get(nx, ny)
        if i in (BLACK, CLEAR):
            touch_out = True
        elif i in FLESH or i in CREASE:
            touch_cut = True
    if touch_out:
        outer_seeds.append((x, y))
    if touch_cut:
        cut_seeds.append((x, y))

d_out = bfs(outer_seeds)
d_cut = bfs(cut_seeds)

for (x, y) in region:
    do = d_out.get((x, y), 99)
    dc = d_cut.get((x, y), 99)
    if dc <= 1:
        col = RIND_PIT            # hard shadow line right under the overhang
    elif do == 1:
        col = RIND_LIT            # top edge of the rind wall catches the light
    elif do == 2:
        col = RIND_MID
    elif dc == 2:
        col = RIND_DEEP
    elif dc == 3 or do >= 6:
        col = RIND_DARK
    else:
        col = RIND_DARK if (x + y) % 7 else RIND_DEEP
    out.set(x, y, col)

# broken fibrous streaks on the cavity floor, along the segment's long axis
for k, (x0, y0, x1, y1) in enumerate([(9, 47, 19, 40), (14, 52, 25, 42),
                                      (11, 51, 22, 41)]):
    dx, dy = x1 - x0, y1 - y0
    n = max(abs(dx), abs(dy))
    for s in range(n + 1):
        x = x0 + round(dx * s / n)
        y = y0 + round(dy * s / n)
        if (s + k) % 4 == 0:
            continue
        if (x, y) in region and out.get(x, y) in (RIND_DARK, RIND_DEEP):
            out.set(x, y, RIND_DEEP)

# verify only the bottom lobe moved
changed = {(x, y) for y in range(64) for x in range(64)
           if out.get(x, y) != input_canvas.get(x, y)}
print("changed", len(changed), "outside region", len(changed - region))
print(out.stats_text())
view(out)
finish(out)
