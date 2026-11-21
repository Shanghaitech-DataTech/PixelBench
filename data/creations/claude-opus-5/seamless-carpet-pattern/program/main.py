C = new_canvas(32, 32, name="carpet")

DARK  = C.color("#3b1a14", "dark")
RED   = C.color("#9e3b26", "red")
RED2  = C.color("#8a3220", "red2")
RUST  = C.color("#c05a2a", "rust")
GOLD  = C.color("#e0a44b", "gold")
CREAM = C.color("#f2dcb3", "cream")
TEAL  = C.color("#3f6b63", "teal")


def px(x, y, col):
    C.set(x % 32, y % 32, col)


def u(v):
    """wrapped distance of a coordinate from the tile seam (between 31 and 0)"""
    return v + 0.5 if v <= 15 else 31.5 - v


# ---- woven field -------------------------------------------------
C.dither(0, 0, 32, 32, [RED, RED2], pattern="checker")

# ---- border frame rings (mitred, straddling the seam) ------------
RING = {2.5: DARK, 3.5: GOLD, 4.5: RUST}
for y in range(32):
    for x in range(32):
        r = min(u(x), u(y))
        if r < 2:
            C.set(x, y, CREAM)
        elif r in RING:
            C.set(x, y, RING[r])

# ---- floral vine in the cream band -------------------------------
def flower(c, horiz):
    """4x4 rosette centred on the seam, c = centre along the band (x.5)"""
    a = int(c - 0.5)
    b = a + 1
    for s in (31, 0):
        for t, col in ((a - 1, RUST), (a, GOLD), (b, GOLD), (b + 1, RUST)):
            px(t, s, col) if horiz else px(s, t, col)
    for s in (30, 1):
        for t in (a, b):
            px(t, s, RUST) if horiz else px(s, t, RUST)


def leaf(c, horiz):
    a = int(c - 0.5)
    for s in (31, 0):
        for t in (a, a + 1):
            px(t, s, TEAL) if horiz else px(s, t, TEAL)


for horiz in (True, False):
    for c in (3.5, 11.5, 19.5, 27.5):
        flower(c, horiz)
    for c in (7.5, 15.5, 23.5):
        leaf(c, horiz)

# ---- corner rosette (4x4 block over the tile corner) -------------
CORNER = [
    [TEAL, RUST, RUST, TEAL],
    [RUST, GOLD, GOLD, RUST],
    [RUST, GOLD, GOLD, RUST],
    [TEAL, RUST, RUST, TEAL],
]
for j, row in enumerate(CORNER):
    for i, col in enumerate(row):
        px(30 + i, 30 + j, col)

# ---- central diamond medallion -----------------------------------
MED = {9: DARK, 8: GOLD, 7: CREAM, 6: TEAL, 5: TEAL, 4: CREAM, 3: RUST, 2: RUST, 1: GOLD}
for y in range(5, 27):
    for x in range(5, 27):
        d = (abs(2 * x - 31) + abs(2 * y - 31)) // 2
        if d in MED:
            C.set(x, y, MED[d])

# ---- small diamonds in the field corners -------------------------
SMALL = {0: CREAM, 1: GOLD, 2: RUST}
for cy in (8, 23):
    for cx in (8, 23):
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                d = abs(dx) + abs(dy)
                if d in SMALL:
                    C.set(cx + dx, cy + dy, SMALL[d])

# ---- woven weft highlights in the open field ---------------------
for y in range(6, 26):
    for x in range(6, 26):
        d = (abs(2 * x - 31) + abs(2 * y - 31)) // 2
        if d > 9 and (x + y) % 4 == 0 and (x - y) % 4 == 0:
            C.set(x, y, GOLD)

# ---- tiling check on a throwaway working canvas ------------------
T = new_canvas(96, 96, name="tilecheck")
for ty in range(3):
    for tx in range(3):
        T.blit(C, tx * 32, ty * 32)
view(T)
view(C)
print(C.stats_text())
finish(C)
