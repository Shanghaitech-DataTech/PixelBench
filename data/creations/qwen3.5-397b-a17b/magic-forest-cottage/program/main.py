from pixelbench_api import new_canvas, finish

# Create 128x128 canvas
c = new_canvas(128, 128, name="magic_cottage")

# Define color palette - staying under 86 colors
# Sky colors (deep purple night)
sky_dark = c.color("#1a0a2e", "sky_dark")
sky_mid = c.color("#2d1b4e", "sky_mid")
sky_light = c.color("#4a2d7a", "sky_light")

# Moon colors
moon_dark = c.color("#f4e4bc", "moon_dark")
moon_mid = c.color("#fff8dc", "moon_mid")
moon_bright = c.color("#ffffff", "moon_bright")

# Cottage wall colors (wood and stone)
wall_dark = c.color("#3d2817", "wall_dark")
wall_mid = c.color("#5c4033", "wall_mid")
wall_light = c.color("#7a5c47", "wall_light")
stone_dark = c.color("#4a4a4a", "stone_dark")
stone_mid = c.color("#6b6b6b", "stone_mid")
stone_light = c.color("#8a8a8a", "stone_light")

# Roof colors (steep, mossy)
roof_dark = c.color("#2a1f1a", "roof_dark")
roof_mid = c.color("#3d2f25", "roof_mid")
moss_dark = c.color("#3a5f3a", "moss_dark")
moss_mid = c.color("#5a8f5a", "moss_mid")
moss_light = c.color("#7abf7a", "moss_light")

# Window light (warm orange)
window_dark = c.color("#cc6600", "window_dark")
window_mid = c.color("#ff9933", "window_mid")
window_bright = c.color("#ffcc66", "window_bright")
window_glow = c.color("#ffaa44", "window_glow")

# Well colors
well_stone = c.color("#5a5a5a", "well_stone")
well_dark = c.color("#3a3a3a", "well_dark")
well_highlight = c.color("#7a7a7a", "well_highlight")

# Winch (wooden)
winch_dark = c.color("#4a3525", "winch_dark")
winch_mid = c.color("#6b4f35", "winch_mid")

# Path (stone slabs)
path_dark = c.color("#4a4540", "path_dark")
path_mid = c.color("#6a6560", "path_mid")
path_light = c.color("#8a8580", "path_light")

# Tree trunks (twisted, ancient)
trunk_dark = c.color("#2a1a10", "trunk_dark")
trunk_mid = c.color("#4a3020", "trunk_mid")
trunk_light = c.color("#6a4a30", "trunk_light")

# Leaves (dark red brown purple)
leaf_dark = c.color("#3a1a2a", "leaf_dark")
leaf_mid = c.color("#5a2a3a", "leaf_mid")
leaf_red = c.color("#6a3040", "leaf_red")
leaf_purple = c.color("#4a2050", "leaf_purple")
leaf_brown = c.color("#5a3525", "leaf_brown")

# Mist colors
mist_light = c.color("#6a5a7a40", "mist_light")
mist_mid = c.color("#8a7a9a30", "mist_mid")

# Ground
ground_dark = c.color("#1a1510", "ground_dark")
ground_mid = c.color("#2a2018", "ground_mid")
ground_light = c.color("#3a3025", "ground_light")

# Draw sky gradient (top to middle)
for y in range(0, 70):
    ratio = y / 70
    if ratio < 0.33:
        sky_col = sky_dark
    elif ratio < 0.66:
        sky_col = sky_mid
    else:
        sky_col = sky_light
    c.rect(0, y, 128, 1, sky_col)

# Draw full moon (upper right)
moon_x, moon_y = 95, 25
moon_r = 12
c.circle(moon_x, moon_y, moon_r, moon_mid)
# Add moon crater details
c.set(moon_x - 3, moon_y - 2, moon_dark)
c.set(moon_x + 2, moon_y + 3, moon_dark)
c.set(moon_x - 1, moon_y + 4, moon_dark)
c.set(moon_x + 4, moon_y - 1, moon_dark)
# Moon glow
c.circle(moon_x, moon_y, moon_r + 2, "#ffffff20")

# Draw ground (bottom portion)
for y in range(75, 128):
    ratio = (y - 75) / 53
    if ratio < 0.3:
        ground_col = ground_dark
    elif ratio < 0.6:
        ground_col = ground_mid
    else:
        ground_col = ground_light
    c.rect(0, y, 128, 1, ground_col)

# Draw mist layers (near ground)
for y in range(65, 85):
    alpha = int(60 - (y - 65) * 3)
    if alpha > 0:
        c.rect(0, y, 128, 1, f"#8a7a9a{alpha:02x}")

# Draw stone path (from bottom center toward cottage)
# Path curves slightly
path_points = [(64, 127), (62, 115), (60, 103), (58, 95), (56, 88), (55, 82)]
for i in range(len(path_points) - 1):
    x0, y0 = path_points[i]
    x1, y1 = path_points[i + 1]
    c.line(x0, y0, x1, y1, path_mid)
    # Path width
    for w in range(-3, 4):
        if 0 <= x0 + w < 128:
            c.set(x0 + w, y0, path_dark)
            c.set(x1 + w, y1, path_dark)

