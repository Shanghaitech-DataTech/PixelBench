from pixelbench_api import *

# Create a 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="camera")

# Define colors
dark_outline = c.color("#1a1a1a", "outline")
leather_dark = c.color("#3d2817", "leather_dark")
leather_mid = c.color("#5c3d2a", "leather_mid")
leather_light = c.color("#7a523a", "leather_light")
lens_dark = c.color("#0d0d0d", "lens_dark")
lens_mid = c.color("#2a2a2a", "lens_mid")
lens_highlight = c.color("#6b8cff", "lens_glass")
metal_dark = c.color("#4a4a4a", "metal_dark")
metal_mid = c.color("#6a6a6a", "metal_mid")
metal_light = c.color("#8a8a8a", "metal_light")
button_color = c.color("#5a5a5a", "button")

# Draw main camera body (rectangular with rounded corners feel)
# Body outline - dark
c.rect(4, 10, 24, 16, dark_outline, fill=True)

# Leather body - main fill
c.rect(5, 11, 22, 14, leather_dark, fill=True)

# Top plate of camera
c.rect(6, 8, 20, 4, metal_dark, fill=True)
c.rect(7, 9, 18, 2, metal_mid, fill=True)

# Draw lens (circular, centered on body)
# Lens outer ring
c.circle(16, 18, 6, dark_outline, fill=True)
c.circle(16, 18, 5, metal_dark, fill=True)
c.circle(16, 18, 4, lens_dark, fill=True)
c.circle(16, 18, 3, lens_mid, fill=True)
# Lens glass highlight
c.set(14, 16, lens_highlight)
c.set(15, 16, lens_highlight)
c.set(14, 17, lens_highlight)

# Shutter button on top
c.rect(20, 7, 4, 3, metal_light, fill=True)
c.set(21, 7, button_color)
c.set(22, 7, button_color)
c.set(21, 8, button_color)

# Film advance lever (small detail on top)
c.rect(26, 7, 2, 2, metal_mid, fill=True)

# Leather texture - small dots pattern on body
leather_dots = [
    (7, 13), (10, 13), (13, 13), (16, 13), (19, 13), (22, 13), (25, 13),
    (8, 15), (11, 15), (14, 15), (17, 15), (20, 15), (23, 15),
    (7, 17), (10, 17), (13, 17), (16, 17), (19, 17), (22, 17), (25, 17),
    (8, 19), (11, 19), (14, 19), (17, 19), (20, 19), (23, 19),
    (7, 21), (10, 21), (13, 21), (16, 21), (19, 21), (22, 21), (25, 21),
]
for x, y in leather_dots:
    c.set(x, y, leather_mid)

# Add some leather highlights
c.set(6, 12, leather_light)
c.set(8, 12, leather_light)
c.set(24, 12, leather_light)
c.set(26, 12, leather_light)

# Viewfinder window on top back
c.rect(8, 8, 4, 2, dark_outline, fill=True)
c.rect(9, 9, 2, 1, "#1a1a1a", fill=True)

# Bottom plate detail
c.rect(6, 24, 20, 2, metal_dark, fill=True)
c.set(8, 25, metal_mid)
c.set(24, 25, metal_mid)

# Add outline around entire camera for definition
# Left side
c.line(4, 8, 4, 26, dark_outline)
# Right side
c.line(28, 8, 28, 26, dark_outline)
# Top
c.line(4, 8, 28, 8, dark_outline)
# Bottom
c.line(4, 26, 28, 26, dark_outline)

# Lens ring details
c.circle(16, 18, 5, metal_mid, fill=False)

# Print stats to check
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

# Submit the result
finish(c)
