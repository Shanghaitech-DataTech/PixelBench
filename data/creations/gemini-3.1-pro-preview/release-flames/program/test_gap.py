from pixelbench_api import *

w, h = 80, 63
f2 = new_canvas(w, h, name="f2")
f2.blit(input_canvas, 0, 0)

# Clear flame
for y in range(12, 28):
    for x in range(35, 47):
        pixel = f2.get(x, y)
        if pixel in [13, 14, 15]:  # m, n, o
            f2.set(x, y, None)

# Upper body
upper = f2.select(10, 0, 32, 34)
f2.clear(10, 0, 32, 34)
upper.copy_to(13, 1, f2)

# Fix the gap at y=34, x=10..32
# Staff and cloak
# Let's just use a few lines to connect the shifted part (dx=3, dy=1)
# to the unshifted part.
for x in range(10, 40):
    for y in range(33, 36):
        # We can just draw some pixels to bridge
        pass

# A simpler way is to copy a slice and stretch it
slice_y33 = f2.select(13, 33, 32, 1)
slice_y33.copy_to(12, 34, f2)
slice_y33.copy_to(11, 34, f2)

# Front leg
front_leg = f2.select(19, 52, 13, 11)
f2.clear(19, 52, 13, 11)
front_leg.copy_to(25, 52, f2)

# Flame
flame = input_canvas.select(37, 12, 10, 14)
flame.copy_to(55, 14, f2)

view(f2)
