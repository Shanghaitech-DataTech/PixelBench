from pixelbench_api import input_canvas, new_canvas, canvas, canvases

c = input_canvas
print(c.stats_text())
print("size:", c.stats()["size"])

# Dump the palette
for p in c.palette():
    print(p)
