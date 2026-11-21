import numpy as np
import math
from pixelbench_api import *

# Initialize canvas
W, H = 256, 256

PALETTE = {
    # Sky and Atmosphere
    "sky_0": (24, 30, 42),
    "sky_1": (42, 54, 70),
    "sky_2": (68, 86, 106),
    "sky_3": (102, 124, 146),
    "sky_4": (144, 168, 188),
    "sky_5": (188, 206, 218),
    "sky_6": (222, 234, 240),
    "sky_7": (244, 248, 250),

    # Sun / Moon
    "sun_0": (255, 252, 240),
    "sun_1": (250, 235, 200),
    "sun_2": (230, 208, 170),
    "sun_3": (198, 180, 150),

    # Distant Mountains
    "mtn_far_0": (90, 110, 130),
    "mtn_far_1": (115, 138, 158),
    "mtn_far_2": (145, 168, 186),
    "mtn_far_3": (175, 195, 210),

    # Mid Mountains / Karst Peaks
    "mtn_mid_0": (26, 35, 46),
    "mtn_mid_1": (40, 52, 66),
    "mtn_mid_2": (58, 74, 92),
    "mtn_mid_3": (80, 100, 120),
    "mtn_mid_4": (110, 132, 150),

    # Foreground Cliff / Rocks
    "rock_0": (12, 16, 22),
    "rock_1": (22, 28, 38),
    "rock_2": (36, 46, 58),
    "rock_3": (54, 66, 80),
    "rock_4": (78, 92, 108),
    "rock_5": (110, 126, 142),
    "moss_0": (28, 42, 30),
    "moss_1": (46, 68, 48),
    "moss_2": (72, 98, 70),

    # Pine Branch
    "pine_wood_0": (16, 20, 24),
    "pine_wood_1": (32, 36, 40),
    "pine_wood_2": (52, 54, 56),
    "pine_leaf_0": (18, 32, 26),
    "pine_leaf_1": (30, 52, 40),
    "pine_leaf_2": (48, 80, 60),

    # Bamboo Hat (Douli)
    "douli_shadow": (42, 28, 14),
    "douli_dark":   (76, 54, 28),
    "douli_base":   (120, 92, 48),
    "douli_mid":    (162, 130, 72),
    "douli_light":  (198, 168, 104),
    "douli_hi":     (228, 202, 142),
    "douli_bright": (248, 228, 180),

    # Skin Tones & Face
    "skin_dark":   (82, 48, 38),
    "skin_shadow": (128, 82, 64),
    "skin_base":   (172, 120, 96),
    "skin_mid":    (208, 158, 130),
    "skin_light":  (234, 194, 168),
    "skin_hi":     (248, 222, 202),
    "lip_red":     (170, 80, 84),
    "eye_white":   (210, 218, 226),

    # Hair
    "hair_0": (10, 12, 16),
    "hair_1": (20, 24, 32),
    "hair_2": (36, 44, 56),
    "hair_3": (56, 68, 84),
    "hair_4": (84, 102, 124),

    # Dark Robe
    "robe_darkest": (8, 10, 14),
    "robe_shadow":  (16, 20, 28),
    "robe_base":    (26, 32, 44),
    "robe_mid_low": (38, 48, 64),
    "robe_mid":     (54, 68, 88),
    "robe_light":   (74, 92, 118),
    "robe_hi":      (104, 126, 156),
    "robe_rim":     (148, 172, 202),

    # Inner Robe / Trim
    "inner_0": (34, 40, 50),
    "inner_1": (64, 76, 92),
    "inner_2": (116, 132, 150),
    "inner_3": (180, 194, 210),
    "inner_4": (230, 238, 246),

    # Crimson Sash & Knots
    "sash_dark":   (56, 12, 18),
    "sash_shadow": (92, 20, 28),
    "sash_base":   (144, 28, 40),
    "sash_mid":    (196, 44, 58),
    "sash_light":  (232, 74, 88),
    "sash_hi":     (250, 128, 138),

    # Gold / Bronze Ornaments
    "gold_0": (58, 40, 14),
    "gold_1": (108, 78, 26),
    "gold_2": (168, 126, 42),
    "gold_3": (224, 178, 64),
    "gold_4": (252, 222, 122),

    # Jade Pendant
    "jade_0": (20, 48, 40),
    "jade_1": (38, 86, 72),
    "jade_2": (72, 144, 122),
    "jade_3": (148, 212, 192),

    # Straight Jian Sword
    "sword_wood":  (24, 16, 20),
    "sword_wood_l":(44, 28, 36),
    "steel_0":     (22, 26, 32),
    "steel_1":     (48, 56, 68),
    "steel_2":     (92, 106, 124),
    "steel_3":     (156, 174, 194),
    "steel_4":     (235, 244, 252),

    # Boots & Leg Wraps
    "boot_0": (14, 14, 16),
    "boot_1": (28, 26, 28),
    "boot_2": (48, 44, 46),
    "boot_3": (76, 70, 72),
    "boot_wrap": (118, 108, 100),

    # Drifting Autumn/Bamboo Leaves
    "leaf_0": (112, 34, 22),
    "leaf_1": (174, 58, 32),
    "leaf_2": (222, 94, 46),
    "leaf_3": (246, 152, 74),

    # Outline & Deep Shadow
    "black": (6, 8, 12),
}

