from pixelbench_api import new_canvas, finish

W = H = 32
c = new_canvas(W, H, name="carpet")


def reg(rgb):
    return c.color(tuple(rgb))


bg_dark = reg((94, 22, 24))      # deep maroon ground
bg = reg((114, 34, 32))         # maroon field
gold_l = reg((240, 208, 130))   # pale gold
gold = reg((206, 158, 76))      # gold
gold_d = reg((152, 108, 42))    # dark gold
cream = reg((242, 228, 194))    # cream
rust = reg((176, 92, 46))        # rust / terracotta
terr = reg((136, 54, 32))        # deep terracotta
petal = reg((228, 146, 76))      # warm orange


def setw(x, y, colour):
    c.set(x % W, y % H, colour)


def diamond(x, y, r, colour, fill=True):
    c.poly([(x, y - r), (x + r, y), (x, y + r), (x - r, y)], colour, fill=fill)


def diamondw(x, y, colour):
    """1px diamond centred at (x, y) with wrap-around."""
    setw(x, y - 1, colour)
    setw(x + 1, y, colour)
    setw(x, y + 1, colour)
    setw(x - 1, y, colour)
    setw(x, y, colour)


# ---------------- ground & border ----------------
c.rect(0, 0, W, H, bg_dark)
for y in range(H):
    for x in range(W):
        if x < 3 or x >= W - 3 or y < 3 or y >= H - 3:
            setw(x, y, gold_d)
for i in range(W):
    setw(i, 0, gold_l)
    setw(i, 31, gold_l)
for i in range(3, 29):
    setw(i, 3, gold)
    setw(i, 28, gold)
    setw(3, i, gold)
    setw(28, i, gold)
c.rect(4, 4, 24, 24, bg)

# ---------------- border ornaments ----------------
# corner accents on the band
for (cx, cy) in [(2, 2), (30, 2), (2, 30), (30, 30)]:
    diamond(cx, cy, 1, cream)
    setw(cx, cy, gold)

# flowers at band side centres (wrap around the seams too)
for (fx, fy) in [(16, 1), (16, 30), (1, 16), (30, 16)]:
    setw(fx, fy, gold)
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        setw(fx + dx, fy + dy, cream)
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        setw(fx + dx, fy + dy, rust)

# small diamonds along the band (edges wrap around)
for (sx, sy) in [(8, 1), (24, 1), (1, 8), (1, 24), (31, 8), (31, 24), (8, 31), (24, 31)]:
    diamondw(sx, sy, rust)
    setw(sx, sy, gold_l)

# dots on the inner frame between flowers and corner diamonds
for (px, py) in [(16, 5), (16, 27), (5, 16), (27, 16)]:
    setw(px, py, gold_l)

# ---------------- central geometric motif ----------------
diamond(16, 16, 10, rust)               # outer diamond
diamond(16, 16, 10, gold, fill=False)   # gold outline
diamond(16, 16, 6, gold)                # gold band
diamond(16, 16, 3, cream)               # cream centre
diamond(16, 16, 1, gold)                # golden core
for (qx, qy) in [(14, 14), (18, 14), (14, 18), (18, 18)]:
    setw(qx, qy, terr)
for (qx, qy) in [(16, 11), (16, 21), (11, 16), (21, 16)]:
    setw(qx, qy, petal)

# field corner diamonds
for (cx, cy) in [(7, 7), (25, 7), (7, 25), (25, 25)]:
    diamond(cx, cy, 3, gold_l)
    setw(cx, cy, gold)

# ---------------- woven texture ----------------
pal_snap = {p['index']: p['rgba'] for p in c.palette()}


def weave_pixel(x, y):
    m = (x + y) % 4
    if m in (0, 2):
        idx = c.get(x, y)
        r_, g_, b_, a_ = pal_snap[idx]
        if a_ == 0:
            return
        f = 0.85 if m == 0 else 1.05
        c.set(x, y, (min(255, int(r_ * f)), min(255, int(g_ * f)), min(255, int(b_ * f)), a_))


for y in range(H):
    for x in range(W):
        weave_pixel(x, y)

# Enforce full tile symmetry about the canvas centre so all four
# edges tile seamlessly: col(31-x) == col(x), row(31-y) == row(y).
for y in range(H):
    for x in range(W // 2):
        c.set(W - 1 - x, y, c.get(x, y))
for y in range(H // 2):
    for x in range(W):
        c.set(x, H - 1 - y, c.get(x, y))

# verify seams
bad = 0
for y in range(H):
    if c.get(0, y) != c.get(31, y):
        bad += 1
for x in range(W):
    if c.get(x, 0) != c.get(x, 31):
        bad += 1
print("seam mismatches:", bad)

print(c.stats_text())
for p in c.palette():
    print(p['index'], p['rgba'])

result = c
finish(result)
