import math
from collections import deque

W = H = 256

# ------------------------------------------------------------------ palettes
SKY = ["#040c08", "#061009", "#08160d", "#0b1d11", "#0f2616", "#142f1b",
       "#193a21", "#1f4727", "#26542e", "#2e6336", "#387440", "#44864b",
       "#539a58", "#67b068", "#82c87c", "#a6df93"]
BARK = ["#191007", "#2a1f10", "#3f2e18", "#57401f", "#6f5429", "#8f7038"]
MOSS = ["#22421f", "#2f5b2a", "#3f7a33", "#55a044", "#79c25c"]
EYE = ["#0d2e16", "#146b32", "#2fb556", "#6bf08a", "#c8ffd4"]
VINE = ["#16290f", "#21391a", "#2e5024"]
SOIL = ["#070805", "#0e100a", "#171a0f", "#232714", "#31361a", "#414722"]
LICH = "#8fa87a"
DARK = "#0d0803"
FAR = "#050d08"
FAR2 = "#030906"

CAN_COLS = ["#071509", "#0a1c10", "#0d2314", "#0d2417", "#0a1d12", "#0f2a1a", "#16351f"]

CH = {}
for i, h in enumerate(SKY):
    CH[h] = ".:oO"[min(3, i // 4)]
for i, h in enumerate(BARK):
    CH[h] = "123456"[i]
for i, h in enumerate(MOSS):
    CH[h] = "mMgG&"[i]
for i, h in enumerate(EYE):
    CH[h] = "eEBS*"[i]
for i, h in enumerate(VINE):
    CH[h] = "v"
for i, h in enumerate(SOIL):
    CH[h] = "_-=+~:"[i]
for h in CAN_COLS:
    CH[h] = "T"
CH[LICH] = "l"
CH[DARK] = "K"
CH["#0a0602"] = "K"
CH["#221a0c"] = "k"
CH[FAR] = "t"
CH[FAR2] = "t"

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def clamp(v, a, b):
    return a if v < a else (b if v > b else v)


def h2(x, y, s=0):
    n = (int(x) * 374761393 + int(y) * 668265263 + s * 1442695041) & 0xffffffff
    n = (n ^ (n >> 13)) & 0xffffffff
    n = (n * 1274126177) & 0xffffffff
    return ((n ^ (n >> 16)) & 0xffff) / 65535.0


def vnoise(x, y, scale=1.0, s=0):
    fx = x * scale
    fy = y * scale
    ix = math.floor(fx)
    iy = math.floor(fy)
    tx = fx - ix
    ty = fy - iy
    tx = tx * tx * (3 - 2 * tx)
    ty = ty * ty * (3 - 2 * ty)
    a = h2(ix, iy, s)
    b = h2(ix + 1, iy, s)
    c = h2(ix, iy + 1, s)
    d = h2(ix + 1, iy + 1, s)
    return (a * (1 - tx) + b * tx) * (1 - ty) + (c * (1 - tx) + d * tx) * ty


def fbm(x, y, scale=1.0, s=0, oct=3):
    v = 0.0
    amp = 0.5
    sc = scale
    tot = 0.0
    for i in range(oct):
        v += amp * vnoise(x, y, sc, s + i * 17)
        tot += amp
        amp *= 0.5
        sc *= 2.0
    return v / tot


# ------------------------------------------------------------- canvases
bg = new_canvas(W, H, background=None, name="bg")
tr = new_canvas(W, H, background=None, name="treant")
fg = new_canvas(W, H, background=None, name="fg")

# ------------------------------------------------------------------ 1. sky
SRC = (198.0, -14.0)
BANDS = [(132, 13, 0.55), (100, 8, 0.32), (70, 17, 0.70), (34, 10, 0.42),
         (2, 20, 0.85), (-32, 9, 0.45), (-62, 15, 0.65), (-98, 10, 0.38),
         (-132, 18, 0.70), (-172, 12, 0.45), (-210, 9, 0.30)]


def rayat(x, y):
    vx, vy = -0.6225, 0.7831
    nx, ny = -vy, vx
    px = x - SRC[0]
    py = y - SRC[1]
    p = px * nx + py * ny
    t = px * vx + py * vy
    r = 0.0
    for (c0, w, amp) in BANDS:
        dd = abs(p - c0)
        if dd < w:
            r += amp * (1.0 - (dd / w) ** 2)
    r *= max(0.0, 1.0 - max(0.0, t) / 380.0)
    r *= 0.60 + 0.80 * fbm(x, y, 0.05, 21, 2)
    return r


def skyval(x, y):
    b = 0.12 + 0.15 * (1.0 - y / 256.0)
    d = math.hypot(x - SRC[0], y - SRC[1])
    b += 0.95 * max(0.0, 1.0 - d / 150.0) ** 1.8
    b += 0.60 * rayat(x, y)
    b *= (1.0 - 0.42 * max(0.0, (y - 145) / 111.0))
    return b


skyidx = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        f = skyval(x, y) * 15.0
        i = int(f)
        if f - i > (BAYER[y % 4][x % 4] + 0.5) / 16.0:
            i += 1
        i = clamp(i, 0, 15)
        skyidx[y][x] = i
        bg.set(x, y, SKY[i])

# ------------------------------------------------------------------ 2. canopy
CANOPY = [(-24, -30, 84), (40, -40, 72), (100, -58, 70), (150, -46, 58),
          (0, 12, 44), (276, -12, 72), (244, -34, 52), (-10, 34, 30)]

cmask = [bytearray(W) for _ in range(H)]
for (cx, cy, r) in CANOPY:
    x0 = max(0, int(cx - r - 8))
    x1 = min(W - 1, int(cx + r + 8))
    y0 = max(0, int(cy - r - 8))
    y1 = min(H - 1, int(cy + r + 8))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            dx = x - cx
            dy = y - cy
            d = math.hypot(dx, dy)
            if d > r + 8:
                continue
            ang = math.atan2(dy, dx)
            rr = r + 4.0 * math.sin(ang * 9.0 + cx * 0.31) + 3.0 * math.sin(ang * 21.0 + cy * 0.2)
            if d < rr:
                cmask[y][x] = 1

for y in range(H):
    for x in range(W):
        if not cmask[y][x]:
            continue
        below = (y + 2 < H) and cmask[y + 2][x]
        below2 = (y + 4 < H) and cmask[y + 4][x]
        n = fbm(x, y, 0.09, 41, 3)
        if not below2:
            col = "#16351f" if n > 0.45 else "#0f2a1a"
        elif not below:
            col = "#0d2417" if n > 0.4 else "#0a1d12"
        else:
            v = n
            col = "#071509" if v < 0.36 else ("#0a1c10" if v < 0.55 else "#0d2314")
        bg.set(x, y, col)

# ------------------------------------------------------------------ 3. far trees
def far_tree(x0, w0, top, bot):
    for y in range(top, bot):
        tt = (y - top) / float(bot - top)
        w = w0 * (0.75 + 0.55 * tt)
        xc = x0 + 2.0 * math.sin((y - top) * 0.05 + x0)
        for x in range(int(xc - w / 2) - 1, int(xc + w / 2) + 2):
            if 0 <= x < W:
                d = abs(x - xc) / max(1.0, w / 2)
                lvl = skyidx[y][x] - (3 if d < 0.60 else 2)
                bg.set(x, y, SKY[clamp(lvl, 0, 15)])
    for (by, bl, dirn) in ((int(top + (bot - top) * 0.26), 18, 1), (int(top + (bot - top) * 0.48), 13, -1)):
        for i in range(bl):
            xx = int(x0 + dirn * i * 0.85)
            yy = int(by - i * 0.5)
            if 0 <= xx < W and 0 <= yy < H:
                bg.set(xx, yy, SKY[clamp(skyidx[yy][xx] - 3, 0, 15)])
                if 1 <= xx < W - 1:
                    bg.set(xx + 1, yy, SKY[clamp(skyidx[yy][xx + 1] - 3, 0, 15)])


far_tree(30, 9, 34, 206)
far_tree(66, 6, 46, 202)
far_tree(226, 8, 26, 204)
far_tree(248, 6, 40, 208)

# ------------------------------------------------------------------ 4. ground
def ground_top(x):
    return 208.0 - 9.0 * ((x - 128.0) / 128.0) ** 2 + 2.6 * math.sin(x * 0.075 + 0.6) + 1.6 * math.sin(x * 0.19)


gt = [int(ground_top(x)) for x in range(W)]
for x in range(W):
    for y in range(gt[x], H):
        dep = (y - gt[x])
        r = rayat(x, y)
        n = fbm(x, y, 0.13, 77, 3)
        b = 1.9 + 0.60 * n + 2.4 * min(1.0, r)
        b -= dep * 0.035
        if dep < 3:
            b += 1.3
        i = int(clamp(b, 0, 5) + 0.5)
        bg.set(x, y, SOIL[i])

# ------------------------------------------------------------------ 5. treant mask
body = [bytearray(W) for _ in range(H)]


def fill_circle(mask, cx, cy, r, val=1):
    if r <= 0.6:
        ix = int(round(cx))
        iy = int(round(cy))
        if 0 <= ix < W and 0 <= iy < H:
            mask[iy][ix] = val
        return
    x0 = max(0, int(math.floor(cx - r)))
    x1 = min(W - 1, int(math.ceil(cx + r)))
    y0 = max(0, int(math.floor(cy - r)))
    y1 = min(H - 1, int(math.ceil(cy + r)))
    r2 = r * r
    for y in range(y0, y1 + 1):
        dy = y - cy
        row = mask[y]
        for x in range(x0, x1 + 1):
            dx = x - cx
            if dx * dx + dy * dy <= r2:
                row[x] = 1


def spline(pts, n=26):
    if len(pts) == 1:
        return [tuple(pts[0])]
    P = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / float(n)
            t2 = t * t
            t3 = t2 * t

            def cr(a, b, c, d):
                return 0.5 * ((2 * b) + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t2 + (-a + 3 * b - 3 * c + d) * t3)
            out.append((cr(p0[0], p1[0], p2[0], p3[0]),
                        cr(p0[1], p1[1], p2[1], p3[1]),
                        cr(p0[2], p1[2], p2[2], p3[2])))
    out.append(tuple(pts[-1]))
    return out


def add_limb(mask, pts, n=26):
    for (x, y, r) in spline(pts, n):
        fill_circle(mask, x, y, max(0.7, r))


TR = [(44, 3, 3, 128), (48, 9, 10, 128), (54, 16, 17, 128), (62, 21, 22, 128),
      (72, 23, 24, 128), (82, 24, 26, 128), (92, 25, 27, 127), (100, 29, 32, 128),
      (108, 34, 37, 129), (118, 36, 39, 129), (130, 34, 37, 129), (142, 32, 35, 128),
      (154, 33, 36, 128), (166, 36, 39, 128), (178, 40, 44, 128), (190, 44, 48, 128),
      (202, 47, 52, 128), (210, 44, 50, 128), (217, 34, 38, 128)]


def interp(pts, y):
    if y <= pts[0][0]:
        return pts[0][1:]
    for i in range(len(pts) - 1):
        y0 = pts[i][0]
        y1 = pts[i + 1][0]
        if y0 <= y <= y1:
            t = (y - y0) / float(y1 - y0)
            return tuple(pts[i][k] + (pts[i + 1][k] - pts[i][k]) * t for k in (1, 2, 3))
    return pts[-1][1:]


def smooth(a, w=4, passes=3):
    a = list(a)
    for _ in range(passes):
        b = []
        for i in range(len(a)):
            s = 0.0
            n = 0
            for k in range(-w, w + 1):
                j = clamp(i + k, 0, len(a) - 1)
                s += a[j]
                n += 1
            b.append(s / n)
        a = b
    return a


YS = list(range(44, 218))
WL, WR, CX = [], [], []
for y in YS:
    wl, wr, cx = interp(TR, y)
    WL.append(wl)
    WR.append(wr)
    CX.append(cx)
WL, WR, CX = smooth(WL), smooth(WR), smooth(CX)
for i, y in enumerate(YS):
    x0 = int(round(CX[i] - WL[i]))
    x1 = int(round(CX[i] + WR[i]))
    for x in range(x0, x1 + 1):
        if 0 <= x < W:
            body[y][x] = 1

# knobby crown
for (x, y, r) in [(120, 50, 9), (137, 49, 8), (128, 45, 10), (110, 58, 7), (146, 60, 7)]:
    fill_circle(body, x, y, r)
# shoulders
fill_circle(body, 101, 112, 16)
fill_circle(body, 155, 112, 17)
fill_circle(body, 96, 124, 12)
fill_circle(body, 160, 124, 12)

# arms
add_limb(body, [(106, 114, 15), (86, 104, 12), (72, 94, 9), (60, 84, 7), (52, 74, 5.5)])
add_limb(body, [(150, 114, 16), (168, 106, 13), (184, 98, 10), (198, 86, 7), (208, 76, 5.5), (212, 70, 5)])

# left hand claws
add_limb(body, [(52, 72, 5.5), (49, 60, 4), (45, 50, 3), (41, 42, 2.2), (38, 36, 0.9)])
add_limb(body, [(50, 72, 5.5), (49, 60, 4), (50, 50, 3), (52, 42, 2.2), (54, 36, 0.9)])
add_limb(body, [(48, 74, 5.5), (40, 70, 4), (31, 66, 3), (22, 62, 2.2), (14, 60, 0.9)])
add_limb(body, [(46, 76, 3.4), (37, 77, 2.6), (28, 79, 1.2)])
add_limb(body, [(50, 52, 2.2), (43, 46, 1.2)])
# right hand claws
add_limb(body, [(212, 68, 5.5), (216, 58, 4), (220, 48, 3), (225, 36, 2.2), (230, 24, 0.9)])
add_limb(body, [(210, 68, 5.5), (208, 56, 4), (207, 44, 3), (208, 32, 2.2), (210, 20, 0.9)])
add_limb(body, [(212, 72, 5.5), (222, 68, 4), (232, 62, 3), (242, 56, 2.2), (250, 52, 0.9)])
add_limb(body, [(208, 74, 3.4), (216, 80, 2.6), (226, 84, 1.2)])
add_limb(body, [(208, 46, 2.2), (202, 40, 1.2)])

# shoulder stumps / broken branches
add_limb(body, [(110, 100, 6), (106, 90, 4.5), (104, 82, 2.6)])
add_limb(body, [(148, 100, 6), (150, 90, 4.5), (152, 84, 2.4)])

# roots
add_limb(body, [(104, 198, 17), (86, 206, 13), (68, 212, 10), (52, 218, 7), (40, 224, 4), (32, 230, 2)])
add_limb(body, [(152, 198, 17), (170, 206, 13), (188, 212, 10), (204, 218, 7), (216, 224, 4), (224, 230, 2)])
add_limb(body, [(128, 206, 15), (126, 218, 11), (124, 228, 7), (122, 238, 3)])
add_limb(body, [(120, 208, 13), (110, 218, 9), (102, 226, 6), (96, 234, 3)])
add_limb(body, [(138, 208, 13), (146, 218, 9), (154, 226, 6), (160, 234, 3)])
# rising roots
add_limb(body, [(62, 230, 6), (60, 216, 4.5), (57, 204, 3), (54, 192, 1.5), (52, 182, 0.7)])
add_limb(body, [(86, 234, 6), (86, 220, 4), (87, 208, 2.5), (88, 198, 1.2)])
add_limb(body, [(176, 234, 6), (178, 222, 4), (180, 210, 2.5), (182, 200, 1.2)])
add_limb(body, [(200, 230, 6), (204, 216, 4.5), (208, 204, 3), (212, 192, 1.5), (214, 182, 0.7)])
add_limb(body, [(112, 238, 5), (110, 226, 3.5), (108, 216, 2), (107, 208, 1.0)])
add_limb(body, [(150, 238, 5), (152, 226, 3.5), (154, 216, 2), (155, 208, 1.0)])

# ------------------------------------------------------------------ 6. distance field
INF = 4000
dist = [[0 if not body[y][x] else INF for x in range(W)] for y in range(H)]
dq = deque()
for y in range(H):
    row = body[y]
    for x in range(W):
        if not row[x]:
            dq.append((x, y))
while dq:
    x, y = dq.popleft()
    d = dist[y][x] + 1
    if x > 0 and dist[y][x - 1] > d:
        dist[y][x - 1] = d
        dq.append((x - 1, y))
    if x < W - 1 and dist[y][x + 1] > d:
        dist[y][x + 1] = d
        dq.append((x + 1, y))
    if y > 0 and dist[y - 1][x] > d:
        dist[y - 1][x] = d
        dq.append((x, y - 1))
    if y < H - 1 and dist[y + 1][x] > d:
        dist[y + 1][x] = d
        dq.append((x, y + 1))

# ------------------------------------------------------------------ 7. paint treant
LX, LY = 0.72, -0.69
MOSS_BLOBS = [(128, 48, 16, 10), (112, 60, 9, 7), (146, 60, 9, 7),
              (100, 112, 11, 8), (158, 114, 11, 8), (94, 132, 9, 13),
              (164, 146, 8, 11), (112, 194, 20, 14), (150, 196, 17, 11),
              (122, 172, 11, 9), (86, 102, 10, 6), (172, 102, 10, 6),
              (64, 84, 6, 5), (198, 78, 6, 5), (100, 146, 7, 9),
              (158, 170, 7, 9), (128, 208, 16, 8)]

for y in range(H):
    for x in range(W):
        if not body[y][x]:
            continue
        d = dist[y][x]
        gx = dist[y][min(W - 1, x + 1)] - dist[y][max(0, x - 1)]
        gy = dist[min(H - 1, y + 1)][x] - dist[max(0, y - 1)][x]
        if gx == 0 and gy == 0:
            nx_, ny_ = 0.0, 0.0
        else:
            l = math.hypot(gx, gy)
            nx_, ny_ = -gx / l, -gy / l
        lit = nx_ * LX + ny_ * LY
        f = 1.0 if d <= 2 else max(0.0, 1.0 - (d - 2) / 11.0)
        tv = 2.3 + 2.4 * lit * f
        # bark grooves
        gxs = x + 2.2 * math.sin(y * 0.10 + 1.3) + 1.1 * math.sin(y * 0.33)
        m = gxs % 10.0
        if m < 1.8:
            tv -= 1.7
        elif m < 2.8:
            tv -= 0.7
        hy = y + 1.6 * math.sin(x * 0.21)
        if (hy % 19.0) < 1.4:
            tv -= 1.0
        tv += (fbm(x, y, 0.42, 5, 2) - 0.5) * 0.9
        idx = clamp(int(tv + 0.5), 0, 5)
        col = BARK[idx]
        # moss
        best = -9.0
        for (mx, my, rx, ry) in MOSS_BLOBS:
            s = 1.0 - ((x - mx) / rx) ** 2 - ((y - my) / ry) ** 2
            if s > best:
                best = s
        if best > 0.05:
            mm = best + (fbm(x * 0.9, y * 0.42, 0.30, 9, 3) - 0.5) * 1.05
            if mm > 0.30:
                mt = 1.7 + (0.8 if lit > 0.12 else -0.6) + (fbm(x, y, 0.5, 31, 2) - 0.5) * 1.4
                col = MOSS[clamp(int(mt + 0.5), 0, 3)]
        # lichen speckles
        if h2(x, y, 11) > 0.985 and idx >= 1:
            col = LICH
        tr.set(x, y, col)

# ------------------------------------------------------------------ 8. bark details
def crack(pts, col=BARK[0]):
    for i in range(len(pts) - 1):
        tr.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], col)


