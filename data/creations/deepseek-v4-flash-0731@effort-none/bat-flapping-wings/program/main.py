from pixelbench_api import *

# Bat input is 27x22 pixels.
# Both frames share 27x30 canvas.
NW, NH = 27, 30
PIVOT = 8  # y-coordinate around which drooping wings flip to raised

# Read all actual (non-transparent) pixels from input.
pixels = {}
for y in range(22):
    for x in range(27):
        idx = input_canvas.get(x, y)
        if idx is not None and idx != 'transparent':
            pixels[(x, y)] = idx

# Frame 1: the original bat content, placed on a 27x30 canvas.
f1 = new_canvas(NW, NH)
for (x, y), idx in pixels.items():
    f1.set(x, y + 5, idx)

# Frame 2: bat with its drooping wings raised into a spread, raised position.
f2 = new_canvas(NW, NH)
for (x, y), idx in pixels.items():
    # The outer side columns forming the drooping wings (y>=6 and x<=6 or x>=20).
    is_wing = (y >= 6 and (x <= 6 or x >= 20))
    if is_wing:
        f2.set(x, 2 * PIVOT - y + 5, idx)
    else:
        f2.set(x, y + 5, idx)

# Print both for inspection.
print("Frame 1:")
print(f1.matrix_text())
print()
print("Frame 2:")
print(f2.matrix_text())
print()
print(f2.stats_text())

finish([f1, f2])

