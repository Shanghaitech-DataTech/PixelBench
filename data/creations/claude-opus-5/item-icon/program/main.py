import math

c = new_canvas(32, 32, name="output")

# ---- palette ----
DARK = c.color("#140d1e", "dark")
GOLD_D = c.color("#7a4a16", "gold_d")
GOLD_M = c.color("#b8832a", "gold_m")
GOLD_L = c.color("#e0b354", "gold_l")
GOLD_H = c.color("#f9eab4", "gold_h")
FACE_D = c.color("#241a2d", "face_d")
FACE_M = c.color("#3a2b40", "face_m")
BLU_D = c.color("#103062", "blu_d")
BLU_M = c.color("#2a6fc0", "blu_m")
BLU_L = c.color("#64bdf0", "blu_l")
WHT = c.color("#eaf8ff", "wht")

CX = CY = 15.5
LX, LY = -0.68, -0.73  # light from upper-left


def lam(dx, dy, r):
    return 1.0 if r < 0.01 else (dx * LX + dy * LY) / r


def gold_shade(n):
    if n > 0.92:
        return GOLD_H
    if n > 0.30:
        return GOLD_L
    if n > -0.50:
        return GOLD_M
    return GOLD_D


# ================= case: outline, bezel, dial =================
for y in range(32):
    for x in range(32):
        dx, dy = x - CX, y - CY
        r = math.hypot(dx, dy)
        if r > 14.6:
            continue
        n = lam(dx, dy, r)
        if r > 12.9:
            col = DARK                     # thick outer outline
        elif r > 10.4:
            col = gold_shade(n)            # gold bezel
        elif r > 9.3:
            col = DARK                     # inner outline
        else:
            col = FACE_D if n < 0.25 else FACE_M
        c.set(x, y, col)

for y in range(32):
    for x in range(32):
        dx, dy = x - CX, y - CY
        r = math.hypot(dx, dy)
        if not 10.4 < r <= 12.9:
            continue
        n = lam(dx, dy, r)
        outer = r > 11.7
        if n > 0.55:
            c.set(x, y, GOLD_H if outer else GOLD_L)
        elif n > -0.25:
            c.set(x, y, GOLD_L if outer else GOLD_M)
        else:
            c.set(x, y, GOLD_M if outer else GOLD_D)

# bezel ticks on the diagonals
for k in (1, 3, 5, 7):
    a = k * math.pi / 4.0
    ux, uy = math.sin(a), -math.cos(a)
    rr = 10.7
    while rr <= 12.6:
        c.set(round(CX + ux * rr), round(CY + uy * rr), DARK)
        rr += 0.45

# ================= 8-point compass rose =================
CARD_L, CARD_W = 9.2, 3.0   # primary arm length / half-width at centre
DIAG_L, DIAG_W = 7.2, 2.1   # secondary arm

rose = {}


def taper(along, across, length, width):
    """Inside a kite arm: width shrinks linearly to the tip."""
    if along < 0 or along > length:
        return False
    return abs(across) <= width * (1.0 - along / length)


for y in range(32):
    for x in range(32):
        dx, dy = x - CX, y - CY
        u, v = (dx + dy) / 1.41421, (dx - dy) / 1.41421

        # secondary (diagonal) arms, mid/dark gold
        if taper(u, v, DIAG_L, DIAG_W):          # SE
            rose[(x, y)] = GOLD_M if v < 0 else GOLD_D
        elif taper(-u, v, DIAG_L, DIAG_W):       # NW
            rose[(x, y)] = GOLD_M if v > 0 else GOLD_D
        elif taper(v, u, DIAG_L, DIAG_W):        # NE
            rose[(x, y)] = GOLD_M if u < 0 else GOLD_D
        elif taper(-v, u, DIAG_L, DIAG_W):       # SW
            rose[(x, y)] = GOLD_M if u > 0 else GOLD_D

        # primary (cardinal) arms overwrite, light/mid gold
        if taper(-dy, dx, CARD_L, CARD_W):       # N
            rose[(x, y)] = GOLD_L if dx < 0 else GOLD_M
        elif taper(dy, dx, CARD_L, CARD_W):      # S
            rose[(x, y)] = GOLD_L if dx < 0 else GOLD_M
        elif taper(-dx, dy, CARD_L, CARD_W):     # W
            rose[(x, y)] = GOLD_L if dy < 0 else GOLD_M
        elif taper(dx, dy, CARD_L, CARD_W):      # E
            rose[(x, y)] = GOLD_L if dy < 0 else GOLD_M

for (x, y), col in rose.items():
    c.set(x, y, col)

# north arm reads brightest, as the marked needle
for yy in range(7, 13):
    for xx in range(13, 18):
        if (xx, yy) in rose:
            c.set(xx, yy, GOLD_H if xx <= 15 else GOLD_L)
c.set(8, 15, GOLD_H)
c.set(9, 15, GOLD_H)

# faint dial pips between the arms
for k in (1, 3, 5, 7):
    a = k * math.pi / 4.0
    px = round(CX + math.sin(a) * 8.0)
    py = round(CY - math.cos(a) * 8.0)
    c.set(px, py, GOLD_D)

BLU_HI = c.color("#a8e6ff", "blu_hi")

# ================= blue crystal centre =================
for y in range(32):
    for x in range(32):
        dx, dy = x - CX, y - CY
        r = math.hypot(dx, dy)
        if r > 4.0:
            continue
        n = lam(dx, dy, r)
        if r > 3.1:
            c.set(x, y, DARK)
        else:
            c.set(x, y, BLU_L if n > 0.45 else (BLU_M if n > -0.3 else BLU_D))

# facets and glint
c.set(14, 14, BLU_HI)
c.set(14, 13, BLU_HI)
c.set(13, 14, BLU_HI)
c.set(15, 14, BLU_L)
c.set(16, 14, BLU_L)
c.set(17, 16, BLU_D)
c.set(16, 17, BLU_D)
c.set(15, 17, BLU_D)
c.set(13, 17, BLU_M)

c.outline(DARK)
view(c)
print(c.stats_text())
finish(c)
