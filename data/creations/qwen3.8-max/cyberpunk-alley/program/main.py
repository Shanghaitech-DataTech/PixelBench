import math, random

W = H = 128
VPX, VPY = 64.0, 80.0          # one-point perspective vanishing point
random.seed(9)

scene = new_canvas(W, H, name="scene")

# ---------------------------------------------------------------- palette ----
SKY   = ['#03040a','#05070e','#070a14','#0a0e1b','#0e1323','#131a31']
HAZE  = ['#150f2c','#1e1540','#2c1c53','#3e2768']
STRT  = ['#5e3157','#8a4770','#bb6788','#e795a4']
BLK   = ['#04050b','#070912','#0b0e1b','#101425','#161b30','#1d2340','#262e50','#313b62']
PINK  = ['#420c22','#7d1239','#c31a58','#ff4d8d','#ff9dc0','#ffd9e7']
CYAN  = ['#072935','#0b5468','#0f93b4','#25dcff','#89efff','#d5fcff']
AMBER = ['#33200a','#6b4210','#b3761d','#ffa62b','#ffd894']
GREEN = ['#07281a','#0c5c37','#15a262','#37ef98']
PURP  = ['#1e0f3d','#3d1f7a','#6c3ad1']
RAIN  = ['#233c5e','#3d628f','#6d92c2']
FIGD  = '#020308'
PUD   = '#05080f'
MEMB  = (150, 205, 235, 62)     # translucent umbrella membrane
RIB   = '#0e1626'
URIM  = '#bfe4f7'

# ---------------------------------------------------------------- helpers ----
BAYER = ((0,8,2,10),(12,4,14,6),(3,11,1,9),(15,7,13,5))
def bth(x, y): return BAYER[y & 3][x & 3] / 16.0

def grad(c, y0, y1, cols, x0=0, x1=W-1):
    """vertical banded gradient with ordered dithering between bands"""
    n = y1 - y0 + 1
    for i in range(n):
        y = y0 + i
        t = i / max(1, n - 1)
        f = t * (len(cols) - 1)
        a = int(f); b = min(a + 1, len(cols) - 1); fr = f - a
        c.line(x0, y, x1, y, cols[a])
        if b != a and fr > 0:
            for x in range(x0, x1 + 1):
                if bth(x, y) < fr:
                    c.set(x, y, cols[b])

def Lq(x0, x1, yt, yb):
    """quad on the LEFT wall: yt/yb are y at the front edge x=0, converging to VP"""
    def yy(x, ye): return ye + (VPY - ye) * (x / VPX)
    return [(x0, int(round(yy(x0, yt)))), (x1, int(round(yy(x1, yt)))),
            (x1, int(round(yy(x1, yb)))), (x0, int(round(yy(x0, yb))))]

def Rq(x0, x1, yt, yb):
    """quad on the RIGHT wall: yt/yb are y at the front edge x=127"""
    def yy(x, ye): return ye + (VPY - ye) * ((W - 1 - x) / (W - 1 - VPX))
    return [(x0, int(round(yy(x0, yt)))), (x1, int(round(yy(x1, yt)))),
            (x1, int(round(yy(x1, yb)))), (x0, int(round(yy(x0, yb))))]

def ring(c, x0, y0, x1, y1, cols):
    """glow halo: concentric rect outlines, dimmest outermost"""
    for i, col in enumerate(cols):
        e = len(cols) - i
        w = (x1 - x0 + 1) + 2 * e
        h = (y1 - y0 + 1) + 2 * e
        if w > 0 and h > 0:
            c.rect(x0 - e, y0 - e, w, h, col, fill=False)

def ground_span(x):
    """rows of the alley floor visible in column x"""
    lo = max(93, math.ceil(128 - x / 1.31428), math.ceil(128 - (127 - x) / 1.28571))
    return (lo, 127) if lo <= 127 else None

