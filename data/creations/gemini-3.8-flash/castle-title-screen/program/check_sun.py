from pixelbench_api import *
import main

c = canvas(-1)
# Inspect row 54 across the sun
row54 = [c.color_name(c.get(x, 54)) for x in range(20, 60)]
print("Row 54 (x=20..59):")
for i, col in enumerate(row54):
    print(f"x={20+i}: {col}")
