from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#0a0d14")

# Test horizontal oblong rings (wider than tall)
# Ring centered around (cx, cy):
# Width 4, Height 2 or 3:
# cx is center-left (cx, cx+1 are hole)
# (cx-1, cy): Left rim
# (cx+2, cy): Right rim
# (cx, cy-1), (cx+1, cy-1): Top rim (highlight)
# (cx, cy+1), (cx+1, cy+1): Bottom rim (shadow)
# (cx, cy), (cx+1, cy): Center hole (dark void)

def draw_horiz_ring(c, cx, cy, col_hi, col_mid, col_shad, col_hole):
    c.set(cx, cy, col_hole)
    c.set(cx + 1, cy, col_hole)
    c.set(cx - 1, cy, col_mid)
    c.set(cx + 2, cy, col_shad)
    c.set(cx, cy - 1, col_hi)
    c.set(cx + 1, cy - 1, col_hi)
    c.set(cx, cy + 1, col_shad)
    c.set(cx + 1, cy + 1, col_shad)

# Grid with cy step = 2, cx step = 3
# If cy step is 2 and cx step is 3:
# Odd rows offset by 1.5? (say 1, then 2)
for r in range(12):
    cy = 2 + r * 2
    ox = (r % 2) * 2  # shift by 2
    for col in range(10):
        cx = col * 4 + ox
        draw_horiz_ring(c, cx, cy, "#f1f5f9", "#94a3b8", "#475569", "#111827")

view(c)
