from pixelbench_api import *

# Create 16x16 canvas with transparent background
c = new_canvas(16, 16, background=None, name="jellyfish")

# Define colors for the glowing jellyfish
# Dark outline color (nearly black with blue tint)
outline = c.color("#0a0a2a")  # Very dark blue, almost black
# Main bell colors (darker to lighter for glow effect)
bell_dark = c.color("#2a2a5a")  # Dark purple-blue
bell_mid = c.color("#4a4a8a")   # Mid purple-blue  
bell_light = c.color("#6a6aaa")  # Light purple-blue
bell_glow = c.color("#8a8aca")  # Glowing purple-blue
bell_highlight = c.color("#aabaff")  # Very light blue with hint of purple
# Inner glow core
inner_glow = c.color("#9a9adc")  # Bright inner core
# Tentacle colors
tentacle_dark = c.color("#3a3a6a")
tentacle_light = c.color("#5a5a9a")

# Draw the jellyfish bell (rounded dome shape)
# Top of bell (row 1-2)
c.set(7, 1, outline)
c.set(8, 1, outline)
c.set(6, 2, outline)
c.set(7, 2, bell_light)
c.set(8, 2, bell_light)
c.set(9, 2, outline)

# Upper bell (row 3)
c.set(5, 3, outline)
c.set(6, 3, bell_mid)
c.set(7, 3, bell_highlight)
c.set(8, 3, bell_highlight)
c.set(9, 3, bell_mid)
c.set(10, 3, outline)

# Upper bell (row 4)
c.set(4, 4, outline)
c.set(5, 4, bell_dark)
c.set(6, 4, bell_mid)
c.set(7, 4, bell_glow)
c.set(8, 4, bell_glow)
c.set(9, 4, bell_mid)
c.set(10, 4, bell_dark)
c.set(11, 4, outline)

# Middle of bell (row 5) - start of widest part
c.set(3, 5, outline)
c.set(4, 5, bell_dark)
c.set(5, 5, bell_mid)
c.set(6, 5, bell_glow)
c.set(7, 5, inner_glow)
c.set(8, 5, inner_glow)
c.set(9, 5, bell_glow)
c.set(10, 5, bell_mid)
c.set(11, 5, bell_dark)
c.set(12, 5, outline)

# Middle of bell (row 6) - widest part
c.set(2, 6, outline)
c.set(3, 6, outline)
c.set(4, 6, bell_dark)
c.set(5, 6, bell_mid)
c.set(6, 6, bell_glow)
c.set(7, 6, bell_highlight)
c.set(8, 6, bell_highlight)
c.set(9, 6, bell_glow)
c.set(10, 6, bell_mid)
c.set(11, 6, bell_dark)
c.set(12, 6, outline)
c.set(13, 6, outline)

# Lower middle (row 7)
c.set(2, 7, outline)
c.set(3, 7, outline)
c.set(4, 7, bell_dark)
c.set(5, 7, bell_mid)
c.set(6, 7, bell_glow)
c.set(7, 7, bell_light)
c.set(8, 7, bell_light)
c.set(9, 7, bell_glow)
c.set(10, 7, bell_mid)
c.set(11, 7, bell_dark)
c.set(12, 7, outline)
c.set(13, 7, outline)

# Lower bell (row 8)
c.set(2, 8, outline)
c.set(3, 8, outline)
c.set(4, 8, bell_dark)
c.set(5, 8, bell_mid)
c.set(6, 8, bell_glow)
c.set(7, 8, bell_light)
c.set(8, 8, bell_light)
c.set(9, 8, bell_glow)
c.set(10, 8, bell_mid)
c.set(11, 8, bell_dark)
c.set(12, 8, outline)
c.set(13, 8, outline)

# Bell bottom curve (row 9)
c.set(2, 9, outline)
c.set(3, 9, outline)
c.set(4, 9, bell_dark)
c.set(5, 9, bell_mid)
c.set(6, 9, bell_glow)
c.set(7, 9, bell_glow)
c.set(8, 9, bell_glow)
c.set(9, 9, bell_mid)
c.set(10, 9, bell_dark)
c.set(11, 9, outline)
c.set(12, 9, outline)
c.set(13, 9, outline)

# Bell rim (row 10)
c.set(3, 10, outline)
c.set(4, 10, bell_dark)
c.set(5, 10, bell_mid)
c.set(6, 10, bell_glow)
c.set(7, 10, bell_light)
c.set(8, 10, bell_light)
c.set(9, 10, bell_glow)
c.set(10, 10, bell_mid)
c.set(11, 10, bell_dark)
c.set(12, 10, outline)

# Tentacles connection points (row 11)
c.set(4, 11, outline)
c.set(5, 11, bell_dark)
c.set(6, 11, tentacle_dark)
c.set(7, 11, bell_dark)
c.set(8, 11, bell_dark)
c.set(9, 11, tentacle_dark)
c.set(10, 11, bell_dark)
c.set(11, 11, outline)

# Tentacles (rows 12-15) - short and wavy
# Left tentacle
c.set(5, 12, outline)
c.set(6, 12, tentacle_dark)
c.set(5, 13, outline)
c.set(6, 13, tentacle_light)
c.set(5, 14, outline)
c.set(6, 14, tentacle_dark)
c.set(5, 15, tentacle_light)

# Middle-left tentacle
c.set(7, 12, tentacle_dark)
c.set(7, 13, tentacle_light)
c.set(8, 13, outline)
c.set(7, 14, tentacle_dark)
c.set(8, 14, outline)
c.set(7, 15, tentacle_light)

# Middle-right tentacle  
c.set(9, 12, tentacle_dark)
c.set(9, 13, tentacle_light)
c.set(8, 14, outline)
c.set(9, 14, tentacle_dark)
c.set(8, 15, outline)
c.set(9, 15, tentacle_light)

# Right tentacle
c.set(10, 12, outline)
c.set(11, 12, tentacle_dark)
c.set(11, 13, outline)
c.set(11, 14, tentacle_light)
c.set(11, 15, outline)
c.set(10, 15, tentacle_dark)

# Add subtle glow particles in the water
c.set(1, 6, bell_glow)
c.set(14, 7, bell_glow)
c.set(1, 10, bell_light)
c.set(14, 11, bell_light)

# Check stats
print(c.stats_text())
print(c.matrix_text())

# Submit the result
finish(c)
