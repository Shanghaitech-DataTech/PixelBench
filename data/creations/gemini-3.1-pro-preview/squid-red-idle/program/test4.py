from pixelbench_api import *

input_canvas = canvas("input")

# Frame 2: squish top of head
f2 = input_canvas.copy(name="f2")
f2.select(0, 0, 58, 30).move_to(0, 1, f2)
view(f2, margin=4)

# Frame 3: squish top of head more
f3 = input_canvas.copy(name="f3")
f3.select(0, 0, 58, 30).move_to(0, 2, f3)
view(f3, margin=4)

# Frame 2 alt: move everything above tentacles
f2_alt = input_canvas.copy(name="f2_alt")
f2_alt.select(0, 0, 58, 44).move_to(0, 1, f2_alt)
view(f2_alt, margin=4)

# Frame 3 alt: move everything above tentacles more
f3_alt = input_canvas.copy(name="f3_alt")
f3_alt.select(0, 0, 58, 44).move_to(0, 2, f3_alt)
view(f3_alt, margin=4)
