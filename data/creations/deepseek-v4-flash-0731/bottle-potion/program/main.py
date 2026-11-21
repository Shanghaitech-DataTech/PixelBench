from pixelbench_api import *

src = input_canvas
WATER = {5, 6, 7, 8, 10}
water = [[False] * 64 for _ in range(64)]
for y in range(64):
    for x in range(64):
        water[y][x] = src.get(x, y) in WATER

out = src.copy(name='output')
REPL = {5: '#481a78', 6: '#8a3fd4', 7: '#b07df0', 8: '#ba8bf5', 10: '#9a5fe0'}
for y in range(64):
    for x in range(64):
        i = src.get(x, y)
        if i in REPL:
            out.set(x, y, REPL[i])

def on_water(cx, cy, r):
    for yy in range(cy - r, cy + r + 1):
        for xx in range(cx - r, cx + r + 1):
            if not (0 <= xx < 64 and 0 <= yy < 64 and water[yy][xx]):
                return False
    return True

bubble_c = '#c39bf7'
glint = '#f6e7ff'
bubs = [
    (18, 55, 2), (36, 50, 2), (26, 34, 2), (12, 31, 1), (38, 47, 2),
    (44, 57, 1), (30, 58, 1), (24, 46, 1), (10, 48, 1), (46, 35, 1),
    (28, 40, 1), (14, 38, 1), (40, 56, 1), (34, 55, 1), (20, 42, 1),
]
for (bx, by, r) in bubs:
    if on_water(bx, by, r):
        if r >= 1:
            out.circle(bx, by, r, bubble_c)
            out.set(bx - 1, by - 1, glint)
        else:
            out.set(bx, by, glint)

# surface fizz along the top of the liquid
fizz = [(13, 27), (17, 26), (22, 27), (27, 26), (33, 26), (37, 27), (42, 26)]
for (fx, fy) in fizz:
    if on_water(fx, fy, 0):
        out.set(fx, fy, glint)

print(out.stats_text())
print(out.matrix_text(region=(0, 22, 63, 63)))
finish(out)
