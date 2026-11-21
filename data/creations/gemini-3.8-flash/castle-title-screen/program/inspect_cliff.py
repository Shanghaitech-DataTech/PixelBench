from pixelbench_api import *

# Let's inspect the pixels along y=70, 80, 90, 100
# to see where the cliff edge actually is in main.py
import main

c = canvas(-1)
for y in [50, 60, 70, 80, 90, 100, 110]:
    edge = -1
    for x in range(128):
        col = c.get(x, y)
        name = c.color_name(col)
        # Check if it's cliff rim
        if name in ['#eb7734', '#fcae52', '#c44835', '#8f2939']:
            edge = x
            break
    print(f"y={y}: rim at x={edge}")
