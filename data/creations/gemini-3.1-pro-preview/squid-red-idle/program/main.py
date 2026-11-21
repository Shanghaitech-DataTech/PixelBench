from pixelbench_api import *

input_canvas = canvas("input")

f1 = input_canvas.copy(name="f1")

f2 = input_canvas.copy(name="f2")
f2.select(0, 0, 58, 48).move_to(0, 1, f2)

f3 = input_canvas.copy(name="f3")
f3.select(0, 0, 58, 48).move_to(0, 2, f3)

finish([f1, f2, f3])
