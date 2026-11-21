from pixelbench_api import *

c = input_canvas
out = c.copy(name='output')

# Right parrot occupies columns >= 34. Recolor its blue body (id3) to yellow (id4)
# and its light-blue accent (id7) to orange (id5), leaving beak/outline/face intact.
for y in range(64):
    for x in range(34, 64):
        idx = out.get(x, y)
        if idx == 3:
            out.set(x, y, 4)
        elif idx == 7:
            out.set(x, y, 5)

finish(out)
