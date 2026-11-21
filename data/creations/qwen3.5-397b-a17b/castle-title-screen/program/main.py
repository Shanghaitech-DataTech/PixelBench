from pixelbench_api import *

# Create canvas for fantasy RPG title screen
c = new_canvas(128, 128, name="castle_title")

# Define color palette for sunset castle scene
# Sky colors (gradient from top to sunset)
c.color("#0a0a2e", "sky_top")        # Dark blue top
c.color("#1a1a4e", "sky_upper")       # Upper mid blue
c.color("#3a2a6e", "sky_mid")         # Middle purple
c.color("#5a3a7e", "sky_lower")       # Lower purple
c.color("#8a4a5e", "sunset_upper")    # Sunset orange-red
c.color("#ca6a3e", "sunset_mid")      # Main sunset orange
c.color("#ea8a2e", "sunset_lower")    # Bright sunset

# Sun colors
c.color("#ffaa00", "sun_outer")       # Sun outer glow
c.color("#ffcc00", "sun_mid")         # Sun middle
c.color("#ffee44", "sun_center")      # Sun center

# Cloud colors
c.color("#ffffff", "cloud_bright")    # Bright cloud
c.color("#e0e0e0", "cloud_mid")       # Mid cloud
c.color("#c0c0c0", "cloud_dark")      # Dark cloud shadow
c.color("#a0a0a0", "cloud_shadow")    # Cloud shadow

# Sea colors
c.color("#1a1a3e", "sea_dark")        # Deep sea
c.color("#2a2a5e", "sea_mid")         # Mid sea
c.color("#3a3a7e", "sea_light")       # Sea highlight

# Cliff and castle colors
c.color("#2a1a1a", "rock_dark")       # Dark rock
c.color("#3a2a2a", "rock_mid")        # Mid rock
c.color("#4a3a3a", "rock_light")      # Light rock
c.color("#1a0a0a", "castle_shadow")   # Castle shadow
c.color("#2a1a1a", "castle_mid")      # Castle mid
c.color("#3a2a2a", "castle_light")    # Castle highlight

# Tower and flag colors
c.color("#4a3a3a", "tower_stone")     # Tower stone
c.color("#6a5a4a", "tower_highlight") # Tower highlight
c.color("#8a2a2a", "flag_red")        # Red flag
c.color("#aa3a3a", "flag_bright")     # Bright flag

# Foreground rocks
c.color("#1a0a0a", "fg_rock_dark")    # Foreground dark
c.color("#2a1a0a", "fg_rock_mid")     # Foreground mid
c.color("#3a2a1a", "fg_rock_light")   # Foreground light

# Draw sky gradient (top to bottom)
for y in range(0, 128):
    if y < 20:
        sky_color = "sky_top"
    elif y < 35:
        sky_color = "sky_upper"
    elif y < 50:
        sky_color = "sky_mid"
    elif y < 65:
        sky_color = "sky_lower"
    elif y < 80:
        sky_color = "sunset_upper"
    elif y < 95:
        sky_color = "sunset_mid"
    else:
        sky_color = "sunset_lower"
    c.rect(0, y, 128, 1, sky_color)

# Draw large orange sun (centered horizontally, low on horizon)
sun_cx, sun_cy = 64, 85
sun_radius = 18
c.circle(sun_cx, sun_cy, sun_radius, "sun_center")
c.circle(sun_cx, sun_cy, sun_radius + 2, "sun_mid")
c.circle(sun_cx, sun_cy, sun_radius + 4, "sun_outer")

# Draw layered clouds (multiple layers at different heights)
# Upper clouds (small, wispy)
c.rect(10, 15, 20, 4, "cloud_dark")
c.rect(15, 12, 12, 3, "cloud_mid")
c.rect(90, 18, 25, 5, "cloud_dark")
c.rect(95, 14, 15, 4, "cloud_mid")
c.rect(45, 22, 18, 4, "cloud_dark")
c.rect(50, 19, 12, 3, "cloud_bright")

# Mid clouds (larger, fluffier)
c.rect(5, 35, 30, 6, "cloud_shadow")
c.rect(10, 32, 25, 5, "cloud_dark")
c.rect(15, 29, 20, 4, "cloud_mid")
c.rect(80, 38, 28, 6, "cloud_shadow")
c.rect(85, 34, 24, 5, "cloud_dark")
c.rect(90, 31, 18, 4, "cloud_mid")

# Lower clouds (near horizon)
c.rect(0, 55, 35, 7, "cloud_shadow")
c.rect(5, 52, 30, 6, "cloud_dark")
c.rect(100, 58, 28, 6, "cloud_shadow")
c.rect(105, 54, 22, 5, "cloud_dark")

# Draw sea (bottom portion, below horizon)
for y in range(95, 128):
    if y < 105:
        sea_color = "sea_light"
    elif y < 115:
        sea_color = "sea_mid"
    else:
        sea_color = "sea_dark"
    c.rect(0, y, 128, 1, sea_color)

# Add sea wave highlights
for x in range(0, 128, 8):
    c.rect(x, 96, 4, 1, "sea_light")
    c.rect(x + 4, 108, 3, 1, "sea_mid")

# Draw cliff (left side, castle sits on it)
# Main cliff body
c.poly([
    (0, 70), (25, 65), (35, 68), (40, 75), (45, 85), (50, 95),
    (50, 128), (0, 128)
], "rock_dark", fill=True)
c.poly([
    (5, 72), (25, 68), (33, 70), (38, 78), (43, 88), (45, 95),
    (45, 128), (5, 128)
], "rock_mid", fill=True)
c.poly([
    (10, 75), (25, 72), (30, 74), (35, 82), (38, 92),
    (38, 128), (10, 128)
], "rock_light", fill=True)

