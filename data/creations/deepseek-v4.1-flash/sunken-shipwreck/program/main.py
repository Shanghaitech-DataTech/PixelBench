import math
from pixelbench_api import *

# ============================================================
#  SUNKEN SHIPWRECK  -  64x64
# ============================================================
c = new_canvas(64, 64, '#123f54')

# ---------------- palette ----------------
WATER = ['#4fa9bd','#4299ae','#3789a0','#2d7a91','#256b82','#1d5c73','#174d63','#123f54']
RAY   = '#63bfcd'
SAND_L= '#ecdcaa'; SAND = '#d3bd8b'; SAND_M = '#bda675'; SAND_D = '#9d855c'; SAND_X = '#806a46'
WOOD_L= '#a37f55'; WOOD = '#7b5c3c'; WOOD_D = '#553f27'; WOOD_X = '#382718'; WOOD_S = '#241a10'
PAT_L = '#7ba98c'; PAT  = '#4e7f6a'; PAT_D  = '#33564a'
COR_L = '#f8b394'; COR  = '#e2705f'; COR_D  = '#b94a3d'
KEL_L = '#66b366'; KEL  = '#429157'; KEL_D  = '#2b6b40'
FISH  = '#0b3149'; FISH_M = '#a8cac6'; FISH_L = '#e6eeda'
BUB   = '#c8ecf4'; SAIL_L = '#ded6ba'; SAIL   = '#b4ac90'; SAIL_D = '#8a8268'; ROPE = '#a08a5e'

