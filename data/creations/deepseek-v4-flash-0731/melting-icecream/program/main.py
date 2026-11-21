from pixelbench_api import input_canvas, finish

src = input_canvas
out = src.copy(name='output')

W, H = 64, 64
CHOCO = 18   # (93,51,53) dark chocolate
HI = 25      # (148,84,82) chocolate highlight

def on_ic(x, y):
    return 0 <= x < W and 0 <= y < H and out.get(x, y) != 1

def paint(x, y, col):
    if on_ic(x, y):
        out.set(x, y, col)

def paint_bg(x, y, col):
    if 0 <= x < W and 0 <= y < H:
        out.set(x, y, col)

def thick_drip(xs, y0, y1, head, tip=()):
    for i, y in enumerate(range(y0, y1 + 1)):
        x = xs[i]
        for dx in (-1, 0, 1):
            paint(x + dx, y, CHOCO)
    hx, hy = head
    for dx in (-1, 0, 1):
        paint(hx + dx, hy, CHOCO)
    paint(hx, hy + 1, CHOCO)
    paint(hx - 1, hy, HI)
    for (tx, ty) in tip:
        paint_bg(tx, ty, CHOCO)

# --- chocolate melt rim at the scoop bottom ---
for x in range(16, 42):
    paint(x, 30, CHOCO)
for x, sag in [(18,1),(22,1),(26,2),(31,2),(35,1),(39,1)]:
    for dy in range(1, sag+1):
        paint(x, 30+dy, CHOCO)
for x in (17, 25, 33, 38):
    paint(x, 30, HI)

# --- drips ---
thick_drip([21]*4 + [22]*4, 31, 38, (22, 39), tip=[(22, 40)])
thick_drip([25]*8 + [26]*9, 31, 47, (26, 48), tip=[(26, 49)])
thick_drip([29]*12 + [30]*8, 31, 50, (30, 51), tip=[(30, 52)])
thick_drip([33]*4 + [32]*4 + [31]*4, 31, 42, (31, 43), tip=[(31, 44)])
thick_drip([37]*7 + [36]*3, 31, 40, (36, 41), tip=[(36, 42)])
thick_drip([40]*3, 32, 34, (40, 35), tip=[(40, 36)])

# center drip reaches the tip and a drop falls off
paint(30, 53, CHOCO)
paint(30, 54, CHOCO)
paint_bg(31, 56, CHOCO)
paint_bg(31, 57, CHOCO)
paint_bg(31, 58, HI)

# loose droplets between drips
for (x, y) in [(28, 44), (28, 45)]:
    paint(x, y, CHOCO)
paint(28, 44, HI)
for (x, y) in [(39, 45), (39, 46)]:
    paint(x, y, CHOCO)
paint(39, 45, HI)

print(out.matrix_text(region=(12, 26, 46, 60), indices=True))

finish(out)
