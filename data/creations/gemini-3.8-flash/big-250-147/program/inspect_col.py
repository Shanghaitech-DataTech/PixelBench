import numpy as np

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

# Let's inspect column 10 (which seems to be open sky from y=0 to y=60)
for y in range(0, 80, 5):
    print(f"x=10, y={y}: {arr[y, 10][:3].tolist()}")
