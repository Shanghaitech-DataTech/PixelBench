from pixelbench_api import new_canvas, finish
import random

# Create the canvas
c = new_canvas(256, 256)

# Define the color palette
# Sky colors (sunset)
c.color("#0a0015", "sky_dark")        # 0 - dark purple/black
c.color("#1a0030", "sky_deep")        # 1 - deep purple
c.color("#300050", "sky_purple")      # 2 - purple
c.color("#501060", "sky_magenta")     # 3 - magenta purple
c.color("#702050", "sky_rose")        # 4 - rose
c.color("#903040", "sky_orange")      # 5 - orange-red
c.color("#b04030", "sky_bright")      # 6 - bright orange
c.color("#d05020", "sky_sun")         # 7 - sun orange
c.color("#f06010", "sky_glow")        # 8 - sun glow

# Mountain colors
c.color("#0d0d15", "mountain_dark")   # 9 - darkest mountain
c.color("#151525", "mountain_mid")    # 10 - mid mountain
c.color("#202035", "mountain_light")  # 11 - light mountain
c.color("#303045", "mountain_far")    # 12 - far mountain

# Castle colors (stone)
c.color("#252530", "stone_dark")      # 13 - dark stone
c.color("#353545", "stone_mid")       # 14 - mid stone
c.color("#454555", "stone_light")     # 15 - light stone
c.color("#555565", "stone_highlight") # 16 - stone highlight

# Fire colors
c.color("#301000", "fire_dark")       # 17 - dark fire base
c.color("#602000", "fire_mid")        # 18 - mid fire
c.color("#903000", "fire_bright")     # 19 - bright fire
c.color("#c04000", "fire_orange")     # 20 - fire orange
c.color("#f05000", "fire_yellow")     # 21 - fire yellow
c.color("#ff6000", "fire_white")      # 22 - fire white hot

# Smoke colors
c.color("#151515", "smoke_dark")      # 23 - dark smoke
c.color("#252525", "smoke_mid")       # 24 - mid smoke
c.color("#353535", "smoke_light")     # 25 - light smoke
c.color("#454545", "smoke_pale")      # 26 - pale smoke

# Dragon colors
c.color("#0a0a0a", "dragon_dark")     # 27 - dragon dark
c.color("#151520", "dragon_body")     # 28 - dragon body
c.color("#252535", "dragon_light")    # 29 - dragon light
c.color("#353545", "dragon_highlight")# 30 - dragon highlight
c.color("#401010", "dragon_wing")     # 31 - dragon wing membrane
c.color("#602020", "dragon_wing_light")# 32 - wing light
c.color("#803000", "dragon_fire")     # 33 - dragon breath fire
c.color("#a04000", "dragon_fire_bright")# 34 - dragon fire bright
c.color("#ffff00", "dragon_eye")      # 35 - dragon eye

# Knight colors
c.color("#202025", "armor_dark")      # 36 - dark armor
c.color("#404050", "armor_mid")       # 37 - mid armor
c.color("#606070", "armor_light")     # 38 - light armor
c.color("#808090", "armor_highlight") # 39 - armor highlight
c.color("#801010", "cloak_red")       # 40 - red cloak
c.color("#600000", "cloak_dark")      # 41 - dark cloak
c.color("#c0c030", "gold_trim")       # 42 - gold trim

# Shield colors
c.color("#302010", "shield_dark")     # 43 - shield dark
c.color("#503020", "shield_mid")      # 44 - shield mid
c.color("#704030", "shield_light")    # 45 - shield light
c.color("#404080", "shield_blue")     # 46 - blue shield
c.color("#6060a0", "shield_blue_light")# 47 - light blue shield

# Spear colors
c.color("#504030", "spear_wood")      # 48 - wood shaft
c.color("#706050", "spear_wood_light")# 49 - light wood
c.color("#808080", "spear_metal")     # 50 - metal tip
c.color("#a0a0a0", "spear_metal_light")# 51 - metal highlight

# Soldier colors (enemy)
c.color("#1a1a1a", "enemy_dark")      # 52 - enemy dark
c.color("#303030", "enemy_mid")       # 53 - enemy mid
c.color("#404040", "enemy_light")     # 54 - enemy light
c.color("#504030", "enemy_leather")   # 55 - leather armor
c.color("#705040", "enemy_leather_light")# 56 - light leather

