from pixelbench_api import *

# Let's inspect Frame 1 coordinates closely around the torso and head
# to see where every feature is located.
print("Frame 1 (dx=5):")
for y in range(10, 26):
    row = ""
    for x in range(5, 42):
        c = input_canvas.get(x - 5, y) if (0 <= x - 5 < 35 and 0 <= y < 47) else 0
        row += f"{c:2d} " if c > 0 else " . "
    print(f"y={y:2d}: {row}")
