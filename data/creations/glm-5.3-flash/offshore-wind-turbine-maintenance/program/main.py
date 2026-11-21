"""Offshore wind turbine maintenance platform - 64x64 pixel art."""

import random

W = H = 64

# ------------------------------------------------------------------ palette
SKY_TOP   = "#4E9CD8"
SKY_MID   = "#6FB6E8"
SKY_LOW   = "#9CD4F4"
SKY_HAZE  = "#C6E6F8"
CLOUD     = "#FFFFFF"
CLOUD_SH  = "#D8E9F5"
SUN       = "#FFE9A8"
SUN_CORE  = "#FFF7DC"
BIRD      = "#3A5A74"

SEA_HAZE  = "#A9D6EE"
SEA_FAR   = "#6FA3CC"
SEA_MID   = "#4A86B8"
SEA_NEAR  = "#2E6BA4"
SEA_DEEP  = "#22558C"
WAVE_LT   = "#5E9CCB"
WAVE_DK   = "#1E4E80"
FOAM      = "#EAF6FD"
FOAM_SH   = "#BFDDEC"
GLITTER   = "#8FC6E8"

STEEL_HI   = "#DCE4EA"
STEEL_LT   = "#C9D4DC"
STEEL_MID  = "#9FAEB9"
STEEL_DK   = "#6E7E8C"
STEEL_EDGE = "#4E5D6B"
STEEL_DARK = "#39434E"
BLADE      = "#E4EBF1"
BLADE_SH   = "#A8B8C6"
YELL       = "#F2C230"
YELL_DK    = "#C0941C"
VEST       = "#FF8A1E"
VEST_SH    = "#D96E10"
HELMET     = "#F5F7F9"
SKIN       = "#E8B48C"
GLOVE      = "#DDE3E8"
NAVY       = "#2E4460"
BOOT       = "#1E2A38"
DIST_NEAR  = "#7BA6C4"
DIST_FAR   = "#9CBFD6"

c = new_canvas(W, H, name="offshore-maintenance")

# ---------------------------------------------------------------------- sky
for y0, y1, col in ((0, 7, SKY_TOP), (8, 15, SKY_MID), (16, 23, SKY_LOW),
                    (24, 31, SKY_HAZE)):
    c.rect(0, y0, W, y1 - y0 + 1, col)

c.circle(6, 6, 3, SUN)
c.circle(6, 6, 1, SUN_CORE)


def cloud(spans):
    n = len(spans)
    for i, (y, x0, x1) in enumerate(spans):
        c.rect(x0, y, x1 - x0 + 1, 1, CLOUD_SH if i == n - 1 else CLOUD)


cloud([(5, 46, 53), (6, 43, 55), (7, 42, 56), (8, 45, 53)])
cloud([(16, 34, 41), (17, 32, 43), (18, 33, 42), (19, 36, 39)])
cloud([(25, 2, 10), (26, 0, 12), (27, 1, 11), (28, 3, 9)])

for bx, by in ((14, 20), (18, 23)):
    c.set(bx, by, BIRD)
    c.set(bx + 1, by - 1, BIRD)
    c.set(bx + 2, by, BIRD)

# ---------------------------------------------------------------------- sea
for y0, y1, col in ((32, 33, SEA_HAZE), (34, 36, SEA_FAR), (37, 43, SEA_MID),
                    (44, 54, SEA_NEAR), (55, 63, SEA_DEEP)):
    c.rect(0, y0, W, y1 - y0 + 1, col)

rnd = random.Random(7)
BANDS = ((34, 37, 2, 2, 3, (WAVE_LT, SEA_MID)),
         (37, 44, 2, 3, 5, (WAVE_LT, SEA_NEAR)),
         (44, 55, 3, 4, 7, (WAVE_LT, WAVE_DK)),
         (55, 64, 2, 5, 9, (WAVE_LT, WAVE_DK, SEA_DEEP)))
for y0, y1, n, l0, l1, cols in BANDS:
    for y in range(y0, y1):
        for _ in range(n):
            x = rnd.randrange(0, 60)
            ln = rnd.randrange(l0, l1 + 1)
            c.rect(x, y, min(ln, W - x), 1, rnd.choice(cols))

for y, x0, x1 in ((35, 3, 6), (38, 2, 5), (41, 4, 8), (44, 2, 6),
                  (47, 3, 7), (50, 2, 6)):
    c.rect(x0, y, x1 - x0 + 1, 1, GLITTER)

