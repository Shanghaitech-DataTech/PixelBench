# -*- coding: utf-8 -*-
"""show: 1:1 matrix dumps of key regions"""
import sys
from drawing import build

c = build()
print(c.stats_text())
regions = {
    "sun": (74, 40, 120, 80),
    "lefthouse": (12, 78, 46, 100),
    "righthouse": (82, 80, 116, 104),
    "pathfoot": (40, 104, 92, 128),
    "horizon": (0, 82, 127, 96),
    "leftedge": (0, 70, 20, 128),
    "topsky": (0, 0, 60, 30),
}
keys = ["horizon", "leftedge"]
if len(sys.argv) > 1 and sys.argv[1] in regions:
    keys = [sys.argv[1]]
for k in keys:
    print(c.matrix_text(region=regions[k]))

