from pixelbench_api import *

W, H = 128, 128
c = new_canvas(W, H, name="red-roofed-forge-house")

# ============================================================
# COLOR PALETTE
# ============================================================
# Grass/ground
GRASS_DARK   = c.color((60, 88, 44))
GRASS_MID    = c.color((78, 108, 54))
GRASS_LIGHT  = c.color((96, 128, 66))

# Building (left wall - cool stone)
WL_DARK  = c.color((86, 88, 92))
WL_MID   = c.color((102, 104, 108))
WL_LIGHT = c.color((122, 124, 128))

# Building (right wall - warm stone)
WR_DARK  = c.color((96, 92, 88))
WR_MID   = c.color((116, 112, 106))
WR_LIGHT = c.color((138, 132, 124))

# Roof red
R_DARK   = c.color((92, 28, 20))
R_MID    = c.color((128, 44, 30))
R_LIGHT  = c.color((162, 60, 40))
R_HIGHL  = c.color((205, 92, 60))
R_BRIGHT = c.color((238, 128, 86))

# Wood
WOOD_D   = c.color((80, 50, 26))
WOOD_M   = c.color((120, 78, 40))
WOOD_L   = c.color((158, 106, 58))

# Door / interior
DOOR_D   = c.color((46, 32, 22))
DOOR_M   = c.color((68, 46, 30))

# Furnace glow
GLOW_D   = c.color((208, 98, 26))
GLOW_M   = c.color((255, 138, 42))
GLOW_L   = c.color((255, 192, 72))
GLOW_X   = c.color((255, 226, 132))

# Chimney
CH_D = c.color((88, 80, 76))
CH_M = c.color((110, 102, 98))
CH_L = c.color((132, 124, 120))

# Smoke
SMK_1 = c.color((122, 122, 128, 140))
SMK_2 = c.color((148, 148, 154, 105))

# Outlines
DARK  = c.color((18, 14, 10))

# Sign
SG_D  = c.color((66, 40, 20))
SG_M  = c.color((98, 62, 34))
SG_L  = c.color((136, 92, 53))
SG_T  = c.color((230, 212, 172))

# Barrel
BR_D  = c.color((68, 46, 24))
BR_M  = c.color((108, 74, 40))
BR_L  = c.color((148, 104, 60))
BR_H  = c.color((60, 60, 66))

# Anvil
ANV   = c.color((54, 48, 52))
ANV_H = c.color((92, 85, 90))

# Shadow
SHADOW  = c.color((28, 38, 24, 130))

# ============================================================
# GROUND
# ============================================================
c.rect(0, 0, W, H, GRASS_DARK)

# Ground highlight diamond around building
c.poly([(64, 18), (4, 66), (64, 114), (124, 66)], GRASS_MID)

# Lighter inner diamond (building platform)
c.poly([(64, 26), (12, 68), (64, 110), (116, 68)], GRASS_LIGHT)

# Ground texture speckle
import random
random.seed(42)
for _ in range(60):
    gx = random.randint(3, 124)
    gy = random.randint(3, 124)
    # Skip building area
    dx = gx - 64
    dy = gy - 68
    if abs(dx) * 0.8 + abs(dy) * 1.2 < 48:
        continue
    c.set(gx, gy, GRASS_MID)

# A few darker patches
for _ in range(25):
    gx = random.randint(5, 122)
    gy = random.randint(5, 122)
    dx = gx - 64
    dy = gy - 68
    if abs(dx) * 0.8 + abs(dy) * 1.2 < 45:
        continue
    c.set(gx, gy, GRASS_DARK)

# ============================================================
# BUILDING GEOMETRY
# Shifted up by 8 from a natural center
# Diamond footprint:
#   Back:  (64, 36)
#   Left:  (25, 66)
#   Right: (103, 66)
#   Front: (64, 95)
# Wall height: WH=24
# ============================================================
WH = 24
# Roof anchor points
RB = (64, 36)
RL = (25, 66)
RR = (103, 66)
RF = (64, 95)

