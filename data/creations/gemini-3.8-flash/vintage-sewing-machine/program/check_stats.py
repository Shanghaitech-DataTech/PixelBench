from pixelbench_api import *

# Let's inspect the current stats
from main import build_sewing_machine
c = build_sewing_machine()
stats = c.stats()
print("Colors used:", stats["colors_used"])
print("Visible pixels:", stats["visible_pixels"])
print("BBox:", stats["bbox"])
