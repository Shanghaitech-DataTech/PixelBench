from pixelbench_api import *
import numpy as np
import time

c = new_canvas(256, 256)
idx_red = c.color("#ff0000")
idx_blue = c.color("#0000ff")

t0 = time.time()
arr = np.full((256, 256), idx_blue, dtype=np.int32)
arr[50:100, 50:100] = idx_red
c.px[:] = arr.flatten().tolist()
print("Bulk assignment time:", time.time() - t0)
view(c)
