from pixelbench_api import *

input_canvas = canvas("input")

# Frame 2
f2 = input_canvas.copy(name="f2")
f2.select(0, 0, 58, 43).move_to(0, 1, f2)
view(f2, margin=4)

# Frame 3
f3 = input_canvas.copy(name="f3")
f3.select(0, 0, 58, 42).move_to(0, 2, f3)
view(f3, margin=4)

