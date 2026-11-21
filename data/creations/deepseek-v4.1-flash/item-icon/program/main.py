from pixelbench_api import *

# 32x32 inventory icon: ancient golden compass, blue crystal centre, top-down
c = new_canvas(32, 32, name="icon")

DARK   = '#140d18'   # thick dark outline
GOLD_H = '#fff6c8'   # specular
GOLD_L = '#f2c552'
GOLD   = '#b8832a'
GOLD_D = '#7d5212'
GOLD_X = '#523208'   # engraved line
FACE   = '#3d2812'   # recessed dial, lit side
FACE_D = '#231609'   # recessed dial, shadow side
CRY_X  = '#0a1638'   # gem contour
CRY_DD = '#123a86'
CRY_D  = '#1a55b4'
CRY    = '#2478e0'
CRY_L  = '#6ccdff'
CRY_H  = '#cdf4ff'
WHITE  = '#ffffff'

CX = CY = 15.5
TAU = 1.4142135


def dxy(x, y):
    return x - CX, y - CY


# ------------------------------------------------------------------ bezel
for y in range(32):
    for x in range(32):
        dx, dy = dxy(x, y)
        d = (dx * dx + dy * dy) ** 0.5
        if d > 14.0:
            continue
        if d > 12.1:                              # thick dark outline ring
            c.set(x, y, DARK)
        elif d > 9.3:                             # gold rim, bevelled
            u = (dx + dy) / (d * TAU)             # -1 upper-left .. +1 lower-right
            if u < -0.35:
                col = GOLD_L
            elif u < 0.40:
                col = GOLD
            else:
                col = GOLD_D
            if u < -0.45 and d > 11.0:
                col = GOLD_H                       # polished specular arc
            c.set(x, y, col)
        elif d > 8.7:                             # engraved inner line
            c.set(x, y, GOLD_X)
        else:                                     # recessed dial face
            u = (dx + dy) / (d * TAU) if d else 0.0
            c.set(x, y, FACE if u < 0.0 else FACE_D)

# ------------------------------------------------- blue crystal (rhombus gem)
for y in range(32):
    for x in range(32):
        dx, dy = dxy(x, y)
        R = abs(dx) + abs(dy)
        if R > 7.5:
            continue
        if R > 6.6:                               # dark gem contour
            c.set(x, y, CRY_X)
            continue
        # four crown facets (light from the upper left)
        if dx < 0 and dy < 0:
            col = CRY_L
        elif dx >= 0 and dy < 0:
            col = CRY
        elif dx < 0:
            col = CRY_D
        else:
            col = CRY_DD
        if R > 6.1:                               # girdle highlight on top edge
            if dy < 0:
                col = CRY_H if dx < 0 else CRY_L
            elif dx < 0:
                col = CRY
        c.set(x, y, col)

# facet ridges running from the centre to the four points
for y in range(32):
    for x in range(32):
        dx, dy = dxy(x, y)
        R = abs(dx) + abs(dy)
        if R > 6.5:
            continue
        if abs(dx) < 0.6:                         # vertical ridge
            c.set(x, y, CRY_H if dy < 0 else CRY)
        elif abs(dy) < 0.6:                       # horizontal ridge
            c.set(x, y, CRY_H if dx < 0 else CRY_L)

# glint on the north point of the crystal
c.set(15, 10, WHITE)
c.set(16, 10, CRY_H)

# ---------------------------------------- gold dial studs on the diagonals
for (px, py) in ((10, 10), (21, 10), (10, 21), (21, 21)):
    c.set(px, py, GOLD_L)
    for (ox, oy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        c.set(px + ox, py + oy, GOLD)

print(c.stats_text())
save("golden_compass_icon", c)
finish(c)
