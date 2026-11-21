"""gold-star-coin - 16x16 pixel art, 5 colours + transparency."""
import math
from collections import deque
from pixelbench_api import *

# ---------------------------------------------------------------- palette
DARK = "#5A3406"    # outline / rim
SHADOW = "#A8701A"  # bevelled lower-right
BASE = "#D99A2B"    # gold face
LIGHT = "#F7D06A"   # bevelled upper-left sheen
STAR = "#FFFFFF"    # star

CX = CY = 7.5  # coin centre (symmetric about x -> 15-x)

# ------------------------------------------------------------ coin shape
MASK = set()
for y in range(16):
    for x in range(16):
        if math.hypot(x - CX, y - CY) <= 7.0:
            MASK.add((x, y))

# 1 px outline = any masked pixel touching the outside (8-neighbourhood)
EDGE = set()
for (x, y) in MASK:
    for ox in (-1, 0, 1):
        for oy in (-1, 0, 1):
            if (ox or oy) and (x + ox, y + oy) not in MASK:
                EDGE.add((x, y))
                break
        if (x, y) in EDGE:
            break

# depth inward from the outline (0 = outline, 1 = bevel ring, >=2 = face)
DEPTH = {p: 0 for p in EDGE}
q = deque(EDGE)
while q:
    x, y = q.popleft()
    for ox, oy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        n = (x + ox, y + oy)
        if n in MASK and n not in DEPTH:
            DEPTH[n] = DEPTH[(x, y)] + 1
            q.append(n)

coin = new_canvas(16, 16, name="coin")
for (x, y) in MASK:
    dep = DEPTH.get((x, y), 9)
    lit = (x - CX) + (y - CY) < 0          # upper-left half is lit
    if dep == 0:
        col = DARK
    elif dep == 1:
        col = LIGHT if lit else SHADOW
    else:
        col = BASE
    coin.set(x, y, col)

# ------------------------------------------------------------------ star
# half-widths per row, symmetric about x = 7.5 (x and 15-x)
STAR_ROWS = [
    [7, 8],
    [6, 7, 8, 9],
    [5, 6, 7, 8, 9, 10],
    [4, 5, 6, 7, 8, 9, 10, 11],
    [5, 6, 7, 8, 9, 10],
    [5, 6, 7, 8, 9, 10],
    [5, 6, 9, 10],
    [5, 10],
]
STAR_TOP = 4
for row, xs in enumerate(STAR_ROWS):
    for x in xs:
        coin.set(x, STAR_TOP + row, STAR)

# ------------------------------------------------------------ validation
used = sorted({coin.get(x, y) for y in range(16) for x in range(16)})
asym = [(x, y) for y in range(16) for x in range(16) if coin.get(x, y) != coin.get(15 - x, y)]
print(coin.stats_text())
print("colours used:", len(used), "| vertical-axis mismatches:", len(asym))
print(coin.matrix_text())

save("gold-star-coin", coin)
finish(coin)
