import math
import numpy as np

# Load original canvas
output = input_canvas.copy(name='output')
w, h = 256, 128

# Get original RGBA and palette indices
_, _, raw_bytes = output.to_rgba()
orig_indices = np.zeros((h, w), dtype=np.int32)
for y in range(h):
    for x in range(w):
        orig_indices[y, x] = output.get(x, y)

# Master Demon King Blood Moon Palette
pal_map = {
    0: (0, 0, 0, 0),         # transparent
    # Deep sky / abyss
    5: (4, 2, 6),            # abyssal black
    54: (12, 5, 14),
    34: (16, 6, 18),
    53: (14, 6, 16),
    0: (20, 8, 22),
    23: (18, 7, 20),
    67: (24, 9, 26),
    69: (22, 8, 24),
    48: (28, 10, 30),
    70: (26, 9, 28),
    52: (22, 8, 24),
    55: (24, 9, 26),
    71: (25, 9, 26),
    # Mid-dark sky
    1: (34, 11, 28),
    49: (40, 13, 32),
    24: (28, 10, 25),
    12: (38, 11, 32),
    19: (50, 13, 40),
    28: (60, 14, 46),
    # Sky midtones (deep wine / dark crimson night sky)
    2: (44, 13, 30),
    45: (48, 14, 32),
    47: (42, 13, 28),
    44: (50, 15, 34),
    51: (54, 16, 36),
    61: (58, 18, 38),
    64: (62, 19, 40),
    65: (52, 15, 34),
    66: (57, 17, 36),
    68: (46, 14, 30),
    3: (68, 20, 42),
    # Cloud shadows (dark volcanic purple & smoky charcoal)
    21: (36, 14, 30),
    37: (56, 18, 38),
    63: (48, 16, 34),
    32: (34, 12, 26),
    # Cloud midtones (crimson-mauve / dusty volcanic plum)
    22: (85, 26, 48),
    31: (75, 22, 42),
    20: (68, 20, 38),
    # Cloud highlights (illuminated by blood moon and volcanic fire)
    4: (124, 32, 50),
    26: (145, 40, 62),
    33: (114, 30, 46),
    35: (104, 27, 42),
    36: (158, 46, 68),
    9: (182, 58, 78),
    11: (212, 78, 92),
    # Celestial arcs / occult runes (blazing crimson & blood red)
    14: (255, 35, 45),
    15: (255, 45, 55),
    10: (255, 95, 105),
    50: (235, 25, 35),
    39: (215, 20, 30),
    27: (255, 65, 35),
    41: (185, 20, 32),
    42: (170, 18, 30),
    40: (155, 16, 28),
    46: (140, 15, 25),
    6: (115, 14, 22),
    7: (95, 12, 20),
    8: (105, 13, 22),
    13: (75, 10, 18),
    # Stars & Embers
    18: (255, 180, 50),
    43: (255, 55, 110),
    30: (255, 120, 35),
    # Castle dark obsidian & volcanic basalt (sharp contrast)
    16: (16, 10, 18),
    17: (26, 14, 22),
    29: (46, 20, 30),
    25: (75, 30, 42),
    72: (108, 42, 54),
    38: (142, 55, 66),
    # Foliage / charred dead woods
    60: (12, 7, 12),
    57: (18, 10, 15),
    62: (28, 14, 18),
    59: (38, 16, 20),
    56: (52, 20, 22),
}

res = new_canvas(w, h, name='demon_king')

# 1. Base palette application
for y in range(h):
    for x in range(w):
        idx = orig_indices[y, x]
        color = pal_map.get(idx, (20, 8, 20))
        res.set(x, y, color)

# Constants:
C_BLACK        = (4, 2, 6)
C_OBSIDIAN     = (16, 9, 16)
C_DARK_STONE   = (32, 14, 24)
C_MID_STONE    = (58, 22, 36)
C_HIGH_STONE   = (98, 36, 48)
C_RIM_RED      = (155, 45, 58)
C_BLOOD_PEAK   = (210, 55, 68)

# Blood Moon Palette:
C_MOON_HALO_OUTER = (60, 6, 16)
C_MOON_HALO_INNER = (95, 10, 24)
C_MOON_EDGE       = (145, 15, 30)
C_MOON_BODY       = (195, 24, 42)
C_MOON_BRIGHT     = (235, 38, 55)
C_MOON_GLOW       = (255, 65, 75)
C_MOON_CORE       = (255, 110, 115)
C_MOON_MARIA_DARK = (110, 12, 24)
C_MOON_MARIA_SOFT = (140, 16, 30)

