from pixelbench_api import input_canvas, finish

out = input_canvas.copy(name="output")
W, H = out.stats()["size"]

WHITE = out.color("#EAF0F7", name="snow_white")   # bright snow surface
BLUE  = out.color("#C3D2E5", name="snow_shadow")  # shaded snow under-layer

def tree(x, y):
    return 0 <= x < W and 0 <= y < H and out.get(x, y) != 0

# Every top-boundary pixel: a tree pixel with nothing above it.
# These trace every ledge of the pine (branch tier tops + outer contour).
bounds = set()
for y in range(H):
    for x in range(W):
        if tree(x, y) and (y == 0 or not tree(x, y - 1)):
            bounds.add((x, y))

def flatness(x, y):
    s = 0
    for dx in (-1, 1):
        if (x + dx, y) in bounds or (x + dx, y + 1) in bounds or (x + dx, y - 1) in bounds:
            s += 1
    return s

# 1) Solid snow cap on the apex (rows 0..9).
for y in range(0, 10):
    for x in range(W):
        if tree(x, y):
            out.set(x, y, WHITE)

# 2) Snow blanket along every ledge / upper contour.
#    Uniform 2px white snow edge; flat ledges get extra blue shade below.
for (x, y) in sorted(bounds):
    if y < 10:
        continue
    out.set(x, y, WHITE)
    f = flatness(x, y)
    if tree(x, y + 1):
        out.set(x, y + 1, WHITE)
        if f >= 1 and tree(x, y + 2):
            out.set(x, y + 2, BLUE)
        if f >= 2 and tree(x, y + 3) and x % 2 == 0:
            out.set(x, y + 3, BLUE)

print(out.stats_text())
finish(out)
