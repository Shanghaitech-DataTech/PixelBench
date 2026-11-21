# Let's inspect where different features are by analyzing rows y = 0 to 146
import numpy as np

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

# Find where the sun is:
sun_mask = (arr[:, :, 0] > 220) & (arr[:, :, 1] > 200) & (arr[:, :, 2] > 180)
sun_ys, sun_xs = np.where(sun_mask)
print(f"Sun bounding box: x in [{sun_xs.min()}, {sun_xs.max()}], y in [{sun_ys.min()}, {sun_ys.max()}]")
print(f"Sun center approx: cx = {(sun_xs.min() + sun_xs.max()) / 2}, cy = {(sun_ys.min() + sun_ys.max()) / 2}")
print(f"Sun diameter: dx = {sun_xs.max() - sun_xs.min() + 1}, dy = {sun_ys.max() - sun_ys.min() + 1}")

# Let's check what is behind or around the sun, and the structure of sky/clouds/mountains
