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

# Front leg step forward
front_leg = f2.select(21, 54, 12, 7)
f2.clear(21, 54, 12, 7)
front_leg.copy_to(27, 54, f2)

# Connect knee
thigh = f2.select(19, 51, 6, 3)
thigh.copy_to(22, 52, f2)
thigh.copy_to(24, 53, f2)

# Shear upper body to lean forward
for y in range(0, 36):
    if y < 10: dx = 4
    elif y < 18: dx = 3
    elif y < 26: dx = 2
    elif y < 32: dx = 1
    else: dx = 0
    
    if dx > 0:
        row = f2.select(0, y, 47, 1)
        f2.clear(0, y, 47, 1)
        row.copy_to(dx, y, f2)

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
