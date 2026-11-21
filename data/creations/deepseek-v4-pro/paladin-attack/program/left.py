from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
for (x0,y0,x1,y1) in [(0,26,16,36),(14,20,28,30),(28,18,42,26),(15,6,30,13)]:
    print(f"=== region {x0},{y0} - {x1},{y1} ===")
    print(c.matrix_text(region=(x0,y0,x1,y1), indices=False))
