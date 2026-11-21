from pixelbench_api import new_canvas, finish

# Create 32x32 canvas
c = new_canvas(32, 32)

# Define colors (7 max including transparency)
# 1. Transparent (background)
# 2. Dark green (shadow)
dark_green = c.color('#1a4d0f')
# 3. Medium green (main body)
medium_green = c.color('#4a8f2a')
# 4. Light green (highlight)
light_green = c.color('#7ab84f')
# 5. Yellow-green (bright highlight)
yellow_green = c.color('#a8d67a')
# 6. Brown (stem)
brown = c.color('#8b5a2b')
# 7. Dark brown (stem detail)
dark_brown = c.color('#5c3a1a')

# Draw pear shape using ellipses and filling
# Main body - bottom bulb (wider part)
c.ellipse(16, 21, 9, 8, medium_green, fill=True)

# Top part (narrower)
c.ellipse(16, 13, 6, 5, medium_green, fill=True)

# Connect the two parts
c.rect(13, 16, 6, 5, medium_green, fill=True)

# Shading on left/bottom side (darker)
c.ellipse(15, 22, 7, 6, dark_green, fill=True)

# Highlight on upper right (lighter)
c.ellipse(18, 18, 5, 4, light_green, fill=True)

# Bright specular highlight
c.ellipse(19, 16, 3, 2, yellow_green, fill=True)

# Draw stem
c.line(16, 8, 16, 11, brown)
c.set(16, 7, brown)
c.set(15, 9, dark_brown)

# Print stats to verify
print(c.stats_text())

# Submit the canvas
finish(c)
