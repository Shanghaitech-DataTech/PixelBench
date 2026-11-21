from pixelbench_api import *

# === 48x48 polar researcher ===
# Facing left, leaning forward into wind, heavy parka, sample case, goggles

c = new_canvas(48, 48, name="polar_researcher")

BLK    = (25, 28, 35)
Navy   = (35, 47, 72)
Base   = (52, 78, 118)
LBlue  = (84, 114, 162)
HBlu   = (128, 158, 200)
White  = (243, 248, 254)
Grey   = (168, 180, 198)
DGrey  = (110, 122, 145)
Skin   = (218, 178, 134)
DSkin  = (165, 128, 95)
Fur    = (100, 70, 54)
FurD   = (72, 50, 40)
GFrame = (35, 40, 56)
GLens  = (58, 88, 142)
Glint  = (190, 225, 255)
Case   = (184, 58, 48)
CaseD  = (132, 40, 34)
CaseL  = (220, 100, 76)
SnowW  = (248, 250, 255)

i_blk   = c.color(BLK, "black")
i_navy  = c.color(Navy, "navy")
i_base  = c.color(Base, "base")
i_lblue = c.color(LBlue, "lblue")
i_hblu  = c.color(HBlu, "hblu")
i_white = c.color(White, "white")
i_grey  = c.color(Grey, "grey")
i_dgrey = c.color(DGrey, "dgrey")
i_skin  = c.color(Skin, "skin")
i_dskin = c.color(DSkin, "dskin")
i_fur   = c.color(Fur, "fur")
i_furd  = c.color(FurD, "furd")
i_gfr   = c.color(GFrame, "gframe")
i_gls   = c.color(GLens, "glens")
i_glt   = c.color(Glint, "glint")
i_case  = c.color(Case, "case")
i_cased = c.color(CaseD, "cased")
i_casel = c.color(CaseL, "casel")
i_snow  = c.color(SnowW, "snow")

# ==========================================
# HEAD AND HOOD
# ==========================================

# Hood dome (large blue shape around head)
for y in range(2, 19):
    for x in range(18, 38):
        dx = (x - 28) / 9.5
        dy = (y - 9) / 8.0
        if dx*dx + dy*dy <= 1.0:
            c.set(x, y, i_base)

# Hood highlight left-top (wind side)
for y in range(3, 10):
    for x in range(19, 26):
        if ((x - 28) / 9.5)**2 + ((y - 9) / 8.0)**2 <= 1.0:
            c.set(x, y, i_lblue)

# Face (skin) - visible through hood opening
for y in range(6, 17):
    for x in range(20, 34):
        dx = (x - 27) / 6.5
        dy = (y - 11) / 5.5
        if dx*dx + dy*dy <= 1.0:
            c.set(x, y, i_skin)

# Goggle frame
for y in range(8, 13):
    for x in range(20, 33):
        dx = (x - 26.5) / 6.0
        dy = (y - 10.5) / 2.2
        if dx*dx + dy*dy <= 1.0:
            c.set(x, y, i_gfr)

# Goggle lens
for y in range(9, 12):
    for x in range(21, 32):
        dx = (x - 26.5) / 5.0
        dy = (y - 10.5) / 1.2
        if dx*dx + dy*dy <= 1.0:
            c.set(x, y, i_gls)

# Pale blue glint (reflection)
c.rect(21, 9, 3, 2, i_glt, fill=True)
c.set(21, 10, i_glt)
c.set(28, 9, i_glt)
c.set(28, 10, i_glt)
# Bright spot
c.set(22, 9, i_white)
c.set(29, 9, i_white)

# Face lower (nose/mouth)
c.set(23, 14, i_dskin)
c.set(25, 14, i_dskin)
c.set(24, 15, i_dskin)

# Hood fur rim 
fur_pts = [
    (19, 5), (18, 6), (17, 7), (17, 8), (17, 9), (17, 10),
    (17, 11), (17, 12), (18, 13), (18, 14), (19, 15), (20, 16),
    (21, 17), (22, 17),
    (20, 4), (22, 3), (24, 3), (26, 3), (28, 3), (30, 3),
    (32, 4), (34, 5), (35, 6), (36, 7), (37, 8),
    (36, 13), (35, 15), (33, 16), (31, 17), (29, 18),
]
for fx, fy in fur_pts:
    c.set(fx, fy, i_fur)

