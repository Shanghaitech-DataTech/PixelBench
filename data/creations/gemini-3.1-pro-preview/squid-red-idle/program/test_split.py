from pixelbench_api import *

input_canvas = canvas("input")

f2 = input_canvas.copy(name="f2")
f2.select(0, 0, 58, 48).move_to(0, 1, f2)
view(f2, margin=4)

f3 = input_canvas.copy(name="f3")
f3.select(0, 0, 58, 48).move_to(0, 1, f3)
f3.select(0, 0, 58, 29).move_to(0, 1, f3)
view(f3, margin=4)

f3_alt = input_canvas.copy(name="f3_alt")
f3_alt.select(0, 0, 58, 48).move_to(0, 2, f3_alt)
view(f3_alt, margin=4)

