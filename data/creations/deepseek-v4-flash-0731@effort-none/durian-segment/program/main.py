from pixelbench_api import *

input_canvas = canvas('input')
output = input_canvas.copy(name='output')

# The durian in the image shows three fleshy segments.
# Remove the bottom segment of durian flesh so the rind underneath (#ffc830) is exposed.
# Keep the other two pieces (the upper fleshy segments) unchanged.
# The bottom segment's flesh (cream color index 6, #fbf4c9) is changed to rind color (index 7, #ffc830).

# The bottom segment of the durian spans y >= 37 in the durian.
# Change the fleshy cream (index 6) pixels in this bottom region to rind (index 7).
for y in range(37, 64):
    for x in range(64):
        if output.get(x, y) == 6:
            output.set(x, y, 7)  # #ffc830 (rind surface color)

finish(output)
