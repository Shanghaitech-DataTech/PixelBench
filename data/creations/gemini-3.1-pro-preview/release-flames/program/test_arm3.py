from pixelbench_api import *

w, h = 70, 63
f2 = new_canvas(w, h, name="f2")
f2.blit(input_canvas, 0, 0)

# Clear flame
for y in range(12, 28):
    for x in range(35, 47):
        if f2.get(x, y) in [13, 14, 15]:
            f2.set(x, y, None)

# Arm thrust
arm = f2.select(25, 21, 13, 5)
f2.clear(25, 21, 13, 5)

# Front leg step forward
front_leg = f2.select(21, 54, 12, 7)
f2.clear(21, 54, 12, 7)
front_leg.copy_to(27, 54, f2)

# Connect knee
thigh = f2.select(19, 51, 6, 3)
thigh.copy_to(22, 52, f2)
thigh.copy_to(24, 53, f2)

# Shear upper body
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

# Arm thrust forward further
arm.copy_to(31, 21, f2)

# Fill arm gap
f2.rect(26, 21, 6, 2, f2.color('c4'))
f2.rect(26, 23, 6, 3, f2.color('c9'))

# Flame
flame = input_canvas.select(37, 12, 10, 14)
flame.copy_to(45, 14, f2)

# Flame trail
f2.line(39, 18, 44, 18, f2.color(13))
f2.line(39, 19, 44, 19, f2.color(14))
f2.line(40, 20, 44, 20, f2.color(15))
f2.line(40, 21, 44, 21, f2.color(14))
f2.line(39, 22, 44, 22, f2.color(13))

view(f2)
