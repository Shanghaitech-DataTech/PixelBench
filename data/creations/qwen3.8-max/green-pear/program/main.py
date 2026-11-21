import math
from pixelbench_api import new_canvas, view, save, finish

W = H = 32

# ---- palette (7 visible colours) ----
OUT  = "#20281a"   # dark outline
DARK = "#456e21"   # shadow green
MID  = "#6ea532"   # body green
LITE = "#a4d34c"   # lit green
PALE = "#d8ef8e"   # specular
BRN  = "#8a5a2c"   # stem
LBRN = "#bd8f52"   # stem highlight

c = new_canvas(W, H, name="pear")

# ---- body silhouette: y -> (left, right) inclusive ----
rows = {
     7: (13, 18),
     8: (12, 19),
     9: (12, 19),
    10: (11, 20),
    11: (11, 20),
    12: (10, 21),
    13: (10, 21),
    14: ( 9, 22),
    15: ( 9, 22),
    16: ( 8, 23),
    17: ( 8, 23),
    18: ( 7, 24),
    19: ( 7, 24),
    20: ( 6, 25),
    21: ( 6, 25),
    22: ( 6, 25),
    23: ( 6, 25),
    24: ( 6, 25),
    25: ( 7, 24),
    26: ( 8, 23),
    27: ( 9, 22),
    28: (10, 21),
    29: (11, 20),
    30: (13, 18),
}
TOP, BOT = min(rows), max(rows)

# outline silhouette
for y, (L, R) in rows.items():
    c.rect(L, y, R - L + 1, 1, OUT)

# interior base + radial shading (light from upper-left)
LX, LY = 11.0, 14.5
for y, (L, R) in rows.items():
    if y == TOP or y == BOT:
        continue
    for x in range(L + 1, R):
        d = math.hypot((x - LX) / 9.0, (y - LY) / 11.5)
        edge = min(x - L, R - x, y - TOP, BOT - y)
        if d < 0.34:
            col = PALE
        elif d < 0.62:
            col = LITE
        elif d < 1.00:
            col = MID
        else:
            col = DARK
        # keep a dark rim on the shadow side
        if edge <= 1 and (x > 16 or y > 24):
            col = DARK
        if y >= 28 and d > 0.55:
            col = DARK
        c.set(x, y, col)

# ---- lenticel speckles ----
speckles = [(13, 19), (16, 22), (10, 23), (19, 17), (14, 26),
            (21, 21), (12, 15), (18, 26), (23, 20), (16, 12)]
i_mid, i_dark = c.color(MID), c.color(DARK)
for (x, y) in speckles:
    (L, R) = rows.get(y, (0, -1))
    if L + 1 <= x <= R - 1 and y not in (TOP, BOT):
        cur = c.get(x, y)
        if cur == i_mid:
            c.set(x, y, LITE)
        elif cur == i_dark:
            c.set(x, y, MID)

# ---- stem ----
stem_core = {2: (17, 18), 3: (17, 18), 4: (16, 17),
             5: (16, 17), 6: (15, 17), 7: (15, 17)}
stem_out  = {1: (16, 19), 2: (16, 19), 3: (16, 19), 4: (15, 18),
             5: (15, 18), 6: (14, 18)}
for y, (L, R) in stem_out.items():
    c.rect(L, y, R - L + 1, 1, OUT)
for y, (L, R) in stem_core.items():
    c.rect(L, y, R - L + 1, 1, BRN)
for y in (2, 3):
    c.set(17, y, LBRN)
for y in (4, 5):
    c.set(16, y, LBRN)
for y in (6,):
    c.set(15, y, LBRN)

# ---- leaf (built on its own layer so outline() only touches the leaf) ----
leaf = new_canvas(W, H, name="leaf")
leaf.path("M 18 6 Q 22 0 29 1 Q 31 4 27 7 Q 22 10 18 6 Z", MID, fill=True)
leaf.line(19, 6, 28, 3, DARK)
leaf.set(23, 2, LITE)
leaf.set(25, 2, LITE)
leaf.set(27, 2, LITE)
leaf.outline(OUT)
c.blit(leaf, 0, 0)

view(c)
save("green_pear", c, indexed=True)
print(c.stats_text())
finish(c)
