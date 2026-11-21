try:
    from pixelbench_api import *  # noqa: F401,F403
except Exception:
    pass

import math

W = H = 48
OX, OY = 24.0, 12.0       # orb / head centre

# ---------------- palette ----------------
OUT_W   = "#24130A"
WOOD_D  = "#5A3418"
WOOD    = "#7E4A20"
WOOD_L  = "#A76B32"
WOOD_HL = "#C9924C"
GRIP    = "#3A210D"
GRIP_L  = "#6B3D1A"
GOLD_D  = "#8A6A1E"
GOLD    = "#C9A227"
GOLD_L  = "#EDD27A"
OUT_G   = "#1B0A2E"
GEM_D   = "#3D1166"
GEM     = "#6D28B8"
GEM_L   = "#A855F7"
GEM_HL  = "#DDB8FF"
SPARK   = "#F3E8FF"
GLOW    = "#8B45E8"
GLOW_D  = "#5B21A6"
REFLECT = "#7A4FA8"

BACK  = new_canvas(W, H, background=None, name="aura")
STAFF = new_canvas(W, H, background=None, name="staff")
FRONT = new_canvas(W, H, background=None, name="sparks")

LX, LY = -0.59, -0.81          # light direction (upper left)


def free(cnv, x, y):
    """True when (x, y) is inside cnv and still fully transparent."""
    w, h, data = cnv.to_rgba()
    if 0 <= x < w and 0 <= y < h:
        return data[(y * w + x) * 4 + 3] == 0
    return False


def shaft_cx(y):
    return 23.0 - 0.25 * (y - 18)


def shaft_x0(y):
    return int(round(shaft_cx(y) - 2.5))


# ---------------- shaft ----------------
for y in range(18, 48):
    x0 = shaft_x0(y)
    for i, col in enumerate((WOOD_L, WOOD, WOOD, WOOD_D, WOOD_D)):
        STAFF.set(x0 + i, y, col)

for gy, dx, col in ((24, -1, WOOD_D), (28, 1, WOOD_D), (33, -1, WOOD_D),
                    (41, 0, WOOD_D), (26, -2, WOOD_HL), (35, -2, WOOD_HL),
                    (31, 1, WOOD_D), (43, -1, WOOD_D)):
    STAFF.set(shaft_x0(gy) + dx, gy, col)

# leather grip
for y in range(38, 45):
    x0 = shaft_x0(y)
    for i in range(5):
        STAFF.set(x0 + i, y, GRIP)
    STAFF.set(x0 + 1 + ((44 - y) % 3), y, GRIP_L)
    STAFF.set(x0 + 3 - ((y - 38) % 2), y, GRIP_L)

# gold ferrule and butt cap
for y, cols in ((45, (GOLD_D, GOLD_L, GOLD, GOLD, GOLD_D)),
                (46, (GOLD_D, GOLD, GOLD, GOLD_D, GOLD_D)),
                (47, (GOLD_D, GOLD_D, GOLD_D, GOLD_D, GOLD_D))):
    x0 = shaft_x0(y)
    for i, col in enumerate(cols):
        STAFF.set(x0 + i, y, col)

# ---------------- curved head: wooden crescent over the orb ----------------
R_OUT, R_IN = 9.2, 5.0
for y in range(int(OY - R_OUT) - 1, int(OY + R_OUT) + 2):
    for x in range(int(OX - R_OUT) - 1, int(OX + R_OUT) + 2):
        d2 = (x - OX) ** 2 + (y - OY) ** 2
        if not (R_IN * R_IN <= d2 <= R_OUT * R_OUT):
            continue
        ang = math.degrees(math.atan2(y - OY, x - OX)) % 360
        if 45 <= ang <= 135:            # the mouth, filled by the gold mount
            continue
        STAFF.set(x, y, WOOD)

# torus shading on the wood: light from the upper left
wood_idx = {STAFF.color(c) for c in (WOOD, WOOD_L, WOOD_D, WOOD_HL)}
for y in range(1, 23):
    for x in range(12, 37):
        if STAFF.get(x, y) not in wood_idx:
            continue
        if math.hypot(x - OX, y - OY) > R_OUT + 1.5:
            continue
        dx, dy = x - OX, y - OY
        d = math.hypot(dx, dy) or 1.0
        t = (dx * LX + dy * LY) / d
        if t > 0.80:
            STAFF.set(x, y, WOOD_HL)
        elif t > 0.50:
            STAFF.set(x, y, WOOD_L)
        elif t < -0.55:
            STAFF.set(x, y, WOOD_D)

for gx, gy, col in ((19, 5, WOOD_D), (28, 4, WOOD_D), (32, 11, WOOD_D),
                    (16, 10, WOOD_HL), (30, 16, WOOD_L), (18, 7, WOOD_D)):
    if STAFF.get(gx, gy) in wood_idx:
        STAFF.set(gx, gy, col)

