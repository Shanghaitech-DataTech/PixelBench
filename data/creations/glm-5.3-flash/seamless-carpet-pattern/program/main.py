# ============================================================
#  Seamless 32x32 carpet tile  (one repeat = the whole tile)
#
#  structure, periodic with period 32 in both directions:
#    * warm red twill field, woven
#    * gold guard squares framing each field cell
#    * cream woven channels between neighbouring guard squares
#    * a dark floral vine runs down the middle of every channel;
#      the channel is centred on the tile seam, so the vine is the
#      pair of lines rows/cols 0 and 31 and joins itself exactly
#    * diamond rosettes + gold beads threaded on the vine
#    * layered diamond medallion in the middle of each field
#
#  every motif is stamped through a wrapping pixel setter, so the
#  left/right and top/bottom edges connect exactly.
# ============================================================
W = H = 32

c = new_canvas(W, H, name='carpet_tile')

# ---------------- palette (warm) ----------------
CREAM  = c.color('#F2E4C4', 'cream')     # channel ground
CREAM2 = c.color('#E3D0A6', 'cream2')    # channel weave shadow
RED    = c.color('#A83A26', 'red')       # field
RED2   = c.color('#993020', 'red2')      # field weave shadow
DRED   = c.color('#7C2416', 'darkred')   # petals, medallion
GOLD   = c.color('#DCA23A', 'gold')      # guards, hearts, beads
BROWN  = c.color('#54331C', 'brown')     # vine, outlines
OLIVE  = c.color('#8C8439', 'olive')     # leaves
IVORY  = c.color('#FBF3DC', 'ivory')     # medallion band

def edist(x, y):
    return min(x, y, W - 1 - x, H - 1 - y)

def pset(x, y, col):
    """pixel setter that wraps around the tile edges"""
    c.set(x % W, y % H, col)

# ---------- 1. woven ground, gold guard ring, woven field ----------
for y in range(H):
    for x in range(W):
        d = edist(x, y)
        tw = ((x + y) % 4) < 2                     # 2 px diagonal twill
        if d == 4:
            col = GOLD                             # guard ring
        elif d >= 5:
            col = RED if tw else RED2              # woven field
        else:
            col = CREAM if tw else CREAM2          # woven channel
        c.set(x, y, col)

# ---------- 2. floral vine down the middle of every channel ----------
for i in range(W):
    pset(i, 0, BROWN);  pset(i, 31, BROWN)
    pset(0, i, BROWN);  pset(31, i, BROWN)

# ---------- 3. rosettes and beads on the vines ----------
def rosette(cx, cy):
    """4x4 diamond flower centred on a half-integer point of the vine"""
    n, m = int(cx), int(cy)
    for dx in (0, 1):
        for dy in (0, 1):
            pset(n + dx, m + dy, GOLD)                       # heart
    for dx, dy in ((-1, 0), (2, 0), (-1, 1), (2, 1),
                   (0, -1), (1, -1), (0, 2), (1, 2)):
        pset(n + dx, m + dy, DRED)                           # petals

def bead(cx, cy, horizontal):
    """gold bead on the vine, olive leaves flanking it across the vine"""
    n, m = int(cx), int(cy)
    for dx in (0, 1):
        for dy in (0, 1):
            pset(n + dx, m + dy, GOLD)
    if horizontal:                          # on a horizontal vine:
        for dx in (0, 1):                   # leaves above / below
            pset(n + dx, m - 1, OLIVE)
            pset(n + dx, m + 2, OLIVE)
    else:                                   # on a vertical vine:
        for dy in (0, 1):                   # leaves left / right
            pset(n - 1, m + dy, OLIVE)
            pset(n + 2, m + dy, OLIVE)

for t in (7, 15, 23, 31):                    # rosettes, period 8
    rosette(t + 0.5, 31.5)                   # on the horizontal vines
    rosette(31.5, t + 0.5)                   # on the vertical vines
for t in (3, 11, 19, 27):                    # beads between rosettes
    bead(t + 0.5, 31.5, True)                # horizontal vine
    bead(31.5, t + 0.5, False)               # vertical vine

# ---------- 4. central diamond medallion ----------
for y in range(9, 23):
    for x in range(9, 23):
        r = abs(x - 15.5) + abs(y - 15.5)
        if r > 7:
            continue
        if   r == 7: col = BROWN
        elif r == 6: col = GOLD
        elif r >= 4: col = IVORY
        elif r == 3: col = DRED
        elif r == 2: col = RED
        else:        col = GOLD
        c.set(x, y, col)

# dark points on the ivory band, N S E W
for px, py in ((15, 11), (16, 11), (15, 20), (16, 20),
               (11, 15), (11, 16), (20, 15), (20, 16)):
    c.set(px, py, DRED)

# ---------- 5. small gold accents in the field ----------
for ax, ay in ((7, 7), (23, 7), (7, 23), (23, 23),        # medallion corners
               (15, 6), (15, 24), (6, 15), (24, 15)):     # edge midpoints
    for dx in (0, 1):
        for dy in (0, 1):
            c.set(ax + dx, ay + dy, GOLD)

# ---------- seam checks ----------
def period_ok(vals, p):
    return all(vals[i] == vals[i % p] for i in range(len(vals)))

for label, vals in (('row 0',  [c.get(x, 0)  for x in range(W)]),
                    ('row 1',  [c.get(x, 1)  for x in range(W)]),
                    ('row 30', [c.get(x, 30) for x in range(W)]),
                    ('row 31', [c.get(x, 31) for x in range(W)]),
                    ('col 0',  [c.get(0, y)  for y in range(H)]),
                    ('col 1',  [c.get(1, y)  for y in range(H)]),
                    ('col 30', [c.get(30, y) for y in range(H)]),
                    ('col 31', [c.get(31, y) for y in range(H)])):
    print(f'{label}: period 8 = {period_ok(vals, 8)}')

# ---------- tiled seam inspection (diagnostic only, not submitted) ----------
tiled = new_canvas(96, 96, name='tiled_check')
for ty in range(3):
    for tx in range(3):
        tiled.blit(c, tx * 32, ty * 32)
print(tiled.stats_text())
print('--- seam crossing at (32,32) of the 3x3 tiling ---')
print(tiled.matrix_text(region=(24, 24, 40, 40)))
print('--- vertical seam strip, rows 4..27 ---')
print(tiled.matrix_text(region=(28, 4, 36, 27)))

print(c.stats_text())
print(c.matrix_text())

finish(c)