# Siege tower colors
c.color("#2a1a10", "tower_dark")      # 57 - tower dark wood
c.color("#402515", "tower_mid")       # 58 - tower mid wood
c.color("#553020", "tower_light")     # 59 - tower light wood
c.color("#302010", "tower_shadow")    # 60 - tower shadow

# Ground colors
c.color("#0f0f0f", "ground_dark")     # 61 - dark ground
c.color("#1a1510", "ground_mid")      # 62 - mid ground
c.color("#252015", "ground_light")    # 63 - light ground
c.color("#302520", "ground_highlight")# 64 - ground highlight

# Ember colors
c.color("#ff4000", "ember_bright")    # 65 - bright ember
c.color("#ff2000", "ember_mid")       # 66 - mid ember
c.color("#801000", "ember_dark")      # 67 - dark ember

# Arrow colors
c.color("#403020", "arrow_wood")      # 68 - arrow wood
c.color("#605040", "arrow_wood_light")# 69 - arrow light
c.color("#707070", "arrow_metal")     # 70 - arrow metal

# Outline color
c.color("#000000", "outline")         # 71 - black outline

# Additional colors for detail
c.color("#201030", "shadow_purple")   # 72
c.color("#151020", "shadow_deep")     # 73
c.color("#3a2a20", "earth_brown")     # 74
c.color("#504035", "earth_light")     # 75
c.color("#101018", "night_sky")       # 76
c.color("#050508", "void")            # 77
c.color("#ff8040", "flame_tip")       # 78
c.color("#ffaa60", "flame_core")      # 79
c.color("#2a2a3a", "stone_edge")      # 80
c.color("#1a1a25", "castle_shadow")   # 81
c.color("#4a3a30", "wood_dark")       # 82
c.color("#6a5a45", "wood_mid")        # 83
c.color("#8a7a5a", "wood_light")      # 84
c.color("#3a3a4a", "metal_dark")      # 85
c.color("#5a5a6a", "metal_mid")       # 86
c.color("#7a7a8a", "metal_light")     # 87
c.color("#9a9aaa", "metal_bright")    # 88
c.color("#503030", "blood_dark")      # 89
c.color("#704040", "blood_mid")       # 90
c.color("#303035", "rock_dark")       # 91
c.color("#404045", "rock_mid")        # 92
c.color("#505055", "rock_light")      # 93
c.color("#202028", "dark_detail")     # 94
c.color("#282830", "mid_detail")      # 95
c.color("#383840", "light_detail")    # 96
c.color("#605050", "dust")            # 97
c.color("#806040", "dust_light")      # 98
c.color("#403025", "dirt")            # 99
c.color("#504035", "dirt_light")      # 100
c.color("#302520", "shadow_brown")    # 101
c.color("#4a3a35", "highlight_brown") # 102
c.color("#ff5020", "spark_bright")    # 103
c.color("#cc4010", "spark_mid")       # 104
c.color("#15151a", "bg_dark")         # 105
c.color("#252025", "bg_mid")          # 106
c.color("#353035", "bg_light")        # 107
c.color("#453540", "accent_dark")     # 108
c.color("#554550", "accent_mid")      # 109
c.color("#655560", "accent_light")    # 110
c.color("#302020", "dark_red")        # 111
c.color("#503025", "rust")            # 112
c.color("#704030", "rust_light")      # 113
c.color("#181820", "deep_shadow")     # 114
c.color("#282830", "mid_shadow")      # 115
c.color("#383840", "light_shadow")    # 116
c.color("#484850", "highlight_shadow")# 117
c.color("#201510", "ground_shadow")   # 118
c.color("#352520", "ground_mid2")     # 119
c.color("#4a3530", "ground_light2")   # 120
c.color("#5f4540", "ground_highlight2")# 121
c.color("#101015", "sky_bottom")      # 122
c.color("#251520", "sky_lower")       # 123
c.color("#402030", "sky_middle")      # 124
c.color("#603040", "sky_upper")       # 125
c.color("#804045", "sky_top")         # 126
c.color("#a05050", "sky_horizon")     # 127
c.color("#1a1a1f", "outline_soft")    # 128
c.color("#2a2a2f", "outline_mid")     # 129
c.color("#0f0f12", "void_soft")       # 130
c.color("#3a3a40", "gray_mid")        # 131
c.color("#5a5a60", "gray_light")      # 132
c.color("#7a7a80", "gray_bright")     # 133
c.color("#4a3a40", "brown_mid")       # 134
c.color("#6a5a50", "brown_light")     # 135
c.color("#8a7a60", "brown_bright")    # 136
c.color("#ff7030", "fire_glow")       # 137
c.color("#ff9050", "fire_bright2")    # 138
c.color("#ffb070", "fire_core2")      # 139

