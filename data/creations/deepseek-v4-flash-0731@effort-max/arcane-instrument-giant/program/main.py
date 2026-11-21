import math

W = H = 256
CX, CY = 128, 92

bg = new_canvas(W, H, name="bg")
gl = new_canvas(W, H, name="glow")
inst = new_canvas(W, H, name="inst")


def sp(c, x, y, col):
    xi, yi = int(round(x)), int(round(y))
    if 0 <= xi < W and 0 <= yi < H:
        c.set(xi, yi, col)


def bands(r0, cols):
    for i, col in enumerate(cols):
        inst.circle(CX, CY, int(round(r0 - i)), col, fill=False)


def tilt_pt(t):
    a = math.radians(18)
    u = 110 * math.cos(math.radians(t))
    v = 76 * math.sin(math.radians(t))
    x = CX + u * math.cos(a) - v * math.sin(a)
    y = CY + u * math.sin(a) + v * math.cos(a)
    return x, y


def tilt_ring(ox, oy, col):
    for t in range(0, 360, 2):
        x, y = tilt_pt(t)
        sp(inst, x + ox, y + oy, col)
        sp(inst, x + ox + 1, y + oy + 1, col)


def ticks(rr, n, short_col, long_col, long_every=4, rot=0.0):
    for i in range(n):
        a = math.radians(rot + i * 360.0 / n)
        ln = 4 if i % long_every == 0 else 2
        x1 = CX + (rr - ln) * math.cos(a)
        y1 = CY + (rr - ln) * math.sin(a)
        x2 = CX + rr * math.cos(a)
        y2 = CY + rr * math.sin(a)
        inst.line(int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2)),
                 long_col if i % long_every == 0 else short_col)


RUNES = [
    ["..##.", "..##.", "#####", "..##.", "..##."],
    ["#...#", "#...#", "#####", "#...#", "#...#"],
    ["#####", "#....", "###..", "#....", "#####"],
    ["#....", "###..", "##...", "###..", "#...."],
    ["..#..", "#.#..", "#####", "#.#..", "..#.."],
    ["#...#", "#.#.#", "#####", "#.#.#", "#...#"],
    ["#####", "..#..", "#..#.", "..#..", "#####"],
    ["#.#.#", "..#..", "#####", "..#..", "#.#.#"],
]


def rune(c, cx, cy, idx, col, glow):
    c.circle(int(round(cx)), int(round(cy)), 7, glow, fill=True)
    g = RUNES[idx % 8]
    for j in range(5):
        for i in range(5):
            if g[j][i] == "#":
                c.set(int(round(cx - 2 + i)), int(round(cy - 2 + j)), col)


def alch(c, cx, cy, typ, col):
    cx = int(round(cx))
    cy = int(round(cy))
    if typ == 0:
        c.circle(cx, cy, 2, col, fill=False)
        c.circle(cx, cy, 1, col, fill=True)
    elif typ == 1:
        c.poly([(cx - 2, cy + 2), (cx + 2, cy + 2), (cx, cy - 2)], col, fill=True)
    elif typ == 2:
        c.rect(cx - 2, cy - 2, 5, 5, col, fill=False)
        c.set(cx, cy, col)
    elif typ == 3:
        c.poly([(cx - 2, cy - 1), (cx + 2, cy - 1), (cx, cy + 2)], col, fill=True)
    elif typ == 4:
        c.poly([(cx, cy - 2), (cx + 2, cy), (cx, cy + 2), (cx - 2, cy)], col, fill=True)
    elif typ == 5:
        c.circle(cx, cy, 2, col, fill=False)
        c.line(cx - 2, cy, cx + 2, cy, col)
        c.line(cx, cy - 2, cx, cy + 2, col)


