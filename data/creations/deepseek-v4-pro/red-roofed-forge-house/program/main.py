# Red-roofed forge house - isometric RTS building tile
# 128x128, clean 2:1 isometric geometry

c = new_canvas(128, 128, background=None, name="output")

# ---------------------------------------------------------------
# palette
# ---------------------------------------------------------------
def col(hexs, name):
    return c.color(hexs, name=name)

outline      = col("#2b1a12", "outline")
wood_left    = col("#8a5a34", "wood_left")
wood_right   = col("#6f4520", "wood_right")
wood_gable   = col("#7a4a28", "wood_gable")
wood_dark    = col("#4a2c14", "wood_dark")
wood_light   = col("#c9935c", "wood_light")
roof_dark    = col("#7e1f14", "roof_dark")
roof_base    = col("#b03124", "roof_base")
roof_light   = col("#d84a36", "roof_light")
roof_hi      = col("#ef6a50", "roof_hi")
tile_line    = col("#8e241c", "tile_line")
glow_yellow  = col("#fff3a0", "glow_yellow")
glow_orange  = col("#ffb340", "glow_orange")
glow_deep    = col("#ff7a1a", "glow_deep")
glow_spill   = col("#ff9a2a80", "glow_spill")
door_frame   = col("#5a3a20", "door_frame")
door_dark    = col("#2a1208", "door_dark")
sign_wood    = col("#b07948", "sign_wood")
sign_border  = col("#5a3a20", "sign_border")
sign_text    = col("#3a2210", "sign_text")
barrel_base  = col("#9a6a3a", "barrel_base")
barrel_dark  = col("#6f4520", "barrel_dark")
barrel_band  = col("#5a5a66", "barrel_band")
barrel_light = col("#c9935c", "barrel_light")
stone_light  = col("#b9b9bd", "stone_light")
stone_dark   = col("#6f6f72", "stone_dark")
stone_mid    = col("#9a9a9a", "stone_mid")
smoke        = col("#c8c8c880", "smoke")
shadow       = col("#140c0880", "shadow")

# ---------------------------------------------------------------
# isometric geometry (2:1 projection)
#   screen = X*(2,1) + Y*(-2,1) + Z*(0,-2)
# ---------------------------------------------------------------
# building footprint: world X length 30, world Y width 20
# top-of-wall diamond corners
T = (54, 37)    # back corner
R = (114, 67)   # right corner
B = (74, 87)    # front corner
L = (14, 57)    # left corner

# ground corners (wall height = 26 px vertical)
H = 26
Tb = (54, 63)
Rb = (114, 93)
Bb = (74, 113)
Lb = (14, 83)

# gabled roof ridge (world Y = 10 centerline, lifted 26 px)
P0 = (34, 21)   # ridge left/back end
P1 = (94, 51)   # ridge right/front end

# ---------------------------------------------------------------
# ground drop shadow
# ---------------------------------------------------------------
c.poly([(60, 71), (120, 101), (80, 121), (20, 91)], shadow, fill=True)

# ---------------------------------------------------------------
# walls (wooden planks)
# ---------------------------------------------------------------
# front-left face
c.poly([L, B, Bb, Lb], wood_left, fill=True)
# front-right face
c.poly([B, R, Rb, Bb], wood_right, fill=True)

