from pixelbench_api import *

W, H = 256, 256
c = new_canvas(W, H, name="dragon_battle")

# ---------- Limited palette ----------
# Sky bands (sunset) - 6 distinct bands
SKY1 = (24, 10, 38)      # top purple
SKY2 = (45, 18, 45)      # purple-magenta
SKY3 = (75, 28, 48)      # magenta-red
SKY4 = (120, 45, 42)     # deep red-orange
SKY5 = (170, 70, 40)     # orange
SKY6 = (210, 100, 45)    # bright orange near horizon

SUN_DISC = (240, 170, 70)
SUN_BRIGHT = (252, 200, 90)
SUN_RING = (220, 130, 55)

CLOUD_DARK = (35, 22, 38)
CLOUD_LIGHT = (55, 32, 45)

MTN_FAR = (42, 25, 55)
MTN_NEAR = (58, 38, 60)

GROUND_D = (45, 38, 35)
GROUND_M = (62, 52, 45)
GROUND_L = (80, 68, 55)

STONE_D = (55, 55, 62)
STONE_M = (78, 78, 88)
STONE_L = (105, 105, 118)
STONE_HL = (130, 130, 140)

OUT_C = (10, 10, 16)

FIRE_D = (150, 30, 18)
FIRE_M = (190, 60, 20)
FIRE_L = (225, 110, 30)
FIRE_HL = (245, 170, 55)

SMOKE1 = (30, 26, 28)
SMOKE2 = (50, 44, 46)
SMOKE3 = (72, 62, 66)

DRGN_BODY = (62, 22, 50)
DRGN_DARK = (38, 14, 36)
DRGN_WING = (85, 35, 62)
DRGN_WINGD = (70, 25, 50)
DRGN_BELLY = (120, 55, 75)
DRGN_EYE = (235, 180, 60)

WPN_METAL = (125, 125, 135)
WPN_METAL2 = (90, 90, 100)
WPN_WOOD = (105, 75, 45)
WPN_WOODD = (75, 55, 32)

ARMOR_D = (50, 50, 58)
ARMOR_M = (80, 80, 90)
ARMOR_L = (115, 115, 125)
ARMOR_HL = (140, 140, 150)

SHIELD_R = (130, 30, 24)
SHIELD_D = (95, 22, 18)

BANNER = (150, 38, 28)
BANNER_D = (110, 28, 20)

WOOD_D = (65, 48, 28)
WOOD_M = (90, 66, 38)
WOOD_L = (120, 88, 50)

EMBER = (220, 110, 35)
EMBER_H = (250, 170, 60)

ARROW_C = (140, 140, 150)

# ---------- Sky: banded sunset ----------
for y in range(H):
    if y < 30:
        col = SKY1
    elif y < 60:
        col = SKY2
    elif y < 90:
        col = SKY3
    elif y < 120:
        col = SKY4
    elif y < 160:
        col = SKY5
    elif y < 195:
        col = SKY6
    else:
        col = SKY6
    for x in range(W):
        c.set(x, y, col)

# ---------- Sun ----------
sun_cx, sun_cy = 220, 165
c.circle(sun_cx, sun_cy, 14, SUN_DISC)
c.circle(sun_cx, sun_cy, 10, SUN_BRIGHT)
c.circle(sun_cx, sun_cy, 5, (255, 220, 120))
# Sun glow ring
c.circle(sun_cx, sun_cy, 20, SUN_RING, fill=False)
c.circle(sun_cx, sun_cy, 26, SUN_RING, fill=False)
# Sun strip on horizon
c.rect(sun_cx - 30, 157, 60, 3, SUN_BRIGHT)