def gear(c, cx, cy, r, teeth):
    cx = int(round(cx))
    cy = int(round(cy))
    c.circle(cx, cy, r, "#1a1508", fill=True)
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        for t in (0.0, 1.0):
            sp(c, cx + (r + 0.5 + t) * math.cos(a), cy + (r + 0.5 + t) * math.sin(a), "#1a1508")
        sp(c, cx + (r + 0.75) * math.cos(a + 0.09), cy + (r + 0.75) * math.sin(a + 0.09), "#1a1508")
        sp(c, cx + (r + 0.75) * math.cos(a - 0.09), cy + (r + 0.75) * math.sin(a - 0.09), "#1a1508")
    c.circle(cx, cy, r - 1, "#3d3218", fill=False)
    c.circle(cx, cy, r - 2, "#8a7332", fill=False)
    c.circle(cx, cy, r - 3, "#c2a248", fill=False)
    c.circle(cx, cy, max(1, r // 3), "#0a0c12", fill=True)
    c.circle(cx, cy, max(1, r // 3 - 1), "#d9b854", fill=False)


def sphere(c, cx, cy, r, body, dark, hi, glow):
    c.circle(int(round(cx)), int(round(cy)), r + 4, glow, fill=True)
    c.circle(int(round(cx)), int(round(cy)), r, dark, fill=True)
    c.circle(int(round(cx)), int(round(cy)), r - 1, body, fill=True)
    c.circle(int(round(cx + r * 0.45)), int(round(cy + r * 0.5)), max(1, int(r * 0.6)), dark, fill=True)
    c.circle(int(round(cx - r * 0.4)), int(round(cy - 0.4 * r)), max(1, int(r * 0.4)), hi, fill=True)
    c.circle(int(round(cx - r * 0.4)), int(round(cy - 0.4 * r)), max(1, int(r * 0.2)), "#ffffff", fill=True)


# ============================= BACKGROUND =============================
grad = ["#04050a", "#06070d", "#090b13", "#0d1019", "#111521", "#161b2a", "#1c2234", "#222a40"]
for y in range(230):
    if y <= 140:
        i = min(7, int(y * 7 / 140))
    else:
        i = max(0, int((229 - y) * 7 / 90))
    bg.rect(0, y, 256, 1, grad[i], fill=True)
bg.rect(0, 230, 256, 26, "#05060a", fill=True)
bg.rect(0, 231, 256, 2, "#0a0c14", fill=True)
bg.rect(0, 236, 256, 2, "#07090e", fill=True)
for x in range(0, 256, 32):
    bg.rect(x, 230, 1, 26, "#04060a", fill=True)

# hall arch
for t in range(180, 361, 2):
    a = math.radians(t)
    sp(bg, CX + 108 * math.cos(a), 234 + 108 * math.sin(a), "#0d1018")
    sp(bg, CX + 106 * math.cos(a), 234 + 106 * math.sin(a), "#1a1f2c")
    sp(bg, CX + 104 * math.cos(a), 234 + 104 * math.sin(a), "#141826")
bg.rect(4, 0, 14, 234, "#0d1018", fill=True)
bg.rect(18, 0, 2, 234, "#1a1f2c", fill=True)
bg.rect(4, 0, 2, 234, "#232a44", fill=True)
bg.rect(238, 0, 14, 234, "#0d1018", fill=True)
bg.rect(236, 0, 2, 234, "#1a1f2c", fill=True)
bg.rect(240, 0, 2, 234, "#232a44", fill=True)

# ============================= GLOW LAYER =============================
gl.circle(CX, CY, 120, (150, 100, 40, 45), fill=True)
gl.circle(CX, CY, 100, (170, 120, 55, 55), fill=True)
gl.circle(CX, CY, 84, (190, 140, 65, 60), fill=True)
gl.circle(CX, CY, 62, (210, 155, 80, 70), fill=True)
for i in range(12):
    a = math.radians(i * 30 + 15)
    col = (255, 205, 120, 70) if i % 2 == 0 else (255, 190, 100, 50)
    x1 = CX + 30 * math.cos(a)
    y1 = CY + 30 * math.sin(a)
    x2 = CX + 74 * math.cos(a)
    y2 = CY + 74 * math.sin(a)
    gl.line(int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2)), col)
gl.ellipse(CX, 246, 74, 20, (190, 140, 70, 50), fill=True)
gl.ellipse(CX, 254, 54, 10, (215, 160, 85, 55), fill=True)
gl.ellipse(CX, 248, 72, 17, (200, 150, 80, 42), fill=False)
for yy in range(180, 200):
    w = max(6, 24 - (yy - 180) * 2)
    col = (200, 140, 80, 70) if yy < 192 else (170, 120, 70, 60)
    gl.rect(CX - w // 2, yy, w, 1, col, fill=True)
gl.rect(CX - 2, 182, 4, 17, (255, 215, 130, 150), fill=True)

# ============================= INSTRUMENT =============================
# outer armillary ring (behind)
tilt_ring(-2, -2, "#8a7332")
tilt_ring(-1, -1, "#c2a248")
tilt_ring(0, 0, "#1a1508")

# concentric brass rings
for r0, cols in [
    (86, ["#1a1508", "#3d3218", "#6f5c28", "#8a7332", "#a68a3d"]),
    (80, ["#1a1508"]),
    (78, ["#d9b854"]),
    (76, ["#1a1508"]),
    (74, ["#6f5c28"]),
    (72, ["#d9b854"]),
    (70, ["#1a1508"]),
    (68, ["#8a7332"]),
    (65, ["#1a1508", "#a68a3d", "#c2a248"]),
    (62, ["#1a1508"]),
    (60, ["#8a7332"]),
    (58, ["#1a1508"]),
    (56, ["#6f5c28"]),
    (54, ["#1a1508", "#d9b854", "#a68a3d"]),
    (51, ["#1a1508"]),
    (49, ["#8a7332"]),
    (47, ["#1a1508", "#c2a248", "#8a7332"]),
    (44, ["#1a1508"]),
    (42, ["#6f5c28"]),
    (40, ["#1a1508", "#c2a248", "#a68a3d"]),
    (37, ["#1a1508"]),
    (35, ["#6f5c28"]),
    (33, ["#1a1508", "#d9b854"]),
    (31, ["#1a1508"]),
    (29, ["#8a7332"]),
    (27, ["#1a1508"]),
    (25, ["#c2a248"]),
    (23, ["#1a1508"]),
    (21, ["#6f5c28"]),
    (19, ["#1a1508", "#a68a3d"]),
    (17, ["#1a1508"]),
]:
    bands(r0, cols)

# studs on the outer armillary ring
for t in (35, 125, 215, 305):
    x, y = tilt_pt(t)
    x = int(round(x))
    y = int(round(y))
    inst.circle(x, y, 3, "#3d3218", fill=True)
    inst.circle(x, y, 2, "#6f5c28", fill=False)

# spokes
for i in range(8):
    a = math.radians(22.5 + i * 45)
    x1 = CX + 88 * math.cos(a)
    y1 = CY + 88 * math.sin(a)
    x2 = CX + 10 * math.cos(a)
    y2 = CY + 10 * math.sin(a)
    inst.line(int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2)), "#1a1508")
    inst.line(int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2)), "#6f5c28")
    x2 = CX + 12 * math.cos(a)
    y2 = CY + 12 * math.sin(a)
    inst.line(int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2)), "#a68a3d")

