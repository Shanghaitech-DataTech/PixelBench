from pixelbench_api import *

c = new_canvas(64, 64)

def col(h):
    return c.color(h)

OUT   = col("#241d18")
TRAY  = col("#e2d3a5")
TRAYD = col("#c9b88a")
HIL   = col("#f2e8c8")
SHAD  = col("#b0a172")

def rr(x, y, w, h, r, color):
    c.rect(x + r, y, w - 2 * r, h, color)
    c.rect(x, y + r, w, h - 2 * r, color)
    c.circle(x + r, y + r, r, color)
    c.circle(x + w - 1 - r, y + r, r, color)
    c.circle(x + r, y + h - 1 - r, r, color)
    c.circle(x + w - 1 - r, y + h - 1 - r, r, color)

# ---- tray ---------------------------------------------------------------
rr(1, 1, 62, 62, 5, OUT)
rr(2, 2, 60, 60, 5, TRAY)
c.rect(2, 2, 60, 1, TRAYD)
c.rect(2, 2, 1, 60, TRAYD)
c.rect(3, 60, 58, 1, HIL)
c.rect(60, 3, 1, 58, HIL)

# ---- shadows ------------------------------------------------------------
c.ellipse(17, 41, 14, 8, SHAD)
c.ellipse(46, 43, 12, 7, SHAD)
c.ellipse(51, 51, 8, 7, SHAD)
c.ellipse(24, 45, 4, 3, SHAD)
c.ellipse(31, 43, 4, 3, SHAD)
c.ellipse(28, 51, 4, 3, SHAD)
c.ellipse(35, 48, 4, 3, SHAD)
c.circle(9, 53, 5, SHAD)
c.circle(16, 57, 5, SHAD)

# ---- burger -------------------------------------------------------------
BUN   = col("#e9a23d"); BUNH  = col("#f4b95f"); BUNB  = col("#d98f2d")
SEED  = col("#f6e3b0"); LETT  = col("#6fae3d"); LETTD = col("#4f8f2e")
CHEESE = col("#f2b31c"); CHEESEL = col("#f9c93f")
PATTY  = col("#7a4522"); PATTYD = col("#5f3418")

# bottom bun
c.ellipse(17, 40, 15, 8, OUT)
c.ellipse(17, 40, 14, 7, BUNB)
# patty
c.ellipse(17, 36, 14, 8, OUT)
c.ellipse(17, 36, 13, 7, PATTY)
for (px, py) in [(13, 35), (17, 38), (20, 34), (15, 39), (19, 33)]:
    c.set(px, py, PATTYD)
# melted cheese
c.ellipse(17, 32, 14, 8, OUT)
c.ellipse(17, 32, 13, 7, CHEESE)
c.ellipse(17, 29, 6, 2, CHEESEL)
for (dx, dy) in [(13, 38), (18, 40), (22, 38)]:
    c.circle(dx, dy, 3, OUT)
    c.circle(dx, dy, 2, CHEESE)
    c.set(dx, dy - 1, CHEESEL)
c.rect(21, 34, 4, 7, OUT)
c.rect(22, 35, 2, 5, CHEESE)
c.rect(22, 35, 2, 1, CHEESEL)
# lettuce
c.ellipse(17, 28, 14, 7, OUT)
c.ellipse(17, 28, 13, 6, LETT)
for (dx, dy) in [(8, 27), (12, 30), (17, 31), (22, 30), (26, 27)]:
    c.circle(dx, dy, 3, OUT)
    c.circle(dx, dy, 2, LETT)
    c.set(dx, dy - 1, LETTD)
# top bun
c.ellipse(17, 23, 12, 7, OUT)
c.ellipse(17, 23, 11, 6, BUN)
c.ellipse(17, 21, 6, 4, BUNH)
for (sx, sy) in [(12, 22), (15, 19), (18, 18), (21, 20), (23, 23),
                (13, 25), (16, 26), (19, 23), (14, 21), (19, 26)]:
    c.set(sx, sy, SEED)

