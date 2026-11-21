import time

c = new_canvas(256, 256)
t0 = time.time()
for y in range(50):
    for x in range(50):
        c.set(x, y, "#ff0000")
t1 = time.time()
print(f"50x50 c.set took: {t1 - t0:.4f}s")
