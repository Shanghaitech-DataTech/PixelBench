from pixelbench_api import *
import math

W = H = 48
c = new_canvas(W, H, name="magic-staff")

# ---- palette ----
wood_out  = c.color("#331c0d")
wood_base = c.color("#7a4b21")
wood_mid  = c.color("#8f5c2a")
wood_light= c.color("#b08044")
wood_hi   = c.color("#d1a263")
wrap_dark = c.color("#3f2a12")
metal    = c.color("#a8aeb8")
metal_hi  = c.color("#d0d6de")
gem_dark  = c.color("#2a0a4e")
gem      = c.color("#5f1fb0")
gem_mid   = c.color("#8d42e6")
gem_light = c.color("#b87cff")
gem_hi    = c.color("#e4ccff")

def stroke(pts, r, color):
    for (x, y) in pts:
        c.circle(round(x), round(y), r, color)

# ---- staff centerline: straight shaft + quarter-circle crook head ----
pts = [(24, y) for y in range(21, 45)]
cx, cy, R = 24, 9, 12
n = 60
for i in range(n + 1):
    a = (math.pi / 2) * (1 - i / n)
    pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for x in range(37, 40):
    pts.append((x, 9))

stroke(pts, 3, wood_out)     # dark outline
stroke(pts, 2, wood_base)    # base wood

# wooden shading
for y in range(23, 42):
    c.set(22, y, wood_light)   # lit left edge
    c.set(26, y, wood_mid)     # shaded right edge
for y in (26, 33, 40):
    c.set(22, y, wood_hi)

# curved-head shading on the outer (convex) edge
for i in range(n + 1):
    a = (math.pi / 2) * (1 - i / n)
    x = cx + R * math.cos(a)
    y = cy + R * math.sin(a)
    dx = (x - cx) / R
    dy = (y - cy) / R
    if 0.08 < i / n < 0.95:
        c.set(round(x + dx * 1.5), round(y + dy * 1.5), wood_light)

# metal wrap near the base
c.rect(21, 30, 7, 2, wrap_dark)
c.rect(22, 31, 5, 1, metal)
c.set(23, 31, metal_hi)

# pointed wooden tip
c.poly([(21, 42), (27, 42), (24, 47)], wood_out)
c.poly([(22, 43), (26, 43), (24, 46)], wood_base)
c.set(24, 45, wood_light)
c.set(23, 42, wood_light)

# ---- glowing orb at the tip ----
ox, oy = 38, 8
c.circle(ox, oy, 5, gem_dark)
c.circle(ox, oy, 4, gem)
c.circle(ox - 1, oy - 1, 2, gem_mid)
c.set(ox - 2, oy - 2, gem_light)
c.set(ox - 1, oy - 2, gem_hi)
c.set(ox - 2, oy - 1, gem_hi)

# ---- purple particles ----
def dot(x, y, col):
    c.set(x, y, col)

def cross(x, y, col):
    for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
        c.set(x + dx, y + dy, col)

dots = [
    (9, 9, gem_light), (14, 17, gem_mid), (7, 25, gem), (5, 33, gem_light),
    (13, 37, gem_mid), (19, 7, gem), (26, 3, gem_light), (31, 13, gem_mid),
    (37, 2, gem_light), (44, 15, gem), (46, 22, gem_light), (43, 28, gem_mid),
    (45, 37, gem), (40, 44, gem_light), (33, 42, gem_mid), (18, 45, gem_light),
    (11, 44, gem_mid), (5, 20, gem), (21, 5, gem_mid), (34, 24, gem),
    (30, 31, gem_light), (24, 11, gem_mid), (43, 13, gem_light), (12, 4, gem_mid),
    (46, 8, gem), (8, 40, gem_light), (36, 24, gem_light),
]
for (x, y, col) in dots:
    dot(x, y, col)

crosses = [
    (17, 5, gem_hi), (40, 19, gem_hi), (11, 29, gem_light), (31, 36, gem_hi),
    (14, 41, gem_hi), (43, 25, gem_light), (27, 38, gem_hi),
]
for (x, y, col) in crosses:
    cross(x, y, col)

print(c.stats_text())

finish(c)
