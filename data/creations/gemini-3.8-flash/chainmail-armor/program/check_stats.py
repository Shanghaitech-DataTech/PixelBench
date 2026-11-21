from generate_armor3 import build_armor_v3
from pixelbench_api import *

c = build_armor_v3()
print("Stats:", c.stats())
print("Unique colors:", len(c.palette()))
print("Visible pixels:", c.stats()['visible_pixels'])