for pts in [
    [(120, 128), (118, 142), (121, 156), (119, 170), (121, 182)],
    [(139, 132), (141, 148), (138, 162), (140, 176)],
    [(106, 96), (107, 108), (105, 120)],
    [(148, 92), (147, 104)],
    [(112, 176), (110, 190), (112, 200)],
    [(146, 178), (148, 192)],
    [(96, 140), (94, 152)],
    [(160, 140), (162, 154)],
]:
    crack(pts)

# knots
for (kx, ky, rx, ry) in [(151, 146, 8, 6), (104, 160, 6, 5), (146, 188, 6, 5), (114, 140, 5, 4)]:
    tr.ellipse(kx, ky, rx, ry, BARK[1], fill=False)
    tr.ellipse(kx, ky, rx - 2, ry - 2, BARK[0])
    tr.ellipse(kx - 1, ky - 1, rx - 4, ry - 3, BARK[1])

# ------------------------------------------------------------------ 9. face
def eye(cx, cy, s):
    def ring(sc, col):
        pts = []
        for i in range(9):
            t = -1.0 + 2.0 * i / 8.0
            h = 4.9 * sc * math.sqrt(max(0.0, 1.0 - t * t))
            pts.append((cx + 7.6 * sc * t, cy + 2.6 * s * t - h))
        for i in range(8, -1, -1):
            t = -1.0 + 2.0 * i / 8.0
            h = 4.9 * sc * math.sqrt(max(0.0, 1.0 - t * t))
            pts.append((cx + 7.6 * sc * t, cy + 2.6 * s * t + h))
        tr.poly(pts, col)
    ring(1.00, "#221a0c")
    ring(0.78, EYE[0])
    ring(0.54, EYE[1])
    ring(0.30, EYE[2])
    tr.rect(cx - 1, cy - 1, 2, 2, EYE[4])
    tr.set(cx + 2, cy + s, EYE[3])
    tr.set(cx - 2, cy, EYE[3])
    for (dx, dy) in ((-4, 5), (-2, 6), (0, 6), (2, 6), (4, 5), (-6, 7), (6, 7)):
        if 0 <= cx + dx < W and 0 <= cy + dy < H:
            tr.set(cx + dx, cy + dy, EYE[0])