# Wall bottom points
BB = (64, 36 + WH)
BL = (25, 66 + WH)
BR_ = (103, 66 + WH)
BF = (64, 95 + WH)

# ============================================================
# GROUND SHADOW
# ============================================================
c.poly([(64, 26), (20, 70), (64, 114), (108, 70)], SHADOW)

# ============================================================
# WALLS
# ============================================================
# Front-left wall
c.poly([RL, RF, BF, BL], WL_MID)
# Front-right wall
c.poly([RF, RR, BR_, BF], WR_MID)
# Back-left wall
c.poly([RB, RL, BL, BB], WL_DARK)
# Back-right wall
c.poly([RB, RR, BR_, BB], WR_DARK)

# Mortar lines (vertical) on front-left
for i in range(1, 6):
    t = i / 6.0
    x1 = RL[0] + (RF[0] - RL[0]) * t
    y1 = RL[1] + (RF[1] - RL[1]) * t
    c.line(int(x1), int(y1), int(x1), int(y1 + WH), WL_DARK)

# Horizontal mortar on front-left
for i in range(1, 6):
    y = RL[1] + WH * i // 6
    c.line(RL[0], y, RF[0], y, WL_LIGHT)

# Stone highlights front-left
c.rect(33, 74, 4, 3, WL_LIGHT)
c.rect(45, 80, 5, 3, WL_DARK)
c.rect(38, 86, 4, 3, WL_LIGHT)
c.rect(53, 84, 4, 3, WL_LIGHT)
c.rect(30, 92, 4, 3, WL_DARK)

# Mortar on front-right
for i in range(1, 6):
    t = i / 6.0
    x1 = RF[0] + (RR[0] - RF[0]) * t
    y1 = RF[1] + (RR[1] - RF[1]) * t
    c.line(int(x1), int(y1), int(x1), int(y1 + WH), WR_DARK)

for i in range(1, 6):
    y = RF[1] + WH * i // 6
    c.line(RF[0], y, RR[0], y, WR_LIGHT)

# Stone highlights front-right
c.rect(72, 78, 4, 3, WR_LIGHT)
c.rect(85, 74, 5, 3, WR_DARK)
c.rect(92, 84, 4, 2, WR_LIGHT)
c.rect(80, 88, 4, 3, WR_DARK)

# ============================================================
# ROOF
# ============================================================
# Roof overhang
Rv_B  = (64, 31)
Rv_L  = (21, 64)
Rv_R  = (107, 64)
Rv_F  = (64, 93)
Pk    = (64, 22)

# Back faces (dark)
c.poly([Rv_B, Rv_L, Pk], R_DARK)
c.poly([Rv_B, Rv_R, Pk], R_DARK)

# Front-left face (light)
c.poly([Rv_L, Rv_F, Pk], R_LIGHT)
# Front-right face (mid)
c.poly([Rv_F, Rv_R, Pk], R_MID)

# Tile lines on front-left face - radial
for i in range(1, 8):
    t = i / 8.0
    ex = Rv_L[0] + (Rv_F[0] - Rv_L[0]) * t
    ey = Rv_L[1] + (Rv_F[1] - Rv_L[1]) * t
    c.line(Pk[0], Pk[1], int(ex), int(ey), R_DARK)

# Tile rows on front-left
for i in range(1, 5):
    t = i / 5.0
    p1x = Rv_L[0] + (Pk[0] - Rv_L[0]) * t
    p1y = Rv_L[1] + (Pk[1] - Rv_L[1]) * t
    p2x = Rv_F[0] + (Pk[0] - Rv_F[0]) * t
    p2y = Rv_F[1] + (Pk[1] - Rv_F[1]) * t
    c.line(int(p1x), int(p1y), int(p2x), int(p2y), R_DARK)

