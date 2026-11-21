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

# Arm thrust
arm = f2.select(26, 21, 15, 6)
f2.clear(26, 21, 15, 6)

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

# Paste arm further right
# The body was shifted by dx=2 at y=21..25, so we should shift the arm by more than 2, e.g. 8
arm.copy_to(26 + 8, 21, f2)

# Connect arm to body
# The body is around x=26+2 = 28. The arm is at x=34. We need to bridge ~6 pixels.
# Let's draw some lines for the arm
f2.line(27, 22, 34, 22, f2.color('c7')) # h
f2.line(27, 23, 34, 23, f2.color('c7'))
f2.line(27, 24, 34, 24, f2.color('c5')) # f
f2.line(27, 25, 34, 25, f2.color('c5'))

view(f2)