# ---------- Clouds ----------
def draw_cloud_flat(x0, y0, w, h, col):
    c.circle(x0 + w//4, y0 + h//2, w//4, col)
    c.circle(x0 + w//2, y0 + h//3, w//3, col)
    c.circle(x0 + 3*w//4, y0 + h//2, w//4, col)
    c.circle(x0 + w//2, y0 + h//2, w//2, col)

# Upper thin clouds
draw_cloud_flat(5, 8, 70, 22, CLOUD_DARK)
draw_cloud_flat(60, 2, 55, 18, CLOUD_LIGHT)
draw_cloud_flat(130, 5, 50, 16, CLOUD_DARK)
draw_cloud_flat(195, 10, 55, 18, CLOUD_LIGHT)
draw_cloud_flat(50, 38, 45, 14, CLOUD_DARK)
draw_cloud_flat(150, 50, 40, 12, CLOUD_DARK)
draw_cloud_flat(30, 70, 60, 16, CLOUD_DARK)
draw_cloud_flat(200, 80, 50, 14, CLOUD_DARK)
draw_cloud_flat(0, 95, 35, 10, CLOUD_DARK)
draw_cloud_flat(225, 45, 30, 10, CLOUD_DARK)
# Streaky clouds near sun
draw_cloud_flat(160, 135, 45, 10, CLOUD_DARK)
draw_cloud_flat(225, 155, 30, 8, CLOUD_DARK)
draw_cloud_flat(140, 115, 35, 8, CLOUD_LIGHT)

# ---------- Distant mountains ----------
c.poly([(0, 148), (25, 130), (50, 142), (75, 124), (100, 138), (125, 128),
        (150, 140), (175, 126), (200, 142), (225, 130), (250, 145), (256, 142),
        (256, 190), (0, 190)], MTN_FAR)

c.poly([(0, 175), (30, 155), (60, 165), (90, 150), (120, 168), (150, 158),
        (180, 168), (210, 155), (240, 170), (256, 165), (256, 200), (0, 200)], MTN_NEAR)

# ---------- Ground ----------
c.rect(0, 200, W, 56, GROUND_D)
# Ground texture
import random
random.seed(7)
for gy in range(202, 256, 2):
    for gx in range(0, W, 3):
        if random.random() < 0.35:
            c.set(gx + random.randint(0, 2), gy, GROUND_M)
        elif random.random() < 0.15:
            c.set(gx + random.randint(0, 2), gy, GROUND_L)

# ---------- Castle (center-left, on a small rise) ----------
# Hill under castle
c.poly([(35, 215), (60, 205), (90, 198), (120, 196), (150, 198), (180, 205), (210, 212), (240, 218), (256, 218), (256, 240), (10, 240)], GROUND_M)

# === Main keep ===
# Keep body
c.rect(95, 180, 70, 28, STONE_M)
# Outline
c.rect(94, 179, 72, 30, OUT_C, fill=False)
# Stone texture lines
c.line(95, 187, 165, 187, STONE_L)
c.line(95, 194, 165, 194, STONE_L)
c.line(95, 201, 165, 201, STONE_L)
# Vertical stone joints
for sx in range(100, 165, 8):
    c.line(sx, 182, sx, 187, STONE_L)
    c.line(sx-3, 188, sx-3, 194, STONE_L)
    c.line(sx, 195, sx, 201, STONE_L)
    c.line(sx-3, 202, sx-3, 208, STONE_L)

# Keep top
c.rect(95, 175, 70, 5, STONE_M)
c.rect(95, 175, 70, 2, STONE_HL)

# Battlements on keep
for bx in range(95, 165, 10):
    c.rect(bx, 166, 6, 9, STONE_M)
    c.rect(bx, 166, 6, 2, STONE_HL)
    # outline each merlon
    c.rect(bx, 166, 6, 9, OUT_C, fill=False)

# === Central tower (taller) ===
c.rect(115, 152, 30, 23, STONE_M)
c.rect(114, 151, 32, 25, OUT_C, fill=False)
for bx in range(115, 145, 10):
    c.rect(bx, 146, 6, 6, STONE_M)
    c.rect(bx, 146, 6, 2, STONE_HL)
# Tower windows with fire
c.rect(127, 160, 6, 8, OUT_C, fill=True)
c.rect(128, 162, 4, 5, FIRE_L)
c.rect(128, 162, 2, 3, FIRE_HL)

# === Left wall ===
c.rect(55, 195, 42, 20, STONE_M)
c.rect(54, 194, 44, 22, OUT_C, fill=False)
for bx in range(55, 97, 9):
    c.rect(bx, 189, 5, 6, STONE_M)
    c.rect(bx, 189, 5, 2, STONE_HL)

# === Right wall ===
c.rect(165, 195, 70, 20, STONE_M)
c.rect(164, 194, 72, 22, OUT_C, fill=False)
for bx in range(165, 235, 9):
    c.rect(bx, 189, 5, 6, STONE_M)
    c.rect(bx, 189, 5, 2, STONE_HL)

# === East tower ===
c.rect(185, 178, 18, 16, STONE_M)
c.rect(184, 177, 20, 18, OUT_C, fill=False)
c.rect(187, 172, 14, 6, STONE_M)
c.rect(187, 172, 14, 2, STONE_HL)
# Fire in tower top
c.poly([(189, 172), (191, 164), (193, 171), (196, 163), (199, 173), (189, 172)], FIRE_M)
c.poly([(191, 171), (193, 166), (195, 170), (197, 167), (198, 171), (191, 171)], FIRE_L)
c.poly([(193, 170), (194, 167), (196, 169), (193, 170)], FIRE_HL)
# Tower window fire
c.rect(191, 183, 6, 6, OUT_C)
c.rect(192, 184, 4, 4, FIRE_L)

# === West tower ===
c.rect(62, 182, 18, 16, STONE_M)
c.rect(61, 181, 20, 18, OUT_C, fill=False)
c.rect(64, 176, 14, 6, STONE_M)
c.rect(64, 176, 14, 2, STONE_HL)
# Tower top fire
c.poly([(66, 176), (68, 168), (70, 175), (74, 167), (77, 176), (66, 176)], FIRE_M)
c.poly([(68, 175), (70, 171), (72, 174), (75, 169), (76, 175), (68, 175)], FIRE_L)
# Tower window
c.rect(68, 187, 4, 5, OUT_C)
c.rect(69, 188, 2, 3, FIRE_L)

# === Large fire on keep roof ===
c.poly([(100, 170), (108, 150), (115, 164), (122, 143), (130, 160), (137, 145),
        (145, 155), (155, 148), (160, 165), (160, 172), (100, 172)], FIRE_D)
c.poly([(108, 168), (112, 155), (120, 165), (128, 148), (135, 160), (142, 152),
        (150, 162), (155, 169), (108, 169)], FIRE_M)
c.poly([(112, 167), (118, 158), (125, 164), (130, 152), (137, 159), (145, 156),
        (150, 166), (112, 166)], FIRE_L)
c.poly([(118, 166), (122, 160), (130, 163), (135, 155), (140, 160), (146, 158), (148, 165), (118, 165)], FIRE_HL)

# === Additional fire on left wall ===
c.poly([(60, 193), (63, 186), (66, 192), (70, 185), (73, 194), (60, 194)], FIRE_D)
c.poly([(62, 192), (64, 188), (66, 191), (69, 187), (71, 192), (62, 192)], FIRE_M)

# Fire on right wall
c.poly([(170, 193), (173, 186), (176, 192), (180, 185), (183, 194), (170, 194)], FIRE_D)
c.poly([(172, 192), (174, 188), (176, 191), (179, 187), (181, 192), (172, 192)], FIRE_M)

# ---------- Windows with fire on keep ----------
for wx in [105, 125, 145]:
    c.rect(wx, 185, 5, 7, OUT_C)
    c.rect(wx+1, 186, 3, 5, FIRE_L)
    c.rect(wx+1, 186, 2, 3, FIRE_HL)

# Gate
c.rect(118, 193, 24, 15, OUT_C)
c.rect(120, 195, 20, 13, WOOD_D)
c.rect(120, 195, 20, 2, WOOD_L)
c.rect(120, 204, 20, 2, WOOD_L)
c.line(130, 195, 130, 208, WOOD_L)

# Arches/gate outline
c.rect(119, 194, 22, 13, OUT_C, fill=False)

# ---------- Knights on ramparts ----------
def draw_knight(x, y):
    """Knight facing right, spec+shield, anchored at y=feet."""
    # legs
    c.rect(x, y-5, 2, 5, ARMOR_D)
    c.rect(x+3, y-5, 2, 5, ARMOR_D)
    # torso
    c.rect(x-1, y-12, 7, 7, ARMOR_D)
    # helmet
    c.rect(x, y-16, 5, 5, ARMOR_L)
    c.rect(x, y-16, 5, 2, ARMOR_HL)
    # plume
    c.rect(x+4, y-17, 2, 2, BANNER)
    # shield (left arm side)
    c.rect(x-2, y-13, 3, 7, SHIELD_R)
    c.rect(x-2, y-13, 1, 7, SHIELD_D)
    # spear
    c.rect(x+6, y-22, 1, 12, WPN_WOOD)
    c.rect(x+6, y-24, 1, 3, WPN_METAL)
    # spear tip wider
    c.set(x+5, y-24, WPN_METAL)
    c.set(x+7, y-24, WPN_METAL)

# Knights on keep battlements
draw_knight(102, 172)
draw_knight(118, 172)
draw_knight(140, 172)
draw_knight(155, 172)

# Knights on left wall
draw_knight(62, 196)
draw_knight(78, 196)
draw_knight(92, 196)

# Knights on right wall
draw_knight(172, 196)
draw_knight(188, 196)
draw_knight(205, 196)
draw_knight(222, 196)
draw_knight(228, 196)

# Knights on east tower
draw_knight(192, 180)

# Knight on west tower
draw_knight(70, 184)

# ---------- Siege towers ----------
def draw_siege_tower(x0, y0):
    """Wooden siege tower from x0 to x0+24, base at y0."""
    h = 42
    # Tower body with crossed beams
    c.rect(x0, y0, 26, h, WOOD_D)
    # Vertical beams
    c.rect(x0, y0, 3, h, WOOD_M)
    c.rect(x0+23, y0, 3, h, WOOD_M)
    # Horizontal beams
    for lx in range(0, h, 10):
        c.rect(x0, y0+lx, 26, 2, WOOD_L)
    # Diagonal cross beams
    c.line(x0+3, y0+4, x0+23, y0+14, WOOD_L)
    c.line(x0+23, y0+4, x0+3, y0+14, WOOD_L)
    c.line(x0+3, y0+16, x0+23, y0+26, WOOD_L)
    c.line(x0+23, y0+16, x0+3, y0+26, WOOD_L)
    # Top platform
    c.rect(x0-2, y0-3, 30, 4, WOOD_M)
    c.rect(x0-2, y0-3, 30, 1, WOOD_L)
    # Outline
    c.rect(x0, y0, 26, h, OUT_C, fill=False)
    # Archer on top
    c.rect(x0+3, y0-10, 4, 7, ARMOR_D)
    c.rect(x0+3, y0-13, 4, 3, ARMOR_L)
    c.rect(x0+3, y0-14, 2, 2, BANNER)
    # Bow
    c.set(x0+6, y0-12, WPN_WOOD)
    c.set(x0+7, y0-10, WPN_WOOD)
    c.set(x0+6, y0-8, WPN_WOOD)
    # Second archer
    c.rect(x0+15, y0-9, 4, 6, ARMOR_D)
    c.rect(x0+15, y0-12, 4, 3, ARMOR_M)
    # Spear
    c.rect(x0+18, y0-18, 1, 8, WPN_WOOD)
    c.rect(x0+18, y0-20, 1, 2, WPN_METAL)
    # Wheel
    c.circle(x0+13, y0+42, 5, WOOD_M, fill=False)
    c.circle(x0+13, y0+42, 5, OUT_C, fill=False)
    c.circle(x0+13, y0+42, 1, OUT_C)
    # Wheel spokes
    c.line(x0+9, y0+42, x0+17, y0+42, WOOD_L)
    c.line(x0+13, y0+38, x0+13, y0+46, WOOD_L)

# Right siege towers
draw_siege_tower(205, 160)
draw_siege_tower(232, 165)

# Left siege tower
draw_siege_tower(8, 168)

# ---------- Soldiers in formation on ground ----------
def draw_soldier(x, y):
    """Small soldier, anchored at y=feet."""
    c.rect(x, y-4, 3, 4, ARMOR_D)
    c.rect(x, y-7, 3, 3, ARMOR_M)
    c.rect(x, y-8, 1, 2, BANNER)
    c.rect(x-1, y-7, 2, 3, SHIELD_R)
    c.rect(x+3, y-10, 1, 6, WPN_WOOD)
    c.rect(x+3, y-12, 1, 2, WPN_METAL)
    c.rect(x, y-4, 3, 2, ARMOR_D)

# Formation left
for i, sx in enumerate(range(30, 80, 8)):
    draw_soldier(sx, 235 - (i % 2))

# Formation right  
for i, sx in enumerate(range(155, 240, 8)):
    draw_soldier(sx, 238 - (i % 2))

# Center approaching
for i, sx in enumerate(range(100, 150, 7)):
    draw_soldier(sx, 240 - (i % 2)*3)

# Extra scattered soldiers
draw_soldier(25, 240)
draw_soldier(90, 242)
draw_soldier(150, 244)
draw_soldier(250, 240)

# ---------- Dragon ----------
# ** Dragon: large, dark dragon flying above the castle **
# Dragon body - thick muscular torso (larger, more prominent)
c.ellipse(155, 55, 48, 14, DRGN_BODY)
# Body scale texture
for bx in range(120, 195, 10):
    c.set(bx, 50, DRGN_DARK)
    c.set(bx+5, 60, DRGN_DARK)
    c.set(bx+2, 45, DRGN_DARK)
    c.set(bx+3, 55, DRGN_DARK)
# Neck reaching left-down
c.poly([(130, 48), (112, 40), (100, 36), (92, 32), (88, 35), (96, 44), (110, 52), (125, 55)], DRGN_BODY)
# Head - large dramatic head
c.ellipse(88, 34, 15, 9, DRGN_BODY)
# Upper jaw / snout
c.poly([(80, 32), (68, 28), (62, 27), (60, 31), (66, 36), (78, 40), (88, 40)], DRGN_BODY)
# Eye - glowing fierce
c.circle(82, 30, 3, DRGN_EYE)
c.circle(80, 29, 1, (255, 230, 120))
c.circle(76, 33, 1, DRGN_EYE)
# Horns - pronounced
c.poly([(90, 28), (88, 20), (94, 26), (98, 22), (100, 28)], DRGN_DARK)
c.poly([(96, 29), (98, 24), (101, 28), (104, 25), (105, 30)], DRGN_DARK)
# Jaw line + teeth
c.line(68, 36, 90, 40, DRGN_DARK)
c.set(72, 37, (200, 200, 210))
c.set(78, 38, (200, 200, 210))
c.set(84, 39, (200, 200, 210))
# Jaw open darker
c.poly([(68, 36), (60, 38), (65, 42), (75, 42), (68, 36)], DRGN_DARK)
c.set(63, 39, (200, 200, 210))
c.set(67, 40, (200, 200, 210))

# Spines on back
c.poly([(135, 42), (140, 32), (145, 41), (152, 30), (157, 41), (164, 34), (169, 42), (178, 38), (182, 45)], DRGN_DARK)
c.poly([(120, 46), (125, 38), (130, 44), (134, 36), (138, 45)], DRGN_DARK)

# Belly
c.ellipse(158, 65, 40, 8, DRGN_BELLY)
# Belly ridges
for bx in range(120, 195, 10):
    c.line(bx, 62, bx, 68, DRGN_BODY)

# Tail curling down-right, dramatic
c.poly([(200, 60), (220, 65), (240, 62), (255, 58), (250, 68), (230, 70), (210, 68), (195, 66)], DRGN_BODY)
# Tail spike tip
c.poly([(255, 58), (262, 52), (258, 62), (264, 60), (260, 66)], DRGN_DARK)
c.set(256, 56, DRGN_DARK)
# Tail detail
c.line(200, 68, 240, 65, DRGN_BELLY)
c.set(205, 63, DRGN_DARK)
c.set(220, 66, DRGN_DARK)
c.set(235, 64, DRGN_DARK)
c.set(238, 61, DRGN_DARK)

# ** Wings - massive dramatic spread wings **
# Left wing (going up-left, large)
wing_pts = [
    (125, 50), (110, 30), (96, 16), (78, 8), (60, 6), 
    (48, 14), (58, 26), (75, 32), (90, 40), (105, 47)
]
c.poly(wing_pts, DRGN_WING)
# Wing membrane (darker inner)
c.poly([(120, 47), (105, 30), (90, 18), (76, 12), (63, 12), (70, 24), (84, 32), (100, 42)], DRGN_WINGD)
# Wing bone lines
c.line(118, 44, 92, 22, DRGN_DARK)
c.line(112, 40, 78, 14, DRGN_DARK)
c.line(106, 37, 66, 8, DRGN_DARK)
c.line(98, 34, 52, 12, DRGN_DARK)
c.line(90, 30, 50, 14, DRGN_DARK)
# Wing outline
c.poly(wing_pts, DRGN_DARK, fill=False)

# Right wing (upper right, massive)
wing_pts2 = [
    (195, 58), (215, 40), (235, 25), (250, 14), (258, 20),
    (248, 32), (230, 42), (210, 52), (195, 62)
]
c.poly(wing_pts2, DRGN_WING)
# Membrane
c.poly([(200, 56), (218, 42), (235, 30), (250, 20), (244, 30), (228, 40), (210, 52)], DRGN_WINGD)
# Wing bone lines
c.line(200, 54, 235, 30, DRGN_DARK)
c.line(208, 50, 248, 22, DRGN_DARK)
c.line(218, 46, 254, 18, DRGN_DARK)
c.poly(wing_pts2, DRGN_DARK, fill=False)

# Right wing trailing edge (lower membrane)
c.poly([(200, 62), (220, 52), (240, 46), (250, 50), (240, 56), (215, 62), (198, 66)], DRGN_WING)
c.line(205, 60, 235, 50, DRGN_WINGD)
c.line(215, 57, 245, 50, DRGN_WINGD)
c.poly([(200, 62), (220, 52), (240, 46), (250, 50), (240, 56), (215, 62), (198, 66)], DRGN_DARK, fill=False)

# Dragon outline on body
c.ellipse(155, 55, 48, 14, OUT_C, fill=False)
c.circle(88, 34, 9, OUT_C, fill=False)

# Claws/talons - fearsome
c.poly([(130, 62), (126, 68), (128, 59), (122, 68), (124, 58)], DRGN_DARK)
c.poly([(160, 68), (156, 74), (158, 65), (152, 74), (154, 64)], DRGN_DARK)
c.poly([(180, 64), (176, 70), (178, 61), (172, 70), (174, 60)], DRGN_DARK)
# Front claw/reaching arm
c.poly([(110, 56), (105, 63), (107, 54), (101, 63), (103, 52), (100, 58)], DRGN_DARK)

# Breathing fire - dramatic flame beam
c.poly([(60, 34), (40, 28), (20, 32), (5, 35), (25, 40), (45, 41)], FIRE_D)
c.poly([(58, 35), (42, 31), (28, 35), (15, 37), (30, 39), (48, 40)], FIRE_M)
c.poly([(55, 36), (44, 33), (32, 36), (22, 37), (33, 38), (48, 39)], FIRE_L)
c.poly([(48, 35), (40, 34), (32, 36), (38, 37)], FIRE_HL)
# Fire glow particles
c.set(48, 30, FIRE_L)
c.set(35, 30, FIRE_M)
c.set(25, 38, FIRE_L)
c.set(15, 35, FIRE_M)

# ---------- Arrows flying ----------
# From castle toward siege towers (to the right)
arrow_pts = [
    # (x, y) start of arrow, arrow goes from castle rightward
    (170, 168),  # from right wall
    (175, 172),
    (165, 160),
]
# Draw arrows - thin lines with metal color
c.line(165, 155, 175, 155, WPN_METAL)
c.set(175, 155, WPN_METAL)
c.line(173, 153, 175, 155, WPN_METAL)  # head
c.line(173, 157, 175, 155, WPN_METAL)

c.line(195, 160, 205, 160, WPN_METAL)
c.set(205, 160, WPN_METAL)
c.line(203, 158, 205, 160, WPN_METAL)
c.line(203, 162, 205, 160, WPN_METAL)

c.line(188, 145, 196, 143, WPN_METAL)
c.set(196, 143, WPN_METAL)
c.line(194, 141, 196, 143, WPN_METAL)
c.line(194, 145, 196, 143, WPN_METAL)

# Arrows from siege towers toward castle (to the left)
c.line(200, 165, 190, 163, WPN_METAL)
c.set(190, 163, WPN_METAL)
c.line(191, 161, 190, 163, WPN_METAL)
c.line(192, 165, 190, 163, WPN_METAL)

c.line(210, 150, 200, 148, WPN_METAL)
c.set(200, 148, WPN_METAL)
c.line(201, 146, 200, 148, WPN_METAL)
c.line(202, 150, 200, 148, WPN_METAL)

# Arrows near dragon
c.line(60, 60, 68, 58, WPN_METAL)
c.line(75, 90, 85, 88, WPN_METAL)
c.line(55, 75, 63, 73, WPN_METAL)

# Arrows around ramparts
c.line(160, 186, 152, 188, WPN_METAL)
c.line(145, 200, 137, 202, WPN_METAL)
c.line(105, 160, 98, 158, WPN_METAL)
c.line(90, 178, 82, 180, WPN_METAL)

# More arrows from the left volley
c.line(40, 120, 52, 118, WPN_METAL)
c.line(62, 110, 72, 112, WPN_METAL)
c.line(35, 140, 47, 138, WPN_METAL)

# ---------- Smoke columns ----------
def draw_smoke_col(x0, y0, h, w, col):
    """Draw a smoke column from x0,y0 upward."""
    for i in range(h):
        y = y0 - i
        if y < 0:
            break
        r = w + (i * 2) // 4
        c.circle(x0, y, r, col)

# Smoke from castle
draw_smoke_col(115, 170, 70, 6, SMOKE1)
draw_smoke_col(130, 172, 55, 8, SMOKE2)
draw_smoke_col(98, 200, 45, 5, SMOKE1)
draw_smoke_col(150, 195, 50, 6, SMOKE2)
draw_smoke_col(140, 175, 60, 7, SMOKE1)
draw_smoke_col(110, 180, 50, 5, SMOKE2)

# Smoke tips (lighter, spreading)
draw_smoke_col(120, 110, 20, 10, SMOKE3)

# ---------- Embers floating up ----------
ember_positions = [
    (120, 145), (135, 138), (100, 155), (150, 148), (90, 160),
    (165, 140), (110, 130), (145, 155), (95, 150), (155, 135),
    (105, 142), (138, 128), (125, 152), (160, 158), (85, 145),
    (175, 130), (115, 120), (148, 165), (170, 150), (135, 145),
    (125, 135), (155, 140), (92, 138), (160, 125), (108, 115),
    (185, 135), (75, 152), (143, 120), (100, 128), (170, 165),
    (190, 170), (65, 168), (155, 115), (88, 128), (128, 112),
    (198, 155), (78, 140), (165, 120), (138, 105), (58, 155),
]
for ex, ey in ember_positions:
    c.set(ex, ey, EMBER)
    # some brighter
    if (ex + ey) % 3 == 0:
        c.set(ex, ey, EMBER_H)

# ---------- Dark outline on main structures ----------
# Additional dark outline strips
# Castle edges darkened
c.line(95, 180, 95, 208, OUT_C)
c.line(165, 180, 165, 208, OUT_C)
# Wall bottom edges
c.line(55, 215, 95, 208, OUT_C)
c.line(165, 215, 235, 215, OUT_C)
# Tower bases
c.line(62, 198, 80, 198, OUT_C)
c.line(185, 194, 203, 194, OUT_C)

# Gateway dark interior
c.rect(120, 200, 20, 8, OUT_C)

# Burning ground fires around castle base
c.poly([(85, 215), (90, 210), (95, 214), (100, 209), (105, 215), (85, 215)], FIRE_D)
c.poly([(88, 214), (92, 211), (96, 213), (99, 211), (102, 214), (88, 214)], FIRE_M)
c.poly([(90, 213), (93, 211), (97, 213), (90, 213)], FIRE_L)

# ---------- Extra cinematic touches ----------
# Silhouette birds (distant)
for bx, by in [(50, 100), (58, 95), (55, 103), (45, 97), (52, 92)]:
    c.set(bx, by, CLOUD_DARK)

# Ground near castle darker
c.rect(50, 215, 200, 15, GROUND_D)

# Sun streak on castle
c.rect(140, 170, 25, 4, SUN_RING)
c.line(190, 195, 210, 195, SUN_BRIGHT)

# Dramatic dark clouds at horizon under sun
draw_cloud_flat(170, 148, 80, 14, CLOUD_DARK)
draw_cloud_flat(190, 180, 65, 12, CLOUD_DARK)

# More low clouds for atmosphere
draw_cloud_flat(0, 120, 50, 14, CLOUD_DARK)
draw_cloud_flat(250, 128, 6, 10, SMOKE2)

# Ground details - scattered rocks
for rk in [(30, 245), (55, 250), (175, 248), (190, 252), (250, 245), (15, 238)]:
    c.set(rk[0], rk[1], STONE_D)
    c.set(rk[0]+1, rk[1]+1, STONE_D)

# More soldiers in the distance (tiny silhouettes)
for sx in range(55, 100, 6):
    c.rect(sx, 220, 2, 4, ARMOR_D)
    c.rect(sx+1, 217, 1, 3, STONE_D)
for sx in range(160, 200, 6):
    c.rect(sx, 222, 2, 4, ARMOR_D)
    c.rect(sx+1, 219, 1, 3, STONE_D)

# Dragon shadow on castle
c.rect(130, 182, 25, 8, STONE_D)

# Second distant dragon silhouette (small, high in the sky)
c.poly([(45, 12), (55, 8), (65, 12), (75, 8), (85, 14), (70, 15), (55, 17)], DRGN_DARK)
c.poly([(55, 12), (45, 6), (40, 10), (50, 15)], DRGN_DARK)
c.poly([(65, 13), (75, 6), (80, 10), (72, 15)], DRGN_DARK)

# Flecks of fire in the sky near the castle
c.set(160, 145, FIRE_L)
c.set(95, 130, EMBER)
c.set(170, 155, EMBER)

print(c.stats_text())

# Quick check with matrix to verify
# Check a small region
# print(c.matrix_text(region=(0, 0, 30, 30)))

finish(c)
print("Dragon battle scene complete!")
