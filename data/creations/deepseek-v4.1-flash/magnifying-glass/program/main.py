import math
from pixelbench_api import *

# ---------------------------------------------------------------------------
# 16x16 detective magnifying glass
# ---------------------------------------------------------------------------
W = H = 16
c = new_canvas(W, H, name="magnifier")

# palette ---------------------------------------------------------------
GOLD_L = '#f7dd8a'   # brass highlight (lit from the top-left)
GOLD   = '#d9a532'   # brass mid tone
GOLD_D = '#96681a'   # brass shadow
GLASS   = '#b7e0f5'  # lens body
GLASS_D = '#82c3e8'  # lens shadow crescent (lower-right interior)
SHINE   = '#ffffff'  # specular reflection

CX, CY = 6, 6        # lens centre

# 45-degree handle, 2 px wide, from the ring edge to the bottom-right ----
HANDLE = {}
for s in range(4, 9):
    HANDLE[(CX + s, CY + s)] = GOLD        # upper-right rail (lit)
    HANDLE[(CX + s - 1, CY + s)] = GOLD_D  # lower-left rail (shadow)

# lens: annulus 3.5 < r <= 5.45 (11 px disc, 7 px aperture) --------------
for y in range(H):
    for x in range(W):
        if (x, y) in HANDLE:
            c.set(x, y, HANDLE[(x, y)])
            continue
        dx, dy = x - CX, y - CY
        d = math.hypot(dx, dy)
        if d <= 3.5:                       # glass
            c.set(x, y, GLASS_D if dx + dy >= 3 else GLASS)
        elif d <= 5.45:                    # brass ring, diagonal gradient
            v = dx + dy
            c.set(x, y, GOLD_L if v <= -5 else (GOLD if v <= 3 else GOLD_D))

# specular reflection curving along the upper-left of the glass ----------
for (x, y) in [(5, 3), (4, 4), (4, 5)]:
    c.set(x, y, SHINE)

print(c.stats_text())
print(c.matrix_text())
print(sorted(cc['rgba'] for cc in c.palette()))
save("magnifier", c)
finish(c)
