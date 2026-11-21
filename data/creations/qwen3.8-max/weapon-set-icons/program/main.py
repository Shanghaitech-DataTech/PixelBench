"""Weapon icon set: 64x64, 2x2 grid (sword, bow, shield, battle axe)."""

# ---------------------------------------------------------------- palette ----
OUT      = '#17111d'
STEEL_HI = '#eef3fa'
STEEL    = '#b6c3d4'
STEEL_MD = '#8493a8'
STEEL_DK = '#525f78'
GOLD_HI  = '#ffe89a'
GOLD     = '#e3ad39'
GOLD_DK  = '#9c6a1c'
WOOD_HI  = '#c98a4b'
WOOD     = '#9a6234'
WOOD_DK  = '#66391b'
RED_HI   = '#e8685e'
RED      = '#bf3a30'
RED_DK   = '#83231f'
STRING   = '#c3ccd8'

METAL = [STEEL_HI, STEEL_HI, STEEL, STEEL, STEEL_MD, STEEL_DK, STEEL_DK]
METALC = [STEEL_DK, STEEL_MD, STEEL, STEEL, STEEL_HI, STEEL_HI]
GOLDR = [GOLD_HI, GOLD_HI, GOLD, GOLD, GOLD_DK, GOLD_DK]
WOODR = [WOOD_HI, WOOD_HI, WOOD, WOOD, WOOD_DK, WOOD_DK]
REDR  = [RED_HI, RED_HI, RED, RED, RED, RED_DK, RED_DK]


def dims(c):
    s = c.stats()['size']
    return s[0], s[1]


def shade_runs(c, base_hex, ramp):
    """Row-wise: recolour every contiguous run of base_hex with the ramp."""
    base = c.color(base_hex)
    w, h = dims(c)
    for y in range(h):
        x = 0
        while x < w:
            if c.get(x, y) == base:
                x0 = x
                while x < w and c.get(x, y) == base:
                    x += 1
                x1 = x - 1
                n = x1 - x0 + 1
                for i, xx in enumerate(range(x0, x1 + 1)):
                    f = (i / (n - 1)) if n > 1 else 0.5
                    c.set(xx, y, ramp[min(int(f * len(ramp)), len(ramp) - 1)])
            else:
                x += 1


def shade_cols(c, base_hex, ramp, x0, x1, y0, y1):
    """Column-wise ramp across a bounding box."""
    base = c.color(base_hex)
    n = x1 - x0 + 1
    for x in range(x0, x1 + 1):
        f = (x - x0) / (n - 1) if n > 1 else 0.5
        col = ramp[min(int(f * len(ramp)), len(ramp) - 1)]
        for y in range(y0, y1 + 1):
            if c.get(x, y) == base:
                c.set(x, y, col)


# ------------------------------------------------------------------ sword ----
def make_sword():
    c = new_canvas(32, 32, name='sword')
    # blade
    c.poly([(16, 1), (19, 5), (19, 20), (13, 20), (13, 5)], OUT)
    c.poly([(16, 3), (18, 6), (18, 19), (14, 19), (14, 6)], STEEL)
    shade_runs(c, STEEL, METAL)
    for y in range(5, 19):          # fuller groove
        c.set(16, y, STEEL_MD)
    # crossguard
    c.poly([(6, 22), (9, 20), (23, 20), (26, 22), (23, 24), (9, 24)], OUT)
    c.poly([(8, 22), (10, 21), (22, 21), (24, 22), (22, 23), (10, 23)], GOLD)
    shade_runs(c, GOLD, GOLDR)
    # grip
    c.rect(13, 23, 6, 6, OUT)
    c.rect(14, 24, 4, 4, RED)
    shade_runs(c, RED, REDR)
    for y in (25, 27):
        for x in range(14, 18):
            c.set(x, y, RED_DK)
    # pommel
    c.circle(16, 29, 2, OUT)
    c.circle(16, 29, 1, GOLD)
    c.set(16, 28, GOLD_HI)
    c.set(15, 29, GOLD_HI)
    c.set(17, 30, GOLD_DK)
    # guard gem
    c.set(16, 21, RED_HI)
    c.set(15, 22, RED)
    c.set(16, 22, RED)
    c.set(17, 22, RED_DK)
    c.set(16, 23, RED_DK)
    return c