eye(116, 86, -1)
eye(140, 86, 1)
# brow ridges
for sgn in (-1, 1):
    tr.poly([(128 + sgn * 3, 74), (128 + sgn * 17, 79), (128 + sgn * 17, 82), (128 + sgn * 3, 78)], BARK[0])

# maw crack
maw = [(104, 116), (112, 113), (118, 119), (126, 114), (134, 120), (142, 115),
       (150, 118), (152, 126), (143, 124), (135, 129), (126, 124), (118, 130),
       (110, 125), (104, 126)]
tr.poly(maw, "#0a0602")
tr.poly([(112, 116), (118, 121), (126, 117), (134, 122), (142, 117), (146, 120), (144, 122), (135, 124), (126, 120), (118, 124), (112, 120)], EYE[0])
for (mx, my) in [(120, 118), (131, 120), (139, 119), (126, 121)]:
    tr.set(mx, my, EYE[1])
    tr.set(mx + 1, my, EYE[2])

# ------------------------------------------------------------------ 10. outline
edge = []
for y in range(H):
    row = body[y]
    for x in range(W):
        if not row[x]:
            continue
        if (x == 0 or not row[x - 1]) or (x == W - 1 or not row[x + 1]) or \
           (y == 0 or not body[y - 1][x]) or (y == H - 1 or not body[y + 1][x]):
            edge.append((x, y))
