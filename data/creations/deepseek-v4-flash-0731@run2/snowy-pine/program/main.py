from pixelbench_api import *

c = input_canvas
out = c.copy(name='output')
W, H = c.stats()['size']

_, _, data = c.to_rgba()
alpha = [[data[(y*W + x)*4 + 3] for x in range(W)] for y in range(H)]
def foliage(x, y):
    return 0 <= x < W and 0 <= y < H and alpha[y][x] > 0

snow_main = out.color('#eff5f9')
snow_shade = out.color('#c3d5e0')

def set_snow(x, y):
    out.set(x, y, snow_main)
def set_shade(x, y):
    out.set(x, y, snow_shade)

# Snow caps resting on the tree tip and on each branch tier: (top_row, height)
bands = [(0, 6), (17, 4), (36, 4), (58, 4), (80, 4), (101, 3)]

for y0, bh in bands:
    # cap: cover the top bh rows of this tier, slight overhang at the very top
    for y in range(y0, min(y0 + bh, H)):
        xs = [x for x in range(W) if foliage(x, y)]
        if not xs:
            continue
        col = snow_shade if y == y0 + bh - 1 else snow_main
        if y == y0:
            if xs[0] - 1 >= 0:
                out.set(xs[0] - 1, y, col)
            if xs[-1] + 1 < W:
                out.set(xs[-1] + 1, y, col)
        for x in xs:
            out.set(x, y, col)
    # drips hanging from the cap over the foliage below
    y = y0 + bh
    for yy in range(y, min(y + 2, H)):
        xs = [x for x in range(W) if foliage(x, yy)]
        if not xs:
            continue
        set_snow(xs[0], yy)
        set_snow(xs[-1], yy)
        step = max(1, len(xs) // 5)
        for i in range(step, len(xs) - 1, step):
            set_snow(xs[i], yy)

print(out.stats_text())
finish(out)
