from pixelbench_api import new_canvas, finish

# Create 64x64 canvas
c = new_canvas(64, 64, name="dining_table")

# Define colors
dark_outline = c.color("#2d1810", "dark_outline")  # Dark brown/black for outlines
wood_dark = c.color("#5c3a21", "wood_dark")  # Dark wood
wood_medium = c.color("#8b5a2b", "wood_medium")  # Medium wood
wood_light = c.color("#a07040", "wood_light")  # Light wood highlight
chair_wood = c.color("#6b4423", "chair_wood")  # Chair wood
chair_seat = c.color("#8b6f47", "chair_seat")  # Chair seat
bowl_white = c.color("#f5f0e8", "bowl_white")  # Ceramic bowl
bowl_shadow = c.color("#d0c8b8", "bowl_shadow")  # Bowl shadow
table_surface = c.color("#9c6b3f", "table_surface")  # Table top
apple_red = c.color("#c41e3a", "apple_red")  # Red apple
apple_highlight = c.color("#e04050", "apple_highlight")
banana_yellow = c.color("#ffe135", "banana_yellow")
orange_color = c.color("#ff8c00", "orange_color")
grape_purple = c.color("#6b3fa0", "grape_purple")
grape_light = c.color("#8b5fc4", "grape_light")
leaf_green = c.color("#2d5a27", "leaf_green")
background = c.color("#3d2817", "background")  # Dark floor background

# Draw background (floor)
c.rect(0, 0, 64, 64, background, fill=True)

# Draw table (top-down view) - centered, roughly 40x28 pixels
table_x, table_y = 12, 18
table_w, table_h = 40, 28

# Table legs (visible from top-down as corners)
# Left leg
c.rect(table_x - 3, table_y + 4, 4, 8, wood_dark, fill=True)
c.rect(table_x - 2, table_y + 5, 2, 6, wood_medium, fill=True)
# Right leg
c.rect(table_x + table_w - 1, table_y + 4, 4, 8, wood_dark, fill=True)
c.rect(table_x + table_w, table_y + 5, 2, 6, wood_medium, fill=True)
# Top leg
c.rect(table_x + 4, table_y - 3, 8, 4, wood_dark, fill=True)
c.rect(table_x + 5, table_y - 2, 6, 2, wood_medium, fill=True)
# Bottom leg
c.rect(table_x + 4, table_y + table_h - 1, 8, 4, wood_dark, fill=True)
c.rect(table_x + 5, table_y + table_h, 6, 2, wood_medium, fill=True)

# Table top surface
c.rect(table_x, table_y, table_w, table_h, table_surface, fill=True)

# Table edge highlight (top-left)
c.line(table_x + 1, table_y + 1, table_x + table_w - 2, table_y + 1, wood_light)
c.line(table_x + 1, table_y + 1, table_x + 1, table_y + table_h - 2, wood_light)

# Table edge shadow (bottom-right)
c.line(table_x + 2, table_y + table_h - 1, table_x + table_w - 1, table_y + table_h - 1, wood_dark)
c.line(table_x + table_w - 1, table_y + 2, table_x + table_w - 1, table_y + table_h - 2, wood_dark)

# Dark outline around table
c.line(table_x, table_y, table_x + table_w, table_y, dark_outline)  # Top
c.line(table_x, table_y + table_h, table_x + table_w, table_y + table_h, dark_outline)  # Bottom
c.line(table_x, table_y, table_x, table_y + table_h, dark_outline)  # Left
c.line(table_x + table_w, table_y, table_x + table_w, table_y + table_h, dark_outline)  # Right

# Draw 4 chairs around the table
# Chair 1 - Top (north)
chair1_x, chair1_y = table_x + 12, table_y - 12
# Chair back
c.rect(chair1_x, chair1_y, 16, 4, chair_wood, fill=True)
c.rect(chair1_x + 1, chair1_y + 1, 14, 2, chair_seat, fill=True)
# Chair seat
c.rect(chair1_x + 2, chair1_y + 4, 12, 6, chair_seat, fill=True)
c.rect(chair1_x + 3, chair1_y + 5, 10, 4, chair_wood, fill=True)
# Chair legs
c.rect(chair1_x + 3, chair1_y + 10, 2, 4, wood_dark, fill=True)
c.rect(chair1_x + 11, chair1_y + 10, 2, 4, wood_dark, fill=True)
# Outline
c.line(chair1_x, chair1_y, chair1_x + 16, chair1_y, dark_outline)
c.line(chair1_x, chair1_y, chair1_x, chair1_y + 4, dark_outline)
c.line(chair1_x + 16, chair1_y, chair1_x + 16, chair1_y + 4, dark_outline)

# Chair 2 - Bottom (south)
chair2_x, chair2_y = table_x + 12, table_y + table_h + 8
# Chair back
c.rect(chair2_x, chair2_y + 8, 16, 4, chair_wood, fill=True)
c.rect(chair2_x + 1, chair2_y + 9, 14, 2, chair_seat, fill=True)
# Chair seat
c.rect(chair2_x + 2, chair2_y + 2, 12, 6, chair_seat, fill=True)
c.rect(chair2_x + 3, chair2_y + 3, 10, 4, chair_wood, fill=True)
# Chair legs
c.rect(chair2_x + 3, chair2_y, 2, 4, wood_dark, fill=True)
c.rect(chair2_x + 11, chair2_y, 2, 4, wood_dark, fill=True)
# Outline
c.line(chair2_x, chair2_y + 8, chair2_x + 16, chair2_y + 8, dark_outline)
c.line(chair2_x, chair2_y + 8, chair2_x, chair2_y + 12, dark_outline)
c.line(chair2_x + 16, chair2_y + 8, chair2_x + 16, chair2_y + 12, dark_outline)