# ---- carton --------------------------------------------------------------
CART  = col("#ce3128"); CARTRD = col("#a8201c"); CARTL = col("#e04a3e")
c.poly([(32, 22), (52, 22), (49, 42), (35, 42)], OUT)
c.poly([(34, 23), (50, 23), (47, 41), (37, 41)], CART)
c.poly([(34, 23), (39, 23), (41, 41), (37, 41)], CARTRD)
c.rect(35, 26, 15, 2, CARTL)

# ---- fries pile ----------------------------------------------------------
FRY  = col("#eeb63f"); FRYD = col("#c98a2e"); FRYL = col("#f8d574")
c.ellipse(44, 15, 11, 10, OUT)
c.ellipse(44, 14, 10, 9, FRYD)
for (fx, fy, fw, fh) in [(37, 8, 3, 15), (41, 6, 3, 17), (45, 7, 3, 16),
                         (49, 9, 3, 14), (38, 5, 3, 17), (43, 9, 3, 14),
                         (47, 5, 3, 18), (36, 10, 3, 13), (51, 8, 3, 15),
                         (40, 7, 3, 15), (44, 5, 3, 18)]:
    c.rect(fx, fy, fw, 2, FRYL)
    c.rect(fx, fy + 2, fw, fh - 2, FRY)

# ---- nuggets -------------------------------------------------------------
NUG  = col("#d29a3c"); NUGL = col("#e8b55a"); NUGD = col("#a97424")
for (cx, cy) in [(24, 44), (31, 42), (28, 50), (35, 47)]:
    c.ellipse(cx, cy, 4, 3, OUT)
    c.ellipse(cx, cy, 3, 2, NUG)
    c.ellipse(cx, cy - 1, 2, 1, NUGL)
    c.set(cx + 1, cy + 1, NUGD)

# ---- sauce cups -----------------------------------------------------------
CUPW = col("#f0e9da"); KTCH = col("#c9261f"); KTCHL = col("#e0553a")
BBQ  = col("#8a4a1c"); BBQL = col("#a5612a")
for (cx, cy, inner, lite) in [(9, 52, KTCH, KTCHL), (16, 56, BBQ, BBQL)]:
    c.circle(cx, cy, 4, OUT)
    c.circle(cx, cy, 3, CUPW)
    c.circle(cx, cy, 2, inner)
    c.set(cx - 1, cy - 1, lite)

# ---- cola cup ------------------------------------------------------------
COLA = col("#3f2416"); ICE  = col("#d6edf6"); ICE_D = col("#a9cfe0")
STRAW = col("#e03939"); STRAWW = col("#f2e6d8")
CUP  = col("#c42b26")
c.ellipse(51, 49, 8, 7, OUT)
c.ellipse(51, 48, 7, 6, CUP)
c.ellipse(51, 47, 5, 5, COLA)
c.rect(45, 46, 13, 2, CUPW)
for (ix, iy) in [(46, 45), (51, 44), (48, 49)]:
    c.rect(ix, iy, 3, 3, ICE)
    c.set(ix + 2, iy, ICE_D)
    c.set(ix, iy + 2, ICE_D)
for off in [(-1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]:
    c.line(38 + off[0], 27 + off[1], 46 + off[0], 43 + off[1], OUT)
c.line(38, 27, 46, 43, STRAW)
c.rect(42, 37, 1, 2, STRAWW)

# ---- extra crumbs / dipping fry --------------------------------------------
for (sx, sy) in [(20, 51), (22, 54), (25, 56)]:
    c.set(sx, sy, SEED)
c.rect(5, 49, 9, 3, OUT)
c.rect(6, 50, 7, 2, FRY)
c.rect(6, 49, 7, 1, FRYL)

print(c.stats_text())
finish(c)
