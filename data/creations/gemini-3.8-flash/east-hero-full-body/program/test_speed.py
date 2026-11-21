import time
from pixelbench_api import *

c = new_canvas(256, 256)
t0 = time.time()
# Test setting pixels
for y in range(50):
    for x in range(50):
        c.set(x, y, "#ff0000")
print("50x50 time:", time.time() - t0)
