from pixelbench_api import *

input_canvas = canvas("input")
output = input_canvas.copy(name="output")

# Drip 1 (left)
for y in range(33, 37): output.set(23, y, "c4")
for y in range(33, 42): output.set(24, y, "c4")
for y in range(33, 40): output.set(25, y, "c4")
output.set(24, 42, "c4")

# Drip 2 (middle)
for y in range(33, 38): output.set(29, y, "c4")
for y in range(33, 45): output.set(30, y, "c4")
for y in range(33, 44): output.set(31, y, "c17")
for y in range(33, 39): output.set(32, y, "c4")
output.set(30, 45, "c4")
output.set(31, 44, "c4")
output.set(30, 46, "c4")

# Drip 3 (right)
for y in range(33, 37): output.set(35, y, "c4")
for y in range(33, 42): output.set(36, y, "c17")
for y in range(33, 40): output.set(37, y, "c17")
for y in range(33, 36): output.set(38, y, "c4")
output.set(36, 42, "c4")
output.set(37, 40, "c4")

view(output)
