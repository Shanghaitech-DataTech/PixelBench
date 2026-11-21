output = input_canvas.copy(name="output")

c5_idx = output.color("#fbf4c9")

# Pixels of the bottom segment of durian flesh:
bottom_segment_pixels = []

# Row 37 to 48: left of Crease 2
crease2_x = {
    37: 25,
    38: 25,
    39: 25,
    40: 25,
    41: 25,
    42: 27,
    43: 27,
    44: 29,
    45: 28,
    46: 29,
    47: 32,
    48: 32,
}

for y, max_x in crease2_x.items():
    for x in range(0, max_x):
        if output.get(x, y) in (7, 8, 9):  # flesh colors
            bottom_segment_pixels.append((x, y))

# Rows 49 to 51: bottom lobe pixels inside the carpel
for y in (49, 50, 51):
    for x in range(0, 35):
        if output.get(x, y) in (7, 8, 9):
            bottom_segment_pixels.append((x, y))

# Replace bottom segment flesh with rind (c5)
for x, y in bottom_segment_pixels:
    output.set(x, y, c5_idx)

view(output)
finish(output)