# === BACKGROUND: Dramatic sunset sky ===
for y in range(256):
    if y < 40:
        color_idx = 0
    elif y < 70:
        color_idx = 1
    elif y < 100:
        color_idx = 2
    elif y < 130:
        color_idx = 3
    elif y < 150:
        color_idx = 4
    elif y < 170:
        color_idx = 5
    elif y < 190:
        color_idx = 6
    elif y < 210:
        color_idx = 7
    else:
        color_idx = 8
    
    for x in range(256):
        c.set(x, y, color_idx)

# Add sun glow effect
for y in range(180, 230):
    for x in range(80, 180):
        dist = ((x - 130)*(x - 130) + (y - 200)*(y - 200)) ** 0.5
        if dist < 50:
            c.set(x, y, 8)
        elif dist < 70:
            c.set(x, y, 7)
        elif dist < 90:
            c.set(x, y, 6)

# === DISTANT MOUNTAINS ===
mountain1_points = [(0, 160), (30, 140), (60, 155), (90, 130), (120, 150), (150, 125), 
                    (180, 145), (210, 135), (240, 150), (256, 140), (256, 180), (0, 180)]
c.poly(mountain1_points, 9, fill=True)

mountain2_points = [(0, 175), (40, 155), (80, 170), (120, 145), (160, 165), (200, 150), 
                    (240, 165), (256, 155), (256, 200), (0, 200)]
c.poly(mountain2_points, 10, fill=True)

mountain3_points = [(0, 190), (50, 170), (100, 185), (140, 160), (180, 180), (220, 165), 
                    (256, 180), (256, 220), (0, 220)]
c.poly(mountain3_points, 11, fill=True)

# === GROUND ===
for y in range(200, 256):
    for x in range(256):
        if y < 210:
            c.set(x, y, 61)
        elif y < 225:
            c.set(x, y, 62)
        elif y < 240:
            c.set(x, y, 63)
        else:
            c.set(x, y, 64)

# === CASTLE ===
c.rect(70, 130, 120, 80, 13, fill=True)
c.rect(75, 135, 110, 70, 14, fill=True)

c.rect(60, 100, 30, 110, 13, fill=True)
c.rect(63, 103, 24, 104, 14, fill=True)
c.rect(55, 95, 40, 10, 15, fill=True)
c.rect(58, 90, 34, 5, 16, fill=True)

c.rect(170, 100, 30, 110, 13, fill=True)
c.rect(173, 103, 24, 104, 14, fill=True)
c.rect(165, 95, 40, 10, 15, fill=True)
c.rect(168, 90, 34, 5, 16, fill=True)

c.rect(105, 60, 45, 150, 13, fill=True)
c.rect(110, 65, 35, 140, 14, fill=True)
c.rect(100, 50, 55, 15, 15, fill=True)
c.rect(103, 45, 49, 8, 16, fill=True)

c.rect(115, 180, 30, 30, 81, fill=True)
c.rect(118, 183, 24, 24, 13, fill=True)

for i in range(7):
    c.rect(75 + i*15, 128, 10, 7, 15, fill=True)
for i in range(2):
    c.rect(63 + i*20, 98, 10, 7, 15, fill=True)
for i in range(2):
    c.rect(173 + i*20, 98, 10, 7, 15, fill=True)
for i in range(3):
    c.rect(103 + i*16, 48, 10, 7, 15, fill=True)

c.rect(118, 80, 8, 12, 77, fill=True)
c.rect(134, 80, 8, 12, 77, fill=True)
c.rect(118, 110, 8, 12, 77, fill=True)
c.rect(134, 110, 8, 12, 77, fill=True)
c.rect(70, 120, 6, 10, 77, fill=True)
c.rect(184, 120, 6, 10, 77, fill=True)