# Add stone slab details to path
for y in range(85, 128, 8):
    for x in range(58, 70):
        if (x + y) % 3 == 0:
            c.set(x, y, path_light)

# Draw cottage (center-left)
cottage_x, cottage_y = 35, 65
cottage_w, cottage_h = 45, 35

# Main cottage walls
c.rect(cottage_x, cottage_y, cottage_w, cottage_h, wall_mid)
# Add stone foundation
c.rect(cottage_x - 2, cottage_y + cottage_h - 8, cottage_w + 4, 8, stone_mid)
c.rect(cottage_x - 1, cottage_y + cottage_h - 6, cottage_w + 2, 6, stone_dark)

# Add wall texture (wood planks)
for y in range(cottage_y + 5, cottage_y + cottage_h - 10, 6):
    c.line(cottage_x, y, cottage_x + cottage_w, y, wall_dark)

# Draw steep roof
roof_start_y = cottage_y - 5
roof_peak_y = cottage_y - 28
roof_center_x = cottage_x + cottage_w // 2

# Left roof slope
c.poly([
    (cottage_x - 5, cottage_y),
    (roof_center_x, roof_peak_y),
    (roof_center_x + 2, roof_peak_y + 3),
    (cottage_x - 3, cottage_y),
], roof_mid, fill=True)

# Right roof slope
c.poly([
    (cottage_x + cottage_w + 5, cottage_y),
    (roof_center_x, roof_peak_y),
    (roof_center_x - 2, roof_peak_y + 3),
    (cottage_x + cottage_w + 3, cottage_y),
], roof_dark, fill=True)

# Add moss to roof (left side more mossy)
for y in range(roof_peak_y + 5, cottage_y, 3):
    for x in range(cottage_x - 3, roof_center_x):
        if (x + y) % 4 == 0:
            c.set(x, y, moss_dark)
        elif (x + y) % 7 == 0:
            c.set(x, y, moss_mid)