# ---------------- water gradient ----------------
for y in range(64):
    c.rect(0, y, 64, 1, WATER[y // 8])
for y in range(8, 64, 8):
    prev = WATER[y // 8 - 1]
    for x in range(64):
        if (x + y) % 2 == 0:
            c.set(x, y, prev)

# ---------------- light rays ----------------
for (x0, w0) in ((6, 3), (21, 2), (43, 3), (54, 2)):
    for y in range(0, 36):
        xs = x0 + y // 3
        ww = max(1, w0 - y // 15)
        for x in range(xs, xs + ww):
            if 0 <= x < 64 and (x + 2 * y) % 3 == 0:
                c.set(x, y, RAY)

# ============================================================
#  SHIP  (own canvas, rotated, then pasted)
# ============================================================
sc = new_canvas(52, 26)

DECK = [(2,8),(49,5),(48,2),(3,5)]
HS   = [(2,8),(3,17),(8,20),(16,23),(26,25),(37,24.5),(45,21),(49,15),(49,5)]

def inside(poly, x, y):
    n = len(poly); j = n - 1; odd = False
    for i in range(n):
        xi, yi = poly[i]; xj, yj = poly[j]
        if (yi > y) != (yj > y):
            xint = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < xint:
                odd = not odd
        j = i
    return odd

def y_n(x):
    return 8 - 3.0 * (x - 2) / 47

def y_d(x):
    return 5 - 3.0 * (x - 3) / 45

def blob(cv, cx, cy, r, col, filt=None):
    for ly in range(int(cy - r) - 1, int(cy + r) + 2):
        for lx in range(int(cx - r) - 1, int(cx + r) + 2):
            if (lx - cx) ** 2 + (ly - cy) ** 2 <= r * r:
                if filt is None or filt(lx, ly):
                    cv.set(lx, ly, col)

# --- open-deck strip ---
sc.poly(DECK, WOOD_X)
for rx in range(7, 49, 6):
    sc.line(rx, int(round(y_d(rx))), rx, int(round(y_n(rx))), WOOD_S)
# broken frames poking above the deck line
for rx, hh in ((10, 4), (22, 6), (34, 3), (45, 5), (16, 2), (40, 3)):
    y0 = int(round(y_d(rx)))
    sc.line(rx, y0, rx, y0 - hh, WOOD_D)
    sc.line(rx + 1, y0, rx + 1, y0 - hh + 1, WOOD_D)
    sc.set(rx, y0 - hh, WOOD)
    sc.set(rx + 1, y0 - hh, WOOD_D)
# ragged edge of the strip
for x in range(4, 49):
    if (x * 37) % 11 < 3:
        sc.set(x, int(round(y_d(x))), None)

# --- hull side with curved shading ---
sc.poly(HS, WOOD)
for x in range(2, 50):
    yn = y_n(x)
    for y in range(6, 27):
        if not inside(HS, x, y):
            continue
        dy = y - yn
        if dy < 0:
            continue
        if dy <= 1.6:
            col = WOOD_L
        elif dy <= 7.6:
            col = WOOD
        elif dy <= 13.6:
            col = WOOD_D
        else:
            col = WOOD_X
        sc.set(x, y, col)
# plank seams
for dy in (4, 9, 14):
    for x in range(2, 50):
        y = int(round(y_n(x) + dy))
        if inside(HS, x, y):
            sc.set(x, y, WOOD_X)
# butt joints
for bx in (16, 31, 42):
    for dy in range(2, 18):
        y = int(round(y_n(bx) + dy))
        if inside(HS, bx, y) and dy % 5 != 0 and dy not in (4, 9, 14):
            sc.set(bx, y, WOOD_X)

# --- corrosion / algae ---
blob(sc, 30, 14, 3, PAT,   lambda x, y: inside(HS, x, y))
blob(sc, 30, 12, 2, PAT_L, lambda x, y: inside(HS, x, y))
blob(sc, 44, 12, 3, PAT,   lambda x, y: inside(HS, x, y))
blob(sc, 8, 18, 2, PAT_D,  lambda x, y: inside(HS, x, y))
blob(sc, 21, 20, 2, PAT_D, lambda x, y: inside(HS, x, y))
# damage hole
sc.poly([(42,11),(45,11),(46,14),(44,16),(41,14)], WOOD_S)
# porthole
sc.rect(23, 15, 2, 2, WOOD_S)
sc.set(23, 15, PAT_L)
# nails
for nx in (8, 28, 46):
    sc.set(nx, int(round(y_n(nx))) + 2, WOOD_S)

# --- rotate & place ---
sel = sc.select(0, 0, 52, 26).rotate(9, 'nearest')
sw, sh = sel.size
sel.copy_to(30 - sw // 2, 43 - sh // 2, c, mode='over')

# ============================================================
#  MAST, SAIL, RIGGING
# ============================================================
c.line(10, 20, 26, 18, WOOD_D)
c.line(10, 19, 26, 17, WOOD_L)
c.set(9, 20, WOOD_X); c.set(27, 17, WOOD_X)
# sail
sail = [(11,21),(27,21),(28,28),(24,25),(22,30),(19,27),(17,30),(14,26),(11,28)]
c.poly(sail, SAIL)
for sy in range(20, 32):
    for sx in range(10, 30):
        if not inside(sail, sx, sy):
            continue
        if sy <= 23:
            c.set(sx, sy, SAIL_L)
        elif sy >= 27 and sx >= 19:
            c.set(sx, sy, SAIL_D)
for p in ((19,25),(23,23),(25,26),(20,28),(16,25),(13,24)):
    c.set(p[0], p[1], SAIL_D)
for p in ((13,22),(15,22),(24,22),(26,23),(18,26),(21,24)):
    c.set(p[0], p[1], SAIL_L)
# mast in front of the sail
for i in range(21):
    x = 20 - int(round(i * 0.10))
    y = 36 - i
    c.set(x, y, WOOD_L)
    c.set(x + 1, y, WOOD)
    c.set(x + 2, y, WOOD_X)
c.set(18, 15, WOOD_X); c.set(19, 15, WOOD_X); c.set(20, 15, WOOD_D)
c.set(19, 16, WOOD_D)

# ============================================================
#  SEA FLOOR
# ============================================================
ctrl = [(0,42),(6,42),(12,44),(18,46),(26,48),(34,48),(42,47),(50,46),(58,46),(63,48)]
def h_at(x):
    for i in range(len(ctrl) - 1):
        x0, y0 = ctrl[i]; x1, y1 = ctrl[i + 1]
        if x0 <= x <= x1:
            t = (x - x0) / (x1 - x0)
            return y0 + (y1 - y0) * t
    return ctrl[-1][1]

top = [int(round(h_at(x))) for x in range(64)]
for x in range(64):
    t = top[x]
    c.rect(x, t, 1, 64 - t, SAND)
    c.set(x, t, SAND_L)
    if x % 2 == 0 and t + 1 < 64:
        c.set(x, t + 1, SAND_L)
    u = t + 7 + int(round(2 * math.sin(x * 0.22)))
    if u < 64:
        c.rect(x, u, 1, 64 - u, SAND_M)
        if x % 2:
            c.set(x, u, SAND)
    v = 59 + int(round(1.5 * math.sin(x * 0.3)))
    if v < 64:
        c.rect(x, v, 1, 64 - v, SAND_D)
        if x % 2 == 0:
            c.set(x, v, SAND_M)

# drift of sand piled against the hull (half-buried look)
for x in range(20, 50):
    bump = int(round(2.4 * math.sin((x - 20) * math.pi / 30.0)))
    if bump <= 0:
        continue
    d = top[x] - bump
    c.rect(x, d, 1, bump + 1, SAND)
    c.set(x, d, SAND_L if x % 2 == 0 else SAND)

# contact shadow where the hull meets the sand
for x in range(7, 55):
    t = top[x]
    if x % 3 != 0 and t + 1 < 64:
        c.set(x, t + 1, SAND_D)
    if x % 5 == 0 and t + 2 < 64:
        c.set(x, t + 2, SAND_M)
# sand ripples in the foreground
for ry in (53, 58):
    for x in range(64):
        y = ry + int(round(1.6 * math.sin(x * 0.30 + ry)))
        if y >= top[x] + 5 and y < 63 and (x % 7) < 5:
            c.set(x, y, SAND)
            if y + 1 < 64:
                c.set(x, y + 1, SAND_D)

# speckles / pebbles
for x in range(64):
    for y in range(top[x] + 3, 64):
        h = (x * 7919 + y * 104729 + x * y * 31) % 1000
        if h % 89 == 0:
            c.set(x, y, SAND_M if (x + y) % 2 else SAND_D)

# ============================================================
#  KELP
# ============================================================
def kelp(x0, ybase, h, ph=0.0):
    for i in range(h):
        y = ybase - i
        x = x0 + int(round(1.6 * math.sin((i + ph) * 0.38)))
        if 0 <= y < 64:
            if 0 <= x < 64:
                c.set(x, y, KEL)
            if 0 <= x + 1 < 64:
                c.set(x + 1, y, KEL_D)
            if (i // 4) % 2 == 0 and 0 <= x - 1 < 64:
                c.set(x - 1, y, KEL_L)

kelp(2, 42, 19, 0.0)
kelp(61, 47, 18, 1.0)
kelp(63, 49, 12, 3.5)

# ============================================================
#  CORAL
# ============================================================
def coral(cx, base, hts, gap=3):
    x0 = cx - (len(hts) - 1) * gap // 2
    for i, h in enumerate(hts):
        fx = x0 + i * gap
        for j in range(h):
            y = base - j
            c.set(fx, y, COR)
            c.set(fx + 1, y, COR_D)
            if j == h - 1:
                c.set(fx, y, COR_L)
                c.set(fx + 1, y, COR_L)
            elif j == h - 2:
                c.set(fx + 1, y, COR)
        c.set(fx - 1, base, COR)
        if h > 4:
            c.set(fx - 1, base - h + 3, COR)
            c.set(fx - 1, base - h + 4, COR_D)

coral(4, 45, [5, 8])
coral(59, 50, [5, 9, 7])
coral(29, 58, [4, 6, 5])
coral(46, 61, [4, 6])

# ============================================================
#  FISH SCHOOL
# ============================================================
def stamp(cv, x0, y0, rows, cmap):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            col = cmap.get(ch)
            if col:
                cv.set(x0 + i, y0 + j, col)

FS = ["o.oo.", ".oooo", "o.oo."]
FB = ["..ooo..", ".ooooe.", "oooooo.", "..ooo.."]
cmD = {'o': FISH, 'e': FISH_M}
cmM = {'o': FISH_M, 'e': FISH}
cmL = {'o': FISH_L, 'e': FISH_M}

for (fx, fy) in ((33,13),(37,9),(43,5),(46,2),(49,10),(55,7),(60,12),
                 (46,14),(53,15),(39,16),(51,19),(58,18),(62,16),(42,19)):
    stamp(c, fx, fy, FS, cmD)
stamp(c, 35, 20, FB, cmL)
stamp(c, 56, 22, FB, cmM)
for (fx, fy) in ((9,10),(15,6),(6,15),(12,16),(22,4),(26,11),(18,2)):
    stamp(c, fx, fy, FS, cmD)

# ============================================================
#  BUBBLES
# ============================================================
for (bx, by, br) in ((28,33,1),(30,28,1),(28,23,0),(31,18,1),(30,13,0),(27,25,0),(33,24,1)):
    if br == 0:
        c.set(bx, by, BUB)
    else:
        c.circle(bx, by, br, BUB)
        c.set(bx, by, '#eaf8fb')

# ============================================================
#  FOREGROUND DEBRIS
# ============================================================
c.line(6, 60, 24, 56, WOOD_S)
c.line(6, 59, 24, 55, WOOD)
c.line(7, 59, 24, 55, WOOD_L)
c.set(25, 55, WOOD_S); c.set(5, 60, WOOD_S)
c.rect(35, 57, 3, 4, WOOD)
c.rect(35, 57, 3, 1, WOOD_L)
c.set(35, 60, WOOD_S); c.set(37, 58, WOOD_S)
for (rx, ry) in ((15,52),(41,52),(50,55),(29,62),(7,57),(33,54)):
    c.rect(rx, ry, 2, 1, SAND_X)
    c.set(rx, ry, SAND_D)

# ============================================================
#  DUMP
# ============================================================
CH = {}
def reg(h, ch):
    CH[c.color(h)] = ch
for i, w in enumerate(WATER):
    reg(w, ' ')
reg(RAY, "'")
reg(SAND_L, 'S'); reg(SAND, 's'); reg(SAND_M, 'm'); reg(SAND_D, 'd'); reg(SAND_X, 'x')
reg(WOOD_L, 'W'); reg(WOOD, 'w'); reg(WOOD_D, 'v'); reg(WOOD_X, 'u'); reg(WOOD_S, 'U')
reg(PAT_L, 'P'); reg(PAT, 'p'); reg(PAT_D, 'o')
reg(COR_L, 'C'); reg(COR, 'c'); reg(COR_D, 'e')
reg(KEL_L, 'K'); reg(KEL, 'k'); reg(KEL_D, 'j')
reg(FISH, 'f'); reg(FISH_M, 'F'); reg(FISH_L, 'G')
reg(BUB, 'O'); reg(SAIL_L, 'A'); reg(SAIL, 'a'); reg(SAIL_D, 'b'); reg(ROPE, 'R')
reg('#eaf8fb', 'o')

for y in range(64):
    row = ''.join(CH.get(c.get(x, y), '?') for x in range(64))
    print('%2d|%s|' % (y, row))

used = set()
for y in range(64):
    for x in range(64):
        used.add(c.get(x, y))
print('distinct visible colours:', len(used))
print(c.stats_text())
save('sunken_shipwreck', c)
finish(c)