# ---------------- gold mount: the arc that cups the orb ----------------
for y in range(int(OY - R_OUT) - 1, int(OY + R_OUT) + 2):
    for x in range(int(OX - R_OUT) - 1, int(OX + R_OUT) + 2):
        d2 = (x - OX) ** 2 + (y - OY) ** 2
        if not (R_IN * R_IN <= d2 <= R_OUT * R_OUT):
            continue
        ang = math.degrees(math.atan2(y - OY, x - OX)) % 360
        if not (35 <= ang <= 145):
            continue
        d = math.sqrt(d2)
        if d > R_OUT - 1.2:
            col = GOLD_D                    # shaded underside
        elif ang > 118:
            col = GOLD_L                    # catching the light, upper left
        elif ang < 62:
            col = GOLD_D
        else:
            col = GOLD
        STAFF.set(x, y, col)

STAFF.outline(OUT_W)

# ---------------- the orb ----------------
ORB_R = 5.2
cells = [(dx, dy) for dy in range(-6, 7) for dx in range(-6, 7)
         if dx * dx + dy * dy <= ORB_R * ORB_R]
cell_set = set(cells)
for dx, dy in cells:
    if any((dx + nx, dy + ny) not in cell_set
           for nx, ny in ((1, 0), (-1, 0), (0, 1), (0, -1))):
        STAFF.set(int(OX) + dx, int(OY) + dy, OUT_G)
        continue
    d = math.hypot(dx, dy) or 1.0
    t = (dx * LX + dy * LY) / d
    if t > 0.80:
        col = GEM_HL
    elif t > 0.40:
        col = GEM_L
    elif d > 3.9 and t < -0.30:
        col = GEM_D          # shadow hugging the lower-right rim
    else:
        col = GEM
    STAFF.set(int(OX) + dx, int(OY) + dy, col)

# bounce light along the orb's lower rim
for dx, dy in ((-1, 5), (0, 5), (1, 5), (-2, 4), (2, 4)):
    if (dx, dy) in cell_set:
        STAFF.set(int(OX) + dx, int(OY) + dy, GEM_L)

# glint
STAFF.set(int(OX) - 2, int(OY) - 2, SPARK)
STAFF.set(int(OX) - 1, int(OY) - 2, GEM_HL)
STAFF.set(int(OX) - 2, int(OY) - 1, GEM_HL)

# purple light the orb casts onto the wood hugging it
for y in range(1, 23):
    for x in range(12, 37):
        if STAFF.get(x, y) not in wood_idx:
            continue
        d = math.hypot(x - OX, y - OY)
        if R_IN <= d <= R_IN + 1.2:
            STAFF.set(x, y, REFLECT)

# ---------------- aura (behind) ----------------
for k in range(44):
    ang = math.radians(k * (360 / 44))
    r = (10.5, 11.5, 12.5, 13.5)[k % 4]
    x = int(round(OX + r * math.cos(ang)))
    y = int(round(OY + 1 + r * math.sin(ang)))
    if free(STAFF, x, y):
        BACK.set(x, y, GLOW if k % 3 == 0 else GLOW_D)

for gy in (25, 30, 35, 40, 44):
    x0 = shaft_x0(gy)
    for sx, col in ((x0 - 7, GLOW_D), (x0 + 7, GLOW)):
        if free(STAFF, sx, gy):
            BACK.set(sx, gy, col)
for gx, gy, col in ((11, 4, GLOW_D), (37, 3, GLOW), (6, 16, GLOW),
                    (41, 17, GLOW_D), (34, 46, GLOW_D), (5, 30, GLOW),
                    (13, 21, GLOW_D), (36, 23, GLOW)):
    if free(STAFF, gx, gy):
        BACK.set(gx, gy, col)

# ---------------- bright sparks (in front) ----------------
def plus(cnv, x, y):
    cnv.set(x, y, SPARK)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        cnv.set(x + dx, y + dy, GEM_L)

plus(FRONT, 10, 4)
plus(FRONT, 38, 6)
plus(FRONT, 33, 23)

TWINKLES = [
    (16, 1, SPARK), (31, 2, GEM_L), (5, 9, GEM_L), (42, 12, SPARK),
    (7, 21, GEM_L), (40, 27, GEM_L), (12, 31, SPARK), (30, 38, GEM_L),
    (4, 37, GEM_L), (21, 34, SPARK), (36, 43, GEM_L), (15, 45, GEM_L),
    (43, 33, SPARK), (3, 26, GEM_L), (27, 47, GEM_L), (11, 12, GEM_L),
]
for x, y, col in TWINKLES:
    if free(STAFF, x, y):
        FRONT.set(x, y, col)

for gy in (24, 30, 36):
    x0 = shaft_x0(gy)
    for sx, sy in ((x0 + 5, gy), (x0 + 5, gy - 1)):
        if free(STAFF, sx, sy):
            FRONT.set(sx, sy, GLOW if sy == gy else GEM_L)

# ---------------- assemble ----------------
result = flatten([BACK, STAFF, FRONT], name="magic-staff")
print(result.stats_text())
print(result.matrix_text())
save("magic-staff", result)
finish(result)
