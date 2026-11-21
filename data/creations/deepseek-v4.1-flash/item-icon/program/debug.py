from pixelbench_api import *
import math

c = new_canvas(32, 32, name="icon")

DARK   = '#140d18'
GOLD_H = '#fff6c8'
GOLD_L = '#f2c552'
GOLD   = '#b8832a'
GOLD_D = '#7d5212'
GOLD_X = '#523208'
FACE   = '#3d2812'
FACE_D = '#231609'
CRY_X  = '#0a1638'
CRY_DD = '#123a86'
CRY_D  = '#1a55b4'
CRY    = '#2478e0'
CRY_L  = '#6ccdff'
CRY_H  = '#cdf4ff'
WHITE  = '#ffffff'

CX = CY = 15.5


def dxy(x, y):
    return x - CX, y - CY


for y in range(32):
    for x in range(32):
        dx, dy = dxy(x, y)
        d = (dx * dx + dy * dy) ** 0.5
        if d > 14.0:
            continue
        if d > 12.1:
            c.set(x, y, DARK)
        elif d > 9.3:
            u = (dx + dy) / (d * 1.4142)
            if u < -0.35:
                col = GOLD_L
            elif u < 0.40:
                col = GOLD
            else:
                col = GOLD_D
            if u < -0.45 and d > 11.0:
                col = GOLD_H
            if u > 0.30 and d > 11.3:
                col = GOLD_X
            c.set(x, y, col)
        elif d > 8.7:
            c.set(x, y, GOLD_X)
        else:
            c.set(x, y, FACE if dx + dy < 2.0 else FACE_D)

for (x, y) in [(12, 7), (13, 7), (18, 7), (19, 7), (7, 12), (24, 12), (26, 12), (25, 12)]:
    print((x, y), c.color_name(c.get(x, y)), "d=%.2f" % (math.hypot(x - 15.5, y - 15.5)))
