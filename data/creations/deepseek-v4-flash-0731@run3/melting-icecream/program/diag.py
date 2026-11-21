from pixelbench_api import *

src = input_canvas
out = input_canvas.copy(name="output")

# Reproduce the drawing
MAIN = 5
CORE = 18
LIGHT = 24

def drip(c, a, b, rad, main=MAIN, core=CORE, light=LIGHT):
    ax, ay = a
    bx, by = b
    n = max(1, abs(by - ay), abs(bx - ax))
    for i in range(n + 1):
        t = i / n
        x = round(ax + (bx - ax) * t)
        y = round(ay + (by - ay) * t)
        c.circle(x, y, rad, main)
    for i in range(n + 1):
        t = i / n
        x = round(ax + (bx - ax) * t)
        y = round(ay + (by - ay) * t)
        c.circle(x, y, max(1, rad - 1), core)
    for i in range(n):
        t = i / n
        x = round(ax + (bx - ax) * t) - 1
        y = round(ay + (by - ay) * t)
        c.set(x, y, light)

drips = [
    ((17, 27), (18, 40), 2),
    ((22, 29), (23, 37), 2),
    ((28, 30), (27, 49), 2),
    ((33, 27), (34, 42), 3),
    ((39, 28), (40, 44), 2),
    ((44, 28), (42, 35), 2),
    ((47, 29), (46, 38), 2),
]
for a, b, r in drips:
    drip(out, a, b, r)
for x, y in [(20, 30), (25, 30), (31, 30), (36, 30), (41, 30)]:
    out.circle(x, y, 2, MAIN)
    out.circle(x - 1, y, 1, CORE)
out.circle(36, 44, 2, MAIN)
out.circle(35, 45, 1, CORE)
out.circle(27, 53, 1, MAIN)
out.circle(28, 55, 1, MAIN)
out.set(28, 56, MAIN)
out.set(27, 55, LIGHT)
out.set(29, 54, CORE)

for y in range(30, 58):
    line = []
    for x in range(20, 40):
        si = src.get(x, y)
        oi = out.get(x, y)
        mark = "=" if si == oi else ("+" if oi in (5, 18, 24) else "!")
        line.append(mark)
    print(y, "".join(line))
