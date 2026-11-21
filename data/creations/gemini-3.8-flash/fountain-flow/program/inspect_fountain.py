from pixelbench_api import *

# Let's inspect the fountain parts:
# Tier 1 (top bowl):
# What are its bounds and rows?
# Tier 2 (middle bowl):
# Tier 3 (lower bowl):
# Central pillar/stem:
# Ground basin:

# Let's print out the character map of columns 10 to 53 for all rows
for y in range(0, 76, 2):
    row_str = "".join([f"{input_canvas.get(x, y):2d}" if input_canvas.get(x, y) != 0 else " ." for x in range(10, 54)])
    print(f"y={y:2d}: {row_str}")
