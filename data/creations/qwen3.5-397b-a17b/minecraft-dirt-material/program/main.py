from pixelbench_api import new_canvas, finish

# Create a 16x16 canvas for the dirt texture
c = new_canvas(16, 16, name="dirt")

# Define dirt color palette (6 colors for granular variation)
dark_brown = c.color('#3d2817')      # darkest shadows
med_dark = c.color('#5a3d2a')         # dark midtones  
mid_brown = c.color('#7a5638')        # base dirt color
light_brown = c.color('#9a7248')      # lighter areas
pale_brown = c.color('#b89060')       # highlights
warm_brown = c.color('#6b4a32')       # warm midtone

# Create a seamless granular dirt texture
# For seamless tiling, edges must match: left=right, top=bottom

# Draw base layer with mid_brown
c.rect(0, 0, 16, 16, mid_brown, fill=True)

# Add granular texture using scattered pixels
# Using a pattern that tiles seamlessly

# Dark speckles (scattered)
dark_pixels = [
    (1, 2), (4, 1), (7, 3), (10, 2), (13, 1),
    (2, 5), (6, 4), (9, 6), (12, 5), (15, 4),
    (0, 8), (3, 7), (5, 9), (8, 8), (11, 7), (14, 9),
    (1, 11), (4, 10), (7, 12), (10, 11), (13, 10),
    (2, 14), (5, 13), (8, 15), (11, 14), (14, 13),
    # Edge-matching pixels for seamless tiling
    (15, 2), (0, 5), (15, 8), (0, 11), (15, 14),
    (1, 15), (4, 15), (7, 15), (10, 15), (13, 15),
]
for x, y in dark_pixels:
    c.set(x, y, dark_brown)

# Medium-dark speckles
med_dark_pixels = [
    (3, 0), (6, 2), (9, 1), (12, 3),
    (0, 3), (5, 6), (8, 5), (11, 4), (14, 6),
    (2, 9), (7, 8), (10, 10), (13, 9),
    (1, 13), (4, 12), (9, 14), (12, 13),
    # Edge matching
    (15, 0), (0, 6), (15, 9), (0, 14),
    (3, 15), (6, 15), (9, 15), (12, 15),
]
for x, y in med_dark_pixels:
    c.set(x, y, med_dark)

# Warm brown accents
warm_pixels = [
    (2, 1), (5, 4), (8, 3), (11, 6), (14, 5),
    (1, 7), (4, 10), (7, 9), (10, 12), (13, 11),
    (3, 14), (6, 13), (9, 15), (12, 14),
    # Edge matching
    (15, 4), (0, 10), (15, 11),
    (2, 15), (5, 15), (8, 15), (11, 15), (14, 15),
]
for x, y in warm_pixels:
    c.set(x, y, warm_brown)

# Light brown highlights (less frequent)
light_pixels = [
    (0, 0), (4, 3), (7, 5), (10, 4), (13, 7),
    (2, 10), (5, 8), (8, 11), (11, 10), (14, 12),
    (1, 15), (4, 14), (7, 13), (10, 15), (13, 14),
    # Edge matching
    (15, 7), (0, 12), (15, 15),
]
for x, y in light_pixels:
    c.set(x, y, light_brown)

# Pale brown rare highlights
pale_pixels = [
    (6, 0), (9, 3), (12, 6), (3, 12), (6, 14),
    (15, 3), (0, 15),
]
for x, y in pale_pixels:
    c.set(x, y, pale_brown)

# Verify color count
stats = c.stats()
print(f"Colors used: {stats['colors_used']}")
print(f"Visible pixels: {stats['visible_pixels']}")
print(c.stats_text())

# Submit the dirt texture
finish(c)
