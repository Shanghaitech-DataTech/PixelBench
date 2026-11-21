import numpy as np

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

# In sky region y < 80:
# Let's see what distinct color groups exist in y < 60
sky_pixels = arr[:60, :, :3].reshape(-1, 3)
unique_sky, counts = np.unique(sky_pixels, axis=0, return_counts=True)
# Sort by count
sorted_indices = np.argsort(-counts)
for i in sorted_indices[:20]:
    print(f"{unique_sky[i].tolist()}: {counts[i]} pixels")