# Draw castle on cliff
# Main castle body (silhouette style with some detail)
castle_base_x = 20
castle_base_y = 45

# Left tower
c.rect(castle_base_x, castle_base_y, 12, 25, "castle_shadow")
c.rect(castle_base_x + 1, castle_base_y + 1, 10, 23, "castle_mid")
c.rect(castle_base_x + 2, castle_base_y + 2, 8, 20, "castle_light")
# Left tower top (crenellations)
c.rect(castle_base_x - 1, castle_base_y - 3, 3, 3, "castle_shadow")
c.rect(castle_base_x + 4, castle_base_y - 3, 3, 3, "castle_shadow")
c.rect(castle_base_x + 9, castle_base_y - 3, 3, 3, "castle_shadow")

# Right tower
tower2_x = 55
c.rect(tower2_x, castle_base_y - 5, 12, 30, "castle_shadow")
c.rect(tower2_x + 1, castle_base_y - 4, 10, 28, "castle_mid")
c.rect(tower2_x + 2, castle_base_y - 3, 8, 25, "castle_light")
# Right tower top (crenellations)
c.rect(tower2_x - 1, castle_base_y - 8, 3, 3, "castle_shadow")
c.rect(tower2_x + 4, castle_base_y - 8, 3, 3, "castle_shadow")
c.rect(tower2_x + 9, castle_base_y - 8, 3, 3, "castle_shadow")

# Castle wall connecting towers
c.rect(castle_base_x + 12, castle_base_y + 8, tower2_x - castle_base_x - 12, 17, "castle_shadow")
c.rect(castle_base_x + 13, castle_base_y + 9, tower2_x - castle_base_x - 14, 15, "castle_mid")

# Castle gate
c.rect(castle_base_x + 28, castle_base_y + 18, 8, 7, "castle_shadow")
c.rect(castle_base_x + 29, castle_base_y + 19, 6, 5, "castle_mid")

# Castle windows
c.rect(castle_base_x + 3, castle_base_y + 8, 2, 4, "castle_light")
c.rect(castle_base_x + 7, castle_base_y + 8, 2, 4, "castle_light")
c.rect(tower2_x + 3, castle_base_y + 3, 2, 4, "castle_light")
c.rect(tower2_x + 7, castle_base_y + 3, 2, 4, "castle_light")

# Draw flags on towers
# Left tower flag
flag1_x = castle_base_x + 6
flag1_y = castle_base_y - 8
c.line(flag1_x, flag1_y, flag1_x, flag1_y - 10, "tower_stone")  # Flag pole
c.poly([
    (flag1_x, flag1_y - 10),
    (flag1_x + 8, flag1_y - 7),
    (flag1_x + 8, flag1_y - 3),
    (flag1_x, flag1_y - 5)
], "flag_red", fill=True)
c.poly([
    (flag1_x, flag1_y - 10),
    (flag1_x + 6, flag1_y - 8),
    (flag1_x + 6, flag1_y - 5),
    (flag1_x, flag1_y - 6)
], "flag_bright", fill=True)

# Right tower flag
flag2_x = tower2_x + 6
flag2_y = castle_base_y - 13
c.line(flag2_x, flag2_y, flag2_x, flag2_y - 12, "tower_stone")  # Flag pole
c.poly([
    (flag2_x, flag2_y - 12),
    (flag2_x + 10, flag2_y - 8),
    (flag2_x + 10, flag2_y - 3),
    (flag2_x, flag2_y - 7)
], "flag_red", fill=True)
c.poly([
    (flag2_x, flag2_y - 12),
    (flag2_x + 7, flag2_y - 9),
    (flag2_x + 7, flag2_y - 5),
    (flag2_x, flag2_y - 8)
], "flag_bright", fill=True)

# Draw foreground dark rocks (bottom of screen)
# Large foreground rock formation
c.poly([
    (0, 100), (15, 95), (30, 98), (45, 92), (60, 96), (75, 90),
    (90, 94), (105, 88), (120, 92), (128, 90), (128, 128), (0, 128)
], "fg_rock_dark", fill=True)

c.poly([
    (5, 102), (15, 98), (28, 100), (42, 95), (58, 98), (72, 93),
    (88, 96), (102, 91), (118, 94), (125, 93), (125, 128), (5, 128)
], "fg_rock_mid", fill=True)

c.poly([
    (10, 105), (20, 102), (35, 104), (50, 100), (65, 103), (80, 98),
    (95, 101), (110, 97), (120, 100), (120, 128), (10, 128)
], "fg_rock_light", fill=True)

# Add some rock texture/detail
c.rect(20, 110, 8, 3, "fg_rock_dark")
c.rect(55, 105, 6, 2, "fg_rock_dark")
c.rect(85, 108, 7, 3, "fg_rock_dark")
c.rect(105, 102, 5, 2, "fg_rock_dark")

# Add some additional atmospheric details
# Sun rays/glow effect (subtle)
for i in range(-3, 4):
    c.line(sun_cx + i * 5, sun_cy - 25, sun_cx + i * 8, sun_cy - 35, "sun_outer")

# Birds in distance (small silhouettes)
c.set(30, 40, "castle_shadow")
c.set(31, 39, "castle_shadow")
c.set(32, 40, "castle_shadow")
c.set(35, 42, "castle_shadow")
c.set(36, 41, "castle_shadow")
c.set(37, 42, "castle_shadow")

# Check color count
stats = c.stats()
print(f"Colors used: {stats['colors_used']}")
print(f"Visible pixels: {stats['visible_pixels']}")
print(c.stats_text())

# Submit the result
finish(c)
