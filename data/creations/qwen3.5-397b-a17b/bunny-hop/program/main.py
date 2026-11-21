from pixelbench_api import *

# Both frames need to be the same size
canvas_w, canvas_h = 45, 35

# Frame 1: Original image centered in larger canvas
frame1 = new_canvas(canvas_w, canvas_h, background=None, name='frame1')

# Get input dimensions
input_w, input_h = 26, 28

# Center the input image in frame1
offset_x = (canvas_w - input_w) // 2
offset_y = (canvas_h - input_h) // 2

# Copy input to frame1
for y in range(input_h):
    for x in range(input_w):
        color_idx = input_canvas.get(x, y)
        if color_idx != -1:
            palette = input_canvas.palette()
            rgba = palette[color_idx]['rgba']
            col = frame1.color(tuple(rgba))
            frame1.set(x + offset_x, y + offset_y, col)

# Frame 2: Rabbit in mid-leap pose
frame2 = new_canvas(canvas_w, canvas_h, background=None, name='frame2')

# Register colors
col_outline = frame2.color('#3a3737', 'outline')
col_light = frame2.color('#b7b3b2', 'light')
col_medium = frame2.color('#827c7c', 'medium')
col_body = frame2.color('#efe9e7', 'body')
col_tan = frame2.color('#d6b39d', 'tan')
col_tan2 = frame2.color('#bc8b6d', 'tan2')
col_yellow = frame2.color('#cdae67', 'yellow')

# Draw a leaping rabbit - draw outline on transparent pixels adjacent to body

# First, draw all body pixels
body_pixels = []

# Back legs and feet
for x in range(5, 13):
    body_pixels.append((x, 24))
    body_pixels.append((x, 25))

# Lower back leg
for x in range(10, 15):
    for y in range(20, 24):
        body_pixels.append((x, y))

# Back thigh
for x in range(13, 18):
    for y in range(16, 20):
        body_pixels.append((x, y))

# Tail
body_pixels.append((4, 21))
body_pixels.append((5, 21))
body_pixels.append((6, 21))

# Body - main stretched portion
for x in range(16, 28):
    for y in range(14, 20):
        body_pixels.append((x, y))

# Front legs
for x in range(27, 30):
    for y in range(15, 21):
        body_pixels.append((x, y))

# Lower front leg
for x in range(29, 31):
    for y in range(20, 24):
        body_pixels.append((x, y))

# Front paw (tan) - separate list
tan_pixels = []
for x in range(30, 34):
    for y in range(24, 26):
        tan_pixels.append((x, y))

# Chest
for x in range(26, 28):
    for y in range(13, 16):
        body_pixels.append((x, y))

# Neck
for x in range(28, 31):
    for y in range(10, 14):
        body_pixels.append((x, y))

# Head
for x in range(30, 37):
    for y in range(8, 14):
        body_pixels.append((x, y))

# Ears
for x in range(31, 37):
    for y in range(5, 8):
        body_pixels.append((x, y))

# Second ear
for x in range(32, 36):
    body_pixels.append((x, 4))

# Draw body pixels
for x, y in body_pixels:
    frame2.set(x, y, col_body)

# Draw tan pixels
for x, y in tan_pixels:
    frame2.set(x, y, col_tan)

# Now add outline on transparent pixels adjacent to body/tan
all_filled = set(body_pixels) | set(tan_pixels)

outline_pixels = set()
for x, y in all_filled:
    # Check all 8 neighbors
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < canvas_w and 0 <= ny < canvas_h:
                if (nx, ny) not in all_filled:
                    outline_pixels.add((nx, ny))

# Draw outline
for x, y in outline_pixels:
    frame2.set(x, y, col_outline)

# Add eye
frame2.set(33, 10, col_yellow)
frame2.set(34, 10, col_medium)

# Add nose (already tan, but make sure it's visible)
# Nose is part of the tan paw area, need to add it to head
frame2.set(36, 11, col_tan)
frame2.set(36, 12, col_tan)

# Body shading
frame2.set(18, 14, col_light)
frame2.set(21, 14, col_light)
frame2.set(24, 14, col_light)

print("Frame 1 stats:", frame1.stats_text())
print("Frame 2 stats:", frame2.stats_text())
print("Frame 2 matrix:")
print(frame2.matrix_text(region=(2, 2, 42, 28)))

finish([frame1, frame2])
