try:
    new_canvas
except NameError:
    from pixelbench_api import *

W = H = 64

# ---------------- palette ----------------
OUT = '#241a2e'
SKIN = '#f6cfa8'; SKIN_SH = '#dca47c'
HAIR_L = '#b9e86e'; HAIR_M = '#8cc94a'; HAIR_D = '#5a9431'
CLOTH_L = '#d6f0cf'; CLOTH_M = '#a8dca4'; CLOTH_D = '#79b87c'; CLOTH_DD = '#548f5c'
LEATH = '#8a5a30'; LEATH_D = '#5c3a1c'; GOLD = '#e6c35c'; GOLD_D = '#b08a34'
WHITE = '#f4f4f0'; IRIS = '#3e8f4a'; LIPS = '#d4788a'
BG1 = '#1d2937'; BG2 = '#2b4148'; GLOW = '#3a5a55'; BG3 = '#35524f'; SHAD = '#141d26'
ARROW = '#d8b46a'; FLETCH = '#d95f5f'; FLETCH2 = '#efe6cf'


def hline(c, y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)


def vline(c, x, y0, y1, col):
    for y in range(y0, y1 + 1):
        c.set(x, y, col)


def rows(c, table, col):
    for y, (x0, x1) in table.items():
        hline(c, y, x0, x1, col)


def line_pixels(x0, y0, x1, y1):
    pts = []
    dx = abs(x1 - x0); dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        pts.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy; x0 += sx
        if e2 < dx:
            err += dx; y0 += sy
    return pts


# ================= BACKGROUND =================
bg = new_canvas(W, H, name='bg')
bg.rect(0, 0, W, H, BG1)
bg.ellipse(32, 33, 25, 28, GLOW)
bg.ellipse(32, 33, 19, 22, BG2)
bg.ellipse(32, 33, 13, 16, BG3)
bg.ellipse(31, 60, 13, 3, SHAD)
for x, y in line_pixels(7, 43, 55, 5):            # bow string, behind everything
    bg.set(x, y, FLETCH2)
for sx, sy, col in [(9, 14, GOLD), (58, 17, HAIR_L), (13, 50, HAIR_L), (58, 45, GOLD),
                    (48, 58, HAIR_L), (11, 4, GOLD), (4, 28, HAIR_L), (6, 55, HAIR_L),
                    (60, 22, GOLD), (60, 33, HAIR_L)]:
    bg.set(sx, sy, col); bg.set(sx - 1, sy, col); bg.set(sx + 1, sy, col)
    bg.set(sx, sy - 1, col); bg.set(sx, sy + 1, col)

# ================= BOW (own layer: behind the figure) =================
bow = new_canvas(W, H, name='bow')
bow.path("M 7 43 Q 34 12 55 5 Q 33 17 7 43 Z", LEATH)
bow.rect(53, 4, 3, 2, GOLD)
bow.rect(6, 42, 3, 2, GOLD)

# ================= FIGURE =================
fig = new_canvas(W, H, name='fig')

# ---- 1. arrows ----
ARROWS = [(40, 13, FLETCH), (42, 10, FLETCH2), (45, 14, FLETCH)]


def draw_arrows(c, deep):
    for ax, top, fcol in ARROWS:
        bot = 22 if deep else 24
        vline(c, ax, top + 3, bot, ARROW)
        hline(c, top, ax - 1, ax, fcol)
        hline(c, top + 1, ax - 1, ax, fcol)
        c.set(ax, top + 2, fcol)


draw_arrows(fig, deep=False)

# ---- 2. quiver ----
QV = {}
for y in range(23, 37):
    QV[y] = (39, 45)
QV[37] = (40, 44)
rows(fig, QV, LEATH)
for y, (x0, x1) in QV.items():
    fig.set(x1, y, LEATH_D)
hline(fig, 23, 39, 45, LEATH_D)
hline(fig, 28, 39, 45, GOLD)
hline(fig, 29, 39, 45, GOLD_D)

