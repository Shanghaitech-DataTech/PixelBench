from pixelbench_api import *

# Create an output copy
output = input_canvas.copy(name='output')

# The durian has 3 flesh segments inside a rind (shell).
# The task is to remove the bottom segment to expose the rind underneath.

# Based on my analysis:
# - The bottom segment is in rows ~45-54
# - The rind interior color is 6 (cream, #fbf4c9)
# - The black outline (color 2) should be preserved

# I'll remove the bottom segment by replacing flesh colors with the rind interior color
# The bottom segment appears to be characterized by colors 7, 9, 5 in the lower portion

# Register the rind interior color (cream)
rind_color = output.color('#fbf4c9')  # color 6

# Remove the bottom segment by replacing flesh colors with rind interior
# The bottom segment is roughly in rows 45-54, between the black outline boundaries

for y in range(45, 56):
    for x in range(64):
        idx = output.get(x, y)
        # Keep background (1) and outline (2)
        # Replace flesh colors (7, 9, 5, and possibly others in the bottom segment) with rind color
        if idx in [7, 9, 5]:  # yellow, orange, brown - flesh colors in bottom segment
            output.set(x, y, rind_color)

# Also handle row 44 which might have some bottom segment pixels
for x in range(64):
    idx = output.get(x, 44)
    if idx in [7, 9, 5]:
        output.set(x, 44, rind_color)

print("Output stats:")
print(output.stats_text())

finish(output)
