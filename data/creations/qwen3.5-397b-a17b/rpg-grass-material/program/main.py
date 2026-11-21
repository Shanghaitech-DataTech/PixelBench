from pixelbench_api import *

# Create a 16x16 canvas for the grass tile
c = new_canvas(16, 16, name="grass_tile")

# Define the color palette - keeping under 86 colors
# Base grass greens - main tones for interleaved speckles
base_green = c.color((68, 136, 68), "base_green")
med_green = c.color((51, 119, 51), "med_green")
dark_green = c.color((34, 85, 34), "dark_green")
light_green = c.color((85, 153, 85), "light_green")
bright_green = c.color((102, 170, 102), "bright_green")
olive_green = c.color((68, 102, 51), "olive_green")
forest_green = c.color((25, 70, 25), "forest_green")

# Yellow for flowers
yellow = c.color((221, 204, 51), "yellow")
pale_yellow = c.color((238, 221, 85), "pale_yellow")

# Brown for dirt patches
dirt_brown = c.color((102, 68, 34), "dirt_brown")
light_dirt = c.color((136, 102, 68), "light_dirt")
dark_dirt = c.color((68, 51, 34), "dark_dirt")

# Fill background with base grass color
c.rect(0, 0, 16, 16, base_green, fill=True)

# Create interleaved speckle pattern - designed for seamless tiling
# Using a pattern that repeats every 4 pixels in both directions
for y in range(16):
    for x in range(16):
        # Pattern repeats every 4 pixels for seamless tiling
        px = x % 4
        py = y % 4
        pattern_val = (px + py * 2) % 4
        
        if pattern_val == 0:
            c.set(x, y, dark_green)
        elif pattern_val == 1:
            c.set(x, y, light_green)
        elif pattern_val == 2:
            c.set(x, y, med_green)
        else:
            c.set(x, y, bright_green)

# Add darker grass tufts - small clusters placed for seamless tiling
# Positions chosen to work when tile repeats
tuft_data = [
    (2, 4, forest_green), (7, 1, forest_green), (12, 5, forest_green),
    (5, 9, forest_green), (10, 12, forest_green), (14, 8, olive_green),
    (1, 13, forest_green), (8, 7, olive_green),
]

for tx, ty, tuft_color in tuft_data:
    c.set(tx, ty, tuft_color)
    # Add adjacent pixels for tuft effect (grass clumps)
    if tx + 1 < 16:
        c.set(tx + 1, ty, olive_green)
    if ty + 1 < 16:
        c.set(tx, ty + 1, med_green)

# Add tiny yellow flowers (sparse) - positioned away from edges for clean tiling
flower_data = [
    (3, 2, yellow), (9, 6, pale_yellow), (1, 7, yellow),
    (11, 10, yellow), (6, 13, pale_yellow), (13, 4, yellow),
]

for fx, fy, flower_color in flower_data:
    c.set(fx, fy, flower_color)

# Add sparse bare-dirt patches - avoid edges for clean tiling
dirt_data = [
    (4, 6, dirt_brown), (11, 3, light_dirt), (2, 10, dark_dirt),
    (8, 2, dirt_brown), (14, 11, light_dirt), (6, 8, dark_dirt),
]

for dx, dy, dirt_color in dirt_data:
    c.set(dx, dy, dirt_color)

# Print stats to verify color count
print(c.stats_text())
print(c.matrix_text())

# Submit the result
finish(c)
