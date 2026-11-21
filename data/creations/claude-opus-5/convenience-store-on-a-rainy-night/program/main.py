import random

# ----------------------------------------------------------------------
# convenience store on a rainy night - 64x64
#   sky 0-7 | roof 8-11 | sign 12-19 | glass 21-42 | base 43-44 | street 45-63
# ----------------------------------------------------------------------
c = new_canvas(64, 64, name="store")

# ---- palette ----
SKY      = "#0d1324"
SKY_G    = "#18203a"
GLOW     = "#273454"

ROOF     = "#1f2638"
ROOF_H   = "#333c56"
WALL     = "#39415a"
WALL_D   = "#272d41"
FRAME    = "#171c29"

SIGN     = "#f2eed9"
SIGN_SH  = "#bdb9a2"
SIGN_TXT = "#1d3a6b"

GL_LIT   = "#fffce6"
GL_MAIN  = "#fff2c0"
GL_MID   = "#f6e0a0"
FLOOR    = "#e5cb8e"
SHELF    = "#c08f4d"
SHELF_D  = "#95672f"
COOLER   = "#d3eaec"
COOL_D   = "#7fabb3"
SKIN     = "#c9975f"
CLERK    = "#54607d"

P_RED    = "#c8452f"
P_BLUE   = "#2f6db5"
P_GRN    = "#74993f"
P_ORG    = "#e08a32"

GROUND   = "#1b2131"
GROUND_D = "#131926"
CURB     = "#2d3449"
SPILL    = "#554c33"
SPILL_D  = "#383522"
WATER    = "#202840"
WATER_D  = "#18203a"
REFL     = "#8f7a48"
REFL_H   = "#d4b872"

COAT     = "#e9c54e"
COAT_D   = "#b2922f"
COAT_H   = "#fff2ae"
FACE_D   = "#6a5222"
DARK     = "#101421"
DARK_H   = "#3c4255"
BOOT     = "#23252f"

# ---- night sky ----
c.rect(0, 0, 64, 45, SKY)
c.dither(0, 1, 64, 7, [SKY, SKY_G], "bayer4")
c.dither(3, 3, 58, 5, [SKY_G, GLOW], "bayer4")

# ---- street ----
c.rect(0, 45, 64, 19, GROUND)
c.line(0, 45, 63, 45, CURB)
c.dither(0, 54, 64, 10, [GROUND, GROUND_D], "bayer4")

# ---- building shell ----
c.rect(2, 8, 60, 37, WALL)
c.rect(2, 43, 60, 2, WALL_D)
c.rect(2, 8, 60, 4, ROOF)
c.line(2, 8, 61, 8, ROOF_H)
c.line(1, 11, 62, 11, FRAME)

# ---- sign band ----
c.rect(4, 12, 56, 8, FRAME)
c.rect(5, 12, 54, 7, SIGN)
c.line(5, 18, 58, 18, SIGN_SH)
c.text(21, 12, "MART", SIGN_TXT, font="5x7")
c.rect(9, 14, 3, 3, P_RED)
c.rect(51, 14, 3, 3, P_GRN)

# ---- lit glass ----
c.rect(5, 20, 54, 23, GL_MAIN)
c.rect(6, 21, 52, 3, GL_LIT)
c.rect(5, 28, 54, 9, GL_MID)
c.rect(5, 38, 54, 5, FLOOR)

# interior: shelf unit, left window
c.rect(7, 28, 10, 11, SHELF)
for row in (28, 31, 34):
    c.line(7, row + 2, 16, row + 2, SHELF_D)
    for i, col in enumerate((7, 10, 13)):
        c.rect(col, row, 2, 2, (P_RED, P_BLUE, P_ORG, P_GRN)[(i + row) % 4])
c.line(7, 38, 16, 38, SHELF_D)

# interior: drinks cooler
c.rect(19, 26, 9, 13, COOLER)
c.rect(19, 26, 9, 13, COOL_D, fill=False)
for row in (27, 31, 35):
    c.line(20, row + 2, 26, row + 2, COOL_D)
    for col in (20, 23):
        c.rect(col, row, 2, 2, P_BLUE if (col + row) % 3 else P_GRN)

# interior: counter and clerk, right window
c.rect(46, 35, 11, 4, SHELF)
c.line(46, 35, 56, 35, SHELF_D)
c.rect(50, 28, 2, 2, SKIN)          # head
c.set(50, 28, FACE_D)               # cap brim shadow
c.poly([(49, 30), (52, 30), (53, 35), (48, 35)], CLERK)
c.set(48, 32, COOL_D)               # sleeve highlight
c.rect(44, 27, 2, 8, SHELF_D)       # door-side stock rack

# ---- mullions, transom, door ----
c.line(5, 20, 58, 20, FRAME)
c.line(5, 42, 58, 42, FRAME)
c.line(5, 25, 58, 25, FRAME)
for fx in (5, 18, 29, 42, 58):
    c.line(fx, 20, fx, 42, FRAME)

