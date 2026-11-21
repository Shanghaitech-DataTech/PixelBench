from pixelbench_api import *

input_canvas = canvas("input")

f2_44 = input_canvas.copy(name="f2_44")
f2_44.select(0, 0, 58, 45).move_to(0, 1, f2_44)
view(f2_44, margin=4)

f2_45 = input_canvas.copy(name="f2_45")
f2_45.select(0, 0, 58, 46).move_to(0, 1, f2_45)
view(f2_45, margin=4)

f3_44 = input_canvas.copy(name="f3_44")
f3_44.select(0, 0, 58, 45).move_to(0, 2, f3_44)
view(f3_44, margin=4)

f3_46 = input_canvas.copy(name="f3_46")
f3_46.select(0, 0, 58, 47).move_to(0, 2, f3_46)
view(f3_46, margin=4)