# fake-CJK glyph strokes in normalised cell space (u right, v down)
GLYPHS = [
    [(0.12,0.88,0.10,0.24),(0.12,0.88,0.42,0.56),(0.12,0.88,0.76,0.90),(0.12,0.26,0.10,0.90),(0.74,0.88,0.10,0.90)],
    [(0.10,0.90,0.22,0.36),(0.10,0.90,0.62,0.76),(0.44,0.56,0.04,0.96),(0.10,0.22,0.22,0.76),(0.78,0.90,0.22,0.76)],
    [(0.14,0.86,0.12,0.26),(0.14,0.86,0.48,0.62),(0.14,0.26,0.12,0.62),(0.74,0.86,0.12,0.62),(0.44,0.56,0.62,0.92),(0.44,0.86,0.86,0.98)],
    [(0.10,0.90,0.40,0.54),(0.44,0.56,0.08,0.92),(0.16,0.30,0.72,0.86),(0.70,0.84,0.72,0.86)],
    [(0.18,0.82,0.26,0.40),(0.18,0.82,0.62,0.76),(0.18,0.30,0.26,0.76),(0.70,0.82,0.26,0.76),(0.08,0.92,0.06,0.16)],
    [(0.10,0.90,0.10,0.22),(0.18,0.82,0.42,0.54),(0.10,0.90,0.76,0.88),(0.44,0.56,0.22,0.76)],
]

def vsign(c, x0, x1, yt, yb, frame, body, bright, hot, ngl=4, side='L'):
    """perspective vertical neon sign on a wall, with fake glyphs"""
    Q = Lq if side == 'L' else Rq
    q = Q(x0, x1, yt, yb)
    ys = [p[1] for p in q]
    ring(c, x0, min(ys), x1, max(ys), [frame, frame])
    c.poly(q, frame, fill=True)
    c.poly(Q(x0 + 1, x1 - 1, yt + 2, yb - 2), body, fill=True)
    top = yt + 4; bot = yb - 4
    for g in range(ngl):
        v0 = top + (bot - top) * g / ngl + 1
        v1 = top + (bot - top) * (g + 1) / ngl - 1
        pat = GLYPHS[(g * 3 + x0) % len(GLYPHS)]
        for (u0, u1, w0, w1) in pat:
            bx0 = x0 + 2 + u0 * (x1 - x0 - 4)
            bx1 = x0 + 2 + u1 * (x1 - x0 - 4)
            c.poly(Q(bx0, bx1, v0 + w0 * (v1 - v0), v0 + w1 * (v1 - v0)), bright, fill=True)
    # hot core dashes down the middle of the tube
    for g in range(ngl):
        v0 = top + (bot - top) * g / ngl + 2
        v1 = top + (bot - top) * (g + 1) / ngl - 2
        c.poly(Q(x0 + 3, x1 - 3, v0, v1), hot, fill=True)

def hsign(c, x0, x1, yt, yb, frame, body, bright, side='L'):
    Q = Lq if side == 'L' else Rq
    c.poly(Q(x0, x1, yt, yb), frame, fill=True)
    c.poly(Q(x0 + 1, x1 - 1, yt + 1.5, yb - 1.5), body, fill=True)
    n = max(2, int((x1 - x0) / 4))
    for i in range(n):
        bx0 = x0 + 2 + i * (x1 - x0 - 4) / n
        bx1 = bx0 + (x1 - x0 - 4) / n * 0.62
        c.poly(Q(bx0, bx1, yt + 2.5, yb - 2.5), bright, fill=True)

# ============================================================== 1. SKY ======
grad(scene, 0, 96, SKY)
scene.ellipse(64, 62, 52, 30, HAZE[0])
scene.ellipse(64, 68, 36, 20, HAZE[1])

# ========================================================= 2. FAR END =======
grad(scene, 47, 82, HAZE, 46, 82)

# distant tower rows (aerial perspective: far row lighter)
for (a, b, t) in [(46,52,58),(52,56,50),(56,61,62),(61,66,44),(66,71,55),(71,76,48),(76,80,60),(80,83,53)]:
    scene.rect(a, t, b - a + 1, 82 - t, PURP[0])
for (a, b, t) in [(46,50,66),(50,55,60),(55,59,70),(59,64,58),(64,69,68),(69,74,62),(74,78,71),(78,83,64)]:
    scene.rect(a, t, b - a + 1, 82 - t, BLK[2])
# tiny distant windows
for _ in range(150):
    x = random.randint(46, 82); y = random.randint(48, 80)
    if random.random() < 0.5:
        scene.set(x, y, random.choice([AMBER[1], CYAN[1], PINK[1], BLK[4]]))

# distant street light pool at the alley mouth
scene.rect(46, 80, 37, 14, STRT[0])
scene.ellipse(64, 89, 20, 8, STRT[1])
scene.ellipse(64, 89, 14, 6, STRT[2])
scene.ellipse(64, 90, 8, 4, STRT[3])
for y in (86, 89, 92, 95, 99):
    scene.line(46, y, 82, y, BLK[1])