c.rect(29, 21, 14, 24, FRAME)
c.rect(31, 23, 10, 21, GL_MAIN)
c.rect(31, 30, 10, 8, GL_MID)
c.rect(31, 38, 10, 6, FLOOR)
c.line(36, 23, 36, 43, FRAME)
c.rect(32, 33, 3, 1, DARK_H)
c.rect(37, 33, 3, 1, DARK_H)

# ---- warm light spilling over the wet street ----
c.poly([(6, 45), (57, 45), (63, 58), (0, 58)], SPILL)
c.dither(0, 50, 64, 6, [SPILL, SPILL_D], "bayer4")
c.dither(0, 55, 64, 9, [SPILL_D, GROUND_D], "bayer4")
c.rect(30, 45, 13, 4, SPILL)

# ---- puddles ----
c.ellipse(13, 57, 10, 3, WATER)
c.ellipse(47, 59, 13, 4, WATER)
c.ellipse(33, 51, 6, 2, WATER_D)
c.ellipse(58, 50, 5, 2, WATER_D)

# window light broken up in the water
for px, top, bot in ((5, 56, 59), (9, 55, 59), (13, 56, 58),
                     (17, 55, 58), (20, 56, 59)):
    c.line(px, top, px, bot, REFL)
for px in (8, 15):
    c.line(px, 56, px, 58, REFL_H)
for px, top, bot in ((38, 57, 62), (42, 56, 62), (46, 57, 63),
                     (50, 56, 62), (54, 57, 61), (57, 58, 61)):
    c.line(px, top, px, bot, REFL)
for px in (41, 49):
    c.line(px, 57, px, 61, REFL_H)
c.line(30, 50, 30, 52, REFL)
c.line(34, 50, 34, 52, REFL_H)
c.line(37, 50, 37, 52, REFL)
c.line(57, 49, 57, 51, REFL)

# ---- parked bicycle, silhouette on the lit pavement ----
c.circle(7, 50, 3, DARK, fill=False)    # rear wheel
c.circle(18, 50, 3, DARK, fill=False)   # front wheel
c.set(7, 50, DARK)
c.set(18, 50, DARK)
c.line(8, 49, 11, 45, DARK)     # down tube
c.line(12, 45, 17, 49, DARK)    # top tube
c.line(9, 50, 16, 50, DARK)     # chainstay
c.line(11, 45, 13, 50, DARK)    # seat tube
c.line(18, 43, 18, 49, DARK)    # fork and steerer
c.line(16, 43, 20, 43, DARK)    # handlebar
c.rect(10, 43, 3, 1, DARK)      # saddle
# wet highlights so the frame separates from the street
c.set(5, 48, DARK_H)
c.set(9, 48, DARK_H)
c.set(16, 48, DARK_H)
c.set(20, 48, DARK_H)
c.set(7, 53, REFL)
c.set(18, 53, REFL)

# ---- umbrella rack by the door ----
c.rect(46, 44, 11, 5, DARK, fill=False)
c.line(46, 46, 56, 46, DARK)
c.line(48, 44, 48, 39, P_RED)
c.path("M47 39 q1.5 -2.5 3 0", P_RED, fill=False)
c.line(51, 44, 52, 40, P_BLUE)
c.path("M51 40 q1.5 -2.5 3 0", P_BLUE, fill=False)
c.line(55, 44, 54, 41, P_GRN)
c.path("M53 41 q1.5 -2 3 0", P_GRN, fill=False)

# ---- person in a raincoat, stepping in ----
c.poly([(37, 26), (40, 30), (40, 33), (34, 33), (34, 30)], COAT)  # hood
c.rect(36, 30, 3, 2, FACE_D)        # face in shadow
c.set(34, 31, COAT_D)
c.set(39, 27, COAT_H)
c.poly([(34, 33), (40, 33), (41, 44), (33, 44)], COAT)
c.poly([(39, 33), (40, 33), (41, 44), (39, 44)], COAT_D)
c.line(34, 34, 33, 43, COAT_H)
c.line(37, 35, 37, 43, COAT_D)
c.set(33, 38, COAT)
c.rect(41, 36, 1, 3, COAT_D)
c.rect(34, 44, 3, 2, BOOT)
c.rect(38, 44, 3, 2, BOOT)
# their warm smear in the wet ground
c.line(35, 47, 35, 50, COAT_D)
c.line(39, 47, 39, 49, COAT_D)
c.set(37, 48, REFL_H)

# ---- rain ----
rain = new_canvas(64, 64, name="rain")
RAIN = "#d8e6ff66"
random.seed(7)
for _ in range(76):
    x = random.randint(1, 63)
    y = random.randint(0, 59)
    rain.line(x, y, x - 1, min(63, y + random.choice([2, 3, 3, 4])), RAIN)
# splash ticks on the kerb line
for x in (6, 24, 44, 60):
    rain.set(x, 62, RAIN)

result = flatten([c, rain], name="result")
print(result.stats_text())
view(result)
finish(result)
