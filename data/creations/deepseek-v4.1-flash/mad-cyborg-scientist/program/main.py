import math

W = H = 64
c = new_canvas(W, H, None, name="result")

# ---------------- palette ----------------
BG0    = '#07080b'
BG1    = '#0f1420'
BG2    = '#171e2c'
BG3    = '#222c3f'
SK_HI  = '#ffdcb4'
SK_HI2 = '#f2c99b'
SK     = '#d8a273'
SK_MD  = '#bb8154'
SK_SH  = '#945c39'
SK_DK  = '#6b3d24'
SK_DK2 = '#432413'
EYE_W  = '#f2ead8'
IRIS   = '#4f8fa8'
PUPIL  = '#0e161c'
HAIR_HI = '#ffffff'
HAIR   = '#e6ebf4'
HAIR_MD = '#bcc4d3'
HAIR_SH = '#8e97ab'
HAIR_DK = '#5f677a'
M_HI   = '#f2f7fd'
M      = '#c2cfdd'
M_MD   = '#8e9dae'
M_SH   = '#5e6b7c'
M_DK   = '#3b4552'
M_DK2  = '#232a34'
CY_HI  = '#d6fffa'
CY     = '#5ef2e6'
CY_MD  = '#22c9c4'
CY_DK  = '#0f7f8a'
CY_DK2 = '#0a4a55'
CO_HI  = '#f4f0e4'
CO     = '#d8d2c1'
CO_MD  = '#b0a996'
CO_SH  = '#877f6d'
CO_DK  = '#5b5447'
DIRT   = '#8a7a4f'
DIRT2  = '#63563a'
LE_HI  = '#946a4c'
LE     = '#6d4a33'
LE_MD  = '#4c3324'
LE_DK  = '#2d1e14'
BELT   = '#31251c'
BRASS  = '#c9a24a'
BRASS_HI = '#f2d97e'
MOUTH  = '#2a1210'
MOUTH2 = '#4a2018'
TOOTH  = '#f6f0e2'
TOOTH_D = '#c9c0a8'
WIRE   = '#c2382e'
WIRE_HI = '#e8705f'

BAYER4 = ((0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))


def quant(t, n, x, y, s=0.55):
    v = t * (n - 1) + (BAYER4[y & 3][x & 3] / 16.0 - 0.5) * s
    i = int(math.floor(v + 0.5))
    return 0 if i < 0 else (n - 1 if i > n - 1 else i)


def hln(y, x0, x1, col):
    if x1 < x0:
        return
    c.rect(x0, y, x1 - x0 + 1, 1, col)


def mask_pixels(drawfn, sent='#010203', ink='#040506'):
    scr = new_canvas(W, H, None)
    scr.rect(0, 0, W, H, sent)
    drawfn(scr, ink)
    ii = scr.color(ink)
    out = set()
    for y in range(H):
        for x in range(W):
            if scr.get(x, y) == ii:
                out.add((x, y))
    return out


def cyl(y, x0, x1, ramp, bright=0.3, s=0.5):
    n = max(1, x1 - x0)
    for x in range(x0, x1 + 1):
        u = (x - x0) / n
        t = min(1.0, abs(u - bright) * 1.45)
        c.set(x, y, ramp[quant(t, len(ramp), x, y, s)])


# ================= BACKGROUND =================
c.rect(0, 0, W, H, BG0)
ramp_bg = [BG3, BG2, BG1, BG0]
for y in range(H):
    for x in range(W):
        dx = (x - 31) / 30.0
        dy = (y - 18) / 28.0
        d = math.sqrt(dx * dx + dy * dy)
        if d > 1.0:
            d = 1.0
        c.set(x, y, ramp_bg[quant(d, 4, x, y, 0.9)])

# ================= NECK =================
NECK = {34: (29, 35), 35: (28, 36), 36: (28, 36), 37: (28, 36), 38: (27, 37),
        39: (27, 37), 40: (26, 38), 41: (26, 38), 42: (26, 38), 43: (25, 39),
        44: (25, 39)}
