from pixelbench_api import *

c = input_canvas
out = c.copy(name='output')

flesh = {6, 7, 8, 9}
rind = 5  # exposed durian rind (#be6f48)

# The bottom flesh segment is the rounded pod outlined in black at rows 49-55.
# Remove its flesh, exposing the rind underneath, and leave the other two pieces intact.
for y in range(49, 56):
    for x in range(64):
        if out.get(x, y) in flesh:
            out.set(x, y, rind)

finish(out)
