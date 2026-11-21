from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, background=None, name="skill_icons")

O = "#1a1f26"          # dark outline
FR = "#ff5a1f"         # fire orange-red
FY = "#ffd23d"         # fire yellow
FD = "#d42a12"         # fire deep red
IS = "#7fd7ff"         # ice body
ID = "#3aa8e8"         # ice dark
IW = "#eaf9ff"         # ice highlight
HS = "#ff7a9e"         # heal pink
HW = "#ffffff"
HD = "#d8346e"
LS = "#ffe14d"         # lightning
LD = "#f5a623"         # lightning dark
LW = "#fffbe0"

def cell(dx, dy):
    return c.rect(dx, dy, 32, 32, "transparent")

# ---------- Fireball (top-left) ----------
cx, cy = 16, 17
# outer red-orange disc with spikes
poly = [(16,3),(18,7),(21,5),(21,9),(25,8),(23,12),(28,12),(24,16),(28,20),
        (23,20),(24,25),(20,23),(19,28),(16,24),(14,28),(12,23),(8,25),(9,20),
        (5,20),(9,16),(4,13),(9,12),(8,8),(12,9),(11,5),(14,8),(16,3)]
c.poly(poly, FR)
# middle orange
c.circle(cx, cy, 10, FD)
# yellow core
c.circle(cx, cy, 6, FY)
c.circle(cx-2, cy-2, 3, "#ffe98a")
# outline
c.poly(poly, O, fill=False)

# ---------- Ice shield (top-right) ----------
bx, by = 44, 16
shield = [(bx,6),(bx+3,6),(bx+5,4),(bx+9,4),(bx+11,6),(bx+14,7),(bx+14,15),
          (bx+12,21),(bx+8,26),(bx+6,27),(bx+4,26),(bx,20),(bx,7),(bx,6)]
c.poly(shield, IS)
c.poly(shield, O, fill=False)
# inner facet highlights
c.line(bx+4,8, bx+5,20, IW)
c.line(bx+3,7, bx+4,20, ID)
# gem
c.circle(bx+7,11,2, IW)
# snowflake center
c.circle(bx+7,14,3, IW)
c.line(bx+7,12, bx+7,16, IW)
c.line(bx+5,14, bx+9,14, IW)

# ---------- Healing (bottom-left) ----------
hx, hy = 16, 48
# rounded cross / plus
c.rect(hx-6, hy-3, 12, 6, HS)
c.rect(hx-3, hy-6, 6, 12, HS)
c.rect(hx-6, hy-3, 12, 6, O, fill=False)
c.rect(hx-3, hy-6, 6, 12, O, fill=False)
# heart in center
hp = [(hx-4,hy+1),(hx,hy-2),(hx+4,hy+1),(hx,hy+5),(hx-4,hy+1)]
c.poly(hp, HD)
c.poly(hp, O, fill=False)
# glint
c.line(hx-3, hy-4, hx-1, hy-2, IW)
c.line(hx+1, hy-4, hx+2, hy-3, IW)
c.line(hx-4, hy-1, hx-2, hy+1, IW)

# ---------- Lightning (bottom-right) ----------
b = [(43,37),(53,37),(53,44),(47,44),(48,51),(39,51),(48,59)]
c.poly(b, LS)
c.poly(b, O, fill=False)
# clean highlights
c.line(45,39, 51,39, LW)

save("skill_icons", c)
print(c.stats_text())
finish(c)