for y in sorted(NECK):
    x0, x1 = NECK[y]
    for x in range(x0, x1 + 1):
        if x <= 31:
            t = 0.18 + 0.62 * (x - x0) / max(1, x1 - x0) + (0.28 if y < 39 else 0)
            c.set(x, y, [SK_HI2, SK, SK_MD, SK_SH, SK_DK][quant(min(t, 1), 5, x, y, 0.5)])
        else:
            t = 0.15 + 0.70 * (x - 32) / max(1, x1 - 32) + (0.28 if y < 39 else 0)
            c.set(x, y, [M, M_MD, M_SH, M_DK, M_DK2][quant(min(t, 1), 5, x, y, 0.5)])

# ================= COAT =================
COAT_SEG = {39: [(20, 26), (38, 45)], 40: [(17, 26), (38, 48)],
            41: [(14, 25), (39, 51)], 42: [(12, 25), (39, 53)],
            43: [(10, 24), (40, 55)], 44: [(8, 24), (40, 57)],
            45: [(6, 58)], 46: [(5, 60)], 47: [(4, 61)], 48: [(3, 62)],
            49: [(2, 63)], 50: [(2, 63)], 51: [(2, 63)], 52: [(2, 63)]}
for y in range(53, 64):
    COAT_SEG[y] = [(2, 63)]

ramp_coat = [CO_HI, CO, CO_MD, CO_SH, CO_DK]
for y in sorted(COAT_SEG):
    for (x0, x1) in COAT_SEG[y]:
        for x in range(x0, x1 + 1):
            t = 0.13 + 0.52 * (x - 2) / 61.0 + 0.28 * (y - 39) / 24.0
            c.set(x, y, ramp_coat[quant(t, 5, x, y, 0.6)])

