from pixelbench_api import *

# Let's inspect the tiers in input_canvas
# Tier 1 (top bowl):
# rim is at y=11..14
print("Tier 1 rim:")
for y in range(10, 15):
    print(f"y={y}:", "".join([f"{input_canvas.get(x, y):2d}" for x in range(16, 48)]))

print("\nTier 2 rim:")
for y in range(20, 25):
    print(f"y={y}:", "".join([f"{input_canvas.get(x, y):2d}" for x in range(10, 54)]))

print("\nTier 3 rim:")
for y in range(30, 35):
    print(f"y={y}:", "".join([f"{input_canvas.get(x, y):2d}" for x in range(8, 56)]))