# rivets on the rim
for i in range(24):
    a = math.radians(i * 15 + 7.5)
    inst.circle(int(round(CX + 79 * math.cos(a))), int(round(CY + 79 * math.sin(a))), 1, "#d9b854", fill=True)

# dial ticks
ticks(52, 48, "#3d3218", "#d9b854", 4, rot=0.0)
ticks(33, 36, "#6f5c28", "#c2a248", 6, rot=7.0)

# glowing runes
for i in range(12):
    a = math.radians(45 + i * 30)
    rune(inst, CX + 60 * math.cos(a), CY + 60 * math.sin(a), i, "#8fe3ff", (96, 200, 255, 84))

# alchemical dial marks
for i in range(8):
    a = math.radians(i * 45 + 22.5)
    alch(inst, CX + 44 * math.cos(a), CY + 44 * math.sin(a), i, "#ffd24d")

# orbiting dust motes
for i in range(6):
    a = math.radians(20 + i * 60)
    col = "#59c4f0" if i % 2 else "#9feaff"
    inst.circle(int(round(CX + 55 * math.cos(a))), int(round(CY + 55 * math.sin(a))), 1, col, fill=True)

# gears
gear(inst, 128, 10, 9, 8)
gear(inst, 128, 174, 7, 7)
gear(inst, 45, 92, 9, 8)
gear(inst, 211, 92, 10, 8)
gear(inst, 170, 52, 6, 6)
gear(inst, 86, 132, 6, 6)
gear(inst, 172, 128, 4, 5)

# crystal spheres
sphere(inst, *tilt_pt(75), 7, "#42c8f0", "#1c5c86", "#b8f2ff", (120, 220, 255, 90))
sphere(inst, *tilt_pt(205), 8, "#c86fff", "#5a2a8a", "#e8c4ff", (190, 130, 255, 90))
sphere(inst, *tilt_pt(320), 6, "#49d18d", "#1d6e46", "#baffe0", (110, 255, 170, 90))
sphere(inst, 150, 122, 5, "#ff5a9e", "#8e2a5c", "#ffc0e6", (255, 120, 180, 90))

# gap chain trinket
inst.circle(128, 182, 2, "#c2a248", fill=False)
inst.circle(129, 183, 1, "#d9b854", fill=True)
inst.circle(122, 186, 2, "#a68a3d", fill=False)

