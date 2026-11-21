from pixelbench_api import *

# Create output canvas as a copy of input
output = input_canvas.copy(name='output')

# Get canvas dimensions
width, height = output.stats()['size']
print(f"Canvas size: {width}x{height}")

# Register colors for the thunderstorm effect
# Semi-transparent rain colors (alpha < 255)
rain_semi = output.color('#8ab4d0a0', 'rain_semi')
rain_light = output.color('#a0c0e080', 'rain_light')
rain_drop = output.color('#c0d8f060', 'rain_drop')

# Lightning colors
lightning_white = output.color('#ffffffff', 'lightning_white')
lightning_glow = output.color('#d0e0ff80', 'lightning_glow')

# Wet ground colors
wet_ground = output.color('#1a2a3aff', 'wet_ground')
wet_highlight = output.color('#2a3a4aff', 'wet_highlight')
puddle_dark = output.color('#153040ff', 'puddle_dark')
puddle_light = output.color('#255060ff', 'puddle_light')

# Storm sky colors
storm_sky = output.color('#0f1a25ff', 'storm_sky')

# Water droplet colors
droplet = output.color('#6090b0c0', 'droplet')

# Vending machine colors - use existing palette colors
vm_colors = [9, 36, 41, 33, 34]  # j, K, P, H, I
display_color = output.color('#406080ff', 'display')

print("Colors registered")

# Step 1: Darken the sky (top 55 pixels)
for y in range(0, 55):
    for x in range(width):
        current = output.get(x, y)
        if current in [38, 13]:  # L or m colors (original sky)
            if y < 35:
                output.set(x, y, storm_sky)
            # Leave gradient area below

print("Sky darkened")

# Step 2: Fill character area with vending machine pattern
# The character was in the lower-middle area, we fill it with vending machine
for y in range(80, 145):
    for x in range(35, 135):
        col_block = (x - 35) // 16
        row_block = (y - 80) // 14
        color_idx = vm_colors[(col_block + row_block) % len(vm_colors)]
        output.set(x, y, color_idx)

# Add display panels to the vending machine
for panel_y in range(0, 4):
    py = 90 + panel_y * 14
    for panel_x in range(0, 5):
        px = 45 + panel_x * 16
        output.rect(px + 2, py + 2, 12, 10, display_color, fill=True)

print("Character removed, vending machine filled in")

# Step 3: Make the ground wet (bottom 30 pixels)
for y in range(height - 30, height):
    for x in range(width):
        # Create wet ground pattern
        if (x * 3 + y * 7) % 11 < 4:
            output.set(x, y, wet_ground)
        elif (x * 5 + y * 3) % 13 < 3:
            output.set(x, y, puddle_dark)
        else:
            output.set(x, y, wet_highlight)

# Add puddle reflections
for i in range(25):
    px = 20 + (i * 37) % (width - 40)
    py = height - 22 + (i * 7) % 10
    output.rect(px, py, 6, 2, puddle_light)

print("Wet ground added")

# Step 4: Add semi-transparent rain drops
# Rain falls diagonally from top-right to bottom-left
# Only draw rain in the upper/middle area, not on the ground
for i in range(120):
    start_x = (i * 13) % width
    start_y = (i * 7) % (height - 50)  # Keep rain above ground
    
    # Rain drop length varies
    length = 3 + (i % 5)
    
    for j in range(length):
        rx = start_x - j
        ry = start_y + j * 2
        
        # Only draw if above ground area
        if 0 <= rx < width and 0 <= ry < height - 30:
            if j == 0:
                output.set(rx, ry, rain_drop)
            elif j < length - 1:
                output.set(rx, ry, rain_semi)
            else:
                output.set(rx, ry, rain_light)

print("Rain added")

# Step 5: Add lightning bolts in the sky
# Lightning bolt 1 - main bolt from top
bolt1 = [(75, 3), (78, 12), (74, 22), (80, 32), (76, 42), (82, 52)]
for i in range(len(bolt1) - 1):
    x0, y0 = bolt1[i]
    x1, y1 = bolt1[i + 1]
    output.line(x0, y0, x1, y1, lightning_white)
    # Add glow around it
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x0 + dx, y0 + dy
            if 0 <= nx < width and 0 <= ny < height:
                output.set(nx, ny, lightning_glow)

# Lightning bolt 2
bolt2 = [(125, 5), (120, 15), (127, 25), (122, 35), (130, 45)]
for i in range(len(bolt2) - 1):
    x0, y0 = bolt2[i]
    x1, y1 = bolt2[i + 1]
    output.line(x0, y0, x1, y1, lightning_white)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x0 + dx, y0 + dy
            if 0 <= nx < width and 0 <= ny < height:
                output.set(nx, ny, lightning_glow)

# Lightning bolt 3 - smaller, on the left
bolt3 = [(30, 8), (35, 18), (32, 28), (38, 38)]
for i in range(len(bolt3) - 1):
    x0, y0 = bolt3[i]
    x1, y1 = bolt3[i + 1]
    output.line(x0, y0, x1, y1, lightning_white)

print("Lightning added")

# Step 6: Add water droplets clinging to ground surface
for i in range(60):
    dx = 15 + (i * 19) % (width - 30)
    dy = height - 25 + (i * 5) % 8
    output.set(dx, dy, droplet)
    if dy + 1 < height:
        output.set(dx, dy + 1, puddle_light)

print("Water droplets added")

# Final stats
print("\nFinal canvas stats:")
print(output.stats_text())

# Save preview
save('thunderstorm', output)

# Submit
finish(output)