# Additional fur around edges
c.set(16, 8, i_fur); c.set(16, 11, i_fur); c.set(34, 5, i_furd)
c.set(18, 4, i_furd); c.set(30, 3, i_furd)
c.set(21, 3, i_furd); c.set(27, 2, i_furd)
c.set(18, 17, i_furd); c.set(25, 17, i_furd)

# ==========================================
# TORSO - leaning forward (weight to the LEFT)
# ==========================================

# Main body - heavy parka, leaning left
for y in range(17, 36):
    if y < 21:
        x0, x1 = 19, 37
    elif y < 26:
        x0, x1 = 20, 36
    else:
        x0, x1 = 21, 35
    for x in range(x0, x1 + 1):
        c.set(x, y, i_base)

# Left highlight on torso (from wind/light side)
for y in range(18, 33):
    if y < 26:
        c.set(20, y, i_lblue)
    if y < 22:
        c.set(21, y, i_lblue)
    if y < 20:
        c.set(19, y, i_lblue)

# Right shadow
for y in range(19, 34):
    if y < 25:
        c.set(36, y, i_navy)
    c.set(35, y, i_navy)

# Zipper
for y in range(20, 33):
    c.set(27, y, i_navy)

# White piping/trim on parka
for y in range(20, 29):
    c.set(23, y, i_white)

# Bottom hem
for x in range(21, 35):
    c.set(x, 34, i_navy)
    c.set(x, 35, i_navy)

# ==========================================
# SCARF
# ==========================================
# Neck wrap
for x in range(25, 35):
    c.set(x, 19, i_case)
    c.set(x, 20, i_case)
    c.set(x, 21, i_case)

# Scarf end tail flying to the right (wind blowing)
c.line(31, 19, 43, 15, i_case)
c.line(32, 20, 45, 16, i_cased)
c.set(43, 15, i_case)
c.set(44, 16, i_cased)
# Second strand
c.line(33, 21, 44, 20, i_case)
c.set(44, 20, i_cased)
# Scarf fluttering tips
c.set(42, 14, i_cased)
c.set(39, 17, i_case)

# Scarf knot
c.set(26, 19, i_cased)
c.set(27, 19, i_cased)

# ==========================================
# BACK ARM (right/back arm) - trailing
# ==========================================
# Slightly bent, trailing behind on the right
for y in range(22, 29):
    x_base = 37 + (y - 22) // 2
    for x in range(x_base, x_base + 3):
        c.set(x, y, i_navy)
    if y >= 24:
        c.set(x_base + 1, y, i_base)

# Back mitt
for y in range(29, 33):
    for x in range(38, 42):
        c.set(x, y, i_dgrey)

# Back arm separation from body
for y in range(22, 28):
    c.set(36, y, i_blk)

# ==========================================
# FRONT ARM (holding case)
# ==========================================
# Arm reaches forward and down to the left
for y in range(20, 28):
    x_base = 20 - (y - 20)
    for x in range(x_base - 1, x_base + 3):
        c.set(x, y, i_base)
    c.set(x_base - 1, y, i_lblue)

# Sleeve cuff (white)
for x in range(8, 14):
    c.set(x, 28, i_white)
    c.set(x, 29, i_white)

# Mitten/hand
for y in range(29, 32):
    for x in range(8, 12):
        c.set(x, y, i_dgrey)

# Front arm separation from body
for y in range(21, 27):
    c.set(19 - (y - 21), y, i_navy)

# ==========================================
# SAMPLE CASE
# ==========================================
# Case is held in front arm, positioned to the left-front
# Case body
for y in range(31, 40):
    for x in range(3, 16):
        c.set(x, y, i_case)

# Case top surface
for x in range(3, 16):
    c.set(x, 30, i_casel)

# Case bottom
for x in range(3, 16):
    c.set(x, 40, i_cased)

# Left highlight
for y in range(32, 39):
    c.set(4, y, i_casel)

# Right shadow edge
for y in range(32, 39):
    c.set(15, y, i_cased)

# Metal strap #1
for x in range(3, 16):
    c.set(x, 34, i_cased)
    c.set(x, 35, i_cased)

