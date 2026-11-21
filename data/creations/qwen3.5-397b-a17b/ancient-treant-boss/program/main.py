from pixelbench_api import *

# Create main canvas
c = new_canvas(256, 256, name="treant_boss")

# Define color palette
# Background colors
sky_dark = c.color("#1a1f2e", "sky_dark")
sky_mid = c.color("#2d3548", "sky_mid")
sky_light = c.color("#3d4a5f", "sky_light")
god_ray = c.color("#6b7a4f", "god_ray")
god_ray_light = c.color("#8a9f6a", "god_ray_light")

# Ground colors
ground_dark = c.color("#1a1410", "ground_dark")
ground_mid = c.color("#2d2218", "ground_mid")
ground_light = c.color("#3d2f22", "ground_light")
grass_dark = c.color("#1f2a1a", "grass_dark")
grass_mid = c.color("#2f3f2a", "grass_mid")
grass_light = c.color("#3f5f3a", "grass_light")

# Tree bark colors
bark_shadow = c.color("#1a1208", "bark_shadow")
bark_dark = c.color("#2d1f10", "bark_dark")
bark_mid = c.color("#3f2f18", "bark_mid")
bark_light = c.color("#5a4428", "bark_light")
bark_highlight = c.color("#7a5f38", "bark_highlight")

# Moss colors
moss_dark = c.color("#1f3a1f", "moss_dark")
moss_mid = c.color("#2f5a2f", "moss_mid")
moss_light = c.color("#3f7a3f", "moss_light")
moss_bright = c.color("#4f9a4f", "moss_bright")

# Vine colors
vine_dark = c.color("#2a3a2a", "vine_dark")
vine_mid = c.color("#3a5a3a", "vine_mid")
vine_light = c.color("#4a7a4a", "vine_light")

# Eye colors (glowing green)
eye_glow = c.color("#00ff00", "eye_glow")
eye_core = c.color("#80ff80", "eye_core")
eye_white = c.color("#ffffff", "eye_white")

# Outline color
outline = c.color("#0a0a0a", "outline")

# Background - sky gradient
for y in range(0, 120):
    ratio = y / 120
    if ratio < 0.33:
        c.rect(0, y, 256, 1, sky_dark)
    elif ratio < 0.66:
        c.rect(0, y, 256, 1, sky_mid)
    else:
        c.rect(0, y, 256, 1, sky_light)

# God rays from top center
for i in range(-8, 9):
    angle = i * 3
    # Draw rays as tapered lines
    ray_width = max(8, 20 - abs(i) * 2)
    for y in range(0, 140):
        x_offset = int(i * y * 0.8 / 140)
        x_start = 128 + x_offset - ray_width // 2
        x_end = 128 + x_offset + ray_width // 2
        if y < 50:
            c.rect(max(0, x_start), y, min(256, x_end - x_start), 1, god_ray)
        elif y < 100:
            c.rect(max(0, x_start), y, min(256, x_end - x_start), 1, god_ray_light)

# Ground - curved horizon
for x in range(256):
    ground_y = 180 + int(10 * ((x - 128) / 128) ** 2)
    for y in range(ground_y, 256):
        if y < ground_y + 15:
            c.set(x, y, ground_dark)
        elif y < ground_y + 30:
            c.set(x, y, ground_mid)
        else:
            c.set(x, y, ground_light)

# Grass patches
for i in range(50):
    gx = 20 + (i * 47) % 220
    gy = 175 + (i * 23) % 20
    for j in range(5):
        c.set(gx + j - 2, gy - j, grass_dark)
        c.set(gx + j - 2, gy - j - 1, grass_mid)

# Main treant body - trunk (centered, towering)
# Main trunk from y=80 to y=230
trunk_center = 128
trunk_width_base = 70
trunk_width_top = 40

# Draw trunk shape with bark texture
for y in range(80, 230):
    progress = (y - 80) / 150
    width = int(trunk_width_base - (trunk_width_base - trunk_width_top) * progress)
    # Add some organic variation
    variation = int(5 * ((y * 0.1) % 3 - 1.5))
    width += variation
    
    for x in range(trunk_center - width, trunk_center + width + 1):
        # Bark texture based on position
        noise = ((x * 7 + y * 13) % 5) / 5
        if noise < 0.2:
            c.set(x, y, bark_shadow)
        elif noise < 0.4:
            c.set(x, y, bark_dark)
        elif noise < 0.6:
            c.set(x, y, bark_mid)
        elif noise < 0.8:
            c.set(x, y, bark_light)
        else:
            c.set(x, y, bark_highlight)

