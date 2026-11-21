from pixelbench_api import *

c = input_canvas.copy(name="output")

# Palette indices of the scoop's chocolate shades (palette is 0-indexed)
MAIN = 5    # #5e363e  (scoop base chocolate)
CORE = 18   # #95524c  (lighter chocolate)
LIGHT = 24  # #99544d  (glossy highlight)

def drip(c, a, b, rad, main=MAIN, core=CORE, light=LIGHT):
    ax, ay = a
    bx, by = b
    n = max(1, abs(by - ay), abs(bx - ax))
    # outer chocolate stream
    for i in range(n + 1):
        t = i / n
        x = round(ax + (bx - ax) * t)
        y = round(ay + (by - ay) * t)
        c.circle(x, y, rad, main)
    # inner lighter core
    for i in range(n + 1):
        t = i / n
        x = round(ax + (bx - ax) * t)
        y = round(ay + (by - ay) * t)
        c.circle(x, y, max(1, rad - 1), core)
    # glossy streak on the left of the stream
    for i in range(n):
        t = i / n
        x = round(ax + (bx - ax) * t) - 1
        y = round(ay + (by - ay) * t)
        c.set(x, y, light)

# ---- Drips pouring from the scoop down the cone ----
drips = [
    ((20, 28), (21, 39), 2),   # left side, runs down the cone face
    ((22, 29), (23, 37), 2),
    ((28, 30), (27, 51), 2),   # centre stream running down to the tip
    ((33, 27), (34, 42), 3),   # thick centre-right stream
    ((39, 28), (40, 44), 2),
    ((44, 28), (42, 35), 2),
    ((47, 29), (46, 38), 2),
]
for a, b, r in drips:
    drip(c, a, b, r)

# ---- Melt bumps pooling over the rim ----
for x, y in [(20, 30), (25, 30), (31, 30), (36, 30), (41, 30)]:
    c.circle(x, y, 2, MAIN)
    c.circle(x - 1, y, 1, CORE)

# flick / bulge on the thick stream
c.circle(36, 44, 2, MAIN)
c.circle(35, 45, 1, CORE)

# droplet hanging off the cone tip (connects to the centre stream)
c.circle(27, 53, 1, MAIN)
c.circle(28, 55, 1, MAIN)
c.set(28, 56, MAIN)
c.set(27, 55, LIGHT)
c.set(29, 54, CORE)

finish(c)