# shadow under the jaw / neck on the chest
for y in range(43, 51):
    w = 10 + (y - 43) * 2
    hln(y, 32 - w // 2, 32 + w // 2, CO_SH if y % 2 else CO_DK)
# fold lines
c.line(9, 49, 14, 63, CO_SH)
c.line(11, 52, 16, 63, CO_MD)
c.line(56, 49, 60, 63, CO_DK)
c.line(5, 51, 9, 63, CO_MD)
c.line(44, 46, 48, 56, CO_SH)

# collar / lapels hugging the neck opening
for y, (a, b) in {39: (25, 27), 40: (24, 27), 41: (23, 26), 42: (22, 26),
                  43: (21, 25), 44: (20, 25), 45: (19, 24), 46: (18, 24),
                  47: (17, 23), 48: (16, 22), 49: (16, 21)}.items():
    hln(y, a, b, CO_HI)
    c.set(a, y, CO_MD)
for y, (a, b) in {39: (36, 38), 40: (37, 40), 41: (37, 41), 42: (38, 42),
                  43: (38, 43), 44: (39, 44), 45: (39, 45), 46: (40, 46),
                  47: (41, 47), 48: (41, 47), 49: (42, 48)}.items():
    hln(y, a, b, CO_HI)
    c.set(b, y, CO_SH)

# ================= APRON =================
APRON = {46: (27, 37), 47: (26, 38), 48: (25, 39), 49: (24, 40), 50: (24, 41),
         51: (23, 42), 52: (23, 43), 53: (22, 43), 54: (22, 44), 55: (21, 45),
         56: (21, 45), 57: (20, 46), 58: (20, 46), 59: (20, 46), 60: (20, 46),
         61: (19, 47), 62: (19, 47), 63: (19, 47)}
ramp_le = [LE_HI, LE, LE_MD, LE_DK]
for y in sorted(APRON):
    x0, x1 = APRON[y]
    for x in range(x0, x1 + 1):
        t = 0.05 + 0.55 * (x - 19) / 28.0 + 0.22 * (y - 46) / 18.0
        c.set(x, y, ramp_le[quant(t, 4, x, y, 0.55)])
# apron straps (narrow)
for i in range(4):
    c.line(27 + i, 47, 23 + i, 41, LE_HI if i in (0, 3) else LE)
    c.line(38 + i, 47, 42 + i, 41, LE_MD if i < 2 else LE)
# apron edge stitches
for y in range(49, 63, 3):
    x0, x1 = APRON[y]
    c.set(x0 + 1, y, LE_HI)
    c.set(x1 - 1, y, LE_DK)
# central seam + pocket
c.line(33, 48, 33, 56, LE_DK)
hln(49, 25, 31, LE_DK)
c.rect(25, 50, 7, 6, LE_MD)
hln(50, 25, 31, LE_HI)
c.rect(26, 51, 5, 4, LE)
c.set(30, 51, LE_DK)
# dirt
c.ellipse(27, 58, 3, 2, DIRT2)
c.set(26, 57, DIRT)
c.set(24, 60, DIRT2)

# ================= TOOL BELT =================
hln(57, 10, 53, '#3d2f24')
hln(58, 9, 53, BELT)
hln(59, 9, 53, BELT)
hln(60, 10, 52, LE_DK)
hln(61, 12, 50, BELT)
for x in range(11, 53, 5):
    c.set(x, 59, LE_MD)
# buckle
hln(57, 29, 36, BRASS_HI)
hln(58, 28, 37, BRASS)
hln(59, 28, 37, BRASS)
hln(60, 29, 36, BRASS_HI)
c.rect(31, 58, 3, 2, BELT)
c.set(30, 57, BRASS_HI)
# hanging tools
c.rect(13, 61, 5, 3, LE_MD)
c.set(13, 61, LE_HI)
c.rect(41, 61, 4, 3, LE_MD)
c.set(44, 61, LE_HI)
c.rect(20, 61, 2, 3, LE_DK)
c.rect(46, 58, 2, 6, M_MD)
c.rect(46, 56, 2, 2, M)
c.set(45, 56, M_SH)

# ================= HEAD =================
HEAD = {8: (24, 39), 9: (22, 41), 10: (20, 43), 11: (19, 44), 12: (18, 45),
        13: (17, 46), 14: (17, 46), 15: (16, 47), 16: (16, 47), 17: (16, 47),
        18: (16, 47), 19: (16, 47), 20: (16, 47), 21: (16, 47), 22: (16, 47),
        23: (16, 47), 24: (16, 47), 25: (17, 46), 26: (17, 46), 27: (18, 45),
        28: (19, 44), 29: (20, 43), 30: (21, 42), 31: (22, 41), 32: (23, 40),
        33: (24, 39), 34: (26, 37), 35: (27, 36), 36: (28, 35), 37: (29, 34)}

SKIN_RAMP = [SK_HI, SK_HI2, SK, SK_MD, SK_SH, SK_DK]
METAL_RAMP = [M_HI, M, M_MD, M_SH, M_DK, M_DK2]


def skin_t(x, y):
    t = 0.50 * (x - 16) / 16.0 + 0.50 * (y - 9) / 28.0
    if y > 30:
        t += (y - 30) * 0.035
    return t


def metal_t(x, y):
    t = 0.45 * (x - 32) / 15.0 + 0.45 * (y - 9) / 28.0 + 0.06
    if y > 30:
        t += (y - 30) * 0.03
    return t


for y in sorted(HEAD):
    x0, x1 = HEAD[y]
    for x in range(x0, x1 + 1):
        if x <= 31:
            c.set(x, y, SKIN_RAMP[quant(skin_t(x, y), 6, x, y, 0.5)])
        else:
            c.set(x, y, METAL_RAMP[quant(metal_t(x, y), 6, x, y, 0.5)])

# rim light on the left silhouette edge
for y in range(15, 29):
    c.set(HEAD[y][0], y, SK_HI)
for y in range(29, 34):
    c.set(HEAD[y][0], y, SK_HI2)
# cyan edge light on the robot side
for y in range(11, 36):
    x1 = HEAD[y][1]
    c.set(x1, y, CY_DK if (y % 4) else CY_MD)
    if y % 5 == 2:
        c.set(x1 - 1, y, CY_DK2)
# bright metal edge at the split
for y in range(11, 34):
    c.set(32, y, M_HI)
for y in (14, 20, 26, 31):
    c.set(33, y, M_HI)
    c.set(33, y + 1, M_SH)

# ---- metal plate details ----
hln(18, 34, 46, M_DK)
hln(17, 34, 45, M_MD)
for x in range(35, 45, 3):
    c.set(x, 16, M_HI)
c.line(44, 12, 44, 16, M_DK)
c.line(45, 12, 45, 16, M_SH)
for y in range(25, 31):
    c.set(41, y, M_DK)
    c.set(42, y, M_MD)
for x in range(34, 40, 2):
    c.set(x, 28, M_DK)
    c.set(x, 29, M_DK2)
c.line(33, 31, 40, 33, M_DK)
c.line(33, 30, 39, 32, M_MD)
for (rx, ry) in [(34, 16), (37, 16), (34, 30), (45, 21), (36, 25)]:
    c.set(rx, ry, M_HI)
    c.set(rx + 1, ry, M_SH)

# ---- eye glow halo (before mouth) ----
for y in range(14, 28):
    for x in range(33, 48):
        d = math.hypot(x - 40, (y - 21) * 1.15)
        if d < 8.0:
            p = (8.0 - d) / 8.0
            if BAYER4[y & 3][x & 3] / 16.0 < p * 0.85:
                c.set(x, y, CY_DK2 if d > 5.0 else CY_DK)

# ================= HUMAN FACE =================
# --- ear ---
hln(21, 14, 16, SK_MD)
hln(22, 13, 16, SK)
hln(23, 13, 15, SK_HI2)
hln(24, 13, 15, SK_MD)
hln(25, 14, 16, SK_SH)
hln(26, 14, 16, SK_MD)
c.set(14, 23, SK_SH)
c.set(14, 24, SK_DK)
c.set(15, 24, SK_SH)

# --- eyebrow (bushy white) ---
hln(14, 22, 27, HAIR_MD)
hln(15, 20, 28, HAIR)
hln(16, 20, 28, HAIR_MD)
hln(15, 21, 24, HAIR_HI)
c.set(19, 16, HAIR_SH)
c.set(28, 16, HAIR_SH)
hln(13, 21, 27, SK_MD)
hln(14, 20, 21, SK_MD)

# --- eye ---
hln(17, 20, 27, SK_SH)
hln(18, 20, 28, SK_DK)
hln(19, 22, 25, EYE_W)
hln(20, 21, 26, EYE_W)
hln(21, 21, 26, EYE_W)
hln(22, 22, 25, EYE_W)
c.set(23, 20, IRIS)
c.set(24, 20, IRIS)
c.set(23, 21, IRIS)
c.set(24, 21, PUPIL)
hln(23, 21, 27, SK_SH)
hln(24, 20, 27, SK_MD)
hln(25, 20, 27, SK_SH)
hln(26, 21, 26, SK_MD)

# --- nose ---
hln(19, 30, 31, SK_MD)
hln(20, 30, 31, SK_MD)
hln(21, 29, 31, SK_MD)
hln(22, 29, 30, SK_MD)
hln(23, 29, 30, SK_MD)
hln(24, 28, 30, SK_MD)
hln(25, 27, 31, SK_HI2)
hln(26, 26, 31, SK_HI2)
hln(27, 27, 31, SK_MD)
c.set(27, 27, SK_DK)
c.set(28, 27, SK_DK)
hln(28, 28, 30, SK_SH)
hln(29, 28, 31, SK_MD)
hln(23, 28, 29, SK_HI2)
hln(24, 28, 29, SK_HI2)

# ================= MOUTH (maniacal grin) =================
M_TOP = {23: 30, 24: 30, 25: 30, 26: 30, 27: 30, 28: 30, 29: 30, 30: 30,
         31: 30, 32: 30, 33: 29, 34: 29, 35: 29, 36: 29, 37: 28, 38: 28,
         39: 28, 40: 28}
M_BOT = {23: 30, 24: 31, 25: 33, 26: 33, 27: 33, 28: 33, 29: 33, 30: 33,
         31: 33, 32: 33, 33: 33, 34: 33, 35: 33, 36: 32, 37: 31, 38: 30,
         39: 29, 40: 28}
for x in sorted(M_TOP):
    ty, by = M_TOP[x], M_BOT[x]
    for y in range(ty, by + 1):
        c.set(x, y, MOUTH)
    if x % 3 != 0:
        c.set(x, ty, TOOTH)
    if by > ty and (x + 1) % 3 != 0:
        c.set(x, by, TOOTH_D)
c.set(23, 30, MOUTH2)
c.set(24, 30, MOUTH2)
c.set(40, 28, MOUTH2)
c.set(39, 28, MOUTH2)
# lips & folds
for x in range(23, 32):
    c.set(x, M_TOP[x] - 1, SK_SH)
for x in range(24, 32):
    c.set(x, M_BOT[x] + 1, SK_SH)
c.line(22, 29, 24, 31, SK_MD)
c.set(21, 30, SK_SH)
c.set(25, 34, SK_SH)
c.set(26, 34, SK_SH)
# metal lip line on the robot side
for x in range(36, 41):
    c.set(x, M_TOP[x] - 1, M_SH)
    c.set(x, M_BOT[x] + 1, M_MD)

# --- chin / jaw ---
hln(34, 26, 31, SK_SH)
hln(34, 27, 29, SK_MD)
hln(35, 28, 31, SK_MD)
hln(35, 32, 35, M_SH)
hln(36, 29, 30, SK)
hln(36, 31, 31, SK_SH)
hln(37, 30, 31, SK_DK)
c.set(26, 34, SK_SH)
c.set(27, 35, SK_SH)
c.set(35, 33, M_SH)
c.set(34, 34, M_SH)
# smirk crease climbing from the right mouth corner
c.set(41, 27, M_MD)
c.set(42, 26, M_SH)
c.set(43, 25, M_DK)

# ================= ROBOT EYE =================
for y in range(19, 24):
    hln(y, 34, 46, M_DK)
hln(18, 35, 46, M_DK2)
hln(24, 35, 46, M_DK2)
hln(17, 35, 46, M_SH)
hln(25, 35, 46, M_SH)
hln(18, 36, 45, M_DK)
hln(24, 36, 45, M_DK)
hln(19, 38, 42, CY_DK2)
hln(20, 37, 43, CY_DK)
hln(21, 37, 44, CY_MD)
hln(22, 38, 43, CY_DK)
hln(23, 39, 42, CY_DK2)
hln(20, 39, 42, CY)
hln(21, 38, 43, CY)
c.set(40, 21, CY_HI)
c.set(41, 21, CY_HI)
c.set(40, 20, CY_HI)
c.set(41, 20, CY)
c.set(39, 22, CY_DK)
hln(16, 35, 46, M)
c.set(36, 16, M_HI)
c.set(37, 16, M_HI)
# audio sensor on the side
c.circle(45, 27, 2, M_SH)
c.circle(45, 27, 1, M_MD)
c.set(45, 27, CY_DK)
c.set(44, 26, M_HI)
# cable running from the sensor to the shoulder
c.path("M47 28 Q55 31 57 41", M_DK, fill=False)
c.path("M47 29 Q54 32 56 41", M_SH, fill=False)
c.set(50, 30, CY_DK2)
c.set(53, 33, CY_DK)
c.set(47, 27, M_MD)

# ================= HAIR =================
HAIR_MASS = {6: (20, 44), 7: (18, 45), 8: (16, 46), 9: (15, 46), 10: (15, 45),
             11: (15, 43), 12: (14, 38), 13: (14, 30), 14: (13, 18),
             15: (13, 17), 16: (12, 16), 17: (12, 16), 18: (13, 16),
             19: (14, 16)}
SPIKES = [[(16, 8), (19, 2), (23, 7)], [(22, 7), (26, 0), (30, 7)],
          [(29, 7), (33, 1), (37, 7)], [(36, 7), (40, 0), (44, 7)],
          [(43, 7), (46, 3), (49, 9)], [(12, 10), (14, 4), (18, 9)]]


def draw_hair(sc, ink):
    for y in HAIR_MASS:
        a, b = HAIR_MASS[y]
        sc.rect(a, y, b - a + 1, 1, ink)
    for s in SPIKES:
        sc.poly(s, ink)


HP = mask_pixels(draw_hair)
ramp_hair = [HAIR_HI, HAIR, HAIR_MD, HAIR_SH, HAIR_DK]
for (x, y) in HP:
    t = 0.50 * (x - 12) / 40.0 + 0.55 * (y - 1) / 18.0
    c.set(x, y, ramp_hair[quant(t, 5, x, y, 0.55)])

# hair strands
c.line(17, 7, 14, 18, HAIR_MD)
c.line(16, 8, 13, 17, HAIR_SH)
c.line(21, 5, 19, 12, HAIR_SH)
c.line(25, 3, 23, 11, HAIR_MD)
c.line(30, 2, 29, 10, HAIR_SH)
c.line(34, 3, 36, 10, HAIR_DK)
c.line(38, 3, 41, 10, HAIR_DK)
c.line(43, 5, 45, 11, HAIR_DK)
c.line(24, 1, 24, 6, HAIR_HI)
c.line(31, 1, 31, 5, HAIR_HI)
c.line(39, 1, 39, 5, HAIR_HI)
c.line(45, 2, 45, 6, HAIR_MD)
c.line(23, 8, 20, 13, HAIR_DK)
c.line(28, 6, 26, 12, HAIR_DK)
c.line(32, 5, 33, 11, HAIR_SH)
c.line(36, 7, 38, 12, HAIR_DK)
c.line(41, 6, 43, 11, HAIR_SH)
c.line(19, 9, 17, 15, HAIR_DK)
c.line(26, 8, 24, 12, HAIR_SH)
hln(13, 14, 16, HAIR_HI)
hln(14, 14, 17, HAIR)
c.set(15, 15, HAIR_HI)
# shadow of the hair on forehead
hln(14, 19, 28, SK_MD)
c.set(29, 14, SK)
c.set(30, 14, SK)
hln(13, 32, 40, M_SH)
hln(12, 39, 43, M_MD)

# ================= ELECTRODE PLUGS + WIRES =================
c.path("M24 5 Q19 0 14 0", M_SH, fill=False)
c.path("M25 6 Q21 1 17 1", M_MD, fill=False)
c.path("M32 2 Q31 0 34 0", M_SH, fill=False)
c.path("M43 8 Q47 3 52 2", M_SH, fill=False)
c.path("M43 9 Q47 4 51 3", M_MD, fill=False)
c.path("M45 16 Q48 22 45 28", M_DK, fill=False)
c.path("M44 21 Q47 25 45 28", CY_DK2, fill=False)
c.path("M46 2 Q52 4 56 9", M_DK, fill=False)
c.set(17, 0, M_MD)
c.set(51, 2, M_MD)
c.set(55, 8, M_SH)

for (px, py) in [(24, 7), (32, 4), (43, 10)]:
    c.circle(px, py, 2, M_SH)
    c.circle(px, py, 1, M)
    c.set(px - 1, py - 1, M_HI)
    c.set(px, py, CY_MD)
    c.set(px + 1, py + 1, M_MD)

# ================= ROBOTIC ARM =================
ARM = {47: (53, 62), 48: (52, 62), 49: (52, 63), 50: (52, 63), 51: (52, 63),
       52: (52, 63), 53: (52, 63), 54: (52, 63), 55: (53, 63), 56: (54, 63),
       57: (54, 63), 58: (54, 63), 59: (54, 63), 60: (53, 63), 61: (53, 63),
       62: (53, 63), 63: (52, 63)}
PALM = {38: (52, 60), 39: (51, 61), 40: (50, 62), 41: (50, 62), 42: (50, 62),
        43: (51, 62), 44: (52, 62), 45: (53, 62), 46: (53, 62)}
FINGERS = {34: [(50, 51), (53, 54), (56, 57), (59, 60)],
           35: [(50, 51), (53, 54), (56, 57), (59, 60)],
           36: [(50, 51), (53, 54), (56, 57), (59, 60)],
           37: [(50, 51), (53, 54), (56, 57), (59, 60)]}
ramp_arm = [M_HI, M, M_MD, M_SH, M_DK]

for y in sorted(ARM):
    cyl(y, ARM[y][0], ARM[y][1], ramp_arm, 0.30)
for y in sorted(PALM):
    cyl(y, PALM[y][0], PALM[y][1], ramp_arm, 0.30)
c.rect(53, 33, 2, 1, M_MD)
c.rect(50, 34, 2, 1, M_MD)
c.rect(56, 34, 2, 1, M_MD)
c.rect(59, 35, 2, 1, M_SH)
for y in sorted(FINGERS):
    for (a, b) in FINGERS[y]:
        for x in range(a, b + 1):
            if y == 34 and a == 56:
                c.set(x, y, M_MD)
            else:
                c.set(x, y, M_HI if x == a else (M if x == b else M_MD))
for (a, b) in [(50, 51), (53, 54), (56, 57), (59, 60)]:
    c.set(a, 36, M_DK)
    c.set(b, 36, M_SH)
# thumb
hln(42, 46, 49, M_MD)
hln(43, 46, 49, M)
hln(44, 47, 49, M_MD)
c.set(46, 42, M_HI)
c.set(46, 43, M_HI)
# wrist joint
hln(46, 52, 62, M_DK)
hln(47, 53, 62, M_MD)
# elbow joint
c.circle(57, 55, 3, M_MD)
c.circle(57, 55, 2, M_SH)
c.set(56, 54, M_HI)
c.set(57, 55, M_DK)
c.set(58, 55, CY_DK)
c.set(56, 56, M_DK)
# cyan rim
for y in range(48, 64):
    if y % 3:
        c.set(ARM[y][1], y, CY_DK)
for y in range(39, 47):
    c.set(PALM[y][1], y, CY_DK)
# forearm plate seam
c.line(58, 48, 58, 63, M_DK)
c.line(59, 48, 59, 63, M_MD)
for y in range(49, 63, 4):
    c.set(57, y, M_HI)

# cables from the prosthetic hand
c.path("M50 44 Q44 49 45 55 Q46 60 42 63", WIRE, fill=False)
c.path("M51 45 Q46 50 47 55", WIRE_HI, fill=False)
c.path("M53 46 Q48 52 51 57 Q53 61 50 63", M_DK, fill=False)
c.set(49, 43, M_MD)
c.set(48, 43, M)
c.set(47, 45, CY_DK2)

# ================= FINAL TOUCHES =================
c.line(17, 44, 24, 49, CO_SH)
c.line(16, 45, 22, 50, CO_DK)
for (x, y) in [(9, 47), (10, 47), (11, 48), (8, 49), (12, 49), (52, 54),
               (53, 54), (54, 55), (51, 56)]:
    c.set(x, y, DIRT2)
c.set(10, 48, DIRT)
c.set(13, 50, DIRT)
hln(45, 15, 20, CO_HI)
hln(46, 12, 17, CO_HI)
c.set(14, 45, '#ffffff')
c.set(15, 46, '#ffffff')

save("mad_cyborg_scientist", c)
print(c.stats_text())

PAL = {p['index']: p['rgba'] for p in c.palette()}
LUM = {}
for k, v in PAL.items():
    LUM[k] = 0.299 * v[0] + 0.587 * v[1] + 0.114 * v[2]


def lumap(x0, y0, x1, y1):
    chars = " .:-=+*#%@"
    print("    " + "".join(str((x // 10) % 10) for x in range(x0, x1 + 1)))
    print("    " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            v = LUM.get(c.get(x, y), 0)
            i = int(v / 25.6)
            row += chars[max(0, min(9, i))]
        print("%3d %s" % (y, row))


lumap(0, 0, 63, 63)

CATS = {}


def _cat(letter, cols):
    for hx in cols:
        CATS[c.color(hx)] = letter


_cat('.', [BG0, BG1, BG2, BG3, DIRT, DIRT2, '#3d2f24'])
_cat('H', [HAIR_HI, HAIR, HAIR_MD, HAIR_SH, HAIR_DK])
_cat('S', [SK_HI, SK_HI2, SK, SK_MD, SK_SH, SK_DK, SK_DK2])
_cat('E', [EYE_W, IRIS, PUPIL])
_cat('M', [M_HI, M, M_MD, M_SH, M_DK, M_DK2])
_cat('C', [CY_HI, CY, CY_MD, CY_DK, CY_DK2])
_cat('W', [CO_HI, CO, CO_MD, CO_SH, CO_DK])
_cat('L', [LE_HI, LE, LE_MD, LE_DK, BELT, BRASS, BRASS_HI])
_cat('T', [MOUTH, MOUTH2, TOOTH, TOOTH_D])
_cat('R', [WIRE, WIRE_HI])


def dump(x0, y0, x1, y1):
    print("    " + "".join(str((x // 10) % 10) for x in range(x0, x1 + 1)))
    print("    " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        print("%3d " % y + "".join(CATS.get(c.get(x, y), '?') for x in range(x0, x1 + 1)))


dump(15, 11, 48, 38)
finish(c)
