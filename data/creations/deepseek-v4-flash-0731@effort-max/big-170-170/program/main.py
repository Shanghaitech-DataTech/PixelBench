from pixelbench_api import *

c = input_canvas
# downsample 2x by reading top-left pixel of each 2x2 block
small = new_canvas(85, 85, name="small")
for y in range(85):
    for x in range(85):
        idx = c.get(x*2, y*2)
        small.set(x, y, idx)
print(small.matrix_text())
