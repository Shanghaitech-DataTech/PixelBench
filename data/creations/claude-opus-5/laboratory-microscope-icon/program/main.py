c = new_canvas(32, 32, name="output")

DK  = c.color("#141826", "ink")
M1  = c.color("#9aa4ba", "metal")
M2  = c.color("#d2dbea", "metal_lt")
M3  = c.color("#6b7592", "metal_dk")
M4  = c.color("#454e68", "metal_dker")
BR  = c.color("#39415a", "stage")
GL  = c.color("#56c4e0", "glass")
GL2 = c.color("#b6effb", "glass_lt")
SL  = c.color("#f2f6ff", "slide")
SP  = c.color("#8a5fc8", "specimen")
KN  = c.color("#e0a93c", "knob")
KN2 = c.color("#9c6c18", "knob_dk")

solid = {}


def add(spans, fill, light=None, shade=None):
    for y, (x0, x1) in spans.items():
        for x in range(x0, x1 + 1):
            col = fill
            if light is not None and x == x0:
                col = light
            elif shade is not None and x == x1:
                col = shade
            solid[(x, y)] = col


# ---- arm / column (right side) ----
add({y: (19, 23) for y in range(10, 24)}, M3, light=M1, shade=M4)

# ---- eyepiece ----
add({1: (8, 12), 2: (8, 12), 3: (8, 12)}, M1, light=M2, shade=M3)
add({4: (8, 13)}, M4)

# ---- body tube ----
tube = {5: (9, 13), 6: (9, 13), 7: (10, 14), 8: (10, 14),
        9: (11, 15), 10: (11, 15), 11: (12, 16), 12: (12, 16)}
add(tube, M1, light=M2, shade=M3)

# ---- nosepiece / turret ----
add({13: (11, 18), 14: (11, 18)}, M1, light=M2)
for x in (11, 12, 13):
    solid[(x, 14)] = M3

# ---- objective lens (hangs under the turret, aimed at the slide) ----
add({15: (13, 17), 16: (13, 17)}, M3, light=M1, shade=M4)
add({17: (14, 16)}, M4, light=M3)
solid[(14, 17)] = GL

# ---- stage ----
add({18: (8, 26), 19: (6, 25)}, M2, shade=M1)
add({20: (6, 24), 21: (7, 23)}, BR, light=M3, shade=M4)

# ---- base (trapezoid, wider toward the front) ----
add({24: (13, 25)}, M1, light=M2, shade=M3)
add({25: (11, 26)}, M1, light=M2, shade=M3)
add({26: (9, 27)}, M3, light=M1, shade=M4)
add({27: (7, 28)}, M3, light=M1, shade=M4)
add({28: (6, 28)}, M3, light=M1, shade=M4)
add({29: (5, 28)}, M4, light=M3)

# ---- slide on the stage ----
for x in range(9, 23):
    solid[(x, 18)] = SL
solid[(14, 18)] = SP
solid[(15, 18)] = SP

# ---- coarse focus knob on the arm ----
for p in [(24, 20), (25, 20),
          (24, 21), (25, 21),
          (24, 22), (25, 22)]:
    solid[p] = KN
solid[(24, 20)] = KN
solid[(25, 20)] = KN2
solid[(25, 21)] = KN2
solid[(25, 22)] = KN2
solid[(24, 22)] = KN2

# ---- eyepiece glass ----
solid[(9, 1)] = GL2
solid[(10, 1)] = GL2
solid[(11, 1)] = GL

for (x, y), col in solid.items():
    c.set(x, y, col)

edge = set()
for (x, y) in solid:
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            p = (x + dx, y + dy)
            if p not in solid:
                edge.add(p)
for (x, y) in edge:
    if 0 <= x < 32 and 0 <= y < 32:
        c.set(x, y, DK)

view(c)
finish(c)
