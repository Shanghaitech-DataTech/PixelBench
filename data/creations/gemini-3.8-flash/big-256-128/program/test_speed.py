import time

c = new_canvas(256, 128)
t0 = time.time()
for y in range(128):
    for x in range(256):
        c.set(x, y, (20, 10, 15, 255))
print(f"Set 32768 pixels took: {time.time() - t0:.3f}s")
