from pixelbench_api import *

# The input canvas is 43x61 pixels
# Frame 1: Keep the original picture
f1 = input_canvas.copy(name='frame1')

# Frame 2: Create attack frame - start with a copy
f2 = input_canvas.copy(name='frame2')

# Register colors we need
white = f2.color('#ffffffff', name='white')
foot_orange = f2.color('#c67b02ff')  # v color
foot_brown = f2.color('#804018ff')   # s color  
foot_gold = f2.color('#ffe38cff')    # t color
foot_dark = f2.color('#332d32ff')    # u color

# For the heavy downward attack:
# 1. Weapon swings down - we'll move bright weapon pixels lower
# 2. White motion trail streams behind the weapon path
# 3. Left foot steps forward

# Step 1: Add motion trail (white streaks in an arc)
trail_positions = [
    (23, 20), (24, 21), (25, 22), (26, 23),
    (22, 21), (23, 22), (24, 23), (25, 24),
    (21, 22), (22, 23), (23, 24), (24, 25),
    (20, 24), (21, 25), (22, 26), (23, 27),
    (19, 26), (20, 27), (21, 28), (22, 29),
    (18, 28), (19, 29), (20, 30), (21, 31),
    (17, 30), (18, 31), (19, 32), (20, 33),
    (16, 32), (17, 33), (18, 34), (19, 35),
    (15, 34), (16, 35), (17, 36), (18, 37),
]

for x, y in trail_positions:
    if 0 <= x < 43 and 0 <= y < 61:
        f2.set(x, y, white)

# Step 2: Move the weapon down
# Move bright weapon pixels (E=white, J=yellow) down by ~12 pixels
weapon_to_move = []
for y in range(22, 36):
    for x in range(18, 32):
        c = f2.get(x, y)
        if c in [31, 36]:  # E (white), J (yellow)
            weapon_to_move.append((x, y, c))

for x, y, c in weapon_to_move:
    new_y = y + 12
    if new_y < 61:
        f2.set(x, y, None)
        f2.set(x, new_y, c)

# Move hilt (H=red, G=green)
hilt_to_move = []
for y in range(24, 32):
    for x in range(16, 28):
        c = f2.get(x, y)
        if c in [34, 33]:  # H, G
            hilt_to_move.append((x, y, c))

for x, y, c in hilt_to_move:
    new_y = y + 10
    new_x = x + 2
    if new_y < 61 and new_x < 43:
        f2.set(x, y, None)
        f2.set(new_x, new_y, c)

# Step 3: Adjust left foot - step it forward
# Instead of complex clearing, just add foot pixels in new position
# The left foot steps forward (down and right)

# Add new foot position without clearing - just overlay
new_foot_x, new_foot_y = 17, 54

# Draw foot stepping forward
f2.set(new_foot_x, new_foot_y, foot_orange)
f2.set(new_foot_x+1, new_foot_y, foot_orange)
f2.set(new_foot_x+2, new_foot_y, foot_brown)
f2.set(new_foot_x+3, new_foot_y, foot_dark)
f2.set(new_foot_x, new_foot_y-1, foot_gold)
f2.set(new_foot_x+1, new_foot_y-1, foot_orange)
f2.set(new_foot_x+2, new_foot_y-1, foot_orange)
f2.set(new_foot_x+3, new_foot_y-1, foot_brown)
f2.set(new_foot_x+1, new_foot_y-2, foot_brown)
f2.set(new_foot_x+2, new_foot_y-2, foot_gold)

# Also add some leg adjustment to show stepping - shift a few pixels down
# This creates the appearance of weight transfer
for offset in range(3):
    orig_x = 14 + offset
    orig_y = 51 + offset
    c = f2.get(orig_x, orig_y)
    if c is not None and c != 0:  # Not transparent
        # Add same color slightly lower to show movement
        f2.set(orig_x, orig_y + 3, c)

print("Frame 2 stats:")
print(f2.stats_text())

# Display key areas
print("\nWeapon/trail area (rows 18-48):")
print(f2.matrix_text(region=(12, 18, 40, 48)))

print("\nFeet area (rows 50-60):")
print(f2.matrix_text(region=(8, 50, 40, 60)))

# Submit the two frames
finish([f1, f2])
