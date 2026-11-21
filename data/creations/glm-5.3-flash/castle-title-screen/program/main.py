# ============================================================
#  EMBERFALL - fantasy RPG title screen, 128x128
#  Castle on a seaside cliff, sunset, two flagged towers,
#  large orange sun, layered clouds, dark foreground rocks.
# ============================================================
W = H = 128
HORIZON = 80

c = new_canvas(W, H, None, "castle-title")

# ---------------- palette ----------------
S1, S2, S3, S4, S5, S6, S7 = "#221440", "#3b1f56", "#5e2a5a", "#8f354c", "#c14a34", "#e8702a", "#f79c33"
HOR = "#ffc251"
SUN_E, SUN_M, SUN_C = "#ff9d3a", "#ffc85c", "#ffe9a8"
CL_D, CL_M, CL_L, CL_B, CL_G = "#2b1a42", "#4e2650", "#83394b", "#c55534", "#ef8f3e"
SEA1, SEA2, SEA3, SEA4, SEA5 = "#dd7c33", "#a85438", "#6e3a44", "#452a4a", "#2a1e3c"
GL1, GL2 = "#ffd98a", "#ffab4a"
RK_D, RK_M, RK_L, RK_E = "#1b1226", "#2e1c32", "#4a2c3e", "#6b4044"
CA_D, CA_M, CA_L, CA_E = "#241828", "#3a2636", "#5c3a44", "#7d5252"
RF, RF_L = "#7a2833", "#b04a44"
FL, FL_D = "#d63c46", "#8e2434"
FG1, FG2 = "#0d0914", "#191022"
T_GOLD, T_SH, T_W = "#ffd878", "#14091c", "#f2e8d0"

# ---------------- helpers ----------------
def dash(y, x0, x1, col, gap=None):
    if gap is None:
        c.rect(x0, y, x1 - x0 + 1, 1, col)
    else:
        c.rect(x0, y, gap - x0, 1, col)
        c.rect(gap + 2, y, x1 - gap - 1, 1, col)

def bird(bx, by, col):
    c.set(bx - 2, by - 1, col)
    c.set(bx - 1, by, col)
    c.set(bx, by, col)
    c.set(bx + 1, by, col)
    c.set(bx + 2, by - 1, col)

# ---------------- sky gradient ----------------
sky = [(0, S1), (12, S2), (24, S3), (36, S4), (48, S5), (60, S6), (71, S7)]
for i, (y0, col) in enumerate(sky):
    y1 = sky[i + 1][0] if i + 1 < len(sky) else HORIZON
    c.rect(0, y0, W, y1 - y0, col)
    if i + 1 < len(sky):
        c.dither(0, y1 - 2, W, 3, [col, sky[i + 1][1]])

# ---------------- large orange sun ----------------
SX, SY, SR = 44, HORIZON, 20
for y in range(SY - 30, HORIZON):
    for x in range(SX - 30, SX + 31):
        d = ((x - SX) ** 2 + (y - SY) ** 2) ** 0.5
        if d <= 26:
            c.set(x, y, HOR)
        elif d <= 29 and (x + y) % 2 == 0:
            c.set(x, y, HOR)
c.circle(SX, SY, SR, SUN_E)
c.circle(SX, SY, 17, SUN_M)
c.circle(SX, SY, 13, SUN_C)
for y in range(SY - SR - 1, HORIZON):
    for x in range(SX - SR - 1, SX + SR + 2):
        d = ((x - SX) ** 2 + (y - SY) ** 2) ** 0.5
        if 17 < d <= 20 and (x + y) % 2 == 0:
            c.set(x, y, SUN_M)
        elif 13 < d <= 15 and (x + y) % 2 == 0:
            c.set(x, y, SUN_C)

