from pixelbench_api import new_canvas, finish

# Create 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="bamboo_steamer")

# Define colors
bamboo_dark = c.color("#8B6914", "bamboo_dark")      # Dark bamboo
bamboo_mid = c.color("#C4A35A", "bamboo_mid")        # Medium bamboo
bamboo_light = c.color("#E8D5A3", "bamboo_light")    # Light bamboo
dumpling_white = c.color("#FFF8E7", "dumpling_white") # Dumpling color
dumpling_shadow = c.color("#D4C4A8", "dumpling_shadow") # Dumpling shadow
steam_white = c.color("#FFFFFF", "steam_white")      # Steam
steam_faint = c.color("#E0E0E0", "steam_faint")      # Faint steam
basket_inner = c.color("#6B5423", "basket_inner")    # Inner basket shadow

# Draw the bamboo steamer basket (bottom part)
# Outer ring of the basket - elliptical shape
# Bottom arc of the basket
for x in range(4, 29):
    # Calculate y position for ellipse bottom
    # Using ellipse formula centered at (16, 22) with rx=12, ry=8
    dx = x - 16
    if dx*dx <= 144:  # rx^2 = 144
        y_offset = int(8 * (1 - (dx*dx)/144)**0.5)
        y = 22 + y_offset
        if y < 32:
            c.set(x, y, bamboo_dark)
            if y > 0:
                c.set(x, y-1, bamboo_mid)

# Draw basket weave pattern on the sides
for row in range(18, 28):
    for col in range(6, 27):
        # Create woven bamboo texture
        if (row + col) % 4 < 2:
            c.set(col, row, bamboo_mid)
        else:
            c.set(col, row, bamboo_dark)

# Draw the three dumplings inside
# Dumpling 1 (left)
c.circle(10, 20, 4, dumpling_white, fill=True)
c.circle(10, 21, 3, dumpling_shadow, fill=False)

# Dumpling 2 (center)
c.circle(16, 21, 4, dumpling_white, fill=True)
c.circle(16, 22, 3, dumpling_shadow, fill=False)

# Dumpling 3 (right)
c.circle(22, 20, 4, dumpling_white, fill=True)
c.circle(22, 21, 3, dumpling_shadow, fill=False)

# Add dumpling pleats/folds
for dumpling_x in [10, 16, 22]:
    for i in range(-2, 3):
        c.set(dumpling_x + i, 18, dumpling_shadow)

# Draw the basket rim (top edge of bottom part)
c.line(5, 18, 27, 18, bamboo_dark)
c.line(5, 17, 27, 17, bamboo_light)

# Draw the lid (partially open - tilted up on right side)
# Lid is an ellipse/oval shape
# Main lid body
for x in range(4, 29):
    dx = x - 16
    if dx*dx <= 144:
        # Lid curves upward, tilted
        y_base = 12 - int(5 * (1 - (dx*dx)/144)**0.5)
        # Tilt: right side higher
        tilt = int(dx * 0.15)
        y = y_base + tilt
        c.set(x, y, bamboo_dark)
        c.set(x, y+1, bamboo_mid)
        c.set(x, y+2, bamboo_light)

# Lid handle/knob on top
c.circle(16, 6, 2, bamboo_dark, fill=True)
c.circle(16, 6, 1, bamboo_light, fill=True)

# Lid rim
c.line(4, 13, 28, 11, bamboo_dark)

# Draw steam rising
# Small wisps of steam
steam_positions = [
    (14, 4), (15, 3), (16, 2), (17, 3), (18, 4),
    (15, 6), (16, 5), (17, 6),
    (14, 8), (18, 8)
]

for sx, sy in steam_positions:
    c.set(sx, sy, steam_faint)

# Add more steam particles
c.set(16, 1, steam_white)
c.set(15, 2, steam_faint)
c.set(17, 2, steam_faint)

# Draw basket weave details on lid
for x in range(6, 27, 3):
    for y in range(8, 13):
        if (x + y) % 2 == 0:
            c.set(x, y, bamboo_light)

# Add some depth/shadow to dumplings
c.set(10, 23, dumpling_shadow)
c.set(16, 24, dumpling_shadow)
c.set(22, 23, dumpling_shadow)

# Inner shadow of basket
for x in range(7, 26):
    c.set(x, 19, basket_inner)

# Print stats to check color count
print(c.stats_text())
print(c.matrix_text())

# Submit the canvas
finish(c)
