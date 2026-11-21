from pixelbench_api import *
from scene import build

c = build()

def bbox_of(hexname):
    xs, ys = [], []
    for y in range(64):
        for x in range(64):
            idx = c.get(x, y)
            if idx >= 0 and c.color_name(idx).startswith(hexname):
                xs.append(x); ys.append(y)
    if xs:
        return (min(xs), min(ys), max(xs), max(ys))
    return None

for name in ["#f0c040", "#d09a28", "#c04545", "#3f6fa8", "#4a3a2c", "#4f9a94", "#2a2d3a", "#2f5a52"]:
    print(name, bbox_of(name))
print(c.stats_text())
