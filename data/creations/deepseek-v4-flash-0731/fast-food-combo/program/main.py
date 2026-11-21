from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="combo")

OUT = "#1c1410"
BG = "#2b2620"
TRAY_RIM = "#c8b892"
TRAY_RIM_D = "#bba97f"
TRAY_SFC = "#efe5cc"
TRAY_SHAD = "#d5c6a2"
BUN = "#e8a84c"
BUN_D = "#c98d3a"
SESAME = "#fdf0cd"
LET = "#5fae3a"
LET_D = "#438a28"
CHE = "#ffcf3f"
PATTY = "#7a4a22"
FRY = "#eab047"
FRY_L = "#ffd878"
FRY_D = "#c98f2e"
CARTON = "#d5372a"
CARTON_D = "#b52a1a"
CARTON_IN = "#8f1f12"
NUG = "#d99a45"
NUG_L = "#f0b95e"
NUG_D = "#a8712a"
CUP = "#f4f2ee"
CUP_D = "#cfc9c0"
RED = "#e02f2a"
COLA = "#4e2a12"
COLA_L = "#6b3a1c"
ICE = "#d6ecf7"
ICE_D = "#a9cfe0"
KET = "#c22323"
KET_D = "#8f1515"
MUST = "#e8b324"
MUST_D = "#b88a17"
RANCH = "#fdf3d8"
RANCH_D = "#e0cfa4"
STRAW_L = "#f9c9c0"


def rrect(x0, y0, x1, y1, r):
    return f"M{x0+r},{y0} H{x1-r} Q{x1},{y0} {x1},{y0+r} V{y1-r} Q{x1},{y1} {x1-r},{y1} H{x0+r} Q{x0},{y1} {x0},{y1-r} V{y0+r} Q{x0},{y0} {x0+r},{y0} Z"


def shad(cx, cy, rx, ry):
    c.ellipse(cx + 2, cy + 2, rx, ry, TRAY_SHAD)


# --- base + tray ---
c.rect(0, 0, W, H, BG)
c.path(rrect(3, 3, 60, 60, 6), TRAY_RIM)
c.path(rrect(3, 3, 60, 60, 6), OUT, fill=False)
c.path(rrect(6, 6, 57, 57, 5), TRAY_SFC)
c.path(rrect(6, 6, 57, 57, 5), TRAY_RIM_D, fill=False)

# --- fries carton ---
cx, cy = 13, 18
shad(cx, cy, 9, 9)
c.poly([(6, 9), (20, 9), (18, 31), (8, 31)], CARTON)
c.poly([(6, 9), (20, 9), (18, 31), (8, 31)], OUT, fill=False)
c.poly([(9, 11), (17, 11), (16, 25), (10, 25)], CARTON_IN)
for (sx, top, w, h) in [(7, 7, 3, 18), (11, 5, 4, 19), (15, 8, 3, 17), (9, 11, 4, 14), (13, 9, 3, 16)]:
    c.rect(sx - 1, top - 1, w + 2, h + 2, OUT)
    c.rect(sx, top, w, h, FRY)
    c.rect(sx, top, w, 2, FRY_L)
c.poly([(7, 23), (19, 23), (18, 31), (8, 31)], CARTON)
c.poly([(7, 23), (19, 23), (18, 31), (8, 31)], OUT, fill=False)
c.line(11, 24, 10, 31, CARTON_D)
c.line(15, 24, 16, 31, CARTON_D)
c.rect(11, 6, 4, 2, FRY_L)

# --- cheeseburger ---
bx, by = 43, 19
shad(bx, by, 10, 9)
c.ellipse(bx, by, 10, 9, OUT)
c.ellipse(bx, by + 1, 9, 8, PATTY)
c.ellipse(bx, by, 9, 7, CHE)
c.ellipse(bx, by, 9, 6, LET)
c.ellipse(bx, by - 1, 10, 7, BUN)
c.ellipse(bx, by + 3, 8, 3, BUN_D)
for (dx, dy) in [(-5, 5), (-1, 7), (3, 6), (6, 4)]:
    c.circle(bx + dx, by + dy, 2, CHE)
for (dx, dy) in [(-5, -4), (0, -6), (4, -3), (5, 0), (-2, -1), (2, 1), (-4, 1)]:
    c.set(bx + dx, by + dy, SESAME)
    c.set(bx + dx + 1, by + dy, SESAME)
for (dx, dy) in [(-8, 0), (-5, 6), (2, 7), (7, 3)]:
    c.set(bx + dx, by + dy, LET_D)

# --- nuggets ---
for (nx, ny) in [(10, 42), (15, 38), (19, 44), (12, 48), (17, 51)]:
    shad(nx, ny, 4, 3)
    c.ellipse(nx, ny, 4, 3, OUT)
    c.ellipse(nx, ny, 3, 2, NUG)
    c.ellipse(nx, ny - 1, 2, 1, NUG_L)
    c.set(nx - 1, ny + 1, NUG_D)
    c.set(nx + 1, ny + 1, NUG_D)

# --- cola cup ---
ccx, ccy = 49, 45
shad(ccx, ccy, 9, 8)
c.path(rrect(ccx - 8, ccy - 6, ccx + 7, ccy + 10, 4), CUP)
c.path(rrect(ccx - 8, ccy - 6, ccx + 7, ccy + 10, 4), OUT, fill=False)
c.rect(ccx - 8, ccy + 3, 16, 3, RED)
c.ellipse(ccx, ccy - 3, 9, 6, OUT)
c.ellipse(ccx, ccy - 3, 8, 5, COLA)
c.ellipse(ccx + 2, ccy - 5, 3, 2, COLA_L)
for (ix, iy, iw, ih) in [(ccx - 5, ccy - 6, 4, 3), (ccx - 1, ccy - 6, 4, 3), (ccx + 2, ccy - 4, 4, 3)]:
    c.rect(ix - 1, iy - 1, iw + 2, ih + 2, OUT)
    c.rect(ix, iy, iw, ih, ICE_D)
    c.rect(ix, iy, iw, 1, ICE)
c.set(ccx - 1, ccy - 1, ICE_D)
c.set(ccx + 2, ccy - 1, ICE_D)
c.rect(ccx + 7, ccy - 22, 2, 13, STRAW_L)
c.line(ccx + 8, ccy - 24, ccx + 8, ccy - 12, RED)
c.rect(ccx + 6, ccy - 24, 3, 3, RED)
c.line(ccx + 8, ccy - 6, ccx + 6, ccy - 2, RED)
c.line(ccx + 9, ccy - 6, ccx + 7, ccy - 2, STRAW_L)
c.rect(ccx + 7, ccy - 4, 3, 4, RED)

# --- sauce cups ---
def sauce_cup(sx, sy, col, cold):
    shad(sx, sy, 4, 4)
    c.circle(sx, sy, 4, OUT)
    c.circle(sx, sy, 3, col)
    c.circle(sx, sy, 2, cold)
    c.set(sx - 1, sy - 2, col)
    c.set(sx + 1, sy, col)

sauce_cup(24, 31, KET, KET_D)
sauce_cup(30, 38, MUST, MUST_D)
sauce_cup(17, 53, RANCH, RANCH_D)

print(c.stats_text())
print(c.matrix_text())
finish(c)