# Drawing buffer
grid = np.full((H, W), "sky_0", dtype=object)

def set_px(x, y, col):
    if 0 <= x < W and 0 <= y < H:
        grid[y, x] = col

def draw_line(x0, y0, x1, y1, col):
    x0, y0, x1, y1 = int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1))
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    x, y = x0, y0
    while True:
        set_px(x, y, col)
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy

def draw_rect(x, y, w, h, col, fill=True):
    for j in range(y, y + h):
        for i in range(x, x + w):
            if fill or (i == x or i == x + w - 1 or j == y or j == y + h - 1):
                set_px(i, j, col)

def draw_circle(cx, cy, r, col, fill=True):
    cx, cy, r = int(round(cx)), int(round(cy)), int(round(r))
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            d2 = (x - cx)**2 + (y - cy)**2
            if fill:
                if d2 <= r*r:
                    set_px(x, y, col)
            else:
                if (r - 0.7)**2 <= d2 <= (r + 0.7)**2:
                    set_px(x, y, col)

def draw_ellipse(cx, cy, rx, ry, col, fill=True):
    cx, cy = int(round(cx)), int(round(cy))
    rx, ry = max(1, int(round(rx))), max(1, int(round(ry)))
    for y in range(cy - ry, cy + ry + 1):
        for x in range(cx - rx, cx + rx + 1):
            val = ((x - cx)**2) / (rx*rx) + ((y - cy)**2) / (ry*ry)
            if fill:
                if val <= 1.0:
                    set_px(x, y, col)
            else:
                if 0.85 <= val <= 1.15:
                    set_px(x, y, col)

def draw_poly(pts, col):
    pts = np.array(pts, dtype=np.float32)
    min_y = int(np.floor(np.min(pts[:, 1])))
    max_y = int(np.ceil(np.max(pts[:, 1])))
    n = len(pts)
    for y in range(max(0, min_y), min(H, max_y + 1)):
        nodes = []
        for i in range(n):
            j = (i + 1) % n
            y0, y1 = pts[i, 1], pts[j, 1]
            x0, x1 = pts[i, 0], pts[j, 0]
            if (y0 <= y < y1) or (y1 <= y < y0):
                if y1 != y0:
                    x = x0 + (y - y0) / (y1 - y0) * (x1 - x0)
                    nodes.append(x)
        nodes.sort()
        for k in range(0, len(nodes), 2):
            if k + 1 < len(nodes):
                x_start = int(np.ceil(nodes[k]))
                x_end = int(np.floor(nodes[k+1]))
                for x in range(max(0, x_start), min(W, x_end + 1)):
                    set_px(x, y, col)

# ----------------- 1. BACKDROP -----------------
sky_bands = [
    (0, 25, "sky_0"),
    (25, 55, "sky_1"),
    (55, 85, "sky_2"),
    (85, 115, "sky_3"),
    (115, 145, "sky_4"),
    (145, 175, "sky_5"),
    (175, 205, "sky_6"),
    (205, 256, "sky_7")
]

for idx, (y_start, y_end, col_name) in enumerate(sky_bands):
    for y in range(y_start, min(H, y_end)):
        for x in range(W):
            if idx > 0 and y < y_start + 4:
                prev_col = sky_bands[idx - 1][2]
                if (x + y) % 2 == 0:
                    grid[y, x] = prev_col
                else:
                    grid[y, x] = col_name
            else:
                grid[y, x] = col_name

# Pale misty moon/sun in upper right
sun_cx, sun_cy = 195, 48
draw_circle(sun_cx, sun_cy, 36, "sun_3")
draw_circle(sun_cx, sun_cy, 28, "sun_2")
draw_circle(sun_cx, sun_cy, 20, "sun_1")
draw_circle(sun_cx, sun_cy, 13, "sun_0")

for i in range(12):
    draw_line(sun_cx - 30 + i*2, sun_cy - 8 + i, sun_cx + 40 + i, sun_cy - 8 + i, "sky_4")
for i in range(8):
    draw_line(sun_cx - 40 + i*3, sun_cy + 10 + i, sun_cx + 30 + i*2, sun_cy + 10 + i, "sky_5")

cranes = [(155, 30), (163, 27), (170, 32), (180, 26)]
for bx, by in cranes:
    set_px(bx, by, "sky_2")
    set_px(bx - 1, by - 1, "sky_2")
    set_px(bx + 1, by - 1, "sky_2")
    set_px(bx - 2, by - 2, "sky_2")
    set_px(bx + 2, by - 2, "sky_2")

# Far Mountain Peaks
far_mtn_1 = [(0, 150), (25, 95), (45, 110), (70, 80), (100, 120), (130, 90), (160, 130), (190, 85), (220, 115), (256, 80), (256, 170), (0, 170)]
draw_poly(far_mtn_1, "mtn_far_1")
for y in range(80, 160):
    for x in range(W):
        if grid[y, x] == "mtn_far_1":
            if y > 130:
                if (x + y) % 2 == 0:
                    grid[y, x] = "mtn_far_2"
                if y > 145:
                    grid[y, x] = "mtn_far_3"