for (x, y) in edge:
    tr.set(x, y, DARK)

# ------------------------------------------------------------------ 11. vines
VINES = [
    [(78, 92), (76, 110), (74, 128), (77, 145), (73, 162)],
    [(96, 120), (94, 138), (97, 156), (93, 175)],
    [(164, 116), (167, 136), (163, 154), (166, 172)],
    [(186, 98), (188, 118), (185, 138), (188, 156)],
    [(58, 66), (56, 82), (59, 98)],
    [(206, 96), (204, 114), (207, 132)],
    [(112, 60), (110, 74)],
    [(146, 58), (149, 72)],
    [(120, 176), (118, 196), (121, 210)],
    [(158, 168), (160, 188)],
]
for v in VINES:
    for i in range(len(v) - 1):
        tr.line(v[i][0], v[i][1], v[i + 1][0], v[i + 1][1], VINE[1])
    # leaves
    for i in range(0, len(v) - 1):
        x0, y0 = v[i]
        x1, y1 = v[i + 1]
        for t in (0.45, 0.8):
            lx = int(x0 + (x1 - x0) * t)
            ly = int(y0 + (y1 - y0) * t)
            tr.set(lx + 1, ly, MOSS[2])
            tr.set(lx + 2, ly, MOSS[1])
            tr.set(lx - 1, ly + 1, MOSS[1])
            tr.set(lx - 2, ly + 1, MOSS[0])

