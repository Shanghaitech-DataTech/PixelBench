from pixelbench_api import *

c = input_canvas
for y in range(0, 22):
    row = [(x, c.get(x, y)) for x in range(27) if c.get(x, y) != 0]
    print(y, row)
