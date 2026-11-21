from pixelbench_api import *

input_canvas = canvas("input")
output = input_canvas.copy(name="output")

# Drip 1 (left)
output.rect(22, 33, 3, 7, "c4")
for y in range(33, 39):
    output.set(23, y, "c17")
output.set(23, 39, "c4")

# Drip 2 (middle left)
output.rect(28, 33, 3, 11, "c4")
for y in range(33, 43):
    output.set(29, y, "c17")
output.set(29, 43, "c4")

# Drip 3 (middle right)
output.rect(35, 35, 3, 9, "c4")
for y in range(35, 43):
    output.set(36, y, "c17")
output.set(36, 43, "c4")

view(output)