# ------------------------------------------------------------------ 12. foreground
for x in range(W):
    for k in range(3):
        if h2(x, k, 3) > 0.55:
            continue
        hgt = 3 + int(h2(x, k, 7) * 9)
        bx = x + (k - 1) * 2
        if not (0 <= bx < W):
            continue
        base = gt[bx] + 1
        for i in range(hgt):
            xx = bx + int(round(math.sin(i * 0.5 + x) * 1.2)) + (i * (k - 1)) // 3
            yy = base - i
            if 0 <= xx < W and 0 <= yy < H:
                fg.set(xx, yy, MOSS[1] if i < hgt - 2 else MOSS[2])

# dark foreground grass mass at the bottom
for x in range(W):
    top = 244 + int(4 * math.sin(x * 0.06))
    for y in range(top, H):
        fg.set(x, y, SOIL[0] if y > top + 2 else SOIL[1])
for x in range(0, W, 5):
    hgt = 6 + int(h2(x, 1, 13) * 12)
    for i in range(hgt):
        xx = x + int(round(math.sin(i * 0.4 + x) * 1.5))
        yy = 245 - i
        if 0 <= xx < W and 0 <= yy < H and fg.get(xx, yy) == fg.get(0, 250):
            fg.set(xx, yy, SOIL[0])