for (x, col) in [(69, PINK[2]), (70, PINK[1]), (54, CYAN[2]), (60, AMBER[2]), (76, CYAN[1])]:
    for y in range(93, 103, 3):
        scene.set(x, y, col)
# far vertical neon tower sign
scene.rect(67, 50, 6, 26, PINK[0])
scene.rect(68, 51, 4, 24, PINK[2])
scene.rect(69, 53, 2, 20, PINK[4])
scene.rect(52, 56, 5, 18, CYAN[0])
scene.rect(53, 57, 3, 16, CYAN[2])
# haze bloom over the far end
for r, col in [(26, HAZE[1]), (19, HAZE[2]), (13, HAZE[3])]:
    scene.ellipse(64, 86, r, int(r * 0.55), col, fill=False)

# ========================================================= 3. WALLS =========
LWALL = [(0,0),(21,0),(46,47),(46,93),(0,128)]
RWALL = [(127,0),(106,0),(82,47),(82,93),(127,128)]
scene.poly(LWALL, BLK[3])
scene.poly(RWALL, BLK[3])

# wall body shading: darker toward the front (near camera), lit near the far end
for x in range(0, 46):
    sh = BLK[1] if x < 14 else (BLK[2] if x < 30 else BLK[3])
    for y in range(0, 128):
        if scene.get(x, y) == scene.color(BLK[3]):
            scene.set(x, y, sh)
for x in range(82, 128):
    sh = BLK[1] if x > 113 else (BLK[2] if x > 96 else BLK[3])
    for y in range(0, 128):
        if scene.get(x, y) == scene.color(BLK[3]):
            scene.set(x, y, sh)

# perspective cornice / ledge lines
for ye, col in [(6, BLK[5]), (34, BLK[4]), (62, BLK[5]), (104, BLK[2])]:
    p = Lq(0, 46, ye, ye + 2)
    scene.poly(p, col)
    p = Rq(82, 127, ye, ye + 2)
    scene.poly(p, col)

# vertical structural seams
for x in (9, 20, 31, 40):
    scene.line(x, 0, x, 127, BLK[2])
for x in (88, 98, 109, 119):
    scene.line(x, 0, x, 127, BLK[2])

# ---- windows -------------------------------------------------------------
def windows(side, bays, floors):
    Q = Lq if side == 'L' else Rq
    for (bx0, bx1) in bays:
        for (fy0, fy1) in floors:
            q = Q(bx0, bx1, fy0, fy1)
            ys = [p[1] for p in q]
            if min(ys) < 2 or max(ys) > 126:
                continue
            r = random.random()
            if r < 0.20:
                lit = random.choice([AMBER[2], CYAN[2], PINK[2], AMBER[3]])
                scene.poly(q, BLK[1]); scene.poly(q, lit)
                scene.poly(Q(bx0, bx1, fy0, fy0 + 1.2), BLK[1])
            else:
                scene.poly(q, BLK[1])
                scene.poly(Q(bx0, bx1, fy1 - 1.2, fy1), BLK[4])

LBAYS = [(1,7),(11,17),(22,27),(31,35),(38,41),(43,45)]
RBAYS = [(83,86),(89,93),(97,102),(106,111),(115,120),(123,126)]
FLOORS = [(4,22),(32,50),(60,78),(88,110)]
windows('L', [(1,8),(12,19),(24,30),(34,39)], FLOORS)
windows('R', [(88,94),(99,106),(110,117),(121,126)], FLOORS)

# ---- left wall neon ------------------------------------------------------
vsign(scene, 4, 17, 2, 58, PINK[0], PINK[1], PINK[3], PINK[5], 4, 'L')
hsign(scene, 21, 34, 26, 38, CYAN[0], CYAN[1], CYAN[3], 'L')
vsign(scene, 36, 44, 44, 74, GREEN[0], GREEN[1], GREEN[3], GREEN[3], 3, 'L')
# projecting box sign (front-facing) near the alley throat
scene.rect(22, 54, 14, 12, PINK[0])
scene.rect(23, 55, 12, 10, PINK[2])
scene.rect(24, 56, 10, 8, PINK[4])
for i in range(2):
    scene.rect(25, 57 + i * 4, 8, 2, PINK[1])
scene.rect(19, 58, 4, 3, BLK[1])