# ---- 3. back hair mass ----
HB = {}
HB[5] = (26, 33); HB[6] = (24, 35); HB[7] = (23, 36); HB[8] = (22, 37); HB[9] = (21, 38)
for y in range(10, 17):
    HB[y] = (20, 38)
for y in range(17, 23):
    HB[y] = (20, 39)
for y in range(23, 40):
    HB[y] = (19, 39)
HB[40] = (19, 38); HB[41] = (20, 38); HB[42] = (20, 37); HB[43] = (21, 37); HB[44] = (22, 36)
rows(fig, HB, HAIR_M)
for y, (x0, x1) in HB.items():
    fig.set(x0, y, HAIR_D)
    fig.set(x1, y, HAIR_D)
for x, y0, y1, col in [(23, 8, 20, HAIR_L), (27, 6, 18, HAIR_L), (31, 6, 16, HAIR_L),
                       (34, 9, 26, HAIR_L), (37, 12, 30, HAIR_L), (25, 7, 22, HAIR_D),
                       (29, 6, 20, HAIR_D), (33, 8, 24, HAIR_D), (36, 11, 30, HAIR_D),
                       (38, 14, 34, HAIR_D)]:
    vline(fig, x, y0, y1, col)

# ---- 4. neck + face ----
fig.rect(27, 22, 3, 3, SKIN)
for x in range(27, 30):
    fig.set(x, 22, SKIN_SH)
FACE = {
    10: (24, 31), 11: (23, 32), 12: (22, 32), 13: (22, 32), 14: (22, 32),
    15: (22, 32), 16: (23, 32), 17: (24, 32), 18: (24, 31), 19: (25, 31),
    20: (26, 30), 21: (27, 29),
}
rows(fig, FACE, SKIN)
for y, (x0, x1) in FACE.items():
    fig.set(x1, y, SKIN_SH)
    if x1 - 1 > x0 + 2:
        fig.set(x1 - 1, y, SKIN_SH)

# ---- 5. torso ----
TOR = {
    23: (25, 32), 24: (23, 34), 25: (22, 35), 26: (22, 35), 27: (21, 36),
    28: (21, 36), 29: (21, 36), 30: (21, 36), 31: (22, 35), 32: (22, 35),
    33: (22, 35), 34: (23, 34), 35: (23, 34), 36: (23, 34), 37: (24, 33),
}
rows(fig, TOR, CLOTH_M)
for y, (x0, x1) in TOR.items():
    fig.set(x0, y, CLOTH_L)
    fig.set(x1, y, CLOTH_D)
for y in (23, 24):
    hline(fig, y, 27, 29, SKIN)                  # open collar
hline(fig, 25, 25, 31, CLOTH_D)

# ---- 6. skirt ----
SK = {}
SK[38] = (21, 36); SK[39] = (21, 37); SK[40] = (20, 37)
for y in range(41, 44):
    SK[y] = (20, 38)
for y in range(44, 48):
    SK[y] = (19, 38)
rows(fig, SK, CLOTH_M)
for y, (x0, x1) in SK.items():
    fig.set(x0, y, CLOTH_L)
    fig.set(x1, y, CLOTH_D)
vline(fig, 26, 39, 46, CLOTH_D)
vline(fig, 31, 39, 46, CLOTH_D)
vline(fig, 35, 41, 46, CLOTH_D)
hline(fig, 47, 19, 38, CLOTH_DD)

# ---- 7. quiver strap (under the belt) ----
fig.line(35, 26, 25, 37, LEATH_D)
fig.line(35, 27, 26, 37, LEATH_D)

# ---- 8. belt ----
hline(fig, 36, 23, 34, LEATH_D)
hline(fig, 37, 24, 33, LEATH_D)
fig.rect(27, 36, 3, 2, GOLD)
fig.set(28, 37, GOLD_D)

# ---- 9. legs ----
for y in range(48, 55):
    hline(fig, y, 24, 27, SKIN); fig.set(27, y, SKIN_SH)
for y in range(48, 54):
    hline(fig, y, 31, 34, SKIN); fig.set(34, y, SKIN_SH)

# ---- 10. boots ----
BL = {}
for y in range(55, 61):
    BL[y] = (24, 29)
