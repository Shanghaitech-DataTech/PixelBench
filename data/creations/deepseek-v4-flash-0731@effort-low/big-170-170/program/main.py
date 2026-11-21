from pixelbench_api import *
import random

out = input_canvas.copy(name='output')

# =========================================================
# 1. THUNDERSTORM DARKENING over the sky (keeps ground detail)
# =========================================================
dark = (6, 13, 24, 150)
out.rect(0, 0, 170, 50, dark)
# darker storm clouds streaks
cloud = (3, 8, 16, 110)
random.seed(11)
for _ in range(60):
    x = random.randint(0, 165); y = random.randint(0, 46)
    out.line(x, y, x + random.randint(4, 14), y, cloud)

# =========================================================
# 2. LIGHTNING in the background
# =========================================================
L = (248, 240, 170, 255)
Lg = (210, 200, 140, 110)
def bolt(pts, thick=True):
    for i in range(len(pts) - 1):
        out.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], Lg)
    if thick:
        out.line(pts[0][0]-1, pts[0][1]+1, pts[-1][0]-1, pts[-1][1]+1, Lg)
    for i in range(len(pts) - 1):
        out.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], L)
bolt([(20,0),(34,15),(25,20),(44,38),(33,46)])
bolt([(146,0),(158,14),(150,22),(166,38)])
bolt([(92,0),(98,10),(94,16)])

# =========================================================
# 3. REMOVE CHARACTER + FILL WITH VENDING MACHINE
# =========================================================
# Redraw a glowing drink vending machine over the character region.
M_BD  = out.color('#0d2b3a')   # dark body outline
M_RD  = out.color('#7e2a18')   # deep red casing
M_RR  = out.color('#c42f0f')   # bright red panel
M_DR  = out.color('#29323b')   # dark
WIN   = out.color('#150f2e')   # glass window
C_A   = out.color('#ffb24a')
C_B   = out.color('#ff5a3a')
C_C   = out.color('#3f8aff')
C_D   = out.color('#4fb64a')
C_E   = out.color('#ff3a72')
GL   = out.color('#ff8a4a')

# body
out.rect(76, 53, 41, 95, M_BD)          # casing x76..116 y53..147
# base
out.rect(74, 145, 45, 6, '#12212b')
out.rect(76, 145, 41, 4, M_RD)
# main red body
out.rect(79, 56, 35, 90, M_RR)
out.rect(81, 56, 31, 90, M_RD)
# glowing brand panel top
out.rect(81, 58, 31, 28, M_RR)
out.rect(83, 60, 27, 5, GL)
# glass window
out.rect(85, 70, 23, 50, WIN)
# shelf interior + drinks (3 columns x 5 rows)
cx = [86, 94, 102]
for r in range(5):
    yy = 72 + r * 10
    for xx in cx:
        col = [C_A, C_C, C_E, C_B, C_D][(r + xx) % 5]
        out.rect(xx, yy, 4, 8, col)
        out.rect(xx, yy, 4, 2, GL)
        out.rect(xx + 1, yy + 3, 2, 1, '#ffffff')
# brand bar
out.rect(83, 124, 27, 3, GL)
# selection buttons
random.seed(7)
for r in range(3):
    for xx in [84, 93, 102]:
        out.rect(xx, 130 + r * 5, 3, 3, C_C if (xx + r) % 2 else C_B)
# lower panel
out.rect(81, 146, 31, 4, '#35120b')

# =========================================================
# 4. RAIN with semi-transparent droplets
# =========================================================
rain = (168, 192, 224, 95)
random.seed(3)
for _ in range(200):
    x = random.randint(0, 167); y = random.randint(0, 166)
    out.line(x, y, x - 2, y + 7, rain)
    if random.random() < 0.35:
        out.set(x, y, (190, 210, 238, 120))

# =========================================================
# 5. WET GROUND with clinging water droplets
# =========================================================
wet = (8, 18, 32, 130)
out.rect(0, 148, 170, 22, wet)
# reflections / glistening streaks
streak = (150, 175, 205, 120)
random.seed(5)
for _ in range(90):
    x = random.randint(0, 163); y = random.randint(149, 168)
    out.line(x, y, x + random.randint(3, 9), y, streak)
# clinging water droplets (small bright blobs on ground surfaces)
drip = (225, 238, 250, 200)
random.seed(9)
for _ in range(120):
    x = random.randint(0, 165); y = random.randint(149, 168)
    out.rect(x, y, 2, 1, drip)
    out.set(x, y + 1, (255, 250, 230, 150))
# droplets clinging on the vending machine / buildings front
for _ in range(40):
    x = random.randint(55, 120); y = random.randint(110, 145)
    out.set(x, y, drip)
# puddle sparkles at street
for _ in range(25):
    x = random.randint(40, 130); y = random.randint(118, 145)
    out.set(x, y, (200, 220, 245, 160))

finish(out)
