import math, random

random.seed(11)

W = H = 256
HOR = 152

c = new_canvas(W, H, name="output")

# ---------------- palette ----------------
SKY = ['#190f30', '#2a1745', '#401d4c', '#5d2550', '#84324b',
       '#ab4440', '#cf6235', '#e88c33', '#f3b94e', '#f8d775']
SUN = ['#f0a640', '#f9cc63', '#ffeca8']
CLOUD_D = '#3a1f44'
CLOUD_M = '#6b3050'
CLOUD_L = '#e78a3c'

MTN_FAR = '#3b2b4e'
MTN_FAR_L = '#5a3b58'
MTN_NEAR = '#281e37'
MTN_NEAR_L = '#3c2a46'

GND_1 = '#4b3650'
GND_2 = '#56394a'
GND_3 = '#43303c'
GND_4 = '#33242e'
RUBBLE = '#60463c'

STONE_L = '#8a8290'
STONE_M = '#6a6274'
STONE_D = '#4a4356'
STONE_X = '#332e3e'
INK = '#140c16'
WIN_G = '#ffc054'
WIN_D = '#2b1b22'

WOOD_L = '#7a5230'
WOOD_M = '#5a3a22'
WOOD_D = '#3a2416'

F_OUT = '#c0351f'
F_MID = '#ef7a28'
F_IN = '#ffc54a'
F_CORE = '#fff0b0'

SMOKE_D = '#2b2334'
SMOKE_M = '#413748'
SMOKE_L = '#5d5162'
SMOKE_H = '#7b6d78'

DRG_D = '#1a1020'
DRG_M = '#33203a'
DRG_L = '#4e2a3e'
DRG_WING = '#5e2634'
DRG_SPINE = '#caa87c'

ARM_D = '#191420'
ARM_RIM = '#d2702c'
STEEL = '#787a8c'
SH_RED = '#8c2f2c'
SH_BLUE = '#33507a'
SH_GOLD = '#c39638'

EMB_1 = '#ffd27a'
EMB_2 = '#ff8a30'


# ---------------- helpers ----------------
def soft_circle(cv, cx, cy, r, col, edge=1.0):
    r0 = r - edge
    for y in range(int(cy - r - 1), int(cy + r + 2)):
        if y < 0 or y >= H:
            continue
        for x in range(int(cx - r - 1), int(cx + r + 2)):
            if x < 0 or x >= W:
                continue
            d = math.hypot(x - cx, y - cy)
            if d <= r0:
                cv.set(x, y, col)
            elif d <= r + 0.4 and (x + y) % 2 == 0:
                cv.set(x, y, col)


BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def sky_gradient():
    n = len(SKY)
    for y in range(HOR):
        t = (y / (HOR - 1)) * (n - 1)
        i = int(t)
        f = t - i
        if i >= n - 1:
            i = n - 2
            f = 1.0
        a, b = SKY[i], SKY[i + 1]
        if f < 0.08:
            c.rect(0, y, W, 1, a)
        elif f > 0.92:
            c.rect(0, y, W, 1, b)
        else:
            thr = f * 16.0
            for x in range(W):
                c.set(x, y, b if BAYER[y % 4][x % 4] < thr else a)


sky_gradient()

# sun
soft_circle(c, 186, 134, 26, SUN[0], edge=5)
soft_circle(c, 186, 134, 18, SUN[1], edge=3)
soft_circle(c, 186, 134, 12, SUN[2], edge=2)

