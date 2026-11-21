from pixelbench_api import *

input_canvas = canvas("input")

# Test squishing near the bottom
f2 = input_canvas.copy(name="f2")
f2.select(0, 0, 58, 53).move_to(0, 1, f2)
view(f2, margin=4)

f3 = input_canvas.copy(name="f3")
f3.select(0, 0, 58, 51).move_to(0, 2, f3)
view(f3, margin=4)

# Test squishing the body but keeping tentacles
f2_body = input_canvas.copy(name="f2_body")
f2_body.select(0, 0, 58, 44).move_to(0, 1, f2_body)
view(f2_body, margin=4)

f3_body = input_canvas.copy(name="f3_body")
f3_body.select(0, 0, 58, 43).move_to(0, 2, f3_body)
view(f3_body, margin=4)