# Lava / Hellfire Palette:
C_LAVA_WHITE   = (255, 255, 210)
C_LAVA_YELLOW  = (255, 215, 60)
C_LAVA_ORANGE  = (255, 115, 15)
C_LAVA_RED     = (225, 35, 10)
C_LAVA_DARK    = (130, 18, 12)
C_LAVA_CRUST   = (35, 10, 14)

# 2. HANGING BLOOD MOON at (136, 22), radius 16
mcx, mcy = 136, 22
m_rad = 16

def get_lunar_maria(dx, dy):
    val = (math.sin(dx * 0.45) * math.cos(dy * 0.45) +
           0.5 * math.sin(dx * 0.9 + dy * 0.7) +
           0.3 * math.cos(dx * 1.3 - dy * 1.1))
    d1 = math.hypot(dx + 4, dy - 1)
    d2 = math.hypot(dx - 5, dy + 4)
    if d1 < 4.5 or d2 < 3.8:
        val += 0.8
    return val

for dy in range(-m_rad - 6, m_rad + 7):
    for dx in range(-m_rad - 6, m_rad + 7):
        dist = math.hypot(dx, dy)
        x = mcx + dx
        y = mcy + dy
        if not (0 <= x < w and 0 <= y < h):
            continue
        
        if dist > m_rad + 4.5:
            continue
        elif dist > m_rad + 2.5:
            if (x + y) % 2 == 0:
                res.set(x, y, C_MOON_HALO_OUTER)
        elif dist > m_rad + 0.8:
            res.set(x, y, C_MOON_HALO_INNER)
        elif dist > m_rad - 0.5:
            res.set(x, y, C_MOON_EDGE)
        else:
            maria_val = get_lunar_maria(dx, dy)
            illum = -(dy * 0.7 + dx * 0.3) / m_rad
            
            if dist < m_rad - 2 and illum > 0.4 and maria_val < 0.2:
                col = C_MOON_CORE if (dist < 8 and illum > 0.6) else C_MOON_GLOW
            elif maria_val > 0.75:
                col = C_MOON_MARIA_DARK
            elif maria_val > 0.3:
                col = C_MOON_MARIA_SOFT
            elif dist < m_rad - 2:
                col = C_MOON_BRIGHT if illum > 0.0 else C_MOON_BODY
            else:
                col = C_MOON_EDGE
            res.set(x, y, col)

# 3. Occult Summoning Circles & Runes around Blood Moon
for angle_deg in range(0, 360, 3):
    rad = math.radians(angle_deg)
    ix = int(round(mcx + 21 * math.cos(rad)))
    iy = int(round(mcy + 21 * math.sin(rad)))
    if 0 <= ix < w and 0 <= iy < h:
        if angle_deg % 6 == 0:
            res.set(ix, iy, C_MOON_GLOW)
    
    if angle_deg % 30 == 0:
        for r_step in range(23, 29):
            sx = int(round(mcx + r_step * math.cos(rad)))
            sy = int(round(mcy + r_step * math.sin(rad)))
            if 0 <= sx < w and 0 <= sy < h:
                res.set(sx, sy, C_LAVA_ORANGE if r_step == 23 else C_MOON_GLOW)

for tx in range(88, 116):
    if orig_indices[23, tx] in [7, 8, 14, 15, 39, 40]:
        res.set(tx, 23, C_MOON_GLOW)
        res.set(tx, 22, C_MOON_HALO_INNER)
for tx in range(156, 184):
    if orig_indices[23, tx] in [7, 8, 14, 15, 39, 40]:
        res.set(tx, 23, C_MOON_GLOW)
        res.set(tx, 22, C_MOON_HALO_INNER)

# 4. Demon King's Citadel Architecture

# A. Sweeping Curved Demonic Horns on Central Spire
left_horn_spine = [
    (134, 25), (133, 24), (131, 23), (129, 21), (127, 19), (125, 17), (124, 14),
    (124, 11), (125, 8), (127, 6), (129, 4)
]
for i, (hx, hy) in enumerate(left_horn_spine):
    res.set(hx, hy, C_RIM_RED)
    if i < len(left_horn_spine) - 2:
        res.set(hx + 1, hy, C_OBSIDIAN)
        res.set(hx + 1, hy + 1, C_DARK_STONE)
        if i < 6:
            res.set(hx + 2, hy + 1, C_BLACK)

