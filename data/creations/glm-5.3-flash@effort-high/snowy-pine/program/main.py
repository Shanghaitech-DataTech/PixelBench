W, H, data = input_canvas.to_rgba()
out = input_canvas.copy(name='output')

def alpha(x, y):
    if 0 <= x < W and 0 <= y < H:
        return data[4 * (y * W + x) + 3]
    return 0

# ---- snow palette ----
SNOW  = out.color('#f2f7f9', 'snow')
SHADE = out.color('#cfe3ec', 'snow_shade')
DEEP  = out.color('#a9c8d8', 'snow_deep')

# ---- find upward-facing edges (pixels with sky directly above) ----
edges = {}
for y in range(H):
    for x in range(W):
        if alpha(x, y) == 0:
            continue
        s = 0
        yy = y - 1
        while yy >= 0 and alpha(x, yy) == 0:
            s += 1
            yy -= 1
        open_top = (yy < 0)
        if s >= 1 or open_top:
            edges[(x, y)] = True

# ---- horizontal run length of each edge pixel (flatness measure) ----
runlen = {}
for (x, y) in edges:
    n = 1
    xx = x - 1
    while (xx, y) in edges:
        n += 1; xx -= 1
    xx = x + 1
    while (xx, y) in edges:
        n += 1; xx += 1
    runlen[(x, y)] = n

def hsh(x, y):
    return ((x * 73856093) ^ (y * 19349663)) & 0xffffffff

# ---- paint the snow ----
for (x, y) in edges:
    r = hsh(x, y) % 100
    n = runlen[(x, y)]
    out.set(x, y, SHADE if r < 12 else SNOW)
    below = alpha(x, y + 1) != 0
    if not below:
        continue
    if n >= 3:
        # flat ledge: a real layer of snow, 2px thick with a shaded base
        out.set(x, y + 1, SHADE)
        if n >= 5 and alpha(x, y + 2) != 0 and hsh(x, y + 7) % 100 < 55:
            out.set(x, y + 2, DEEP)
    else:
        # sloping edge: thin dusting, occasional thicker drift
        if r < 30:
            out.set(x, y + 1, SHADE)

# coarse overview: 3x3 blocks, dominant snow vs tree
for by in range(0, 135, 3):
    line = ""
    for bx in range(0, 82, 3):
        snow = 0; tree = 0
        for yy in range(by, min(by+3, 135)):
            for xx in range(bx, min(bx+3, 82)):
                a = alpha(xx, yy)
                if a == 0: continue
                idx = out.get(xx, yy)
                if idx in (SNOW, SHADE, DEEP): snow += 1
                else: tree += 1
        if snow == 0 and tree == 0: line += " "
        elif snow > tree: line += "*"
        elif tree > 0: line += "#"
        else: line += "."
    print(line)
finish(out)
