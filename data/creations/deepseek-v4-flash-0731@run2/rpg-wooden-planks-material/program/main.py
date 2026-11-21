import math, random
from pixelbench_api import new_canvas, finish

W = H = 16
c = new_canvas(W, H, name="rpg-wooden-planks")

GROOVE  = (44, 28, 16)
GROOVE2 = (70, 46, 26)
GRAIN_T = (78, 46, 24)
HILI_T  = (236, 200, 152)
K1 = (80, 50, 28); K2 = (116, 76, 44); K3 = (150, 106, 64)

board_cols = [(1, 2, 3), (5, 6, 7), (9, 10, 11), (13, 14, 15)]
base_tones = [(200, 154, 102), (148, 102, 62), (192, 146, 94), (140, 96, 56)]
joint_y    = [5, 11, 2, 8]

random.seed(23)
ph = {x: random.random() for x in range(16)}
st = {x: random.choice([-1.0, -0.5, 0, 0, 0.5, 1.0]) for x in range(16)}

def q(v, step=0.05):
    # quantize to discrete shading levels
    lo, hi = -0.125, 0.275
    v = max(lo, min(hi, v))
    return round(v / step) * step

def shade(base, a, target):
    if a >= 0:
        return tuple(int(base[i] + (target[i] - base[i]) * min(1.0, a)) for i in range(3))
    return tuple(int(base[i] + (HILI_T[i] - base[i]) * min(1.0, -a)) for i in range(3))

def board_of(x):
    for cols in board_cols:
        if x in cols:
            return cols
    return None

def board_tone(x):
    for cc, tone in zip(board_cols, base_tones):
        if x in cc:
            return tone
    return (100, 70, 40)

# grooves: quantized dark seam gradient
for y in range(H):
    for x in (0, 4, 8, 12):
        f = 0.5 + 0.5 * math.sin(2 * math.pi * (y / 16 + ph[x]))
        if f < 0.3:
            g = GROOVE
        elif f < 0.7:
            g = tuple(int((GROOVE[i] + GROOVE2[i]) / 2) for i in range(3))
        else:
            g = GROOVE2
        c.set(x, y, g)

# board bodies with quantized wood grain
for y in range(H):
    for x in range(W):
        if x in (0, 4, 8, 12):
            continue
        cols = board_of(x)
        base = board_tone(x)
        bev = -0.06 if x == cols[0] else (0.04 if x == cols[-1] else 0.0)
        d = (bev + 0.06 * st[x]
             + 0.09 * math.sin(2 * math.pi * (y / 16 + ph[x]))
             + 0.05 * math.sin(2 * math.pi * (y / 16 + 2 * ph[x])))
        c.set(x, y, shade(base, q(d), GRAIN_T))

# board ends: staggered horizontal joints, alternating light/dark end slivers
for i, (cols, jy, tone) in enumerate(zip(board_cols, joint_y, base_tones)):
    above = 0.0 if i % 2 == 0 else -0.05
    below = 0.15 if i % 2 == 0 else 0.10
    for x in cols:
        c.set(x, jy,   shade(tone, 0.55, GRAIN_T))
        c.set(x, jy - 1, shade(tone, above, GRAIN_T))
        c.set(x, jy + 1, shade(tone, below, GRAIN_T))

def knot(kx, ky, big=True):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            c.set(kx + dx, ky + dy, K2)
    c.set(kx, ky, K1)
    if big:
        c.set(kx - 1, ky - 2, K3)
        c.set(kx + 1, ky + 2, K3)

knot(2, 10, True)
knot(6, 4,  True)
knot(10, 9, True)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15)))
finish(c)
