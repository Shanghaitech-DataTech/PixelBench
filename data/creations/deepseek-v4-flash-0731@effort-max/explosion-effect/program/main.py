from pixelbench_api import *

W = H = 64
c = new_canvas(W, H)

WHITE  = c.color("#ffffff")
L_YEL  = c.color("#ffe873")
YEL   = c.color("#ffd100")
ORG   = c.color("#ff7b00")
D_ORG = c.color("#e84e00")
RED   = c.color("#d92b00")
D_RED = c.color("#9e1f00")

# ===== Frame 1 : bright yellow fireball, left cell (x 0..31), center (16, 32) =====
fx, fy = 16, 32
c.circle(fx, fy, 10, D_ORG)
for dx, dy in [(8, 5), (0, 9), (-8, 5), (-8, -5), (0, -9), (8, -5), (11, 0), (-11, 0)]:
    c.circle(fx + dx, fy + dy, 4, D_ORG)
c.circle(fx, fy, 8, ORG)
c.circle(fx, fy, 6, YEL)
c.circle(fx, fy, 4, L_YEL)
c.circle(fx, fy, 2, WHITE)
for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1)]:
    c.set(fx + dx, fy + dy, WHITE)
    c.set(fx - dx, fy - dy, WHITE)

# ===== Frame 2 : expanding orange-red blast with sparks, right cell (x 32..63), center (48, 32) =====
bx, by = 48, 32
c.circle(bx, by, 11, D_RED)
for dx, dy in [(9, 5), (0, 11), (-9, 5), (-9, -5), (0, -11), (9, -5), (11, 0), (-11, 0)]:
    c.circle(bx + dx, by + dy, 4, D_RED)
c.circle(bx, by, 9, RED)
c.circle(bx, by, 7, ORG)
c.circle(bx, by, 5, YEL)
c.circle(bx, by, 3, L_YEL)
c.circle(bx, by, 1, WHITE)

sparks = [
    (14, -11, L_YEL), (-13, -11, YEL), (0, -17, WHITE), (-10, 13, YEL),
    (12, 12, L_YEL), (-15, 3, L_YEL), (15, -4, YEL), (-5, 16, ORG),
    (7, -16, ORG), (-13, 9, YEL), (9, 14, YEL), (0, 18, YEL),
    (-16, -3, YEL), (11, -14, L_YEL), (-11, -14, YEL), (-8, -15, ORG),
    (3, 15, D_RED), (-12, 13, D_RED), (6, -17, D_RED),
]
for dx, dy, col in sparks:
    c.set(bx + dx, by + dy, col)

print(c.stats_text())
finish(c)