BL[61] = (24, 29); BL[62] = (25, 29)
BR = {}
for y in range(54, 60):
    BR[y] = (31, 36)
BR[60] = (31, 35); BR[61] = (31, 35); BR[62] = (32, 35)
rows(fig, BL, LEATH); rows(fig, BR, LEATH)
for tb in (BL, BR):
    for y, (x0, x1) in tb.items():
        fig.set(x1, y, LEATH_D)
hline(fig, 61, 31, 35, LEATH_D)
hline(fig, 62, 25, 29, LEATH_D)
hline(fig, 62, 32, 35, LEATH_D)

# ---- 11. near arm ----
LA = {25: (22, 25), 26: (21, 24), 27: (21, 24), 28: (20, 24), 29: (20, 23),
      30: (20, 23), 31: (20, 23), 32: (20, 23), 33: (20, 23), 34: (20, 22)}
rows(fig, LA, CLOTH_M)
for y, (x0, x1) in LA.items():
    fig.set(x0, y, CLOTH_L)
    fig.set(x1, y, CLOTH_D)
for y in range(35, 40):
    hline(fig, y, 20, 22, SKIN); fig.set(22, y, SKIN_SH)
hline(fig, 40, 19, 22, SKIN); hline(fig, 41, 19, 22, SKIN); hline(fig, 42, 20, 22, SKIN)
for y in (40, 41, 42):
    fig.set(22, y, SKIN_SH)

# ---- 12. pointed ears ----
FAR_EAR = {8: (17, 19), 9: (16, 19), 10: (16, 20), 11: (17, 21),
           12: (18, 21), 13: (19, 22), 14: (20, 22), 15: (21, 22)}
NEAR_EAR = {5: (36, 37), 6: (35, 38), 7: (35, 38), 8: (34, 38), 9: (34, 38),
            10: (33, 37), 11: (33, 37), 12: (33, 36), 13: (33, 36), 14: (33, 35),
            15: (33, 35), 16: (33, 34), 17: (33, 34), 18: (33, 34)}
rows(fig, FAR_EAR, SKIN)
rows(fig, NEAR_EAR, SKIN)

# ---- 13. side-swept fringe ----
FRINGE = {22: 13, 23: 12, 24: 11, 25: 10, 26: 10, 27: 10, 28: 10, 29: 10, 30: 10,
          31: 10, 32: 10}
for x, ymax in FRINGE.items():
    vline(fig, x, 10, ymax, HAIR_M)
    fig.set(x, ymax, HAIR_D)

# ---- 14. long hair strands ----
LS = {}
for y in range(16, 23):
    LS[y] = (17, 21)
for y in range(23, 33):
    LS[y] = (17, 20)
for y in range(33, 52):
    LS[y] = (17, 19)
rows(fig, LS, HAIR_M)
for y, (x0, x1) in LS.items():
    fig.set(x1, y, HAIR_D)
    if x1 - x0 > 1:
        fig.set(x0 + 1, y, HAIR_L)
RS2 = {}
for y in range(24, 41):
    RS2[y] = (36, 38)
for y in range(41, 47):
    RS2[y] = (36, 37)
for y in range(47, 52):
    RS2[y] = (37, 37)
rows(fig, RS2, HAIR_M)
for y, (x0, x1) in RS2.items():
    fig.set(x0, y, HAIR_L)
    fig.set(x1, y, HAIR_D)

# ---- 15. face features (3/4: shifted to the near side) ----
for x in (25, 26, 30, 31):
    fig.set(x, 13, HAIR_D)                       # brows
for x in (25, 26, 30, 31):
    fig.set(x, 14, OUT)                          # lash lines
fig.set(24, 14, OUT); fig.set(32, 14, OUT)       # flicks
fig.set(25, 15, IRIS); fig.set(26, 15, WHITE)
fig.set(30, 15, IRIS); fig.set(31, 15, WHITE)
fig.set(28, 17, SKIN_SH)                         # nose
fig.set(27, 19, LIPS); fig.set(28, 19, LIPS)     # lips

