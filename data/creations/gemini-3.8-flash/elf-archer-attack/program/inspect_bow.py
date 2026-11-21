from pixelbench_api import *

# Let's inspect the bow pixels in input_canvas
# Bow is roughly in cols 22-34
for y in range(47):
    row_str = ""
    for x in range(22, 35):
        c = input_canvas.get(x, y)
        if c == 0:
            row_str += " ."
        else:
            row_str += f"{c:2d}"
    print(f"y={y:2d}: {row_str}")