# Tile lines on front-right face
for i in range(1, 8):
    t = i / 8.0
    ex = Rv_F[0] + (Rv_R[0] - Rv_F[0]) * t
    ey = Rv_F[1] + (Rv_R[1] - Rv_F[1]) * t
    c.line(Pk[0], Pk[1], int(ex), int(ey), R_DARK)

for i in range(1, 5):
    t = i / 5.0
    p1x = Rv_F[0] + (Pk[0] - Rv_F[0]) * t
    p1y = Rv_F[1] + (Pk[1] - Rv_F[1]) * t
    p2x = Rv_R[0] + (Pk[0] - Rv_R[0]) * t
    p2y = Rv_R[1] + (Pk[1] - Rv_R[1]) * t
    c.line(int(p1x), int(p1y), int(p2x), int(p2y), R_DARK)

# Roof edge highlights
c.line(Rv_L[0], Rv_L[1], Rv_F[0], Rv_F[1], R_HIGHL)
c.line(Rv_F[0], Rv_F[1], Rv_R[0], Rv_R[1], R_LIGHT)

# Peak and ridge lines
c.line(Rv_B[0], Rv_B[1], Pk[0], Pk[1], R_LIGHT)
c.line(Rv_F[0], Rv_F[1], Pk[0], Pk[1], R_BRIGHT)
c.line(Rv_L[0], Rv_L[1], Pk[0], Pk[1], R_HIGHL)
c.line(Rv_R[0], Rv_R[1], Pk[0], Pk[1], R_MID)

# Roof outline
c.poly([Rv_B, Rv_L, Rv_F, Rv_R], DARK, fill=False)

# Bright peak cap
c.circle(Pk[0], Pk[1], 1, R_BRIGHT)

# ============================================================
# CHIMNEY
# ============================================================
# On right slope of roof - make it larger and more visible
ch_x = 78
ch_y = 26
ch_w = 15
ch_h = 18
c.rect(ch_x, ch_y, ch_w, ch_h, CH_M)
c.rect(ch_x + 2, ch_y, ch_w - 4, ch_h, CH_L)
c.rect(ch_x + ch_w - 3, ch_y + 1, 3, ch_h - 1, CH_D)
c.line(ch_x + 1, ch_y + 1, ch_x + 1, ch_y + ch_h - 1, CH_L)
# Chimney cap
c.rect(ch_x - 3, ch_y - 4, ch_w + 6, 4, CH_D)
c.rect(ch_x - 2, ch_y - 4, ch_w + 4, 3, CH_M)
c.rect(ch_x - 1, ch_y - 4, ch_w + 2, 2, CH_L)
# Glow inside chimney
c.rect(ch_x + 4, ch_y - 6, 5, 3, GLOW_M)
c.rect(ch_x + 5, ch_y - 6, 3, 2, GLOW_L)

# ============================================================
# DOOR with furnace glow (front-left wall)
# ============================================================
door_x = 42
door_w = 14
door_h = 18
door_y = BF[1] - door_h  # bottom wall minus door height

