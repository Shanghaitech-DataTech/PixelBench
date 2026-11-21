import random
from pixelbench_api import new_canvas, finish

W = H = 16

# Palette (Minecraft-style dirt browns). At most 10 colours.
DARK     = (0x33, 0x24, 0x14)  # dark soil
DARKBRN  = (0x48, 0x33, 0x1d)  # dark brown
BASE     = (0x58, 0x3d, 0x24)  # base dirt
MID      = (0x68, 0x49, 0x2c)  # mid
LIGHT    = (0x79, 0x56, 0x36)  # light
TAN      = (0x8c, 0x66, 0x42)  # tan specks
SPECK    = (0x9c, 0x74, 0x4c)  # light speck

random.seed(7)

# Seamless periodic value noise: a small grid that wraps around.
G = 4
vals = [[random.random() for _ in range(G)] for _ in range(G)]

def period_value(u, v):
    i = int(u) % G
    j = int(v) % G
    a = u - int(u)
    b = v - int(v)
    x0 = vals[(i) % G][(j) % G]
    x1 = vals[(i + 1) % G][(j) % G]
    y0 = vals[(i) % G][(j + 1) % G]
    y1 = vals[(i + 1) % G][(j + 1) % G]
    # smoothstep
    a = a * a * (3 - 2 * a)
    b = b * b * (3 - 2 * b)
    top = x0 + (x1 - x0) * a
    bot = y0 + (y1 - y0) * a
    return top + (bot - top) * b

# Precompute a second noise channel for variety.
random.seed(11)
vals2 = [[random.random() for _ in range(G)] for _ in range(G)]

def period_value2(u, v):
    i = int(u) % G
    j = int(v) % G
    a = u - int(u)
    b = v - int(v)
    x0 = vals2[(i) % G][(j) % G]
    x1 = vals2[(i + 1) % G][(j) % G]
    y0 = vals2[(i) % G][(j + 1) % G]
    y1 = vals2[(i + 1) % G][(j + 1) % G]
    a = a * a * (3 - 2 * a)
    b = b * b * (3 - 2 * b)
    top = x0 + (x1 - x0) * a
    bot = y0 + (y1 - y0) * a
    return top + (bot - top) * b

c = new_canvas(W, H)

# Deterministic speckle map, periodic.
random.seed(23)
specks = {}
pebbles = {}
for y in range(H):
    for x in range(W):
        if random.random() < 0.06:
            specks[(x, y)] = TAN
        elif random.random() < 0.13:
            specks[(x, y)] = SPECK
        r = random.random()
        if r < 0.05:
            pebbles[(x, y)] = DARK

for y in range(H):
    for x in range(W):
        u = x * (G / W)
        v = y * (G / H)
        n1 = period_value(u, v)
        n2 = period_value2(u, v)
        # combine
        val = 0.65 * n1 + 0.35 * n2
        extra = specks.get((x, y))
        if extra is not None:
            colour = extra
        elif (x, y) in pebbles:
            colour = pebbles[(x, y)]
        else:
            if val < 0.34:
                colour = DARKBRN
            elif val < 0.48:
                colour = BASE
            elif val < 0.62:
                colour = DARKBRN if val < 0.55 else MID
            elif val < 0.78:
                colour = MID
            elif val < 0.9:
                colour = LIGHT
            else:
                colour = DARK
        c.set(x, y, colour)

# Sprinkle tiny clusters for granularity (periodic-aware).
for y in range(H):
    for x in range(W):
        if (x % 4 == 0 and y % 4 == 0) and random.random() < 0.5:
            c.set((x + 1) % W, y, DARK)

print(c.stats_text())
finish(c)
