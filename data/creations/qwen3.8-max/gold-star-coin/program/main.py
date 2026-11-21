import math
from pixelbench_api import new_canvas, view, save, finish

W = H = 16
c = new_canvas(W, H, name="coin")

# ---- palette (6 colours, transparency is free) ----
OUT   = '#3A2408'   # dark brown outline
RIM_D = '#8A5A16'   # shadowed gold
RIM_L = '#E3A72C'   # mid gold
FACE  = '#FFD24A'   # bright gold face
HI    = '#FFF0A8'   # pale highlight
STAR  = '#A85F14'   # deep amber star

cx = cy = 7.5
R_OUT = 8.0     # disc edge (inclusive)
R_OL  = 7.0     # inside this: rim
R_RIM = 5.8     # inside this: face

SQ2 = math.sqrt(2.0)

for y in range(H):
    for x in range(W):
        dx = x - cx
        dy = y - cy
        d = math.hypot(dx, dy)
        if d > R_OUT:
            continue
        if d > R_OL:
            c.set(x, y, OUT)
            continue
        # t = -1 toward top-left, +1 toward bottom-right
        t = (dx + dy) / (SQ2 * d) if d > 0 else 0.0
        if d > R_RIM:
            if t < -0.55:
                c.set(x, y, HI)
            elif t > 0.15:
                c.set(x, y, RIM_D)
            else:
                c.set(x, y, RIM_L)
        else:
            if t < -0.45 and d > 4.9:
                c.set(x, y, HI)
            elif t > 0.60 and d > 4.4:
                c.set(x, y, RIM_L)
            else:
                c.set(x, y, FACE)

# ---- star (hand-drawn 9x8 bitmap, centred on the coin) ----
STAR_MAP = [
    "....##....",
    "....##....",
    "...####...",
    "##########",
    "...####...",
    "..##..##..",
    ".##....##.",
    "##......##",
]
sx, sy = 3, 4
for ry, row in enumerate(STAR_MAP):
    for rx, ch in enumerate(row):
        if ch == "#":
            c.set(sx + rx, sy + ry, STAR)

print(c.stats_text())
p = view(c)
print(p)
save("coin", c)
finish(c)
