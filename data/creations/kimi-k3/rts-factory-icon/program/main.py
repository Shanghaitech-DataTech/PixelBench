# RTS factory icon, 32x32
c = new_canvas(32, 32, background=None, name="factory")

OUT     = "#201410"
BRICK   = "#a34928"
BRICK_D = "#7a3016"
ROOF    = "#3b404c"
ROOF_L  = "#5b6172"
METAL   = "#8b939f"
METAL_D = "#474c56"
WIN     = "#ffd061"
WIN_L   = "#ffecae"
WIN_D   = "#b8862e"
SHADOW  = "#10101055"

# chimney (left)
c.rect(7, 5, 4, 9, OUT)                 # shaft outline x7..10 y5..13
c.rect(8, 6, 2, 7, BRICK)               # shaft fill x8..9 y6..12
c.set(8, 9, BRICK_D); c.set(9, 9, BRICK_D)
c.rect(6, 2, 6, 4, OUT)                 # cap outline x6..11 y2..5
c.rect(7, 3, 4, 2, METAL)               # cap fill y3..4

# right vent stack
c.rect(22, 7, 4, 6, OUT)                # x22..25 y7..12
c.rect(23, 8, 2, 4, METAL_D)
c.set(23, 8, METAL); c.set(24, 8, METAL)

# flat roof with 1px overhang
c.rect(3, 11, 26, 4, OUT)               # x3..28 y11..14
c.rect(4, 12, 24, 2, ROOF)              # y12..13
c.rect(4, 12, 24, 1, ROOF_L)            # top highlight

# brick walls
c.rect(4, 15, 24, 15, OUT)              # x4..27 y15..29
c.rect(5, 16, 22, 12, BRICK)            # x5..26 y16..27

# mortar lines + staggered joints
for y in (19, 23, 27):
    c.line(5, y, 26, y, BRICK_D)
for x in (8, 13, 18, 23):
    c.set(x, 21, BRICK_D)
for x in (10, 15, 20, 25):
    c.set(x, 17, BRICK_D); c.set(x, 25, BRICK_D)

# concrete plinth
c.rect(5, 28, 22, 1, METAL_D)

# windows
for wx in (6, 14, 22):
    c.rect(wx, 17, 4, 4, OUT)
    c.rect(wx + 1, 18, 2, 2, WIN)
    c.set(wx + 1, 18, WIN_L)
    c.set(wx + 2, 19, WIN_D)

# wall vents
for vx in (6, 21):
    c.rect(vx, 24, 5, 4, OUT)
    c.rect(vx + 1, 25, 3, 1, METAL)
    c.rect(vx + 1, 26, 3, 1, METAL_D)

# chimney smoke puffs
SMOKE_L = "#6f6f78"
SMOKE   = "#54525b"
SMOKE_D = "#3e3c44"
c.set(7, 0, SMOKE); c.set(8, 0, SMOKE_L)
c.set(9, 0, SMOKE_D)
c.set(11, 0, SMOKE_D); c.set(12, 0, SMOKE)

# roller door (center)
c.rect(13, 22, 6, 8, OUT)
c.rect(14, 23, 4, 6, METAL)
c.line(14, 24, 17, 24, METAL_D)
c.line(14, 26, 17, 26, METAL_D)
c.line(14, 28, 17, 28, METAL_D)

# soft ground shadow
c.line(5, 30, 26, 30, SHADOW)

view(c)
finish(c)
