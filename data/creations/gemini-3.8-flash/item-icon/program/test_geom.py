# Let's inspect circle geometry in python
import math

cx, cy = 15.5, 17.5
r = 11.8

grid = [["." for _ in range(32)] for _ in range(32)]
for y in range(32):
    for x in range(32):
        d = math.hypot(x - cx, y - cy)
        if d <= r:
            grid[y][x] = "#"

for row in grid:
    print("".join(row))
