from pixelbench_api import *

c = input_canvas.copy(name='output')

W = c.color('#ffffff')
DARK = c.color('#2e1f12ff')
SKIN = c.color('#f2c49bff')
WOOD_D = c.color('#5a3a20ff')   # dark side of the staff
WOOD = c.color('#73492aff')    # lit side of the staff
B_L = c.color('#9adcf5ff')     # crystal light
B_M = c.color('#3da5d9ff')     # crystal mid
B_D = c.color('#1d6fa5ff')     # crystal dark

# 1) Remove the old sword (crossguard + blade + pommel remnants)
for y in range(39, 41):
    for x in range(40, 47):
        c.set(x, y, W)
for y in range(41, 56):
    for x in range(41, 48):
        c.set(x, y, W)
for y in (35, 36, 37, 38):
    c.set(44, y, W)

# 2) Hand still grips the staff (fingers on the near side)
for y in (35, 36, 37):
    c.set(40, y, SKIN)
    c.set(41, y, SKIN)
c.set(40, 38, DARK)
c.set(41, 38, DARK)

# 3) Wooden staff shaft running from the ground up beside the body
for y in range(12, 55):
    c.set(42, y, WOOD_D)
    c.set(43, y, WOOD)

# 4) Crystal orb topping the staff
c.set(42, 8, B_L); c.set(43, 8, B_L)
c.set(41, 9, B_M); c.set(42, 9, W); c.set(43, 9, B_M); c.set(44, 9, B_M)
c.set(41, 10, B_M); c.set(42, 10, B_M); c.set(43, 10, B_D); c.set(44, 10, B_D)
c.set(41, 11, B_D); c.set(42, 11, B_D); c.set(43, 11, B_D); c.set(44, 11, B_D)

# checks
leftover = [(x, y, c.get(x, y)) for y in range(0, 64) for x in range(0, 64) if c.get(x, y) in (18, 19, 20)]
print("leftover sword pixels:", leftover)
nonbg = [(x, y, c.get(x, y)) for y in range(0, 64) for x in range(45, 64) if c.get(x, y) not in (0, 1)]
print("non-background pixels at x>=45:", nonbg)

print(c.stats_text())
print(c.matrix_text(region=(36, 4, 50, 56)))
finish(c)