# ---- 16. outline ----
fig.outline(OUT)

# ---- 17. details that must survive the outline ----
draw_arrows(fig, deep=True)
for ear in (NEAR_EAR, FAR_EAR):
    for y, (x0, x1) in ear.items():
        for x in range(x0 + 1, x1):
            fig.set(x, y, SKIN)
for x, y in [(34, 12), (34, 13), (34, 14), (34, 15)]:
    fig.set(x, y, SKIN_SH)                       # near-ear concha
for x, y in [(19, 11), (19, 12), (20, 13)]:
    fig.set(x, y, SKIN_SH)                       # far-ear concha

# hair shine + cheek blush (painted inside the outline, so both survive)
for x, y in [(27, 6), (28, 6), (29, 6), (30, 6), (31, 6),
             (37, 27), (37, 31), (37, 35)]:
    fig.set(x, y, HAIR_L)
fig.set(31, 17, SKIN_SH); fig.set(32, 17, SKIN_SH)

# ================= COMPOSITE =================
result = flatten([bg, bow, fig], name='result')

# ================= DEBUG =================
FAMS = {
    'HAIR': [HAIR_L, HAIR_M, HAIR_D],
    'SKIN': [SKIN, SKIN_SH],
    'CLOTH': [CLOTH_L, CLOTH_M, CLOTH_D, CLOTH_DD],
    'LEATH': [LEATH, LEATH_D],
    'GOLD': [GOLD, GOLD_D],
    'OUT': [OUT],
    'EYE': [IRIS, WHITE],
    'MISC': [ARROW, FLETCH, FLETCH2, LIPS],
    'BG': [BG1, BG2, GLOW, BG3, SHAD],
}
FAMOF = {}
for _f, _hs in FAMS.items():
    for _h in _hs:
        FAMOF[_h] = _f
SHORT = {'HAIR': 'H', 'SKIN': 'S', 'CLOTH': 'C', 'LEATH': 'L', 'GOLD': 'G',
         'OUT': 'O', 'EYE': 'E', 'MISC': 'M', 'BG': '.'}


def rle(c, x0, x1, y0, y1, label=''):
    print(f'--- rle {label} x{x0}-{x1} ---')
    for y in range(y0, y1 + 1):
        runs = []
        prev = None
        start = x0
        for x in range(x0, x1 + 1):
            i = c.get(x, y)
            fam = '.' if i == 0 else SHORT.get(FAMOF.get(c.color_name(i)[:7], '?'), '?')
            if fam != prev:
                if prev is not None:
                    runs.append(f'{prev}{start}-{x - 1}')
                prev = fam
                start = x
        runs.append(f'{prev}{start}-{x1}')
        print(f'{y:2d}: ' + ' '.join(runs))


rle(result, 12, 48, 4, 24, 'head')
rle(result, 14, 44, 44, 63, 'lower')


def probe(c, pts):
    for label, x, y in pts:
        i = c.get(x, y)
        print(f'  {label:12s} ({x:2d},{y:2d}) {c.color_name(i)}')


probe(result, [
    ('L iris', 25, 15), ('L glint', 26, 15), ('R iris', 30, 15), ('R glint', 31, 15),
    ('lips', 27, 19), ('nose', 28, 17), ('chin', 28, 21),
    ('earF tip', 18, 8), ('earF mid', 18, 11), ('earF base', 21, 14),
    ('earN tip', 36, 5), ('earN mid', 36, 9), ('earN base', 34, 16),
    ('cap up', 54, 4), ('cap low', 7, 42), ('bow up', 47, 9), ('bow lo', 11, 39),
    ('quiver', 42, 32), ('band', 42, 28), ('shaft', 42, 20), ('fletch', 42, 11),
    ('belt', 28, 36), ('buckle', 28, 37), ('bootL', 26, 58), ('bootR', 33, 58),
    ('legL', 26, 50), ('skirt', 28, 44), ('handL', 20, 41), ('collar', 28, 25),
    ('strap', 30, 32), ('boot btm', 26, 62),
])
print(result.stats_text())
finish(result)