# little ferns near the roots
for (fx, fy) in [(70, 210), (188, 212), (100, 218), (160, 216)]:
    for a in (-1.0, -0.5, 0.0, 0.5, 1.0):
        for i in range(7):
            xx = int(fx + math.sin(a) * i * 1.3)
            yy = int(fy - i * 1.2 + abs(a) * i * 0.9)
            if 0 <= xx < W and 0 <= yy < H:
                fg.set(xx, yy, MOSS[1] if i < 5 else MOSS[3])

# glowing motes
for (mx, my, r) in [(58, 150, 1), (74, 176, 0), (196, 140, 1), (210, 168, 0),
                    (44, 120, 0), (176, 120, 1), (90, 190, 0), (150, 148, 0),
                    (230, 96, 0), (30, 96, 0)]:
    fg.set(mx, my, EYE[4])
    if r:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            fg.set(mx + dx, my + dy, EYE[3])

# ------------------------------------------------------------------ 12b. extra hanging vines from arms
for v in ([(62, 78), (60, 92), (62, 106), (59, 118)],
          [(198, 82), (200, 96), (197, 110), (200, 122)],
          [(84, 100), (82, 114)],
          [(174, 104), (176, 118), (173, 132)],
          [(128, 214), (126, 228)]):
    for i in range(len(v) - 1):
        tr.line(v[i][0], v[i][1], v[i + 1][0], v[i + 1][1], VINE[0])
        tr.line(v[i][0] + 1, v[i][1], v[i + 1][0] + 1, v[i + 1][1], VINE[1])
    x0, y0 = v[-1]
    tr.set(x0, y0 + 1, MOSS[2])
    tr.set(x0 + 1, y0 + 1, MOSS[1])
    tr.set(x0 - 1, y0 + 2, MOSS[0])