# === FIRE on castle ===
for i in range(5):
    fx = 65 + i*4
    fy = 85 - i*3
    c.set(fx, fy, 22)
    c.set(fx-1, fy+1, 21)
    c.set(fx+1, fy+1, 21)
    c.set(fx, fy+2, 20)
    c.set(fx-1, fy+2, 19)
    c.set(fx+1, fy+2, 19)
    c.set(fx, fy+3, 18)
    c.set(fx-1, fy+3, 17)
    c.set(fx+1, fy+3, 17)

for i in range(5):
    fx = 175 + i*4
    fy = 85 - i*3
    c.set(fx, fy, 22)
    c.set(fx-1, fy+1, 21)
    c.set(fx+1, fy+1, 21)
    c.set(fx, fy+2, 20)
    c.set(fx-1, fy+2, 19)
    c.set(fx+1, fy+2, 19)
    c.set(fx, fy+3, 18)
    c.set(fx-1, fy+3, 17)
    c.set(fx+1, fy+3, 17)

for i in range(8):
    fx = 115 + i*3
    fy = 40 - i*4
    c.set(fx, fy, 22)
    c.set(fx-1, fy+1, 21)
    c.set(fx+1, fy+1, 21)
    c.set(fx, fy+2, 20)
    c.set(fx-1, fy+2, 19)
    c.set(fx+1, fy+2, 19)
    c.set(fx-2, fy+2, 18)
    c.set(fx+2, fy+2, 18)
    c.set(fx, fy+3, 17)
    c.set(fx-1, fy+3, 17)
    c.set(fx+1, fy+3, 17)

for i in range(4):
    fx = 90 + i*15
    fy = 125
    c.set(fx, fy, 21)
    c.set(fx-1, fy+1, 20)
    c.set(fx+1, fy+1, 20)
    c.set(fx, fy+2, 19)
    c.set(fx-1, fy+2, 18)
    c.set(fx+1, fy+2, 18)

# === SMOKE ===
smoke_positions = [
    (70, 80), (90, 75), (115, 50), (140, 75), (170, 80),
    (80, 60), (100, 55), (120, 35), (145, 55), (165, 60)
]
for sx, sy in smoke_positions:
    for i in range(15):
        offset_x = (i * 3) % 20 - 10
        offset_y = -i * 4
        smoke_x = sx + offset_x + (i % 3) * 5
        smoke_y = sy + offset_y
        if smoke_y > 10:
            if i < 5:
                c.set(smoke_x, smoke_y, 23)
            elif i < 10:
                c.set(smoke_x, smoke_y, 24)
            else:
                c.set(smoke_x, smoke_y, 25)

for cloud_x in range(60, 200, 30):
    for cy in range(30, 80, 15):
        c.circle(cloud_x + (cy % 20), cy, 8 + (cy % 10), 24, fill=True)
        c.circle(cloud_x + (cy % 20) + 5, cy - 5, 6 + (cy % 8), 25, fill=True)

# === DRAGON ===
dragon_body_x = 128
dragon_body_y = 35

c.ellipse(dragon_body_x, dragon_body_y, 25, 12, 28, fill=True)
c.ellipse(dragon_body_x + 5, dragon_body_y - 2, 22, 10, 29, fill=True)

neck_points = [(dragon_body_x - 20, dragon_body_y - 5), 
               (dragon_body_x - 35, dragon_body_y - 15),
               (dragon_body_x - 45, dragon_body_y - 25),
               (dragon_body_x - 50, dragon_body_y - 35)]
c.path("M {} {} L {} {} L {} {} L {} {}".format(neck_points[0][0], neck_points[0][1], neck_points[1][0], neck_points[1][1], neck_points[2][0], neck_points[2][1], neck_points[3][0], neck_points[3][1]), 28, fill=True)

head_x = dragon_body_x - 55
head_y = dragon_body_y - 40
c.ellipse(head_x, head_y, 12, 10, 28, fill=True)
c.ellipse(head_x - 3, head_y - 2, 10, 8, 29, fill=True)

