from pixelbench_api import *

OUT = "#1a120c"      # dark outline
LEA = "#7a3f1d"      # leather
LEA_D = "#5a2c12"    # leather shade / spine
LEA_L = "#96552c"    # leather highlight
MET = "#b8b2a0"      # metal
MET_L = "#e2dcc8"    # metal highlight
PAG = "#e6d9b8"      # page edge

c = new_canvas(32, 32, name="spellbook")

# main cover body (spine on left at x=5..8, cover x=8..27, y=7..25)
c.rect(5, 7, 23, 19, LEA)
# spine strip
c.rect(5, 7, 4, 19, LEA_D)
# page edges peeking on right
c.rect(26, 9, 2, 15, PAG)

# outlines
c.line(5, 6, 27, 6, OUT)      # top
c.line(5, 26, 27, 26, OUT)    # bottom
c.line(4, 7, 4, 25, OUT)      # left (spine outer)
c.line(28, 8, 28, 24, OUT)    # right, around pages
# spine/cover seam
c.line(9, 7, 9, 25, OUT)
# page edge top/bottom ticks
c.set(27, 8, OUT); c.set(28, 8, OUT)
c.set(27, 24, OUT); c.set(28, 24, OUT)
c.set(27, 7, OUT); c.set(28, 7, OUT)
c.set(27, 25, OUT); c.set(28, 25, OUT)

# leather highlight on top edge of cover
c.line(10, 8, 26, 8, LEA_L)
# subtle leather shading bottom
c.line(10, 24, 26, 24, LEA_D)

# metal corners (cover corners): top-left of cover, bottom-left, top-right, bottom-right
def corner(cx, cy, dx, dy):
    # L-shaped metal corner 3x3
    for i in range(3):
        c.set(cx + dx * i, cy, MET)
        c.set(cx, cy + dy * i, MET)
    c.set(cx + dx, cy + dy, MET)
    c.set(cx + dx * 2, cy, MET_L)
    c.set(cx, cy + dy * 2, MET_L)

corner(10, 8, 1, 1)     # top-left of cover
corner(10, 24, 1, -1)   # bottom-left
corner(26, 8, -1, 1)    # top-right
corner(26, 24, -1, -1)  # bottom-right

# clasp on right edge middle
c.rect(26, 15, 3, 3, MET)
c.set(28, 16, MET_L)
c.set(26, 15, OUT); c.set(26, 17, OUT)
c.set(28, 15, OUT); c.set(28, 17, OUT)

# rune emblem on cover centre
c.line(17, 12, 19, 12, MET)
c.line(17, 13, 19, 13, MET)
c.set(18, 14, MET)
c.line(17, 15, 19, 15, MET_L)
c.set(18, 16, MET)

# spine ridges (bands)
for yy in (10, 22):
    c.line(5, yy, 8, yy, OUT)

print(c.stats_text())

save("leather-spellbook", c, indexed=True)
finish(c)
print(c.matrix_text())