# Mid Mountain Peaks
mid_mtn_l = [(0, 190), (0, 95), (22, 65), (38, 85), (55, 60), (75, 100), (95, 140), (110, 185), (0, 190)]
draw_poly(mid_mtn_l, "mtn_mid_1")
mid_mtn_r = [(165, 200), (180, 120), (205, 80), (225, 105), (242, 70), (256, 90), (256, 200), (165, 200)]
draw_poly(mid_mtn_r, "mtn_mid_1")

for x, y_top in [(22, 65), (55, 60), (205, 80), (242, 70)]:
    for dy in range(50):
        draw_line(x - dy//3, y_top + dy, x - dy//3 + 2, y_top + dy, "mtn_mid_2")
        draw_line(x + dy//4, y_top + dy, x + dy//4 + 1, y_top + dy, "mtn_mid_0")

for tx, ty in [(30, 82), (48, 75), (65, 105), (215, 98), (235, 88)]:
    draw_line(tx, ty, tx, ty + 8, "rock_0")
    draw_line(tx - 3, ty + 2, tx + 3, ty + 2, "pine_leaf_0")
    draw_line(tx - 5, ty + 4, tx + 5, ty + 4, "pine_leaf_1")
    draw_line(tx - 4, ty + 6, tx + 4, ty + 6, "pine_leaf_0")

# Sea of Clouds
for cy, cr, col, cols in [
    (145, 18, "sky_5", [(40, 150), (80, 142), (120, 148), (170, 140), (210, 146)]),
    (160, 22, "sky_6", [(20, 165), (60, 158), (105, 162), (150, 155), (195, 162), (235, 158)]),
    (178, 26, "sky_7", [(0, 180), (45, 175), (90, 178), (140, 172), (185, 176), (230, 174), (256, 175)])
]:
    for cx, cy_pt in cols:
        draw_ellipse(cx, cy_pt, cr + 15, cr - 4, col)

# Framing Pine Branch at Top-Left
pine_trunk = [(0, 10), (12, 14), (25, 18), (38, 22), (48, 28), (56, 36)]
for i in range(len(pine_trunk) - 1):
    x0, y0 = pine_trunk[i]
    x1, y1 = pine_trunk[i+1]
    draw_line(x0, y0, x1, y1, "pine_wood_0")
    draw_line(x0, y0 + 1, x1, y1 + 1, "pine_wood_1")
    draw_line(x0, y0 + 2, x1, y1 + 2, "pine_wood_0")

pine_clusters = [(15, 16), (28, 20), (40, 25), (50, 32), (58, 40), (32, 28), (44, 38)]
for px, py in pine_clusters:
    draw_ellipse(px, py, 7, 4, "pine_leaf_0")
    draw_ellipse(px, py - 1, 5, 3, "pine_leaf_1")
    draw_ellipse(px, py - 2, 3, 2, "pine_leaf_2")

# Foreground Rocky Cliff Platform
cliff_pts = [(20, 256), (35, 235), (60, 220), (95, 212), (140, 214), (185, 218), (225, 225), (256, 232), (256, 256), (20, 256)]
draw_poly(cliff_pts, "rock_2")

cliff_rim = [(35, 235), (60, 220), (95, 212), (140, 214), (185, 218), (225, 225), (256, 232)]
for i in range(len(cliff_rim) - 1):
    x0, y0 = cliff_rim[i]
    x1, y1 = cliff_rim[i+1]
    draw_line(x0, y0, x1, y1, "rock_4")
    draw_line(x0, y0 + 1, x1, y1 + 1, "rock_3")
    draw_line(x0, y0 - 1, x1, y1 - 1, "rock_5")

cracks = [
    [(70, 222), (75, 235), (72, 248)],
    [(115, 216), (120, 230), (128, 245)],
    [(160, 220), (165, 236), (172, 252)],
    [(210, 228), (218, 242), (225, 256)]
]
for crk in cracks:
    for i in range(len(crk) - 1):
        x0, y0 = crk[i]
        x1, y1 = crk[i+1]
        draw_line(x0, y0, x1, y1, "rock_0")
        draw_line(x0 + 1, y0, x1 + 1, y1, "rock_1")

moss_spots = [(55, 221), (68, 221), (82, 214), (125, 215), (150, 217), (175, 219), (200, 224)]
for mx, my in moss_spots:
    draw_ellipse(mx, my, 5, 2, "moss_1")
    draw_ellipse(mx, my - 1, 3, 1, "moss_2")
    draw_line(mx - 2, my + 1, mx + 2, my + 1, "moss_0")

# ----------------- 2. HERO CHARACTER -----------------

# LAYER A: Loose Hair blowing in wind to right (Behind torso)
hair_tresses = [
    [(136, 68), (150, 75), (165, 82), (182, 88), (175, 89), (158, 83), (142, 75), (136, 68)],
    [(138, 72), (156, 80), (174, 90), (192, 98), (180, 101), (160, 92), (144, 80), (138, 72)],
    [(140, 78), (158, 88), (176, 102), (188, 114), (176, 115), (156, 100), (142, 86), (140, 78)],
    [(138, 84), (152, 96), (168, 110), (180, 126), (170, 128), (152, 112), (140, 94), (138, 84)]
]
for poly in hair_tresses:
    draw_poly(poly, "hair_1")
    for i in range(len(poly)-1):
        draw_line(poly[i][0], poly[i][1], poly[i+1][0], poly[i+1][1], "black")
# Hair sheen lines
draw_line(145, 74, 175, 85, "hair_3")
draw_line(148, 82, 180, 93, "hair_3")
draw_line(152, 81, 172, 89, "hair_4")
draw_line(150, 90, 175, 104, "hair_2")

# LAYER B: Billowing Right Sleeve (Behind torso, sweeping to right)
sleeve_poly = [
    (146, 92), (165, 100), (185, 110), (202, 122), (206, 134), (198, 146),
    (182, 155), (165, 152), (154, 142), (146, 126), (144, 108), (146, 92)
]
draw_poly(sleeve_poly, "robe_base")

# Inner sleeve opening / lining (facing left/down)
inner_sleeve_poly = [(198, 146), (182, 155), (165, 152), (175, 144), (190, 140), (198, 146)]
draw_poly(inner_sleeve_poly, "inner_1")
draw_line(182, 155, 165, 152, "inner_3")

# Sleeve folds and shading
sleeve_folds = [
    [(150, 98), (172, 108), (196, 118)],
    [(152, 108), (175, 118), (198, 130)],
    [(150, 118), (170, 128), (188, 140)],
    [(148, 128), (162, 136), (178, 148)]
]
for fld in sleeve_folds:
    for i in range(len(fld)-1):
        draw_line(fld[i][0], fld[i][1], fld[i+1][0], fld[i+1][1], "robe_shadow")
        draw_line(fld[i][0], fld[i][1]-1, fld[i+1][0], fld[i+1][1]-1, "robe_light")
        draw_line(fld[i][0], fld[i][1]-2, fld[i+1][0], fld[i+1][1]-2, "robe_hi")

# Sleeve wind rim highlight
draw_line(185, 110, 202, 122, "robe_rim")
draw_line(202, 122, 206, 134, "robe_rim")
draw_line(206, 134, 198, 146, "robe_light")

# Outline of right sleeve
for i in range(len(sleeve_poly)-1):
    draw_line(sleeve_poly[i][0], sleeve_poly[i][1], sleeve_poly[i+1][0], sleeve_poly[i+1][1], "black")

# LAYER C: Legs, Pants & Martial Boots (under lower robes)
# Left leg (front, weight-bearing):
left_shin_poly = [(101, 185), (109, 185), (111, 214), (99, 214), (101, 185)]
draw_poly(left_shin_poly, "boot_1")
# Leg wraps (xing-teng) criss-cross strapping
for wy in range(188, 213, 4):
    draw_line(100, wy, 110, wy + 2, "boot_wrap")
    draw_line(100, wy + 2, 110, wy, "boot_0")
# Left boot (firmly on stone)
left_boot_poly = [(96, 214), (111, 214), (112, 222), (104, 224), (94, 222), (92, 218), (96, 214)]
draw_poly(left_boot_poly, "boot_1")
draw_poly([(96, 214), (111, 214), (110, 217), (96, 217)], "boot_2")
draw_line(94, 222, 108, 223, "boot_3") # sole rim
draw_line(92, 224, 112, 224, "boot_0") # sole base
for i in range(len(left_boot_poly)-1):
    draw_line(left_boot_poly[i][0], left_boot_poly[i][1], left_boot_poly[i+1][0], left_boot_poly[i+1][1], "black")

# Right leg (back, braced):
right_shin_poly = [(138, 190), (147, 190), (148, 217), (137, 217), (138, 190)]
draw_poly(right_shin_poly, "boot_0")
for wy in range(192, 216, 4):
    draw_line(138, wy, 147, wy + 2, "boot_2")
    draw_line(138, wy + 2, 147, wy, "boot_0")
# Right boot
right_boot_poly = [(136, 217), (148, 217), (150, 224), (142, 226), (134, 224), (136, 217)]
draw_poly(right_boot_poly, "boot_1")
draw_line(134, 225, 149, 225, "boot_3")
draw_line(133, 226, 150, 226, "boot_0")
for i in range(len(right_boot_poly)-1):
    draw_line(right_boot_poly[i][0], right_boot_poly[i][1], right_boot_poly[i+1][0], right_boot_poly[i+1][1], "black")

# LAYER D: Flowing Lower Robes (Skirts & Mantle)
# Back sweeping robe panel (billowing to the right in wind)
back_skirt_poly = [
    (134, 134), (146, 145), (164, 158), (185, 172), (204, 186), (208, 198),
    (196, 204), (180, 202), (165, 206), (150, 208), (142, 204), (135, 175), (134, 134)
]
draw_poly(back_skirt_poly, "robe_base")

# Major fold ridges on sweeping skirt
skirt_folds = [
    [(136, 138), (152, 154), (175, 174), (200, 188)],
    [(135, 148), (150, 165), (170, 184), (192, 200)],
    [(134, 160), (146, 178), (162, 196), (180, 202)],
    [(134, 172), (142, 190), (154, 202), (165, 206)]
]
for fld in skirt_folds:
    for i in range(len(fld)-1):
        draw_line(fld[i][0], fld[i][1], fld[i+1][0], fld[i+1][1], "robe_darkest")
        draw_line(fld[i][0]+1, fld[i][1]-1, fld[i+1][0]+1, fld[i+1][1]-1, "robe_shadow")
        draw_line(fld[i][0]+2, fld[i][1]-2, fld[i+1][0]+2, fld[i+1][1]-2, "robe_mid")
        draw_line(fld[i][0]+3, fld[i][1]-3, fld[i+1][0]+3, fld[i+1][1]-3, "robe_light")

# Robe rim highlights on billowing skirt edge
draw_line(185, 172, 204, 186, "robe_rim")
draw_line(204, 186, 208, 198, "robe_rim")
draw_line(208, 198, 196, 204, "robe_light")

# Back skirt outline
for i in range(len(back_skirt_poly)-1):
    draw_line(back_skirt_poly[i][0], back_skirt_poly[i][1], back_skirt_poly[i+1][0], back_skirt_poly[i+1][1], "black")

# Front Robe Panel (hanging down between and over legs)
front_skirt_poly = [
    (110, 134), (135, 134), (136, 165), (132, 192), (128, 210), (120, 212),
    (114, 208), (108, 195), (105, 175), (108, 150), (110, 134)
]
draw_poly(front_skirt_poly, "robe_mid_low")

# Front panel folds
draw_line(116, 135, 114, 206, "robe_shadow")
draw_line(118, 135, 116, 206, "robe_light")
draw_line(123, 135, 122, 210, "robe_darkest")
draw_line(125, 135, 124, 210, "robe_light")
draw_line(126, 135, 125, 210, "robe_hi")
draw_line(130, 135, 128, 208, "robe_shadow")

# Front panel outline
for i in range(len(front_skirt_poly)-1):
    draw_line(front_skirt_poly[i][0], front_skirt_poly[i][1], front_skirt_poly[i+1][0], front_skirt_poly[i+1][1], "black")

# LAYER E: Torso, High Collar & Chest Cross-over
torso_poly = [
    (102, 92), (114, 82), (130, 80), (146, 88), (144, 112), (138, 122),
    (136, 132), (110, 132), (108, 120), (100, 110), (102, 92)
]
draw_poly(torso_poly, "robe_base")

# Crossed Lapels (Yiling / Hanfu collar crossover)
# High collar wrapping neck
collar_inner = [(116, 78), (124, 76), (130, 77), (128, 84), (122, 85), (116, 83), (116, 78)]
draw_poly(collar_inner, "inner_3")
draw_poly([(117, 79), (123, 77), (127, 78), (125, 83), (117, 81)], "inner_4")

# Robe crossover lines (left over right lapel)
crossover_pts = [(116, 82), (122, 95), (126, 108), (130, 122)]
for i in range(len(crossover_pts)-1):
    x0, y0 = crossover_pts[i]
    x1, y1 = crossover_pts[i+1]
    # White silk lining edge
    draw_line(x0 - 1, y0, x1 - 1, y1, "inner_3")
    draw_line(x0, y0, x1, y1, "inner_4")
    # Lapel shadow seam
    draw_line(x0 + 1, y0, x1 + 1, y1, "robe_darkest")
    draw_line(x0 + 2, y0, x1 + 2, y1, "robe_shadow")

# Right lapel under-layer
draw_line(128, 82, 120, 95, "inner_2")
draw_line(129, 82, 121, 95, "inner_1")

# Chest & Abdominal fabric tension folds
draw_line(106, 96, 116, 108, "robe_shadow")
draw_line(107, 95, 117, 107, "robe_light")
draw_line(105, 104, 114, 116, "robe_shadow")
draw_line(106, 103, 115, 115, "robe_light")
draw_line(136, 96, 128, 106, "robe_shadow")
draw_line(138, 106, 128, 114, "robe_shadow")
draw_line(139, 105, 129, 113, "robe_light")

# Torso outline
for i in range(len(torso_poly)-1):
    draw_line(torso_poly[i][0], torso_poly[i][1], torso_poly[i+1][0], torso_poly[i+1][1], "black")

# LAYER F: Crimson Sash (Belt) & Ornaments
sash_poly = [(110, 122), (137, 122), (138, 133), (111, 133), (110, 122)]
draw_poly(sash_poly, "sash_base")

# Sash shading & rich cinnabar gradient
draw_line(110, 122, 137, 122, "sash_shadow")
draw_line(110, 123, 137, 123, "sash_mid")
draw_line(110, 124, 137, 124, "sash_light")
draw_line(111, 125, 137, 125, "sash_hi")
draw_line(111, 126, 137, 126, "sash_mid")
draw_line(111, 127, 137, 127, "sash_base")
draw_line(111, 128, 137, 128, "sash_shadow")
draw_line(111, 129, 137, 129, "sash_mid")
draw_line(111, 130, 137, 130, "sash_base")
draw_line(111, 131, 137, 131, "sash_shadow")
draw_line(111, 132, 137, 132, "sash_dark")

# Tied knot at left hip
draw_ellipse(114, 128, 4, 3, "sash_mid")
draw_ellipse(114, 128, 2, 2, "sash_light")
draw_circle(114, 128, 1, "sash_hi")

# Long sash tails fluttering down and back in the wind
sash_tail_1 = [(114, 131), (118, 142), (124, 155), (132, 168), (142, 178), (140, 180), (130, 170), (121, 156), (115, 143), (112, 132), (114, 131)]
draw_poly(sash_tail_1, "sash_mid")
draw_line(118, 142, 142, 178, "sash_light")
draw_line(120, 143, 141, 177, "sash_hi")
for i in range(len(sash_tail_1)-1):
    draw_line(sash_tail_1[i][0], sash_tail_1[i][1], sash_tail_1[i+1][0], sash_tail_1[i+1][1], "sash_dark")

sash_tail_2 = [(116, 132), (123, 145), (132, 158), (144, 168), (152, 174), (150, 176), (138, 170), (128, 160), (119, 146), (116, 132)]
draw_poly(sash_tail_2, "sash_base")
for i in range(len(sash_tail_2)-1):
    draw_line(sash_tail_2[i][0], sash_tail_2[i][1], sash_tail_2[i+1][0], sash_tail_2[i+1][1], "black")

# Center Bronze/Gold Belt Plaque
draw_rect(122, 124, 6, 6, "gold_1")
draw_rect(123, 125, 4, 4, "gold_3")
draw_rect(124, 126, 2, 2, "gold_4")

# Jade Pendant (Yu Pei) hanging below belt
draw_line(120, 132, 120, 136, "gold_2") # silk cord
draw_circle(120, 139, 3, "jade_1")
draw_circle(120, 139, 2, "jade_2")
set_px(120, 139, "jade_3")
# Jade fringe tassel
draw_line(120, 142, 121, 150, "sash_mid")
draw_line(121, 142, 122, 149, "sash_light")

# Sash outline
draw_line(110, 122, 137, 122, "black")
draw_line(111, 133, 138, 133, "black")
draw_line(110, 122, 111, 133, "black")
draw_line(137, 122, 138, 133, "black")

# LAYER G: Left Arm (Resting on Jian Sword) & Bracer
left_arm_poly = [
    (102, 92), (95, 102), (92, 114), (88, 126), (93, 127),
    (98, 116), (102, 106), (108, 98), (102, 92)
]
draw_poly(left_arm_poly, "robe_base")

# Left forearm bracer (leather / lacquered vambrace)
bracer_poly = [(93, 114), (88, 126), (93, 127), (98, 116), (93, 114)]
draw_poly(bracer_poly, "boot_1")
# Bracer metal studs and straps
draw_line(93, 114, 98, 116, "gold_2")
draw_line(91, 118, 96, 120, "boot_wrap")
draw_line(90, 122, 95, 124, "boot_wrap")
draw_line(88, 126, 93, 127, "gold_2")
set_px(94, 115, "gold_4")
set_px(92, 119, "gold_3")
set_px(91, 123, "gold_3")

# Left arm fold highlights & outline
draw_line(100, 95, 96, 106, "robe_light")
draw_line(99, 96, 95, 107, "robe_hi")
for i in range(len(left_arm_poly)-1):
    draw_line(left_arm_poly[i][0], left_arm_poly[i][1], left_arm_poly[i+1][0], left_arm_poly[i+1][1], "black")

# LAYER H: Straight Jian Sword & Sword-Resting Hand
# Left Hand resting atop the sword pommel:
# Hand knuckles and thumb curled over pommel at (89..94, 127..133)
hand_poly = [(88, 127), (94, 127), (95, 132), (91, 134), (87, 132), (88, 127)]
draw_poly(hand_poly, "skin_base")
draw_poly([(89, 128), (93, 128), (94, 131), (90, 132)], "skin_mid")
draw_line(89, 128, 93, 128, "skin_light") # knuckle highlight
set_px(91, 127, "skin_hi")
draw_line(88, 130, 93, 130, "skin_shadow") # finger creases
for i in range(len(hand_poly)-1):
    draw_line(hand_poly[i][0], hand_poly[i][1], hand_poly[i+1][0], hand_poly[i+1][1], "skin_dark")

# Jian Sword Geometry:
# Pommel (just below/under hand):
draw_circle(90, 134, 3, "gold_2")
draw_circle(90, 134, 2, "gold_3")
set_px(90, 134, "gold_4")
draw_circle(90, 134, 3, "gold_0", fill=False)

# Sword Pommel Tassel (Crimson silk tassel blowing back in the wind)
tassel_poly = [
    (91, 136), (97, 140), (105, 146), (114, 155), (110, 158),
    (101, 152), (94, 145), (91, 139), (91, 136)
]
draw_poly(tassel_poly, "sash_mid")
draw_line(93, 138, 112, 154, "sash_light")
draw_line(95, 140, 111, 153, "sash_hi")
draw_line(91, 136, 91, 139, "gold_3") # tassel ring
for i in range(len(tassel_poly)-1):
    draw_line(tassel_poly[i][0], tassel_poly[i][1], tassel_poly[i+1][0], tassel_poly[i+1][1], "sash_dark")

# Grip (Hilt):
# Straight vertical cylinder from y=135 to 146, x=89..91
for gy in range(135, 147):
    draw_line(89, gy, 91, gy, "steel_1")
# Cord wrap cross-hatching
for gy in range(135, 147, 3):
    draw_line(89, gy, 91, gy + 1, "gold_2")
    draw_line(89, gy + 1, 91, gy, "boot_0")

# Sword Guard (Classic Taoist/Wuxia wing/cloud shaped guard at y=147..150):
guard_pts = [(83, 149), (86, 147), (90, 146), (94, 147), (97, 149), (94, 151), (90, 150), (86, 151), (83, 149)]
draw_poly(guard_pts, "gold_2")
draw_poly([(85, 148), (90, 147), (95, 148), (93, 150), (90, 149), (87, 150)], "gold_3")
draw_line(88, 147, 92, 147, "gold_4")
for i in range(len(guard_pts)-1):
    draw_line(guard_pts[i][0], guard_pts[i][1], guard_pts[i+1][0], guard_pts[i+1][1], "gold_0")

# Scabbard & Straight Jian:
# Descends straight from (90, 151) down to (82, 233)
# Scabbard width ~ 4 pixels
scabbard_pts = [(88, 151), (92, 151), (84, 233), (80, 233), (88, 151)]
draw_poly(scabbard_pts, "sword_wood")

# Scabbard wood luster and edge highlight
for sy in range(151, 233):
    # interpolate x
    t = (sy - 151) / (233 - 151)
    sx_center = (1 - t) * 90 + t * 82
    set_px(int(round(sx_center - 1)), sy, "sword_wood_l")
    set_px(int(round(sx_center)), sy, "sword_wood")
    set_px(int(round(sx_center + 1)), sy, "black")
    # Left edge steel gleam (straight blade line)
    set_px(int(round(sx_center - 2)), sy, "steel_2")

# Scabbard Decorative Gold/Brass Fittings:
# 1. Top throat collar (y = 151..156)
for gy in range(151, 157):
    t = (gy - 151) / (233 - 151)
    sx = int(round((1 - t) * 90 + t * 82))
    draw_line(sx - 2, gy, sx + 2, gy, "gold_2")
    set_px(sx - 1, gy, "gold_4")
    set_px(sx, gy, "gold_3")

# 2. Middle suspension bands (y = 176..181)
for gy in range(176, 182):
    t = (gy - 151) / (233 - 151)
    sx = int(round((1 - t) * 90 + t * 82))
    draw_line(sx - 2, gy, sx + 2, gy, "gold_2")
    set_px(sx - 1, gy, "gold_4")
    set_px(sx, gy, "gold_3")
# Suspension ring
t_ring = (178 - 151) / (233 - 151)
sx_ring = int(round((1 - t_ring) * 90 + t_ring * 82))
draw_circle(sx_ring + 3, 178, 2, "gold_3", fill=False)

# 3. Bottom chape (y = 227..234)
for gy in range(227, 235):
    t = (gy - 151) / (233 - 151)
    sx = int(round((1 - t) * 90 + t * 82))
    draw_line(sx - 2, gy, sx + 2, gy, "gold_2")
    set_px(sx - 1, gy, "gold_4")
# Chape tip point
set_px(82, 234, "gold_3")
set_px(81, 234, "gold_4")
set_px(82, 235, "gold_0")

# Scabbard dark outlines
for i in range(len(scabbard_pts)-1):
    draw_line(scabbard_pts[i][0], scabbard_pts[i][1], scabbard_pts[i+1][0], scabbard_pts[i+1][1], "black")

# LAYER I: Face & Hair (Under the Hat)
# Neck
draw_poly([(118, 77), (128, 77), (128, 84), (118, 84)], "skin_shadow")

# Jaw and Lower Face
face_pts = [
    (115, 66), (128, 65), (131, 72), (128, 76), (122, 80), (117, 78), (115, 72), (115, 66)
]
draw_poly(face_pts, "skin_base")

# Deep hat shadow over upper half of face (eyes & brow area)
hat_shadow_poly = [(114, 65), (130, 64), (131, 72), (126, 73), (120, 73), (114, 71), (114, 65)]
draw_poly(hat_shadow_poly, "skin_dark")

# Piercing gaze visible through the shadow:
# Left eye (narrow, intense wuxia gaze)
draw_line(116, 70, 119, 70, "black")
set_px(117, 70, "eye_white")
set_px(118, 70, "hair_0")
# Sharp eye brow
draw_line(115, 68, 120, 68, "black")

# Nose bridge:
# Highlights catching light on left edge of nose
draw_line(120, 71, 120, 75, "skin_light")
set_px(120, 72, "skin_hi")
draw_line(121, 72, 121, 75, "skin_mid")
set_px(120, 75, "skin_shadow") # nostril shadow

# Mouth (calm, stoic, determined):
draw_line(119, 77, 123, 77, "skin_dark")
set_px(121, 77, "lip_red")
set_px(121, 78, "skin_shadow") # under-lip shadow

# Jawline highlight and chin
draw_line(117, 78, 121, 80, "skin_mid")
set_px(121, 80, "skin_light")
draw_line(121, 80, 128, 76, "skin_shadow")

# Face outline
draw_line(115, 72, 117, 78, "skin_dark")
draw_line(117, 78, 121, 80, "black")
draw_line(121, 80, 128, 76, "black")
draw_line(128, 76, 131, 72, "black")

# Front hair strands framing face
# Left front lock:
lock_l = [(113, 65), (112, 74), (113, 84), (114, 94), (112, 98), (113, 85), (114, 75), (113, 65)]
draw_poly(lock_l, "hair_1")
draw_line(113, 72, 113, 88, "hair_3")
for i in range(len(lock_l)-1):
    draw_line(lock_l[i][0], lock_l[i][1], lock_l[i+1][0], lock_l[i+1][1], "black")

# Right side lock (framing ear/jaw):
lock_r = [(129, 66), (132, 74), (133, 84), (131, 92), (130, 84), (129, 74), (129, 66)]
draw_poly(lock_r, "hair_1")
draw_line(131, 72, 132, 85, "hair_2")
for i in range(len(lock_r)-1):
    draw_line(lock_r[i][0], lock_r[i][1], lock_r[i+1][0], lock_r[i+1][1], "black")

# Black hat tie cords under chin
draw_line(116, 73, 119, 81, "black")
draw_line(127, 72, 122, 81, "black")
draw_line(120, 81, 122, 82, "black") # tie knot
# Cord flutter
draw_line(121, 82, 125, 88, "black")
draw_line(125, 88, 130, 92, "hair_2")

# LAYER J: Bamboo Conical Hat (Douli)
# Iconic wide bamboo hat tilted down covering upper face
# Hat Apex: (124, 42)
# Hat Brim: Ellipse with center (124, 62), rx = 44, ry = 9
# Tilted so left is slightly lower: rx spans 80 to 168

hat_poly = [
    (124, 42), (145, 50), (160, 56), (168, 62), (160, 66), (144, 69),
    (124, 71), (104, 70), (88, 68), (80, 64), (88, 58), (103, 50), (124, 42)
]
draw_poly(hat_poly, "douli_base")

# Underside shadow of hat (along front-left rim)
underside_pts = [(80, 64), (88, 68), (104, 70), (124, 71), (124, 67), (104, 66), (88, 64), (80, 64)]
draw_poly(underside_pts, "douli_shadow")

# Bamboo Woven Texture:
# Concentric woven rings
for r_scale in [0.25, 0.5, 0.72, 0.88]:
    pts_ring = []
    for deg in range(0, 360, 15):
        rad = math.radians(deg)
        x_pt = 124 + math.cos(rad) * 44 * r_scale
        y_center = 42 + (62 - 42) * r_scale
        y_pt = y_center + math.sin(rad) * 9 * r_scale
        pts_ring.append((x_pt, y_pt))
    for i in range(len(pts_ring)):
        x0, y0 = pts_ring[i]
        x1, y1 = pts_ring[(i+1)%len(pts_ring)]
        draw_line(x0, y0, x1, y1, "douli_dark")
        draw_line(x0, y0-1, x1, y1-1, "douli_light")

# Radial bamboo ribs from apex
for deg in range(10, 175, 12):
    rad = math.radians(deg)
    bx = 124 + math.cos(rad) * 44
    by = 62 + math.sin(rad) * 9
    draw_line(124, 42, bx, by, "douli_mid")
    draw_line(124, 42, bx + 1, by, "douli_dark")

# Bamboo lighting & highlights (Light coming from upper right / sky)
# Right slope highlight:
draw_line(124, 42, 150, 53, "douli_hi")
draw_line(124, 43, 148, 54, "douli_bright")
draw_line(125, 42, 160, 58, "douli_light")
draw_line(126, 42, 164, 62, "douli_mid")

# Left slope shadow:
draw_line(124, 42, 95, 53, "douli_dark")
draw_line(123, 42, 85, 60, "douli_dark")
draw_line(122, 43, 82, 64, "douli_shadow")

# Apex cap (ornate top woven knot/finial)
draw_circle(124, 42, 3, "douli_dark")
draw_circle(124, 42, 2, "douli_mid")
draw_circle(124, 41, 1, "douli_bright")

# Crisp dark rim outline of the Douli
for i in range(len(hat_poly)-1):
    draw_line(hat_poly[i][0], hat_poly[i][1], hat_poly[i+1][0], hat_poly[i+1][1], "black")

# ----------------- 3. ATMOSPHERIC DETAILS -----------------

# Drifting Autumn / Bamboo Leaves swirling in the mountain wind
leaves = [
    (65, 142, "leaf_1", "leaf_2"),
    (74, 168, "leaf_2", "leaf_3"),
    (85, 195, "leaf_0", "leaf_1"),
    (155, 140, "leaf_1", "leaf_2"),
    (178, 162, "leaf_2", "leaf_3"),
    (192, 125, "leaf_0", "leaf_1"),
    (212, 150, "leaf_1", "leaf_2"),
    (225, 175, "leaf_2", "leaf_3"),
]
for lx, ly, c0, c1 in leaves:
    draw_ellipse(lx, ly, 3, 2, c0)
    set_px(lx - 1, ly - 1, c1)
    set_px(lx, ly, c1)
    set_px(lx + 2, ly + 1, "leaf_0")

# Low ground fog curling around the hero's boots and stone rim
for fx, fy in [(88, 224), (105, 226), (125, 225), (145, 228), (160, 227)]:
    draw_ellipse(fx, fy, 10, 2, "sky_6")
    draw_ellipse(fx + 2, fy - 1, 6, 1, "sky_7")

print("Hero rendering complete.")

# ----------------- 4. TRANSFER TO CANVAS -----------------
c = new_canvas(W, H)

# Register all palette colors into canvas
color_map = {}
for name, rgb in PALETTE.items():
    hex_str = "#{:02x}{:02x}{:02x}".format(*rgb)
    color_map[name] = c.color(hex_str, name=name)

# Map grid to indices
idx_array = np.zeros((H, W), dtype=np.int32)
for y in range(H):
    for x in range(W):
        col_name = grid[y, x]
        idx_array[y, x] = color_map[col_name]

# Fast bulk transfer
c.px[:] = idx_array.flatten().tolist()

stats = c.stats()
print(f"Stats: colors used = {stats['colors_used']}, size = {stats['size']}")
save("wuxia_hero", c)
view(c)
