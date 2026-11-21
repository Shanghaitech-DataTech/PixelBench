import math

# ---------------------------------------------------------------- palette
OUT      = '#241a13'   # dark outline
T_MID    = '#a76f3d'   # table wood body
T_LIGHT  = '#cb9760'   # lit edge (top / left)
T_DARK   = '#7a4a26'   # shaded edge (bottom / right)
T_SEAM   = '#8a5430'   # plank seams
T_GRAIN  = '#bb8244'   # light grain flecks
T_SHADOW = '#8d5d32'   # bowl drop shadow on the table

CH_DARK  = '#6b3d1f'
CH_MID   = '#9c6233'
CH_LIGHT = '#bd8450'

CU_LIGHT = '#7fae9f'   # cushion highlight
CU_MID   = '#56877b'   # cushion (soft teal)
CU_DARK  = '#3d665c'   # cushion shadow

B_LIGHT  = '#f0eadd'   # ceramic rim
B_SHEEN  = '#fdfbf4'   # ceramic shine
B_MID    = '#cfc6b2'   # bowl floor
B_DARK   = '#a2967f'   # inner wall in shadow

APPLE    = '#cf3d38'; APPLE_L  = '#ea7563'
ORANGE   = '#f0912c'; ORANGE_L = '#f9b85e'
LIME     = '#8cb84a'; LIME_L   = '#b3d272'
GRAPE    = '#7b4d94'; GRAPE_L  = '#a276b8'
LEMON    = '#f2cd3e'; LEMON_L  = '#f8e076'

c = new_canvas(64, 64, name='dining-table')

# ---------------------------------------------------------------- helpers
def chamfer_spans(x0, y0, x1, y1, ch):
    spans = []
    for y in range(y0, y1 + 1):
        d = min(y - y0, y1 - y)
        inset = max(0, ch - d)
        spans.append((y, x0 + inset, x1 - inset))
    return spans

def fill_spans(cv, spans, colour):
    for y, a, b in spans:
        cv.rect(a, y, b - a + 1, 1, colour)

def disc(cv, cx, cy, r, colour, grow=0.5):
    R = r + grow
    for dy in range(-r, r + 1):
        w = int(round(math.sqrt(max(0.0, R * R - dy * dy))))
        w = min(w, r)
        cv.rect(cx - w, cy + dy, 2 * w + 1, 1, colour)

FRUIT = [(-1, -2, 1), (-2, -1, 2), (-2, 0, 2), (-2, 1, 2), (-1, 2, 1)]

def berry(cv, cx, cy, colour, shine=None, hi=None):
    for dx0, dy, dx1 in FRUIT:
        cv.rect(cx + dx0, cy + dy, dx1 - dx0 + 1, 1, colour)
    if shine:
        cv.set(cx - 1, cy - 1, shine)

COLMAP = {'#': OUT, 'w': CH_DARK, 'm': CH_MID, 'l': CH_LIGHT,
          'C': CU_LIGHT, 'c': CU_MID, 's': CU_DARK}

CHAIR = [
    "..#########..",
    "..#lllllll#..",
    "..#mmmmmmm#..",
    "..#wwwwwww#..",
    ".###########.",
    ".#mCCCCCCCm#.",
    ".#mcccccccm#.",
    ".#mcccccccm#.",
    ".#mcccccccm#.",
    ".#msssssssm#.",
    ".#mmmmmmmmm#.",
    ".###########.",
    ".............",
]

def draw_chair(cv, ox, oy, orient):
    for ly, row in enumerate(CHAIR):
        for lx, ch in enumerate(row):
            if ch == '.':
                continue
            if orient == 'N':
                x, y = ox + lx, oy + ly
            elif orient == 'S':
                x, y = ox + lx, oy + 12 - ly
            elif orient == 'W':
                x, y = ox + ly, oy + lx
            else:  # 'E'
                x, y = ox + 12 - ly, oy + lx
            cv.set(x, y, COLMAP[ch])

# ---------------------------------------------------------------- table top
OUTER = chamfer_spans(16, 16, 48, 48, 3)
INNER = chamfer_spans(17, 17, 47, 47, 2)
fill_spans(c, OUTER, OUT)
fill_spans(c, INNER, T_MID)

# bevel: lit on top / left, shaded on bottom / right
for y, a, b in INNER:
    if y == 17:
        c.line(a, y, b, y, T_LIGHT)
    elif y == 47:
        c.line(a, y, b, y, T_DARK)
    else:
        c.set(a, y, T_LIGHT)
        c.set(b, y, T_DARK)

# ----- plank seams & grain
c.line(18, 21, 46, 21, T_SEAM)
c.line(18, 43, 46, 43, T_SEAM)
c.line(20, 19, 27, 19, T_SEAM)
c.line(35, 19, 44, 19, T_GRAIN)
c.line(20, 45, 28, 45, T_SEAM)
c.line(36, 45, 44, 45, T_GRAIN)
c.line(18, 26, 21, 26, T_GRAIN)
c.line(18, 32, 20, 32, T_SEAM)
c.line(19, 38, 21, 38, T_GRAIN)
c.line(43, 27, 46, 27, T_SEAM)
c.line(44, 34, 46, 34, T_GRAIN)
c.line(43, 40, 46, 40, T_SEAM)

# ---------------------------------------------------------------- chairs
draw_chair(c, 26, 1, 'N')
draw_chair(c, 26, 51, 'S')
draw_chair(c, 1, 26, 'W')
draw_chair(c, 51, 26, 'E')

# ---------------------------------------------------------------- fruit bowl
disc(c, 33, 34, 10, T_SHADOW)       # shadow cast on the wood
disc(c, 32, 32, 10, OUT)            # dark rim outline
disc(c, 32, 32, 9, B_LIGHT)         # ceramic rim disc
disc(c, 32, 32, 8, B_DARK)          # inner wall in shadow
disc(c, 32, 32, 7, B_MID)           # bowl floor
# ceramic shine on the upper-left rim
for px, py in ((29, 23), (30, 23), (28, 24)):
    c.set(px, py, B_SHEEN)

# fruit
berry(c, 29, 29, APPLE, APPLE_L)
berry(c, 35, 29, ORANGE, ORANGE_L)
berry(c, 29, 35, LIME, LIME_L)
berry(c, 35, 35, GRAPE, GRAPE_L)
# centre lemon (plus / diamond shape fills the gap)
c.set(32, 31, LEMON)
c.rect(31, 32, 3, 1, LEMON)
c.set(32, 33, LEMON)
c.set(32, 32, LEMON_L)

print(c.stats_text())
print('colors used:', len(c.palette()))
print(c.matrix_text(region=(22, 20, 44, 46), indices=True))

save('dining-table', c)
finish(c)
