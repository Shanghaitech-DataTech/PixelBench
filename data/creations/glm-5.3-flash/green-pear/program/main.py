# green-pear: 32x32 pixel art, <= 7 visible colours
import math

W = H = 32
c = new_canvas(W, H, background=None, name="pear")

# ---- palette (7 colours) ----
OUT    = c.color("#3f5d2a", name="outline")
SHADE  = c.color("#6e9440", name="shade")
BODY   = c.color("#93c251", name="body")
MID    = c.color("#b1d76e", name="mid")
HILITE = c.color("#d3ea9f", name="highlight")
STEM   = c.color("#7a5230", name="stem")
LEAF   = c.color("#5d9c38", name="leaf")

# ---- pear silhouette (bulbous bottom, narrow neck) ----
c.path(
    "M 16 7 "
    "C 19 7 21 10 22 14 "
    "C 24 16 26 18 26 22 "
    "C 26 27 22 31 16 31 "
    "C 10 31 6 27 6 22 "
    "C 6 18 8 16 10 14 "
    "C 11 10 13 7 16 7 Z",
    BODY, fill=True,
)

# ---- dark rim outline ----
c.outline(OUT)

# ---- curved banded shading, light from the upper left ----
LX, LY = 12, 18
for y in range(H):
    for x in range(W):
        if c.get(x, y) == BODY:
            d = math.sqrt((x - LX) ** 2 + ((y - LY) * 1.15) ** 2)
            if d <= 5:
                c.set(x, y, HILITE)
            elif d <= 9:
                c.set(x, y, MID)
            elif d <= 13.5:
                c.set(x, y, BODY)
            else:
                c.set(x, y, SHADE)

# ---- stem ----
c.line(16, 6, 16, 4, STEM)
c.set(17, 3, STEM)
c.set(17, 2, STEM)

# ---- leaf: lens shape pointing up-right ----
c.path("M 18 6 Q 20 2 26 2 Q 25 7 18 6 Z", LEAF, fill=True)
# darker lower edge for depth
for x, y in [(19, 6), (20, 6), (21, 6), (22, 5), (23, 5), (24, 4), (25, 3)]:
    if c.get(x, y) == LEAF:
        c.set(x, y, SHADE)

print(c.stats_text())
print(c.matrix_text())

finish(c)
