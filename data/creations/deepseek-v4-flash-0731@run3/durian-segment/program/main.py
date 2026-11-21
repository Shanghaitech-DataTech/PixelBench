from pixelbench_api import *

out = input_canvas.copy(name="output")

# The durian consists of three segments:
#   - top segment   : the cap at the upper right (rows 3-43)
#   - middle segment: the main body (rows 15-43)
#   - bottom segment: the bowl/rind at the bottom (rows 44-57) whose interior
#                     holds cream/yellow flesh (rows 44-53).
# Remove the BOTTOM segment's flesh so the rind underneath is exposed:
# recolor that flesh to the rind's inner surface orange (#ef9d0e).
# The other two pieces stay unchanged.
RIND_INNER = '#ef9d0e'
for y in range(44, 57):
    for x in range(64):
        c = out.get(x, y)
        if c in (6, 7, 8):   # flesh colours: cream c5, ylw c6, lylw c7
            out.set(x, y, RIND_INNER)

print(out.stats_text())
finish(out)
