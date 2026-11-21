from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#0a0d14")

# True 3x3 circular rings:
# cx = 4, 8, 12, 16... / 6, 10, 14, 18...
# cy = 2, 4, 6, 8, 10...
# Each ring:
# (cx, cy): HOLE
# (cx, cy-1): TOP (highlight)
# (cx-1, cy): LEFT (mid)
# (cx+1, cy): RIGHT (shad)
# (cx, cy+1): BOTTOM (shad)
# Overlap points:
# The adjacent ring at (cx+2, cy+1) has:
# top at (cx+2, cy), which sits between (cx+1, cy) and (cx+3, cy)!

def draw_circle_ring(c, cx, cy, col_hi, col_mid, col_shad, col_hole):
    c.set(cx, cy, col_hole)
    c.set(cx, cy - 1, col_hi)
    c.set(cx - 1, cy, col_mid)
    c.set(cx + 1, cy, col_shad)
    c.set(cx, cy + 1, col_shad)

for r in range(12):
    cy = 3 + r * 2
    ox = 2 if (r % 2 == 1) else 0
    for col in range(10):
        cx = col * 4 + ox
        draw_circle_ring(c, cx, cy, "#f1f5f9", "#cbd5e1", "#475569", "#111827")

view(c)
