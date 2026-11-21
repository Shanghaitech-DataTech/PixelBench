from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

# ---- Base room: cool white wall, baseboard, floor tiles ----
Wall = '#E4ECF3'
WallLo = '#D3DEE9'
Base = '#B9C7D6'
Floor = '#C6D2DE'
Tile = '#AFBFCe'.replace('e', 'E')
Ceil = '#D4DFE9'
Light = '#EAF6FF'   # fluorescent cool white

c.rect(0, 0, 64, 2, Ceil)          # ceiling
c.rect(0, 0, 28, 1, Floor)         # (ceiling tint)
c.rect(0, 2, 64, 46, Wall)         # main wall (y2..47)
# fluorescent fixtures
c.rect(7, 1, 20, 2, Light)
c.rect(37, 1, 20, 2, Light)
c.rect(7, 1, 20, 1, '#FFFFFF')
c.rect(37, 1, 20, 1, '#FFFFFF')
# subtle wall shading near floor
c.rect(0, 44, 64, 4, WallLo)       # lower wall tint
c.rect(0, 48, 64, 2, Base)         # baseboard
c.rect(0, 50, 64, 14, Floor)       # floor (y50..63)
# floor tiles
for yy in (53, 56, 59, 62):
    c.line(0, yy, 63, yy, Tile)
for xx in (8, 16, 24, 32, 40, 48, 56):
    c.line(xx, 50, xx, 63, Tile)

# ---- Wall clock ----
def clock(cx, cy):
    c.circle(cx, cy, 4, '#33404C')
    c.circle(cx, cy, 3, '#FFFFFF')
    c.line(cx, cy - 1, cx, cy + 2, '#5A6b7a'.replace('b', 'B'))
    c.line(cx - 2, cy, cx, cy, '#D3452E')
    c.set(cx, cy - 2, '#33404C')
    c.line(cx - 2, cy - 1, cx + 1, cy, '#D3452E')
clock(31, 7)

# ---- Front-loading washing machines: two rows ----
def machine(x, y):
    Outline = '#7E93A6'
    Body = '#F1F5F9'
    Panel = '#44515E'
    Knob = '#D6E1EB'
    Rim = '#B6C4D1'
    Glass = '#2E5A78'
    Gl = '#95C4DB'
    # control panel
    c.rect(x, y, 19, 3, Panel)
    c.circle(x + 16, y + 1, 1, Knob)
    c.set(x + 3, y + 1, '#7FB3D4')
    # body
    c.rect(x, y + 3, 19, 15, Body)
    c.rect(x, y + 3, 19, 15, Outline, fill=False)
    # feet
    c.set(x + 2, y + 17, Outline)
    c.set(x + 16, y + 17, Outline)
    # porthole door
    c.circle(x + 9, y + 10, 5, Rim)
    c.circle(x + 9, y + 10, 4, Glass)
    c.circle(x + 9, y + 10, 5, Outline, fill=False)
    c.circle(x + 6, y + 8, 1, Gl)
    c.set(x + 8, y + 8, Gl)

# Row 1 (top)
machine(10, 11)
machine(33, 11)
# Row 2 (bottom)
machine(10, 30)
machine(33, 30)

# ---- Folding table (front, in front of machines, on floor) ----
Table = '#E8EEF5'
TableEdge = '#8FA3B4'
Leg = '#A9B9C8'
c.rect(23, 49, 18, 2, Table)
c.rect(23, 49, 18, 2, TableEdge)
c.rect(24, 51, 4, 9, Leg)
c.rect(37, 51, 4, 9, Leg)
c.rect(24, 59, 17, 1, TableEdge)

# ---- Laundry basket on floor (left) ----
Basket = '#D9BC8E'
BasketE = '#A97F4C'
c.rect(8, 57, 13, 7, Basket)
c.rect(8, 57, 13, 2, BasketE)
c.rect(8, 57, 13, 7, BasketE, fill=False)
for vx in (11, 14, 17):
    c.line(vx, 58, vx, 63, BasketE)
c.line(9, 57, 14, 55, BasketE)
c.set(15, 55, BasketE)

print(c.stats_text())
finish(c)
