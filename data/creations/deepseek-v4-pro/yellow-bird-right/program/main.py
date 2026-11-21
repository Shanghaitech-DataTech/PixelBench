from pixelbench_api import *

out = input_canvas.copy(name='output')

BLUE = out.color((0, 151, 224))
YELLOW = out.color((255, 207, 26))
LIGHT_BLUE = out.color((46, 205, 245))
ORANGE = out.color((213, 72, 24))

# The two parrots are mirror-symmetric with a white gap at x=30..33.
# Recolour only the right-hand parrot (x >= 32): body blue -> yellow,
# wing/tail accent light blue -> orange.
for y in range(64):
    for x in range(32, 64):
        idx = out.get(x, y)
        if idx == BLUE:
            out.set(x, y, YELLOW)
        elif idx == LIGHT_BLUE:
            out.set(x, y, ORANGE)

finish(out)
