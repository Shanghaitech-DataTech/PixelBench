import random

random.seed(7)

W, H = 82, 135
g = [[input_canvas.get(x, y) for x in range(W)] for y in range(H)]

def idx(x, y):
    if 0 <= x < W and 0 <= y < H:
        return g[y][x]
    return 0

TRANS = 0
DARK = 3
FOL = {1, 2, 3, 4}

out = input_canvas.copy(name="output")
SNOW = out.color("#f2f6fc", "snow")
SNOW_MID = out.color("#cfdcea", "snow_mid")
SNOW_SHADE = out.color("#a9bdd2", "snow_shade")

painted = {}

rows = []
for y in range(H):
    cand = [x for x in range(W) if idx(x, y) in FOL and idx(x, y - 1) in (TRANS, DARK)]
    runs = []
    for x in cand:
        if runs and runs[-1][-1] == x - 1:
            runs[-1].append(x)
        else:
            runs.append([x])
    rows.append(runs)

for y in range(H):
    for run in rows[y]:
        L = len(run)
        exterior = all(idx(x, y - 1) == TRANS for x in run)
        if L >= 3:
            keep = True
        elif L == 2:
            keep = random.random() < 0.7
        else:
            keep = random.random() < 0.4
        if not keep:
            continue
        for x in run:
            painted[(x, y)] = SNOW
        if L >= 5:
            for x in run[1:-1]:
                if idx(x, y + 1) in FOL and random.random() < 0.75:
                    painted.setdefault((x, y + 1), SNOW_MID)
        if exterior and L >= 6:
            for x in run[1:-1]:
                if idx(x, y - 1) == TRANS and random.random() < 0.6:
                    painted.setdefault((x, y - 1), SNOW)

# scattered specks of snow on remaining foliage, denser near the top
for y in range(H):
    for x in range(W):
        if (x, y) in painted or idx(x, y) not in FOL:
            continue
        p = 0.05 + 0.08 * max(0.0, 1.0 - y / 90.0)
        if random.random() < p and idx(x, y) != DARK:
            painted[(x, y)] = SNOW_MID

for (x, y), c in painted.items():
    out.set(x, y, c)

# edge definition: shade the underside and outer rim of the snow so it reads
snow_set = {SNOW, SNOW_MID, SNOW_SHADE}
edge = []
for y in range(H):
    for x in range(W):
        if out.get(x, y) not in snow_set:
            continue
        below = out.get(x, y + 1) if y + 1 < H else 0
        if below == 0:
            edge.append((x, y, SNOW_SHADE))
        else:
            left = out.get(x - 1, y) if x > 0 else 0
            right = out.get(x + 1, y) if x + 1 < W else 0
            if (left == 0 or right == 0) and out.get(x, y) == SNOW:
                edge.append((x, y, SNOW_MID))

for x, y, c in edge:
    out.set(x, y, c)

# a few flecks of snow caught on the trunk
for y in range(H):
    for x in range(W):
        if idx(x, y) in (5, 6, 7) and idx(x, y - 1) == TRANS:
            out.set(x, y, SNOW_MID)

view(out)
finish(out)
