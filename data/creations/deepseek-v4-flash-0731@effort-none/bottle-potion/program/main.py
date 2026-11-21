from pixelbench_api import *

c = canvas("input")

# Create output copy
out = c.copy(name='output')

# Map water colors to purple magic potion colors
dark_purple = out.color((100, 30, 170), 'dark_purple')
mid_purple = out.color((158, 72, 215), 'mid_purple')
light_purple = out.color((190, 120, 235), 'light_purple')
bubble_fill = out.color((225, 175, 250), 'bubble_fill')
bubble_edge = out.color((120, 40, 190), 'bubble_edge')

# Determine which pixels were originally water
water_pixels = set()
for y in range(64):
    for x in range(64):
        idx = c.get(x, y)
        if idx in [5, 6, 7, 8, 10]:
            water_pixels.add((x, y))

# Apply the color mapping
for y in range(64):
    for x in range(64):
        idx = out.get(x, y)
        if idx == 5:   # c4 dark blue -> dark purple
            out.set(x, y, dark_purple)
        elif idx == 6:  # c5 -> mid purple
            out.set(x, y, mid_purple)
        elif idx == 7:  # c6 -> light purple
            out.set(x, y, light_purple)
        elif idx == 8:  # c7 -> light purple
            out.set(x, y, light_purple)
        elif idx == 10: # c9 -> light purple
            out.set(x, y, light_purple)

# Helper to check if a circle would be entirely within water area
def circle_in_water(cx, cy, r):
    for dy in range(-r, r+1):
        for dx in range(-r, r+1):
            if dx*dx + dy*dy <= r*r:
                px, py = cx+dx, cy+dy
                if (px, py) not in water_pixels:
                    return False
    return True

# Draw filled bubbles inside the liquid
# Larger and more visible bubbles clustered in the main body of the liquid
bubble_filled = [
    (38, 50, 2), (28, 48, 2), (33, 44, 2), (42, 41, 2),
    (25, 39, 2), (36, 36, 2), (45, 34, 2), (30, 32, 2),
    (38, 29, 2), (22, 33, 2), (40, 53, 1), (18, 46, 1),
    (46, 44, 1), (24, 42, 1), (35, 39, 1), (27, 36, 1),
    (34, 32, 1), (42, 30, 1), (26, 28, 1), (20, 39, 1),
    (44, 37, 1), (32, 40, 1), (42, 46, 1), (30, 54, 1),
    (36, 55, 1), (22, 55, 1), (44, 52, 1), (28, 52, 1),
    (18, 51, 1), (47, 47, 1), (24, 46, 1), (41, 35, 1),
]

ring_bubbles = [
    (31, 46, 1), (40, 45, 1), (23, 37, 1), (36, 33, 1),
    (28, 30, 1), (20, 29, 1), (33, 38, 1), (25, 50, 1),
    (44, 49, 1), (37, 43, 1), (29, 41, 1), (31, 35, 1),
    (25, 33, 1), (40, 39, 1), (22, 42, 1), (35, 30, 1),
    (43, 30, 1), (26, 26, 1), (38, 52, 1), (46, 38, 1),
    (33, 27, 1), (17, 49, 1), (32, 53, 1), (41, 47, 1),
    (27, 44, 1), (34, 47, 1), (20, 36, 1), (44, 42, 1),
]

drawn = 0
for bx, by, br in bubble_filled:
    if circle_in_water(bx, by, br):
        out.circle(bx, by, br, bubble_fill, fill=True)
        drawn += 1

for bx, by, br in ring_bubbles:
    if circle_in_water(bx, by, br):
        out.circle(bx, by, br, bubble_edge, fill=False)
        drawn += 1

print(f"Drew {drawn} bubbles")

# Print the output matrix
print(out.matrix_text(region=(0,0,63,63), indices=False))

print(out.stats())
print(out.stats_text())

finish(out)
