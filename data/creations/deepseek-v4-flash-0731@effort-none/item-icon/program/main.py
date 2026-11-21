from pixelbench_api import *

c = new_canvas(32, 32)

# Palette colors
GOLD_DARK  = "#7a5f16"
GOLD       = "#c9a227"
GOLD_LIGHT = "#e8c84a"
GOLD_HI    = "#f5e08a"
DARK       = "#171207"
BLUE_DARK  = "#0b2d5e"
BLUE       = "#1e5fc4"
BLUE_LIGHT = "#3d8bf5"
BLUE_HI    = "#7ab8ff"
CREAM      = "#f8f2d8"

# === Structure: center (16,16). Outer 31px disc dark outline.
c.circle(16, 16, 15, DARK)
c.circle(16, 16, 13, GOLD_DARK)      # dark gold rim foundation
c.circle(16, 16, 12, GOLD)            # main gold ring
c.circle(16, 16, 10, GOLD)            # inner gold plate (fills to radius 10)

# Shade inner ring bottom edge
c.circle(16, 16, 11, GOLD_DARK, fill=False)

# === Rim top-left highlight ===
for pt in [(10,6),(11,5),(12,4),(13,4),(14,3),(15,3),(16,3),(17,3),(18,4),(19,4),(20,5)]:
    c.set(pt[0], pt[1], GOLD_LIGHT)
# intense specks
for pt in [(12,4),(14,3),(16,3),(18,4)]:
    c.set(pt[0], pt[1], GOLD_HI)

# Rim bottom-right shadow hint
for pt in [(11,27),(12,28),(13,28),(14,29),(16,29),(17,29),(18,28),(19,28),(20,27),(21,26)]:
    c.set(pt[0], pt[1], GOLD_DARK)

# === Cardinal ticks (bright) ===
# North
for (x,y) in [(15,2),(16,2),(17,2),(15,1),(16,1),(17,1)]:
    c.set(x,y,GOLD_LIGHT)
c.set(16,1,GOLD_HI)
# South
for (x,y) in [(15,29),(16,29),(17,29),(15,30),(16,30),(17,30)]:
    c.set(x,y,GOLD_LIGHT)
# West
for (x,y) in [(2,15),(2,16),(2,17),(1,15),(1,16),(1,17)]:
    c.set(x,y,GOLD_LIGHT)
c.set(1,16,GOLD_HI)
# East
for (x,y) in [(29,15),(29,16),(29,17),(30,15),(30,16),(30,17)]:
    c.set(x,y,GOLD_LIGHT)
c.set(30,16,GOLD_HI)

# === Compass rose star (bronze/gold quadrants) ===
# North pointer - long bright
c.poly([(16,7),(13,14),(16,12),(19,14)], GOLD_LIGHT)
# East pointer
c.poly([(25,16),(18,13),(20,16),(18,19)], GOLD_LIGHT)
# South pointer - dark bronze
c.poly([(16,25),(13,18),(16,20),(19,18)], GOLD_DARK)
# West pointer - dark bronze
c.poly([(7,16),(14,13),(12,16),(14,19)], GOLD_DARK)

# Bright edge on north pointer
c.line(16,8,16,11, GOLD_HI)
c.set(16,7,GOLD_HI)

# Divot highlight between pointer tips and crystal - small gold-light fill
# diagonal mini-arms (NE, NW, SE, SW) tiny
for (dx,dy) in [(1,-1),(-1,-1),(1,1),(-1,1)]:
    c.set(16+dx*2, 16+dy*2, GOLD_DARK)

# === Blue crystal octagon ===
cx, cy = 16, 16
c.poly([(cx, cy-7), (cx+5, cy-3), (cx+5, cy+3), (cx, cy+7), (cx-5, cy+3), (cx-5, cy-3)], DARK)
c.poly([(cx, cy-6), (cx+4, cy-2), (cx+4, cy+2), (cx, cy+6), (cx-4, cy+2), (cx-4, cy-2)], BLUE)
c.line(cx, cy-3, cx+3, cy, BLUE_DARK)
c.line(cx, cy+3, cx+3, cy, BLUE_DARK)
c.line(cx, cy-3, cx-3, cy, BLUE_DARK)
c.line(cx, cy+3, cx-3, cy, BLUE_DARK)
c.poly([(cx, cy-4), (cx+2, cy), (cx, cy+4), (cx-2, cy)], BLUE_LIGHT)
c.poly([(cx, cy-5), (cx+2, cy-1), (cx, cy), (cx-2, cy-1)], BLUE_HI)
c.set(cx-1, cy-3, CREAM)
c.set(cx, cy-2, CREAM)
c.set(cx+1, cy-1, CREAM)
c.set(cx, cy-4, CREAM)
c.set(cx+1, cy-2, CREAM)
c.set(cx+2, cy, CREAM)

# === Rivets on gold ring at NE/NW/SE/SW ===
for (rx, ry) in [(23,9),(9,9),(23,23),(9,23)]:
    c.circle(rx, ry, 1, GOLD_HI)
# shadow under each rivet
for (rx, ry) in [(23,10),(9,10),(23,24),(9,24)]:
    c.set(rx, ry, GOLD_DARK)

print(c.stats_text())
result = c
finish(result)
