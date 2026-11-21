import random

W = H = 16
c = new_canvas(W, H, name="stone")

# palette (7 visible colours total, limit is 10)
GRAYS = ["#6f6f6f", "#7d7d7d", "#8b8b8b", "#999999", "#a6a6a6"]
CRACK = "#454545"

# ---- tileable value noise (wrapped grid sampling => seamless) ----
def noise_grid(g, seed):
    r = random.Random(seed)
    return [[r.random() for _ in range(g)] for _ in range(g)]

g4 = noise_grid(4, 1)
g8 = noise_grid(8, 2)

def sample(grid, g, x, y):
    fx = x * g / W
    fy = y * g / H
    x0 = int(fx) % g
    y0 = int(fy) % g
    x1 = (x0 + 1) % g
    y1 = (y0 + 1) % g
    tx = fx - int(fx)
    ty = fy - int(fy)
    tx = tx * tx * (3 - 2 * tx)
    ty = ty * ty * (3 - 2 * ty)
    a = grid[y0][x0]
    b = grid[y0][x1]
    cc = grid[y1][x0]
    d = grid[y1][x1]
    return (a * (1 - tx) + b * tx) * (1 - ty) + (cc * (1 - tx) + d * tx) * ty

vals = []
for y in range(H):
    row = []
    for x in range(W):
        row.append(0.6 * sample(g4, 4, x, y) + 0.4 * sample(g8, 8, x, y))
    vals.append(row)

flat = [v for row in vals for v in row]
lo, hi = min(flat), max(flat)

for y in range(H):
    for x in range(W):
        t = (vals[y][x] - lo) / (hi - lo + 1e-9)
        idx = min(4, int(t * 5))
        c.set(x, y, GRAYS[idx])

# ---- cracks: non-reversing random walks (thin), modulo coords => seamless ----
def crack(seed, x, y, steps):
    r = random.Random(seed)
    dx, dy = r.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    for _ in range(steps):
        c.set(x % W, y % H, CRACK)
        # turn 90 deg sometimes, never reverse -> stays a thin 1px line
        if r.random() < 0.4:
            if r.random() < 0.5:
                dx, dy = dy, dx
            else:
                dx, dy = -dy, -dx
        x += dx
        y += dy

crack(21, 3, 1, 11)
crack(22, 12, 10, 10)
crack(23, 7, 14, 8)

print(c.stats_text())
view(c)

# tiling check: 2x2 stamp to confirm seamless edges (not submitted)
t = new_canvas(32, 32, name="tilecheck")
t.blit(c, 0, 0).blit(c, 16, 0).blit(c, 0, 16).blit(c, 16, 16)
view(t)

finish(c)
