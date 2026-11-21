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

# Upper body lean
# We can shear it manually or use rotate. Let's try rotate first.
upper = f2.select(11, 0, 31, 34)
f2.clear(11, 0, 31, 34)
upper_rot = upper.rotate(10)
upper_rot.copy_to(13, 2, f2) # shifted a bit right and down

# Front leg step forward
# Front leg is around x=20 to 32, y=52 to 62
front_leg = f2.select(19, 52, 13, 11)
f2.clear(19, 52, 13, 11)
front_leg.copy_to(25, 52, f2)

view(f2)