c.poly([(head_x - 10, head_y), (head_x - 18, head_y - 3), 
        (head_x - 18, head_y + 3), (head_x - 10, head_y)], 28, fill=True)

c.set(head_x - 8, head_y - 3, 35)
c.set(head_x - 9, head_y - 3, 35)
c.set(head_x - 8, head_y - 2, 35)

horn1_points = [(head_x - 5, head_y - 8), (head_x - 10, head_y - 20), 
                (head_x - 15, head_y - 25), (head_x - 12, head_y - 15)]
c.poly(horn1_points, 27, fill=True)
horn2_points = [(head_x, head_y - 8), (head_x - 3, head_y - 18), 
                (head_x - 6, head_y - 22), (head_x - 4, head_y - 14)]
c.poly(horn2_points, 27, fill=True)

jaw_points = [(head_x - 10, head_y + 5), (head_x - 20, head_y + 8),
              (head_x - 25, head_y + 12), (head_x - 15, head_y + 10),
              (head_x - 8, head_y + 8)]
c.poly(jaw_points, 27, fill=True)

for i in range(20):
    fx = head_x - 25 - i * 3
    fy = head_y + 10 + (i % 5) - 2
    if i < 5:
        c.set(fx, fy, 34)
        c.set(fx, fy+1, 34)
        c.set(fx, fy-1, 33)
    elif i < 10:
        c.set(fx, fy, 33)
        c.set(fx, fy+1, 33)
        c.set(fx, fy-1, 21)
    elif i < 15:
        c.set(fx, fy, 21)
        c.set(fx, fy+1, 20)
        c.set(fx, fy-1, 19)
    else:
        c.set(fx, fy, 19)
        c.set(fx, fy+1, 18)

wing_left_base_x = dragon_body_x - 10
wing_left_base_y = dragon_body_y - 8
wing_left_points = [
    (wing_left_base_x, wing_left_base_y),
    (wing_left_base_x - 30, wing_left_base_y - 40),
    (wing_left_base_x - 60, wing_left_base_y - 30),
    (wing_left_base_x - 80, wing_left_base_y - 10),
    (wing_left_base_x - 70, wing_left_base_y + 10),
    (wing_left_base_x - 40, wing_left_base_y + 5),
    (wing_left_base_x - 10, wing_left_base_y + 10)
]
c.poly(wing_left_points, 31, fill=True)

c.line(wing_left_base_x, wing_left_base_y, wing_left_base_x - 30, wing_left_base_y - 40, 27)
c.line(wing_left_base_x - 30, wing_left_base_y - 40, wing_left_base_x - 60, wing_left_base_y - 30, 27)
c.line(wing_left_base_x - 60, wing_left_base_y - 30, wing_left_base_x - 80, wing_left_base_y - 10, 27)
c.line(wing_left_base_x - 30, wing_left_base_y - 40, wing_left_base_x - 40, wing_left_base_y + 5, 27)

wing_right_base_x = dragon_body_x + 15
wing_right_base_y = dragon_body_y - 5
wing_right_points = [
    (wing_right_base_x, wing_right_base_y),
    (wing_right_base_x + 25, wing_right_base_y - 35),
    (wing_right_base_x + 50, wing_right_base_y - 25),
    (wing_right_base_x + 65, wing_right_base_y - 5),
    (wing_right_base_x + 55, wing_right_base_y + 10),
    (wing_right_base_x + 30, wing_right_base_y + 5),
    (wing_right_base_x, wing_right_base_y + 8)
]
c.poly(wing_right_points, 31, fill=True)
c.line(wing_right_base_x, wing_right_base_y, wing_right_base_x + 25, wing_right_base_y - 35, 27)
c.line(wing_right_base_x + 25, wing_right_base_y - 35, wing_right_base_x + 50, wing_right_base_y - 25, 27)

