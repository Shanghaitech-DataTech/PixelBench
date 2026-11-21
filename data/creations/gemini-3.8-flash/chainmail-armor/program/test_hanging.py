from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#0a0d14")

# Test U-shaped hanging rings
# Ring centered at (cx, cy):
# (cx-1, cy-1): Top-left hook (bright)
# (cx+1, cy-1): Top-right hook (mid)
# (cx-1, cy):   Left side (light mid)
# (cx+1, cy):   Right side (shadow)
# (cx,   cy+1): Bottom rim (shadow)
# (cx,   cy):   Center hole (dark void)

def draw_hanging_ring(c, cx, cy, col_hi, col_mid, col_shad, col_hole):
    c.set(cx, cy, col_hole)
    c.set(cx - 1, cy - 1, col_hi)
    c.set(cx + 1, cy - 1, col_mid)
    c.set(cx - 1, cy, col_mid)
    c.set(cx + 1, cy, col_shad)
    c.set(cx, cy + 1, col_shad)

# Grid:
# cy = 3, 6, 9, 12, ... (step 3)
# cx spacing = 3 (offset by 1.5 or alternate)
# If cy step is 2:
for r in range(12):
    cy = 2 + r * 2
    ox = 2 if (r % 2 == 1) else 0
    for col in range(10):
        cx = col * 4 + ox
        draw_hanging_ring(c, cx, cy, "#f1f5f9", "#94a3b8", "#475569", "#111827")

view(c)
