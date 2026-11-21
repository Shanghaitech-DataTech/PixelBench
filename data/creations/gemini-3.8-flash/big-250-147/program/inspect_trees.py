import numpy as np

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

# Tree region: y >= 100
tree_highlights = []
for y in range(100, 147):
    for x in range(250):
        r, g, b, _ = arr[y, x]
        if r > 50 and b < 50:
            tree_highlights.append((r, g, b))

print("Found tree highlights:", len(tree_highlights))
if tree_highlights:
    print("Unique highlight colors:", np.unique(tree_highlights, axis=0))
