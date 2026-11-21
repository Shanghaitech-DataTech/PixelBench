from pixelbench_api import *

print("get on transparent (0,0):", repr(input_canvas.get(0, 0)))
print("get on opaque (13,10):", repr(input_canvas.get(13, 10)))
print("palette:", input_canvas.palette())
