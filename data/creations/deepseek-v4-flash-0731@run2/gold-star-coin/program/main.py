import math
from pixelbench_api import *

W = H = 16
c = new_canvas(W, H, name="gold-coin")

OUT   = c.color("#5c3d08", "outline")   # dark outline
GOLD  = c.color("#c98a15", "gold")     # main gold face
BRIGHT= c.color("#eeb933", "bright")   # bright rim
SHADE = c.color("#8f5f0a", "shade")    # shaded gold
STAR  = c.color("#ffe46b", "star")     # star fill
SPARK = c.color("#fff8d8", "spark")    # sparkle highlight

# ---- coin body ----
c.circle(8, 8, 7, OUT)      # 15px dark disc
c.circle(8, 8, 6, GOLD)     # 13px gold face
c.circle(9, 9, 5, SHADE)    # shade bottom-right
c.circle(7, 7, 5, GOLD)     # restore gold top-left -> crescent shading
c.circle(8, 8, 5, BRIGHT, fill=False)  # bright inner rim ring

# ---- star in the middle ----
star_pts = [(8, 2), (10, 5), (12, 6), (11, 9), (11, 12),
            (8, 11), (5, 12), (5, 9), (4, 6), (6, 5)]
c.poly(star_pts, STAR)

# ---- sparkle highlights on the rim ----
c.set(2, 3, SPARK)
c.set(3, 2, SPARK)
c.set(13, 13, SPARK)

print(c.stats_text())
print()
print(c.matrix_text())

finish(c)
