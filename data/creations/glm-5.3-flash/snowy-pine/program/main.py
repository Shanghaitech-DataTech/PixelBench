out = input_canvas.copy(name='output')
W, H = 82, 135
BRIGHT = out.color('gt09')
SHADOW = out.color('gt08')

orig = [[input_canvas.get(x, y) != 0 for x in range(W)] for y in range(H)]

# ---- morphological closing: bridge gaps <= 2 px to get the tree's mass ----
solid = [row[:] for row in orig]

def close_rows(m):
    for y in range(H):
        x = 0
        while x < W:
            if m[y][x]:
                x += 1
                continue
            e = x
            while e < W and not m[y][e]:
                e += 1
            if x > 0 and e < W and (e - x) <= 2:
                for k in range(x, e):
                    m[y][k] = True
                x = e
            else:
                x = max(e, x + 1)

def close_cols(m):
    for x in range(W):
        y = 0
        while y < H:
            if m[y][x]:
                y += 1
                continue
            e = y
            while e < H and not m[e][x]:
                e += 1
            if y > 0 and e < H and (e - y) <= 2:
                for k in range(y, e):
                    m[k][x] = True
                y = e
            else:
                y = max(e, y + 1)

for _ in range(2):
    close_rows(solid)
    close_cols(solid)

y_top = [None] * W
for x in range(W):
    for y in range(H):
        if solid[y][x]:
            y_top[x] = y
            break
cols = [x for x in range(W) if y_top[x] is not None]
colset = set(cols)

def hsh(n, seed):
    n = (n * 374761393 + seed * 668265263 + 1013904223) & 0xFFFFFFFF
    n ^= n >> 13
    n = (n * 1274126177) & 0xFFFFFFFF
    return ((n >> 8) & 0xFFFF) / 65535.0

def vnoise(x, period, seed):
    f = x / period
    i = int(f)
    frac = f - i
    a = hsh(i, seed)
    b = hsh(i + 1, seed)
    t = frac * frac * (3 - 2 * frac)
    return a + (b - a) * t

def n2(x, y, period, seed):
    fx = x / period
    fy = y / period
    ix = int(fx); iy = int(fy)
    tx = fx - ix; ty = fy - iy
    tx = tx * tx * (3 - 2 * tx); ty = ty * ty * (3 - 2 * ty)
    a = hsh(ix + iy * 131, seed)
    b = hsh(ix + 1 + iy * 131, seed)
    c = hsh(ix + (iy + 1) * 131, seed)
    e = hsh(ix + 1 + (iy + 1) * 131, seed)
    return (a * (1 - tx) + b * tx) * (1 - ty) + (c * (1 - tx) + e * tx) * ty

# ---- desired snow thickness per column ----
d = {}
for x in cols:
    t = y_top[x]
    base = 3 + int(vnoise(x, 3.0, 11) * 3)          # 3..5 with drift
    x0 = x
    while x0 - 1 in colset and y_top[x0 - 1] == t:
        x0 -= 1
    x1 = x
    while x1 + 1 in colset and y_top[x1 + 1] == t:
        x1 += 1
    hrun = x1 - x0 + 1
    ld = (y_top[x0 - 1] - t) if (x0 - 1) in colset else 0
    rd = (y_top[x1 + 1] - t) if (x1 + 1) in colset else 0
    if hrun >= 3 and max(ld, rd) >= 2:
        base += 1                                    # a tier lip holds more
    if hrun == 1:
        base = min(base, 1)
    elif hrun == 2:
        base = min(base, 2)
    d[x] = max(1, min(6, base))

s = {x: y_top[x] - d[x] for x in cols}

# ---- relaxation: snow piles up against a step, clamped to a small overhang ----
order = sorted(cols)
for _ in range(10):
    changed = False
    for x in order:
        nb = [s[j] for j in (x - 1, x + 1) if j in s]
        if not nb:
            continue
        tgt = min(nb) + 1              # rise to just under the neighbour's snow
        if tgt < s[x]:
            s[x] = max(tgt, y_top[x] - 4)   # but never float far above our foliage
            changed = True
    if not changed:
        break

snow = {}
tip = 0
for x in cols:
    t = y_top[x]
    top = s[x]
    if t == 0:
        snow[(x, 0)] = BRIGHT
        tip += 1
        continue
    if top < 0:
        for y in range(0, t + 1):
            snow[(x, y)] = BRIGHT
        tip += 1
        continue
    top = min(top, t - 1)
    top = max(top, t - 6)
    thick = t - top
    if thick <= 1:
        snow[(x, t - 1)] = BRIGHT
    else:
        for y in range(top, t - 1):
            snow[(x, y)] = BRIGHT
        snow[(x, t - 1)] = SHADOW
        if thick >= 5:
            snow[(x, t)] = SHADOW

# ---- drop snow that has nothing underneath it ----
def is_tree(x, y):
    return 0 <= x < W and 0 <= y < H and orig[y][x]

for _ in range(6):
    kill = []
    for (x, y) in sorted(snow, key=lambda p: -p[1]):
        if (x, y + 1) in snow or is_tree(x, y + 1) or is_tree(x - 1, y) or is_tree(x + 1, y):
            continue
        kill.append((x, y))
    if not kill:
        break
    for p in kill:
        del snow[p]

# ---- snow packed into the canopy's interior slits ----
holes = [(x, y) for y in range(H) for x in range(W) if (not orig[y][x]) and solid[y][x]]
hf = 0
for (x, y) in holes:
    if n2(x, y, 4.0, 31) < 0.42:
        continue
    near = any((xx, yy) in snow for xx in (x - 1, x, x + 1) for yy in (y - 2, y - 1, y))
    snow[(x, y)] = BRIGHT if near else SHADOW
    hf += 1

for (x, y), col in snow.items():
    if 0 <= x < W and 0 <= y < H:
        out.set(x, y, col)

print("snow:", len(snow), "tipcols:", tip, "holes:", hf, "/", len(holes))
print(out.stats_text())

# ---- final polish: a few bright accents where drifts crest on tier lips ----
acc = 0
for x in cols:
    t = y_top[x]
    if (x, t - 1) in snow and snow[(x, t - 1)] == SHADOW:
        x0 = x
        while x0 - 1 in colset and y_top[x0 - 1] == t and (x0 - 1, t - 1) in snow:
            x0 -= 1
        x1 = x
        while x1 + 1 in colset and y_top[x1 + 1] == t and (x1 + 1, t - 1) in snow:
            x1 += 1
        if 2 <= (x1 - x0 + 1) <= 4 and vnoise(x0, 5.0, 91) > 0.55:
            for k in range(x0, x1 + 1):
                snow[(k, t - 1)] = BRIGHT
                acc += 1
for (x, y), col in snow.items():
    if 0 <= x < W and 0 <= y < H:
        out.set(x, y, col)
print("accents:", acc)

for y0 in range(0, H, 45):
    print("=== snow rows", y0, min(y0 + 44, H - 1))
    for y in range(y0, min(y0 + 45, H)):
        row = "".join('#' if (x, y) in snow else ('.' if not orig[y][x] else ' ') for x in range(W))
        print(row)

finish(out)
