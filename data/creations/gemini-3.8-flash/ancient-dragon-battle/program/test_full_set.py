import time

c = new_canvas(256, 256)
t0 = time.time()
for y in range(256):
    for x in range(256):
        c.set(x, y, "#12081c")
t1 = time.time()
print(f"256x256 c.set took: {t1 - t0:.4f}s")