# ---------------------------------------------------------- distant turbines
def distant(cx, base_y, h, col):
    top = base_y - h
    c.line(cx, base_y, cx, top, col)
    hx, hy = cx + 1, top
    c.set(hx, hy, col)
    L = max(3, h // 3)
    c.line(hx, hy, hx, hy - L, col)
    c.line(hx, hy, hx + L, hy + L // 2, col)
    c.line(hx, hy, hx - L, hy + L // 2, col)


distant(46, 36, 13, DIST_NEAR)
distant(57, 34, 8, DIST_FAR)
for x, y in ((45, 37), (46, 37), (47, 37), (46, 38), (56, 35), (57, 35),
             (58, 35), (57, 36)):
    c.set(x, y, GLITTER)

# --------------------------------------------------------------- main tower
def tower_x(y):
    h = 2.3 + (y - 14) * 3.0 / 38.0
    return round(25.5 - h), round(25.5 + h)


def steel_row(x0, x1):
    w = x1 - x0 + 1
    if w <= 3:
        return [STEEL_LT, STEEL_MID, STEEL_EDGE][:w]
    if w == 4:
        return [STEEL_LT, STEEL_MID, STEEL_DK, STEEL_EDGE]
    n_dk = max(2, w // 4)
    n_mid = w - 3 - n_dk
    return ([STEEL_HI, STEEL_LT] + [STEEL_MID] * n_mid
            + [STEEL_DK] * n_dk + [STEEL_EDGE])


for y in range(14, 53):
    x0, x1 = tower_x(y)
    for i, col in enumerate(steel_row(x0, x1)):
        c.set(x0 + i, y, col)

for fy in (21, 30, 39, 47):
    x0, x1 = tower_x(fy)
    c.set(x0 - 1, fy, STEEL_MID)
    c.set(x1 + 1, fy, STEEL_MID)
    for x in range(x0, x1 + 1):
        c.set(x, fy, STEEL_DK)
    c.set(x0, fy, STEEL_EDGE)
    c.set(x1, fy, STEEL_EDGE)

# ------------------------------------------------- rotor (behind the hub) ---
c.poly([(28, 9), (30, 11), (41, 4)], BLADE)
c.poly([(30, 9), (28, 11), (18, 4)], BLADE)
c.poly([(29, 10), (32, 10), (30, 22)], BLADE)
c.line(30, 11, 41, 4, BLADE_SH)
c.line(28, 11, 18, 4, BLADE_SH)
c.line(31, 10, 30, 21, BLADE_SH)

# ---------------------------------------------------------------- nacelle --
c.rect(23, 8, 6, 1, STEEL_LT)
c.rect(22, 9, 9, 4, STEEL_MID)
c.rect(22, 9, 1, 4, STEEL_LT)
c.rect(30, 9, 1, 4, STEEL_DK)
c.rect(22, 13, 9, 1, STEEL_DK)

c.circle(30, 10, 2, STEEL_LT)
c.set(29, 8, STEEL_LT)
c.set(32, 9, STEEL_DK)
c.set(32, 10, STEEL_DK)
c.set(32, 11, STEEL_DK)
c.set(31, 8, STEEL_MID)
c.set(31, 12, STEEL_MID)
c.set(30, 10, STEEL_MID)
c.set(27, 7, VEST)            # aviation beacon on the roof

# ----------------------------------------------------------------- ladder --
c.rect(24, 18, 1, 34, STEEL_EDGE)
c.rect(27, 18, 1, 34, STEEL_EDGE)
for ry in (20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50):
    c.rect(25, ry, 2, 1, STEEL_DK)

# --------------------------------------------------- technician climbing ---
c.set(25, 22, HELMET)
c.set(26, 22, HELMET)
c.set(25, 23, SKIN)
c.set(26, 23, SKIN)
c.set(24, 23, GLOVE)          # left hand on the rail
c.set(25, 24, VEST)
c.set(26, 24, VEST)
c.set(27, 24, GLOVE)          # right hand on the rail
c.set(25, 25, VEST)
c.set(26, 25, VEST)
c.set(25, 26, VEST_SH)
c.set(26, 26, VEST_SH)
c.set(25, 27, NAVY)
c.set(26, 27, NAVY)
c.set(25, 28, NAVY)
c.set(26, 28, NAVY)
c.set(25, 29, BOOT)           # left foot on a rung
c.set(26, 29, NAVY)
c.set(26, 30, NAVY)
c.set(26, 31, NAVY)
c.set(26, 32, BOOT)           # right foot on the rung below

# ------------------------------------------------------------------ deck ---
c.rect(10, 44, 31, 1, STEEL_LT)
c.rect(10, 45, 31, 1, STEEL_MID)
c.rect(10, 46, 31, 1, STEEL_EDGE)
for x in range(13, 40, 4):
    c.set(x, 44, STEEL_MID)

# under-deck legs and braces
c.rect(11, 47, 2, 6, STEEL_DK)
c.rect(38, 47, 2, 6, STEEL_DK)
c.set(11, 47, STEEL_MID)
c.set(38, 47, STEEL_MID)
c.line(13, 47, 18, 52, STEEL_DARK)
c.line(37, 47, 33, 52, STEEL_DARK)

# ------------------------------------------------------- second technician -
c.set(14, 33, HELMET)
c.set(15, 33, HELMET)
c.set(14, 34, SKIN)
c.set(15, 34, SKIN)
c.set(13, 35, VEST_SH)
c.set(16, 35, VEST_SH)
c.set(14, 35, VEST)
c.set(15, 35, VEST)
c.set(13, 36, VEST_SH)
c.set(16, 36, VEST_SH)
c.set(14, 36, VEST)
c.set(15, 36, VEST)
c.set(13, 37, GLOVE)
c.set(16, 37, GLOVE)
c.set(14, 37, VEST)
c.set(15, 37, VEST)
c.set(14, 38, VEST)
c.set(15, 38, VEST)
c.set(14, 39, NAVY)
c.set(15, 39, NAVY)
c.set(14, 40, NAVY)
c.set(15, 40, NAVY)
c.set(14, 41, NAVY)
c.set(15, 41, NAVY)
c.set(14, 42, NAVY)
c.set(15, 42, NAVY)
c.set(14, 43, BOOT)
c.set(15, 43, BOOT)

# gear bag on the deck
c.rect(18, 42, 3, 2, YELL_DK)
c.set(19, 42, YELL)

# ---------------------------------------------------------------- railing --
for px_ in (12, 17, 26, 31, 36):
    c.rect(px_, 38, 1, 6, YELL_DK)
c.rect(10, 38, 31, 1, YELL)
c.rect(10, 40, 31, 1, YELL_DK)

# life-ring buoy on the rail
c.rect(33, 39, 3, 1, VEST)
c.set(33, 40, VEST)
c.set(35, 40, VEST)
c.set(34, 40, HELMET)
c.rect(33, 41, 3, 1, VEST)

# --------------------------------------------------- waterline and splash --
for x, y in ((11, 51), (38, 51), (12, 50), (37, 50),
             (9, 52), (10, 52), (11, 52), (12, 52), (13, 52), (14, 52),
             (15, 52), (16, 52), (17, 52), (34, 52), (35, 52), (36, 52),
             (37, 52), (38, 52), (39, 52), (40, 52), (41, 52),
             (10, 53), (11, 53), (12, 53), (13, 53), (14, 53), (15, 53),
             (16, 53), (17, 53), (33, 53), (34, 53), (35, 53), (36, 53),
             (37, 53), (38, 53), (39, 53), (40, 53),
             (18, 53), (19, 53), (30, 53), (31, 53), (32, 53),
             (8, 53), (41, 53), (12, 54), (15, 54), (35, 54), (38, 54),
             (7, 54), (42, 54), (9, 54), (40, 54)):
    c.set(x, y, FOAM)

for x, y in ((10, 54), (11, 54), (13, 54), (14, 54), (36, 54), (37, 54),
             (39, 54), (8, 54), (41, 54), (17, 54), (32, 54), (12, 55),
             (37, 55), (14, 55), (35, 55)):
    c.set(x, y, FOAM_SH)

# --------------------------------------------------------- reflection ------
for y, x0, x1 in ((55, 20, 31), (56, 20, 30), (58, 21, 29), (59, 21, 28),
                  (61, 22, 27)):
    c.rect(x0, y, x1 - x0 + 1, 1, WAVE_DK)
for x, y in ((19, 55), (32, 55), (19, 56), (31, 56), (20, 58), (30, 58),
             (22, 61), (27, 61)):
    c.set(x, y, STEEL_DK)

# ------------------------------------------------------- foreground waves --
for x0, x1, y in ((2, 7, 57), (14, 20, 59), (25, 32, 58), (40, 47, 60),
                  (52, 60, 57), (19, 25, 62), (44, 50, 62), (8, 13, 62),
                  (55, 62, 61), (33, 39, 63), (2, 6, 63), (48, 53, 63)):
    c.rect(x0, y, x1 - x0 + 1, 1, FOAM_SH)
for x, y in ((4, 57), (17, 59), (28, 58), (44, 60), (56, 57), (22, 62),
             (47, 62), (36, 63), (4, 63), (50, 63)):
    c.set(x, y, FOAM)

# ------------------------------------------------------------------ probe --
def bbox(label, specs):
    idx = {c.color(s) for s in specs}
    pts = [(x, y) for y in range(H) for x in range(W) if c.get(x, y) in idx]
    if pts:
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        print(f"{label:12s} x {min(xs):2d}..{max(xs):2d}  "
              f"y {min(ys):2d}..{max(ys):2d}  n={len(pts)}")
    else:
        print(f"{label:12s} none")


bbox("helmet", (HELMET,))
bbox("vest", (VEST, VEST_SH))
bbox("navy", (NAVY,))
bbox("boot", (BOOT,))
bbox("skin", (SKIN,))
bbox("blade", (BLADE, BLADE_SH))
bbox("foam", (FOAM,))

print(c.stats_text())
print(c.matrix_text(region=(18, 6, 44, 34)))
finish(c)
