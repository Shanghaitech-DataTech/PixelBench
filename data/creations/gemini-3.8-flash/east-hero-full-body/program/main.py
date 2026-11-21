import numpy as np
import math
from pixelbench_api import *

W, H = 256, 256

PALETTE = {
    # Sky and Atmosphere
    "sky_0": (24, 32, 44),
    "sky_1": (38, 50, 66),
    "sky_2": (60, 78, 98),
    "sky_3": (92, 114, 136),
    "sky_4": (136, 160, 180),
    "sky_5": (180, 200, 214),
    "sky_6": (216, 230, 238),
    "sky_7": (242, 248, 252),

    # Celestial Sun / Moon
    "sun_0": (255, 253, 242),
    "sun_1": (252, 238, 204),
    "sun_2": (234, 210, 165),
    "sun_3": (202, 180, 135),

    # Distant Karst Mountains
    "mtn_far_0": (68, 88, 106),
    "mtn_far_1": (88, 110, 128),
    "mtn_far_2": (114, 136, 154),
    "mtn_far_3": (148, 170, 186),
    "mtn_far_4": (182, 200, 212),

    # Midground Karst Peaks
    "mtn_mid_0": (26, 36, 46),
    "mtn_mid_1": (40, 54, 68),
    "mtn_mid_2": (58, 76, 92),
    "mtn_mid_3": (82, 102, 120),
    "mtn_mid_4": (110, 132, 150),

    # Ancient Mountain Pine
    "pine_bark_0": (16, 22, 20),
    "pine_bark_1": (30, 38, 34),
    "pine_bark_2": (48, 58, 50),
    "pine_leaf_0": (18, 30, 24),
    "pine_leaf_1": (28, 48, 38),
    "pine_leaf_2": (46, 76, 58),
    "pine_leaf_3": (68, 104, 78),

    # Foreground Cliff Rock & Strata
    "rock_0": (12, 18, 24),
    "rock_1": (20, 28, 36),
    "rock_2": (32, 44, 54),
    "rock_3": (50, 66, 78),
    "rock_4": (72, 90, 104),
    "rock_5": (104, 124, 140),
    "moss_0": (30, 48, 34),
    "moss_1": (52, 80, 56),
    "moss_2": (84, 120, 88),

    # Bamboo Conical Hat (Douli)
    "douli_shadow": (38, 24, 12),
    "douli_dark":   (70, 48, 24),
    "douli_base":   (118, 84, 42),
    "douli_mid":    (168, 126, 66),
    "douli_light":  (208, 164, 96),
    "douli_hi":     (236, 196, 132),
    "douli_bright": (250, 224, 174),

    # Hero Face & Skin
    "skin_dark":   (68, 38, 30),
    "skin_shadow": (112, 64, 50),
    "skin_base":   (164, 100, 78),
    "skin_mid":    (208, 142, 114),
    "skin_light":  (235, 180, 154),
    "skin_hi":     (248, 212, 192),
    "lip_red":     (160, 68, 72),
    "eye_white":   (234, 238, 242),

    # Hair
    "hair_0": (8, 10, 14),
    "hair_1": (18, 22, 30),
    "hair_2": (32, 40, 52),
    "hair_3": (52, 64, 82),
    "hair_4": (78, 96, 120),

    # Dark Robe
    "robe_darkest": (6, 8, 12),
    "robe_shadow":  (14, 18, 26),
    "robe_base":    (24, 30, 42),
    "robe_mid_low": (36, 46, 62),
    "robe_mid":     (52, 66, 88),
    "robe_light":   (72, 90, 118),
    "robe_hi":      (102, 124, 156),
    "robe_rim":     (146, 168, 198),

    # Inner Robe Silk Trim
    "inner_0": (32, 40, 50),
    "inner_1": (64, 76, 92),
    "inner_2": (112, 128, 146),
    "inner_3": (174, 188, 204),
    "inner_4": (232, 240, 246),

    # Crimson Sash & Silk Ribbons
    "sash_dark":   (56, 10, 16),
    "sash_shadow": (96, 18, 26),
    "sash_base":   (148, 26, 40),
    "sash_mid":    (202, 40, 58),
    "sash_light":  (236, 78, 96),
    "sash_hi":     (252, 150, 164),

    # Gold / Bronze Ornaments & Sword Guard
    "gold_0": (64, 44, 12),
    "gold_1": (116, 82, 22),
    "gold_2": (172, 126, 38),
    "gold_3": (220, 172, 64),
    "gold_4": (250, 216, 124),

    # Jade Pendant
    "jade_0": (18, 42, 34),
    "jade_1": (34, 76, 62),
    "jade_2": (64, 124, 102),
    "jade_3": (116, 186, 162),

    # Straight Jian Sword
    "sword_wood":  (26, 16, 22),
    "sword_wood_l":(48, 28, 38),
    "steel_0":     (26, 32, 40),
    "steel_1":     (52, 64, 78),
    "steel_2":     (96, 112, 128),
    "steel_3":     (160, 178, 198),
    "steel_4":     (238, 244, 252),

    # Boots & Leg Wraps
    "boot_0": (14, 14, 16),
    "boot_1": (28, 28, 30),
    "boot_2": (52, 50, 54),
    "boot_3": (84, 80, 86),
    "boot_wrap": (132, 124, 116),

    # Drifting Autumn / Bamboo Leaves
    "leaf_0": (116, 28, 18),
    "leaf_1": (172, 48, 28),
    "leaf_2": (218, 86, 40),
    "leaf_3": (248, 150, 62),

    # Crisp Dark Outline
    "black": (5, 6, 8),
}

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
                if 0.82 <= val <= 1.18:
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

