from pixelbench_api import *
import random

c = new_canvas(16, 16)

base = c.color('#757575', 'base')
light_noise = c.color('#828282', 'light_noise')
dark_noise = c.color('#636363', 'dark_noise')
highlight = c.color('#969696', 'highlight')
shadow = c.color('#525252', 'shadow')
mortar = c.color('#363636', 'mortar')
crack = c.color('#222222', 'crack')

c.rect(0, 0, 16, 16, base)

random.seed(45)
for y in range(16):
    for x in range(16):
        r = random.random()
        if r < 0.2:
            c.set(x, y, light_noise)
        elif r < 0.4:
            c.set(x, y, dark_noise)

# Draw Mortar
for i in range(16):
    c.set(i, 7, mortar)
    c.set(i, 15, mortar)

for y in range(8):
    c.set(7, y, mortar)
    c.set(15, y, mortar)

for y in range(8, 16):
    c.set(3, y, mortar)
    c.set(11, y, mortar)

def draw_brick(x0, y0, x1, y1):
    for x in range(x0, x1):
        c.set(x % 16, y0 % 16, highlight)
    for y in range(y0, y1):
        c.set(x0 % 16, y % 16, highlight)
    for x in range(x0, x1):
        c.set(x % 16, (y1 - 1) % 16, shadow)
    for y in range(y0, y1):
        c.set((x1 - 1) % 16, y % 16, shadow)
    c.set(x0 % 16, (y1 - 1) % 16, shadow)
    c.set((x1 - 1) % 16, y0 % 16, shadow)

draw_brick(0, 0, 7, 7)
draw_brick(8, 0, 15, 7)
draw_brick(12, 8, 19, 15)
draw_brick(4, 8, 11, 15)

cracks = [
    # Brick 1
    [(3, 0), (3, 1), (4, 2), (4, 3), (5, 4), (4, 5), (5, 6)],
    [(4, 3), (3, 4), (2, 4), (1, 5)],
    # Brick 2
    [(8, 5), (9, 4), (10, 4), (11, 3), (11, 2), (12, 1)],
    [(10, 4), (10, 5), (11, 6)],
    # Brick 3
    [(14, 14), (15, 13), (0, 12), (1, 11), (2, 10), (1, 9)],
    [(0, 12), (0, 11), (15, 10)],
    # Brick 4
    [(5, 8), (6, 9), (7, 10), (7, 11), (8, 12), (9, 13)],
    [(7, 10), (8, 9), (9, 9)]
]

for crack_line in cracks:
    for x, y in crack_line:
        hx, hy = (x + 1) % 16, (y + 1) % 16
        if c.get(hx, hy) != mortar:
            c.set(hx, hy, highlight)
            
for crack_line in cracks:
    for x, y in crack_line:
        c.set(x % 16, y % 16, crack)

finish(c)
