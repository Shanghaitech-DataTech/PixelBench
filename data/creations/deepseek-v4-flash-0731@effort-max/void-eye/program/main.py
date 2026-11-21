import math
from pixelbench_api import *


def mix(a, b, t):
    return tuple(int(round(a[i] * (1 - t) + b[i] * t)) for i in range(3))


c = new_canvas(64, 64, name="void_eye")

# palette
body  = c.color("#0b0512")
body2 = c.color("#130b20")
body3 = c.color("#1a0f2e")
body4 = c.color("#211540")
vein  = c.color("#2b1a48")
veinr = c.color("#3a1648")
rim   = c.color("#4d3784")
iris  = [c.color(h) for h in ("#14043f", "#1b0754", "#230b6c", "#2d1088", "#3916a6", "#471ec4")]
ga    = c.color(mix((0x39, 0x16, 0xa6), (0xdc, 0xcf, 0xff), 0.30))
gb    = c.color(mix((0x47, 0x1e, 0xc4), (0xdc, 0xcf, 0xff), 0.52))
p1    = c.color(mix((0x57, 0x30, 0xdc), (0xdc, 0xcf, 0xff), 0.78))
p2    = c.color("#d9cdff")
wht   = c.color("#ffffff")
f     = c.color("#0a0410")
ft    = c.color("#c9b8f2")


def tent(pts, r0, col):
    """Thick tapered tentacle along a polyline."""
    ptsf = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        n = max(1, int(round(math.hypot(x1 - x0, y1 - y0) * 2)))
        for k in range(n + 1):
            ptsf.append((x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n))
    m = len(ptsf)
    for i, (x, y) in enumerate(ptsf):
        r = max(1.0, r0 * (1 - (i / (m - 1)) * 0.82))
        c.circle(round(x), round(y), round(r), col)


# faint void aura so the boss reads on anything
c.ellipse(32, 27, 22, 23, (110, 70, 220, 16))
c.ellipse(32, 27, 19, 20, (110, 70, 220, 8))

# top spikes -> menacing silhouette
c.poly([(26, 11), (33, 2), (39, 10)], body)
c.poly([(15, 17), (21, 8), (25, 15)], body)
c.poly([(40, 15), (45, 8), (50, 17)], body)

# main orb, shaded upper-left
c.ellipse(32, 27, 20, 21, body)
c.ellipse(31, 26, 17, 18, body2)
c.ellipse(30, 25, 13, 14, body3)
c.ellipse(30, 24, 9, 10, body4)

# vessels crawling out from under the iris
for ang in (-158, -128, -98, -68, -38, -16, 10, 32, 60, 90, 120, 150):
    a = math.radians(ang)
    c.line(round(32 + 13.5 * math.cos(a)), round(28 + 14.5 * math.sin(a)),
           round(32 + 19.2 * math.cos(a)), round(27 + 20.2 * math.sin(a)), vein)
c.line(24, 17, 29, 13, veinr)
c.line(40, 17, 35, 13, veinr)

# deep purple iris, layered
for rx, ry, colr in ((12, 13, iris[0]), (10, 11, iris[1]), (8, 9, iris[2]),
                    (6, 7, iris[3]), (4, 5, iris[4])):
    c.ellipse(32, 28, rx, ry, colr)

# faintly glowing pupil
c.circle(32, 28, 8, ga)
c.circle(32, 28, 6, gb)
c.circle(32, 28, 5, p1)
c.circle(32, 28, 3, p2)
c.set(32, 28, wht)
c.set(33, 27, wht)
c.set(31, 29, wht)

# brow crease and a small fanged maw
c.line(24, 14, 40, 14, f)
c.ellipse(32, 41, 4, 2, f)
c.poly([(29, 41), (30, 44), (31, 41)], ft)
c.poly([(33, 41), (34, 44), (35, 41)], ft)

# short tentacles
tent([(13, 45), (8, 51), (7, 54), (6, 55)], 6, body)
tent([(22, 48), (18, 54), (17, 56)], 5, body)
tent([(27, 48), (26, 56), (26, 58), (25, 59)], 4, body2)
tent([(37, 48), (38, 56), (38, 58), (39, 59)], 4, body2)
tent([(42, 48), (46, 54), (47, 56), (48, 57)], 5, body)
tent([(51, 45), (56, 50), (57, 53), (58, 55)], 6, body)
c.set(12, 46, body3)
c.set(51, 46, body3)

# rim light along the top edge
for i in range(46):
    a = math.radians(192 + i * 3)
    c.set(round(32 + 20.2 * math.cos(a)), round(27 + 21.2 * math.sin(a)), rim)
c.set(32, 6, rim)

# floating motes
for x, y, k in ((8, 20, 0), (54, 13, 0), (7, 32, 1), (57, 28, 1),
               (50, 7, 1), (13, 9, 0), (58, 44, 1), (5, 48, 0)):
    c.set(x, y, "#4a2f7a" if k else "#241440")

# soft hover shadow beneath
c.ellipse(32, 60, 22, 3, (0, 0, 0, 40))
c.ellipse(32, 60, 17, 2, (0, 0, 0, 80))
c.ellipse(32, 60, 11, 2, (0, 0, 0, 120))

print(c.stats_text())
print("palette size:", len(c.palette()))
print(c.matrix_text(region=(20, 20, 44, 40), indices=False))

finish(c)
