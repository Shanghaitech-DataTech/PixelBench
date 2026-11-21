# City bus, side view (facing right), 64x32, transparent background
from pixelbench_api import new_canvas, finish, view, save

c = new_canvas(64, 32, background=None, name="city-bus")

# ---- palette ----
BODY    = c.color("#E3E7EB", name="body")
ROOF    = c.color("#C6CCD2", name="roof")
PANEL   = c.color("#CFD5DA", name="panel")
SKIRT   = c.color("#3A3F46", name="skirt")
STRIPE  = c.color("#2E7DD1", name="stripe")
GLASS   = c.color("#8FCDE4", name="glass")
GLASS_T = c.color("#5FA8C4", name="glass_top")
FRAME   = c.color("#4A5058", name="frame")
DARK    = c.color("#14161A", name="dark")
AMBER   = c.color("#FFB03A", name="display_text")
HEADL   = c.color("#FFE9A8", name="headlight")
TAIL    = c.color("#D8352A", name="taillight")
HUB     = c.color("#9AA0A8", name="hub")

# ---- roof + AC unit ----
c.rect(18, 6, 14, 1, PANEL)          # AC unit top  x=18..31
c.rect(18, 7, 14, 1, HUB)            # AC unit shade
c.rect(4, 8, 55, 1, ROOF)            # roof line y=8

# ---- body ----
c.rect(3, 9, 57, 14, BODY)           # main body y=9..22, x=3..59
c.rect(58, 9, 2, 12, PANEL)          # front face panel x=58..59
c.rect(3, 19, 57, 2, STRIPE)         # livery stripe y=19..20
c.rect(3, 21, 57, 2, SKIRT)          # skirt y=21..22

# ---- electronic route display (front top, dot matrix) ----
c.rect(45, 8, 13, 5, DARK)           # panel x=45..57, y=8..12
# digit "1"
c.rect(49, 8, 1, 5, AMBER)
c.set(48, 9, AMBER)
c.rect(48, 12, 3, 1, AMBER)
# digit "2"
c.rect(53, 8, 3, 1, AMBER)
c.set(55, 9, AMBER)
c.rect(53, 10, 3, 1, AMBER)
c.set(53, 11, AMBER)
c.rect(53, 12, 3, 1, AMBER)

# ---- window band y=14..18 ----
c.rect(6, 14, 22, 5, GLASS)          # rear group x=6..27
c.rect(6, 14, 22, 1, GLASS_T)
for px in (12, 18, 23):
    c.rect(px, 14, 1, 5, BODY)       # pillars
c.rect(37, 14, 9, 5, GLASS)          # mid group x=37..45
c.rect(37, 14, 9, 1, GLASS_T)
c.rect(41, 14, 1, 5, BODY)
c.rect(55, 14, 3, 5, GLASS)          # driver window x=55..57
c.rect(55, 14, 3, 1, GLASS_T)

# ---- doors (two-leaf, glass upper half) ----
def door(x0):
    c.rect(x0, 13, 7, 10, FRAME, fill=False)   # y=13..22
    c.rect(x0 + 1, 14, 2, 5, GLASS)
    c.rect(x0 + 4, 14, 2, 5, GLASS)
    c.rect(x0 + 3, 14, 1, 8, FRAME)            # centre split y=14..21
door(29)   # rear door  x=29..35
door(47)   # front door x=47..53

# ---- lights ----
c.rect(58, 15, 2, 3, HEADL)          # headlight, front face
c.rect(3, 15, 2, 3, TAIL)            # taillight, rear edge

# ---- wheels + arches ----
c.clear(9, 20, 9, 3)                 # rear arch x=9..17, y=20..22
c.clear(38, 20, 9, 3)                # front arch x=38..46
c.circle(13, 23, 3, DARK)            # rear tire
c.circle(42, 23, 3, DARK)            # front tire
c.circle(13, 23, 1, HUB)
c.circle(42, 23, 1, HUB)
c.set(13, 23, DARK)
c.set(42, 23, DARK)

# ---- bumpers + mirror ----
c.rect(59, 21, 3, 3, SKIRT)          # front bumper x=59..61
c.rect(1, 21, 2, 3, SKIRT)           # rear bumper x=1..2
c.line(58, 8, 59, 7, SKIRT)          # mirror stem
c.set(60, 6, DARK)                   # mirror head
c.set(60, 7, DARK)

print(c.stats_text())
print(c.matrix_text(region=(0, 4, 63, 28)))
view(c)
save("city-bus", c)

finish(c)
