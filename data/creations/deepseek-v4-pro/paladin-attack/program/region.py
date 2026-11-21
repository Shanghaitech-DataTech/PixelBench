from pixelbench_api import *

c = input_canvas
for (x0,y0,x1,y1) in [(22,4,32,14),(30,14,42,22),(15,19,30,24),(8,26,20,34),(25,24,37,34)]:
    print(f"=== region {x0},{y0} - {x1},{y1} ===")
    print(c.matrix_text(region=(x0,y0,x1,y1), indices=False))
