from PIL import Image
import numpy as np

arr = np.zeros((256, 256, 4), dtype=np.uint8)
arr[:, :, 0] = 100
arr[:, :, 1] = 50
arr[:, :, 2] = 150
arr[:, :, 3] = 255

img = Image.fromarray(arr, 'RGBA')
img.save('test_load.png')

c = load('test_load.png')
print("Loaded canvas:", c, "colors:", c.stats()['colors_used'])