# Metal strap #2  
for x in range(3, 16):
    c.set(x, 38, i_cased)

# Latch plate
for x in range(7, 12):
    c.set(x, 31, i_grey)
    c.set(x, 32, i_grey)

# Label / ID tag 
for y in range(33, 36):
    for x in range(4, 7):
        c.set(x, y, i_white)

# Medical cross on case
for x in range(9, 13):
    c.set(x, 37, i_white)
c.set(10, 36, i_white)
c.set(11, 36, i_white)
c.set(10, 38, i_white)
c.set(11, 38, i_white)

# Case handle (gripped by hand)
for x in range(8, 12):
    c.set(x, 29, i_grey)
c.set(9, 30, i_grey)
c.set(10, 30, i_grey)

# Case bottom corners
for x in range(3, 5):
    c.set(x, 39, i_casel)
    c.set(x, 40, i_casel)

# ==========================================
# LEGS - braced against strong wind
# ==========================================
# Front/left leg, visible lower portion
for y in range(34, 40):
    if y < 37:
        x0, x1 = 23, 27
    elif y < 39:
        x0, x1 = 22, 27
    else:
        x0, x1 = 22, 26
    for x in range(x0, x1 + 1):
        c.set(x, y, i_navy)

# Boot 1 (front/left foot) - planted forward
for x in range(21, 28):
    c.set(x, 40, i_navy)
    c.set(x, 41, i_dgrey)
    c.set(x, 42, i_navy)
    c.set(x, 43, i_blk)
    c.set(x, 44, i_blk)
    c.set(x, 45, i_blk)

# Boot trim (white stripe)
for x in range(22, 27):
    c.set(x, 41, i_white)

# Boot toe extends
c.set(20, 43, i_blk)
c.set(20, 44, i_blk)

# Back/right leg - planted behind
for y in range(35, 40):
    if y < 38:
        x0, x1 = 29, 32
    else:
        x0, x1 = 28, 31
    for x in range(x0, x1 + 1):
        c.set(x, y, i_navy)

# Boot 2 (back/right foot)
for x in range(26, 33):
    c.set(x, 40, i_navy)
    c.set(x, 41, i_grey)
    c.set(x, 42, i_navy)
    c.set(x, 43, i_blk)
    c.set(x, 44, i_blk)
    c.set(x, 45, i_blk)

# Boot trim (white stripe)
for x in range(27, 32):
    c.set(x, 41, i_white)

# ==========================================
# ADDITIONAL DETAILS
# ==========================================
# Parka chest pocket detail
for x in range(30, 34):
    c.set(x, 26, i_navy)
    c.set(x, 28, i_navy)
# Pocket flap
for x in range(30, 34):
    c.set(x, 25, i_lblue)

# Hood-to-shoulder transition detail
for x in range(19, 24):
    c.set(x, 18, i_lblue)

# Wind buffeting lines near character
c.line(5, 26, 9, 26, i_lblue)
c.line(7, 39, 10, 39, i_lblue)
# Short wind streaks in open space
c.line(2, 33, 5, 33, i_lblue)
c.line(11, 22, 13, 22, i_lblue)

# ==========================================
# SNOW PARTICLES
# ==========================================
snows = [
    (1, 3), (3, 7), (5, 2), (2, 12), (7, 9),
    (4, 18), (9, 5), (3, 25), (11, 13), (6, 31),
    (2, 38), (10, 21), (14, 5), (8, 16), (4, 28),
    (12, 25), (7, 39), (2, 43), (1, 20), (13, 9),
    (9, 33), (5, 44), (12, 3), (1, 35), (3, 15),
    (8, 24), (13, 17), (6, 12), (11, 30), (15, 3),
    (16, 7), (10, 37), (5, 23), (1, 10), (18, 5),
    (19, 2), (4, 41), (15, 10), (8, 30), (12, 20),
]
for sx, sy in snows:
    c.set(sx, sy, i_snow)

# Wind streaks
c.set(1, 25, i_white); c.set(2, 25, i_white)
c.set(1, 11, i_white); c.set(2, 11, i_white)
c.set(1, 39, i_white); c.set(2, 39, i_white)
c.set(14, 30, i_white); c.set(15, 30, i_white)

print(c.stats_text())
finish(c)
