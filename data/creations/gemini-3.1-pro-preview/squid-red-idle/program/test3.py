from pixelbench_api import *

input_canvas = canvas("input")

# Frame 2
f2 = input_canvas.copy(name="f2")
f2.select(0, 0, 58, 46).move_to(0, 1, f2)
f2.select(0, 0, 58, 22).move_to(0, 1, f2)
view(f2, margin=4)

# Frame 3
f3 = input_canvas.copy(name="f3")
f3.select(0, 0, 58, 46).move_to(0, 2, f3)
f3.select(0, 0, 58, 22).move_to(0, 2, f3)
view(f3, margin=4)

# Alternative Frame 2 without head squish
f2_alt = input_canvas.copy(name="f2_alt")
f2_alt.select(0, 0, 58, 46).move_to(0, 1, f2_alt)
view(f2_alt, margin=4)

# Alternative Frame 3 without head squish
f3_alt = input_canvas.copy(name="f3_alt")
f3_alt.select(0, 0, 58, 46).move_to(0, 2, f3_alt)
view(f3_alt, margin=4)