# ---------------- layered clouds ----------------
# high, cold silhouettes
c.ellipse(28, 12, 20, 3, CL_D)
c.ellipse(70, 9, 14, 2, CL_D)
c.ellipse(104, 15, 22, 3, CL_D)
c.ellipse(52, 18, 12, 2, CL_D)
c.ellipse(16, 20, 9, 2, CL_D)
# mid band
c.ellipse(20, 32, 18, 4, CL_M)
c.ellipse(96, 30, 20, 4, CL_M)
c.ellipse(58, 40, 24, 3, CL_M)
c.ellipse(20, 35, 16, 2, CL_L)
c.ellipse(96, 33, 18, 2, CL_L)
c.ellipse(58, 42, 22, 2, CL_L)
# low bright band crossing the sun
c.ellipse(44, 56, 26, 3, CL_B)
c.ellipse(16, 60, 16, 3, CL_B)
c.ellipse(104, 54, 20, 3, CL_B)
c.ellipse(44, 58, 24, 2, CL_G)
c.ellipse(104, 56, 18, 2, CL_G)
c.ellipse(74, 62, 14, 2, CL_G)
# thin horizon streaks
c.ellipse(18, 73, 14, 1, CL_G)
c.ellipse(72, 75, 20, 1, CL_G)
c.ellipse(112, 72, 14, 1, CL_B)

# birds
bird(30, 38, CL_D)
bird(42, 31, CL_D)
bird(22, 45, CL_D)

# ---------------- sea ----------------
sea = [(80, HOR), (83, SEA1), (88, SEA2), (95, SEA3), (102, SEA4), (109, SEA5)]
for i, (y0, col) in enumerate(sea):
    y1 = sea[i + 1][0] if i + 1 < len(sea) else H
    c.rect(0, y0, W, y1 - y0, col)
    if i + 1 < len(sea):
        c.dither(0, y1 - 2, W, 3, [col, sea[i + 1][1]])

# sun reflection column
dash(81, 34, 54, HOR)
dash(83, 37, 51, GL1, 44)
dash(85, 33, 55, GL2, 42)
dash(87, 38, 50, GL1, 45)
dash(89, 32, 54, GL2, 40)
dash(91, 39, 49, GL1, 45)
dash(93, 35, 53, GL2, 43)
dash(96, 40, 48, GL2, 44)
dash(99, 37, 51, GL2, 45)
dash(102, 41, 47, SUN_E)

# wave texture
dash(86, 4, 20, SEA2);  dash(86, 62, 74, SEA2)
dash(90, 8, 24, SEA3);  dash(90, 58, 70, SEA3)
dash(94, 2, 18, SEA3)
dash(97, 12, 30, SEA4); dash(97, 60, 72, SEA4)
dash(100, 4, 22, SEA4)
dash(105, 10, 26, SEA5); dash(105, 56, 68, SEA5)
dash(110, 2, 20, SEA5)

# ---------------- distant sea stack (left) ----------------
c.poly([(3, 82), (5, 71), (8, 68), (11, 72), (13, 82)], RK_D)
c.line(8, 68, 11, 72, RK_L)
c.line(11, 72, 13, 80, RK_L)

# ---------------- seaside cliff ----------------
cliff = [(70, 127), (74, 112), (71, 104), (78, 96), (75, 88), (83, 80),
         (80, 72), (88, 64), (86, 58), (94, 56), (127, 56), (127, 127)]
c.rect(70, 127, 58, 1, RK_D)  # ensure the bottom row is filled
c.poly(cliff, RK_D)
c.line(71, 104, 78, 96, RK_L)
c.line(78, 96, 75, 88, RK_L)
c.line(75, 88, 83, 80, RK_L)
c.line(80, 72, 88, 64, RK_M)
c.line(86, 58, 94, 56, RK_E)
# strata
c.rect(88, 84, 14, 1, RK_M)
c.rect(84, 92, 18, 1, RK_M)
c.rect(90, 104, 24, 1, RK_M)
c.rect(96, 116, 28, 1, RK_M)
c.rect(100, 124, 26, 1, RK_M)

# ---------------- castle ----------------
# curtain wall
c.rect(90, 48, 38, 12, CA_D)
for mx in range(90, 127, 4):
    c.rect(mx, 45, 2, 3, CA_D)