tail_points = [
    (dragon_body_x + 25, dragon_body_y),
    (dragon_body_x + 45, dragon_body_y + 5),
    (dragon_body_x + 65, dragon_body_y + 3),
    (dragon_body_x + 85, dragon_body_y - 5),
    (dragon_body_x + 100, dragon_body_y - 15),
    (dragon_body_x + 110, dragon_body_y - 25)
]
c.path("M {} {} L {} {} L {} {} L {} {} L {} {} L {} {}".format(tail_points[0][0], tail_points[0][1], tail_points[1][0], tail_points[1][1], tail_points[2][0], tail_points[2][1], tail_points[3][0], tail_points[3][1], tail_points[4][0], tail_points[4][1], tail_points[5][0], tail_points[5][1]), 28, fill=True)
c.poly([(dragon_body_x + 108, dragon_body_y - 28), 
        (dragon_body_x + 115, dragon_body_y - 32),
        (dragon_body_x + 112, dragon_body_y - 22)], 27, fill=True)

c.line(dragon_body_x - 5, dragon_body_y + 8, dragon_body_x - 10, dragon_body_y + 20, 27)
c.line(dragon_body_x + 5, dragon_body_y + 8, dragon_body_x + 8, dragon_body_y + 18, 27)

# === KNIGHTS ON RAMPARTS ===
knight_positions = [
    (85, 125), (100, 125), (130, 125), (145, 125), (160, 125),
    (72, 95), (82, 95), (178, 95), (188, 95),
    (115, 45), (135, 45)
]

for kx, ky in knight_positions:
    c.rect(kx - 3, ky - 8, 6, 12, 37, fill=True)
    c.rect(kx - 2, ky - 7, 4, 10, 38, fill=True)
    c.set(kx, ky - 12, 39)
    c.set(kx - 1, ky - 11, 38)
    c.set(kx + 1, ky - 11, 38)
    c.set(kx, ky - 11, 39)
    c.set(kx, ky - 14, 40)
    c.set(kx, ky - 15, 40)
    c.rect(kx - 6, ky - 5, 4, 7, 46, fill=True)
    c.rect(kx - 5, ky - 4, 2, 5, 47, fill=True)
    c.line(kx + 3, ky - 6, kx + 8, ky - 15, 48)
    c.set(kx + 8, ky - 15, 50)
    c.set(kx + 9, ky - 16, 51)

# === SOLDIERS IN FORMATION ===
for row in range(3):
    for col in range(8):
        sx = 30 + col * 25
        sy = 215 + row * 12
        c.rect(sx - 3, sy - 8, 6, 10, 53, fill=True)
        c.rect(sx - 2, sy - 7, 4, 8, 54, fill=True)
        c.set(sx, sy - 11, 54)
        c.set(sx - 1, sy - 10, 53)
        c.set(sx + 1, sy - 10, 53)
        c.line(sx + 3, sy - 5, sx + 6, sy - 12, 48)
        c.set(sx + 6, sy - 12, 50)
        c.rect(sx - 6, sy - 4, 3, 6, 55, fill=True)

# === SIEGE TOWERS ===
tower1_x = 40
tower1_y = 150
c.rect(tower1_x - 15, tower1_y - 50, 30, 60, 57, fill=True)
c.rect(tower1_x - 12, tower1_y - 47, 24, 54, 58, fill=True)
c.rect(tower1_x - 15, tower1_y - 30, 30, 3, 60, fill=True)
c.rect(tower1_x - 15, tower1_y - 15, 30, 3, 60, fill=True)
c.circle(tower1_x - 10, tower1_y + 10, 5, 57, fill=True)
c.circle(tower1_x + 10, tower1_y + 10, 5, 57, fill=True)
c.rect(tower1_x + 15, tower1_y - 40, 20, 5, 82, fill=True)

tower2_x = 210
tower2_y = 155
c.rect(tower2_x - 15, tower2_y - 50, 30, 60, 57, fill=True)
c.rect(tower2_x - 12, tower2_y - 47, 24, 54, 58, fill=True)
c.rect(tower2_x - 15, tower2_y - 30, 30, 3, 60, fill=True)
c.rect(tower2_x - 15, tower2_y - 15, 30, 3, 60, fill=True)
c.circle(tower2_x - 10, tower2_y + 10, 5, 57, fill=True)
c.circle(tower2_x + 10, tower2_y + 10, 5, 57, fill=True)
c.rect(tower2_x - 35, tower2_y - 35, 20, 5, 82, fill=True)

