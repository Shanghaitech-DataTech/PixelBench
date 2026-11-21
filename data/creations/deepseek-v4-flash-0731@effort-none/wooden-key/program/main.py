from pixelbench_api import *

c = new_canvas(16, 16, name="wooden_key")

# Palette - wooden key colors (4 distinct visible)
wood_dark = c.color("#4a2e15")   # outline / shadow - 'a'
wood_mid  = c.color("#9a6636")   # main body - 'b'
wood_light= c.color("#c9863f")   # highlight - 'c'
wood_pale = c.color("#e8c28a")   # brightest highlight - 'd'

# ============================================================
# WOODEN KEY - clean, centered silhouette
# Ring left, shaft to bit at right, teeth dropping down
# ============================================================

# ----- RING (hollow) cols 1-7, rows 0-7 -----
for x in (2,3,4,5,6):
    c.set(x,0,wood_dark); c.set(x,7,wood_dark)
for y in (1,2,3,4,5,6):
    c.set(1,y,wood_dark); c.set(7,y,wood_dark)
for y in (1,2,3,4,5,6):
    c.set(2,y,wood_mid); c.set(6,y,wood_mid)
for x in (2,3,4,5,6):
    c.set(x,1,wood_mid); c.set(x,6,wood_mid)
# ring highlight
for x in (2,3,4,5): c.set(x,1,wood_light)
c.set(2,1,wood_pale); c.set(3,1,wood_pale)
c.set(2,2,wood_light); c.set(2,3,wood_light)

# ----- SHAFT (cols 8-11, rows 3-4) -----
for x in (8,9,10,11):
    c.set(x,2,wood_dark); c.set(x,3,wood_mid); c.set(x,4,wood_mid); c.set(x,5,wood_dark)
for x in (9,10):
    c.set(x,3,wood_light)
c.set(9,3,wood_pale)

# ----- BIT (head at right) cols 12-14, rows 1-7 -----
for x in (12,13,14):
    for y in (1,2,3,4,5,6,7):
        c.set(x,y,wood_mid)
# bit outline
for x in (12,13,14): c.set(x,1,wood_dark)
for y in (2,3,4,5,6,7): c.set(14,y,wood_dark)
c.set(12,7,wood_dark); c.set(13,7,wood_dark); c.set(14,7,wood_dark)
# bit highlight
c.set(13,2,wood_light); c.set(13,3,wood_light); c.set(13,4,wood_light)

# ----- TEETH -----
# Two teeth form a stepped edge below the bit
# Tooth A (col 14, longest)
c.set(14,8,wood_mid); c.set(14,9,wood_mid); c.set(14,10,wood_mid)
c.set(14,11,wood_dark)         # bottom
# Tooth B (col 13, medium)
c.set(13,8,wood_mid); c.set(13,9,wood_mid)
c.set(13,10,wood_dark)         # bottom (a step up from tooth A)
# left wall under the bit (col 12) to frame the teeth
c.set(12,8,wood_dark)
# tooth highlights
c.set(14,9,wood_light); c.set(14,10,wood_light)
c.set(13,9,wood_light)

# wood grain suggestion on bit
c.set(12,4,wood_dark)

print(c.stats_text())
print(c.matrix_text())
result = c.copy(name="result")
finish(result)
