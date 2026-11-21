from pixelbench_api import new_canvas, finish
import math

c = new_canvas(16, 16)

# Palette
OUTLINE = "#4a3008"
DARK    = "#a97b16"
MID     = "#d9a52a"
LIGHT   = "#f0c34a"
SHADE   = "#8a5f10"
STAR    = "#fff3a0"

cx, cy = 7, 7

# Coin body
c.circle(cx, cy, 6, OUTLINE)
c.circle(cx, cy, 5, DARK)
c.circle(cx, cy, 4, MID)
c.circle(cx, cy, 3, LIGHT)

# Rim highlight
c.circle(cx - 1, cy - 1, 5, LIGHT, fill=False)
c.circle(cx - 1, cy - 1, 4, LIGHT, fill=False)

# Bottom shading
c.circle(cx, cy + 1, 4, SHADE, fill=False)

# Star (5-pointed poly)
def star_poly(cg, cx, cy, R, r):
    pts_o=[]; pts_i=[]
    for k in range(5):
        a = math.radians(-90 + k*72)
        pts_o.append((cx+R*math.cos(a), cy-R*math.sin(a)))
        a = math.radians(-90 + 36 + k*72)
        pts_i.append((cx+r*math.cos(a), cy-r*math.sin(a)))
    poly=[]
    for k in range(5):
        poly.append(pts_o[k]); poly.append(pts_i[k])
    cg.poly(poly, STAR)

star_poly(c, cx, cy, 3.2, 1.3)

print(c.stats_text())
finish(c)