# clouds: broken sunset streaks, lit from the sun side
def cloud(cx, cy, rx, ry, lit=True):
    n = max(3, rx // 7)
    puffs = []
    for i in range(n):
        t = (i / (n - 1)) * 2 - 1
        px = cx + t * rx * 0.8
        py = cy + math.sin(i * 1.7 + cx) * ry * 0.5
        pr = rx * (0.30 + 0.22 * (1 - abs(t)))
        pry = max(1, ry * (0.55 + 0.6 * (1 - abs(t))))
        puffs.append((px, py, pr, pry))
    for px, py, pr, pry in puffs:
        c.ellipse(int(px), int(py), int(pr), int(pry), CLOUD_D)
    for px, py, pr, pry in puffs:
        if pry >= 2:
            c.ellipse(int(px), int(py - 1), int(pr * 0.72), int(pry - 1), CLOUD_M)
    if lit:
        for px, py, pr, pry in puffs:
            c.line(int(px - pr * 0.7), int(py + pry), int(px + pr * 0.7),
                   int(py + pry), CLOUD_L)


for args in [(46, 30, 34, 4), (154, 22, 26, 3), (214, 50, 24, 3),
             (66, 66, 40, 5), (184, 86, 32, 4), (26, 100, 28, 4),
             (132, 108, 36, 4), (232, 116, 22, 3)]:
    cloud(*args)

# ---------------- mountains ----------------
far = [(0, 140), (16, 126), (32, 134), (52, 112), (70, 128), (88, 120),
       (104, 136), (122, 126), (140, 108), (158, 126), (176, 116),
       (196, 132), (214, 118), (236, 134), (255, 124), (255, 160), (0, 160)]
c.poly(far, MTN_FAR)
for i in range(len(far) - 3):
    x0, y0 = far[i]
    x1, y1 = far[i + 1]
    if x1 > x0 and y1 < y0:
        c.line(x0, y0, x1, y1, MTN_FAR_L)

near = [(0, 150), (28, 140), (58, 148), (88, 137), (118, 146), (148, 135),
        (178, 145), (208, 137), (236, 147), (255, 141), (255, 168), (0, 168)]
c.poly(near, MTN_NEAR)
for i in range(len(near) - 3):
    x0, y0 = near[i]
    x1, y1 = near[i + 1]
    if y1 < y0:
        c.line(x0, y0, x1, y1, MTN_NEAR_L)

# ---------------- ground ----------------
c.rect(0, 156, W, 100, GND_1)
c.dither(0, 160, W, 6, [GND_1, GND_2], pattern="bayer4")
c.rect(0, 166, W, 18, GND_2)
c.dither(0, 184, W, 6, [GND_2, GND_3], pattern="bayer4")
c.rect(0, 190, W, 16, GND_3)
c.dither(0, 200, W, 6, [GND_3, GND_4], pattern="checker")
c.rect(0, 206, W, 50, GND_4)

# scorched patches and rubble
for i in range(90):
    x = random.randrange(0, W)
    y = random.randrange(158, 206)
    w = random.randrange(1, 5)
    c.rect(x, y, w, 1, random.choice([GND_3, RUBBLE, GND_4]))

# small field fires
for fx, fy, fr in [(14, 196, 7), (236, 190, 6), (96, 180, 5), (206, 172, 4)]:
    soft_circle(c, fx, fy, fr, '#6b3324', edge=2)
    soft_circle(c, fx, fy, fr - 3, F_OUT, edge=1)

# =================================================================
# CASTLE
# =================================================================
GB = 176  # castle ground baseline

# rocky plateau under the castle
c.poly([(44, 182), (62, 172), (96, 168), (150, 168), (188, 171),
        (210, 182), (210, 190), (44, 190)], STONE_X)
c.line(62, 172, 96, 168, '#413a4a')
c.line(150, 168, 188, 171, '#413a4a')
c.dither(44, 182, 166, 5, [STONE_X, GND_3], pattern="bayer4")


def stone_block(x, y, w, h):
    """Rectangular masonry with sun-lit right edge and brick texture."""
    c.rect(x, y, w, h, STONE_M)
    c.rect(x + w - 3, y, 3, h, STONE_L)
    c.rect(x, y, 2, h, STONE_D)
    for by in range(y + 3, y + h, 4):
        c.line(x, by, x + w - 1, by, STONE_D)
    for i in range(max(1, (w * h) // 26)):
        bx = random.randrange(x + 2, x + w - 2)
        by = random.randrange(y + 1, y + h - 1)
        c.rect(bx, by, 2, 1, STONE_X if random.random() < 0.5 else STONE_L)
    c.rect(x, y, w, h, INK, fill=False)


def crenellate(x, w, y_top, step=6, merlon=4, hgt=5):
    """Merlons along a wall top; returns list of gap centres."""
    gaps = []
    xx = x
    while xx + merlon <= x + w:
        c.rect(xx, y_top - hgt, merlon, hgt + 1, STONE_M)
        c.rect(xx + merlon - 2, y_top - hgt, 2, hgt + 1, STONE_L)
        c.rect(xx, y_top - hgt, merlon, 1, STONE_L)
        c.rect(xx, y_top - hgt, merlon, hgt + 1, INK, fill=False)
        gaps.append(xx + merlon + (step - merlon) // 2)
        xx += step
    return gaps


# --- curtain wall ---
stone_block(70, 150, 116, GB - 150)
wall_gaps = crenellate(70, 116, 150)

# gatehouse arch
c.rect(120, 162, 14, 14, WIN_D)
c.path("M120 170 L120 166 Q127 158 134 166 L134 170 Z", WIN_D)
c.rect(120, 160, 14, 16, INK, fill=False)
c.rect(122, 170, 10, 6, WOOD_M)
c.rect(122, 170, 10, 6, WOOD_D, fill=False)
c.line(123, 170, 123, 175, WOOD_L)
c.line(128, 170, 128, 175, WOOD_L)

# --- side towers ---
for tx in (56, 176):
    stone_block(tx, 128, 24, GB - 128)
    crenellate(tx, 24, 128, step=6, merlon=4, hgt=5)
    for wy in (138, 150, 162):
        c.rect(tx + 10, wy, 3, 4, WIN_D)
        c.rect(tx + 11, wy + 1, 1, 2, WIN_G)

# --- keep ---
stone_block(100, 112, 56, 40)
crenellate(100, 56, 112, step=7, merlon=5, hgt=6)
for wy in (120, 132, 142):
    for wx in (108, 124, 140):
        c.rect(wx, wy, 4, 5, WIN_D)
        c.rect(wx + 1, wy + 1, 2, 3, WIN_G)

# --- tall keep tower (hit, roof torn open) ---
stone_block(114, 82, 26, 32)
c.rect(114, 82, 26, 4, STONE_X)
c.poly([(114, 84), (120, 78), (126, 84), (131, 76), (139, 83)], STONE_D)
c.rect(119, 92, 5, 7, WIN_D)
c.rect(120, 93, 3, 4, WIN_G)
c.rect(130, 92, 5, 7, WIN_D)
c.rect(131, 93, 3, 4, WIN_G)
# broken battlement debris falling
for dx, dy in [(142, 96), (146, 104), (110, 100), (150, 114), (106, 92)]:
    c.rect(dx, dy, 2, 2, STONE_D)
    c.set(dx, dy, INK)

# banners on the towers
for bx in (66, 186):
    c.line(bx, 118, bx, 130, WOOD_D)
    c.poly([(bx + 1, 119), (bx + 9, 122), (bx + 1, 125)], SH_RED)
    c.poly([(bx + 1, 119), (bx + 9, 122), (bx + 1, 125)], INK, fill=False)
    c.set(bx + 4, 122, SH_GOLD)


# =================================================================
# FIRE + SMOKE
# =================================================================
def flame(cx, base, h, w):
    c.path("M%d %d Q%d %d %d %d Q%d %d %d %d Z" % (
        cx - w, base, cx - w, base - h * 0.6, cx, base - h,
        cx + w, base - h * 0.6, cx + w, base), F_OUT)
    c.path("M%d %d Q%d %d %d %d Q%d %d %d %d Z" % (
        cx - w * 0.6, base, cx - w * 0.6, base - h * 0.5,
        cx, base - h * 0.72, cx + w * 0.6, base - h * 0.5,
        cx + w * 0.6, base), F_MID)
    c.path("M%d %d Q%d %d %d %d Q%d %d %d %d Z" % (
        cx - w * 0.3, base, cx - w * 0.3, base - h * 0.35,
        cx, base - h * 0.5, cx + w * 0.3, base - h * 0.35,
        cx + w * 0.3, base), F_IN)
    c.set(cx, base - int(h * 0.3), F_CORE)


def smoke_column(x0, ybase, ytop, spread, drift=0.6):
    y = ybase
    r = 4.0
    i = 0
    while y > ytop:
        t = (ybase - y) / max(1.0, (ybase - ytop))
        cx = x0 + drift * (ybase - y) + math.sin(i * 0.9) * spread * t
        rr = r + t * spread
        col = SMOKE_M if t < 0.35 else (SMOKE_L if t < 0.7 else SMOKE_H)
        soft_circle(c, int(cx), int(y), int(rr), col, edge=max(1.5, rr * 0.5))
        soft_circle(c, int(cx - rr * 0.3), int(y + 1), int(rr * 0.6),
                    SMOKE_D if t < 0.5 else SMOKE_M, edge=1.5)
        y -= max(3, int(rr * 0.75))
        i += 1


smoke_column(126, 84, 16, 13, drift=0.55)
smoke_column(172, 128, 60, 9, drift=0.7)
smoke_column(64, 130, 74, 8, drift=0.45)

# fires on the castle
flame(126, 86, 22, 9)
flame(118, 114, 13, 5)
flame(148, 114, 11, 5)
flame(178, 130, 12, 5)
flame(60, 130, 10, 4)
flame(96, 152, 11, 5)
flame(160, 152, 9, 4)
for i in range(26):
    x = random.randrange(70, 186)
    y = random.randrange(148, 152)
    c.set(x, y, random.choice([F_MID, F_IN, F_OUT]))

# =================================================================
# SIEGE TOWERS, TROOPS, ARROWS
# =================================================================
def siege_tower(x, base, w, h, flip=False):
    top = base - h
    c.rect(x, top, w, h, WOOD_M)
    c.rect(x, top, w, h, WOOD_D, fill=False)
    # uprights and cross-bracing
    for ux in (x + 1, x + w // 2, x + w - 2):
        c.line(ux, top + 1, ux, base - 1, WOOD_D)
    for by in range(top + 5, base - 2, 7):
        c.line(x + 1, by, x + w - 2, by, WOOD_L)
        c.line(x + 1, by + 6, x + w - 2, by, WOOD_D)
    # fighting top with hoarding
    c.rect(x - 2, top - 7, w + 4, 8, WOOD_L)
    c.rect(x - 2, top - 7, w + 4, 8, INK, fill=False)
    for mx in range(x - 2, x + w + 2, 4):
        c.rect(mx, top - 10, 2, 4, WOOD_M)
        c.rect(mx, top - 10, 2, 4, WOOD_D, fill=False)
    # drop bridge
    bx = x + w if not flip else x - 12
    c.line(bx, top + 1, bx + (12 if not flip else -12), top - 5, WOOD_L)
    c.line(bx, top + 2, bx + (12 if not flip else -12), top - 4, WOOD_D)
    # wheels
    for wx in (x + 3, x + w - 4):
        c.circle(wx, base, 2, WOOD_D)
        c.set(wx, base, WOOD_L)
    # tiny soldiers on top
    for sx in range(x, x + w, 5):
        c.rect(sx + 1, top - 13, 2, 4, ARM_D)
        c.set(sx + 2, top - 14, ARM_RIM)


siege_tower(20, 186, 22, 36, flip=False)
siege_tower(214, 182, 22, 32, flip=True)

# catapult silhouette, right foreground
c.poly([(176, 206), (198, 206), (196, 198), (178, 198)], WOOD_D)
c.line(180, 198, 196, 182, WOOD_M)
c.line(181, 199, 197, 183, WOOD_D)
c.circle(180, 207, 3, WOOD_D)
c.circle(194, 207, 3, WOOD_D)


def soldier(x, y, scale=1, shield=None, spear=True, lean=0, body=ARM_D):
    """Tiny infantry silhouette. y is ground line."""
    if scale == 1:
        c.rect(x, y - 5, 2, 4, body)      # torso + legs
        c.set(x, y - 1, body)
        c.set(x + 1, y - 1, body)
        c.set(x, y - 6, body)             # helm
        c.set(x + 1, y - 6, ARM_RIM)
        if spear:
            c.line(x + 2 + lean * 3, y - 11, x + 2, y - 3, body)
            c.set(x + 2 + lean * 3, y - 11, STEEL)
        if shield:
            c.rect(x - 1, y - 5, 2, 3, shield)
            c.set(x - 1, y - 5, INK)
    else:
        h = 4 * scale
        c.rect(x, y - h, 2 * scale, h, body)
        c.rect(x, y - h - 2 * scale + 1, 2 * scale, 2 * scale - 1, body)
        c.rect(x + scale, y - h - 2 * scale + 1, scale, 1, ARM_RIM)
        if spear:
            sx = x + 2 * scale
            c.line(sx + lean * 2, y - h - 6 * scale, sx, y - scale, body)
            c.rect(sx + lean * 2, y - h - 6 * scale, 1, 2, STEEL)
        if shield:
            c.rect(x - scale, y - h - scale, 2 * scale, 3 * scale, shield)
            c.rect(x - scale, y - h - scale, 2 * scale, 3 * scale, INK,
                   fill=False)


# knights on the ramparts (wall top, tower tops, keep top)
for i, gx in enumerate(wall_gaps):
    if 72 < gx < 184:
        soldier(gx, 150, 1, shield=[SH_RED, SH_BLUE, SH_GOLD][i % 3])
for gx in (60, 66, 180, 186):
    soldier(gx, 128, 1, shield=SH_BLUE if gx < 120 else SH_RED)
for gx in (104, 112, 136, 148):
    soldier(gx, 112, 1, shield=SH_GOLD if gx % 3 else SH_RED)

# soldiers in formation: tight pike blocks separated by clear gaps
blocks = [(8, 62, 186, 5, SH_RED, 1), (98, 150, 188, 5, SH_BLUE, -1),
          (198, 248, 186, 5, SH_GOLD, 1),
          (20, 80, 200, 6, SH_BLUE, 1), (160, 240, 202, 6, SH_RED, -1)]
for x0, x1, row_y, step, sh, lean in blocks:
    k = 0
    x = x0
    while x < x1:
        soldier(x, row_y + (k % 2), 1, shield=sh if k % 2 else None, lean=lean)
        x += step
        k += 1

# unit banners among the mid-ground ranks
for bx, by, bc in [(40, 186, SH_RED), (120, 188, SH_BLUE), (214, 186, SH_GOLD),
                   (56, 200, SH_BLUE), (196, 202, SH_RED)]:
    c.line(bx, by, bx, by - 18, WOOD_D)
    c.poly([(bx + 1, by - 18), (bx + 9, by - 15), (bx + 1, by - 11)], bc)
    c.poly([(bx + 1, by - 18), (bx + 9, by - 15), (bx + 1, by - 11)],
           INK, fill=False)
    c.set(bx + 4, by - 15, SH_GOLD if bc != SH_GOLD else SH_RED)

# =================================================================
# FOREGROUND RIDGE: dark silhouette band framing the bottom
# =================================================================
FG = '#140f1a'
FG_L = '#241d2c'
ridge = [(0, 236)]
for i in range(1, 17):
    x = i * 16
    ridge.append((x, 236 + int(math.sin(i * 1.3) * 4) - (3 if i % 3 else 0)))
ridge += [(256, 238), (256, 256), (0, 256)]
c.poly(ridge, FG)
for i in range(len(ridge) - 3):
    x0, y0 = ridge[i]
    x1, y1 = ridge[i + 1]
    c.line(x0, y0, x1, y1, FG_L)


def fg_knight(x, y, shield, lean=1, crest=SH_RED, s=1):
    """Large foreground knight, ground point x,y. ~34px tall."""
    BODY = '#2c2335'
    PLATE = '#3c3147'
    # cloak
    c.path("M%d %d L%d %d L%d %d L%d %d Z" % (
        x - 2, y - 24, x + 10, y - 24, x + 14, y, x - 6, y), BODY)
    c.path("M%d %d L%d %d L%d %d L%d %d Z" % (
        x - 2, y - 24, x + 10, y - 24, x + 14, y, x - 6, y), INK, fill=False)
    for i in range(-4, 13, 4):
        c.line(x + i, y - 22, x + i + 2, y - 1, INK)
    # legs
    c.rect(x + 1, y - 10, 3, 10, BODY)
    c.rect(x + 7, y - 10, 3, 10, BODY)
    # torso / cuirass
    c.rect(x, y - 26, 11, 14, PLATE)
    c.rect(x, y - 26, 11, 14, INK, fill=False)
    c.rect(x + 8, y - 25, 2, 12, '#50435e')
    # pauldrons
    c.rect(x - 2, y - 27, 4, 4, PLATE)
    c.rect(x + 9, y - 27, 4, 4, PLATE)
    c.rect(x - 2, y - 27, 4, 4, INK, fill=False)
    c.rect(x + 9, y - 27, 4, 4, INK, fill=False)
    # helm
    c.rect(x + 2, y - 34, 7, 8, PLATE)
    c.rect(x + 2, y - 34, 7, 8, INK, fill=False)
    c.rect(x + 3, y - 31, 5, 2, INK)          # visor
    c.rect(x + 4, y - 37, 3, 3, crest)        # crest
    c.set(x + 5, y - 38, crest)
    # rim light, sun side
    c.rect(x + 12, y - 26, 1, 14, ARM_RIM)
    c.rect(x + 9, y - 34, 1, 8, ARM_RIM)
    c.rect(x + 10, y - 2, 4, 2, ARM_RIM)
    # spear
    sx = x + 14
    c.line(sx + lean * 6, y - 62, sx, y - 8, INK)
    c.line(sx + lean * 6 + 1, y - 60, sx + 1, y - 10, WOOD_L)
    c.poly([(sx + lean * 6, y - 72), (sx + lean * 6 - 2, y - 64),
            (sx + lean * 6 + 2, y - 64)], STEEL)
    c.set(sx + lean * 6, y - 73, '#b4b6c8')
    # kite shield
    c.path("M%d %d L%d %d L%d %d Q%d %d %d %d Z" % (
        x - 10, y - 28, x - 1, y - 28, x - 1, y - 12, x - 5, y - 4,
        x - 10, y - 12), shield)
    c.path("M%d %d L%d %d L%d %d Q%d %d %d %d Z" % (
        x - 10, y - 28, x - 1, y - 28, x - 1, y - 12, x - 5, y - 4,
        x - 10, y - 12), INK, fill=False)
    acc = SH_GOLD if shield != SH_GOLD else INK
    c.rect(x - 7, y - 25, 2, 15, acc)
    c.rect(x - 9, y - 21, 7, 2, acc)
    c.rect(x - 10, y - 28, 1, 16, '#c0c2d4')


# four framing knights, centre kept open for the castle silhouette
fg_knight(16, 250, SH_RED, lean=1, crest=SH_RED)
fg_knight(52, 254, SH_BLUE, lean=-1, crest=SH_GOLD)
fg_knight(206, 252, SH_GOLD, lean=-1, crest=SH_BLUE)
fg_knight(240, 256, SH_RED, lean=1, crest=SH_RED)

# mid foreground spear hedge, low and sparse, behind the knights
for i, x in enumerate(range(84, 190, 9)):
    gy = 240 + (i % 3)
    c.line(x + (1 if i % 2 else -1) * 3, gy - 26, x, gy - 4, INK)
    c.set(x + (1 if i % 2 else -1) * 3, gy - 27, STEEL)
    c.rect(x - 2, gy - 10, 5, 10, '#241d2c')
    c.rect(x - 2, gy - 14, 4, 4, '#241d2c')
    c.set(x + 2, gy - 13, ARM_RIM)
    c.rect(x + 2, gy - 10, 1, 9, ARM_RIM)

# two tall foreground standards
for bx, bc in [(98, SH_RED), (178, SH_BLUE)]:
    c.line(bx, 252, bx, 196, WOOD_D)
    c.line(bx + 1, 252, bx + 1, 198, INK)
    c.poly([(bx + 2, 196), (bx + 20, 203), (bx + 2, 212)], bc)
    c.poly([(bx + 2, 196), (bx + 20, 203), (bx + 2, 212)], INK, fill=False)
    c.rect(bx + 7, 202, 4, 4, SH_GOLD)
    c.rect(bx - 1, 193, 3, 4, SH_GOLD)


def arrow(x0, y0, x1, y1, col=STEEL):
    c.line(x0, y0, x1, y1, ARM_D)
    c.set(x1, y1, col)
    # fletching
    mx = x0 + (x1 - x0) // 6
    my = y0 + (y1 - y0) // 6
    c.set(mx, my, '#b8a898')


# arrow volleys: besiegers upward, defenders downward
for i in range(30):
    x0 = random.randrange(0, 90)
    y0 = random.randrange(150, 200)
    dx = random.randrange(7, 13)
    dy = -random.randrange(4, 10)
    arrow(x0, y0, x0 + dx, y0 + dy)
for i in range(26):
    x0 = random.randrange(170, 254)
    y0 = random.randrange(140, 196)
    dx = -random.randrange(7, 13)
    dy = -random.randrange(3, 9)
    arrow(x0, y0, x0 + dx, y0 + dy)
for i in range(18):
    x0 = random.randrange(70, 190)
    y0 = random.randrange(132, 160)
    dx = random.choice([-1, 1]) * random.randrange(8, 13)
    dy = random.randrange(3, 8)
    arrow(x0, y0, x0 + dx, y0 + dy)

# =================================================================
# ANCIENT DRAGON
# =================================================================
drg = new_canvas(W, H, name="dragon")

BODY_PTS = None

# --- wings (far wing first, darker) ---
# far wing, swept back behind the body
drg.path("M118 56 C100 34 72 24 40 26 C56 36 60 44 58 52 "
         "C70 46 78 48 84 54 C92 48 102 50 108 58 Z", DRG_M)
drg.path("M118 56 C100 34 72 24 40 26 C56 36 60 44 58 52 "
         "C70 46 78 48 84 54 C92 48 102 50 108 58 Z", INK, fill=False)
for d in ["M112 55 C96 40 74 32 48 30", "M110 57 C96 44 78 40 58 44",
          "M108 59 C98 52 88 50 76 52"]:
    drg.path(d, DRG_D, fill=False)

# near wing, raised high and spread wide to the right
drg.path("M132 54 C150 22 188 8 232 14 "
         "C214 28 210 40 212 52 "
         "C196 42 184 44 176 54 "
         "C166 44 152 46 144 58 Z", DRG_WING)
drg.path("M132 54 C150 22 188 8 232 14 "
         "C214 28 210 40 212 52 "
         "C196 42 184 44 176 54 "
         "C166 44 152 46 144 58 Z", INK, fill=False)
# wing membrane shading + finger bones
drg.path("M138 50 C156 26 190 14 226 18", DRG_D, fill=False)
drg.path("M140 52 C158 34 186 28 212 34", DRG_D, fill=False)
drg.path("M138 54 C154 42 170 40 186 46", DRG_D, fill=False)
drg.path("M136 56 C148 48 158 48 168 54", DRG_D, fill=False)
# sunlit top edge of the near wing
drg.path("M133 52 C151 21 189 7 231 13", '#8d4440', fill=False)
drg.path("M150 28 C176 16 206 12 228 15", '#c4663a', fill=False)

# --- tail ---
drg.path("M118 70 C96 86 72 98 44 104 C66 98 90 86 108 74 Z", DRG_M)
drg.path("M118 70 C96 86 72 98 44 104", INK, fill=False)
drg.path("M112 66 C92 82 68 94 44 102", INK, fill=False)
# tail fin
drg.poly([(50, 103), (34, 96), (30, 108), (42, 110)], DRG_L)
drg.poly([(50, 103), (34, 96), (30, 108), (42, 110)], INK, fill=False)

# --- body ---
drg.path("M118 50 C136 48 150 56 150 64 C150 76 134 82 120 78 "
         "C110 75 106 66 108 58 Z", DRG_L)
drg.path("M118 50 C136 48 150 56 150 64 C150 76 134 82 120 78 "
         "C110 75 106 66 108 58 Z", INK, fill=False)
# belly plates
for i in range(5):
    drg.line(116 + i * 5, 74 - i, 119 + i * 5, 77 - i, DRG_SPINE)

# --- neck + head, turned to the left, breathing down at the castle ---
drg.path("M112 54 C96 52 82 58 72 70 C68 76 70 82 76 84 "
         "C82 86 86 80 88 74 C92 64 102 60 114 62 Z", DRG_L)
drg.path("M112 54 C96 52 82 58 72 70 C68 76 70 82 76 84 "
         "C82 86 86 80 88 74 C92 64 102 60 114 62 Z", INK, fill=False)

# head
drg.path("M76 72 C66 70 56 76 52 84 C50 90 56 94 64 92 "
         "C72 90 78 84 78 78 Z", DRG_L)
drg.path("M76 72 C66 70 56 76 52 84 C50 90 56 94 64 92 "
         "C72 90 78 84 78 78 Z", INK, fill=False)
# jaw open
drg.poly([(58, 88), (48, 94), (56, 96), (66, 92)], DRG_M)
drg.poly([(58, 88), (48, 94), (56, 96), (66, 92)], INK, fill=False)
# teeth
for tx in (51, 54, 57, 60):
    drg.set(tx, 93, '#e8dcc0')
    drg.set(tx + 1, 90, '#e8dcc0')
# eye
drg.set(66, 82, '#ffe066')
drg.set(67, 82, F_MID)
# horns
drg.path("M74 74 C78 66 86 62 94 62", DRG_SPINE, fill=False)
drg.path("M72 76 C74 68 80 62 88 58", DRG_SPINE, fill=False)
drg.set(94, 62, '#f0e0b0')
drg.set(88, 58, '#f0e0b0')
# cheek frills
drg.poly([(70, 86), (62, 96), (72, 94)], DRG_M)
drg.poly([(70, 86), (62, 96), (72, 94)], INK, fill=False)

# --- spine ridge from head to tail ---
spine = [(96, 56), (106, 50), (118, 46), (130, 47), (140, 52), (146, 60),
         (142, 70), (130, 78), (118, 80), (106, 80)]
for i in range(len(spine) - 1):
    x0, y0 = spine[i]
    x1, y1 = spine[i + 1]
    if i < 6:
        drg.poly([(x0, y0), ((x0 + x1) // 2, y0 - 5), (x1, y1)], DRG_SPINE)
        drg.poly([(x0, y0), ((x0 + x1) // 2, y0 - 5), (x1, y1)], INK,
                 fill=False)

# --- legs and claws ---
drg.path("M124 76 C122 86 116 92 108 96", DRG_M, fill=False)
drg.path("M126 77 C124 87 118 93 110 97", DRG_D, fill=False)
for cxp, cyp in [(106, 96), (109, 99), (112, 97)]:
    drg.line(cxp, cyp, cxp - 3, cyp + 3, DRG_SPINE)
drg.path("M140 74 C142 84 138 92 130 96", DRG_M, fill=False)
drg.path("M141 75 C143 85 139 93 132 97", DRG_D, fill=False)
for cxp, cyp in [(129, 96), (132, 99), (135, 97)]:
    drg.line(cxp, cyp, cxp - 3, cyp + 3, DRG_SPINE)

drg.outline(INK)

# dragon body shading: lit underside from the fires below, cool top
for i in range(6):
    drg.line(114 + i * 6, 76 - i, 118 + i * 6, 79 - i, '#7a3a3a')
drg.path("M116 52 C132 50 146 56 148 64", '#6b3b50', fill=False)
drg.set(60, 90, F_MID)   # firelight on the jaw
drg.set(57, 92, F_IN)
drg.set(54, 94, F_IN)

c.blit(drg, 56, -4)

# dragon shadow over the castle wall
for x in range(96, 178, 2):
    for y in range(150, 158, 2):
        if (x + y) % 4 == 0:
            c.set(x, y, '#3f3a4c')

# --- dragon fire breath, aimed down-left at the castle ---
BX, BY = 56 + 50, -4 + 94
c.path("M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d Z" % (
    BX, BY - 4, BX - 24, BY + 10, BX - 44, BY + 30, BX - 54, BY + 58,
    BX - 34, BY + 40, BX - 18, BY + 22, BX + 4, BY + 4), F_OUT)
c.path("M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d Z" % (
    BX - 1, BY - 2, BX - 22, BY + 12, BX - 38, BY + 30, BX - 46, BY + 52,
    BX - 30, BY + 38, BX - 16, BY + 22, BX + 1, BY + 5), F_MID)
c.path("M%d %d C%d %d %d %d %d %d C%d %d %d %d %d %d Z" % (
    BX - 2, BY, BX - 18, BY + 14, BX - 30, BY + 28, BX - 36, BY + 44,
    BX - 24, BY + 34, BX - 14, BY + 20, BX - 1, BY + 6), F_IN)
c.path("M%d %d C%d %d %d %d %d %d" % (
    BX - 3, BY + 2, BX - 14, BY + 12, BX - 20, BY + 20, BX - 24, BY + 32),
    F_CORE, fill=False)
# fire impact glow where the breath lands
soft_circle(c, BX - 56, BY + 62, 9, F_OUT, edge=4)
soft_circle(c, BX - 56, BY + 62, 5, F_MID, edge=2)
soft_circle(c, BX - 56, BY + 62, 2, F_CORE, edge=1)
for i in range(40):
    a = random.random() * math.tau
    r = random.random() * 18
    x = int(BX - 56 + math.cos(a) * r)
    y = int(BY + 62 + math.sin(a) * r * 0.7)
    if 0 <= x < W and 0 <= y < H:
        c.set(x, y, random.choice([F_MID, F_IN, F_OUT]))

# =================================================================
# EMBERS + ATMOSPHERE
# =================================================================
for i in range(220):
    x = random.randrange(0, W)
    y = random.randrange(20, 250)
    r = random.random()
    col = EMB_1 if r < 0.3 else (EMB_2 if r < 0.7 else F_OUT)
    c.set(x, y, col)
    if r < 0.08:
        c.set(x, y - 1, col)

# warm haze along the horizon behind the castle
for i in range(260):
    x = random.randrange(0, W)
    y = random.randrange(148, 176)
    if random.random() < 0.3:
        c.set(x, y, '#6b3324')

# god rays from the sun, low opacity dither
for i, (ax, ay) in enumerate([(120, 150), (150, 160), (230, 170), (250, 120)]):
    steps = 90
    for s in range(steps):
        t = s / steps
        x = int(186 + (ax - 186) * t)
        y = int(134 + (ay - 134) * t)
        if (x + y) % 6 == 0 and 0 <= x < W and 0 <= y < H:
            c.set(x, y, '#f3b94e')

# final vignette: a faint darkening of the extreme corners only
for y in range(H):
    for x in range(W):
        dx = (x - 128) / 128.0
        dy = (y - 128) / 128.0
        d = dx * dx + dy * dy
        if d > 1.62 and (x + y) % 4 == 0:
            c.set(x, y, INK)
        elif d > 1.86 and (x + y) % 2 == 0:
            c.set(x, y, INK)

view(c)
print(c.stats_text())
save("dragon_battle", c)
finish(c)
