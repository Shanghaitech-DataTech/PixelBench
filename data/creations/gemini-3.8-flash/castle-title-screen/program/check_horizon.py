from pixelbench_api import *
import main

c = canvas(-1)
print("Column check at x=31..45, y=72..80:")
for y in range(72, 81):
    row_str = "".join([c.color_name(c.get(x, y))[:4] for x in range(30, 46)])
    print(f"y={y}: {row_str}")