# Door opening (dark interior silhouette)
c.rect(door_x, door_y, door_w, door_h, DOOR_D)
# Rounded/arched top
c.ellipse(door_x + door_w//2, door_y, door_w//2, 4, DOOR_D)
c.ellipse(door_x + door_w//2, door_y, door_w//2 - 1, 3, DOOR_M)

# Bright furnace glow inside
c.rect(door_x + 1, door_y + 1, door_w - 2, door_h - 1, GLOW_D)
c.rect(door_x + 3, door_y + 3, door_w - 6, door_h - 3, GLOW_M)
c.rect(door_x + 4, door_y + 6, door_w - 8, door_h - 8, GLOW_L)
c.rect(door_x + 5, door_y + 9, door_w - 10, door_h - 10, GLOW_X)

# Door frame (dark wood)
c.rect(door_x - 2, door_y - 1, 2, door_h + 2, WOOD_D)
c.rect(door_x + door_w, door_y - 1, 2, door_h + 2, WOOD_D)
c.rect(door_x - 2, door_y - 3, door_w + 4, 3, WOOD_D)
c.rect(door_x - 2, door_y + door_h, door_w + 4, 1, WOOD_D)

# Glow spill on ground in front of door
c.ellipse(door_x + door_w//2, door_y + door_h + 4, 8, 3, GLOW_D)
c.ellipse(door_x + door_w//2, door_y + door_h + 5, 5, 2, GLOW_L)

# ============================================================
# WINDOW (front-right wall)
# ============================================================
win_x = 74
win_w = 14
win_h = 12
win_y = 92

c.rect(win_x, win_y, win_w, win_h, GLOW_M)
c.rect(win_x + 2, win_y + 2, win_w - 4, win_h - 4, GLOW_L)
c.rect(win_x - 1, win_y - 1, win_w + 2, 1, WOOD_D)
c.rect(win_x - 1, win_y + win_h, win_w + 2, 1, WOOD_D)
c.rect(win_x - 1, win_y, 1, win_h, WOOD_D)
c.rect(win_x + win_w, win_y, 1, win_h, WOOD_D)
c.line(win_x + win_w//2, win_y, win_x + win_w//2, win_y + win_h, WOOD_D)
c.line(win_x, win_y + win_h//2, win_x + win_w, win_y + win_h//2, WOOD_D)

# ============================================================
# WOODEN SIGN (left area)
# ============================================================
pst_x = 28
pst_y = 90
c.rect(pst_x, pst_y, 3, 16, WOOD_D)

sg_x = 32
sg_w = 13
sg_h = 16
sg_y = 94
c.rect(sg_x, sg_y, sg_w, sg_h, SG_M)
c.rect(sg_x, sg_y, sg_w, 1, SG_L)
c.rect(sg_x, sg_y + sg_h - 1, sg_w, 1, SG_D)
c.rect(sg_x, sg_y, 1, sg_h, SG_D)
c.rect(sg_x + sg_w - 1, sg_y, 1, sg_h, SG_D)
# Hammer symbol
c.rect(sg_x + 5, sg_y + 3, 3, sg_h - 6, SG_D)
c.rect(sg_x + 4, sg_y + 3, 5, 2, SG_D)
# Chains
c.line(pst_x + 1, pst_y + 2, sg_x + 1, sg_y, WOOD_D)
c.line(pst_x + 1, pst_y + 2, sg_x + sg_w - 1, sg_y, WOOD_D)

# ============================================================
# BARRELS (right side, beside the building)
# ============================================================
# Bottom barrel
b1x = 104
b1y = 98
b1w = 18
b1h = 14
# Ground shadow
c.ellipse(b1x + b1w//2, b1y + b1h - 1, 10, 3, SHADOW)
# Barrel body
c.rect(b1x + 2, b1y, b1w - 4, b1h - 2, BR_M)
c.ellipse(b1x + b1w//2, b1y - 1, b1w//2 - 4, 2, BR_L)
c.ellipse(b1x + b1w//2, b1y + b1h - 3, b1w//2 - 4, 2, BR_D)
# Hoops
c.line(b1x + 2, b1y + 3, b1x + b1w - 2, b1y + 3, BR_H)
c.line(b1x + 2, b1y + b1h - 5, b1x + b1w - 2, b1y + b1h - 5, BR_H)
# Barrel top opening
c.ellipse(b1x + b1w//2, b1y - 1, b1w//2 - 5, 2, WOOD_L)
# Stave lines
c.line(b1x + 6, b1y + 1, b1x + 6, b1y + b1h - 3, BR_D)
c.line(b1x + 10, b1y + 1, b1x + 10, b1y + b1h - 3, BR_D)
c.line(b1x + 14, b1y + 1, b1x + 14, b1y + b1h - 3, BR_D)

# Top barrel
b2x = 109
b2y = 84
b2w = 15
b2h = 14
c.ellipse(b2x + b2w//2, b2y + b2h - 1, 8, 2, SHADOW)
c.rect(b2x + 2, b2y, b2w - 4, b2h - 2, BR_M)
c.ellipse(b2x + b2w//2, b2y - 1, b2w//2 - 4, 2, BR_L)
c.ellipse(b2x + b2w//2, b2y + b2h - 3, b2w//2 - 4, 2, BR_D)
c.line(b2x + 2, b2y + 3, b2x + b2w - 2, b2y + 3, BR_H)
c.line(b2x + 2, b2y + b2h - 4, b2x + b2w - 2, b2y + b2h - 4, BR_H)
c.ellipse(b2x + b2w//2, b2y - 1, b2w//2 - 5, 2, WOOD_L)
c.line(b2x + 5, b2y + 1, b2x + 5, b2y + b2h - 3, BR_D)
c.line(b2x + 10, b2y + 1, b2x + 10, b2y + b2h - 3, BR_D)

# ============================================================
# ANVIL (left of building)
# ============================================================
an_x = 24
an_y = 112
c.rect(an_x, an_y, 12, 3, ANV)
c.rect(an_x + 2, an_y - 2, 8, 2, ANV)
c.rect(an_x + 3, an_y - 4, 6, 2, ANV_H)
c.rect(an_x + 4, an_y - 5, 4, 1, GLOW_M)

# ============================================================
# SMOKE
# ============================================================
c.circle(86, 18, 4, SMK_2)
c.circle(89, 12, 5, SMK_1)
c.circle(85, 5, 4, SMK_2)

# ============================================================
# Building outlines
# ============================================================
# Wall ground edges
c.line(BL[0], BL[1], BF[0], BF[1], DARK)
c.line(BF[0], BF[1], BR_[0], BR_[1], DARK)
c.line(BB[0], BB[1], BL[0], BL[1], DARK)
c.line(BB[0], BB[1], BR_[0], BR_[1], DARK)

# Wall top corners
c.line(RL[0], RL[1], BL[0], BL[1], DARK)
c.line(RF[0], RF[1], BF[0], BF[1], DARK)
c.line(RR[0], RR[1], BR_[0], BR_[1], DARK)

# Front edge
c.line(RF[0], RF[1], BF[0], BF[1], WL_LIGHT)

# ============================================================
# Extra details
# ============================================================
# Small grass tufts around edges
for gx, gy in [(12, 62), (118, 58), (105, 115), (35, 122), (78, 20), (20, 105)]:
    c.rect(gx, gy, 3, 2, GRASS_DARK)

# Small stones on ground
for sx, sy in [(15, 100), (110, 100), (60, 120)]:
    c.rect(sx, sy, 3, 2, GRASS_DARK)

# Woodpile near left wall of the building
# Small stack of logs against the left wall
lp_x = 21
lp_y = 88
for li in range(4):
    c.rect(lp_x, lp_y + li * 2, 8, 2, WOOD_M)
c.rect(lp_x + 1, lp_y, 2, 8, WOOD_L)
c.rect(lp_x + 5, lp_y, 2, 8, WOOD_L)

# Hot coals pit / small furnace outside, left of anvil
c.ellipse(36, 114, 6, 3, GLOW_D)
c.ellipse(36, 113, 5, 2, GLOW_M)
c.ellipse(36, 112, 3, 1, GLOW_L)

# Path/stone walkway leading to door
c.rect(58, 118, 3, 2, c.color((138, 134, 128), "path_stone"))
c.rect(64, 120, 3, 2, c.color((140, 136, 130), "path_stone2"))
c.rect(53, 122, 3, 2, c.color((142, 138, 132), "path_stone3"))

# ============================================================
# Stats
# ============================================================
stats = c.stats()
print(f"Size: {stats['size']}")
print(f"Colors used: {stats['colors_used']}")
print(f"Coverage: {stats['coverage']:.1%}")
print(f"BBox: {stats['bbox']}")

finish(c)