# vertical plank seams
for x in range(20, 75, 6):
    c.line(x, 50 + x//2, x, 76 + x//2, wood_dark)
for x in range(80, 115, 6):
    c.line(x, 124 - x//2, x, 150 - x//2, wood_dark)

# horizontal beams (framing)
c.line(14, 60, 74, 90, wood_dark)
c.line(14, 80, 74, 110, wood_dark)
c.line(74, 84, 114, 64, wood_dark)
c.line(74, 110, 114, 90, wood_dark)

# ---------------------------------------------------------------
# door with furnace glow (front-left wall)
# ---------------------------------------------------------------
# door frame
c.poly([(36, 72), (52, 80), (52, 102), (36, 94)], door_frame, fill=True)
# glowing opening
c.poly([(38, 75), (50, 81), (50, 101), (38, 95)], glow_orange, fill=True)
# fire core
c.ellipse(44, 95, 4, 2, glow_deep, fill=True)
c.ellipse(44, 94, 2, 1, glow_yellow, fill=True)

# warm light spilling onto the ground in front of the door
c.poly([(38, 95), (50, 101), (60, 112), (28, 106)], glow_spill, fill=True)

# ---------------------------------------------------------------
# forge window (front-left wall, right of door)
# ---------------------------------------------------------------
c.poly([(58, 87), (66, 91), (66, 101), (58, 97)], glow_orange, fill=True)
c.line(62, 88, 62, 100, door_frame)
c.line(58, 94, 66, 90, door_frame)

# ---------------------------------------------------------------
# roof
# ---------------------------------------------------------------
# far/back slope
c.poly([P0, T, R, P1], roof_dark, fill=True)
# main/front slope
c.poly([P0, L, B, P1], roof_base, fill=True)

# tile courses (parallel to ridge/eave)
for t in [0.12, 0.25, 0.38, 0.5, 0.62, 0.75, 0.88]:
    qx = round(34 - 20*t); qy = round(21 + 36*t)
    rx = round(94 - 20*t); ry = round(51 + 36*t)
    c.line(qx, qy, rx, ry, tile_line)

# tile seams (perpendicular courses)
for s in [0.3, 0.5, 0.7]:
    tx = round(34 + 60*s); ty = round(21 + 30*s)
    bx = round(14 + 60*s); by = round(57 + 30*s)
    c.line(tx, ty, bx, by, roof_dark)

# ---------------------------------------------------------------
# right gable (wooden triangular wall)
# ---------------------------------------------------------------
c.poly([P1, R, B], wood_gable, fill=True)
for x in [80, 86, 92, 98, 104, 110]:
    if x <= 94:
        ytop = 51 + round(1.8 * (94 - x))
    else:
        ytop = 51 + round(0.8 * (x - 94))
    ybot = 124 - round(0.5 * x)
    if ytop < ybot:
        c.line(x, ytop, x, ybot, wood_dark)

# ---------------------------------------------------------------
# small stone chimney on the front roof slope
# ---------------------------------------------------------------
c.poly([(54, 24), (66, 24), (66, 46), (54, 40)], stone_light, fill=True)
c.poly([(66, 24), (70, 26), (70, 48), (66, 46)], stone_dark, fill=True)
c.ellipse(63, 25, 6, 2, stone_dark, fill=True)
c.ellipse(63, 25, 4, 1, door_dark, fill=True)
c.line(54, 40, 66, 46, outline)

# ---------------------------------------------------------------
# wooden sign (front-right wall)
# ---------------------------------------------------------------
c.rect(80, 84, 31, 10, sign_wood, fill=True)
c.rect(80, 84, 31, 10, sign_border, fill=False)
c.text(81, 85, "FORGE", sign_text, font="5x7")
# hanging bracket
c.line(94, 76, 94, 84, outline)
c.line(94, 80, 82, 84, outline)
c.line(94, 80, 108, 84, outline)

# ---------------------------------------------------------------
# stacked barrels (left of the door)
# ---------------------------------------------------------------
# bottom barrel
c.ellipse(26, 100, 8, 2, barrel_light, fill=True)
c.rect(18, 100, 16, 14, barrel_base, fill=True)
c.line(18, 103, 34, 103, barrel_band)
c.line(18, 111, 34, 111, barrel_band)
c.line(20, 100, 20, 113, barrel_light)
# top barrel
c.ellipse(26, 84, 8, 2, barrel_light, fill=True)
c.rect(18, 85, 16, 14, barrel_base, fill=True)
c.line(18, 88, 34, 88, barrel_band)
c.line(18, 96, 34, 96, barrel_band)
c.line(20, 85, 20, 98, barrel_light)

# ---------------------------------------------------------------
# crisp outlines
# ---------------------------------------------------------------
# walls
c.line(14, 57, 14, 83, outline)
c.line(74, 87, 74, 113, outline)
c.line(114, 67, 114, 93, outline)
c.line(14, 83, 74, 113, outline)
c.line(74, 113, 114, 93, outline)
# roof edges
c.line(54, 37, 114, 67, outline)   # back eave
c.line(14, 57, 74, 87, outline)    # front-left eave
c.line(74, 87, 114, 67, outline)   # front-right eave / gable base
c.line(34, 21, 54, 37, outline)    # left gable edge (back)
c.line(94, 51, 114, 67, outline)   # right gable edge (back)
c.line(34, 21, 14, 57, outline)    # left roof slope edge
c.line(94, 51, 74, 87, outline)    # right roof slope edge
# ridge highlight
c.line(34, 21, 94, 51, roof_hi)
# door / window frames
c.poly([(38, 75), (50, 81), (50, 101), (38, 95)], outline, fill=False)
c.poly([(58, 87), (66, 91), (66, 101), (58, 97)], outline, fill=False)
# barrel sides
c.line(18, 100, 18, 113, barrel_dark)
c.line(34, 100, 34, 113, barrel_dark)
c.line(18, 85, 18, 98, barrel_dark)
c.line(34, 85, 34, 98, barrel_dark)

# ---------------------------------------------------------------
# smoke from the chimney
# ---------------------------------------------------------------
c.circle(66, 18, 3, smoke, fill=True)
c.circle(72, 13, 4, smoke, fill=True)
c.circle(80, 10, 5, smoke, fill=True)

# ---------------------------------------------------------------
# inspect / submit
# ---------------------------------------------------------------
print(c.stats_text())
finish(c)
