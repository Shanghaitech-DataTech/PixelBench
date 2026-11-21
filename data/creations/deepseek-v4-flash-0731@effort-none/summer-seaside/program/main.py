from pixelbench_api import *

c = new_canvas(128, 128, name="beach")

# Palette colors
SKY = c.color("#7EC8F0")
SKY2 = c.color("#A5DCF7")
SUN = c.color("#FFEB3B")
SUNH = c.color("#FFF59D")
CLOUD = c.color("#FFFFFF")

DEEP_BLUE = c.color("#0E4FA0")
MID_BLUE = c.color("#1E72C8")
TEAL = c.color("#2FA0A0")
TEAL_L = c.color("#5BD5AF")
FOAM = c.color("#FFFFFF")

SAND = c.color("#F7E3A8")
SAND_D = c.color("#E8CB7B")

RED = c.color("#E3352D")
POLE = c.color("#8D6E63")
WHITE = c.color("#FFFFFF")

TOW = c.color("#E91E63")
TOW_S = c.color("#F7A8C4")

FLIP = c.color("#4CAF50")
STAP = c.color("#FFFFFF")

BOAT_H = c.color("#C62828")
BOAT_S = c.color("#FFFFFF")

GULL = c.color("#2F3640")

# ---------------- SKY ----------------
c.rect(0, 0, 128, 45, SKY)
# lighter band near horizon
c.rect(0, 44, 128, 9, SKY2)

# ---------------- SUN ----------------
c.circle(20, 20, 13, SUNH)
c.circle(20, 20, 8, SUN)

# ---------------- CLOUDS ----------------
def cloud(cx, cy):
    pts = [(-12,4,5),(-6,-2,7),(1,-5,8),(9,-3,6),(13,3,5),(4,3,7),(-4,4,5)]
    for ox, oy, r in pts:
        c.circle(cx+ox, cy+oy, r, CLOUD)

cloud(68, 14)
cloud(50, 30)
cloud(100, 22)
cloud(104, 38)

# ---------------- OCEAN ----------------
# horizon at y=53
c.rect(0, 53, 128, 13, DEEP_BLUE)
c.rect(0, 66, 128, 13, MID_BLUE)
c.rect(0, 79, 128, 13, TEAL)
c.rect(0, 92, 128, 11, TEAL_L)

# foam wave texture (dotted lines)
import random
random.seed(7)
for y in range(70, 103):
    if y in (74, 87, 99):
        for x in range(0, 128, 4):
            if random.random() < 0.7:
                c.set(x + random.randint(0,2), y, FOAM)

# shoreline foam
for x in range(0, 128):
    if x % 3 == 1:
        c.set(x, 102, FOAM)

# sun reflection on water (vertical shimmer under sun)
for y in range(53, 103, 2):
    for dx in range(-1, 2):
        c.set(20+dx, y, FOAM if (y%4<2) else SUNH)

# ---------------- SAILBOAT (far out) ----------------
bx, by = 95, 60
# wake
c.line(bx+8, by+7, bx-2, by+10, MID_BLUE)
# hull
c.poly([(bx, by+5),(bx+10, by+5),(bx+12, by+7),(bx-1, by+7)], BOAT_H)
# sails
c.poly([(bx+4, by+5),(bx+4, by-6),(bx+9, by+5)], BOAT_S)
c.poly([(bx+6, by+5),(bx+6, by-9),(bx+11, by+5)], BOAT_S)

# ---------------- SAND ----------------
c.rect(0, 105, 128, 23, SAND)
# subtle wet sand line
c.rect(0, 105, 128, 3, SAND_D)

# ---------------- UMBRELLA (left) ----------------
ux = 30
# pole
c.line(ux+12, 88, ux+12, 127, POLE)
# dome with alternating red/white horizontal stripes
# dome spans roughly x from 8 to 52, top around 66
for row in range(68, 89):
    t = (row - 66) / 23.0          # 0 at top of dome to 1 at full width
    half = int(20.0 * t)  # half width increases toward bottom
    if half < 1:
        continue
    col = RED if (row // 2) % 2 == 0 else WHITE
    c.line(ux+12-half, row, ux+12+half-1, row, col)
# finial on top
c.set(ux+12, 66, POLE)
# shadow under umbrella
c.line(8, 90, 52, 90, SAND_D)

# ---------------- TOWEL (right side) ----------------
c.rect(76, 114, 36, 9, TOW)
for i in range(3):
    c.rect(76, 114+i*3+1, 36, 1, TOW_S)

# ---------------- FLIP FLOPS ----------------
# pair on sand left of towel
c.rect(66, 120, 6, 5, FLIP)
c.line(68, 121, 70, 124, STAP)
c.rect(73, 120, 6, 5, FLIP)
c.line(75, 121, 77, 124, STAP)

# ---------------- GULLS ----------------
def gull(x, y, s=1):
    c.line(x, y, x+int(3*s), y-int(1*s), GULL)
    c.line(x, y, x-int(3*s), y-int(1*s), GULL)

gull(50, 40)
gull(116, 16)

print(c.stats_text())
finish(c)
