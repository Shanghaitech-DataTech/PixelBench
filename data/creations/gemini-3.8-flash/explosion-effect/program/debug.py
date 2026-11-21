# Check pixels near center of Frame 2
import numpy as np

# Let's inspect where grid <= 3
import main
for y in range(20, 45):
    for x in range(40, 60):
        val = main.grid[y, x]
        if 1 <= val <= 3:
            print(f"Dark pixel at ({x}, {y}) = {val}")