# Bark grooves (vertical lines)
for groove_x in [108, 118, 138, 148]:
    for y in range(90, 220):
        if (y + groove_x) % 3 == 0:
            c.set(groove_x, y, bark_shadow)

# Head area (top of trunk, y=60-90)
for y in range(60, 90):
    width = int(35 + 15 * ((90 - y) / 30))
    for x in range(trunk_center - width, trunk_center + width + 1):
        noise = ((x * 7 + y * 13) % 5) / 5
        if noise < 0.3:
            c.set(x, y, bark_dark)
        elif noise < 0.6:
            c.set(x, y, bark_mid)
        else:
            c.set(x, y, bark_light)

# Glowing green eyes
# Left eye
eye_y = 75
left_eye_x = 115
right_eye_x = 141

# Eye glow area
for dx in range(-6, 7):
    for dy in range(-4, 5):
        dist = (dx**2 + dy**2) ** 0.5
        if dist < 5:
            if dist < 2:
                c.set(left_eye_x + dx, eye_y + dy, eye_core)
            elif dist < 4:
                c.set(left_eye_x + dx, eye_y + dy, eye_glow)

# Right eye
for dx in range(-6, 7):
    for dy in range(-4, 5):
        dist = (dx**2 + dy**2) ** 0.5
        if dist < 5:
            if dist < 2:
                c.set(right_eye_x + dx, eye_y + dy, eye_core)
            elif dist < 4:
                c.set(right_eye_x + dx, eye_y + dy, eye_glow)

# Eye highlights
c.set(left_eye_x - 1, eye_y - 1, eye_white)
c.set(right_eye_x - 1, eye_y - 1, eye_white)

