from pixelbench_api import *

src = input_canvas
W, H = 66, 119
G = [[src.get(x, y) for x in range(W)] for y in range(H)]

def remap_row(row, cx_dst, kL, kR):
    """Perspective-ish horizontal mapping: the side with the larger k is
    foreshortened (turned away from the viewer); smaller k is the near side."""
    cx_src = (W - 1) / 2
    out = [None] * W
    for dx in range(W):
        rel = dx - cx_dst
        sx = cx_src + rel * (kL if rel < 0 else kR)
        ix = int(round(sx))
        if 0 <= ix < W:
            out[dx] = row[ix]
    return out

def shift_h(grid, dx):
    ng = [[None] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            v = grid[y][x]
            if v is None:
                continue
            nx = x + dx
            if 0 <= nx < W:
                ng[y][nx] = v
    return ng

def bbox(grid):
    xs = [x for y in range(H) for x in range(W) if grid[y][x] is not None]
    return min(xs), max(xs)

def center_h(grid):
    a, b = bbox(grid)
    d = int(round((W - 1) / 2 - (a + b) / 2))
    return shift_h(grid, d)

def canvas_from(grid, name):
    c = new_canvas(W, H, name=name)
    for y, row in enumerate(grid):
        for x, idx in enumerate(row):
            if idx is not None:
                c.set(x, y, int(idx))
    return c

# ---------- Frame 1: three-quarter, character turned 45 deg to its left ----------
# The left half is slightly compressed (foreshortened turn) while the far side
# recedes; the whole composition is kept in the same palette.
kL, kR = 1.55, 1.12
f1g = center_h([remap_row(G[y], 32.5, kL, kR) for y in range(H)])

# ---------- Frame 2: opposite three-quarter (turned to its right) ----------
f2g = [row[::-1] for row in f1g]

# ---------- Frame 3: rear view (from directly behind) ----------
HAIR = [8, 9, 10, 11, 12, 13]   # pure hair rows (no face pixels)
f3g = [list(row) for row in G]
# entire back of head covered with hair
for y in range(15, 50):
    p = HAIR[(y - 15) % 6]
    for x in range(7, 59):
        f3g[y][x] = G[p][x]
# long hair falling down the back
for y in range(50, 71):
    p = HAIR[(y - 15) % 6]
    for x in range(15, 52):
        f3g[y][x] = G[p][x]
# solid tapering hair ends
taper = {71: (18, 48), 72: (20, 46), 73: (22, 44), 74: (24, 42), 75: (26, 40)}
for y, (a, b) in taper.items():
    p = HAIR[(y - 15) % 6]
    for x in range(a, b + 1):
        f3g[y][x] = G[p][x]

f1 = canvas_from(f1g, "f1")
f2 = canvas_from(f2g, "f2")
f3 = canvas_from(f3g, "f3")

print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())

# Verify f2 is exactly the horizontal mirror of f1
same = all(all((f1g[y][x] is None and f2g[y][W - 1 - x] is None) or
              (f1g[y][x] is not None and f2g[y][W - 1 - x] is not None and f1g[y][x] == f2g[y][W - 1 - x])
              for x in range(W)) for y in range(H))
print("f2 == mirror(f1):", same)

finish([f1, f2, f3])
print("SUBMITTED 3 frames")
