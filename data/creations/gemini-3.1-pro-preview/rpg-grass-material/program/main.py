from pixelbench_api import *
import random

random.seed(42)

c = new_canvas(16, 16)

base = "#5A9E54"
light = "#7BC676"
dark = "#3D7A3E"
vdark = "#26522B"
dirt_l = "#A07654"
dirt_d = "#7A543A"
flower_y = "#F2D852"
flower_c = "#D69438"

c.rect(0, 0, 16, 16, base)

for y in range(16):
    for x in range(16):
        r = random.random()
        if r < 0.25:
            c.set(x, y, light)
        elif r < 0.5:
            c.set(x, y, dark)

def draw_wrap(x, y, color):
    c.set(x % 16, y % 16, color)

dirt_patches = [
    (12, 12), (3, 3), (9, 2)
]
for dx, dy in dirt_patches:
    for iy in range(-1, 2):
        for ix in range(-1, 2):
            if abs(ix) + abs(iy) < 2 or random.random() < 0.5:
                if random.random() < 0.3:
                    draw_wrap(dx + ix, dy + iy, dirt_d)
                else:
                    draw_wrap(dx + ix, dy + iy, dirt_l)

tufts = [
    (7, 7), (13, 5), (2, 9), (10, 14), (5, 13)
]
for tx, ty in tufts:
    draw_wrap(tx - 1, ty - 1, light)
    draw_wrap(tx + 1, ty - 1, light)
    draw_wrap(tx, ty, dark)
    draw_wrap(tx - 1, ty, dark)
    draw_wrap(tx + 1, ty, dark)
    draw_wrap(tx, ty + 1, vdark)

flowers = [
    (14, 2), (4, 8), (8, 11), (1, 14)
]
for fx, fy in flowers:
    if random.random() < 0.5:
        draw_wrap(fx, fy, flower_y)
        draw_wrap(fx, fy+1, vdark)
    else:
        draw_wrap(fx, fy, flower_y)
        draw_wrap(fx+1, fy, flower_y)
        draw_wrap(fx, fy+1, flower_y)
        draw_wrap(fx+1, fy+1, flower_c)
        draw_wrap(fx, fy+2, vdark)
        draw_wrap(fx+1, fy+2, vdark)

finish(c)
