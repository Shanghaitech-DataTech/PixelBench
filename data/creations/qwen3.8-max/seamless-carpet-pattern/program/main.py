try:
    from pixelbench_api import new_canvas, view, save, finish
except Exception:
    pass

N = 32
c = new_canvas(N, N, name="carpet")


def P(x, y, col):
    """Wrapped pixel set -> guarantees seamless tiling in both directions."""
    c.set(x % N, y % N, col)


# ---------------------------------------------------------------- palette ---
CREAM   = c.color('#F4E6C7', 'cream')
CREAM_D = c.color('#E0C79B', 'cream_d')
BEIGE   = c.color('#EBD6AC', 'beige')
BEIGE_D = c.color('#D2B585', 'beige_d')
DARK    = c.color('#3A2216', 'dark')
BROWN   = c.color('#5C3A20', 'brown')
MAROON  = c.color('#7C2A22', 'maroon')
RED     = c.color('#A83A2A', 'red')
TERRA   = c.color('#C4653A', 'terra')
GOLD    = c.color('#DFA63E', 'gold')
IVORY   = c.color('#F8EED8', 'ivory')
LEAF    = c.color('#6C7A38', 'leaf')

# ------------------------------------------------------- woven ground -------
# 2x2 basket weave: alternating "horizontal" and "vertical" thread blocks,
# each shaded across its own width.  Period 4 divides 32 -> seamless.
for y in range(N):
    for x in range(N):
        if (x // 2 + y // 2) % 2 == 0:
            col = CREAM if y % 2 == 0 else CREAM_D
        else:
            col = BEIGE if x % 2 == 0 else BEIGE_D
        P(x, y, col)

# faint warp speckle for pile texture (period 8, seamless)
for y in range(N):
    for x in range(N):
        if (x % 8 == 3 and y % 8 == 3) or (x % 8 == 7 and y % 8 == 7):
            P(x, y, BEIGE_D)

# ------------------------------------------------------- floral vine --------
# Voids of the diamond lattice lie on the lines x+y = 16 and x-y = 16 (mod 32).
def on_vine(x, y):
    return (x + y) % N == 16 or (x - y) % N == 16


def node_flower(cx, cy):
    """Big 4-petal bloom where two vines cross."""
    for sx in (1, -1):
        for sy in (1, -1):
            P(cx + 2 * sx, cy + 2 * sy, LEAF)
            P(cx + 3 * sx, cy + 3 * sy, LEAF)
            P(cx + sx, cy + sy, TERRA)
    for s in (1, -1):
        P(cx + s, cy, IVORY)
        P(cx, cy + s, IVORY)
        P(cx + 2 * s, cy, IVORY)
        P(cx, cy + 2 * s, IVORY)
        P(cx + 3 * s, cy, RED)
        P(cx, cy + 3 * s, RED)
    P(cx, cy, GOLD)


def bud(cx, cy, fam1):
    """Small bloom on the vine, halfway between two nodes."""
    dx, dy = (1, -1) if fam1 else (1, 1)      # along the vine
    px, py = (1, 1) if fam1 else (1, -1)      # across the vine
    P(cx + 2 * dx, cy + 2 * dy, RED)
    P(cx - 2 * dx, cy - 2 * dy, RED)
    P(cx + dx, cy + dy, IVORY)
    P(cx - dx, cy - dy, IVORY)
    P(cx + px, cy + py, LEAF)
    P(cx - px, cy - py, LEAF)
    P(cx, cy, GOLD)


def leafpair(cx, cy, fam1):
    px, py = (1, 1) if fam1 else (1, -1)
    P(cx + px, cy + py, LEAF)
    P(cx - px, cy - py, LEAF)
    P(cx, cy, GOLD)


for y in range(-6, N + 6):
    for x in range(-6, N + 6):
        fam1 = (x + y) % N == 16
        fam2 = (x - y) % N == 16
        if not (fam1 or fam2):
            continue
        mx, my = x % 16, y % 16
        if mx == 0 and my == 0:
            continue                      # drawn after the vine is laid
        elif mx == 8 and my == 8:
            continue
        elif (mx, my) in ((4, 12), (12, 4), (4, 4), (12, 12)):
            continue
        P(x, y, BROWN)

for y in range(-6, N + 6):
    for x in range(-6, N + 6):
        fam1 = (x + y) % N == 16
        fam2 = (x - y) % N == 16
        if not (fam1 or fam2):
            continue
        mx, my = x % 16, y % 16
        if mx == 0 and my == 0:
            node_flower(x, y)
        elif mx == 8 and my == 8:
            bud(x, y, fam1)
        elif (mx, my) in ((4, 12), (12, 4)):
            leafpair(x, y, True)
        elif (mx, my) in ((4, 4), (12, 12)):
            leafpair(x, y, False)

# --------------------------------------------------------- diamonds ---------
R = 11


def ring_col(d):
    if d > 11:  return None
    if d == 11: return DARK
    if d == 10: return MAROON
    if d == 9:  return GOLD
    if d == 8:  return RED
    if d == 7:  return RED
    if d == 6:  return RED
    if d == 5:  return TERRA
    if d == 4:  return IVORY
    return MAROON          # field, d <= 3


def diamond(cx, cy):
    for y in range(cy - R, cy + R + 1):
        for x in range(cx - R, cx + R + 1):
            d = abs(x - cx) + abs(y - cy)
            col = ring_col(d)
            if col is not None:
                P(x, y, col)
    # dotted band ornament
    for s in (1, -1):
        P(cx + 7 * s, cy, IVORY)
        P(cx, cy + 7 * s, IVORY)
        P(cx + 4 * s, cy + 4 * s, IVORY)
        P(cx + 4 * s, cy - 4 * s, IVORY)
    # floral heart: four-petal floret in the maroon field
    P(cx, cy, GOLD)
    for s in (1, -1):
        P(cx + s, cy, IVORY)
        P(cx, cy + s, IVORY)
        P(cx + 2 * s, cy, IVORY)
        P(cx, cy + 2 * s, IVORY)
        P(cx + s, cy + s, TERRA)
        P(cx + s, cy - s, TERRA)
        P(cx + 3 * s, cy, GOLD)
        P(cx, cy + 3 * s, GOLD)


for j in range(-1, 3):
    for i in range(-1, 3):
        if (i + j) % 2 == 0:
            diamond(16 * i, 16 * j)

save('carpet', c, indexed=True)
print(c.stats_text())
print(view(c))

# seam check: 2x2 tiling of the tile (working canvas, not submitted)
tile = new_canvas(64, 64, name="tilecheck")
tile.blit(c, 0, 0)
tile.blit(c, 32, 0)
tile.blit(c, 0, 32)
tile.blit(c, 32, 32)
print(view(tile))
finish(c)
