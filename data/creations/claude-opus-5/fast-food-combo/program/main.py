OUT = "#1e1318"
BG = "#2a222e"
WALL = "#372e3c"

TRAY_D = "#8f2b23"
TRAY = "#c3392e"
TRAY_L = "#e76b52"
FLOOR = "#ab3127"
LINER = "#f2e6cb"
LINER_S = "#d8c6a2"

c = new_canvas(64, 64, background=BG, name="output")
c.rect(0, 0, 64, 18, WALL)

# ---------------- tray ----------------
c.poly([(6, 15), (58, 15), (63, 60), (1, 60)], OUT)
c.poly([(8, 17), (56, 17), (61, 58), (3, 58)], TRAY)
c.line(9, 17, 55, 17, TRAY_L)
c.poly([(2, 56), (62, 56), (62, 59), (2, 59)], TRAY_D)
c.poly([(11, 20), (53, 20), (57, 55), (7, 55)], FLOOR)
c.line(11, 20, 53, 20, TRAY_D)
c.poly([(11, 21), (53, 21), (54, 28), (10, 28)], TRAY_D)

# paper liner patch under the nuggets, plus contact shadows
c.poly([(28, 44), (50, 44), (53, 55), (24, 55)], LINER)
c.line(28, 44, 50, 44, LINER_S)
c.line(24, 55, 53, 55, LINER_S)
c.ellipse(16, 56, 12, 2, TRAY_D)
c.ellipse(15, 45, 11, 2, TRAY_D)
c.ellipse(49, 46, 8, 2, TRAY_D)

# ---------------- french fries ----------------
FRY = "#efc158"
FRY_L = "#ffe08c"
FRY_D = "#c08f2c"


def fry(x, y, bot=25):
    c.rect(x - 1, y - 1, 4, bot - y + 2, OUT)
    c.rect(x, y, 2, bot - y + 1, FRY)
    c.rect(x, y, 1, bot - y + 1, FRY_L)
    c.set(x + 1, y, FRY_D)


for fx, fy in [(8, 13), (11, 9), (14, 6), (17, 8), (20, 11), (22, 15),
               (10, 16), (13, 13), (16, 14), (19, 17)]:
    fry(fx, fy)

# loose fries resting on the tray floor
for lx, ly in [(27, 29), (34, 27), (29, 33)]:
    c.rect(lx - 1, ly - 1, 7, 4, OUT)
    c.rect(lx, ly, 5, 2, FRY)
    c.line(lx, ly, lx + 4, ly, FRY_L)

# ---------------- fry carton ----------------
CAR = "#d63c33"
CAR_D = "#9e241c"
CAR_L = "#f2614f"
c.poly([(4, 21), (15, 24), (27, 21), (24, 44), (9, 44)], OUT)
c.poly([(6, 23), (15, 25), (25, 23), (23, 43), (10, 43)], CAR)
c.poly([(19, 24), (25, 23), (23, 43), (19, 43)], CAR_D)
c.poly([(6, 23), (10, 24), (11, 42), (10, 43)], CAR_L)
c.poly([(13, 31), (17, 31), (18, 38), (12, 38)], CAR_L)
c.line(10, 42, 23, 42, CAR_D)

# ---------------- cola cup ----------------
COLA = "#6b3318"
COLA_D = "#43200d"
COLA_L = "#8c4a22"
ICE = "#b4713d"
ICE_L = "#d79a63"
LID = "#eef1f3"
LID_S = "#bcc6cc"
STRAW = "#e2493d"
STRAW_D = "#a52a22"

c.poly([(39, 15), (59, 15), (56, 46), (42, 46)], OUT)
c.poly([(41, 17), (57, 17), (55, 45), (43, 45)], COLA)
c.poly([(52, 17), (57, 17), (55, 45), (52, 45)], COLA_D)
c.rect(44, 21, 2, 21, COLA_L)
for ix, iy, iw, ih in [(46, 19, 5, 4), (51, 21, 4, 4), (45, 25, 5, 4),
                       (50, 29, 4, 4), (46, 34, 5, 4), (50, 38, 4, 3)]:
    c.rect(ix, iy, iw, ih, ICE)
    c.rect(ix, iy, iw - 1, 1, ICE_L)
    c.set(ix, iy + 1, ICE_L)
c.line(43, 44, 54, 44, COLA_D)
# glossy highlight down the cup wall
c.line(42, 19, 43, 43, ICE_L)
c.ellipse(49, 15, 11, 4, OUT)
c.ellipse(49, 15, 10, 3, LID)
c.ellipse(49, 14, 8, 2, LID_S)
c.line(40, 16, 58, 16, LID)
c.line(51, 12, 58, 2, OUT)
c.line(52, 12, 59, 2, OUT)
c.line(53, 12, 60, 2, OUT)
c.line(52, 12, 59, 3, STRAW)
c.line(52, 13, 59, 4, STRAW_D)

