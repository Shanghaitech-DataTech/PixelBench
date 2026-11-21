import math

W = H = 64
c = new_canvas(W, H, name="terraces")

# ---------------------------------------------------------------- helpers
def hx(s):
    s = s.lstrip('#')
    return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))

def tohex(t):
    return '#%02x%02x%02x' % (max(0, min(255, int(round(t[0])))),
                              max(0, min(255, int(round(t[1])))),
                              max(0, min(255, int(round(t[2])))))

def lerp(a, b, t):
    a = hx(a) if isinstance(a, str) else a
    b = hx(b) if isinstance(b, str) else b
    return tohex(tuple(a[i] + (b[i] - a[i]) * t for i in range(3)))

def hsh(a, b):
    v = (a * 374761393 + b * 668265263 + 1013904223) & 0xffffffff
    v = ((v ^ (v >> 13)) * 1274126177) & 0xffffffff
    v = v ^ (v >> 16)
    return v & 0x7fffffff

# ---------------------------------------------------------------- terrain
BASES = [10, 16, 23, 31, 40, 50, 59]
N = len(BASES)          # contour ridges; field band k = 0..N-1

def shape(x):
    return (3.2 * math.sin(x * 0.055 + 0.6)
            + 1.6 * math.sin(x * 0.130 + 2.0)
            + 0.8 * math.sin(x * 0.290 + 0.3))

def ridge_y(k, x):
    f = 0.26 + 0.085 * k
    arch = (1.2 + 0.55 * k) * math.cos((x - 32) / 32.0 * (math.pi / 2))
    return BASES[k] + shape(x) * f + 1.0 * math.sin(x * 0.21 + k * 2.1) - arch

RIDGE = [[int(round(ridge_y(k, x))) for x in range(W)] for k in range(N)]

KIND = ['crop', 'crop', 'harvest', 'crop', 'stubble', 'harvest', 'crop']

def ramp(k):
    t = k / float(N - 1)
    return dict(
        wall=lerp('#8d7d51', '#40290c', t),
        bund=lerp('#eee3b6', '#f0c05e', t),
        base=lerp('#d6c793', '#c07f22', t),
        lite=lerp('#e9dfb4', '#f0c258', t),
        dark=lerp('#b3a878', '#8a5514', t),
        stub=lerp('#e2d8ac', '#dcae52', t),
        stubd=lerp('#c4b98a', '#a97a30', t),
    )

RAMPS = [ramp(k) for k in range(N)]
MIX = [lerp(RAMPS[k]['stub'], RAMPS[k]['base'], 0.45) for k in range(N)]

# distant hill tones (quantized)
HAZE = '#e0e0c6'
HILLM = '#cfc99b'
HILL = '#b8b281'
FARTREE = '#8b9469'
FARTREE2 = '#79855c'

# village / trees / figures
ROOF = '#7d5a38'; ROOFR = '#a8845a'; EAVE = '#4f3722'
WALL = '#d8c8a4'; WALLS = '#9c8a64'
TREE_D = '#3c5a2b'; TREE_L = '#5f7f3d'
HAT = '#f0e0b0'; HATD = '#c8ac72'
CLOTH1 = '#39465e'; CLOTH2 = '#6b3a3a'
POLE = '#5d4022'; BUNDLE = '#e6c268'; LEGS = '#2c2c34'

