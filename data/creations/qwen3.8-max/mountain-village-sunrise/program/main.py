import math
try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 128
c = new_canvas(W, H, name="village")

BAYER = ((0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))


def bt(x, y):
    return (BAYER[y & 3][x & 3] + 0.5) / 16.0


def hx(t):
    return '#%02x%02x%02x' % (int(t[0]), int(t[1]), int(t[2]))


def px(x, y, col):
    if 0 <= x < W and 0 <= y < H:
        c.set(int(x), int(y), col)


def profile(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    out = []
    for x in range(W):
        if x <= xs[0]:
            out.append(ys[0])
            continue
        if x >= xs[-1]:
            out.append(ys[-1])
            continue
        for i in range(len(pts) - 1):
            if xs[i] <= x <= xs[i + 1]:
                t = (x - xs[i]) / float(xs[i + 1] - xs[i])
                out.append(int(round(ys[i] + (ys[i + 1] - ys[i]) * t)))
                break
    return out


# =====================================================================
# SKY
# =====================================================================
SKY = ((0, (20, 16, 40)), (12, (44, 30, 68)), (26, (92, 49, 96)),
       (40, (156, 82, 78)), (54, (204, 122, 72)), (70, (236, 164, 84)),
       (84, (250, 198, 118)), (100, (255, 224, 164)))


def sky_pair(y):
    for i in range(len(SKY) - 1):
        y0, c0 = SKY[i]
        y1, c1 = SKY[i + 1]
        if y <= y1:
            t = (y - y0) / float(y1 - y0)
            return c0, c1, t
    return SKY[-1][1], SKY[-1][1], 0.0


for y in range(H):
    a, b, t = sky_pair(y)
    ca, cb = hx(a), hx(b)
    for x in range(W):
        c.set(x, y, cb if t > bt(x, y) else ca)

# =====================================================================
# SUN + GLOW
# =====================================================================
SUNX, SUNY, SUNR = 88, 45, 10
GLOW = ((14, (255, 228, 166), 0.75), (21, (255, 204, 130), 0.45),
        (31, (255, 178, 110), 0.22), (45, (250, 156, 104), 0.10))
for y in range(0, 104):
    for x in range(W):
        d = math.hypot(x - SUNX, (y - SUNY) * 1.05)
        for r, col, p in GLOW:
            if d <= r:
                if p > bt(x, y):
                    c.set(x, y, hx(col))
                break

c.circle(SUNX, SUNY, SUNR, '#ffe3a2', fill=True)
c.circle(SUNX, SUNY, SUNR - 3, '#fff1c6', fill=True)
c.circle(SUNX, SUNY - 1, SUNR - 6, '#fffae2', fill=True)


# =====================================================================
# CLOUDS
# =====================================================================
def cloud(cx, cy, rx, ry, dark, mid, lit):
    c.ellipse(cx, cy, rx, ry, dark, fill=True)
    c.ellipse(cx - rx // 3, cy - 1, rx // 2, ry, dark, fill=True)
    c.ellipse(cx + 1, cy + 1, rx - 1, max(1, ry - 1), mid, fill=True)
    c.ellipse(cx + 2, cy + 2, rx - 3, max(1, ry - 1), lit, fill=True)


CD, CM, CL = '#7a4668', '#b06a72', '#f0a468'
cloud(26, 24, 14, 3, CD, CM, CL)
cloud(52, 16, 10, 2, CD, CM, CL)
cloud(104, 20, 12, 3, CD, CM, CL)
cloud(74, 32, 8, 2, CD, CM, CL)
cloud(14, 40, 9, 2, CD, CM, CL)

# birds
def bird(x, y, col='#241a3a'):
    c.line(x, y, x + 1, y - 1, col)
    c.line(x + 1, y - 1, x + 2, y, col)
    c.line(x + 2, y, x + 3, y - 1, col)
    c.line(x + 3, y - 1, x + 4, y, col)


bird(30, 52)
bird(38, 47)
bird(44, 55)

# =====================================================================
# MOUNTAIN RANGES
# =====================================================================
def draw_range(prof, base, col, hi, sh, snow=None, snow_y=None,
               lit_depth=3, sh_depth=5):
    for x in range(W):
        y = prof[x]
        c.rect(x, y, 1, base - y + 1, col)
    # snow caps
    if snow is not None:
        for x in range(W):
            y = prof[x]
            if y <= snow_y:
                d = 2 + ((x * 5) % 3) + max(0, (snow_y - y) // 4)
                for k in range(d):
                    px(x, y + k, snow)
                # dithered lower edge
                for k in range(d, d + 2):
                    if bt(x, y + k) < 0.5:
                        px(x, y + k, snow)
    # slope shading
    for x in range(W):
        y = prof[x]
        sl = prof[max(0, x - 3)]
        sr = prof[min(W - 1, x + 3)]
        slope = sr - sl
        if slope >= 3:
            for k in range(lit_depth):
                px(x, y + k, hi)
            if bt(x, y) < 0.5:
                px(x, y + lit_depth, hi)
        elif slope <= -3:
            for k in range(sh_depth):
                px(x, y + k, sh)
            if bt(x, y) < 0.5:
                px(x, y + sh_depth, sh)
        else:
            px(x, y, hi)


def mist(prof, top, bot, col, maxp=0.8):
    for y in range(top, bot + 1):
        t = (y - top) / float(max(1, bot - top))
        p = maxp * (0.25 + 0.75 * t)
        for x in range(W):
            if y >= prof[x] and p > bt(x, y):
                c.set(x, y, col)


# --- far range ---
FAR = profile([(0, 70), (8, 62), (16, 53), (24, 58), (32, 49), (40, 55),
               (48, 45), (56, 53), (64, 48), (72, 57), (80, 52), (88, 49),
               (96, 57), (104, 50), (112, 59), (120, 54), (127, 61)])
draw_range(FAR, 100, '#8d79ad', '#b6a2d0', '#746093',
           snow='#e9dff4', snow_y=52)
mist(FAR, 84, 98, '#c3a8c4', 0.75)

# --- mid range ---
MID = profile([(0, 82), (8, 74), (16, 65), (24, 70), (32, 61), (40, 68),
               (48, 75), (56, 82), (64, 86), (72, 84), (80, 79), (88, 73),
               (96, 67), (104, 61), (112, 68), (120, 63), (127, 71)])
draw_range(MID, 110, '#6a5a8b', '#8d78a8', '#524473',
           snow='#d8cbe6', snow_y=64, lit_depth=3, sh_depth=6)
mist(MID, 94, 106, '#b392ab', 0.7)

# --- near hills (blue green) ---
NEAR = profile([(0, 98), (10, 94), (20, 98), (30, 92), (40, 96), (50, 93),
                (60, 96), (70, 93), (80, 97), (90, 93), (100, 97),
                (110, 94), (120, 98), (127, 95)])
draw_range(NEAR, 127, '#41545a', '#5d7268', '#33454b', lit_depth=2, sh_depth=4)
mist(NEAR, 100, 108, '#b392ab', 0.4)


# =====================================================================
# PINE TREES
# =====================================================================
def pine(x, base, h, col, hi, dk, layers=4, trunk=True, wf=0.30):
    x = int(x)
    base = int(base)
    hw = max(2, int(round(h * wf)))
    if trunk:
        c.rect(x, base - 3, 1, max(0, min(4, H - (base - 3))), dk)
    n = layers
    for i in range(n):
        apex_y = base - h + int(i * (h * 0.60) / n)
        bot_y = apex_y + int(h * 0.34) + 2
        t = (i + 1) / float(n)
        w_i = max(1, int(round(hw * t)))
        c.poly([(x, apex_y), (x - w_i, bot_y), (x + w_i, bot_y)], col, fill=True)
        # lit right edge
        for yy in range(apex_y, bot_y + 1):
            f = (yy - apex_y) / float(max(1, bot_y - apex_y))
            xr = x + int(round(w_i * f))
            if bt(x, yy) < 0.75:
                px(xr, yy, hi)
        # dark left edge
        for yy in range(apex_y + 1, bot_y + 1):
            f = (yy - apex_y) / float(max(1, bot_y - apex_y))
            xl = x - int(round(w_i * f))
            px(xl, yy, dk)


# distant hazy pines on the near hill crest
for x, hh in ((4, 9), (9, 12), (14, 8), (19, 11), (25, 9), (31, 13), (36, 10),
              (42, 8), (86, 10), (92, 13), (98, 9), (104, 12), (110, 10),
              (116, 13), (122, 9), (126, 11)):
    y0 = NEAR[x] + 1
    pine(x, y0, hh, '#3b4f4a', '#4d6357', '#2c3d3a', layers=2, trunk=False)

# =====================================================================
# VALLEY FLOOR
# =====================================================================
VAL = profile([(0, 104), (12, 101), (24, 105), (36, 100), (48, 103),
               (60, 100), (72, 103), (84, 100), (96, 104), (108, 101),
               (120, 105), (127, 102)])
for x in range(W):
    y = VAL[x]
    c.rect(x, y, 1, H - y, '#465a41')
# warm lit ground toward the right (sun side) + crest highlight
for x in range(W):
    y = VAL[x]
    for k in range(2):
        px(x, y + k, '#6a7449')
    if bt(x, y) < 0.5:
        px(x, y + 2, '#6a7449')
for y in range(100, H):
    for x in range(W):
        t = (x - 40) / 90.0
        if t > 0 and y >= VAL[x] + 2:
            if t * 0.55 > bt(x, y):
                px(x, y, '#54684a')
# shadowed ground bottom-left
for y in range(104, H):
    for x in range(W):
        if y >= VAL[x] + 2:
            t = (60 - x) / 90.0 + (y - 104) / 60.0
            if t > 0 and t * 0.7 > bt(x, y):
                px(x, y, '#2c4131')

# mid-ground pine cluster behind the village
for x, hh in ((6, 20), (12, 26), (18, 18), (24, 23), (30, 17), (36, 21),
              (43, 16), (48, 20), (84, 19), (90, 24), (96, 17), (102, 22),
              (108, 18), (114, 25), (120, 19), (125, 22)):
    pine(x, VAL[x] + 4, hh, '#2c4131', '#3d5740', '#213325', layers=3, trunk=False)

# =====================================================================
# HOUSES
# =====================================================================
WOOD_DK = '#4e3320'
WOOD_LN = '#74492a'
WOOD = '#8a5c33'
WOOD_LT = '#a97442'
WOOD_HI = '#c98f52'
ROOF_DK = '#33201a'
ROOF = '#573627'
ROOF_LT = '#7c4c33'
ROOF_HI = '#a56a41'
STONE_D = '#3b352c'
STONE = '#574e41'
STONE_L = '#736853'
WIN = '#ffc95f'
WIN_H = '#ffeeb0'
FRAME = '#33201a'
CHIM = '#4a4238'
CHIM_L = '#6b6252'
CHIM_D = '#332e26'


def wall_region(x, y, w, h, base, line):
    c.rect(x, y, w, h, base)
    for yy in range(y + 2, y + h - 1, 3):
        c.rect(x, yy, w, 1, line)


def house(x0, w, base_y, wall_h, roof_h, over=3, wins=(), door=None,
          chim=None, glow=True):
    x0 = int(x0)
    top_y = base_y - wall_h - roof_h
    eave_y = base_y - wall_h
    cx = x0 + w // 2
    # chimney behind roof
    if chim:
        cxp, cw, ch = chim
        c.rect(cxp, top_y - ch, cw, ch + 3, CHIM)
        c.rect(cxp, top_y - ch, 1, ch + 3, CHIM_D)
        c.rect(cxp + cw - 1, top_y - ch, 1, ch + 3, CHIM_L)
        c.rect(cxp - 1, top_y - ch - 1, cw + 2, 2, CHIM_L)
        c.rect(cxp - 1, top_y - ch + 1, cw + 2, 1, CHIM_D)
    # walls
    sh_w = max(2, w // 3)
    lt_w = max(3, w // 4)
    wall_region(x0, eave_y, sh_w, wall_h, WOOD_DK, '#3d2718')
    wall_region(x0 + sh_w, eave_y, w - sh_w - lt_w, wall_h, WOOD, WOOD_LN)
    wall_region(x0 + w - lt_w, eave_y, lt_w, wall_h, WOOD_LT, WOOD_LN)
    for yy in range(eave_y, base_y):
        px(x0 + w - 1, yy, WOOD_HI)
    # foundation
    c.rect(x0, base_y - 2, w, 2, STONE)
    for xx in range(x0, x0 + w, 3):
        px(xx, base_y - 2, STONE_L)
        px(xx, base_y - 1, STONE_D)
    # roof, row by row
    half = w / 2.0 + over
    for yy in range(top_y, eave_y + 1):
        t = (yy - top_y) / float(max(1, eave_y - top_y))
        hw = t * half
        xl = int(round(cx - hw))
        xr = int(round(cx + hw))
        row_dark = ((yy - top_y) % 4 == 3)
        split = cx + int(t * 2)
        for xx in range(xl, split):
            px(xx, yy, ROOF_DK if row_dark else ROOF)
        for xx in range(split, xr + 1):
            px(xx, yy, ROOF if row_dark else ROOF_LT)
        px(xr, yy, ROOF_HI)
        px(xr - 1, yy, ROOF_HI if not row_dark else ROOF_LT)
        px(xl, yy, ROOF_DK)
    # eave shadow on the wall
    c.rect(x0 - over, eave_y, w + over * 2, 1, ROOF_DK)
    for xx in range(x0, x0 + w):
        if bt(xx, eave_y) < 0.6:
            px(xx, eave_y + 1, WOOD_DK)
    # ridge cap
    c.line(cx - 1, top_y, cx + 1, top_y, ROOF_HI)
    # windows
    for (wx, wy, ww, wh) in wins:
        c.rect(wx, wy, ww, wh, FRAME)
        c.rect(wx + 1, wy + 1, ww - 2, wh - 2, WIN)
        c.rect(wx + 1, wy + 1, ww - 2, 1, WIN_H)
        if ww >= 5:
            c.rect(wx + ww // 2, wy + 1, 1, wh - 2, FRAME)
        c.rect(wx + 1, wy + wh // 2, ww - 2, 1, FRAME)
        if glow:
            for k in range(1, 4):
                for xx in range(wx - k, wx + ww + k):
                    if bt(xx, wy + wh + k) < 0.35 / k:
                        px(xx, wy + wh + k, WOOD_LN)
    # door
    if door:
        dx, dy, dw, dh = door
        c.rect(dx, dy, dw, dh, FRAME)
        c.rect(dx + 1, dy + 1, dw - 2, dh - 1, WOOD_LN)
        c.rect(dx + 1, dy + 1, 1, dh - 1, WOOD_DK)
        px(dx + dw - 2, dy + dh // 2, WIN_H)


# --- left house (smaller, in shadow) ---
house(18, 20, 114, 12, 9, over=3,
      wins=[(22, 105, 5, 4), (31, 105, 5, 4)],
      door=(26, 106, 5, 8), chim=(32, 4, 4))

# --- right house ---
house(90, 22, 113, 13, 10, over=3,
      wins=[(94, 103, 5, 4), (104, 103, 5, 4)],
      door=(99, 105, 5, 8), chim=(105, 4, 5))

# --- centre house (focal, largest) ---
house(50, 28, 115, 16, 12, over=4,
      wins=[(54, 104, 6, 5), (69, 104, 6, 5)],
      door=(62, 105, 6, 10), chim=(69, 5, 8))

# warm light spill on the ground from the centre door
for k in range(1, 7):
    for xx in range(62 - k, 68 + k):
        if bt(xx, 115 + k) < 0.5 - k * 0.06:
            px(xx, 115 + k, WOOD_LN)

# =====================================================================
# FOREGROUND BAND
# =====================================================================
FG = profile([(0, 116), (10, 118), (20, 116), (30, 119), (40, 117),
              (50, 120), (60, 121), (70, 121), (80, 120), (90, 117),
              (100, 119), (110, 116), (120, 118), (127, 116)])
for x in range(W):
    y = FG[x]
    c.rect(x, y, 1, H - y, '#2b3b2a')
for x in range(W):
    y = FG[x]
    px(x, y, '#465a3c')
    if bt(x, y) < 0.55:
        px(x, y + 1, '#465a3c')
for y in range(114, H):
    for x in range(W):
        if y >= FG[x] + 1:
            t = (y - 116) / 14.0 + (55 - x) / 130.0
            if t > 0 and t * 0.8 > bt(x, y):
                px(x, y, '#212e21')

# =====================================================================
# STONE PATH
# =====================================================================
def path_edges(y):
    t = (y - 113) / float(H - 113)
    t = max(0.0, min(1.0, t))
    hw = 3.5 + t * t * 13.0
    cxp = 64.5 - t * 1.5
    return int(round(cxp - hw)), int(round(cxp + hw))


for y in range(113, H):
    xl, xr = path_edges(y)
    for x in range(xl, xr + 1):
        c.set(x, y, '#6b5a42')
for y in range(113, H):
    xl, xr = path_edges(y)
    for x in range(xl, xr + 1):
        if bt(x, y) < 0.4:
            c.set(x, y, '#7a6749')
    for x in (xl, xl + 1, xr, xr - 1):
        if bt(x, y) < 0.7:
            c.set(x, y, '#4d4130')

# stones
stones = []
yy = 115
row = 0
while yy < H:
    xl, xr = path_edges(yy)
    span = xr - xl
    n = max(2, int(span / 6))
    for i in range(n):
        sx = xl + 1 + int((i + 0.5) * (span - 2) / n) + ((row * 3 + i * 5) % 3) - 1
        sw = 2 + (row % 2) + (1 if row > 3 else 0)
        sh = 2 if row < 4 else 3
        stones.append((sx, yy, sw, sh))
    yy += 3 if row < 4 else 4
    row += 1

for (sx, sy, sw, sh) in stones:
    if sy + sh > H:
        continue
    c.rect(sx, sy, sw, sh, '#857761')
    c.rect(sx, sy, sw, 1, '#a2937a')
    c.rect(sx, sy + sh - 1, sw, 1, '#4d4130')
    px(sx + sw - 1, sy, STONE_L)

# =====================================================================
# FENCE + FOREGROUND DETAILS
# =====================================================================
def fence(x0, x1, y, col=WOOD_DK, lit=WOOD_LN):
    for xx in range(x0, x1, 6):
        c.rect(xx, y - 7, 2, 8, col)
        px(xx + 1, y - 7, lit)
    c.rect(x0, y - 6, x1 - x0, 1, col)
    c.rect(x0, y - 3, x1 - x0, 1, col)
    for xx in range(x0, x1):
        if bt(xx, y) < 0.3:
            px(xx, y - 6, lit)


fence(38, 56, 116)
fence(76, 92, 116)


def tuft(x, y, col, col2=None):
    px(x, y, col)
    px(x - 1, y + 1, col)
    px(x + 1, y + 1, col)
    px(x, y - 1, col2 or col)
    px(x + 2, y, col)
    px(x - 2, y + 1, col)


for (tx, ty) in ((8, 122), (16, 125), (24, 120), (33, 124), (42, 122),
                 (95, 121), (104, 125), (113, 120), (121, 124), (28, 118),
                 (88, 119), (100, 118), (14, 118), (50, 126), (84, 126)):
    tuft(tx, ty, '#465a3c', '#54684a')

# rocks
def rock(x, y, r):
    c.ellipse(x, y, r, max(1, r - 1), CHIM)
    c.ellipse(x, y - 1, r - 1, max(1, r - 2), CHIM_L)
    for xx in range(x - r + 1, x + r):
        px(xx, y - r + 1, STONE_L)


rock(20, 124, 4)
rock(108, 123, 3)
rock(6, 118, 2)

# =====================================================================
# FRAMING FOREGROUND PINES
# =====================================================================
pine(5, 128, 60, '#1a2a1e', '#2b4030', '#12201a', layers=5, wf=0.40)
pine(16, 128, 42, '#1e3023', '#31492f', '#152418', layers=5, wf=0.40)
pine(123, 128, 64, '#182819', '#2a3d2c', '#101c14', layers=5, wf=0.40)
pine(112, 128, 44, '#1c2c1f', '#2f4530', '#14221a', layers=5, wf=0.40)

# =====================================================================
# CHIMNEY SMOKE
# =====================================================================
def smoke(x0, y0, height, drift, width, cols, wob=1.6):
    for i in range(height):
        y = y0 - i
        t = i / float(height)
        cxp = x0 + drift * (t ** 1.35) + wob * math.sin(i * 0.28)
        w = width + t * 6.0
        dens = (1.0 - t) ** 1.05
        ci = 0 if t < 0.35 else (1 if t < 0.7 else 2)
        col = cols[ci]
        for dx in range(-int(w) - 1, int(w) + 2):
            xx = int(round(cxp)) + dx
            d = abs(dx) / float(w + 0.5)
            if d > 1.0:
                continue
            p = dens * (1.0 - d * d * 0.8)
            if p > bt(xx, y) * 0.5:
                px(xx, y, col)


SMOKE_COLS = ('#f0e0d4', '#c9b3ab', '#c9b3ab')
smoke(72, 78, 44, 13, 2.0, SMOKE_COLS)
smoke(34, 87, 32, 9, 1.6, SMOKE_COLS)
smoke(107, 83, 28, 8, 1.4, SMOKE_COLS)

# =====================================================================
print(c.stats_text())
view(c)
save('village', c)
finish(c)
