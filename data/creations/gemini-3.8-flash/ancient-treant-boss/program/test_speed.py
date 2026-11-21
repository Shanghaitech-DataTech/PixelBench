import time
c = new_canvas(256, 256, background="#000000")
t0 = time.time()
for y in range(256):
    for x in range(256):
        if (x + y) % 2 == 0:
            c.set(x, y, "#ffffff")
t1 = time.time()
print(f"Elapsed: {t1 - t0:.3f}s")
finish(c)