right_horn_spine = [
    (138, 25), (139, 24), (141, 23), (143, 21), (145, 19), (147, 17), (148, 14),
    (148, 11), (147, 8), (145, 6), (143, 4)
]
for i, (hx, hy) in enumerate(right_horn_spine):
    res.set(hx, hy, C_RIM_RED)
    if i < len(right_horn_spine) - 2:
        res.set(hx - 1, hy, C_OBSIDIAN)
        res.set(hx - 1, hy + 1, C_DARK_STONE)
        if i < 6:
            res.set(hx - 2, hy + 1, C_BLACK)

# Floating Flaming Demonic Eye of Chaos at (136, 14)
eye_cx, eye_cy = 136, 14
for dy in range(-3, 4):
    for dx in range(-3, 4):
        d = math.hypot(dx, dy * 1.3)
        if d <= 3.2:
            res.set(eye_cx + dx, eye_cy + dy, C_LAVA_ORANGE)
        if d <= 2.2:
            res.set(eye_cx + dx, eye_cy + dy, C_LAVA_YELLOW)
        if d <= 1.2:
            res.set(eye_cx + dx, eye_cy + dy, C_LAVA_WHITE)
for py in range(-2, 3):
    res.set(eye_cx, eye_cy + py, C_BLACK)

# Spikes on central tower balcony
res.set(133, 29, C_RIM_RED)
res.set(132, 29, C_LAVA_ORANGE)
res.set(139, 29, C_OBSIDIAN)
res.set(140, 29, C_LAVA_ORANGE)

res.set(132, 35, C_RIM_RED)
res.set(131, 35, C_BLOOD_PEAK)
res.set(140, 35, C_OBSIDIAN)
res.set(141, 35, C_BLOOD_PEAK)

# B. Slender Gothic Spires on flanking towers
left_spire_pts = [
    (109, 36), (109, 37), (109, 38), (109, 39),
    (108, 40), (109, 40), (110, 40),
    (108, 41), (109, 41), (110, 41),
    (108, 42), (109, 42), (110, 42),
    (107, 43), (108, 43), (109, 43), (110, 43), (111, 43),
    (107, 44), (108, 44), (109, 44), (110, 44), (111, 44),
    (107, 45), (108, 45), (109, 45), (110, 45), (111, 45),
]
for sx, sy in left_spire_pts:
    if sx <= 108:
        res.set(sx, sy, C_RIM_RED)
    elif sx == 109:
        res.set(sx, sy, C_MID_STONE)
    else:
        res.set(sx, sy, C_OBSIDIAN)
res.set(106, 43, C_RIM_RED)
res.set(112, 43, C_OBSIDIAN)

right_spire_pts = [
    (155, 35), (155, 36), (155, 37), (155, 38),
    (154, 39), (155, 39), (156, 39),
    (154, 40), (155, 40), (156, 40),
    (154, 41), (155, 41), (156, 41),
    (153, 42), (154, 42), (155, 42), (156, 42), (157, 42),
    (153, 43), (154, 43), (155, 43), (156, 43), (157, 43),
]
for sx, sy in right_spire_pts:
    if sx <= 154:
        res.set(sx, sy, C_RIM_RED)
    elif sx == 155:
        res.set(sx, sy, C_MID_STONE)
    else:
        res.set(sx, sy, C_OBSIDIAN)
res.set(152, 42, C_RIM_RED)
res.set(158, 42, C_OBSIDIAN)

# Outpost spires on the left ridge
for sy in range(86, 94):
    res.set(36, sy, C_RIM_RED)
    res.set(37, sy, C_OBSIDIAN)
for sy in range(85, 93):
    res.set(54, sy, C_RIM_RED)
    res.set(55, sy, C_OBSIDIAN)

# C. Glowing Hellfire Windows & Sinister Slits
citadel_windows = [
    (135, 27), (137, 27),
    (135, 35), (137, 35),
    (134, 41), (138, 41),
    (128, 51), (129, 51),
    (143, 53), (144, 53),
    (109, 61), (110, 61),
    (118, 67), (119, 67),
    (135, 65), (136, 65),
    (153, 63), (154, 63),
    (160, 71),
    (124, 77), (125, 77),
    (144, 75), (145, 75),
    (102, 81), (103, 81),
    (112, 87), (113, 87),
    (138, 85), (139, 85),
    (156, 83), (157, 83),
    (36, 95), (54, 94),
]
for wx, wy in citadel_windows:
    res.set(wx, wy, C_LAVA_YELLOW)
    res.set(wx, wy - 1, C_LAVA_RED)

