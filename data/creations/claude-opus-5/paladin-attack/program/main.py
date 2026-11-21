import math

W, H = 72, 72
OX, OY = 3, 6

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, OX, OY)

f2 = f1.copy(name="f2")

# ---------------------------------------------------------------- palette
BLACK = "#101010"
GOLD = "#af7a18"
GOLD_D = "#512a13"
GOLD_L = "#ffcc43"
STEEL_D = "#332d32"
STEEL_M = "#5a565a"
STEEL = "#858086"
STEEL_L = "#a9a5ab"
STEEL_H = "#dccaca"
HEAD_D = "#78655a"
HEAD_M = "#a8a098"
HEAD_L = "#ffffd5"
WHITE = "#ffffff"
TRAIL_S = "#f2f0f8"
TRAIL_E = "#b9b4c8"
SHADOW = "#17003599"

# ------------------------------------------- erase frame-1 weapon and arm
ERASE = [(r, 16, 31) for r in range(0, 8)] + [
    (8, 20, 31), (9, 21, 31), (10, 22, 33), (11, 26, 35), (12, 27, 36),
    (13, 28, 37), (14, 24, 37), (15, 27, 38), (16, 27, 39), (17, 27, 41),
    (18, 27, 42), (19, 28, 42), (20, 28, 42), (21, 36, 42), (22, 37, 42),
]
for r, x0, x1 in ERASE:
    f2.clear(x0 + OX, r + OY, x1 - x0 + 1, 1)


# ------------------------------------------------------------- geometry
def thick(c, p0, p1, w, col):
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    half = (w - 1) / 2.0
    for i in range(max(1, int(w))):
        o = -half + i
        c.line(round(x0 + nx * o), round(y0 + ny * o),
               round(x1 + nx * o), round(y1 + ny * o), col)
    return c


PIV = (29.0, 28.0)                 # shoulder pivot of the swing
SH = (33.0, 27.0)
EL = (40.0, 33.0)
HAND = (45.0, 40.0)
ANG = math.radians(55.0)
DIR = (math.cos(ANG), math.sin(ANG))
PRP = (-DIR[1], DIR[0])
HEADC = (HAND[0] + 15 * DIR[0], HAND[1] + 15 * DIR[1])

# ------------------------------------------------------- motion trail
th0 = math.radians(-110.0)
th1 = math.atan2(HEADC[1] - PIV[1], HEADC[0] - PIV[0])
r0 = 24.0
r1 = math.hypot(HEADC[0] - PIV[0], HEADC[1] - PIV[1])


def ribbon(c, t_lo, col, wscale):
    """Scan-convert the swing band: one test per pixel, so no sampling gaps."""
    for y in range(H):
        for x in range(W):
            dx, dy = x + 0.5 - PIV[0], y + 0.5 - PIV[1]
            r = math.hypot(dx, dy)
            if r < 8:
                continue
            t = (math.atan2(dy, dx) - th0) / (th1 - th0)
            if not (t_lo <= t <= 1.0):
                continue
            rc = r0 + (r1 - r0) * t ** 2.2
            hw = (0.4 + 3.1 * t ** 1.3) * wscale
            if abs(r - rc) <= hw:
                c.set(x, y, col)


ribbon(f2, 0.05, TRAIL_E, 1.15)
ribbon(f2, 0.18, TRAIL_S, 0.88)
ribbon(f2, 0.42, WHITE, 0.52)

# ------------------------------------------------------- pauldron
f2.ellipse(34, 24, 5, 4, BLACK)
f2.ellipse(34, 24, 4, 3, STEEL_M)
f2.ellipse(33, 23, 2, 1, STEEL_L)
f2.set(32, 22, STEEL_H)
f2.line(31, 27, 37, 27, GOLD)
f2.set(33, 28, GOLD_L)

# ------------------------------------------------------- arm
thick(f2, SH, EL, 8, BLACK)
thick(f2, EL, HAND, 7, BLACK)
thick(f2, SH, EL, 6, STEEL_M)
thick(f2, EL, HAND, 5, STEEL_M)
f2.line(SH[0] - 1, SH[1] - 1, EL[0] - 1, EL[1] - 1, STEEL)
f2.line(EL[0] - 1, EL[1] - 1, HAND[0] - 1, HAND[1] - 1, STEEL)
f2.line(SH[0] - 2, SH[1] - 2, EL[0] - 2, EL[1] - 2, STEEL_L)
f2.line(38, 30, 42, 34, GOLD)          # elbow band
f2.set(39, 30, GOLD_L)

# gauntlet
f2.circle(round(HAND[0]), round(HAND[1]), 4, BLACK)
f2.circle(round(HAND[0]), round(HAND[1]), 3, STEEL_D)
f2.circle(round(HAND[0]) - 1, round(HAND[1]) - 1, 1, STEEL)
f2.set(round(HAND[0]) - 2, round(HAND[1]) - 2, STEEL_H)
f2.set(round(HAND[0]) + 2, round(HAND[1]) + 1, GOLD)

# ------------------------------------------------------- weapon
BUTT = (HAND[0] - 5 * DIR[0], HAND[1] - 5 * DIR[1])
HTIP = (HEADC[0] - 1.0 * DIR[0], HEADC[1] - 1.0 * DIR[1])
thick(f2, BUTT, HTIP, 5, BLACK)
thick(f2, BUTT, HTIP, 3, GOLD_D)
f2.line(round(BUTT[0] + PRP[0] * 0.6), round(BUTT[1] + PRP[1] * 0.6),
        round(HTIP[0] + PRP[0] * 0.6), round(HTIP[1] + PRP[1] * 0.6), GOLD)


def quad(c, cx, cy, half_len, half_th, col):
    pts = []
    for sl, st in ((1, 1), (1, -1), (-1, -1), (-1, 1)):
        pts.append((round(cx + PRP[0] * half_len * sl + DIR[0] * half_th * st),
                    round(cy + PRP[1] * half_len * sl + DIR[1] * half_th * st)))
    c.poly(pts, col)


quad(f2, HEADC[0], HEADC[1], 6.4, 4.2, BLACK)
quad(f2, HEADC[0], HEADC[1], 5.2, 3.0, HEAD_M)
quad(f2, HEADC[0] - PRP[0] * 2.4, HEADC[1] - PRP[1] * 2.4, 2.4, 2.4, HEAD_L)
quad(f2, HEADC[0] + PRP[0] * 3.3, HEADC[1] + PRP[1] * 3.3, 1.5, 2.6, HEAD_D)
quad(f2, HEADC[0], HEADC[1], 0.7, 3.0, GOLD_D)   # ferrule band

# ------------------------------------------------- left foot steps forward
shadow_idx = f1.color(SHADOW)
BX, BY, BW, BH = 12, 57, 9, 8
foot = f2.select(BX, BY, BW, BH)
for yy in range(BY, BY + BH):
    for xx in range(BX, BX + BW):
        f2.set(xx, yy, SHADOW if f1.get(xx, yy) == shadow_idx else None)
foot.copy_to(BX - 2, BY + 2, f2, mode="over")

# greave bridging hip to the lowered boot
f2.rect(13, 55, 6, 5, STEEL_D)
f2.rect(14, 55, 3, 5, STEEL_M)
f2.line(12, 55, 12, 59, BLACK)
f2.line(19, 55, 19, 59, BLACK)
f2.line(14, 58, 17, 58, GOLD)
f2.set(14, 56, STEEL_L)
# shadow smear under the advanced foot
f2.line(10, 67, 17, 67, SHADOW)
f2.set(9, 66, SHADOW)

view(f1)
view(f2)
finish([f1, f2])
