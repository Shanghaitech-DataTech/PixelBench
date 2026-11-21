from pixelbench_api import *
from generate_icons import build_palette, paste_ascii

# Let's write a dedicated builder for the sword that ensures perfect symmetry and sharpness!
c = new_canvas(32, 32)
pal = build_palette(c)

# We can draw the sword grid directly
grid = [['.' for _ in range(32)] for _ in range(32)]

def set_px(x, y, ch):
    if 0 <= x < 32 and 0 <= y < 32:
        grid[y][x] = ch

# Centerline is from (27, 3) down to (6, 24)
# Blade from (27, 3) down to (15, 15)
# Guard around (14, 14)
# Grip from (13, 15) down to (8, 20)
# Pommel at (6, 22)

# Blade tip:
# (27, 2) is the very tip point!
grid[2][27] = 'k'
grid[3][27] = 'w'
grid[3][26] = 'h'
grid[4][27] = 's'
grid[2][26] = 'k'
grid[4][28] = 'k'
grid[3][28] = 'k'

# Blade steps: for i from 4 to 14:
# Center is (28 - i, i)
for i in range(4, 14):
    cx = 28 - i
    cy = i
    # Outline left:
    grid[cy - 1][cx - 1] = 'k'
    # Bright cutting edge:
    grid[cy][cx - 1] = 'h'
    # Highlight / fuller:
    grid[cy][cx] = 'l'
    # Shadow bevel:
    grid[cy + 1][cx] = 'm'
    grid[cy + 1][cx + 1] = 's'
    # Outline right:
    grid[cy + 2][cx + 1] = 'k'

# Let's check crossguard:
# Center is (14, 14) -> x+y=28.
# Up-left arm: (13,13), (12,12), (11,11), (10,10), (9,9), (8,8)
# Down-right arm: (15,15), (16,16), (17,17), (18,18), (19,19), (20,20)
# Let's draw guard, grip, pommel, print the ASCII representation, and view.

lines = ["".join(row) for row in grid]
for y, l in enumerate(lines[:16]):
    print(f"{y:2d}: {l}")