# Angry brow ridges
for i in range(-8, 9):
    c.set(left_eye_x + i, eye_y - 6 - abs(i) // 2, bark_shadow)
    c.set(right_eye_x + i, eye_y - 6 - abs(i) // 2, bark_shadow)

# Branch arms
# Left arm (extends from trunk left side around y=120)
left_arm_start = (90, 120)
# Draw left arm going up and out
arm_points_left = [
    (90, 120), (70, 110), (50, 100), (30, 95), (15, 100), (10, 110)
]
for i in range(len(arm_points_left) - 1):
    x0, y0 = arm_points_left[i]
    x1, y1 = arm_points_left[i + 1]
    c.line(x0, y0, x1, y1, bark_mid)
    # Arm thickness
    for t in range(-4, 5):
        c.set(x0 + t, y0, bark_dark)
        c.set(x1 + t, y1, bark_dark)

# Left arm claw (branch fingers)
claw_base = (10, 110)
fingers_left = [
    [(10, 110), (5, 105), (2, 100)],
    [(10, 110), (7, 108), (5, 102)],
    [(10, 110), (10, 107), (10, 100)],
    [(10, 110), (13, 108), (15, 103)],
    [(10, 110), (15, 110), (18, 108)]
]
for finger in fingers_left:
    for i in range(len(finger) - 1):
        x0, y0 = finger[i]
        x1, y1 = finger[i + 1]
        c.line(x0, y0, x1, y1, bark_shadow)
        c.line(x0 + 1, y0, x1 + 1, y1, bark_dark)

# Right arm (extends from trunk right side around y=120)
arm_points_right = [
    (166, 120), (186, 110), (206, 100), (226, 95), (241, 100), (246, 110)
]
for i in range(len(arm_points_right) - 1):
    x0, y0 = arm_points_right[i]
    x1, y1 = arm_points_right[i + 1]
    c.line(x0, y0, x1, y1, bark_mid)
    for t in range(-4, 5):
        c.set(x0 + t, y0, bark_dark)
        c.set(x1 + t, y1, bark_dark)

# Right arm claw
claw_base_r = (246, 110)
fingers_right = [
    [(246, 110), (251, 105), (254, 100)],
    [(246, 110), (249, 108), (251, 102)],
    [(246, 110), (246, 107), (246, 100)],
    [(246, 110), (243, 108), (241, 103)],
    [(246, 110), (241, 110), (238, 108)]
]
for finger in fingers_right:
    for i in range(len(finger) - 1):
        x0, y0 = finger[i]
        x1, y1 = finger[i + 1]
        c.line(x0, y0, x1, y1, bark_shadow)
        c.line(x0 - 1, y0, x1 - 1, y1, bark_dark)

# Moss patches on trunk and arms
moss_patches = [
    (100, 100, 15, 10),
    (145, 95, 12, 8),
    (85, 140, 10, 12),
    (160, 135, 8, 10),
    (120, 180, 20, 8),
    (50, 105, 8, 6),
    (200, 100, 10, 7)
]
for mx, my, mw, mh in moss_patches:
    for x in range(mx, mx + mw):
        for y in range(my, my + mh):
            if ((x + y) % 3) == 0:
                c.set(x, y, moss_dark)
            elif ((x + y) % 3) == 1:
                c.set(x, y, moss_mid)
            else:
                c.set(x, y, moss_light)

# Hanging vines from arms and shoulders
vines = [
    # From left shoulder
    [(70, 115), (68, 130), (70, 145), (68, 160), (70, 175)],
    [(75, 118), (73, 135), (75, 150), (73, 165)],
    # From right shoulder
    [(186, 115), (188, 130), (186, 145), (188, 160), (186, 175)],
    [(181, 118), (183, 135), (181, 150), (183, 165)],
    # From head area
    [(100, 85), (98, 100), (100, 115)],
    [(156, 85), (158, 100), (156, 115)]
]
for vine in vines:
    for i in range(len(vine) - 1):
        x0, y0 = vine[i]
        x1, y1 = vine[i + 1]
        c.line(x0, y0, x1, y1, vine_dark)
        c.line(x0 + 1, y0, x1 + 1, y1, vine_mid)
    # Vine leaves
    for vx, vy in vine[::3]:
        c.set(vx - 2, vy, moss_light)
        c.set(vx + 2, vy, moss_light)

# Roots at base
root_patterns = [
    # Main roots spreading out
    [(128, 225), (100, 240), (70, 250)],
    [(128, 225), (120, 245), (115, 255)],
    [(128, 225), (135, 245), (140, 255)],
    [(128, 225), (155, 240), (185, 250)],
    # Smaller roots
    [(110, 230), (95, 245), (85, 255)],
    [(145, 230), (160, 245), (170, 255)],
    [(118, 235), (110, 250)],
    [(138, 235), (145, 250)]
]
for root in root_patterns:
    for i in range(len(root) - 1):
        x0, y0 = root[i]
        x1, y1 = root[i + 1]
        # Root thickness
        c.line(x0, y0, x1, y1, bark_dark)
        c.line(x0 + 1, y0, x1 + 1, y1, bark_mid)
        c.line(x0 - 1, y0, x1 - 1, y1, bark_shadow)

# Additional details - smaller branches from main trunk
small_branches = [
    [(105, 150), (90, 145), (80, 140)],
    [(150, 155), (165, 150), (175, 145)],
    [(100, 170), (85, 165)],
    [(155, 175), (170, 170)]
]
for branch in small_branches:
    for i in range(len(branch) - 1):
        x0, y0 = branch[i]
        x1, y1 = branch[i + 1]
        c.line(x0, y0, x1, y1, bark_dark)

# Dark outline around the treant
# This creates a menacing silhouette effect
outline_points = []
# Trace around the treant shape
for y in range(60, 230):
    # Find leftmost and rightmost bark pixels
    left_found = None
    right_found = None
    for x in range(256):
        if c.get(x, y) in [bark_shadow, bark_dark, bark_mid, bark_light, bark_highlight]:
            if left_found is None:
                left_found = x
            right_found = x
    if left_found is not None:
        outline_points.append((left_found - 1, y))
        outline_points.append((right_found + 1, y))

# Draw outline
for ox, oy in outline_points:
    if 0 <= ox < 256 and 0 <= oy < 256:
        # Only outline if adjacent to background
        c.set(ox, oy, outline)

# Add some atmospheric particles/spores
for i in range(30):
    px = 50 + (i * 67) % 160
    py = 100 + (i * 43) % 100
    c.set(px, py, god_ray_light)

# Check color count
stats = c.stats()
print(f"Colors used: {stats['colors_used']}")
print(f"Visible pixels: {stats['visible_pixels']}")
print(c.stats_text())

# Submit
finish(c)
