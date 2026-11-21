from pixelbench_api import new_canvas, finish

# Create 16x16 canvas
c = new_canvas(16, 16)

# Define colors (max 6 including transparent)
# 1. Dark gold/brown - outline
dark_gold = c.color((139, 90, 43), "dark_gold")
# 2. Gold - main coin
gold = c.color((218, 165, 32), "gold")
# 3. Light gold - highlight
light_gold = c.color((255, 215, 0), "light_gold")
# 4. Bright yellow - star
star_yellow = c.color((255, 255, 100), "star_yellow")
# 5. Darker gold - shadow/depth
shadow_gold = c.color((184, 134, 11), "shadow_gold")

# Draw the coin as a circle (center at 8,8, radius 7)
# Using filled circle for the base
c.circle(8, 8, 7, gold, fill=True)

# Add outline/darker edge
c.circle(8, 8, 7, dark_gold, fill=False)

# Add inner ring for depth
c.circle(8, 8, 6, shadow_gold, fill=False)

# Add highlight on top-left
c.circle(6, 6, 4, light_gold, fill=True)

# Draw a 5-pointed star in the center
# Star points (approximate for 16x16, centered at 8,8)
# Using a simple star pattern
star_points = [
    (8, 4),   # top
    (9, 7),   # upper right
    (12, 7),  # right
    (10, 9),  # lower right
    (11, 12), # bottom right
    (8, 10),  # bottom
    (5, 12),  # bottom left
    (6, 9),   # lower left
    (4, 7),   # left
    (7, 7),   # upper left
]
c.poly(star_points, star_yellow, fill=True)

# Add small highlight dots on the star
c.set(8, 7, light_gold)
c.set(7, 8, light_gold)

print(c.stats_text())
print(c.matrix_text())

finish(c)
