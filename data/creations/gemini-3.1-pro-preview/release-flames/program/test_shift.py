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
upper = f2.select(11, 0, 31, 34)
f2.clear(11, 0, 31, 34)
upper.copy_to(14, 1, f2)

# Front leg
front_leg = f2.select(19, 52, 13, 11)
f2.clear(19, 52, 13, 11)
front_leg.copy_to(25, 52, f2)

# Fix staff connection
# The staff is color c2 (#0b0102ff, id 3) and c4 (#7d423aff, id 5)
# Let's just draw a line to connect the staff
f2.line(18, 34, 21, 34, f2.color(3))
f2.line(18, 35, 21, 35, f2.color(3))

# Flame
flame = input_canvas.select(37, 12, 10, 14)
flame.copy_to(55, 14, f2)

# Flame trail
f2.line(45, 18, 54, 18, f2.color(13))
f2.line(46, 19, 54, 19, f2.color(14))
f2.line(47, 20, 54, 20, f2.color(15))
f2.line(46, 21, 54, 21, f2.color(14))
f2.line(45, 22, 54, 22, f2.color(13))

view(f2)
