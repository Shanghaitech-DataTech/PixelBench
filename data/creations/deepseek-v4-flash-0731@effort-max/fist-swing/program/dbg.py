from pixelbench_api import *

c = input_canvas
W, H = 29, 44
print("cols:", "".join(str(i % 10) for i in range(W)))
for y in range(H):
    print(f"y{y:02d} " + "".join(str(c.get(x, y)) if c.get(x, y) else "." for x in range(W)))
