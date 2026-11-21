from pixelbench_api import new_canvas, finish

# Create 128x128 canvas
c = new_canvas(128, 128)

# Define colors for the sunrise mountain village scene
# Sky colors (sunrise gradient from top to horizon)
sky_dark = c.color((30, 20, 60), "sky_dark")       # Deep purple at top
sky_mid = c.color((80, 40, 100), "sky_mid")        # Purple-pink
sky_light = c.color((150, 80, 120), "sky_light")   # Pink
sky_horizon = c.color((255, 150, 80), "sky_horizon")  # Orange at horizon
sun_core = c.color((255, 220, 100), "sun_core")    # Sun center
sun_glow = c.color((255, 180, 50), "sun_glow")     # Sun glow

# Distant mountains (layered, lighter for depth)
mountain_far = c.color((120, 130, 150), "mountain_far")
mountain_mid = c.color((80, 90, 110), "mountain_mid")
mountain_near = c.color((50, 60, 80), "mountain_near")

# Pine tree colors
pine_dark = c.color((20, 60, 30), "pine_dark")
pine_mid = c.color((30, 90, 45), "pine_mid")
pine_light = c.color((50, 120, 60), "pine_light")

# House colors (wooden)
house_wall = c.color((120, 80, 40), "house_wall")
house_dark = c.color((80, 50, 25), "house_dark")
house_roof = c.color((60, 40, 20), "house_roof")
house_window = c.color((255, 200, 100), "house_window")
house_door = c.color((70, 45, 25), "house_door")

# Stone path
path_stone = c.color((100, 100, 110), "path_stone")
path_light = c.color((130, 130, 140), "path_light")
path_dark = c.color((70, 70, 80), "path_dark")

# Ground/grass
ground = c.color((60, 80, 40), "ground")
ground_dark = c.color((40, 60, 25), "ground_dark")

# Smoke
smoke = c.color((200, 200, 210), "smoke")
smoke_light = c.color((230, 230, 240), "smoke_light")

# Chimney
chimney = c.color((70, 50, 40), "chimney")

# === DRAWING FROM BACK TO FRONT ===

# 1. Sky gradient (top to bottom)
for y in range(64):
    # Interpolate from dark purple to orange
    t = y / 64
    r = int(30 + t * 225)
    g = int(20 + t * 130)
    b = int(60 + t * 60)
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255
    color = c.color((r, g, b))
    c.rect(0, y, 128, 1, color)

# 2. Sun (rising behind mountains, center-ish)
# Sun glow
c.circle(64, 55, 18, sun_glow, fill=True)
# Sun core
c.circle(64, 55, 10, sun_core, fill=True)

# 3. Distant mountains (back layer - lightest)
c.poly([(0, 70), (20, 55), (40, 65), (60, 50), (80, 60), (100, 48), (127, 58), (127, 80), (0, 80)], mountain_far, fill=True)

# 4. Middle mountains
c.poly([(0, 75), (15, 62), (35, 72), (55, 58), (75, 68), (95, 55), (115, 65), (128, 70), (128, 90), (0, 90)], mountain_mid, fill=True)

# 5. Near mountains (darker, more detail)
c.poly([(0, 85), (10, 72), (30, 80), (50, 68), (70, 78), (90, 65), (110, 75), (128, 82), (128, 100), (0, 100)], mountain_near, fill=True)

# 6. Ground (foreground area)
c.rect(0, 95, 128, 33, ground, fill=True)
c.rect(0, 110, 128, 18, ground_dark, fill=True)

# 7. Stone path (winding from bottom center toward houses)
# Main path - wider at bottom, narrowing toward houses
path_points = [(58, 127), (62, 127), (60, 115), (64, 115), (58, 105), (66, 105), (55, 95), (69, 95), (52, 88), (72, 88)]
for i in range(len(path_points) - 1):
    x0, y0 = path_points[i]
    x1, y1 = path_points[i+1]
    c.line(x0, y0, x1, y1, path_stone)
    c.line(x0+1, y0, x1+1, y1, path_stone)
    c.line(x0+2, y0, x1+2, y1, path_light)
    c.line(x0-1, y0, x1-1, y1, path_dark)