# ----------------- 1. SHANSHUI BACKDROP -----------------

# Sky gradient
sky_bands = [
    (0, 26, "sky_0"),
    (26, 56, "sky_1"),
    (56, 88, "sky_2"),
    (88, 120, "sky_3"),
    (120, 150, "sky_4"),
    (150, 180, "sky_5"),
    (180, 212, "sky_6"),
    (212, 256, "sky_7")
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

# Luminous celestial disc (Moon / Sun) in upper right
sun_cx, sun_cy = 200, 48
draw_circle(sun_cx, sun_cy, 36, "sun_3")
draw_circle(sun_cx, sun_cy, 28, "sun_2")
draw_circle(sun_cx, sun_cy, 20, "sun_1")
draw_circle(sun_cx, sun_cy, 13, "sun_0")

for r, col in [(32, "sun_3"), (25, "sun_2"), (17, "sun_1")]:
    for a in range(0, 360, 8):
        rad = math.radians(a)
        px = int(round(sun_cx + math.cos(rad) * r))
        py = int(round(sun_cy + math.sin(rad) * r))
        if (px + py) % 2 == 0:
            set_px(px, py, col)

# Distant migrating cranes
cranes = [(145, 26), (154, 22), (163, 27), (174, 21)]
for bx, by in cranes:
    set_px(bx, by, "sky_1")
    set_px(bx - 1, by - 1, "sky_1")
    set_px(bx + 1, by - 1, "sky_1")
    set_px(bx - 2, by - 2, "sky_2")
    set_px(bx + 2, by - 2, "sky_2")

# Distant Mountain Silhouettes (Layer 1)
far_mtn_pts = [
    (0, 160), (18, 115), (38, 90), (58, 118), (82, 85), (108, 126),
    (136, 96), (166, 132), (192, 92), (218, 114), (242, 86), (256, 95),
    (256, 175), (0, 175)
]
draw_poly(far_mtn_pts, "mtn_far_1")
for y in range(85, 175):
    for x in range(W):
        if grid[y, x] == "mtn_far_1":
            if y < 105 and (x + y) % 3 == 0:
                grid[y, x] = "mtn_far_0"
            elif y > 135:
                if (x + y) % 2 == 0:
                    grid[y, x] = "mtn_far_2"
                if y > 150:
                    grid[y, x] = "mtn_far_3"
                if y > 162:
                    grid[y, x] = "mtn_far_4"

# Midground Towering Karst Crags (Layer 2)
mid_l_pts = [(0, 195), (0, 85), (18, 62), (34, 80), (52, 54), (72, 92), (94, 138), (110, 185), (0, 195)]
draw_poly(mid_l_pts, "mtn_mid_1")
mid_r_pts = [(168, 205), (182, 128), (204, 78), (224, 102), (244, 68), (256, 84), (256, 205), (168, 205)]
draw_poly(mid_r_pts, "mtn_mid_1")

for x, y_top in [(18, 62), (52, 54), (204, 78), (244, 68)]:
    for dy in range(65):
        draw_line(x - dy//4, y_top + dy, x - dy//4 + 1, y_top + dy, "mtn_mid_2")
        set_px(x, y_top + dy, "mtn_mid_3")
        draw_line(x + dy//3, y_top + dy, x + dy//3 + 2, y_top + dy, "mtn_mid_0")

for tx, ty in [(26, 78), (44, 70), (66, 98), (214, 94), (236, 84)]:
    draw_line(tx, ty, tx - 1, ty + 7, "rock_0")
    draw_ellipse(tx - 2, ty + 1, 4, 2, "pine_leaf_0")
    draw_ellipse(tx + 2, ty + 2, 4, 2, "pine_leaf_1")
    draw_ellipse(tx, ty + 4, 6, 2, "pine_leaf_0")
    draw_ellipse(tx - 1, ty + 4, 3, 1, "pine_leaf_2")

# Sea of Clouds rolling through valleys
cloud_layers = [
    ("sky_5", [(35, 148, 30, 12), (85, 142, 36, 14), (135, 146, 34, 13), (180, 140, 32, 12), (225, 145, 38, 14)]),
    ("sky_6", [(15, 164, 40, 15), (65, 158, 44, 16), (115, 162, 48, 18), (165, 156, 46, 16), (215, 162, 46, 17)]),
    ("sky_7", [(0, 182, 46, 18), (50, 176, 52, 20), (100, 180, 54, 20), (150, 174, 54, 20), (200, 178, 52, 19), (250, 175, 46, 18)])
]
for col, lobes in cloud_layers:
    for cx, cy, rx, ry in lobes:
        draw_ellipse(cx, cy, rx, ry, col)

# Framing Pine Branch at Top-Left
pine_trunk_pts = [(0, 10), (12, 13), (24, 16), (36, 22), (48, 30), (58, 42)]
for i in range(len(pine_trunk_pts) - 1):
    x0, y0 = pine_trunk_pts[i]
    x1, y1 = pine_trunk_pts[i+1]
    draw_line(x0, y0, x1, y1, "pine_bark_0")
    draw_line(x0, y0 + 1, x1, y1 + 1, "pine_bark_1")
    draw_line(x0, y0 + 2, x1, y1 + 2, "pine_bark_2")
    draw_line(x0, y0 + 3, x1, y1 + 3, "pine_bark_0")

pine_fans = [(15, 14), (28, 18), (40, 24), (52, 32), (60, 44), (32, 26), (46, 38)]
for fx, fy in pine_fans:
    for a in range(-50, 60, 15):
        rad = math.radians(a + 90)
        nx = int(round(fx + math.cos(rad) * 9))
        ny = int(round(fy + math.sin(rad) * 6))
        draw_line(fx, fy, nx, ny, "pine_leaf_0")
        set_px(nx, ny, "pine_leaf_2")
    draw_circle(fx, fy, 2, "pine_leaf_1")

# Foreground Rocky Precipice (Hero's ledge)
cliff_pts = [
    (10, 256), (28, 238), (55, 224), (90, 216), (135, 217), (180, 221),
    (220, 227), (256, 235), (256, 256), (10, 256)
]
draw_poly(cliff_pts, "rock_2")

cliff_rim = [(28, 238), (55, 224), (90, 216), (135, 217), (180, 221), (220, 227), (256, 235)]
for i in range(len(cliff_rim) - 1):
    x0, y0 = cliff_rim[i]
    x1, y1 = cliff_rim[i+1]
    draw_line(x0, y0 - 1, x1, y1 - 1, "rock_5")
    draw_line(x0, y0, x1, y1, "rock_4")
    draw_line(x0, y0 + 1, x1, y1 + 1, "rock_3")

rock_fissures = [
    [(62, 225), (70, 238), (66, 250)],
    [(112, 219), (118, 234), (126, 250)],
    [(162, 223), (168, 240), (176, 255)],
    [(212, 229), (218, 246), (226, 256)]
]
for crk in rock_fissures:
    for i in range(len(crk) - 1):
        x0, y0 = crk[i]
        x1, y1 = crk[i+1]
        draw_line(x0, y0, x1, y1, "rock_0")
        draw_line(x0 + 1, y0, x1 + 1, y1, "rock_1")

moss_patches = [(48, 225), (66, 225), (82, 218), (126, 218), (154, 220), (176, 222), (204, 226)]
for mx, my in moss_patches:
    draw_ellipse(mx, my, 6, 2, "moss_0")
    draw_ellipse(mx, my - 1, 4, 1, "moss_1")
    set_px(mx, my - 1, "moss_2")

# ----------------- 2. HERO CHARACTER (FULL BODY) -----------------

# (A) Flowing Loose Hair (Natural, silky hair cascading from behind hat)
# Hair flows down behind the neck/shoulders with sleek fluttering strands:
hair_mass = [
    (134, 60), (144, 66), (154, 76), (164, 90), (168, 104),
    (162, 108), (152, 102), (142, 92), (136, 80), (134, 60)
]
draw_poly(hair_mass, "hair_1")
draw_line(140, 68, 160, 88, "hair_3")
draw_line(146, 76, 164, 96, "hair_3")
draw_line(148, 78, 162, 92, "hair_4")
for i in range(len(hair_mass) - 1):
    draw_line(hair_mass[i][0], hair_mass[i][1], hair_mass[i+1][0], hair_mass[i+1][1], "black")

# Fine fluttering hair wisps trailing in the wind:
wisp_1 = [(154, 76), (168, 80), (180, 84), (174, 85), (162, 81), (154, 76)]
draw_poly(wisp_1, "hair_1")
draw_line(158, 78, 176, 83, "hair_3")
wisp_2 = [(160, 88), (174, 94), (184, 100), (178, 102), (166, 96), (160, 88)]
draw_poly(wisp_2, "hair_1")
draw_line(164, 91, 180, 98, "hair_3")

# (B) Right Arm & Draped Sleeve (Held calmly by the hip / back)
right_arm = [
    (146, 90), (153, 100), (154, 114), (148, 126), (141, 130),
    (138, 122), (143, 110), (144, 98), (146, 90)
]
draw_poly(right_arm, "robe_mid_low")

# Daopao sleeve draping down naturally:
draped_sleeve = [
    (146, 108), (155, 116), (162, 128), (164, 142), (158, 154),
    (150, 158), (142, 150), (140, 138), (138, 126), (146, 108)
]
draw_poly(draped_sleeve, "robe_base")

draw_line(148, 114, 158, 134, "robe_shadow")
draw_line(150, 113, 160, 133, "robe_light")
draw_line(146, 124, 154, 144, "robe_shadow")
draw_line(148, 123, 156, 143, "robe_light")

draw_line(155, 116, 162, 128, "robe_rim")
draw_line(162, 128, 164, 142, "robe_rim")

for i in range(len(draped_sleeve) - 1):
    draw_line(draped_sleeve[i][0], draped_sleeve[i][1], draped_sleeve[i+1][0], draped_sleeve[i+1][1], "black")

# (C) Heroic Stance - Legs & Martial Arts Boots
# Left leg (front, weight-bearing):
left_shin = [(98, 184), (108, 184), (111, 216), (97, 216), (98, 184)]
draw_poly(left_shin, "boot_1")
for wy in range(188, 215, 4):
    draw_line(98, wy, 109, wy + 2, "boot_wrap")
    draw_line(98, wy + 2, 109, wy, "boot_0")
left_boot = [(94, 216), (112, 216), (114, 223), (105, 225), (92, 223), (90, 219), (94, 216)]
draw_poly(left_boot, "boot_1")
draw_poly([(94, 216), (112, 216), (111, 219), (94, 219)], "boot_2")
draw_line(92, 223, 108, 224, "boot_3")
draw_line(90, 225, 114, 225, "boot_0")
for i in range(len(left_boot) - 1):
    draw_line(left_boot[i][0], left_boot[i][1], left_boot[i+1][0], left_boot[i+1][1], "black")

# Right leg (back, braced):
right_shin = [(138, 188), (148, 188), (150, 218), (137, 218), (138, 188)]
draw_poly(right_shin, "boot_0")
for wy in range(190, 216, 4):
    draw_line(138, wy, 149, wy + 2, "boot_2")
    draw_line(138, wy + 2, 149, wy, "boot_0")
right_boot = [(136, 218), (151, 218), (153, 225), (144, 227), (133, 225), (136, 218)]
draw_poly(right_boot, "boot_1")
draw_line(134, 226, 151, 226, "boot_3")
draw_line(132, 227, 153, 227, "boot_0")
for i in range(len(right_boot) - 1):
    draw_line(right_boot[i][0], right_boot[i][1], right_boot[i+1][0], right_boot[i+1][1], "black")

# (D) Flowing Lower Robes (Skirts, Mantle & Billowing Hem)
# Back sweeping robe panel billowing gracefully to the right:
back_skirt = [
    (134, 132), (148, 144), (168, 158), (190, 172), (210, 186), (215, 198),
    (204, 206), (186, 204), (170, 208), (154, 208), (142, 204), (136, 172), (134, 132)
]
draw_poly(back_skirt, "robe_base")

skirt_folds = [
    [(136, 138), (154, 154), (178, 174), (206, 188)],
    [(135, 150), (152, 166), (172, 184), (198, 200)],
    [(134, 162), (148, 178), (164, 196), (184, 202)],
    [(134, 174), (144, 190), (156, 202), (168, 206)]
]
for fld in skirt_folds:
    for i in range(len(fld) - 1):
        x0, y0 = fld[i]
        x1, y1 = fld[i+1]
        draw_line(x0, y0 + 1, x1, y1 + 1, "robe_darkest")
        draw_line(x0, y0, x1, y1, "robe_shadow")
        draw_line(x0 + 1, y0 - 1, x1 + 1, y1 - 1, "robe_mid")
        draw_line(x0 + 2, y0 - 2, x1 + 2, y1 - 2, "robe_light")
        draw_line(x0 + 3, y0 - 3, x1 + 3, y1 - 3, "robe_hi")

draw_line(190, 172, 210, 186, "robe_rim")
draw_line(210, 186, 215, 198, "robe_rim")
draw_line(215, 198, 204, 206, "robe_light")

for i in range(len(back_skirt) - 1):
    draw_line(back_skirt[i][0], back_skirt[i][1], back_skirt[i+1][0], back_skirt[i+1][1], "black")

# Front Robe Panel (Draped gracefully over legs down to mid-calf)
front_skirt = [
    (108, 132), (136, 132), (138, 165), (134, 194), (128, 208), (116, 210),
    (106, 206), (100, 192), (100, 170), (104, 148), (108, 132)
]
draw_poly(front_skirt, "robe_mid_low")

draw_line(112, 134, 108, 204, "robe_shadow")
draw_line(114, 134, 110, 204, "robe_light")
draw_line(120, 134, 118, 208, "robe_darkest")
draw_line(122, 134, 120, 208, "robe_light")
draw_line(123, 134, 121, 208, "robe_hi")
draw_line(128, 134, 126, 206, "robe_shadow")
draw_line(130, 134, 128, 206, "robe_mid")

for i in range(len(front_skirt) - 1):
    draw_line(front_skirt[i][0], front_skirt[i][1], front_skirt[i+1][0], front_skirt[i+1][1], "black")

# (E) Torso, High Collar & Chest Cross-over
torso_poly = [
    (100, 92), (114, 82), (132, 80), (148, 88), (146, 112), (140, 122),
    (137, 132), (108, 132), (106, 120), (98, 110), (100, 92)
]
draw_poly(torso_poly, "robe_base")

inner_collar = [(116, 76), (125, 74), (132, 75), (130, 83), (123, 84), (116, 82), (116, 76)]
draw_poly(inner_collar, "inner_3")
draw_poly([(117, 77), (124, 75), (129, 76), (127, 82), (118, 80)], "inner_4")

lapel_seam = [(116, 82), (122, 94), (127, 108), (132, 122)]
for i in range(len(lapel_seam) - 1):
    x0, y0 = lapel_seam[i]
    x1, y1 = lapel_seam[i+1]
    draw_line(x0 - 1, y0, x1 - 1, y1, "inner_3")
    draw_line(x0, y0, x1, y1, "inner_4")
    draw_line(x0 + 1, y0, x1 + 1, y1, "robe_darkest")
    draw_line(x0 + 2, y0, x1 + 2, y1, "robe_shadow")

draw_line(130, 81, 121, 94, "inner_2")
draw_line(131, 81, 122, 94, "inner_1")

draw_line(105, 96, 116, 108, "robe_shadow")
draw_line(106, 95, 117, 107, "robe_light")
draw_line(104, 104, 114, 116, "robe_shadow")
draw_line(105, 103, 115, 115, "robe_light")
draw_line(138, 96, 128, 108, "robe_shadow")
draw_line(140, 106, 129, 116, "robe_shadow")
draw_line(141, 105, 130, 115, "robe_light")

for i in range(len(torso_poly) - 1):
    draw_line(torso_poly[i][0], torso_poly[i][1], torso_poly[i+1][0], torso_poly[i+1][1], "black")

# (F) Crimson Sash, Golden Plaque & Jade Pendant
sash_poly = [(108, 122), (138, 122), (139, 133), (109, 133), (108, 122)]
draw_poly(sash_poly, "sash_base")

draw_line(108, 122, 138, 122, "sash_shadow")
draw_line(108, 123, 138, 123, "sash_mid")
draw_line(108, 124, 138, 124, "sash_light")
draw_line(109, 125, 138, 125, "sash_hi")
draw_line(109, 126, 138, 126, "sash_mid")
draw_line(109, 127, 138, 127, "sash_base")
draw_line(109, 128, 138, 128, "sash_shadow")
draw_line(109, 129, 138, 129, "sash_mid")
draw_line(109, 130, 139, 130, "sash_base")
draw_line(109, 131, 139, 131, "sash_shadow")
draw_line(109, 132, 139, 132, "sash_dark")

draw_ellipse(112, 128, 4, 3, "sash_mid")
draw_ellipse(112, 128, 2, 2, "sash_light")
set_px(112, 128, "sash_hi")

sash_tail_1 = [
    (112, 131), (117, 142), (124, 156), (133, 168), (144, 180),
    (141, 182), (130, 172), (121, 158), (114, 144), (110, 132), (112, 131)
]
draw_poly(sash_tail_1, "sash_mid")
draw_line(117, 142, 144, 180, "sash_light")
draw_line(119, 143, 143, 179, "sash_hi")
for i in range(len(sash_tail_1) - 1):
    draw_line(sash_tail_1[i][0], sash_tail_1[i][1], sash_tail_1[i+1][0], sash_tail_1[i+1][1], "sash_dark")

sash_tail_2 = [
    (114, 132), (121, 146), (131, 160), (144, 170), (153, 176),
    (150, 178), (138, 172), (127, 162), (117, 148), (114, 132)
]
draw_poly(sash_tail_2, "sash_base")
draw_line(121, 146, 152, 176, "sash_mid")
for i in range(len(sash_tail_2) - 1):
    draw_line(sash_tail_2[i][0], sash_tail_2[i][1], sash_tail_2[i+1][0], sash_tail_2[i+1][1], "black")

# Center Bronze/Gold Belt Plaque
draw_rect(122, 124, 7, 7, "gold_1")
draw_rect(123, 125, 5, 5, "gold_3")
draw_rect(124, 126, 3, 3, "gold_4")
set_px(125, 127, "gold_2")

# Jade Pendant (Yu Pei)
draw_line(119, 132, 119, 136, "gold_2")
draw_circle(119, 140, 3, "jade_1")
draw_circle(119, 140, 2, "jade_2")
set_px(119, 140, "jade_3")
draw_line(119, 143, 120, 152, "sash_mid")
draw_line(120, 143, 121, 151, "sash_light")

draw_line(108, 122, 138, 122, "black")
draw_line(109, 133, 139, 133, "black")
draw_line(108, 122, 109, 133, "black")
draw_line(138, 122, 139, 133, "black")

# (G) Left Arm (Holding / Resting on Straight Jian)
left_arm_poly = [
    (100, 92), (93, 102), (90, 114), (86, 126), (92, 127),
    (96, 116), (101, 106), (107, 98), (100, 92)
]
draw_poly(left_arm_poly, "robe_base")

bracer_poly = [(91, 114), (86, 126), (92, 127), (96, 116), (91, 114)]
draw_poly(bracer_poly, "boot_1")
draw_line(91, 114, 96, 116, "gold_2")
draw_line(89, 118, 94, 120, "boot_wrap")
draw_line(88, 122, 93, 124, "boot_wrap")
draw_line(86, 126, 92, 127, "gold_2")
set_px(92, 115, "gold_4")
set_px(90, 119, "gold_3")
set_px(89, 123, "gold_3")

draw_line(98, 95, 94, 106, "robe_light")
draw_line(97, 96, 93, 107, "robe_hi")
for i in range(len(left_arm_poly) - 1):
    draw_line(left_arm_poly[i][0], left_arm_poly[i][1], left_arm_poly[i+1][0], left_arm_poly[i+1][1], "black")

# (H) Hand Resting on Pommel & Straight Jian Sword
hand_poly = [(86, 127), (93, 127), (94, 132), (89, 134), (85, 132), (86, 127)]
draw_poly(hand_poly, "skin_base")
draw_poly([(87, 128), (92, 128), (93, 131), (88, 132)], "skin_mid")
draw_line(87, 128, 92, 128, "skin_light")
set_px(89, 127, "skin_hi")
draw_line(86, 130, 92, 130, "skin_shadow")
for i in range(len(hand_poly) - 1):
    draw_line(hand_poly[i][0], hand_poly[i][1], hand_poly[i+1][0], hand_poly[i+1][1], "skin_dark")

# Straight Jian Pommel
draw_circle(89, 134, 3, "gold_2")
draw_circle(89, 134, 2, "gold_3")
set_px(89, 134, "gold_4")
draw_circle(89, 134, 3, "gold_0", fill=False)

# Sword Pommel Tassel
draw_line(89, 135, 94, 139, "gold_3")
draw_line(94, 139, 98, 142, "sash_mid")
draw_ellipse(99, 143, 3, 2, "sash_light")
tassel_fringe = [
    [(99, 144), (106, 148), (116, 154)],
    [(99, 145), (108, 150), (118, 157)],
    [(98, 145), (105, 152), (114, 160)]
]
for tr in tassel_fringe:
    for i in range(len(tr) - 1):
        draw_line(tr[i][0], tr[i][1], tr[i+1][0], tr[i+1][1], "sash_mid")
        draw_line(tr[i][0], tr[i][1] - 1, tr[i+1][0], tr[i+1][1] - 1, "sash_light")

# Hilt / Grip:
for gy in range(135, 147):
    draw_line(88, gy, 90, gy, "steel_1")
for gy in range(135, 147, 3):
    draw_line(88, gy, 90, gy + 1, "gold_2")
    draw_line(88, gy + 1, 90, gy, "boot_0")

# Guard:
guard_pts = [(82, 149), (85, 147), (89, 146), (93, 147), (96, 149), (93, 151), (89, 150), (85, 151), (82, 149)]
draw_poly(guard_pts, "gold_2")
draw_poly([(84, 148), (89, 147), (94, 148), (92, 150), (89, 149), (86, 150)], "gold_3")
draw_line(87, 147, 91, 147, "gold_4")
for i in range(len(guard_pts) - 1):
    draw_line(guard_pts[i][0], guard_pts[i][1], guard_pts[i+1][0], guard_pts[i+1][1], "gold_0")

# Scabbard:
scabbard_pts = [(87, 151), (91, 151), (83, 233), (79, 233), (87, 151)]
draw_poly(scabbard_pts, "sword_wood")

for sy in range(151, 233):
    t = (sy - 151) / (233 - 151)
    sx_center = (1 - t) * 89 + t * 81
    set_px(int(round(sx_center - 1)), sy, "sword_wood_l")
    set_px(int(round(sx_center)), sy, "sword_wood")
    set_px(int(round(sx_center + 1)), sy, "black")
    set_px(int(round(sx_center - 2)), sy, "steel_2")

# Fittings
for gy in range(151, 157):
    t = (gy - 151) / (233 - 151)
    sx = int(round((1 - t) * 89 + t * 81))
    draw_line(sx - 2, gy, sx + 2, gy, "gold_2")
    set_px(sx - 1, gy, "gold_4")
    set_px(sx, gy, "gold_3")

for gy in range(176, 182):
    t = (gy - 151) / (233 - 151)
    sx = int(round((1 - t) * 89 + t * 81))
    draw_line(sx - 2, gy, sx + 2, gy, "gold_2")
    set_px(sx - 1, gy, "gold_4")
    set_px(sx, gy, "gold_3")
t_ring = (178 - 151) / (233 - 151)
sx_ring = int(round((1 - t_ring) * 89 + t_ring * 81))
draw_circle(sx_ring + 3, 178, 2, "gold_3", fill=False)

for gy in range(227, 235):
    t = (gy - 151) / (233 - 151)
    sx = int(round((1 - t) * 89 + t * 81))
    draw_line(sx - 2, gy, sx + 2, gy, "gold_2")
    set_px(sx - 1, gy, "gold_4")
set_px(81, 234, "gold_3")
set_px(80, 234, "gold_4")
set_px(81, 235, "gold_0")

for i in range(len(scabbard_pts) - 1):
    draw_line(scabbard_pts[i][0], scabbard_pts[i][1], scabbard_pts[i+1][0], scabbard_pts[i+1][1], "black")

# (I) Bamboo Conical Hat (Douli) & Face
hat_pts = [
    (124, 38), (146, 46), (162, 53), (170, 60), (162, 64), (145, 66),
    (124, 67), (103, 66), (86, 64), (78, 60), (86, 53), (102, 46), (124, 38)
]
draw_poly(hat_pts, "douli_base")

for r_scale in [0.22, 0.45, 0.68, 0.86]:
    pts_ring = []
    for deg in range(0, 360, 12):
        rad = math.radians(deg)
        x_pt = 124 + math.cos(rad) * 46 * r_scale
        y_center = 38 + (60 - 38) * r_scale
        y_pt = y_center + math.sin(rad) * 8 * r_scale
        pts_ring.append((x_pt, y_pt))
    for i in range(len(pts_ring)):
        x0, y0 = pts_ring[i]
        x1, y1 = pts_ring[(i+1)%len(pts_ring)]
        draw_line(x0, y0, x1, y1, "douli_dark")
        draw_line(x0, y0 - 1, x1, y0 - 1, "douli_light")

for deg in range(5, 180, 10):
    rad = math.radians(deg)
    bx = 124 + math.cos(rad) * 46
    by = 60 + math.sin(rad) * 8
    draw_line(124, 38, bx, by, "douli_mid")
    draw_line(124, 38, bx + 1, by, "douli_dark")

draw_line(124, 38, 150, 48, "douli_hi")
draw_line(124, 39, 148, 49, "douli_bright")
draw_line(125, 38, 162, 53, "douli_light")
draw_line(126, 38, 166, 58, "douli_mid")

draw_line(124, 38, 94, 48, "douli_dark")
draw_line(123, 38, 84, 55, "douli_dark")
draw_line(122, 39, 80, 59, "douli_shadow")

draw_circle(124, 38, 3, "douli_dark")
draw_circle(124, 38, 2, "douli_mid")
draw_circle(124, 37, 1, "douli_bright")

for i in range(len(hat_pts) - 1):
    draw_line(hat_pts[i][0], hat_pts[i][1], hat_pts[i+1][0], hat_pts[i+1][1], "black")

# Head, Face & Neck
neck_pts = [(116, 76), (128, 76), (128, 85), (116, 85)]
draw_poly(neck_pts, "skin_shadow")

face_poly = [
    (115, 62), (129, 61), (132, 70), (129, 76), (123, 82), (117, 80), (114, 72), (115, 62)
]
draw_poly(face_poly, "skin_base")

hat_shadow_poly = [(114, 62), (130, 61), (132, 71), (126, 73), (120, 73), (114, 71), (114, 62)]
draw_poly(hat_shadow_poly, "skin_dark")

draw_line(116, 69, 119, 69, "black")
set_px(117, 69, "eye_white")
set_px(118, 69, "hair_0")
draw_line(115, 67, 120, 67, "black")

draw_line(120, 71, 120, 76, "skin_light")
set_px(120, 72, "skin_hi")
draw_line(121, 72, 121, 76, "skin_mid")
set_px(120, 76, "skin_shadow")

draw_line(119, 78, 123, 78, "skin_dark")
set_px(121, 78, "lip_red")
set_px(121, 79, "skin_shadow")

draw_line(117, 80, 123, 82, "skin_mid")
set_px(123, 82, "skin_light")
draw_line(123, 82, 129, 76, "skin_shadow")

draw_line(114, 72, 117, 80, "skin_dark")
draw_line(117, 80, 123, 82, "black")
draw_line(123, 82, 129, 76, "black")
draw_line(129, 76, 132, 70, "black")

lock_l = [(113, 62), (112, 74), (113, 84), (114, 96), (112, 100), (113, 86), (114, 75), (113, 62)]
draw_poly(lock_l, "hair_1")
draw_line(113, 72, 113, 90, "hair_3")
for i in range(len(lock_l) - 1):
    draw_line(lock_l[i][0], lock_l[i][1], lock_l[i+1][0], lock_l[i+1][1], "black")

lock_r = [(130, 63), (133, 74), (134, 84), (132, 94), (131, 85), (130, 74), (130, 63)]
draw_poly(lock_r, "hair_1")
draw_line(132, 72, 133, 86, "hair_2")
for i in range(len(lock_r) - 1):
    draw_line(lock_r[i][0], lock_r[i][1], lock_r[i+1][0], lock_r[i+1][1], "black")

draw_line(116, 68, 119, 83, "black")
draw_line(127, 67, 123, 83, "black")
draw_line(120, 83, 123, 84, "black")
draw_line(121, 84, 126, 90, "black")
draw_line(126, 90, 131, 95, "hair_2")

draw_line(78, 60, 103, 66, "douli_shadow")
draw_line(79, 61, 103, 67, "douli_dark")

# ----------------- 3. ATMOSPHERIC WIND & LEAVES -----------------
leaves = [
    (60, 136, "leaf_1", "leaf_2"),
    (70, 164, "leaf_2", "leaf_3"),
    (80, 192, "leaf_0", "leaf_1"),
    (156, 134, "leaf_1", "leaf_2"),
    (178, 156, "leaf_2", "leaf_3"),
    (196, 118, "leaf_0", "leaf_1"),
    (216, 144, "leaf_1", "leaf_2"),
    (230, 170, "leaf_2", "leaf_3"),
]
for lx, ly, c0, c1 in leaves:
    draw_ellipse(lx, ly, 3, 2, c0)
    set_px(lx - 1, ly - 1, c1)
    set_px(lx, ly, c1)
    set_px(lx + 2, ly + 1, "leaf_0")

# ----------------- 4. COMPOSITE & EXPORT -----------------
c = new_canvas(W, H)

color_map = {}
for name, rgb in PALETTE.items():
    hex_str = "#{:02x}{:02x}{:02x}".format(*rgb)
    color_map[name] = c.color(hex_str, name=name)

idx_array = np.zeros((H, W), dtype=np.int32)
for y in range(H):
    for x in range(W):
        col_name = grid[y, x]
        idx_array[y, x] = color_map[col_name]

c.px[:] = idx_array.flatten().tolist()

stats = c.stats()
print(f"Stats: colors used = {stats['colors_used']}, size = {stats['size']}")

view(c)
finish(c)
