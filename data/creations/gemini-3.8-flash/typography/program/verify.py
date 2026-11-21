from main import build_complete_title_screen
from pixelbench_api import *

c = build_complete_title_screen()
stats = c.stats()
print("Stats:", stats)
print("Colors used:", stats['colors_used'])
assert stats['colors_used'] <= 86, f"Too many colors: {stats['colors_used']}"
assert stats['size'] == [64, 64], f"Wrong size: {stats['size']}"
print("All assertions passed!")
