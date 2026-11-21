import math
from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H)

# ----- height field: contour terraces around a summit, wobbled contours -----
PX, PY = 28.0, 10.0
SP = 5.4

def darken(hexv, f):
    h = hexv.lstrip("#")
    r = int(h[0:2], 16); g = int(h[2:4], 16); b = int(h[4:6], 16)
    return (int(r * f), int(g * f), int(b * f))

golds = ["#d6d0a2", "#dccb98", "#dfc68c", "#e0c080", "#dfb874", "#dbae68",
         "#d4a25c", "#ca9451", "#be8648", "#b07840", "#a06a38", "#8e5c30",
         "#7c4e2a", "#6a4224"]
gidx  = [c.color(g) for g in golds]
shades = [c.color(darken(g, 0.82)) for g in golds]
risers = [c.color(darken(g, 0.56)) for g in golds]
haze   = [c.color(x) for x in ("#c6d3d5", "#aebfc2", "#99abb0")]
spk    = [c.color(x) for x in ("#b6a05e", "#86623a")]

def hh_at(x, y):
    dx = x - PX; dy = y - PY
    d = math.sqrt(dx * dx * 0.85 + dy * dy * 1.35)
    return d + 3.2 * math.sin(dx * 0.27 + dy * 0.20) + 2.4 * math.cos(dx * 0.11 - dy * 0.23)

for y in range(H):
    for x in range(W):
        dx = x - PX; dy = y - PY
        edge = -4.0 + 2.0 * math.sin(dx * 0.30 + 0.5)
        if dy < edge:                       # far mountain wall -> atmospheric haze
            hh = hh_at(x, y)
            col = haze[0] if hh > 24 else (haze[1] if hh > 13 else haze[2])
            c.set(x, y, col)
            continue
        hh = hh_at(x, y)
        t = int(hh / SP)
        if t > 13: t = 13
        f = hh / SP - t
        if f < 0.16:
            col = risers[t]                 # narrow soil ridge between steps
        elif f < 0.34:
            col = shades[t]                 # shaded terrace value
        else:
            r = ((x * 73) ^ (y * 151)) & 255
            col = spk[1] if r < 13 else (spk[0] if r < 26 else gidx[t])
        c.set(x, y, col)

# ----- distant village on the summit plateau -----
roof  = c.color("#b45a42"); roofd = c.color("#8f4434")
wall  = c.color("#ecdcba"); win  = c.color("#33363e"); shd  = c.color("#8a7440")

def house(x, y):
    c.rect(x,     y, 4, 1, roof)
    c.rect(x,     y + 1, 4, 1, roofd)
    c.set(x,     y + 2, wall); c.set(x + 1, y + 2, wall)
    c.set(x + 2, y + 2, win);  c.set(x + 3, y + 2, wall)
    c.set(x + 1, y + 3, shd);  c.set(x + 2, y + 3, shd)

tl  = c.color("#79b268"); td = c.color("#4a8a4c"); tsh = c.color("#5a5a34")

def tree(x, y):
    c.set(x,     y, tl); c.set(x + 1, y, tl)
    c.set(x,     y + 1, td); c.set(x + 1, y + 1, td)
    c.set(x + 2, y + 1, tsh)

for hx, hy in [(20, 9), (26, 8), (32, 9), (38, 11), (24, 10), (30, 13)]:
    house(hx, hy)
for tx, ty in [(12, 5), (16, 6), (21, 6), (29, 6), (35, 6), (41, 6), (45, 6),
              (14, 8), (33, 12), (44, 13), (5, 24), (58, 17), (7, 30)]:
    tree(tx, ty)

# ----- small reservoir pond in the near corner -----
pond_base  = c.color("#6f9fae")
pond_light = c.color("#a8d2de")
pond_lite  = c.color("#d2eef2")
c.circle(9, 55, 5, pond_base)
c.circle(9, 55, 3, pond_light)
c.set(7, 53, pond_lite); c.set(11, 56, pond_lite)

# ----- harvest sheaves (drying bundles) -----
sheaf = c.color("#e8ca80")
for sx, sy in [(13, 34), (14, 35), (26, 45), (27, 46), (41, 41), (42, 42),
              (18, 50), (49, 37), (36, 23), (20, 43)]:
    c.set(sx, sy, sheaf)

# ----- two farmers standing on narrow ridges -----
hat   = c.color("#eccd7c"); brim = c.color("#dfb45c")
shirt1 = c.color("#f2eee0"); shirt2 = c.color("#e8a04a")
pants = c.color("#34363e"); bask  = c.color("#8a5630"); fsh = c.color("#5e4224")

def frac(x, y):
    hh = hh_at(x, y)
    return hh / SP - int(hh / SP)

def find_ridge_row(fx, y0, y1):
    for fy in range(y0, y1):
        if frac(fx, fy) < 0.20:
            return fy
    return None

def farmer(fx, fy, shirt, basket=False):
    c.set(fx, fy - 3, hat)
    c.rect(fx - 1, fy - 2, 3, 1, brim)
    c.set(fx, fy - 1, shirt)
    if basket:
        c.set(fx + 1, fy - 1, bask)
    c.set(fx, fy, pants)
    c.set(fx, fy + 1, fsh)

fy1 = find_ridge_row(30, 34, 54)
fy2 = find_ridge_row(47, 40, 58)
if fy1 is not None:
    farmer(30, fy1, shirt1, True)
if fy2 is not None:
    farmer(47, fy2, shirt2, False)
print("farmer rows:", fy1, fy2)

print(c.stats_text())
finish(c)
