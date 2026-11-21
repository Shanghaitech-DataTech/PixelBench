from pixelbench_api import new_canvas, finish

# Create a 16x16 canvas for the wooden key
c = new_canvas(16, 16, name="wooden_key")

# Define color palette (max 6 colors for detective game aesthetic)
# Dark to light browns for wood texture
darkest = c.color('#2a1810')  # deepest shadows/outline
dark_brown = c.color('#4a2c1a')  # shadow wood
medium_brown = c.color('#6b3d23')  # main wood body
light_brown = c.color('#8b5a3a')  # highlighted wood
tan = c.color('#b8865b')  # bright highlights
pale = c.color('#d4a57a')  # brightest specular

# Draw wooden key - classic skeleton key shape made of wood

# Key bow (handle) - circular top part
# Outer ring
c.circle(8, 5, 3, dark_brown, fill=True)
# Inner hole (transparent)
c.circle(8, 5, 1, None, fill=True)
# Highlight on bow
c.set(7, 3, tan)
c.set(8, 3, pale)
c.set(9, 4, light_brown)

# Key shaft (stem) - vertical part connecting bow to bit
c.rect(7, 8, 2, 6, medium_brown, fill=True)
# Shaft highlights (wood grain effect)
c.set(7, 9, light_brown)
c.set(8, 10, tan)
c.set(7, 11, light_brown)
c.set(8, 12, tan)
# Shaft edges
c.set(7, 8, dark_brown)
c.set(8, 8, dark_brown)
c.set(7, 13, dark_brown)
c.set(8, 13, dark_brown)

# Key bit (the part that enters the lock) - horizontal teeth
c.rect(6, 14, 4, 2, medium_brown, fill=True)
# Bit teeth details
c.set(6, 15, dark_brown)
c.set(9, 15, dark_brown)
c.set(7, 14, light_brown)
c.set(8, 14, tan)

# Add wood grain texture on bow
c.set(6, 5, light_brown)
c.set(10, 5, light_brown)
c.set(7, 6, tan)
c.set(9, 6, tan)

# Outline/shadow for depth
c.set(6, 5, dark_brown)
c.set(10, 5, dark_brown)
c.set(5, 8, darkest)
c.set(9, 8, darkest)
c.set(5, 14, darkest)

# Check our work
print(c.stats_text())
print(c.matrix_text())

finish(c)