# === ARROWS FLYING ===
arrow_paths = [
    [(30, 200), (60, 180), (90, 160)],
    [(220, 200), (190, 180), (160, 160)],
    [(50, 190), (80, 175), (110, 160)],
    [(200, 190), (170, 175), (140, 160)],
    [(100, 195), (115, 180), (130, 165)],
    [(40, 170), (70, 155), (100, 140)],
    [(210, 170), (180, 155), (150, 140)],
]

for path in arrow_paths:
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i + 1]
        c.line(x0, y0, x1, y1, 68)
    ax, ay = path[-1]
    c.set(ax, ay, 70)
    c.set(ax - 1, ay, 69)
    c.set(ax + 1, ay, 69)
    fx, fy = path[0]
    c.set(fx, fy, 69)
    c.set(fx - 1, fy - 1, 68)
    c.set(fx - 1, fy + 1, 68)

# === EMBERS ===
random.seed(42)
for _ in range(80):
    ex = random.randint(60, 200)
    ey = random.randint(50, 180)
    ember_type = random.choice([65, 66, 67, 103, 104])
    c.set(ex, ey, ember_type)
    if random.random() < 0.3:
        c.set(ex + 1, ey, ember_type)

# === DARK OUTLINE ===
castle_outline = [
    (55, 95), (100, 95), (100, 50), (155, 50), (155, 95), (200, 95),
    (200, 210), (170, 210), (170, 100), (140, 100), (140, 65), (120, 65),
    (120, 100), (90, 100), (90, 210), (60, 210), (60, 100), (55, 100)
]
for i in range(len(castle_outline) - 1):
    x0, y0 = castle_outline[i]
    x1, y1 = castle_outline[i + 1]
    c.line(x0, y0, x1, y1, 128)

dragon_outline_points = [
    (head_x - 18, head_y), (head_x - 10, head_y - 10),
    (head_x, head_y - 12), (head_x + 10, head_y - 10),
    (head_x + 20, head_y - 5), (dragon_body_x + 30, dragon_body_y),
    (dragon_body_x + 50, dragon_body_y + 5), (dragon_body_x + 80, dragon_body_y),
    (dragon_body_x + 100, dragon_body_y - 10), (dragon_body_x + 112, dragon_body_y - 25),
    (dragon_body_x + 105, dragon_body_y - 20), (dragon_body_x + 85, dragon_body_y - 5),
    (dragon_body_x + 60, dragon_body_y + 5), (dragon_body_x + 30, dragon_body_y + 10),
    (dragon_body_x - 10, dragon_body_y + 10), (dragon_body_x - 40, dragon_body_y + 5),
    (dragon_body_x - 70, dragon_body_y + 10), (dragon_body_x - 80, dragon_body_y - 10),
    (dragon_body_x - 60, dragon_body_y - 30), (dragon_body_x - 30, dragon_body_y - 40),
    (dragon_body_x - 10, dragon_body_y - 10), (dragon_body_x - 50, dragon_body_y - 35),
    (head_x - 15, head_y - 25), (head_x - 18, head_y)
]
for i in range(len(dragon_outline_points) - 1):
    x0, y0 = dragon_outline_points[i]
    x1, y1 = dragon_outline_points[i + 1]
    c.line(x0, y0, x1, y1, 128)

c.line(0, 200, 256, 200, 128)
c.line(0, 200, 0, 256, 128)
c.line(256, 200, 256, 256, 128)

# === FINAL DETAILS ===
for i in range(10):
    px = 80 + i * 12
    py = 60 - i * 3
    c.circle(px, py, 5 + i % 3, 25, fill=True)

for fy in range(40, 100, 8):
    for fx in range(70, 190, 15):
        c.set(fx + random.randint(-2, 2), fy, 103)
        c.set(fx + random.randint(-1, 1), fy + 1, 104)

for kx, ky in knight_positions[:5]:
    c.set(kx, ky - 5, 39)
    c.set(kx - 1, ky - 4, 39)

c.rect(128, 25, 3, 20, 40, fill=True)
flag_points = [(131, 25), (145, 30), (145, 40), (131, 35)]
c.poly(flag_points, 40, fill=True)

for dx in range(0, 256, 40):
    c.circle(dx + 20, 205, 8, 97, fill=True)
    c.circle(dx + 35, 208, 6, 98, fill=True)

print(c.stats_text())

finish(c)
