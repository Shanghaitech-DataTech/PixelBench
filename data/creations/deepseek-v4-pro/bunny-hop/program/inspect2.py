from pixelbench_api import *

c = input_canvas
print(c.matrix_text(indices=True))
print("--- pixels by color ---")
from collections import defaultdict
d = defaultdict(list)
for y in range(28):
    for x in range(26):
        idx = c.get(x, y)
        if idx != 0:
            d[idx].append((x, y))
for idx, pts in sorted(d.items()):
    print("idx", idx, c.color_name(idx), "count", len(pts))
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    print("  x range", min(xs), max(xs), "y range", min(ys), max(ys))
