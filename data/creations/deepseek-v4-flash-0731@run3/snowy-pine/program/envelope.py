from pixelbench_api import input_canvas

c = input_canvas
W, H = c.stats()["size"]
def tree(x, y):
    return 0 <= x < W and 0 <= y < H and c.get(x, y) != 0

env = {}
for x in range(W):
    for y in range(H):
        if tree(x, y):
            env[x] = y
            break

# print envelope heights as bars
for y in range(H):
    cols = [x for x in range(W) if env.get(x) == y]
    if not cols:
        continue
    print(f"y={y:3d}: n={len(cols):2d} cols {min(cols)}-{max(cols)}")
