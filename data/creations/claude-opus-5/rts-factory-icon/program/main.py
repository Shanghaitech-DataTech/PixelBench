c = new_canvas(32, 32, name="output")

# palette
OUT = c.color("#241a16", "outline")
BRK_D = c.color("#6e2f24", "brick_dark")
BRK = c.color("#9c4330", "brick")
BRK_L = c.color("#bf5a3c", "brick_light")
ROOF_D = c.color("#3a4047", "roof_dark")
ROOF = c.color("#555f69", "roof")
ROOF_L = c.color("#788695", "roof_light")
MET_D = c.color("#4a555f", "metal_dark")
MET = c.color("#8d99a6", "metal")
MET_L = c.color("#c3cdd6", "metal_light")
WIN = c.color("#2b3b4a", "window")
WIN_L = c.color("#6fc2d9", "window_lit")
SMOKE_D = c.color("#8e99a3", "smoke_dark")
SMOKE = c.color("#c2cad1", "smoke")

# ============ behind the roof: chimney and metal stack ============
# brick chimney shaft
c.rect(7, 4, 6, 11, OUT)
c.rect(8, 5, 4, 10, BRK)
c.rect(8, 5, 1, 10, BRK_L)
c.rect(11, 5, 1, 10, BRK_D)
for y in (7, 10, 13):
    c.rect(8, y, 4, 1, BRK_D)
# chimney cap
c.rect(6, 1, 8, 4, OUT)
c.rect(7, 2, 6, 2, MET)
c.rect(7, 2, 6, 1, MET_L)

# metal stack, right
c.rect(23, 6, 5, 9, OUT)
c.rect(24, 7, 3, 8, MET)
c.rect(24, 7, 1, 8, MET_L)
c.rect(26, 7, 1, 8, MET_D)
c.rect(22, 3, 7, 4, OUT)
c.rect(23, 4, 5, 2, MET)
c.rect(23, 4, 5, 1, MET_L)

# ============ flat roof slab ============
c.rect(2, 12, 28, 4, OUT)
c.rect(3, 13, 26, 2, ROOF)
c.rect(3, 13, 26, 1, ROOF_L)

# ============ brick body ============
c.rect(3, 15, 26, 15, OUT)
c.rect(4, 16, 24, 13, BRK)
c.rect(4, 16, 1, 13, BRK_L)
c.rect(27, 16, 1, 13, BRK_D)
# mortar courses
for y in (19, 22, 25, 28):
    c.rect(5, y, 22, 1, BRK_D)
# staggered vertical joints
for y, off in ((17, 5), (20, 7), (23, 5), (26, 7)):
    for x in range(off, 27, 4):
        c.set(x, y, BRK_D)

# ============ roof vent housing (louvred) ============
c.rect(13, 8, 9, 5, OUT)
c.rect(14, 9, 7, 3, MET)
c.rect(14, 9, 7, 1, MET_L)
for x in (15, 17, 19):
    c.rect(x, 10, 1, 2, MET_D)

# ============ main door ============
c.rect(12, 20, 9, 10, OUT)
c.rect(13, 21, 7, 8, MET)
c.rect(13, 21, 7, 1, MET_L)
for y in (23, 25, 27):
    c.rect(13, y, 7, 1, MET_D)

# ============ lit windows flanking the door ============
for wx in (6, 21):
    c.rect(wx, 17, 5, 4, OUT)
    c.rect(wx + 1, 18, 3, 2, WIN)
    c.rect(wx + 1, 18, 3, 1, WIN_L)

# ============ wall vent grilles ============
for vx in (6, 21):
    c.rect(vx, 24, 5, 5, OUT)
    c.rect(vx + 1, 25, 3, 3, MET_D)
    c.rect(vx + 1, 25, 3, 1, MET_L)
    c.rect(vx + 1, 27, 3, 1, MET)

# ============ smoke ============
c.rect(14, 0, 2, 2, SMOKE)
c.set(16, 1, SMOKE_D)
c.set(17, 0, SMOKE)
c.set(13, 1, SMOKE_D)

view(c)
save("rts-factory", c)
finish(c)
