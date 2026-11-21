import numpy as np
from pixelbench_api import *

def render_masterpiece():
    c = new_canvas(128, 128)
    
    # -------------------------------------------------------------
    # 1. PALETTE DEFINITIONS
    # -------------------------------------------------------------
    # Sky / Sunset
    SKY_0 = "#0b0716"
    SKY_1 = "#160e29"
    SKY_2 = "#26123b"
    SKY_3 = "#3e1547"
    SKY_4 = "#611a4c"
    SKY_5 = "#872249"
    SKY_6 = "#b0323e"
    SKY_7 = "#d14e32"
    SKY_8 = "#e8732e"
    SKY_9 = "#f59f3d"
    SUN_GOLD = "#fcd05d"
    SUN_CORE = "#fff1a8"
    SUN_WHITE = "#ffffff"

    # Ruins & Mountains
    MNT_DARK = "#1a0f26"
    RUIN_WALL = "#120b1c"
    RUIN_EDGE = "#351c3d"
    RUIN_GOLD = "#6e2e48"

    # Ground
    GND_DEEP = "#0c0812"
    GND_DARK = "#181220"
    GND_MID = "#281f30"
    GND_LIGHT = "#3d3245"
    GND_SURF = "#594c61"
    GND_GOLD_RIM = "#a87158"

    # Red Knight Palette
    K_OUTLINE = "#120308"
    K_SHADE = "#2b050f"
    K_RED_DARK = "#520a17"
    K_RED_MID = "#871221"
    K_RED_BRIGHT = "#c21d2d"
    K_RED_LIGHT = "#eb3846"
    K_RED_SPEC = "#ffa1ab"

    K_GOLD_DARK = "#3d2005"
    K_GOLD_MID = "#7a460b"
    K_GOLD_BRIGHT = "#c2911d"
    K_GOLD_LIGHT = "#fae164"

    K_STEEL_DARK = "#14161f"
    K_STEEL_MID = "#3f475c"
    K_STEEL_LIGHT = "#7484a3"
    K_STEEL_BRIGHT = "#b5c7e3"
    K_STEEL_WHITE = "#ffffff"

    K_VISOR_CYAN = "#22f2e6"
    K_VISOR_CORE = "#d4fffc"

    K_PLUME_DARK = "#4a0814"
    K_PLUME_MID = "#8f1426"
    K_PLUME_LIGHT = "#db273b"
    K_PLUME_TIP = "#ff6373"

    # Green Rogue Palette
    R_OUTLINE = "#050e07"
    R_CLOAK_DARK = "#0d2114"
    R_CLOAK_MID = "#164526"
    R_CLOAK_BRIGHT = "#22703c"
    R_CLOAK_LIGHT = "#38ab5e"
    R_CLOAK_SPEC = "#70e395"
    R_CLOAK_TIP = "#baffd3"

    R_LEATHER_DARK = "#110e14"
    R_LEATHER_MID = "#261e27"
    R_LEATHER_LIGHT = "#453744"
    R_LEATHER_GOLD = "#6e5852"

    R_EYE_AMBER = "#ffb017"
    R_EYE_CORE = "#fff596"

    # FX
    FX_EMBER_1 = "#c73a24"
    FX_EMBER_2 = "#ff9924"
    FX_EMBER_3 = "#ffea78"

    # -------------------------------------------------------------
    # 2. BACKGROUND & SKY
    # -------------------------------------------------------------
    bands = [
        (0, 11, SKY_0), (12, 22, SKY_1), (23, 33, SKY_2), (34, 44, SKY_3),
        (45, 54, SKY_4), (55, 64, SKY_5), (65, 73, SKY_6), (74, 82, SKY_7),
        (83, 90, SKY_8), (91, 98, SKY_9)
    ]
    for y0, y1, col in bands:
        c.rect(0, y0, 128, y1 - y0 + 1, col)

    for i in range(len(bands) - 1):
        yb = bands[i][1]
        c_nxt = bands[i+1][2]
        c_cur = bands[i][2]
        for x in range(128):
            if (x + yb) % 3 == 0:
                c.set(x, yb, c_nxt)
            if (x + yb + 1) % 3 == 0:
                c.set(x, yb + 1, c_cur)

    # Setting Sun
    sun_cx, sun_cy = 64, 75
    c.circle(sun_cx, sun_cy, 24, SKY_8, fill=True)
    c.circle(sun_cx, sun_cy, 19, SKY_9, fill=True)
    c.circle(sun_cx, sun_cy, 15, SUN_GOLD, fill=True)
    c.circle(sun_cx, sun_cy, 11, SUN_CORE, fill=True)
    c.circle(sun_cx, sun_cy, 7, SUN_WHITE, fill=True)

    c.line(26, 75, 102, 75, SUN_CORE)
    c.line(40, 74, 88, 74, SUN_GOLD)
    c.line(40, 76, 88, 76, SUN_GOLD)
    c.line(50, 75, 78, 75, SUN_WHITE)

    # Clouds
    c.line(8, 24, 42, 24, SKY_3)
    c.line(12, 23, 38, 23, SKY_5)
    c.line(78, 34, 120, 34, SKY_4)
    c.line(84, 33, 114, 33, SKY_6)
    c.line(14, 48, 48, 48, SKY_4)
    c.line(86, 54, 124, 54, SKY_5)

    # Mountains
    mnt_pts = [
        (0, 98), (0, 76), (14, 73), (26, 77), (38, 72), (50, 76),
        (64, 78), (78, 75), (90, 70), (104, 74), (116, 69), (127, 72), (127, 98)
    ]
    c.poly(mnt_pts, MNT_DARK, fill=True)

    # Spires
    c.rect(4, 56, 10, 42, RUIN_WALL)
    c.poly([(3, 56), (9, 44), (15, 56)], RUIN_WALL, fill=True)
    c.line(9, 44, 9, 39, RUIN_GOLD)
    c.rect(7, 63, 3, 7, SKY_5)
    c.line(14, 56, 14, 98, RUIN_EDGE)

    c.rect(20, 68, 4, 30, RUIN_WALL)
    c.line(20, 68, 23, 68, RUIN_EDGE)
    c.line(24, 68, 24, 98, RUIN_EDGE)

    c.rect(114, 55, 9, 43, RUIN_WALL)
    c.poly([(113, 55), (118, 45), (124, 55)], RUIN_WALL, fill=True)
    c.line(118, 45, 118, 40, RUIN_GOLD)
    c.line(114, 55, 114, 98, RUIN_EDGE)
    c.rect(104, 67, 5, 31, RUIN_WALL)
    c.line(104, 67, 108, 67, RUIN_EDGE)

    # -------------------------------------------------------------
    # 3. GROUND
    # -------------------------------------------------------------
    ground_y = 98
    c.rect(0, ground_y, 128, 128 - ground_y, GND_MID)
    for x in range(128):
        edge_col = GND_GOLD_RIM if (32 <= x <= 96) else GND_SURF
        c.set(x, ground_y, edge_col)
        c.set(x, ground_y + 1, GND_SURF if (x % 3 == 0) else GND_MID)

    for sy in [104, 112, 120]:
        c.line(0, sy, 127, sy, GND_DEEP)
        c.line(0, sy + 1, 127, sy + 1, GND_LIGHT)
    c.line(0, 127, 127, 127, GND_DEEP)

    v_cracks = [
        (12, 99, 104), (28, 99, 104), (46, 99, 104), (64, 99, 104), (82, 99, 104), (102, 99, 104), (120, 99, 104),
        (6, 104, 112), (22, 104, 112), (38, 104, 112), (56, 104, 112), (74, 104, 112), (92, 104, 112), (110, 104, 112),
        (16, 112, 120), (34, 112, 120), (52, 112, 120), (70, 112, 120), (88, 112, 120), (106, 112, 120),
        (24, 120, 127), (44, 120, 127), (66, 120, 127), (86, 120, 127), (108, 120, 127)
    ]
    for vx, vy0, vy1 in v_cracks:
        for vy in range(vy0, vy1):
            c.set(vx + (vy % 2), vy, GND_DEEP)
            c.set(vx + (vy % 2) + 1, vy, GND_SURF)

    # Center fracture
    frac = [(58, 99), (59, 102), (61, 105), (60, 108), (63, 113), (62, 118), (65, 123), (66, 127)]
    for i in range(len(frac) - 1):
        x0, y0 = frac[i]
        x1, y1 = frac[i+1]
        c.line(x0, y0, x1, y1, GND_DEEP)
        c.line(x0 + 1, y0, x1 + 1, y1, GND_GOLD_RIM)

    # -------------------------------------------------------------
    # 4. RED KNIGHT
    # -------------------------------------------------------------
    # Shadows
    c.line(16, 100, 25, 100, GND_DEEP)
    c.line(33, 100, 44, 100, GND_DEEP)

    # Solid Cape (flowing back to left: x=10..24, y=60..97)
    for y in range(60, 98):
        t = (y - 60) / 37.0
        x0 = int(24 - 14 * t)
        x1 = int(27 - 5 * t)
        c.line(x0, y, x1, y, K_RED_DARK)
        c.set(x0, y, K_OUTLINE)
        c.set(x0 + 1, y, K_SHADE)
        c.set(x1, y, K_RED_MID)
    # Highlight folds on cape
    c.line(15, 76, 19, 93, K_RED_MID)
    c.line(18, 66, 22, 85, K_RED_BRIGHT)

    # Helmet Plume: arching back from top of helm
    plume_coords = [
        (29, 47), (28, 46), (27, 45), (26, 44), (25, 43), (24, 43),
        (23, 42), (22, 42), (21, 41), (20, 41), (19, 41), (18, 42),
        (17, 42), (16, 43), (15, 43), (14, 44), (13, 45)
    ]
    for px, py in plume_coords:
        c.set(px, py, K_PLUME_LIGHT)
        c.set(px, py - 1, K_OUTLINE)
        c.set(px, py + 1, K_PLUME_MID)
    c.line(19, 41, 25, 42, K_PLUME_TIP)
    c.line(22, 41, 24, 41, K_RED_SPEC)

    # Back Leg (Left Leg: braced back at x=20..26, y=78..100)
    for y in range(78, 86):
        c.line(21, y, 25, y, K_RED_DARK)
        c.set(20, y, K_OUTLINE)
        c.set(26, y, K_SHADE)
    # Knee cop
    for y in range(86, 90):
        c.line(19, y, 24, y, K_RED_MID)
        c.set(18, y, K_OUTLINE)
    c.set(21, 87, K_GOLD_BRIGHT)
    # Shin / Greave
    for y in range(90, 98):
        c.line(19, y, 23, y, K_RED_DARK)
        c.set(18, y, K_OUTLINE)
        c.set(20, y, K_RED_MID)
    # Sabaton
    c.line(17, 98, 24, 98, K_STEEL_MID)
    c.line(16, 99, 24, 99, K_STEEL_DARK)
    c.line(17, 100, 24, 100, K_OUTLINE)
    c.set(23, 98, K_STEEL_LIGHT)

    # Front Leg (Right Leg: stepped forward at x=32..42, y=78..100)
    for y in range(78, 86):
        x_st = 30 + (y - 78) // 3
        c.line(x_st, y, x_st + 5, y, K_RED_MID)
        c.line(x_st + 2, y, x_st + 5, y, K_RED_BRIGHT)
        c.set(x_st - 1, y, K_OUTLINE)
        c.set(x_st + 6, y, K_GOLD_BRIGHT)
    # Knee cop
    for y in range(86, 90):
        c.line(33, y, 38, y, K_RED_BRIGHT)
        c.set(32, y, K_OUTLINE)
        c.set(39, y, K_RED_LIGHT)
    c.line(34, 87, 37, 87, K_GOLD_LIGHT)
    c.set(38, 87, K_RED_SPEC)
    # Shin / Greave
    for y in range(90, 98):
        c.line(34, y, 39, y, K_RED_MID)
        c.line(37, y, 39, y, K_RED_BRIGHT)
        c.set(33, y, K_OUTLINE)
        c.set(40, y, K_RED_LIGHT)
    # Sabaton
    c.line(33, 98, 42, 98, K_STEEL_LIGHT)
    c.line(32, 99, 42, 99, K_STEEL_MID)
    c.line(33, 100, 42, 100, K_OUTLINE)
    c.set(41, 98, K_STEEL_WHITE)

    # Faulds / Tassets (y=73..78, x=26..34)
    for y in range(73, 79):
        c.line(26, y, 34, y, K_RED_MID)
        c.line(30, y, 34, y, K_RED_BRIGHT)
        c.set(25, y, K_OUTLINE)
        c.set(35, y, K_GOLD_BRIGHT)
    c.line(26, 73, 34, 73, K_GOLD_MID)
    c.line(29, 73, 31, 73, K_GOLD_LIGHT)
    c.line(26, 78, 34, 78, K_GOLD_BRIGHT)

    # Breastplate (y=60..73, tapering from chest x=26..35 to waist x=27..33)
    for y in range(60, 73):
        w_left = 26 if y < 67 else 27
        w_right = 35 if y < 66 else (34 if y < 70 else 33)
        c.line(w_left, y, w_right, y, K_RED_MID)
        c.line(w_left + 4, y, w_right, y, K_RED_BRIGHT)
        c.set(w_left - 1, y, K_OUTLINE)
        c.set(w_right + 1, y, K_RED_LIGHT)
    c.line(28, 64, 33, 64, K_GOLD_BRIGHT)
    c.line(30, 62, 30, 66, K_GOLD_BRIGHT)
    c.set(30, 64, K_GOLD_LIGHT)

    # Back Pauldron (x=23..26, y=58..64)
    for y in range(58, 65):
        c.line(23, y, 26, y, K_RED_DARK)
        c.set(22, y, K_OUTLINE)
    c.line(22, 58, 22, 64, K_GOLD_MID)

    # Helmet (x=27..35, y=49..57)
    c.line(29, 49, 33, 49, K_GOLD_BRIGHT)
    c.set(31, 48, K_GOLD_LIGHT)
    for y in range(50, 54):
        c.line(28, y, 34, y, K_RED_MID)
        c.line(31, y, 34, y, K_RED_BRIGHT)
        c.set(27, y, K_OUTLINE)
        c.set(35, y, K_OUTLINE)
    # Slanted glowing visor slit
    c.line(29, 53, 34, 53, K_OUTLINE)
    c.line(30, 53, 34, 53, K_VISOR_CYAN)
    c.set(33, 53, K_VISOR_CORE)
    c.set(34, 53, K_STEEL_WHITE)
    for y in range(54, 58):
        c.line(29, y, 33, y, K_RED_MID)
        c.set(28, y, K_OUTLINE)
        c.set(34, y, K_RED_LIGHT)
    c.set(31, 57, K_GOLD_LIGHT)

    # Neck
    c.line(29, 58, 32, 58, K_STEEL_DARK)
    c.line(29, 59, 32, 59, K_STEEL_MID)

    # Front Pauldron (Right shoulder: x=34..41, y=57..66)
    for y in range(57, 67):
        pw = 6 if (59 <= y <= 64) else 4
        c.line(34, y, 34 + pw, y, K_RED_BRIGHT)
        c.set(33, y, K_OUTLINE)
        c.set(34 + pw + 1, y, K_OUTLINE)
        c.set(34 + pw, y, K_RED_LIGHT)
    c.line(35, 57, 39, 57, K_GOLD_LIGHT)
    c.line(39, 58, 41, 62, K_GOLD_LIGHT)
    c.line(41, 63, 39, 66, K_GOLD_BRIGHT)
    c.line(35, 66, 38, 66, K_GOLD_MID)
    c.set(41, 61, K_STEEL_WHITE)

    # Arms & Greatsword
    # Right arm & gauntlet: x=34..38, y=66..71
    c.poly([(34, 66), (38, 66), (39, 71), (35, 71)], K_STEEL_MID, fill=True)
    c.line(35, 69, 39, 69, K_GOLD_BRIGHT)
    c.line(28, 67, 33, 70, K_STEEL_MID)

    # Hilt & Crossguard
    c.circle(34, 73, 1, K_GOLD_BRIGHT, fill=True)
    c.line(35, 72, 37, 70, K_STEEL_DARK)
    c.line(37, 71, 40, 67, K_GOLD_LIGHT)
    c.line(36, 70, 39, 66, K_GOLD_BRIGHT)
    c.set(38, 69, K_RED_BRIGHT)

    # Slender Greatsword Blade (extends from (39, 68) to (54, 77))
    blade_pts = [
        (39, 68), (40, 69), (41, 69), (42, 70), (43, 70), (44, 71), (45, 71),
        (46, 72), (47, 73), (48, 73), (49, 74), (50, 74), (51, 75), (52, 75),
        (53, 76), (54, 77)
    ]
    for bx, by in blade_pts:
        c.set(bx, by, K_STEEL_LIGHT)
        c.set(bx, by + 1, K_STEEL_MID)
        c.set(bx - 1, by + 1, K_STEEL_DARK)
    c.line(43, 70, 52, 75, K_STEEL_BRIGHT)
    c.line(46, 72, 51, 75, K_STEEL_WHITE)
    c.set(54, 77, K_STEEL_WHITE)
    c.set(55, 78, K_STEEL_WHITE)
    c.set(54, 79, K_VISOR_CYAN)

    # -------------------------------------------------------------
    # 5. GREEN-CLOAKED ROGUE
    # -------------------------------------------------------------
    c.line(75, 100, 85, 100, GND_DEEP)
    c.line(101, 100, 111, 100, GND_DEEP)

    # Solid Cloak Billowing (x=97..124, y=63..95)
    for y in range(63, 96):
        t = (y - 63) / 32.0
        x0 = int(96 + 3 * t)
        x1 = int(103 + 19 * np.sin(t * np.pi * 0.85) + 3 * np.cos(t * np.pi * 2))
        x1 = min(x1, 126)
        c.line(x0, y, x1, y, R_CLOAK_MID)
        c.line(x1 - 3, y, x1, y, R_CLOAK_LIGHT)
        c.set(x0, y, R_CLOAK_DARK)
        c.set(x1, y, R_OUTLINE)
        c.set(x1 - 1, y, R_CLOAK_SPEC if y % 2 == 0 else R_CLOAK_LIGHT)
    c.set(122, 71, R_CLOAK_SPEC)
    c.set(124, 75, R_CLOAK_TIP)
    c.set(120, 83, R_CLOAK_SPEC)

    # Rear Leg (Right leg stretched back: x=96..110, y=80..100)
    for y in range(80, 88):
        c.line(96, y, 102, y, R_LEATHER_DARK)
        c.set(95, y, R_OUTLINE)
        c.set(103, y, R_LEATHER_MID)
    for y in range(88, 98):
        c.line(100, y, 106, y, R_LEATHER_MID)
        c.set(99, y, R_OUTLINE)
        c.set(107, y, R_OUTLINE)
        if y % 3 == 0:
            c.line(101, y, 105, y, R_LEATHER_LIGHT)
    c.line(102, 98, 109, 98, R_LEATHER_LIGHT)
    c.line(101, 99, 109, 99, R_LEATHER_MID)
    c.line(102, 100, 109, 100, R_OUTLINE)

    # Lead Leg (Left leg deep bent crouch: x=77..88, y=80..100)
    for y in range(80, 88):
        c.line(80, y, 88, y, R_LEATHER_MID)
        c.line(80, y, 84, y, R_LEATHER_LIGHT)
        c.set(79, y, R_OUTLINE)
        c.set(89, y, R_LEATHER_DARK)
    for y in range(88, 92):
        c.line(78, y, 84, y, R_LEATHER_MID)
        c.set(77, y, R_OUTLINE)
        c.set(78, y, R_LEATHER_LIGHT)
    for y in range(92, 98):
        c.line(79, y, 84, y, R_LEATHER_MID)
        c.set(78, y, R_OUTLINE)
        c.set(85, y, R_LEATHER_DARK)
        if y % 3 == 0:
            c.line(79, y, 83, y, R_LEATHER_LIGHT)
    c.line(76, 98, 84, 98, R_LEATHER_GOLD)
    c.line(75, 99, 84, 99, R_LEATHER_MID)
    c.line(76, 100, 84, 100, R_OUTLINE)

    # Torso (Coiled crouch: x=86..95, y=66..79)
    for y in range(66, 80):
        c.line(86, y, 94, y, R_LEATHER_MID)
        c.line(86, y, 89, y, R_LEATHER_LIGHT)
        c.set(85, y, R_OUTLINE)
        c.set(95, y, R_OUTLINE)
    c.line(87, 67, 93, 77, R_LEATHER_GOLD)
    c.line(93, 67, 87, 75, R_LEATHER_GOLD)
    c.set(90, 72, K_GOLD_BRIGHT)
    c.line(85, 78, 95, 78, R_CLOAK_MID)
    c.line(85, 79, 95, 79, R_CLOAK_BRIGHT)

    # Assassin Hood & Face (x=87..96, y=56..65)
    c.line(90, 56, 94, 56, R_CLOAK_BRIGHT)
    c.set(89, 56, R_OUTLINE)
    c.set(95, 56, R_OUTLINE)
    for y in range(57, 65):
        c.line(88, y, 95, y, R_CLOAK_MID)
        c.line(88, y, 91, y, R_CLOAK_BRIGHT)
        c.set(87, y, R_OUTLINE)
        c.set(96, y, R_OUTLINE)
    # Pointed beak of hood
    c.line(86, 58, 88, 57, R_CLOAK_LIGHT)
    c.line(85, 59, 87, 59, R_CLOAK_BRIGHT)
    c.line(86, 60, 88, 61, R_CLOAK_MID)
    c.set(84, 59, R_OUTLINE)

    # Shadow under hood & mask
    c.rect(87, 60, 5, 4, R_OUTLINE)
    c.line(87, 63, 92, 63, R_LEATHER_MID)
    c.line(87, 64, 92, 64, R_LEATHER_DARK)

    # Amber eye!
    c.line(88, 61, 91, 61, R_EYE_AMBER)
    c.set(89, 61, R_EYE_CORE)
    c.set(88, 61, SUN_WHITE)

    # Shoulder cowl
    for y in range(65, 69):
        c.line(85, y, 93, y, R_CLOAK_MID)
        c.line(85, y, 88, y, R_CLOAK_BRIGHT)
        c.set(84, y, R_OUTLINE)

    # Lead Arm & Forward Dagger (x=66..84, y=70..78)
    c.line(84, 70, 78, 74, R_LEATHER_MID)
    c.line(83, 71, 77, 75, R_LEATHER_DARK)
    c.line(78, 74, 74, 77, R_LEATHER_LIGHT)
    c.set(73, 77, K_GOLD_MID)

    # Dagger blade extending forward-up
    dag_pts = [(72, 76), (71, 75), (70, 74), (69, 74), (68, 73), (67, 73), (66, 72)]
    for dx, dy in dag_pts:
        c.set(dx, dy, K_STEEL_LIGHT)
        c.set(dx, dy + 1, K_STEEL_MID)
    c.set(66, 72, K_STEEL_WHITE)
    c.set(65, 71, K_STEEL_WHITE)
    c.set(66, 73, R_CLOAK_SPEC)

    # Rear Arm & Reverse Stiletto (x=95..109, y=66..81)
    c.line(95, 67, 101, 70, R_LEATHER_MID)
    c.line(101, 70, 103, 73, R_LEATHER_LIGHT)
    c.set(103, 72, K_GOLD_MID)
    stiletto_pts = [(104, 74), (105, 75), (106, 77), (107, 79), (108, 81)]
    for sx, sy in stiletto_pts:
        c.set(sx, sy, K_STEEL_LIGHT)
        c.set(sx + 1, sy, K_STEEL_MID)
    c.set(108, 81, K_STEEL_WHITE)

    # -------------------------------------------------------------
    # 6. ATMOSPHERE & GAP TENSION
    # -------------------------------------------------------------
    embers = [
        (59, 71, FX_EMBER_2), (63, 67, FX_EMBER_3), (66, 72, FX_EMBER_1),
        (56, 61, FX_EMBER_3), (68, 63, FX_EMBER_2), (58, 79, FX_EMBER_1),
        (63, 81, FX_EMBER_3), (53, 68, FX_EMBER_2), (70, 68, FX_EMBER_3),
        (48, 57, FX_EMBER_1), (73, 60, FX_EMBER_2), (61, 55, FX_EMBER_3)
    ]
    for ex, ey, ecol in embers:
        c.set(ex, ey, ecol)
        c.set(ex + 1, ey, FX_EMBER_1 if ecol == FX_EMBER_2 else ecol)

    wind_lines = [(54, 76, 7), (58, 70, 6), (61, 74, 8), (52, 82, 6), (64, 80, 6)]
    for wx, wy, wlen in wind_lines:
        for dx in range(wlen):
            if dx % 2 == 0:
                c.set(wx + dx, wy, SUN_WHITE if dx == wlen // 2 else SUN_GOLD)

    return c

c = render_masterpiece()
finish(c)
view(c)
print("Color count:", len(c.palette()))
