import numpy as np

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

# Let's inspect rows from top to bottom
# Let's print unique colors per row or gradient characteristics
for y in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]:
    row_colors = np.unique(arr[y, :, :3], axis=0)
    print(f"y={y}: {len(row_colors)} distinct colors; sample: {row_colors[:3].tolist()}")
