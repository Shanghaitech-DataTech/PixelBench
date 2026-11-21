import numpy as np
from PIL import Image

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

# Let's save arr as PNG so we can analyze or inspect its features
# Let's inspect the distinct regions by color clustering or connected components
print("Array shape:", arr.shape)

# Let's inspect unique RGBs
unique_rgbs = np.unique(arr[:, :, :3].reshape(-1, 3), axis=0)
print("Total unique RGB colors:", len(unique_rgbs))
