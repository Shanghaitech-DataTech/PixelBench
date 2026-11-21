from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
for y in range(h):
    row = ''.join('#' if c.get(x,y)!=0 else '.' for x in range(w))
    print(f"{y:02d} {row}")
