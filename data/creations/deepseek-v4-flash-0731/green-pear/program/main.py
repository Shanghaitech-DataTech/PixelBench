from pixelbench_api import new_canvas, finish

W = H = 32
c = new_canvas(W, H)

# Palette (6 visible colours)
OUT = c.color("#2c5e1e")    # dark outline green
BODY = c.color("#6abf3f")   # base pear green
HI = c.color("#a8e882")     # highlight
SH = c.color("#468f2c")     # shadow
STEM = c.color("#8a5a2b")   # brown stem
LEAF = c.color("#3f7d1f")   # leaf green

# Pear silhouette: half-width vs y (centre x = 16)
profile = [
    (7, 2.0),
    (9, 3.8),
    (11, 5.1),
    (13, 5.8),
    (15, 6.6),
    (17, 7.7),
    (19, 8.8),
    (21, 9.3),
    (22, 9.3),
    (23, 8.7),
    (24, 7.9),
    (25, 6.8),
    (26, 5.6),
    (27, 4.3),
    (28, 3.0),
    (29, 1.6),
]


def half_width(y):
    for i in range(len(profile) - 1):
        y0, w0 = profile[i]
        y1, w1 = profile[i + 1]
        if y0 <= y <= y1:
            t = (y - y0) / (y1 - y0)
            return w0 + t * (w1 - w0)
    return 0.0


def in_body(x, y):
    w = half_width(y)
    return w > 0 and abs(x - 16) <= w


# Body with outline and simple top-left light / bottom-right shade
for y in range(H):
    w = half_width(y)
    if w <= 0:
        continue
    for x in range(W):
        if not in_body(x, y):
            continue
        edge = any(not in_body(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        if edge:
            col = OUT
        else:
            t = (x - 16) / w
            if y <= 18 and t <= -0.45:
                col = HI
            elif y >= 26:
                col = SH
            elif y >= 20 and t >= 0.30:
                col = SH
            else:
                col = BODY
        c.set(x, y, col)

# Stem
c.rect(15, 3, 2, 4, STEM)

# Leaf sticking out to the right of the neck
c.poly([(18, 6), (21, 3), (25, 6), (22, 9)], LEAF)
c.poly([(18, 6), (21, 3), (25, 6), (22, 9)], OUT, fill=False)

print(c.stats_text())
finish(c)