# ---------------------------------------------------------------- base pass
for x in range(W):
    for y in range(H):
        b = 0
        while b < N and y >= RIDGE[b][x]:
            b += 1
        if b == 0:
            ry = max(1, RIDGE[0][x])
            t = y / float(ry)
            col = HAZE if t < 0.40 else (HILLM if t < 0.75 else HILL)
            u = hsh(x // 2, y // 2) % 13
            if u == 0:
                col = FARTREE
            elif u == 1:
                col = FARTREE2
            c.set(x, y, col)
            continue

        k = b - 1
        R = RAMPS[k]
        d = y - RIDGE[k][x]
        kind = KIND[k]
        wallth = 2 if k >= 4 else 1

        if d < wallth:
            col = R['wall']
        elif d == wallth:
            col = R['bund']
        else:
            dd = d - wallth
            u = hsh(x + k * 91, dd * 7 + k * 3) % 100
            if kind == 'crop':
                m = dd % 3
                if m == 0:
                    col = R['lite']
                elif m == 1:
                    col = R['base']
                else:
                    col = R['dark'] if u < 30 else R['base']
                if u >= 96:
                    col = R['lite']
            elif kind == 'harvest':
                if dd % 3 == 1:
                    col = R['stubd']
                elif u < 12:
                    col = R['dark']
                elif u >= 97:
                    col = R['bund']          # cut sheaf dot
                else:
                    col = R['stub'] if u < 60 else MIX[k]
            else:  # stubble
                col = R['stubd'] if dd % 2 == 0 else R['stub']
                if u < 8:
                    col = R['dark']
        c.set(x, y, col)

# faint terrace contours on the distant hillside
for x in range(W):
    arch = math.cos((x - 32) / 32.0 * (math.pi / 2))
    c.set(x, int(round(4 + shape(x) * 0.15 - 0.7 * arch)), HILLM)
    c.set(x, int(round(7 + shape(x) * 0.22 - 1.0 * arch)), HILL)

# ---------------------------------------------------------------- footpath
for y in range(RIDGE[0][34], H):
    px = 34 + int(round(2.4 * math.sin(y * 0.16) + 1.2 * math.sin(y * 0.07)))
    b = 0
    while b < N and y >= RIDGE[b][px]:
        b += 1
    if b > 0:
        c.set(px, y, RAMPS[b - 1]['bund'])

# ---------------------------------------------------------------- village
def house(hx0, hy0, w, h):
    c.rect(hx0, hy0, w, h, ROOF)
    c.line(hx0, hy0 + (1 if h > 2 else 0), hx0 + w - 1, hy0 + (1 if h > 2 else 0), ROOFR)
    c.line(hx0, hy0 + h - 1, hx0 + w - 1, hy0 + h - 1, EAVE)
    c.rect(hx0, hy0 + h, w, 1, WALL)
    c.line(hx0, hy0 + h + 1, hx0 + w - 1, hy0 + h + 1, WALLS)

def tree(tx, ty, r, dark, lite):
    c.circle(tx, ty, r, dark)
    c.set(tx - (1 if r > 1 else 0), ty - (1 if r > 1 else 0), lite)

village = [(6, 4, 3), (11, 3, 4), (17, 4, 3), (23, 3, 4), (29, 4, 3)]
for (sx, hh, ww) in village:
    top = RIDGE[0][sx + ww // 2] - hh - 2
    house(sx, max(1, top), ww, hh)

# tree line hugging the far contour, skipping the village span
for tx in range(0, W):
    if 4 <= tx <= 34:
        continue
    if hsh(tx, 7) % 4 != 0:
        continue
    c.set(tx, RIDGE[0][tx] - 1, TREE_D if hsh(tx, 3) % 2 else FARTREE2)

# scattered trees on terrace bunds
for (k, tx) in [(1, 47), (2, 3), (3, 58), (4, 8), (5, 52), (6, 26)]:
    tree(tx, RIDGE[k][tx] - 1, 1 if k < 4 else 2, TREE_D, TREE_L)

# ---------------------------------------------------------------- farmers
def farmer(fx, fy, pole=False, cloth=CLOTH1, carry=False):
    if carry:
        c.set(fx + 1, fy - 1, BUNDLE)
        c.set(fx, fy - 1, BUNDLE); c.set(fx + 2, fy - 1, BUNDLE)
    c.set(fx + 1, fy, HAT)
    c.set(fx, fy + 1, HAT); c.set(fx + 1, fy + 1, HATD); c.set(fx + 2, fy + 1, HAT)
    c.set(fx, fy + 2, cloth); c.set(fx + 1, fy + 2, cloth); c.set(fx + 2, fy + 2, cloth)
    c.set(fx + 1, fy + 3, LEGS)
    if pole:
        c.line(fx - 2, fy + 1, fx - 1, fy + 1, POLE)
        c.line(fx + 3, fy + 1, fx + 4, fy + 1, POLE)
        c.set(fx - 2, fy + 2, BUNDLE); c.set(fx + 4, fy + 2, BUNDLE)

# harvested sheaf stooks standing in the cut fields
for (k, sx) in [(2, 12), (2, 40), (5, 16), (5, 30), (5, 58)]:
    sy = RIDGE[k][sx] + 4
    c.set(sx, sy - 1, BUNDLE)
    c.set(sx - 1, sy, BUNDLE); c.set(sx, sy, BUNDLE); c.set(sx + 1, sy, BUNDLE)
    c.set(sx, sy + 1, RAMPS[k]['stubd'])

f1x = 20; f1y = RIDGE[3][f1x] + 1 - 3
farmer(f1x, f1y, pole=True)
f2x = 44; f2y = RIDGE[5][f2x] + 2 - 3
farmer(f2x, f2y, carry=True, cloth=CLOTH2)

print(c.stats_text())
view(c)
save('terraces', c)
finish(c)
