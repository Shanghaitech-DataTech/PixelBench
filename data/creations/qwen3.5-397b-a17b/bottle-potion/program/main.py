from pixelbench_api import *

# Create an editable copy
output = input_canvas.copy(name='output')

# Register colors for the potion
purple_dark = output.color('#6a3d9a')  # Dark purple for main potion
purple_mid = output.color('#9b59b6')   # Medium purple
purple_light = output.color('#be93d4') # Light purple for highlights
bubble_color = output.color('#d8a7e8') # Very light purple for bubbles
sparkle = output.color('#ffffff')      # White sparkles

# Get canvas dimensions from stats
stats = output.stats()
width, height = stats['size']

# Replace water colors with purple variants
for y in range(height):
    for x in range(width):
        idx = output.get(x, y)
        if idx == 5:  # c4 - main water
            output.set(x, y, purple_dark)
        elif idx == 6:  # c5 - highlight
            output.set(x, y, purple_mid)
        elif idx == 7:  # c6 - highlight
            output.set(x, y, purple_light)
        elif idx == 8:  # c7 - highlight
            output.set(x, y, purple_light)
        elif idx == 10:  # c9 - highlight
            output.set(x, y, purple_light)

# Add bubbles - small circles in the liquid area
bubble_positions = [
    (20, 30, 2), (35, 28, 3), (45, 35, 2), (25, 40, 2),
    (40, 42, 3), (30, 45, 2), (50, 38, 2), (15, 35, 1),
    (55, 45, 2), (22, 50, 2), (38, 32, 1), (48, 48, 2),
    (28, 38, 2), (42, 26, 2), (33, 44, 1), (18, 42, 2),
    (52, 30, 1), (25, 33, 2), (45, 40, 2), (35, 48, 2)
]

for bx, by, br in bubble_positions:
    if 0 <= bx < width and 0 <= by < height:
        output.circle(bx, by, br, bubble_color, fill=True)

# Add some white sparkles for magic effect
sparkle_positions = [
    (28, 35), (42, 30), (35, 42), (22, 45), (48, 38),
    (30, 28), (45, 45), (25, 48), (38, 36), (20, 40)
]

for sx, sy in sparkle_positions:
    if 0 <= sx < width and 0 <= sy < height:
        output.set(sx, sy, sparkle)
        if sx > 0: output.set(sx-1, sy, sparkle)
        if sx < width-1: output.set(sx+1, sy, sparkle)
        if sy > 0: output.set(sx, sy-1, sparkle)
        if sy < height-1: output.set(sx, sy+1, sparkle)

# Submit the result
finish(output)
