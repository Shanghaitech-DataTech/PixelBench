from pixelbench_api import *

input_canvas = canvas("input")
output = input_canvas.copy(name="output")

# Left drip (shadowed)
drip1_x = 24
for y in range(33, 40):
    output.set(drip1_x, y, "c4")
    output.set(drip1_x+1, y, "c4")
output.set(drip1_x, 40, "c4")
output.set(drip1_x+1, 39, "c4") # round the bottom

# Middle drip (mixed lighting)
drip2_x = 30
for y in range(33, 43):
    output.set(drip2_x, y, "c4")
    output.set(drip2_x+1, y, "c17")
    output.set(drip2_x+2, y, "c4")
output.set(drip2_x, 43, "c4")
output.set(drip2_x+1, 43, "c4")
output.set(drip2_x+2, 42, "c4")
output.set(drip2_x+1, 44, "c4")

# Right drip (lit)
drip3_x = 36
for y in range(33, 38):
    output.set(drip3_x, y, "c17")
    output.set(drip3_x+1, y, "c17")
    output.set(drip3_x+2, y, "c4")
output.set(drip3_x, 38, "c17")
output.set(drip3_x+1, 38, "c4")
output.set(drip3_x+1, 39, "c4")

view(output)
