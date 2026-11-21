import math
from pixelbench_api import *

c = new_canvas(16, 16, name="gold-star-coin")

# palette (5 visible colors)
DARK = c.color("#3a2406")    # dark rim / outline
SHADOW = c.color("#8f6a12")  # outer gold shadow band
BODY = c.color("#d4a017")   # main gold
DISC = c.color("#f0c33c")   # inner light disc
STAR = c.color("#fff0a0")   # bright embossed star

# 15px coin centered -> circle center at (8,8)
cx, cy = 8, 8
c.circle(cx, cy, 7, DARK)     # 15px rim
c.circle(cx, cy, 6, SHADOW)   # shadow band
c.circle(cx, cy, 5, BODY)     # main gold ring
c.circle(cx, cy, 4, DISC)     # inner disc

# solid 5-point star: 5 arm triangles + center pentagon (even-odd safe)
R, r = 4.0, 1.8
outer = [(cx + R * math.cos(math.radians(i * 72 - 90)),
          cy + R * math.sin(math.radians(i * 72 - 90))) for i in range(5)]
inner = [(cx + r * math.cos(math.radians(i * 72 - 54)),
          cy + r * math.sin(math.radians(i * 72 - 54))) for i in range(5)]

for i in range(5):
    tri = [outer[i], inner[i], inner[(i - 1) % 5]]
    c.poly(tri, STAR)
c.poly(inner, STAR)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15)))
finish(c)
