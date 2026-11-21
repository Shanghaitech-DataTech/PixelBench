from pixelbench_api import *
from PIL import Image
import numpy as np

arr = np.zeros((256, 256, 4), dtype=np.uint8)
arr[:, :, 0] = 50
arr[:, :, 1] = 80
arr[:, :, 2] = 100
arr[:, :, 3] = 255
# Red square
arr[100:150, 100:150, 0] = 220
arr[100:150, 100:150, 1] = 40
arr[100:150, 100:150, 2] = 40

img = Image.fromarray(arr, 'RGBA')
img.save('test_load.png')

c = load('test_load.png')
print("Loaded canvas:", c, "stats:", c.stats())
view(c)
