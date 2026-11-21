import numpy as np
from pixelbench_api import *

# Canvas size
W, H = 256, 256
img = np.zeros((H, W, 3), dtype=np.uint8)

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

print(f"Total palette colors: {len(PALETTE)}")
