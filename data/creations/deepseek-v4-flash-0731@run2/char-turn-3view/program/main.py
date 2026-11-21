from pixelbench_api import *

c = canvas(input_canvas)
for (y0, y1) in [(60, 89), (90, 118)]:
    print("=== rows", y0, "-", y1, "===")
    print(c.matrix_text(region=(0, y0, 65, y1), indices=False))