# Draw windows with warm light
# Main window
win_x, win_y = cottage_x + 12, cottage_y + 10
win_w, win_h = 10, 12
c.rect(win_x, win_y, win_w, win_h, window_dark)
c.rect(win_x + 1, win_y + 1, win_w - 2, win_h - 2, window_mid)
c.rect(win_x + 3, win_y + 3, win_w - 6, win_h - 6, window_bright)
# Window frame
c.line(win_x + win_w // 2, win_y, win_x + win_w // 2, win_y + win_h, wall_dark)
c.line(win_x, win_y + win_h // 2, win_x + win_w, win_y + win_h // 2, wall_dark)

# Second window
win2_x, win2_y = cottage_x + 28, cottage_y + 10
c.rect(win2_x, win2_y, win_w, win_h, window_dark)
c.rect(win2_x + 1, win2_y + 1, win_w - 2, win_h - 2, window_mid)
c.rect(win2_x + 3, win2_y + 3, win_w - 6, win_h - 6, window_bright)
c.line(win2_x + win_w // 2, win2_y, win2_x + win_w // 2, win2_y + win_h, wall_dark)
c.line(win2_x, win2_y + win_h // 2, win2_x + win_w, win2_y + win_h // 2, wall_dark)

# Window glow effect
for dy in range(-3, 4):
    for dx in range(-3, 4):
        if abs(dx) + abs(dy) > 5:
            px, py = win_x + win_w // 2 + dx, win_y + win_h // 2 + dy
            if 0 <= px < 128 and 0 <= py < 128:
                orig = c.get(px, py)
                if orig in [wall_mid, wall_dark]:
                    c.set(px, py, window_glow)

# Draw door
door_x, door_y = cottage_x + 18, cottage_y + 20
door_w, door_h = 12, 15
c.rect(door_x, door_y, door_w, door_h, wall_dark)
c.rect(door_x + 1, door_y + 1, door_w - 2, door_h - 1, wall_mid)
# Door handle
c.set(door_x + door_w - 3, door_y + door_h // 2, stone_light)

# Draw stone well (right side)
well_x, well_y = 95, 85
well_r = 8
# Well base
c.circle(well_x, well_y + 8, well_r, well_stone, fill=True)
c.circle(well_x, well_y + 8, well_r - 2, well_dark, fill=True)
# Well rim
for x in range(well_x - well_r - 2, well_x + well_r + 3):
    c.set(x, well_y, well_highlight)
    c.set(x, well_y + 1, well_stone)

# Well support posts
c.rect(well_x - 10, well_y - 15, 4, 18, winch_dark)
c.rect(well_x + 6, well_y - 15, 4, 18, winch_dark)
# Cross beam
c.rect(well_x - 11, well_y - 18, 22, 4, winch_mid)
# Winch wheel
c.circle(well_x, well_y - 16, 4, winch_dark, fill=False)
# Rope
c.line(well_x, well_y - 16, well_x, well_y + 5, "#cccccc")
# Bucket
c.rect(well_x - 3, well_y + 2, 6, 5, wall_dark)

# Draw twisted ancient trees
# Left tree
tree1_x, tree1_y = 15, 75
# Trunk
c.poly([(tree1_x - 4, tree1_y + 30), (tree1_x + 2, tree1_y + 30),
        (tree1_x + 4, tree1_y + 10), (tree1_x - 2, tree1_y + 10),
        (tree1_x - 5, tree1_y - 5), (tree1_x - 3, tree1_y - 5)], trunk_mid, fill=True)
c.poly([(tree1_x - 3, tree1_y + 30), (tree1_x + 1, tree1_y + 30),
        (tree1_x + 2, tree1_y + 10), (tree1_x - 1, tree1_y + 10),
        (tree1_x - 4, tree1_y - 5), (tree1_x - 2, tree1_y - 5)], trunk_dark, fill=True)

# Left tree foliage
c.circle(tree1_x - 5, tree1_y - 10, 18, leaf_dark, fill=True)
c.circle(tree1_x + 5, tree1_y - 15, 15, leaf_mid, fill=True)
c.circle(tree1_x - 10, tree1_y - 5, 12, leaf_purple, fill=True)
c.circle(tree1_x, tree1_y - 20, 14, leaf_red, fill=True)
c.circle(tree1_x - 8, tree1_y - 18, 10, leaf_brown, fill=True)

# Right tree
tree2_x, tree2_y = 110, 70
# Trunk
c.poly([(tree2_x - 3, tree2_y + 35), (tree2_x + 5, tree2_y + 35),
        (tree2_x + 6, tree2_y + 15), (tree2_x - 2, tree2_y + 15),
        (tree2_x - 4, tree2_y), (tree2_x - 1, tree2_y)], trunk_mid, fill=True)
c.poly([(tree2_x - 2, tree2_y + 35), (tree2_x + 4, tree2_y + 35),
        (tree2_x + 5, tree2_y + 15), (tree2_x - 1, tree2_y + 15),
        (tree2_x - 3, tree2_y), (tree2_x, tree2_y)], trunk_dark, fill=True)

# Right tree foliage
c.circle(tree2_x + 8, tree2_y - 8, 20, leaf_dark, fill=True)
c.circle(tree2_x - 5, tree2_y - 12, 16, leaf_mid, fill=True)
c.circle(tree2_x + 12, tree2_y - 3, 14, leaf_purple, fill=True)
c.circle(tree2_x, tree2_y - 18, 16, leaf_red, fill=True)
c.circle(tree2_x + 5, tree2_y - 20, 12, leaf_brown, fill=True)

# Background tree silhouettes
for bx in [5, 25, 100, 120]:
    by = 60
    c.poly([(bx - 3, 85), (bx + 3, 85), (bx + 4, 65), (bx, 50), (bx - 4, 65)], "#1a0f1a", fill=True)

# Add more mist near ground (wispy)
for _ in range(30):
    mx = (hash(str(_)) % 100) + 10
    my = 75 + (hash(str(_ + 1)) % 15)
    c.set(mx, my, "#9a8aaa20")
    c.set(mx + 1, my, "#9a8aaa15")

# Add some stars in the sky
import random
random.seed(42)
for _ in range(25):
    sx = random.randint(5, 123)
    sy = random.randint(5, 55)
    # Avoid moon area
    if (sx - moon_x) ** 2 + (sy - moon_y) ** 2 > 25:
        star_bright = random.choice([moon_bright, moon_mid, "#aaaaaa"])
        c.set(sx, sy, star_bright)

# Add chimney smoke
chimney_x, chimney_y = cottage_x + 38, cottage_y - 15
for i in range(8):
    smoke_x = chimney_x + (i % 3) - 1
    smoke_y = chimney_y - i * 3
    smoke_alpha = 60 - i * 7
    if smoke_alpha > 0:
        c.circle(smoke_x, smoke_y, 3 + i // 2, f"#aaaaaa{smoke_alpha:02x}", fill=True)

# Add foreground grass/vegetation
for x in range(0, 128, 3):
    if x < 25 or x > 85:  # Not on path
        gy = 120 + (x % 5)
        c.set(x, gy, "#2a4a2a")
        c.set(x, gy - 1, "#3a5a3a")
        c.set(x + 1, gy, "#1a3a1a")

# Add some small flowers near path
for fx in [55, 72, 58, 70]:
    fy = 100 + (fx % 4)
    c.set(fx, fy, "#aa66aa")
    c.set(fx, fy + 1, "#66aa66")

# Add final atmospheric touches - more mist around trees
for ty in range(70, 95):
    for tx in [10, 20, 105, 115]:
        if (tx + ty) % 5 == 0:
            c.set(tx, ty, "#7a6a8a25")
            c.set(tx + 1, ty, "#8a7a9a15")

# Check color count
stats = c.stats()
print(f"Colors used: {stats['colors_used']}")
print(f"Visible pixels: {stats['visible_pixels']}")
print(c.stats_text())

# Submit
finish(c)
