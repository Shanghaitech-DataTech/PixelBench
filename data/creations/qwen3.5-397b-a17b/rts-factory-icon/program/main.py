from pixelbench_api import new_canvas, finish

# Create a 32x32 canvas for the RTS factory icon
c = new_canvas(32, 32, name="factory")

# Define color palette (keeping under 86 colors)
# Brick colors
brick_dark = c.color("#5a4a3a", "brick_dark")
brick_mid = c.color("#7a6a5a", "brick_mid")
brick_light = c.color("#9a8a7a", "brick_light")

# Roof colors
roof_dark = c.color("#4a4a4a", "roof_dark")
roof_mid = c.color("#6a6a6a", "roof_mid")
roof_light = c.color("#8a8a8a", "roof_light")

# Chimney colors
chimney_dark = c.color("#5a5a5a", "chimney_dark")
chimney_mid = c.color("#7a7a7a", "chimney_mid")

# Vent colors
vent_dark = c.color("#3a3a3a", "vent_dark")
vent_mid = c.color("#5a5a5a", "vent_mid")

# Highlight/accent
highlight = c.color("#baaa9a", "highlight")
shadow = c.color("#2a2a2a", "shadow")

# Smoke
smoke = c.color("#aaaaaa", "smoke")

# Draw the main building body (brick walls)
# Building spans from x=4 to x=28, y=12 to y=28
for y in range(12, 29):
    for x in range(4, 29):
        # Create brick pattern
        brick_row = (y - 12) % 4
        brick_col = (x - 4) % 6
        if brick_row == 0:
            c.set(x, y, brick_dark)
        elif brick_row == 1:
            c.set(x, y, brick_mid)
        elif brick_row == 2:
            c.set(x, y, brick_light)
        else:
            c.set(x, y, brick_mid)

# Add brick mortar lines (darker)
for y in range(12, 29, 4):
    for x in range(4, 29):
        c.set(x, y, shadow)

for x in range(4, 29, 6):
    for y in range(12, 29):
        c.set(x, y, shadow)

# Draw flat roof (y=8 to y=11)
for y in range(8, 12):
    for x in range(3, 30):
        if y == 8:
            c.set(x, y, roof_light)
        elif y == 9:
            c.set(x, y, roof_mid)
        else:
            c.set(x, y, roof_dark)

# Roof edge highlight
for x in range(3, 30):
    c.set(x, 7, highlight)

# Draw chimney (left side of roof)
# Chimney from y=2 to y=8, x=8 to x=13
for y in range(2, 9):
    for x in range(8, 14):
        if x == 8 or x == 13:
            c.set(x, y, chimney_dark)
        elif y == 2:
            c.set(x, y, chimney_mid)
        else:
            c.set(x, y, chimney_mid)

# Chimney top
for x in range(7, 15):
    c.set(x, 1, chimney_dark)
    c.set(x, 2, chimney_mid)

# Smoke from chimney
c.set(10, 0, smoke)
c.set(11, 0, smoke)
c.set(9, 1, smoke)
c.set(12, 1, smoke)

# Draw vents on the building
# Vent 1 (left side)
for y in range(16, 20):
    for x in range(7, 13):
        if y == 16 or y == 19:
            c.set(x, y, vent_dark)
        elif x == 7 or x == 12:
            c.set(x, y, vent_dark)
        else:
            c.set(x, y, vent_mid)
# Vent slats
for x in range(8, 12):
    c.set(x, 17, vent_dark)
    c.set(x, 18, vent_dark)

# Vent 2 (right side)
for y in range(22, 26):
    for x in range(20, 26):
        if y == 22 or y == 25:
            c.set(x, y, vent_dark)
        elif x == 20 or x == 25:
            c.set(x, y, vent_dark)
        else:
            c.set(x, y, vent_mid)
# Vent slats
for x in range(21, 25):
    c.set(x, 23, vent_dark)
    c.set(x, 24, vent_dark)

# Add windows
# Window 1
for y in range(14, 18):
    for x in range(16, 22):
        if y == 14 or y == 17:
            c.set(x, y, shadow)
        elif x == 16 or x == 21:
            c.set(x, y, shadow)
        else:
            c.set(x, y, "#4a5a6a")

# Window 2
for y in range(24, 28):
    for x in range(10, 16):
        if y == 24 or y == 27:
            c.set(x, y, shadow)
        elif x == 10 or x == 15:
            c.set(x, y, shadow)
        else:
            c.set(x, y, "#4a5a6a")

# Add ground shadow
for x in range(3, 30):
    c.set(x, 29, shadow)
    c.set(x, 30, "#1a1a1a")

# Outline for clean silhouette
c.outline(shadow)

# Check stats
print(c.stats_text())

# Submit the result
finish(c)
