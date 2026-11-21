# Create a copy to work on
output = input_canvas.copy(name='output')

# The fountain has water in the upper basin (colors c5, c6, c7 = indices 5, 6, 7)
# Water should cascade down from the basin edges

# Add water flowing down the left side of the fountain
# Starting from the upper basin edge around row 24-28
for y in range(26, 55):
    # Left cascade - following the fountain contour
    # The fountain gets wider as we go down, so water flows outward
    if y < 35:
        x_left = 18
    elif y < 45:
        x_left = 16 + (y - 35) // 5
    else:
        x_left = 14 + (y - 45) // 4
    
    # Add water stream
    if output.get(x_left, y) == 0:
        output.set(x_left, y, 6 if y % 2 == 0 else 5)
    if x_left + 1 < 64 and output.get(x_left + 1, y) == 0:
        output.set(x_left + 1, y, 5 if y % 2 == 0 else 6)

# Add water flowing down the right side
for y in range(26, 55):
    if y < 35:
        x_right = 46
    elif y < 45:
        x_right = 48 - (y - 35) // 5
    else:
        x_right = 50 - (y - 45) // 4
    
    if output.get(x_right, y) == 0:
        output.set(x_right, y, 6 if y % 2 == 1 else 5)
    if x_right - 1 >= 0 and output.get(x_right - 1, y) == 0:
        output.set(x_right - 1, y, 5 if y % 2 == 1 else 6)

# Add center water streams
for y in range(28, 52):
    cx = 32
    if output.get(cx - 1, y) == 0:
        output.set(cx - 1, y, 6)
    if output.get(cx, y) == 0:
        output.set(cx, y, 5)
    if output.get(cx + 1, y) == 0:
        output.set(cx + 1, y, 6)

# Add splash/foam where water hits middle tiers (around y=45-50)
for x in range(15, 25):
    if output.get(x, 47) == 0:
        output.set(x, 47, 4 if x % 3 == 0 else 6)
    if output.get(x, 48) == 0:
        output.set(x, 48, 6 if x % 2 == 0 else 5)

for x in range(40, 50):
    if output.get(x, 47) == 0:
        output.set(x, 47, 4 if x % 3 == 1 else 6)
    if output.get(x, 48) == 0:
        output.set(x, 48, 5 if x % 2 == 0 else 6)

# Add water pooling in lower basin (y=55-65)
for x in range(22, 43):
    for y in range(55, 68):
        if output.get(x, y) == 0:
            dist = abs(x - 32)
            water_top = 57 + min(dist // 2, 4)
            if y >= water_top and y < water_top + 4:
                output.set(x, y, 5 if (x + y) % 2 == 0 else 6)

# Add droplets falling
droplets = [
    (14, 50), (16, 54), (18, 58), (20, 62),
    (50, 50), (48, 54), (46, 58), (44, 62),
    (30, 55), (34, 55), (31, 60), (33, 60), (32, 65)
]
for dx, dy in droplets:
    if 0 <= dx < 64 and 0 <= dy < 76 and output.get(dx, dy) == 0:
        output.set(dx, dy, 6)

# Add spray at top spout
for x in range(28, 37):
    for y in range(5, 15):
        if output.get(x, y) == 0 and (x + y) % 5 == 0:
            output.set(x, y, 6)

# Add horizontal overflow from basin edges
for x in range(16, 24):
    if output.get(x, 26) == 0:
        output.set(x, 26, 6 if x % 2 == 0 else 5)
for x in range(41, 49):
    if output.get(x, 26) == 0:
        output.set(x, 26, 5 if x % 2 == 0 else 6)

print("Output stats:")
print(output.stats_text())

# Submit the result
finish(output)
