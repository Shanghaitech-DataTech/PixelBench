import numpy as np

arr = np.zeros((147, 250, 4), dtype=np.uint8)
palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

for y in range(147):
    for x in range(250):
        arr[y, x] = pal_dict[input_canvas.get(x, y)]

# Let's inspect the colors of:
# 1. Sky
# 2. Clouds
# 3. Sun
# 4. Mountains
# 5. Trees

# Sun mask:
sun_mask = (arr[:, :, 0] > 220) & (arr[:, :, 1] > 200) & (arr[:, :, 2] > 180)

# Let's find mountain skyline (transition from sky/cloud to mountain)
# Notice mountains have distinct RGB profiles compared to sky.
# Sky colors: generally R > 120, G around 90-110, B around 130-145 (purple/pink)
# Clouds: darker purple-gray, or pinkish highlights
# Mountains:
# Pink slope: R~212, G~122, B~132
# Shadow slopes of mountains: R around 40-84, G around 30-46, B around 52-76
# Trees: R around 20-28, G around 6-10, B around 4-12, highlights R around 68-120, G around 34-60, B around 28-40.

# Let's print out the exact color ranges for each region
print("Sample sky pixels (x=10, y=10):", arr[10, 10][:3].tolist())
print("Sample cloud pixels (x=100, y=25):", arr[25, 100][:3].tolist())
print("Sample pink mountain pixels (x=110, y=90):", arr[90, 110][:3].tolist())
print("Sample dark mountain pixels (x=50, y=100):", arr[100, 50][:3].tolist())
print("Sample tree pixels (x=50, y=130):", arr[130, 50][:3].tolist())
print("Sample tree highlight pixels (x=115, y=120):", arr[120, 115][:3].tolist())
