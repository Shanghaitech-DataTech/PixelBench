from pixelbench_api import *

# Create an output copy
output = input_canvas.copy(name='output')

# Register colors for the country road scene
sky_blue = output.color('#87CEEB', 'sky')
road_gray = output.color('#696969', 'road')
road_dark = output.color('#505050', 'road_dark')
grass_green = output.color('#228B22', 'grass')
grass_light = output.color('#32CD32', 'grass_light')
yellow_line = output.color('#FFD700', 'yellow_line')

# Replace white background with sky/grass/road, keeping motorcycle intact

# Draw sky at top (rows 0-25)
for y in range(0, 26):
    for x in range(64):
        if output.get(x, y) == 1:  # White background
            output.set(x, y, sky_blue)

# Draw grass/horizon area (rows 26-34)
for y in range(26, 35):
    for x in range(64):
        if output.get(x, y) == 1:
            if (x + y) % 5 == 0:
                output.set(x, y, grass_light)
            else:
                output.set(x, y, grass_green)

# Draw road from row 30 to bottom - centered with perspective
for y in range(30, 64):
    progress = (y - 30) / 34
    road_half_width = int(10 + progress * 12)
    center_x = 32
    
    for x in range(max(0, center_x - road_half_width), min(64, center_x + road_half_width)):
        if output.get(x, y) == 1:
            if x <= center_x - road_half_width + 1 or x >= center_x + road_half_width - 2:
                output.set(x, y, road_dark)
            else:
                output.set(x, y, road_gray)

# Add dashed yellow center line
for y in range(34, 64, 7):
    progress = (y - 30) / 34
    road_half_width = int(10 + progress * 12)
    center_x = 32
    for dy in range(min(3, 64 - y)):
        cx = center_x
        if 0 <= cx < 64:
            curr = output.get(cx, y + dy)
            if curr == output.color(road_gray) or curr == output.color(road_dark):
                output.set(cx, y + dy, yellow_line)

# Fill remaining white areas with grass
for y in range(30, 64):
    for x in range(64):
        if output.get(x, y) == 1:
            if (x + y) % 4 == 0:
                output.set(x, y, grass_light)
            else:
                output.set(x, y, grass_green)

print("Final output stats:", output.stats_text())

# Submit the result
finish(output)