# ------------------------------------------------------------------ 13. compose
out = flatten([bg, tr, fg], name="result")

print(out.stats_text())
save("ancient-treant-boss", out)
finish(out)


def cls(r, g, b):
    v = max(r, g, b)
    if v < 24:
        return "K"
    return "?"


def palmap(canv):
    m = {}
    for p in canv.palette():
        i = p["index"]
        r, g, b, a = p["rgba"]
        h = str(canv.color_name(i)).lower()
        if len(h) == 9 and h.startswith("#"):
            h = h[:7]
        m[i] = " " if a == 0 else CH.get(h, cls(r, g, b))
    return m


def ascii_map(canv, step=4):
    pal = palmap(canv)
    lines = []
    for y in range(0, H, step):
        row = ""
        for x in range(0, W, step):
            row += pal.get(canv.get(x, y), "?")
        lines.append(row)
    return "\n".join(lines)


def region_map(canv, x0, y0, x1, y1):
    pal = palmap(canv)
    lines = []
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            row += pal.get(canv.get(x, y), "?")
        lines.append("%3d %s" % (y, row))
    return "\n".join(lines)


print(ascii_map(out, 4))
print("--- face (100,68)-(160,110) ---")
print(region_map(out, 100, 68, 160, 110))
print("--- maw/base (96,108)-(164,150) ---")
print(region_map(out, 96, 108, 164, 150))
