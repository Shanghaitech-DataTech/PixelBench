# Comprehensive analysis of vending machine and character
pal = {entry['index']: entry['rgba'] for entry in input_canvas.palette()}

# Let's inspect the bounding box of the vending machine
# Vending machine top is around y=58 to 60.
# Let's find top-left, top-right, bottom-left, bottom-right corners of vending machine
print("Row 60:")
for x in range(80, 140):
    rgba = pal[input_canvas.get(x, 60)]
    if rgba[0] > 30 or rgba[2] > 50: # non-sky
        pass

# Let's print the colors of the vending machine:
# White luminous area:
# Let's find white/bright pixels:
bright = []
for y in range(60, 120):
    for x in range(85, 125):
        r, g, b, a = pal[input_canvas.get(x, y)]
        if r > 180 and g > 180 and b > 180: # white-ish interior
            bright.append((x, y))

if bright:
    min_x = min(p[0] for p in bright)
    max_x = max(p[0] for p in bright)
    min_y = min(p[1] for p in bright)
    max_y = max(p[1] for p in bright)
    print(f"Bright interior box approx: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")

# Let's look at the shelf structure on the right side of the interior (which is visible)
# x from 105 to 118:
for y in range(65, 115):
    line = ""
    for x in range(104, 120):
        r, g, b, a = pal[input_canvas.get(x, y)]
        # classify
        if r > 200 and g > 200 and b > 200:
            ch = "." # white light
        elif b > r + 30:
            ch = "B" # blue/purple
        elif g > r and g > b:
            ch = "G" # green
        elif r > g + 30:
            ch = "R" # red/brown
        elif r < 50 and g < 50 and b < 50:
            ch = "#" # dark
        else:
            ch = "+"
        line += ch
    # print every 2nd or all rows
    if y % 5 == 0:
        print(f"y={y:3d}: {line}")
