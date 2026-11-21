import time

c = new_canvas(256, 256)
t0 = time.time()
for y in range(256):
    for x in range(256):
        c.set(x, y, "#101020")
t1 = time.time()
print(f"Filled 256x256 in {t1 - t0:.3f}s")
