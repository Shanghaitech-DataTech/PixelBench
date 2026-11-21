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
arm.copy_to(25 + 8, 21, f2)

# Connect arm to body
sleeve_slice = f2.select(33, 21, 2, 5)
sleeve_slice.copy_to(31, 21, f2)
sleeve_slice.copy_to(29, 21, f2)
sleeve_slice.copy_to(27, 21, f2)

# Fill background gaps if any (e.g. at x=25..27)
# For y=21..25, x=25..27, body color is 'e' (c4) and 'j' (c9)
# Let's just draw some e's and j's
f2.rect(25, 21, 3, 3, f2.color('c4'))
f2.rect(25, 24, 3, 2, f2.color('c9'))

view(f2)
