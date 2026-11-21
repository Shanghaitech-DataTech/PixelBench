from pixelbench_api import *

src = input_canvas

# ---- Frame 1: original picture content on a roomier canvas ----
W, H = 38, 30
f1 = new_canvas(W, H)
f1.blit(src, 6, 1)

# ---- Frame 2: mid-leap pose ----
# Warp: horizontal stretch around x=13, pitch so the front (head, +x) rises,
# plus a global lift.  Inverse-map each destination pixel.
sx = 1.30      # horizontal stretch (elongate for the leap)
p  = 0.22      # pitch coefficient: head side rises, rear trails
lift = 3       # overall air lift
dxs = 3        # extra shift right
f2 = new_canvas(W, H)

for dy in range(H):
    for dx in range(W):
        x = (dx - dxs - 13) / sx + 13
        y = dy + lift - p * (13 - x)
        xi, yi = int(round(x)), int(round(y))
        if 0 <= xi < 26 and 0 <= yi < 28:
            col = src.get(xi, yi)
            if col != 0:
                f2.set(dx, dy, col)

# ---- Hole fill: patch isolated transparent pixels inside the body ----
fills = []
for dy in range(H):
    for dx in range(W):
        if f2.get(dx, dy) == 0:
            nb = []
            for ox, oy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = dx + ox, dy + oy
                if 0 <= nx < W and 0 <= ny < H:
                    col = f2.get(nx, ny)
                    if col != 0:
                        nb.append(col)
            if len(nb) >= 3:
                fills.append((dx, dy, max(set(nb), key=nb.count)))
for dx, dy, col in fills:
    f2.set(dx, dy, col)

print("f1:", f1.stats_text())
print(f1.matrix_text())
print("f2:", f2.stats_text())
print(f2.matrix_text())

finish([f1, f2])
