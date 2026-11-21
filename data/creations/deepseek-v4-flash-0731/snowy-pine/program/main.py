from pixelbench_api import *
import random

out = input_canvas.copy(name='output')
w, h = out.stats()['size']

SNOW = out.color('#f5f8f5', name='snow')
SNOW_D = out.color('#cfe0ea', name='snow_shadow')

pal = {p['index']: p['rgba'] for p in out.palette()}

def alpha_at(x, y):
    if not (0 <= x < w and 0 <= y < h):
        return 0
    return pal[out.get(x, y)][3]

def tree_at(x, y):
    return alpha_at(x, y) > 0

def color_at(x, y):
    if not (0 <= x < w and 0 <= y < h):
        return None
    return pal[out.get(x, y)]

SNOW = out.color('#f5f8f5', name='snow')
SNOW_D = out.color('#cfe0ea', name='snow_shadow')

top = {}
bot = {}
for x in range(w):
    ts = [y for y in range(h) if tree_at(x, y)]
    if ts:
        top[x] = ts[0]
        bot[x] = ts[-1]

def depth_for(t):
    if t < 12:
        return random.randint(9, 12)
    if t < 24:
        return random.randint(7, 9)
    if t < 48:
        return random.randint(6, 8)
    if t < 80:
        return random.randint(5, 7)
    if t < 110:
        return random.randint(4, 6)
    return random.randint(4, 5)

rng = random.Random(7)

# 1) snow cap along every column, depth by tier
for x, t in top.items():
    b = bot[x]
    d = depth_for(t)
    d = min(d, b - t)
    end = t + d
    for y in range(t, end + 1):
        if tree_at(x, y):
            out.set(x, y, SNOW)
    # shadowed underside
    out.set(x, end, SNOW_D)

# 2) overhang: 1px snow clinging just outside branch tips at snow edges
for x in range(w):
    if x not in top:
        continue
    t = top[x]
    if t > 100:
        continue
    for nx in (x - 1, x + 1):
        if 0 <= nx < w and (nx not in top or top[nx] > t + 4):
            # neighbor is outside the tree at this height -> pile snow on the tip
            for dy in range(2):
                yy = t + dy - 1  # just above/at the tip, sticking out sideways
                if 0 <= yy < h and not tree_at(nx, yy):
                    out.set(nx, yy, SNOW if rng.random() < 0.8 else SNOW_D)

# 3) drips: a few downward snow trails from the snow bottom
for x in list(top.keys()):
    t = top[x]
    if t > 110:
        continue
    b = bot[x]
    d = depth_for(t)
    end = min(t + d, b)
    if end < b and rng.random() < 0.16:
        dl = min(b, end + rng.randint(1, 3))
        for y in range(end + 1, dl + 1):
            if tree_at(x, y):
                out.set(x, y, SNOW_D if y > end + 1 else SNOW)
                if y == dl:
                    break
        # drip tip shadow
        if dl < b:
            out.set(x, min(b, dl + 1), SNOW_D)

# 4) snow on trunk: clean cap on top of the trunk + a couple of clumps on the sides
trunk_px = [(x, y) for y in range(116, h) for x in range(w)
           if tree_at(x, y) and color_at(x, y) and color_at(x, y)[0] < 130
           and color_at(x, y)[0] > color_at(x, y)[2]]
if trunk_px:
    miny = min(y for _, y in trunk_px)
    xs = sorted({x for x, y in trunk_px if y == miny})
    for x in xs:
        for dy in range(2):
            yy = miny + dy
            if yy < h and tree_at(x, yy) and color_at(x, yy)[0] < 130:
                out.set(x, yy, SNOW)
        if miny + 2 < h and tree_at(x, miny + 2):
            out.set(x, miny + 2, SNOW_D)
    # small clumps sticking to the trunk sides
    for x, y in [(39, 129), (48, 130), (40, 131), (47, 128)]:
        if tree_at(x, y):
            out.set(x, y, SNOW)
            if y + 1 < h and tree_at(x, y + 1):
                out.set(x, y + 1, SNOW_D)

# 5) shadows: re-assert snow_shadow just under snow columns that now have tree below the cap
for x in list(top.keys()):
    t = top[x]
    d = depth_for(t)
    b = bot[x]
    end = min(t + d, b)
    if end + 1 <= b:
        out.set(x, end, SNOW_D)

finish(out)
