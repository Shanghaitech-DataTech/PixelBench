from pixelbench_api import *

# Let's inspect what colors are actually in the canvas
from main import build_title_prototype

c = build_title_prototype()
print("Pixel at (8, 8):", c.get(8, 8), c.color_name(c.get(8, 8)))
print("Pixel at (4, 4):", c.get(4, 4), c.color_name(c.get(4, 4)))
print("Pixel at (0, 0):", c.get(0, 0), c.color_name(c.get(0, 0)))
print("Stats:", c.stats())