# radiant core
inst.circle(CX, CY, 15, "#1a1508", fill=True)
inst.circle(CX, CY, 12, "#a0340a", fill=True)
inst.circle(CX, CY, 9, "#ff9430", fill=True)
inst.circle(CX, CY, 6, "#ffd45a", fill=True)
inst.circle(CX, CY, 4, "#fff6b8", fill=True)
inst.circle(CX, CY, 2, "#ffffff", fill=True)

# ============================= PEDESTAL =============================
inst.rect(90, 196, 76, 8, "#16181d", fill=True)
inst.rect(92, 198, 72, 4, "#3a3f49", fill=True)
inst.rect(96, 198, 64, 2, "#565c68", fill=True)
inst.rect(100, 204, 56, 3, "#202329", fill=True)
inst.rect(102, 207, 52, 4, "#2c3038", fill=True)
inst.rect(106, 209, 44, 28, "#16181d", fill=True)
inst.rect(110, 209, 36, 28, "#202329", fill=True)
inst.rect(112, 211, 32, 24, "#2c3038", fill=True)
inst.rect(112, 214, 32, 1, "#3a3f49", fill=True)
for j in range(4):
    inst.rect(112, 218 + j * 6, 32, 1, "#4a505c", fill=True)
inst.rect(124, 222, 8, 3, "#565c68", fill=True)
for k in range(4):
    for j in range(3):
        alch(inst, 116 + k * 8, 218 + j * 5, (k + j) % 6, "#565c68")
inst.rect(88, 234, 80, 6, "#16181d", fill=True)
inst.rect(84, 238, 88, 4, "#202329", fill=True)
inst.rect(80, 243, 96, 5, "#2c3038", fill=True)
inst.rect(66, 248, 124, 5, "#16181d", fill=True)
inst.rect(58, 252, 124, 4, "#202329", fill=True)
inst.rect(60, 253, 136, 3, "#2c3038", fill=True)
inst.rect(52, 254, 152, 2, "#3a3f49", fill=True)
rune(inst, 128, 250, 4, "#ffd24d", (255, 214, 90, 80))

# dark outline
inst.outline("#0a0806")

result = flatten([bg, gl, inst], name="arcane-instrument-giant")

# ---- quantize to the visible-colour limit ----
def quantize(c, k=132, iters=26):
    w, h, idx, pal = c.to_indexed(1)
    from collections import defaultdict
    cnt = defaultdict(int)
    for i in idx:
        cnt[i] += 1
    items = sorted(cnt.items(), key=lambda kv: -kv[1])
    cols = [tuple(pal[i][:3]) for i, _ in items]
    wts = [float(n) for _, n in items]
    centers = []
    seen = set()
    for col in cols:
        if col not in seen:
            seen.add(col)
            centers.append(list(col))
        if len(centers) >= k:
            break
    while len(centers) < k:
        centers.append(list(cols[len(centers) % len(cols)]))
    for _ in range(iters):
        acc = [[0.0, 0.0, 0.0] for _ in centers]
        ac = [0.0] * len(centers)
        for col, wt in zip(cols, wts):
            best = min(range(len(centers)),
                      key=lambda j: (col[0]-centers[j][0])**2 + (col[1]-centers[j][1])**2 + (col[2]-centers[j][2])**2)
            acc[best][0] += col[0]*wt; acc[best][1] += col[1]*wt; acc[best][2] += col[2]*wt
            ac[best] += wt
        moved = 0
        for j in range(len(centers)):
            if ac[j] > 0:
                nc = [acc[j][0]/ac[j], acc[j][1]/ac[j], acc[j][2]/ac[j]]
                if (abs(nc[0]-centers[j][0]) + abs(nc[1]-centers[j][1]) + abs(nc[2]-centers[j][2])) > 0.5:
                    moved += 1
                centers[j] = [int(round(v)) for v in nc]
        if moved == 0:
            break
    mapping = {}
    for i, col in enumerate(cols):
        j = min(range(len(centers)),
                key=lambda jj: (col[0]-centers[jj][0])**2 + (col[1]-centers[jj][1])**2 + (col[2]-centers[jj][2])**2)
        mapping[i] = (centers[j][0], centers[j][1], centers[j][2], 255)
    out = new_canvas(w, h, name="quantized")
    row = 0
    for y in range(h):
        for x in range(w):
            out.set(x, y, mapping[idx[row]])
            row += 1
    return out

result = quantize(result)
print(result.stats_text())
print("palette size:", len(result.palette()))
finish(result)