# ---- right wall neon -----------------------------------------------------
hsign(scene, 92, 124, 18, 30, CYAN[0], CYAN[1], CYAN[4], 'R')
vsign(scene, 84, 92, 40, 78, PURP[0], PURP[1], PURP[2], CYAN[4], 3, 'R')
hsign(scene, 100, 122, 40, 50, AMBER[0], AMBER[1], AMBER[3], 'R')
vsign(scene, 122, 127, 56, 92, PINK[0], PINK[1], PINK[3], PINK[5], 3, 'R')

# pipes + fire escape silhouettes
for x in (19, 20):
    scene.line(x, 0, x, 127, BLK[1])
scene.line(30, 40, 30, 96, BLK[1])
for y in range(58, 96, 7):
    scene.line(96, y, 120, y - 6, BLK[1])
for y in range(58, 96, 7):
    scene.line(96, y, 96, y + 7, BLK[1]); scene.line(120, y - 6, 120, y + 1, BLK[1])

# doorway with warm interior light, left foreground
scene.poly(Lq(1, 9, 96, 128), BLK[0])
scene.poly(Lq(2, 8, 100, 128), AMBER[0])
scene.poly(Lq(3, 7, 106, 128), AMBER[1])
scene.line(5, 108, 5, 127, BLK[0])

# wet-wall neon streaks + small wall fixtures
for (x, y0, y1, col) in [(8,58,92,PINK[1]),(12,58,86,PINK[0]),(26,38,70,CYAN[1]),
                        (40,74,92,GREEN[1]),(104,30,52,CYAN[1]),(112,50,86,AMBER[1]),
                        (88,78,96,PURP[1])]:
    for y in range(y0, y1, 2):
        scene.set(x, y, col)
scene.rect(24, 68, 6, 5, BLK[1]); scene.rect(25, 69, 4, 3, BLK[4])
scene.line(24, 70, 29, 70, BLK[0]); scene.line(24, 72, 29, 72, BLK[0])
scene.set(27, 66, AMBER[3]); scene.set(26, 67, AMBER[1]); scene.set(27, 67, AMBER[1]); scene.set(28, 67, AMBER[1])

# ========================================================= 4. GROUND ========
scene.poly([(46,93),(82,93),(127,128),(0,128)], BLK[1])
for y in range(93, 128):
    t = (y - 93) / 34.0
    col = BLK[3] if t < 0.2 else (BLK[1] if t > 0.8 else BLK[2])
    scene.line(0, y, 127, y, col)
    for x in range(0, 128):
        sp = ground_span(x)
        if sp and sp[0] <= y <= sp[1]:
            if bth(x, y) < t * 0.45:
                scene.set(x, y, BLK[1] if t < 0.5 else BLK[0])
# faint perspective paving seams
for x0 in range(-40, 170, 14):
    scene.line(x0, 127, 64, 93, BLK[2])
for y in (98, 104, 112, 121):
    scene.line(0, y, 127, y, BLK[2])

# light pool spilling from the alley mouth
scene.ellipse(64, 96, 26, 7, STRT[0])
scene.ellipse(64, 95, 17, 5, STRT[1])
for x in range(38, 91):
    for y in range(93, 104):
        if scene.get(x, y) in (scene.color(BLK[0]), scene.color(BLK[1])) and bth(x, y) < 0.35:
            scene.set(x, y, STRT[0])

# ---- broad wet reflections under each light source -----------------------
def reflect(x0, x1, cols, y0=93, y1=127, strength=0.75, jitter=1):
    for x in range(x0, x1 + 1):
        sp = ground_span(x)
        if not sp: continue
        a = max(sp[0], y0)
        d = (x - (x0 + x1) / 2.0) / max(1.0, (x1 - x0) / 2.0)
        fade = 1.0 - abs(d) ** 1.4
        for y in range(a, min(sp[1], y1) + 1):
            t = (y - a) / max(1.0, (min(sp[1], y1) - a))
            p = fade * strength * (1.0 - t * 0.6)
            if p <= 0: continue
            jx = x + random.randint(-jitter, jitter)
            if random.random() < p:
                ci = int((1 - p) * (len(cols) - 1))
                ci = min(len(cols) - 1, max(0, ci))
                scene.set(jx, y, cols[ci])

