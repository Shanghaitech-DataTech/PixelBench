import math
from pixelbench_api import new_canvas

c = new_canvas(16, 16)
OUTLINE = "#4a3008"; DARK = "#a97b16"; MID = "#d9a52a"
LIGHT = "#f0c34a"; SHADE = "#8a5f10"; STAR = "#fff3a0"
c.circle(7, 7, 6, OUTLINE)
c.circle(7, 7, 5, DARK)
c.circle(7, 7, 4, MID)
c.circle(7, 7, 3, LIGHT)
c.circle(6, 6, 5, LIGHT, fill=False)
c.circle(6, 6, 4, LIGHT, fill=False)
c.circle(7, 8, 4, SHADE, fill=False)
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
star_poly(c, 7, 7, 3.2, 1.3)
print(c.matrix_text(region=(0,0,15,15)))