# Hellfire Braziers / Torches along walls and bridges
braziers = [
    (114, 101), (118, 105), (123, 107), (132, 109), (144, 113),
    (108, 70), (160, 76), (128, 84), (142, 82),
]
for bx, by in braziers:
    res.set(bx, by, C_LAVA_YELLOW)
    res.set(bx, by - 1, C_LAVA_ORANGE)

# D. The Great Hell Gate Portal at (122..126, 93..97)
for gy in range(92, 98):
    for gx in range(121, 127):
        if gy == 92 and gx in (121, 126):
            continue
        if gy == 92 or gx in (121, 126):
            res.set(gx, gy, C_LAVA_RED)
        else:
            if gx in (123, 124) and gy in (94, 95, 96):
                res.set(gx, gy, C_LAVA_WHITE)
            elif gy in (93, 94, 95, 96):
                res.set(gx, gy, C_LAVA_YELLOW)
            else:
                res.set(gx, gy, C_LAVA_ORANGE)

# 5. Natural Organic MOLTEN LAVA RIVER on the winding road
for y in range(95, 128):
    for x in range(100, 168):
        orig_idx = orig_indices[y, x]
        if orig_idx in [18, 30]:
            res.set(x, y, C_LAVA_WHITE if (x + y) % 3 == 0 else C_LAVA_YELLOW)
        elif orig_idx in [38]:
            res.set(x, y, C_LAVA_ORANGE)
        elif orig_idx in [72]:
            res.set(x, y, C_LAVA_RED)
        elif orig_idx in [25]:
            res.set(x, y, C_LAVA_CRUST if (x + y) % 2 == 0 else C_LAVA_DARK)

# Volcanic lava fissures branching across the mountain rock
fissures = [
    [(114, 104), (111, 105), (107, 106), (104, 107), (100, 109), (96, 110)],
    [(139, 112), (141, 115), (142, 118), (141, 122), (140, 126)],
    [(128, 86), (128, 89), (127, 92), (126, 94)],
    [(153, 123), (157, 122), (162, 121), (167, 120), (172, 121), (178, 123)],
]
for f_line in fissures:
    for i, (fx, fy) in enumerate(f_line):
        if 0 <= fx < w and 0 <= fy < h:
            res.set(fx, fy, C_LAVA_YELLOW if i % 2 == 0 else C_LAVA_ORANGE)
            if fx + 1 < w:
                res.set(fx + 1, fy, C_LAVA_RED)

# 6. Dead Demonic Tree Silhouette (bottom-right: x=220..255, y=80..127)
dead_branches = [
    (241, 112), (242, 108), (243, 104), (244, 100), (244, 96), (245, 92),
    (243, 104), (240, 102), (237, 100), (234, 97), (231, 95), (228, 92), (226, 90), (224, 87),
    (231, 95), (229, 97), (226, 98), (223, 99),
    (245, 92), (246, 88), (247, 85), (247, 81), (246, 78),
    (246, 88), (243, 86), (240, 84), (238, 82),
    (245, 96), (248, 94), (251, 92), (254, 90),
]
for bx, by in dead_branches:
    if 0 <= bx < w and 0 <= by < h:
        res.set(bx, by, C_BLACK)
        if by > 85:
            res.set(bx, by + 1, C_BLACK)
            if bx + 1 < w:
                res.set(bx + 1, by, C_OBSIDIAN)

# Glowing evil eyes in the dead tree
res.set(234, 102, C_LAVA_YELLOW)
res.set(236, 102, C_LAVA_YELLOW)
res.set(244, 110, C_MOON_GLOW)
res.set(246, 110, C_MOON_GLOW)

# 7. Drifting Embers and Hellish Sparks
import random
rng = random.Random(777)
for _ in range(60):
    ex = rng.randint(85, 185)
    ey = rng.randint(10, 105)
    if math.hypot(ex - mcx, ey - mcy) < 16:
        continue
    ember_col = rng.choice([C_LAVA_YELLOW, C_LAVA_ORANGE, C_MOON_GLOW, C_MOON_BRIGHT])
    res.set(ex, ey, ember_col)

# View and finish
view(res)
finish(res)