reflect(3, 18,   [PINK[1], PINK[2], PINK[3]], strength=0.75)
reflect(20, 35,  [CYAN[1], CYAN[2]], strength=0.55)
reflect(35, 45,  [GREEN[1], GREEN[2]], strength=0.55)
reflect(50, 78,  [STRT[0], STRT[1], STRT[2]], strength=0.85)
reflect(84, 93,  [PURP[1], PURP[2]], strength=0.6)
reflect(92, 126, [CYAN[1], CYAN[2], GREEN[2], AMBER[2]], strength=0.75)
reflect(120, 127,[PINK[1], PINK[2]], strength=0.7)

# ---- puddles: mirror pools with sharp broken reflections -----------------
PUDDLES = [
    [(14,112),(34,108),(46,114),(52,122),(40,127),(16,127),(8,120)],
    [(56,116),(74,112),(92,116),(96,124),(78,127),(58,126)],
    [(86,98),(104,96),(116,100),(112,106),(90,105)],
    [(30,96),(44,94),(52,98),(40,101),(28,100)],
]
pud_idx = scene.color(PUD)
for poly in PUDDLES:
    scene.poly(poly, PUD)
for poly in PUDDLES:
    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            if 0 <= x < W and 0 <= y < H and scene.get(x, y) == pud_idx:
                # sky sheen + a bright dash where a reflection lands
                if bth(x, y) < 0.16:
                    scene.set(x, y, BLK[4])
