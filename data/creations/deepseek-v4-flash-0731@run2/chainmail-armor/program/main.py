from pixelbench_api import new_canvas, finish

W = 32
c = new_canvas(W, W)

# Chainmail hauberk silhouette: shoulders wide at the top, tapering to the waist.
# Rows: y -> (x0, x1) inclusive, centered near x=15.5
shape = {
    2: (13, 18),
    3: (9, 22),
    4: (7, 24),
    5: (5, 26),
    6: (4, 27),
    7: (4, 27),
    8: (4, 27),
    9: (5, 26),
    10: (5, 26),
    11: (5, 26),
    12: (5, 26),
    13: (6, 25),
    14: (6, 25),
    15: (7, 24),
    16: (7, 24),
    17: (8, 23),
    18: (8, 23),
    19: (9, 22),
    20: (9, 22),
    21: (10, 21),
    22: (11, 20),
    23: (12, 19),
    24: (13, 18),
    25: (13, 18),
    26: (14, 17),
    27: (14, 17),
    28: (15, 16),
}

# 5 brightness variants: (top-left, top/left, right/bottom, bottom-right)
METAL = [
    ((242, 245, 248), (224, 228, 235), (192, 198, 206), (162, 168, 177)),
    ((230, 234, 240), (206, 212, 220), (172, 178, 187), (140, 146, 155)),
    ((214, 219, 227), (184, 191, 199), (150, 156, 166), (118, 124, 133)),
    ((196, 202, 211), (162, 168, 178), (128, 134, 144), (98, 104, 113)),
    ((176, 182, 192), (140, 146, 156), (108, 114, 123), (80, 85, 93)),
]
HOLE = (28, 32, 38)      # dark open link centers / under-shirt shadow
OUT = (15, 17, 21)      # dark outline


def in_shape(x, y):
    r = shape.get(y)
    return r is not None and r[0] <= x <= r[1]


def clamp(v, lo, hi):
    return lo if v < lo else (hi if v > hi else v)


def variant(x, y):
    v = (x - 8) // 5
    if y >= 15:
        v += 1
    if y >= 22:
        v += 1
    # bright spot on the wearer's left shoulder (viewer's left-top)
    if y <= 10 and x <= 14:
        v -= 1
    return clamp(v, 0, 4)


def ring_color(x, y):
    v = variant(x, y)
    band = clamp((y - 4) // 3, 0, 100)
    ry = 4 + 3 * band
    base = 7 if band % 2 == 0 else 8
    cx = base + 3 * round((x - base) / 3)
    dx = clamp(x - cx, -1, 1)
    dy = clamp(y - ry, -1, 1)
    if dx == 0 and dy == 0:
        return HOLE
    if dx < 0 and dy < 0:
        return METAL[v][0]
    if dx < 0 or dy < 0:
        return METAL[v][1]
    if dx > 0 and dy > 0:
        return METAL[v][3]
    return METAL[v][2]


for y in range(W):
    for x in range(W):
        if not in_shape(x, y):
            continue
        if not (in_shape(x - 1, y) and in_shape(x + 1, y) and in_shape(x, y - 1) and in_shape(x, y + 1)):
            c.set(x, y, OUT)
        else:
            c.set(x, y, ring_color(x, y))

print(c.stats_text())
print(c.matrix_text(indices=False))
finish([c])