# Fill path area
c.poly([(58, 127), (62, 127), (72, 88), (52, 88)], path_stone, fill=True)

# 8. Pine trees (scattered, various sizes)
def draw_pine(cx, cy, size, color_dark, color_mid, color_light):
    # Three tiered triangles for pine tree
    if size >= 3:
        # Bottom tier
        c.poly([(cx, cy - size*3), (cx - size, cy - size), (cx + size, cy - size)], color_dark, fill=True)
    if size >= 2:
        # Middle tier
        c.poly([(cx, cy - size*2), (cx - size+1, cy - size), (cx + size-1, cy - size)], color_mid, fill=True)
    # Top tier
    c.poly([(cx, cy - size), (cx - size+2, cy), (cx + size-2, cy)], color_light, fill=True)
    # Trunk
    c.rect(cx-1, cy, 2, 3, (70, 50, 30))

# Draw several pine trees at different positions and sizes
draw_pine(15, 92, 5, pine_dark, pine_mid, pine_light)
draw_pine(110, 90, 6, pine_dark, pine_mid, pine_light)
draw_pine(8, 98, 4, pine_dark, pine_mid, pine_light)
draw_pine(118, 96, 4, pine_dark, pine_mid, pine_light)
draw_pine(25, 88, 3, pine_dark, pine_mid, pine_light)
draw_pine(100, 86, 4, pine_dark, pine_mid, pine_light)

# 9. Three wooden houses (center focal area)
def draw_house(x, y, width, height, has_chimney=True):
    # House base (walls)
    c.rect(x, y, width, height, house_wall, fill=True)
    # Darker edges for depth
    c.rect(x, y, 2, height, house_dark, fill=True)
    c.rect(x + width - 2, y, 2, height, house_dark, fill=True)
    
    # Roof (triangle)
    roof_base_y = y
    roof_peak_y = y - int(height * 0.6)
    roof_overhang = 4
    c.poly([
        (x - roof_overhang, y),
        (x + width + roof_overhang, y),
        (x + width // 2, roof_peak_y)
    ], house_roof, fill=True)
    
    # Door
    door_w = width // 4
    door_h = height // 2
    door_x = x + width // 2 - door_w // 2
    c.rect(door_x, y + height - door_h, door_w, door_h, house_door, fill=True)
    
    # Windows (glowing)
    win_size = 4
    win_y = y + height // 3
    c.rect(x + 4, win_y, win_size, win_size, house_window, fill=True)
    c.rect(x + width - 4 - win_size, win_y, win_size, win_size, house_window, fill=True)
    
    # Chimney and smoke
    if has_chimney:
        chim_x = x + width - 8
        chim_w = 5
        chim_h = 12
        c.rect(chim_x, roof_peak_y - chim_h + 4, chim_w, chim_h, chimney, fill=True)
        # Smoke puffs
        c.circle(chim_x + 2, roof_peak_y - chim_h - 2, 4, smoke, fill=True)
        c.circle(chim_x + 4, roof_peak_y - chim_h - 6, 3, smoke_light, fill=True)
        c.circle(chim_x + 1, roof_peak_y - chim_h - 10, 3, smoke, fill=True)

# Main house (center, largest - focal point)
draw_house(52, 78, 24, 16, has_chimney=True)

# Left house (smaller)
draw_house(28, 82, 18, 12, has_chimney=True)

# Right house (medium)
draw_house(82, 80, 20, 14, has_chimney=False)

# 10. Add some foreground details - small rocks/bushes
for rx, ry in [(20, 115), (45, 120), (85, 118), (105, 122)]:
    c.circle(rx, ry, 2, path_dark, fill=True)

# 11. Add some grass tufts near path (reuse ground color)
for gx, gy in [(50, 110), (70, 108), (55, 98), (68, 95)]:
    c.set(gx, gy, ground)
    c.set(gx-1, gy+1, ground)
    c.set(gx+1, gy+1, ground)

print(c.stats_text())

# Submit the canvas
finish(c)
