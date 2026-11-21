from pixelbench_api import new_canvas, finish
import math

# Shared palette - one consistent style: dark outline, steel/wood/leather/gold/red
OUT = "#14181e"
ST_L = "#e8ecf4"
ST_M = "#9aa4b4"
ST_D = "#5c6474"
GD  = "#d8a93c"
GD_D = "#8a6218"
WD_M = "#7a4a22"
WD_L = "#a8703a"
WD_D = "#4a2c12"
RD  = "#b8432c"
GE  = "#4a7cc8"

def sword():
    c = new_canvas(32, 32, name="sword")
    # blade
    c.poly([(16, 2), (11, 6), (10, 10), (10, 15), (22, 15), (22, 10), (21, 6)], ST_M)
    # crossguard (gold) with dark end pieces
    c.rect(7, 14, 18, 3, GD)
    c.rect(7, 13, 2, 1, GD_D)
    c.rect(23, 13, 2, 1, GD_D)
    # grip + pommel
    c.rect(14, 16, 4, 7, WD_D)
    c.circle(16, 24, 3, GD)
    c.outline(OUT)
    # details
    c.line(16, 4, 16, 13, ST_L)
    c.line(15, 5, 15, 11, ST_L)
    c.line(14, 18, 17, 18, WD_L)
    c.line(14, 20, 17, 20, WD_L)
    c.line(14, 22, 17, 22, WD_L)
    c.set(16, 24, GE)
    return c

def teardrop(c, cx, cy, rx, ry, tip_y, col):
    pts = []
    n = 36
    for i in range(n + 1):
        a = -math.pi / 2 + math.pi * i / n
        pts.append((cx - rx * math.cos(a), cy - ry * math.sin(a)))
    pts.append((cx, tip_y))
    c.poly(pts, col)

def bow():
    c = new_canvas(32, 32, name="bow")
    for y in range(4, 29):
        t = (y - 4) / 24
        xc = 21 - round(9 * math.sin(math.pi * t))
        col = GD if y in (4, 5, 27, 28) else WD_M
        c.rect(xc - 1, y, 3, 1, col)
    c.outline(OUT)
    for y in range(4, 29):
        t = (y - 4) / 24
        xc = 21 - round(9 * math.sin(math.pi * t))
        c.rect(xc - 1, y, 1, 1, WD_L)
    c.rect(22, 4, 1, 24, ST_D)    # string
    c.rect(12, 15, 5, 3, WD_D)    # grip on the limb
    c.rect(12, 16, 5, 1, WD_L)
    c.outline(OUT)
    return c

def shield():
    c = new_canvas(32, 32, name="shield")
    # body silhouette (dome top, taper to a point)
    teardrop(c, 16, 15, 9, 13, 31, ST_M)
    # inner red field
    teardrop(c, 16, 16, 7, 10, 29, RD)
    # gold cross emblem
    c.rect(15, 8, 2, 15, GD)
    c.rect(12, 16, 7, 2, GD)
    # light rim edge up the right side
    c.line(17, 4, 23, 12, ST_L)
    c.line(23, 12, 24, 20, ST_L)
    # rivets in the border
    c.set(10, 12, GD_D); c.set(22, 12, GD_D)
    c.set(10, 20, GD_D); c.set(22, 20, GD_D)
    c.outline(OUT)
    return c

def axe():
    c = new_canvas(32, 32, name="axe")
    # bearded head (rows 0-18): blade faces left, head spans top-left
    c.poly([(24, 2), (19, 0), (14, 2), (12, 5), (11, 9), (13, 18), (20, 17), (23, 12)], ST_M)
    # handle running down to the bottom-right + wrap
    c.rect(23, 6, 4, 19, WD_M)
    c.rect(23, 8, 4, 10, WD_D)
    # gold pommel
    c.circle(25, 26, 3, GD)
    c.outline(OUT)
    # details
    c.line(13, 3, 12, 9, ST_L)
    c.line(12, 10, 14, 15, ST_L)
    c.line(16, 6, 18, 10, GD)
    c.line(16, 2, 18, 2, GD_D)
    c.line(24, 7, 24, 21, WD_L)
    c.line(24, 10, 25, 10, WD_L)
    c.line(24, 13, 25, 13, WD_L)
    c.line(24, 16, 25, 16, WD_L)
    c.set(25, 26, GE)
    return c

sw = sword()
bo = bow()
sh = shield()
ax = axe()

result = new_canvas(64, 64, name="weapon-set")
result.blit(sw, 0, 0)
result.blit(bo, 32, 0)
result.blit(sh, 0, 32)
result.blit(ax, 32, 32)

print(result.stats_text())
print("=== SWORD ===")
print(sw.matrix_text())
print("=== BOW ===")
print(bo.matrix_text())
print("=== SHIELD ===")
print(sh.matrix_text())
print("=== AXE ===")
print(ax.matrix_text())

finish(result)
