from pixelbench_api import *

input_canvas = canvas("input")
output = input_canvas.copy(name="output")

c_base = "c4"
c_high = "c17"

def draw_drip(x, y_start, lengths):
    y = y_start
    for w in lengths:
        if w == 3:
            output.set(x-1, y, c_base)
            output.set(x, y, c_high)
            output.set(x+1, y, c_base)
        elif w == 2:
            output.set(x, y, c_high)
            output.set(x+1, y, c_base)
        elif w == 1:
            output.set(x, y, c_base)
        y += 1

draw_drip(23, 33, [3, 3, 3, 2, 2, 2, 1])
draw_drip(29, 33, [3, 3, 3, 3, 2, 2, 2, 2, 1, 1])
draw_drip(36, 33, [3, 3, 3, 3, 3, 2, 2, 2, 1])

view(output)
