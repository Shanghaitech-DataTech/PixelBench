from pixelbench_api import *

input_canvas = canvas("input")

# Frame 2: move 0-48 down by 1
f2 = input_canvas.copy(name="f2")
f2.select(0, 0, 58, 49).move_to(0, 1, f2)

# Frame 3: move 0-48 down by 2, but we need to split it so it squishes rather than just moves.
# Actually, the previous split was good! Let's try splitting at row 30.
f3 = input_canvas.copy(name="f3")
f3.select(0, 0, 58, 49).move_to(0, 1, f3) # move whole top half down by 1
f3.select(0, 0, 58, 32).move_to(0, 1, f3) # move the top quarter down another 1

view(f3, margin=4)

