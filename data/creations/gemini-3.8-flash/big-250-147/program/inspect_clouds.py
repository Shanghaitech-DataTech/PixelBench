import numpy as np

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

cloud_color = np.array([132, 98, 132])
matches = np.all(arr[:, :, :3] == cloud_color, axis=-1)
ys, xs = np.where(matches)
print(f"Cloud color appears at y from {ys.min()} to {ys.max()}")
print(f"At y=0, count = {np.sum(matches[0, :])}")
print(f"At y=10, count = {np.sum(matches[10, :])}")
print(f"At y=25, count = {np.sum(matches[25, :])}")
print(f"At y=35, count = {np.sum(matches[35, :])}")
print(f"At y=45, count = {np.sum(matches[45, :])}")

# Let's inspect the vertical profile of the sky
print("\nMost common color per row in y < 65:")
for y in range(0, 65, 5):
    row = arr[y, :, :3]
    unique_row, counts_row = np.unique(row, axis=0, return_counts=True)
    best_idx = np.argmax(counts_row)
    print(f"y={y}: most common = {unique_row[best_idx].tolist()} ({counts_row[best_idx]} px)")