# ---------------- dipping sauce cups ----------------
CUP = "#f1ece0"
CUP_S = "#c8bfaa"
SAUCE_R = "#d13a2b"
SAUCE_RL = "#ec7260"
SAUCE_Y = "#e8a93f"
SAUCE_YL = "#f6cf84"


def sauce(cx, cy, col, hi):
    c.ellipse(cx, cy, 5, 4, OUT)
    c.ellipse(cx, cy, 4, 3, CUP)
    c.ellipse(cx, cy + 2, 4, 1, CUP_S)
    c.ellipse(cx, cy - 1, 4, 2, OUT)
    c.ellipse(cx, cy - 1, 3, 1, col)
    c.line(cx - 2, cy - 2, cx, cy - 2, hi)


sauce(33, 34, SAUCE_R, SAUCE_RL)
sauce(51, 50, SAUCE_Y, SAUCE_YL)

# ---------------- chicken nuggets ----------------
NUG = "#e2ab4b"
NUG_L = "#f7cf7c"
NUG_D = "#a97023"


def nugget(cx, cy, rx=6, ry=4):
    c.ellipse(cx, cy, rx + 1, ry + 1, OUT)
    c.ellipse(cx, cy, rx, ry, NUG)
    c.ellipse(cx - 1, cy - 1, rx - 2, ry - 2, NUG_L)
    c.ellipse(cx + 1, cy + ry - 1, rx - 2, 1, NUG_D)
    c.set(cx - rx + 1, cy + 1, NUG_D)
    # crumb speckles
    c.set(cx + 2, cy - 2, NUG_D)
    c.set(cx - 3, cy + 1, NUG_L)
    c.set(cx + rx - 2, cy, NUG_L)


nugget(44, 46, 6, 4)
nugget(32, 50, 6, 4)
nugget(42, 54, 6, 4)

# ---------------- cheeseburger ----------------
BUNB = "#c2823f"
BUNB_D = "#9a6128"
PAT = "#6e3b22"
PAT_D = "#4a2414"
CHZ = "#f6b53c"
CHZ_D = "#d2882a"
LET = "#71b03d"
LET_D = "#4b7d25"
BUN = "#dc9c51"
BUN_L = "#f0bf79"
BUN_D = "#b1753a"
SES = "#fbecc3"

# bottom bun
c.ellipse(16, 54, 12, 3, OUT)
c.ellipse(16, 54, 11, 2, BUNB)
c.line(6, 55, 26, 55, BUNB_D)
# patty
c.ellipse(16, 51, 13, 3, OUT)
c.ellipse(16, 51, 12, 2, PAT)
c.line(5, 52, 27, 52, PAT_D)
c.line(6, 53, 26, 53, PAT_D)
# cheese
c.ellipse(16, 48, 14, 2, OUT)
c.ellipse(16, 48, 13, 1, CHZ)
for dx in (-12, -6, 3, 10):
    c.rect(16 + dx, 49, 3, 4, OUT)
    c.rect(16 + dx, 49, 2, 3, CHZ)
    c.set(16 + dx + 1, 51, CHZ_D)
c.line(4, 49, 28, 49, CHZ)
c.line(5, 50, 27, 50, CHZ_D)
# lettuce
c.ellipse(16, 45, 14, 2, OUT)
c.ellipse(16, 45, 13, 1, LET)
for dx, dd in [(-12, 1), (-9, 2), (-6, 1), (-3, 2), (0, 1), (3, 2),
               (6, 1), (9, 2), (12, 1)]:
    c.ellipse(16 + dx, 45 + dd, 1, 1, OUT)
    c.set(16 + dx, 45 + dd, LET)
    c.set(16 + dx, 46 + dd, LET_D)
c.line(4, 45, 28, 45, LET)
c.line(5, 46, 27, 46, LET_D)
# top bun
c.ellipse(16, 38, 11, 6, OUT)
c.ellipse(16, 38, 10, 5, BUN)
c.ellipse(14, 36, 6, 3, BUN_L)
c.line(7, 42, 25, 42, BUN_D)
c.line(9, 43, 23, 43, BUN_D)
for sx, sy in [(11, 34), (17, 33), (21, 36), (9, 38), (14, 37), (19, 39),
               (12, 40), (22, 40), (16, 41)]:
    c.set(sx, sy, SES)
    c.set(sx + 1, sy, SES)

view(c)
print(c.stats_text())
save("combo", c)
finish(c)