# coloured mirror streaks inside the puddles
def pud_streak(x, y0, y1, cols):
    for y in range(y0, y1 + 1):
        if 0 <= x < W and scene.get(x, y) == pud_idx:
            k = (y - y0 + x // 2) % 7
            if k < 3:
                scene.set(x, y, cols[min(len(cols) - 1, (y - y0) // 6)])
for x in range(6, 20):   pud_streak(x, 108, 127, [PINK[2], PINK[1], PINK[0]])
for x in range(21, 34):  pud_streak(x, 106, 127, [PINK[1], PINK[0], PINK[0]])
for x in range(36, 47):  pud_streak(x, 106, 127, [GREEN[1], GREEN[0]])
for x in range(56, 80):  pud_streak(x, 110, 127, [STRT[1], STRT[0], STRT[0]])
for x in range(80, 98):  pud_streak(x, 110, 127, [CYAN[2], CYAN[1], CYAN[0]])
for x in range(99, 118): pud_streak(x, 112, 127, [CYAN[1], GREEN[1], CYAN[0]])
for x in range(88, 116): pud_streak(x, 95, 106, [CYAN[1], CYAN[0]])
for x in range(30, 52):  pud_streak(x, 94, 101, [STRT[0], STRT[0]])

# ==================================================== 5. VENDING MACHINES ===
def vending(x0, y0, x1, y1, banner, body, glow, dots):
    w = x1 - x0 + 1; h = y1 - y0 + 1
    scene.rect(x0, y0, w, h, BLK[0])
    scene.rect(x0 + 1, y0 + 1, max(1, w - 2), 4, banner)
    scene.rect(x0 + 1, y0 + 6, max(1, w - 2), max(1, h - 12), body)
    scene.rect(x0 + 2, y0 + 7, max(1, w - 4), max(1, h - 16), glow)
    ix = x0 + 3; iy = y0 + 8
    k = 0
    while iy < y1 - 10:
        while ix < x1 - 3:
            scene.rect(ix, iy, 3, 3, dots[k % len(dots)])
            scene.rect(ix, iy, 3, 1, BLK[0])
            ix += 4; k += 1
        ix = x0 + 3; iy += 5
    scene.rect(x0 + 1, y1 - 5, max(1, w - 2), 4, BLK[1])
    scene.rect(x0 + 2, y1 - 4, 4, 2, AMBER[3])
    scene.line(x0, y0, x0, y1, BLK[0]); scene.line(x1, y0, x1, y1, BLK[0])

vending(94, 96, 112, 127, AMBER[3], CYAN[1], CYAN[2], [PINK[3], AMBER[3], GREEN[3], CYAN[4]])
vending(114, 101, 127, 127, PINK[3], GREEN[1], GREEN[2], [AMBER[3], CYAN[4], PINK[4]])
# small machine further back
vending(84, 88, 93, 104, CYAN[3], PURP[1], PURP[2], [AMBER[3], PINK[4]])

# spill light on the ground from the machines
for x in range(78, 128):
    for y in range(104, 128):
        sp = ground_span(x)
        if not sp or not (sp[0] <= y <= sp[1]): continue
        cur = scene.get(x, y)
        if cur in (scene.color(BLK[0]), scene.color(BLK[1]), scene.color(BLK[2])):
            d = math.hypot((x - 104) / 26.0, (y - 118) / 12.0)
            if d < 1.0 and bth(x, y) < (1 - d) * 0.45:
                scene.set(x, y, CYAN[0] if d > 0.55 else CYAN[1])

# ================================================ 6. FOREGROUND LEFT =======
scene.poly([(0,104),(10,101),(20,105),(24,114),(20,127),(0,127)], BLK[0])
scene.poly([(0,110),(9,108),(16,112),(14,127),(0,127)], BLK[1])
scene.line(0, 104, 10, 101, BLK[4]); scene.line(10, 101, 20, 105, BLK[4])
scene.line(20, 105, 24, 114, PINK[2]); scene.line(24, 114, 20, 127, PINK[1])
# bollard + pipes
scene.rect(28, 108, 4, 20, BLK[0]); scene.rect(28, 108, 1, 20, BLK[4])
scene.rect(27, 106, 6, 3, AMBER[2])
for x in (0, 1, 2):
    scene.line(x, 84, x, 127, BLK[0])
scene.line(2, 84, 2, 127, BLK[4])

# ========================================================= 7. CABLES ========
CABLES = [
    ("M -1 12 Q 64 40 128 8", BLK[5], 2),
    ("M -1 24 Q 64 54 128 20", BLK[5], 2),
    ("M 14 4 Q 64 26 112 2", BLK[4], 1),
    ("M 30 34 Q 64 52 98 32", BLK[5], 2),
    ("M -1 44 Q 40 62 82 44", BLK[4], 1),
    ("M 46 46 Q 64 56 82 46", BLK[4], 1),
]
for d, col, _ in CABLES:
    scene.path(d, col, fill=False)
# faint wet highlight along the two main cables
scene.path("M -1 13 Q 64 41 128 9", BLK[6], fill=False)
scene.path("M 30 35 Q 64 53 98 33", BLK[6], fill=False)
# hanging lamps + junction boxes on the cables
for (x, y, col) in [(24,20,BLK[4]),(44,29,BLK[4]),(88,26,BLK[4]),(104,17,BLK[4]),(60,47,BLK[4])]:
    scene.rect(x - 2, y, 5, 4, col)
for (x, y, col, gl) in [(34,25,AMBER[3],AMBER[1]),(76,32,PINK[4],PINK[1]),(52,44,CYAN[4],CYAN[1])]:
    scene.line(x, y - 3, x, y, BLK[0])
    scene.set(x, y, gl); scene.set(x - 1, y + 1, col); scene.set(x, y + 1, col); scene.set(x + 1, y + 1, col)
    scene.set(x, y + 2, gl)

# atmospheric rim on the wall edges nearest the far glow
for y in range(47, 94):
    scene.set(45, y, PURP[0]); scene.set(82, y, PURP[0])
    if 60 < y < 92:
        scene.set(44, y, HAZE[1]); scene.set(83, y, HAZE[1])

# ========================================================= 8. RAIN ==========
def rain(n, cols, y0=0, y1=127, len_min=3, len_max=7, slope=-0.30):
    for _ in range(n):
        x = random.randint(-14, W + 6); y = random.randint(y0, y1)
        L = random.randint(len_min, len_max)
        col = random.choice(cols)
        x2 = int(x + slope * L); y2 = y + L
        scene.line(x, y, x2, y2, col)

rain(150, [RAIN[0]], len_min=3, len_max=5)
rain(70, [RAIN[1]], len_min=4, len_max=7)
rain(26,  [RAIN[2]], len_min=5, len_max=8)
# backlit rain in front of the bright alley mouth
for _ in range(45):
    x = random.randint(44, 84); y = random.randint(52, 96)
    L = random.randint(3, 6)
    scene.line(x, y, int(x - 0.3 * L), y + L, random.choice([PINK[2], STRT[2], CYAN[2]]))
# splash ripples on the wet ground
for _ in range(26):
    x = random.randint(4, 122); y = random.randint(96, 126)
    sp = ground_span(x)
    if sp and sp[0] <= y <= sp[1]:
        scene.line(x - 2, y, x + 2, y, RAIN[1])
        scene.set(x, y, RAIN[2])

# ========================================================= 9. PERSON ========
FIG = FIGD
scene.ellipse(50, 115, 13, 3, BLK[0])          # contact shadow on wet ground
# legs + boots
scene.rect(45, 104, 4, 10, FIG)
scene.rect(52, 103, 4, 11, FIG)
scene.rect(43, 113, 7, 3, FIG)
scene.rect(51, 113, 8, 3, FIG)
# long coat
scene.poly([(43,86),(57,86),(59,98),(61,107),(39,107),(41,98)], FIG)
# shoulders / torso
scene.poly([(45,82),(55,82),(58,88),(42,88)], FIG)
# hood + head
scene.poly([(46,73),(54,73),(56,79),(54,84),(46,84),(44,79)], FIG)
scene.poly([(47,71),(53,71),(55,76),(45,76)], FIG)
# arm holding the umbrella shaft
scene.poly([(54,86),(58,88),(58,95),(54,94)], FIG)
# rim light: cyan from the vending machines on the right, pink from the sign left
RIM_R = CYAN[3]; RIM_L = PINK[3]
for y in range(73, 84):
    scene.set(55 if y < 79 else 54, y, RIM_R)
scene.line(56, 84, 58, 88, RIM_R)
scene.line(58, 89, 59, 98, RIM_R)
scene.line(59, 99, 61, 107, RIM_R)
scene.set(56, 104, RIM_R); scene.set(56, 106, RIM_R); scene.set(56, 108, RIM_R)
scene.set(56, 113, RIM_R); scene.set(57, 115, RIM_R)
for y in range(74, 84):
    scene.set(45 if y < 79 else 44, y, RIM_L)
scene.line(43, 87, 42, 88, RIM_L)
scene.line(41, 98, 39, 107, RIM_L)
scene.set(44, 100, RIM_L); scene.set(44, 103, RIM_L)
scene.set(44, 106, RIM_L); scene.set(43, 114, RIM_L)
# face shadow gap + a faint lit cheek
scene.set(51, 79, BLK[4]); scene.set(52, 80, PINK[1])
# the person's reflection in the puddle
for y in range(117, 127):
    for x in range(40, 64):
        if scene.get(x, y) == pud_idx and (x + y) % 3 != 0:
            if 45 <= x <= 57:
                scene.set(x, y, FIG)
            elif x in (44, 58):
                scene.set(x, y, BLK[1])
for y in (118, 121, 124):
    for x in range(42, 62):
        if scene.get(x, y) == FIG:
            scene.set(x, y, PUD)
scene.set(58, 118, CYAN[1]); scene.set(58, 122, CYAN[1]); scene.set(44, 120, PINK[1])

# umbrella shaft + handle (opaque, in front of the body)
scene.line(52, 66, 56, 90, BLK[0])
scene.line(53, 66, 57, 90, BLK[4])
scene.line(57, 90, 57, 94, BLK[4])
scene.line(57, 94, 60, 95, BLK[4])
scene.poly([(54,88),(59,89),(59,93),(54,92)], FIG)

# ============================================== 10. UMBRELLA (translucent) ==
umb = new_canvas(W, H, name="umbrella")
CAN = "M 35 70 C 36 56 44 50 51 50 C 58 50 66 56 67 70 Q 61 64 56 69 Q 51 63 46 69 Q 40 64 35 70 Z"
umb.path(CAN, MEMB, fill=True)
# ribs + edge (crisp, opaque: the structure you see through the membrane)
for tx, ty in ((35, 69), (46, 68), (56, 68), (67, 69)):
    umb.line(51, 51, tx, ty, RIB)
umb.path("M 35 70 Q 40 64 46 69 Q 51 63 56 69 Q 61 64 67 70", URIM, fill=False)
umb.path("M 35 70 C 36 56 44 50 51 50 C 58 50 66 56 67 70", URIM, fill=False)
umb.line(51, 46, 51, 51, RIB)
umb.set(51, 45, URIM)
# specular dashes on the wet canopy
for (x, y) in [(40,58),(42,56),(44,55),(47,54),(58,55),(61,57),(63,59),(46,61),(55,60)]:
    umb.set(x, y, CYAN[4])
for (x, y) in [(41,59),(45,56),(59,56),(62,58)]:
    umb.set(x, y, PINK[4])

result = flatten([scene, umb], name="result")

print(result.stats_text())
view(result)
save("cyberpunk_alley", result, indexed=True)
finish(result)
