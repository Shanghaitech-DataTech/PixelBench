import math
from pixelbench_api import new_canvas, finish

W = H = 64
CX, CY, SC = 31.5, 35.0, 23.0
INF = float('inf')

def clamp(v, a, b):
    if v < a: return a
    if v > b: return b
    return v

def noise(x, y, s):
    v = math.sin(x * 127.1 + y * 311.7 + s * 74.7) * 43758.5453
    return v - math.floor(v)

def seg_dist(x, y, x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    L2 = dx * dx + dy * dy
    t = clamp(((x - x0) * dx + (y - y0) * dy) / L2, 0.0, 1.0)
    return math.hypot(x - (x0 + t * dx), y - (y0 + t * dy))

def in_heart(x, y):
    nx = (x - CX) / SC
    ny = (CY - y) / SC
    v = (nx * nx + ny * ny - 1.0) ** 3 - nx * nx * ny ** 3
    if v > 0.0:
        return False
    dx, dy = nx, ny - 0.90          # deepen the notch between the lobes
    if (dx / 0.30) ** 2 + (dy / 0.30) ** 2 < 1.0:
        return False
    return True

def in_vessel(x, y):
    if seg_dist(x, y, 31.0, 10.0, 30.0, -10.0) <= 3.8:
        return True
    if seg_dist(x, y, 37.8, 12.0, 45.0, -10.0) <= 2.8:
        return True
    return False

def in_mask(x, y):
    return in_heart(x, y) or in_vessel(x, y)

def build_mask():
    m = [[False] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            m[y][x] = in_mask(x, y)
    return m

def dist_field(mask):
    d = [[INF if mask[y][x] else 0 for x in range(W)] for y in range(H)]
    for y in range(H):
        for x in range(W):
            if d[y][x]:
                b = d[y][x]
                if y and d[y - 1][x] + 1 < b: b = d[y - 1][x] + 1
                if x and d[y][x - 1] + 1 < b: b = d[y][x - 1] + 1
                d[y][x] = b
    for y in range(H - 1, -1, -1):
        for x in range(W - 1, -1, -1):
            if d[y][x]:
                b = d[y][x]
                if y < H - 1 and d[y + 1][x] + 1 < b: b = d[y + 1][x] + 1
                if x < W - 1 and d[y][x + 1] + 1 < b: b = d[y][x + 1] + 1
                d[y][x] = b
    return d

def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t)

# ---- fixed palette (58 colours, well under the 86 limit) ----
pal = []
for i in range(36):
    t = i / 35.0
    pal.append((round(48 + 202 * t), round(10 + 52 * t), round(18 + 86 * t)))
for i in range(14):
    t = i / 13.0
    pal.append((round(215 + 40 * t), round(140 + 105 * t), round(152 + 94 * t)))
for r, g, b in [(22, 4, 9), (30, 6, 13), (38, 9, 17), (14, 3, 6),
               (60, 13, 24), (80, 18, 32), (255, 246, 246), (250, 228, 232)]:
    pal.append((r, g, b))

def quant(rgb):
    best, bi = 1e18, 0
    r, g, b = rgb
    for i, p in enumerate(pal):
        dr = r - p[0]; dg = g - p[1]; db = b - p[2]
        e = dr * dr * 3 + dg * dg * 4 + db * db * 2
        if e < best:
            best, bi = e, i
    return pal[bi]

VEINS = [
    [(33, 11), (35, 17), (34, 23), (31, 29), (30, 35), (31, 41), (31.5, 47), (32, 50)],
    [(34, 20), (37, 25), (41, 30), (43, 36), (44, 42)],
    [(31.5, 25), (27.5, 30), (24.5, 33.5), (22, 36)],
    [(37.5, 15), (40, 19)],
    [(29.5, 16), (28, 21)],
    [(26, 27), (22.5, 30), (19.5, 32)],
    [(42, 26), (45.5, 30), (48, 34)],
]

def vein_dist(x, y):
    best = INF
    for vein in VEINS:
        for i in range(len(vein) - 1):
            dd = seg_dist(x, y, vein[i][0], vein[i][1], vein[i + 1][0], vein[i + 1][1])
            if dd < best:
                best = dd
    return best

def main():
    mask = build_mask()

    # silhouette preview (rows that exist: y: minx-maxx)
    rows = [(y, xs[0], xs[-1]) for y in range(H) if (xs := [x for x in range(W) if mask[y][x]])]
    print("rows_with_pixels:", len(rows))
    print("extents:", rows)

    d = dist_field(mask)
    c = new_canvas(W, H)

    for y in range(H):
        for x in range(W):
            if not mask[y][x]:
                continue
            dd = d[y][x]
            ao = clamp(dd / 6.0, 0.0, 1.0)
            n = noise(x, y, 5.0)

            if in_vessel(x, y):
                u = 0.50 + 0.25 * ((y + 8.0) / 24.0)
                u = clamp(u, 0.30, 0.78)
                u *= (0.55 + 0.45 * ao)
                u += 0.05 * (n - 0.5)
                target = lerp((52, 10, 18), (165, 40, 52), clamp(u, 0.0, 1.0))
                target = lerp(target, (120, 26, 42), 0.15)
                if dd < 1.6:
                    target = lerp(target, (30, 7, 13), 0.55)
            else:
                u = 0.78 - 0.44 * ((y - 30.0) / 32.0)
                u *= (0.48 + 0.52 * ao ** 0.7)
                u += 0.05 * (1.0 - abs(x - 33.0) / 26.0)
                u = clamp(u, 0.0, 1.0)
                u += 0.09 * (n - 0.5)
                u = clamp(u, 0.0, 1.0)
                target = lerp(pal[0], pal[35], u)

                g1 = math.exp(-(((x - 24.5) / 6.8) ** 2 * 0.65 + ((y - 20.0) / 8.2) ** 2 * 0.75))
                target = lerp(target, (253, 224, 230), min(1.0, g1 ** 1.25))
                g2 = math.exp(-(((x - 41.0) / 5.2) ** 2 * 0.6 + ((y - 21.0) / 6.2) ** 2 * 0.7))
                target = lerp(target, (255, 212, 222), min(1.0, g2 ** 1.35) * 0.40)
                g3 = math.exp(-(((x - 23.5) / 4.6) ** 2 * 0.7 + ((y - 15.5) / 5.2) ** 2 * 0.8))
                target = lerp(target, (255, 234, 236), min(1.0, g3 ** 1.3) * 0.55)

                vd = vein_dist(x, y)
                if vd < 2.2:
                    target = lerp(target, (62, 12, 24), 0.62 * (1.0 - vd / 2.2))
                if dd < 1.3:
                    target = lerp(target, (26, 5, 10), 0.5 * (1.0 - dd / 1.3))
                if dd < 0.6:
                    target = lerp(target, (16, 3, 7), 0.5)

            c.set(x, y, quant(target))

    print(c.stats_text())

    pal_by_idx = {d['index']: d['rgba'] for d in c.palette()}
    # ASCII brightness map so I can read the composition
    def lum(rgb):
        return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    ch = ['1', '2', '3', '4', '5']
    bucket = lambda L: ch[min(4, max(0, int(L / 33.0)))]
    for yy in range(H):
        row = ''
        for xx in range(W):
            if not mask[yy][xx]:
                row += '.'
                continue
            pix = c.get(xx, yy)
            row += bucket(lum(pal_by_idx[pix][:3]))
        print(row)
    finish(c)

main()