# central keep
c.rect(100, 40, 14, 10, CA_D)
c.poly([(98, 41), (115, 41), (106, 31)], RF)
c.line(98, 41, 106, 31, RF_L)
# left (tall) tower
c.rect(90, 26, 11, 24, CA_D)
c.poly([(88, 27), (102, 27), (95, 15)], RF)
c.line(88, 27, 95, 15, RF_L)
c.rect(95, 4, 1, 12, CA_M)
c.poly([(95, 9), (86, 12), (95, 15)], FL)
c.line(95, 15, 90, 13, FL_D)
# right (short) tower
c.rect(114, 34, 11, 16, CA_D)
c.poly([(112, 35), (126, 35), (119, 24)], RF)
c.line(112, 35, 119, 24, RF_L)
c.rect(119, 13, 1, 12, CA_M)
c.poly([(119, 18), (111, 21), (119, 24)], FL)
c.line(119, 24, 114, 22, FL_D)
# lit edges facing the sun
c.rect(90, 26, 1, 23, CA_L)
c.rect(90, 48, 1, 11, CA_M)
c.rect(100, 40, 1, 9, CA_M)
c.rect(114, 34, 1, 15, CA_M)
for mx in range(90, 127, 4):
    c.rect(mx, 45, 2, 1, CA_M)
c.set(90, 26, CA_E); c.set(91, 26, CA_E)
c.set(90, 45, CA_E); c.set(100, 40, CA_E); c.set(114, 34, CA_E)
# glowing windows
for wx, wy in [(93, 31), (96, 37), (93, 42), (117, 39), (121, 43), (104, 44), (109, 44)]:
    c.rect(wx, wy, 1, 2, HOR)
# gate arch
c.rect(105, 53, 6, 6, HOR)
c.rect(106, 52, 4, 1, HOR)

# ---------------- foreground rocks ----------------
lm = [(0, 127), (0, 104), (5, 100), (11, 104), (17, 98), (24, 103),
      (31, 99), (38, 104), (46, 108), (54, 113), (60, 127)]
c.rect(0, 127, 61, 1, FG1)  # ensure the bottom row is filled
c.poly(lm, FG1)
c.line(0, 104, 5, 100, RK_L)
c.line(5, 100, 11, 104, FG2)
c.line(11, 104, 17, 98, RK_L)
c.line(17, 98, 24, 103, FG2)
c.line(24, 103, 31, 99, RK_L)
c.line(31, 99, 38, 104, FG2)
c.line(38, 104, 46, 108, FG2)
c.line(46, 108, 54, 113, FG2)
rm = [(56, 127), (62, 118), (70, 122), (80, 116), (90, 121), (100, 117),
      (110, 122), (120, 118), (127, 122), (127, 127)]
c.rect(56, 127, 72, 1, FG1)  # ensure the bottom row is filled
c.poly(rm, FG1)
c.line(56, 127, 62, 118, FG2)
c.line(62, 118, 70, 122, FG2)
c.line(70, 122, 80, 116, RK_L)
c.line(80, 116, 90, 121, FG2)
c.line(90, 121, 100, 117, RK_L)
c.line(100, 117, 110, 122, FG2)
c.line(110, 122, 120, 118, FG2)
c.line(120, 118, 128, 122, FG2)
# grass tufts on the near rocks (anchored to the rock edge so none float)
lm_pts = [(0, 104), (5, 100), (11, 104), (17, 98), (24, 103), (31, 99),
          (38, 104), (46, 108), (54, 113), (60, 127)]

def rock_edge_y(px):
    for (ax, ay), (bx, by) in zip(lm_pts, lm_pts[1:]):
        if ax <= px <= bx:
            return round(ay + (px - ax) * (by - ay) / (bx - ax))
    return 128

for gx, hgt in [(8, 6), (14, 5), (20, 6), (27, 5), (33, 6), (44, 5), (50, 4)]:
    ey = rock_edge_y(gx)
    c.rect(gx, ey - hgt, 1, hgt + 2, FG1)
    if hgt >= 5:
        c.rect(gx + 1, ey - hgt + 2, 1, hgt, FG1)

# foam where the cliff meets the water
dash(103, 68, 80, SEA1)
dash(106, 66, 76, SEA1)
dash(109, 70, 82, SEA2)

# ---------------- title ----------------
c.text(38, 4, "EMBERFALL", T_SH, font="5x7")
c.text(37, 3, "EMBERFALL", T_GOLD, font="5x7")
c.rect(44, 12, 15, 1, T_GOLD)
c.rect(69, 12, 15, 1, T_GOLD)
c.set(63, 11, T_GOLD); c.set(62, 12, T_GOLD); c.set(64, 12, T_GOLD); c.set(63, 13, T_GOLD)
c.set(63, 12, T_W)

c.text(31, 118, "PRESS START", T_W, font="5x7")

print(c.stats_text())
finish(c)
