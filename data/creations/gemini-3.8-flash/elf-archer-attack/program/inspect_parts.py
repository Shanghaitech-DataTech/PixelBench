from pixelbench_api import *

# Let's write a script to inspect input_canvas pixels and colors
# Let's inspect the exact bounding box and distribution
stats = input_canvas.stats()
print("Stats:", stats)

# Let's check non-transparent pixels in rows 0-15 (head/hair/quiver/top of bow)
# rows 16-25 (chest, arms, bow handle)
# rows 26-46 (lower body, legs, boots, bottom of bow)