# ------------------------------------------------------------------- bow -----
def make_bow():
    c = new_canvas(32, 32, name='bow')
    x0, amp = 9.0, 13.0
    ymid, half = 16.0, 14.0

    for y in range(2, 31):          # string
        c.set(9, y, STRING)
    c.set(9, 16, '#98a4b4')

    spans = {}
    for y in range(2, 31):
        t = (y - ymid) / half
        u = max(0.0, 1.0 - t * t)
        xc = x0 + amp * (u ** 0.75)
        w = 1.0 + 1.5 * u
        ix0, ix1 = int(round(xc - w)), int(round(xc + w))
        spans[y] = (ix0, ix1)
        for x in range(ix0, ix1 + 1):
            c.set(x, y, OUT)
        for x in range(ix0 + 1, ix1):
            c.set(x, y, WOOD)
        if ix1 - ix0 >= 3:
            c.set(ix0 + 1, y, WOOD_HI)
            c.set(ix1 - 1, y, WOOD_DK)
        if ix1 - ix0 >= 4:
            c.set(ix0 + 2, y, WOOD)

    for y in (3, 4, 28, 29):        # gold nock bindings at the tips
        ix0, ix1 = spans[y]
        for x in range(ix0, ix1 + 1):
            c.set(x, y, OUT if x in (ix0, ix1) else GOLD)
        if ix1 - ix0 >= 3:
            c.set(ix0 + 1, y, GOLD_HI)
            c.set(ix1 - 1, y, GOLD_DK)

    for y in range(13, 20):         # red grip wrap
        ix0, ix1 = spans[y]
        for x in range(ix0 + 1, ix1):
            c.set(x, y, RED)
        if ix1 - ix0 >= 3:
            c.set(ix0 + 1, y, RED_HI)
            c.set(ix1 - 1, y, RED_DK)
    for y in (14, 16, 18):
        ix0, ix1 = spans[y]
        for x in range(ix0 + 1, ix1):
            c.set(x, y, RED_DK)
    return c


# ---------------------------------------------------------------- shield -----
def make_shield():
    c = new_canvas(32, 32, name='shield')
    outer = ("M 6 2 L 26 2 Q 29 2 29 5 L 29 15 C 29 22 24 27 16 30 "
             "C 8 27 3 22 3 15 L 3 5 Q 3 2 6 2 Z")
    rim = ("M 6.5 4 L 25.5 4 Q 27 4 27 5.5 L 27 15 C 27 21 22.5 25.5 16 28 "
           "C 9.5 25.5 5 21 5 15 L 5 5.5 Q 5 4 6.5 4 Z")
    field = ("M 8 6 L 24 6 L 25 7 L 25 15 C 25 20 21 24 16 26 "
             "C 11 24 7 20 7 15 L 7 7 Z")
    c.path(outer, OUT)
    c.path(rim, GOLD)
    shade_runs(c, GOLD, GOLDR)
    c.path(field, RED)
    shade_runs(c, RED, REDR)

    # gold cross emblem
    c.poly([(13, 7), (18, 7), (18, 12), (23, 12), (23, 17), (18, 17),
            (18, 25), (13, 25), (13, 17), (8, 17), (8, 12), (13, 12)], OUT)
    c.rect(14, 8, 4, 17, GOLD)
    c.rect(9, 13, 14, 4, GOLD)
    for i, x in enumerate((14, 15, 16, 17)):
        col = (GOLD_HI, GOLD, GOLD, GOLD_DK)[i]
        for y in range(8, 25):
            c.set(x, y, col)
    for i, y in enumerate((13, 14, 15, 16)):
        row = (GOLD_HI, GOLD, GOLD, GOLD_DK)[i]
        for x in range(9, 23):
            c.set(x, y, row)

    # centre boss
    c.circle(16, 14, 3, OUT)
    c.circle(16, 14, 2, STEEL)
    shade_runs(c, STEEL, METAL)
    c.set(15, 13, STEEL_HI)
    c.set(16, 13, STEEL_HI)
    c.set(16, 16, STEEL_DK)

    # rivets on the rim
    for (rx, ry) in ((7, 5), (25, 5), (5, 12), (27, 12), (16, 27)):
        c.set(rx, ry, OUT)
    for (rx, ry) in ((7, 4), (25, 4)):
        c.set(rx, ry, GOLD_HI)
    return c


