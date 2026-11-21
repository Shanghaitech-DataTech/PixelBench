import math
from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, name="sports_bike")

BLACK   = c.color('#141416')
BODY    = c.color('#2e2e34')
BODY2   = c.color('#3f3f47')
SILVER  = c.color('#c9c9d0')
SILVER2 = c.color('#9a9aa4')
METAL   = c.color('#6f6f78')
RED     = c.color('#e0242c')
REDD    = c.color('#8a0f14')
WHITE   = c.color('#f2f2f2')
TIRE    = c.color('#101012')
RIM     = c.color('#1b1b20')


def thick_line(x0, y0, x1, y1, col, w=2):
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx = -dy / L
    ny = dx / L
    c.poly([(round(x0 + nx * w), round(y0 + ny * w)),
           (round(x1 + nx * w), round(y1 + ny * w)),
           (round(x1 - nx * w), round(y1 - ny * w)),
           (round(x0 - nx * w), round(y0 - ny * w))], col)


def spokes(cx, cy, n=5, r0=7, r1=13, col=WHITE):
    for i in range(n):
        a = math.radians(90 + i * 360 / n)
        c.line(round(cx + r0 * math.cos(a)), round(cy + r0 * math.sin(a)),
               round(cx + r1 * math.cos(a)), round(cy + r1 * math.sin(a)), col)


# ---------------- WHEELS ----------------
# rear wheel
c.circle(32, 92, 23, TIRE)
c.circle(32, 92, 14, RIM)
spokes(32, 92, 5, 7, 13, WHITE)
c.circle(32, 92, 6, SILVER2)
c.circle(32, 92, 2, BLACK)

# front wheel
c.circle(98, 92, 23, TIRE)
c.circle(98, 92, 14, RIM)
c.circle(98, 92, 11, SILVER)
spokes(98, 92, 5, 5, 12, WHITE)
c.circle(98, 92, 5, SILVER2)
c.circle(98, 92, 2, BLACK)
c.rect(103, 86, 4, 8, RED)          # brake caliper

# fork
c.poly([(94, 92), (103, 92), (102, 73), (99, 46), (95, 46), (93, 73)], SILVER)
c.poly([(96, 92), (101, 92), (100, 77), (97, 50), (95, 50), (94, 77)], METAL)

# swingarm + rear hugger
c.poly([(58, 76), (62, 72), (36, 91), (32, 87)], BODY2)
c.poly([(28, 64), (42, 64), (44, 72), (30, 72)], BODY2)

# ---------------- BODY ----------------
body = [(100, 46), (106, 58), (102, 70), (88, 80), (58, 86), (52, 82),
        (46, 70), (40, 62), (30, 56), (22, 52), (16, 44), (17, 36),
        (28, 40), (40, 42), (56, 44), (70, 40), (84, 36), (92, 40)]
c.poly(body, BODY)

# upper fairing / tank panel
c.poly([(50, 44), (68, 41), (84, 36), (91, 40), (83, 46), (64, 48), (50, 48)], BODY2)

# exhaust (under tail)
thick_line(54, 78, 28, 54, SILVER2, 2)
c.poly([(24, 50), (33, 55), (30, 59), (21, 55)], SILVER2)
c.rect(18, 51, 6, 5, BLACK)

# engine cover (round silver gray)
c.circle(56, 76, 11, SILVER2)
c.circle(56, 76, 7, SILVER)
c.circle(56, 76, 9, RED, fill=False)
c.circle(56, 76, 3, BLACK)

# silver tubular frame
thick_line(90, 45, 58, 74, SILVER, 2)
thick_line(58, 72, 42, 48, SILVER, 2)
thick_line(42, 48, 26, 42, SILVER, 2)

# seat
c.poly([(30, 41), (50, 43), (52, 49), (30, 48)], BLACK)

# windscreen (small, tilted back, black)
c.poly([(80, 29), (92, 35), (90, 43), (78, 40)], BLACK)

# front fender
c.poly([(76, 64), (92, 58), (107, 64), (104, 72), (96, 68), (82, 68)], BODY2)
c.line(80, 66, 94, 61, RED)

# belly edge + vents
c.line(60, 84, 86, 76, SILVER2)
c.line(80, 75, 70, 78, BLACK)
c.line(77, 79, 65, 82, BLACK)

# tail light (red, upswept tail tip)
c.poly([(15, 36), (22, 38), (23, 44), (16, 44)], REDD)
c.poly([(16, 37), (21, 39), (22, 43), (17, 43)], RED)

# headlight
c.poly([(99, 48), (105, 51), (103, 56), (97, 54)], BLACK)
c.poly([(100, 50), (103, 51), (102, 54), (99, 53)], SILVER2)

# handlebar
c.rect(89, 42, 19, 4, BLACK)

# red tank pinstripe
c.line(68, 42, 84, 37, RED)

print(c.stats_text())

finish(c)
