import random

random.seed(2024)

src = input_canvas
W, H = 170, 170

palm = {}
for p in src.palette():
    palm[p['index']] = tuple(p['rgba'])

img = [[None] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        r, g, b, a = palm[src.get(x, y)]
        img[y][x] = (float(r), float(g), float(b))

# ---------------------------------------------------------------
# 1. build a mask for the big central character
# ---------------------------------------------------------------
def ischar(c):
    r, g, b = c
    if r >= g + 18 and r >= b + 12 and r > 50:
        return True
    if r >= g + 18 and b >= g + 18 and b > 55:
        return True
    if b >= r + 26 and b >= g + 26:
        return True
    if r > 190 and g > 140 and b > 120:
        return True
    return False

cand = [[False] * W for _ in range(H)]
for y in range(44, 155):
    for x in range(68, 142):
        if ischar(img[y][x]):
            cand[y][x] = True

seen = [[False] * W for _ in range(H)]
mask = [[False] * W for _ in range(H)]
for y in range(44, 155):
    for x in range(68, 142):
        if cand[y][x] and not seen[y][x]:
            stack = [(x, y)]
            seen[y][x] = True
            comp = []
            while stack:
                cx, cy = stack.pop()
                comp.append((cx, cy))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = cx + dx, cy + dy
                    if 68 <= nx <= 141 and 44 <= ny <= 154 and cand[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        stack.append((nx, ny))
            if len(comp) >= 250:
                cxm = sum(p[0] for p in comp) / float(len(comp))
                if cxm >= 84:
                    for (px, py) in comp:
                        mask[py][px] = True

n0 = sum(1 for y in range(H) for x in range(W) if mask[y][x])
print("raw mask px", n0)

# fill enclosed holes so dark interior of the character goes too
if n0 == 0:
    mask[70][90] = True

xs = [x for x in range(W) if any(mask[y][x] for y in range(H))]
ys = [y for y in range(H) if any(mask[y][x])]
bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
print("mask bbox", bx0, by0, bx1, by1)

outside = [[False] * W for _ in range(H)]
outside[by0][bx0] = True
stack = [(bx0, by0)]
while stack:
    cx, cy = stack.pop()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = cx + dx, cy + dy
        if bx0 <= nx <= bx1 and by0 <= ny <= by1 and not mask[ny][nx] and not outside[ny][nx]:
            outside[ny][nx] = True
            stack.append((nx, ny))
for y in range(by0, by1 + 1):
    for x in range(bx0, bx1 + 1):
        if not outside[y][x]:
            mask[y][x] = True

# dilate by 2 to swallow outlines / rim light
DIL = 2
mask2 = [[False] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if mask[y][x]:
            for dy in range(-DIL, DIL + 1):
                for dx in range(-DIL, DIL + 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        mask2[ny][nx] = True
mask = mask2
print("final mask px", sum(1 for y in range(H) for x in range(W) if mask[y][x]))

# ---------------------------------------------------------------
# 2. inpaint the removed area by diffusion from the border inward
# ---------------------------------------------------------------
known = [[not mask[y][x] for x in range(W)] for y in range(H)]
pending = [(x, y) for y in range(H) for x in range(W) if mask[y][x]]
passes = 0
while pending:
    passes += 1
    rest = []
    filled = []
    for (x, y) in pending:
        tr = tg = tb = 0.0
        wt = 0.0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H and known[ny][nx]:
                    w = 1.0 if (dx == 0 or dy == 0) else 0.7
                    c = img[ny][nx]
                    tr += c[0] * w
                    tg += c[1] * w
                    tb += c[2] * w
                    wt += w
        if wt > 0:
            img[y][x] = (tr / wt, tg / wt, tb / wt)
            filled.append((x, y))
        else:
            rest.append((x, y))
    if not filled:
        break
    for (x, y) in filled:
        known[y][x] = True
    pending = rest
print("inpaint passes", passes)

for _ in range(2):
    newv = {}
    for y in range(H):
        for x in range(W):
            if mask[y][x]:
                tr = tg = tb = 0.0
                wt = 0.0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            c = img[ny][nx]
                            tr += c[0]
                            tg += c[1]
                            tb += c[2]
                            wt += 1.0
                newv[(x, y)] = (tr / wt, tg / wt, tb / wt)
    for (x, y), c in newv.items():
        img[y][x] = c

for y in range(H):
    for x in range(W):
        if mask[y][x]:
            n = (random.random() - 0.5) * 9.0
            c = img[y][x]
            img[y][x] = (c[0] + n, c[1] + n * 0.8, c[2] + n * 0.6)

# ---------------------------------------------------------------
# 3. drawing helpers (work on the RGB buffer)
# ---------------------------------------------------------------
def put(x, y, c, a=255.0):
    if 0 <= x < W and 0 <= y < H:
        if a >= 255.0:
            img[y][x] = (float(c[0]), float(c[1]), float(c[2]))
        else:
            f = a / 255.0
            o = img[y][x]
            img[y][x] = (o[0] + (c[0] - o[0]) * f,
                         o[1] + (c[1] - o[1]) * f,
                         o[2] + (c[2] - o[2]) * f)

# ---------------------------------------------------------------
# 4. the vending machine that was hidden behind the character
# ---------------------------------------------------------------
VX0, VX1, VY0, VY1 = 88, 110, 104, 146

for y in range(VY0 - 4, VY1 + 3):
    for x in range(VX0 - 4, VX1 + 5):
        put(x, y, (70, 132, 172), 22)

for y in range(VY0, VY1 + 1):
    for x in range(VX0, VX1 + 1):
        put(x, y, (16, 33, 46))
for x in range(VX0, VX1 + 1):
    put(x, VY0, (58, 96, 118))
    put(x, VY0 + 1, (36, 66, 84))
for y in range(VY0, VY1 + 1):
    put(VX0, y, (44, 78, 100))
    put(VX1, y, (9, 21, 30))
    put(VX1 - 1, y, (12, 26, 36))

PX0, PX1 = VX0 + 3, VX0 + 16
PY0, PY1 = VY0 + 4, VY0 + 27
for y in range(PY0, PY1 + 1):
    t = (y - PY0) / float(max(1, PY1 - PY0))
    for x in range(PX0, PX1 + 1):
        put(x, y, (int(152 - 62 * t), int(202 - 60 * t), int(224 - 56 * t)))
for x in range(PX0 - 1, PX1 + 2):
    put(x, PY0 - 1, (74, 114, 134))
    put(x, PY1 + 1, (30, 60, 80))
for y in range(PY0 - 1, PY1 + 2):
    put(PX0 - 1, y, (74, 114, 134))
    put(PX1 + 1, y, (30, 60, 80))

prods = [(214, 70, 40), (232, 229, 211), (92, 181, 211), (117, 212, 124), (196, 111, 115)]
for s in range(PY0 + 4, PY1 - 1, 6):
    for x in range(PX0 + 1, PX1):
        put(x, s, (36, 74, 96))
    x = PX0 + 2
    while x < PX1 - 1:
        col = prods[(x + s) % len(prods)]
        put(x, s - 3, col)
        put(x + 1, s - 3, col)
        put(x, s - 2, col)
        put(x + 1, s - 2, col)
        x += 4

for y in range(PY0, PY0 + 10):
    for x in range(PX1 + 2, VX1):
        put(x, y, (26, 50, 68))
for y in range(PY0 + 2, PY0 + 9, 3):
    for x in range(PX1 + 2, VX1):
        put(x, y, (56, 96, 118))
put(VX1 - 2, PY0 + 11, (117, 212, 124))
put(VX1 - 2, PY0 + 12, (117, 212, 124))
put(VX1 - 2, PY0 + 13, (60, 120, 80))

for x in range(VX0 + 3, VX1 - 2):
    put(x, VY1 - 6, (6, 14, 20))
    put(x, VY1 - 5, (11, 24, 32))
for x in range(VX0, VX1 + 1):
    put(x, VY1, (20, 42, 58))
    put(x, VY1 + 1, (8, 18, 26))

# contact shadow on the pavement
for dx in range(-15, 16):
    for dy in range(0, 3):
        x = 99 + dx
        y = VY1 + 2 + dy
        if abs(dx) <= 14 - dy * 4:
            put(x, y, (4, 12, 18), 120 - dy * 30)

# ---------------------------------------------------------------
# 5. wet pavement
# ---------------------------------------------------------------
GY = 146
for y in range(GY, H):
    t = (y - GY) / float(H - GY)
    m = 0.20 + 0.30 * t
    for x in range(W):
        c = img[y][x]
        img[y][x] = (c[0] * (1 - m) + 38 * m,
                     c[1] * (1 - m) + 84 * m,
                     c[2] * (1 - m) + 114 * m)

for i in range(80):
    y = random.randrange(GY, H)
    x0 = random.randrange(-24, W)
    ln = random.randrange(8, 44)
    bright = 50 + random.random() * 45
    for k in range(ln):
        x = x0 + k
        put(x, y, (126, 176, 205), bright)

# reflection of the machine in the wet ground
for y in range(GY + 1, min(H, GY + 14)):
    t = (y - GY) / 13.0
    for x in range(VX0 - 2, VX1 + 3):
        put(x, y, (96, 156, 190), 78 * (1 - t))

# ---------------------------------------------------------------
# 6. quantise everything back onto the scene palette (+ a few
#    extra storm / prop colours) so the art keeps a closed palette
# ---------------------------------------------------------------
basecols = set()
for p in src.palette():
    r, g, b, a = p['rgba']
    if a > 0:
        basecols.add((r, g, b))
extra = [(16, 33, 46), (58, 96, 118), (152, 202, 224), (86, 148, 178),
         (214, 70, 40), (232, 229, 211), (117, 212, 124), (74, 114, 134),
         (26, 50, 68), (30, 60, 80), (126, 176, 205), (4, 12, 18)]
allcols = list(basecols) + [c for c in extra if c not in basecols]
print("palette size for quantise", len(allcols))

qcache = {}
def quant(r, g, b):
    key = (int(r) // 4, int(g) // 4, int(b) // 4)
    v = qcache.get(key)
    if v is None:
        bd = 1e18
        v = allcols[0]
        for c in allcols:
            d = (r - c[0]) * (r - c[0]) + (g - c[1]) * (g - c[1]) + (b - c[2]) * (b - c[2])
            if d < bd:
                bd = d
                v = c
        qcache[key] = v
    return v

fin = [[None] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        c = img[y][x]
        n = (random.random() - 0.5) * 7.0
        q = quant(c[0] + n, c[1] + n, c[2] + n)
        fin[y][x] = (q[0], q[1], q[2], 255)

# ---------------------------------------------------------------
# 7. lightning in the background (glow first, then bolt)
# ---------------------------------------------------------------
def line_pixels(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    pts = []
    while True:
        pts.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return pts

trunk = [(124, -3), (118, 7), (126, 13), (114, 25), (122, 31), (109, 43), (113, 53)]
branch_a = [(114, 25), (101, 31), (104, 39)]
branch_b = [(122, 31), (133, 37), (129, 45)]
core = set()
for pts in (trunk, branch_a, branch_b):
    for i in range(len(pts) - 1):
        for p in line_pixels(pts[i], pts[i + 1]):
            core.add(p)

core_list = list(core)
for y in range(0, 68):
    for x in range(80, 150):
        best = 1e9
        for (cx, cy) in core_list:
            d = (cx - x) * (cx - x) + (cy - y) * (cy - y)
            if d < best:
                best = d
        d = best ** 0.5
        if d < 27:
            f = 0.34 * (1.0 - d / 27.0) ** 2
            r, g, b, al = fin[y][x]
            fin[y][x] = (int(r + (142 - r) * f),
                         int(g + (168 - g) * f),
                         int(b + (216 - b) * f), al)

for (x, y) in core_list:
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if (x + dx, y + dy) not in core:
                d2 = dx * dx + dy * dy
                if d2 <= 2:
                    blend_col = (198, 216, 250)
                    fx = 0.55
                elif d2 <= 5:
                    blend_col = (168, 190, 236)
                    fx = 0.30
                else:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H:
                    r, g, b, al = fin[ny][nx]
                    fin[ny][nx] = (int(r + (blend_col[0] - r) * fx),
                                   int(g + (blend_col[1] - g) * fx),
                                   int(b + (blend_col[2] - b) * fx), al)
for (x, y) in core_list:
    if 0 <= x < W and 0 <= y < H:
        fin[y][x] = (238, 245, 255, 255)

# ---------------------------------------------------------------
# 8. rain: semi transparent droplets / streaks
# ---------------------------------------------------------------
RAIN_CORE = (198, 224, 242)
RAIN_SOFT = (156, 190, 214)

def fput(x, y, c, a):
    if 0 <= x < W and 0 <= y < H:
        fin[y][x] = (c[0], c[1], c[2], a)

for i in range(260):
    x0 = random.randrange(-14, W + 6)
    y0 = random.randrange(-14, H + 6)
    L = random.choice([4, 5, 5, 6, 6, 7, 8])
    drift = random.random() < 0.5
    for k in range(L):
        x = x0 + (k // 3 if drift else k // 4)
        y = y0 + k
        if k == 0 or k == L - 1:
            fput(x, y, RAIN_SOFT, 85)
        else:
            fput(x, y, RAIN_CORE, 145)
    if random.random() < 0.30:
        fput(x0 + (L // 3 if drift else L // 4) + 1, y0 + L - 2, RAIN_SOFT, 70)

# fat falling drops
for i in range(46):
    x = random.randrange(0, W)
    y = random.randrange(0, H - 2)
    fput(x, y, RAIN_CORE, 160)
    fput(x, y + 1, RAIN_SOFT, 100)

# ---------------------------------------------------------------
# 9. clinging water droplets on the wet ground / machine
# ---------------------------------------------------------------
def droplet(cx, cy, rad):
    for dy in range(-rad, rad + 1):
        for dx in range(-rad, rad + 1):
            if dx * dx + dy * dy <= rad * rad + 1:
                fput(cx + dx, cy + dy, (128, 176, 206), 210)
    fput(cx, cy - rad, (238, 252, 255), 245)
    fput(cx - 1, cy - rad, (196, 228, 244), 215)
    fput(cx + rad, cy + rad, (6, 16, 24), 190)
    fput(cx, cy + rad + 1, (10, 24, 34), 150)

for i in range(78):
    x = random.randrange(2, W - 2)
    y = random.randrange(GY + 2, H - 2)
    droplet(x, y, 1)
for i in range(22):
    x = random.randrange(3, W - 3)
    y = random.randrange(GY + 3, H - 3)
    droplet(x, y, 2)

# a few droplets clinging to the vending machine front
for i in range(16):
    x = random.randrange(VX0 + 2, VX1 - 1)
    y = random.randrange(VY0 + 3, VY1 - 2)
    fput(x, y, (222, 246, 255), 170)
    fput(x, y + 1, (150, 196, 220), 120)

# wet pavement mirror flare from the lightning
for y in range(GY + 1, H):
    t = (y - GY) / float(H - GY)
    for x in range(96, 124):
        d = abs(x - 110) / 14.0
        a = int(70 * max(0.0, 1.0 - d) * (1.0 - t))
        if a > 0:
            r, g, b, al = fin[y][x]
            f = a / 255.0
            fin[y][x] = (int(r + (170 - r) * f), int(g + (198 - g) * f),
                         int(b + (232 - b) * f), al)

# ---------------------------------------------------------------
# 10. render
# ---------------------------------------------------------------
out = src.copy(name='output')
for y in range(H):
    for x in range(W):
        r, g, b, a = fin[y][x]
        out.set(x, y, (int(r), int(g), int(b), int(a)))

print(out.stats_text())
save("output", out)
finish(out)
