from pixelbench_api import *

# Create a 48x48 canvas with transparent background
c = new_canvas(48, 48, background=None, name="slash_effect")

# Define colors - white for main slash, grays for trailing effect
white = c.color("#FFFFFF")
gray1 = c.color("#E0E0E0")
gray2 = c.color("#C0C0C0")
gray3 = c.color("#A0A0A0")

# Frame 1: Small arc slash (left half, x=0 to 23)
# Curved slash using quadratic bezier - dynamic arc from upper-left
c.path("M 5 6 Q 11 12 17 18", white, fill=False)

# Frame 2: Larger arc slash with trailing streak (right half, x=24 to 47)
# Main larger arc - more dramatic curve
c.path("M 28 5 Q 36 14 43 24", white, fill=False)

# Trailing streak - fading lines extending from arc end
c.line(43, 24, 42, 28, gray1)
c.line(42, 28, 41, 32, gray2)
c.line(41, 32, 40, 36, gray3)

# Add some extra detail to the main arcs for visual impact
# Small highlight dots along the arcs
c.set(8, 9, white)
c.set(14, 15, white)
c.set(32, 10, white)
c.set(38, 18, white)

print(c.stats_text())
print(c.matrix_text())

finish(c)