# Chair 3 - Left (west)
chair3_x, chair3_y = table_x - 12, table_y + 8
# Chair back (rotated)
c.rect(chair3_y, chair3_x, 4, 16, chair_wood, fill=True)
c.rect(chair3_y + 1, chair3_x + 1, 2, 14, chair_seat, fill=True)
# Chair seat
c.rect(chair3_y + 4, chair3_x + 2, 6, 12, chair_seat, fill=True)
c.rect(chair3_y + 5, chair3_x + 3, 4, 10, chair_wood, fill=True)
# Chair legs
c.rect(chair3_y + 10, chair3_x + 3, 4, 2, wood_dark, fill=True)
c.rect(chair3_y + 10, chair3_x + 11, 4, 2, wood_dark, fill=True)
# Outline
c.line(chair3_y, chair3_x, chair3_y + 4, chair3_x, dark_outline)
c.line(chair3_y, chair3_x, chair3_y, chair3_x + 16, dark_outline)
c.line(chair3_y + 4, chair3_x, chair3_y + 4, chair3_x + 16, dark_outline)

# Chair 4 - Right (east)
chair4_x, chair4_y = table_x + table_w + 8, table_y + 8
# Chair back (rotated)
c.rect(chair4_y, chair4_x, 4, 16, chair_wood, fill=True)
c.rect(chair4_y + 1, chair4_x + 1, 2, 14, chair_seat, fill=True)
# Chair seat
c.rect(chair4_y + 4, chair4_x + 2, 6, 12, chair_seat, fill=True)
c.rect(chair4_y + 5, chair4_x + 3, 4, 10, chair_wood, fill=True)
# Chair legs
c.rect(chair4_y + 10, chair4_x + 3, 4, 2, wood_dark, fill=True)
c.rect(chair4_y + 10, chair4_x + 11, 4, 2, wood_dark, fill=True)
# Outline
c.line(chair4_y, chair4_x, chair4_y + 4, chair4_x, dark_outline)
c.line(chair4_y, chair4_x, chair4_y, chair4_x + 16, dark_outline)
c.line(chair4_y + 4, chair4_x, chair4_y + 4, chair4_x + 16, dark_outline)

# Draw bowl of fruit on the table (center)
bowl_x, bowl_y = table_x + 14, table_y + 8
bowl_w, bowl_h = 12, 8

# Bowl base (oval shape using multiple rects for pixel art)
c.rect(bowl_x + 2, bowl_y + 2, 8, 4, bowl_white, fill=True)
c.rect(bowl_x + 1, bowl_y + 3, 10, 2, bowl_white, fill=True)
c.rect(bowl_x, bowl_y + 4, 12, 2, bowl_white, fill=True)

# Bowl rim
c.line(bowl_x, bowl_y + 4, bowl_x + 12, bowl_y + 4, bowl_shadow)
c.line(bowl_x + 1, bowl_y + 3, bowl_x + 11, bowl_y + 3, bowl_white)

# Bowl shadow/depth
c.set(bowl_x + 1, bowl_y + 5, bowl_shadow)
c.set(bowl_x + 10, bowl_y + 5, bowl_shadow)
c.set(bowl_x + 2, bowl_y + 5, bowl_shadow)
c.set(bowl_x + 9, bowl_y + 5, bowl_shadow)

# Bowl outline
c.line(bowl_x, bowl_y + 4, bowl_x + 12, bowl_y + 4, dark_outline)
c.line(bowl_x, bowl_y + 5, bowl_x, bowl_y + 6, dark_outline)
c.line(bowl_x + 12, bowl_y + 5, bowl_x + 12, bowl_y + 6, dark_outline)

# Draw fruits in the bowl
# Red apple
c.set(bowl_x + 3, bowl_y + 2, apple_red)
c.set(bowl_x + 4, bowl_y + 2, apple_red)
c.set(bowl_x + 3, bowl_y + 3, apple_red)
c.set(bowl_x + 4, bowl_y + 3, apple_highlight)
c.set(bowl_x + 4, bowl_y + 1, leaf_green)  # Stem

# Orange
c.set(bowl_x + 6, bowl_y + 2, orange_color)
c.set(bowl_x + 7, bowl_y + 2, orange_color)
c.set(bowl_x + 6, bowl_y + 3, orange_color)
c.set(bowl_x + 7, bowl_y + 3, orange_color)

# Banana (curved)
c.set(bowl_x + 8, bowl_y + 3, banana_yellow)
c.set(bowl_x + 9, bowl_y + 3, banana_yellow)
c.set(bowl_x + 9, bowl_y + 4, banana_yellow)

# Grapes (purple cluster)
c.set(bowl_x + 5, bowl_y + 4, grape_purple)
c.set(bowl_x + 6, bowl_y + 4, grape_light)
c.set(bowl_x + 5, bowl_y + 5, grape_purple)

# Add some cozy atmosphere - warm lighting effect on table
# Subtle gradient on table surface
for i in range(5):
    c.line(table_x + 5 + i, table_y + 5, table_x + 35 - i, table_y + 5, wood_light)

# Add wood grain texture to table
c.line(table_x + 8, table_y + 10, table_x + 32, table_y + 10, wood_dark)
c.line(table_x + 10, table_y + 15, table_x + 30, table_y + 15, wood_dark)
c.line(table_x + 6, table_y + 20, table_x + 34, table_y + 20, wood_dark)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 64, 64), indices=False))

finish(c)