# ------------------------------------------------------------------- axe -----
def make_axe():
    c = new_canvas(32, 32, name='axe')
    steel_idx = {c.color(h) for h in (STEEL_HI, STEEL, STEEL_MD, STEEL_DK)}

    # handle
    c.rect(12, 2, 6, 29, OUT)
    c.rect(13, 3, 4, 27, WOOD)
    shade_runs(c, WOOD, WOODR)

    # back spike
    c.path("M 12 7 L 5 10 L 3 12 L 5 14 L 12 17 Z", OUT)
    c.path("M 12 8.6 L 6.2 11 L 5 12 L 6.2 13 L 12 15.4 Z", STEEL)
    shade_runs(c, STEEL, METAL)

    # flared blade: sloped top/bottom edges, pointed corners, convex edge
    c.path("M 14 8 L 20 5 L 26 3 Q 29 12 26 21 L 20 19 L 14 16 Z", OUT)
    c.path("M 15 9.4 L 20.5 6.8 L 25 5 Q 27.4 12 25 19 L 20.5 17.2 "
           "L 15 14.6 Z", STEEL)
    shade_cols(c, STEEL, METALC, 14, 28, 3, 21)

    # bright cutting edge, clipped to the filled blade
    for y in range(4, 21):
        xr = None
        for x in range(28, 14, -1):
            if c.get(x, y) in steel_idx:
                xr = x
                break
        if xr is not None and xr > 16:
            c.set(xr, y, STEEL_HI)
            c.set(xr - 1, y, STEEL_HI if 7 <= y <= 17 else STEEL)

    # rivets on the head
    for (rx, ry) in ((16, 10), (16, 14), (20, 12)):
        c.set(rx, ry, OUT)
    for (rx, ry) in ((16, 9), (16, 13), (20, 11)):
        c.set(rx, ry, STEEL_HI)

    # gold band under the head
    c.rect(11, 21, 7, 4, OUT)
    c.rect(12, 22, 5, 2, GOLD)
    c.rect(12, 22, 5, 1, GOLD_HI)
    c.rect(12, 23, 5, 1, GOLD_DK)

    # red grip wrap
    c.rect(13, 25, 4, 4, RED)
    c.rect(13, 25, 1, 4, RED_HI)
    c.rect(16, 25, 1, 4, RED_DK)
    for y in (26, 28):
        c.rect(13, y, 4, 1, RED_DK)

    # steel butt cap and crown
    c.rect(12, 28, 6, 3, OUT)
    c.rect(13, 29, 4, 1, STEEL)
    c.set(13, 29, STEEL_HI)
    c.set(16, 29, STEEL_DK)
    c.rect(13, 3, 4, 1, STEEL_HI)
    return c


# ----------------------------------------------------------------- assemble --
result = new_canvas(64, 64, name='weapon_set')
result.blit(make_sword(), 0, 0)
result.blit(make_bow(), 32, 0)
result.blit(make_shield(), 0, 32)
result.blit(make_axe(), 32, 32)

print(result.stats_text())
p = view(result)
print('preview:', p)
for _nm in ('sword', 'bow', 'shield', 'axe'):
    view(canvas(_nm), scale=12, margin=1)
save('weapon_set', result, indexed=True)
finish(result)
