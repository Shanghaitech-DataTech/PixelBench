from pixelbench_api import *

c = new_canvas(32, 32, name="steamer")

BAMBOO   = c.color("#C89F5A")
BAMBOO_D = c.color("#8B6B3D")
BAMBOO_L = c.color("#E0C084")
FILL     = c.color("#6E4F2A")
DOUGH    = c.color("#F2E3C6")
DOUGH_S  = c.color("#D9C09A")
STEAM    = c.color("#DDDDDD")
OUTLINE  = c.color("#4A3520")

# ---- basket body: y 18..29 ----
# outer walls
c.rect(4, 18, 24, 12, BAMBOO)
c.rect(6, 20, 20, 8, FILL)      # inside cavity
# rim top edge highlight
c.line(4, 18, 27, 18, BAMBOO_L)
c.line(4, 29, 27, 29, BAMBOO_D)
# vertical weave strips on walls
for x in (7, 12, 17, 22, 27):
    c.line(x, 19, x, 28, BAMBOO_D)
# horizontal weave bands
c.line(4, 22, 27, 22, BAMBOO_D)
c.line(4, 25, 27, 25, BAMBOO_D)
# re-stripe walls so bands read as weave
for x in (7, 12, 17, 22, 27):
    c.line(x, 19, x, 28, BAMBOO_D)

# ---- dumplings (three, pleated) inside cavity, y 20..24 ----
def dumpling(cx, cy):
    # body
    c.ellipse(cx, cy, 3, 2, DOUGH)
    # pleat ridge
    c.line(cx-1, cy-2, cx+1, cy-2, DOUGH_S)
    c.set(cx, cy-2, DOUGH_S)
    c.set(cx, cy-3, DOUGH)
    # shadow
    c.line(cx-2, cy+2, cx+2, cy+2, DOUGH_S)

dumpling(10, 22)
dumpling(17, 22)
dumpling(24, 22)

# ---- lid, tilted open, hinged at right side ----
# lid is an ellipse seen edge-on, raised and tilted (left side higher)
# main lid disc
c.ellipse(15, 9, 12, 4, BAMBOO)
# tilt: erase a wedge under right? Instead draw tilted ellipse via path
c.path("M 3 12 Q 14 2 27 8 Q 15 15 3 12 Z", BAMBOO, fill=True)
# lid rim (darker edge)
c.path("M 3 12 Q 14 2 27 8", BAMBOO_D, fill=False)
c.path("M 3 12 Q 15 15 27 8", BAMBOO_D, fill=False)
# knob on top of lid
c.circle(14, 5, 1, BAMBOO_D)
c.set(14, 4, BAMBOO_L)
# weave lines on lid
c.path("M 6 11 Q 14 4 24 8", BAMBOO_D, fill=False)
c.path("M 9 12 Q 15 7 22 9", BAMBOO_D, fill=False)

# ---- steam wisps rising from the open gap (left side) ----
c.line(7, 15, 6, 12, STEAM)
c.line(6, 12, 7, 10, STEAM)
c.set(7, 9, STEAM)
c.line(11, 14, 12, 11, STEAM)
c.set(12, 10, STEAM)
c.set(4, 14, STEAM)

print(c.stats_text())
save("bamboo-steamer", c)
finish(c)
