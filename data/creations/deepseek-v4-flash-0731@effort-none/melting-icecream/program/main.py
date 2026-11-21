from pixelbench_api import *

# Start fresh from the input
output = input_canvas.copy(name='output')

# The ice cream scoop is chocolate on top of a waffle cone.
# I'll make the chocolate melt and drip down the cone.
# Add vertical chocolate drip streams flowing from the scoop bottom down the cone.

# Chocolate colors: 5=[94,54,62], 6=[97,54,61], 13=[94,54,65], 18=[149,82,76]

# Main drips flowing down the cone:

# DRIP A: Left side of cone - from scoop bottom down the left face
for y in range(32, 38):
    for x in (22, 23):
        output.set(x, y, 5)
output.set(23, 38, 5)
output.set(24, 39, 5)
output.set(24, 40, 5)

# DRIP B: Center-left, extends down the cone
for y in range(32, 37):
    for x in (27, 28, 29):
        output.set(x, y, 5)
for y in range(37, 40):
    output.set(28, y, 5)
    output.set(29, y, 5)
output.set(29, 41, 5)

# DRIP C: Center of the cone - long flow
for y in range(31, 36):
    for x in (33, 34, 35, 36):
        output.set(x, y, 5)
for y in range(36, 40):
    for x in (34, 35):
        output.set(x, y, 5)
output.set(35, 41, 5)
output.set(35, 42, 5)
output.set(35, 43, 5)

# DRIP D: Center-right, main dramatic drip going far down
for y in range(31, 42):
    if y < 37:
        for x in (38, 39, 40, 41, 42):
            output.set(x, y, 5)
    elif y < 44:
        for x in (38, 39, 40):
            output.set(x, y, 5)
    elif y < 47:
        for x in (39, 40):
            output.set(x, y, 5)
    else:
        output.set(40, y, 5)
# rounded droplet tip
output.set(39, 47, 5)
output.set(41, 47, 5)
output.set(40, 48, 5)

# DRIP E: Right side of the cone
for y in range(32, 39):
    for x in (43, 44, 45):
        output.set(x, y, 5)
for y in range(39, 41):
    output.set(44, y, 5)
output.set(44, 42, 5)
output.set(43, 43, 5)
output.set(43, 44, 5)

# DRIP F: Far left, small drip
for y in range(32, 35):
    output.set(20, y, 5)
output.set(21, y, 5) if y == 34 else None
output.set(20, 36, 5)
output.set(19, 36, 5)

# Add shading for depth - darker edges
# DRIP D shading
for y in range(33, 46):
    output.set(38, y, 6)
for y in range(33, 44):
    output.set(42, y, 13)
# DRIP C shading
for y in range(33, 38):
    output.set(33, y, 6)
    output.set(36, y, 13)
# DRIP A shading
for y in range(33, 37):
    output.set(22, y, 6)
# DRIP B shading
for y in range(33, 38):
    output.set(27, y, 13)
# DRIP E shading
for y in range(33, 40):
    output.set(45, y, 6)

# Add highlights for a wet look
for y in range(33, 40):
    output.set(40, y, 18)
for y in range(33, 36):
    output.set(35, y, 18)
for y in range(34, 38):
    output.set(29, y, 18)
for y in range(34, 37):
    output.set(24, y, 6)

# Add a few individual chocolate droplets on the cone
droplet_spots = [
    (26, 38), (26, 39), (31, 37), (37, 38), (37, 39),
    (32, 36), (33, 42), (37, 42), (42, 44), (43, 45),
    (25, 41), (30, 42), (36, 45), (42, 47),
]
for (x, y) in droplet_spots:
    output.set(x, y, 5)

# Also make the scoop's bottom edge look slightly melty/wavy by
# adding a few chocolate pixels just below the existing scoop line
melt_rim = [
    # Various extension points
    (19, 32), (24, 32), (25, 32), (26, 32), (29, 32), 
    (30, 32), (31, 32), (32, 32), (37, 32), (41, 32),
    (42, 32), (46, 32), (46, 33), (24, 33), (25, 33),
    (47, 33), (47, 34), (31, 34), (26, 34),
]
for (x, y) in melt_rim:
    output.set(x, y, 5)

finish(output)
