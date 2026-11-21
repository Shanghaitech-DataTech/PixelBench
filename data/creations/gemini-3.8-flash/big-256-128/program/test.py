import time

output = input_canvas.copy(name='output')
t0 = time.time()
pal = output.palette()
print(f"Palette length: {len(pal)}")
# print some palette colors
for i, entry in enumerate(pal[:15]):
    print(i, entry)

# test reading all pixels
w, h = 256, 128
pixels = [output.get(x, y) for y in range(h) for x in range(w)]
print(f"Read 32768 pixels in {time.time() - t0:.3f}s")
