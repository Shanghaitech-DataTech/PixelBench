# -*- coding: utf-8 -*-
"""inspect regions of the saved drawing"""
import sys
from pixelbench_api import load

c = load("exports/mvs.pixelart.json", add=False)
regions = {
    "houses": (14, 70, 114, 110),
    "path": (60, 95, 127, 127),
    "sun": (70, 30, 127, 92),
    "left": (0, 60, 64, 127),
    "sky": (0, 0, 63, 45),
    "full": (0, 0, 127, 127),
}
which = sys.argv[1] if len(sys.argv) > 1 else "houses"
print(c.matrix_text(region=regions[which]))
