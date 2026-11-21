import math

# ---------- palette ----------
DARK = '#171522'
STEEL_L = '#eef3fb'
STEEL_M = '#aab8ca'
STEEL_D = '#6d7d95'
WOOD_L = '#c08346'
WOOD_M = '#8d5427'
WOOD_D = '#5c3517'
GOLD_L = '#ffe07a'
GOLD_M = '#d9a63a'
GOLD_D = '#9c6a1c'
BLUE_L = '#5b8fc7'
BLUE_M = '#3e6fa6'
BLUE_D = '#26456b'
LEATHER_L = '#7d5c4b'
LEATHER = '#5c4238'
LEATHER_D = '#3d2b24'

CELL = 32


# ---------- helpers ----------
def alpha_of(c):
    return {p['index']: (p['rgba'][3] if len(p['rgba']) > 3 else 255) for p in c.palette()}


def row_spans(c, w=CELL, h=CELL):
    am = alpha_of(c)
    out = []
    for y in range(h):
        first = last = None
        for x in range(w):
            if am.get(c.get(x, y), 0) > 0:
                if first is None:
                    first = x
                last = x
        out.append((first, last))
    return out


def outline_layer(c, colour=DARK):
    w, h = c.stats()['size']
    sil = new_canvas(w, h)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            sil.blit(c, dx, dy)
    am = alpha_of(sil)
    for y in range(h):
        for x in range(w):
            if am.get(sil.get(x, y), 0) > 0:
                sil.set(x, y, colour)
    out = new_canvas(w, h)
    out.blit(sil, 0, 0)
    out.blit(c, 0, 0)
    return out


# ---------- sword ----------
def make_sword():
    c = new_canvas(CELL, CELL)
    cx = 15
    # blade
    for y in range(2, 20):
        if y == 2:
            half = 0
        elif y == 3:
            half = 1
        else:
            half = 2
        x0, x1 = cx - half, cx + half
        for x in range(x0, x1 + 1):
            off = x - x0
            if off <= 1:
                col = STEEL_L
            elif x == x1:
                col = STEEL_D
            else:
                col = STEEL_M
            c.set(x, y, col)
    # cross guard
    for x in range(9, 22):
        c.set(x, 20, GOLD_L)
    for x in range(8, 23):
        c.set(x, 21, GOLD_M)
    for x in range(10, 21):
        c.set(x, 22, GOLD_D)
    # grip
    for y in range(23, 27):
        base = LEATHER_D if y % 2 == 0 else LEATHER
        c.set(14, y, LEATHER_L)
        c.set(15, y, base)
        c.set(16, y, LEATHER_D)
    # pommel
    c.circle(15, 28, 2, GOLD_M)
    c.set(14, 27, GOLD_L)
    c.set(16, 29, GOLD_D)
    return c


# ---------- bow ----------
def make_bow():
    c = new_canvas(CELL, CELL)
    P0 = (12.0, 3.0)
    P1 = (31.0, 16.0)
    P2 = (12.0, 29.0)
    pts = []
    for i in range(161):
        t = i / 160.0
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
        pts.append((x, y))
    for (x, y) in pts:
        c.circle(int(round(x)), int(round(y)), 1, WOOD_M)
    # limb shading by row
    for y, (a, b) in enumerate(row_spans(c)):
        if a is None:
            continue
        c.set(a, y, WOOD_L)
        c.set(b, y, WOOD_D)
    # nocks
    c.circle(12, 3, 1, GOLD_M)
    c.circle(12, 29, 1, GOLD_M)
    c.set(11, 2, GOLD_L)
    c.set(11, 28, GOLD_L)
    # leather grip
    for y in range(13, 20):
        a, b = row_spans(c)[y]
        if a is None:
            continue
        for x in range(a, b + 1):
            if y in (14, 17):
                col = LEATHER_D
            elif x == a:
                col = LEATHER_L
            elif x == b:
                col = LEATHER_D
            else:
                col = LEATHER
            c.set(x, y, col)
    return c


def add_string(c):
    c.line(11, 4, 11, 29, DARK)
    return c


# ---------- shield ----------
def make_shield():
    c = new_canvas(CELL, CELL)
    outer = [(7, 4), (24, 4), (24, 12), (21, 19), (15, 28), (9, 19), (7, 12)]
    field = [(9, 6), (22, 6), (22, 12), (19, 17), (15, 24), (11, 17), (9, 12)]
    c.poly(outer, STEEL_M)
    # rim lighting / shading
    sp = row_spans(c)
    for y, (a, b) in enumerate(sp):
        if a is None:
            continue
        c.set(a, y, STEEL_L)
        c.set(b, y, STEEL_D)
    for x in range(8, 24):
        c.set(x, 4, STEEL_L)
        c.set(x, 5, STEEL_M)

    field_c = new_canvas(CELL, CELL)
    field_c.poly(field, BLUE_M)
    for y, (a, b) in enumerate(row_spans(field_c)):
        if a is None:
            continue
        field_c.set(a, y, BLUE_L)
        field_c.set(b, y, BLUE_D)
    # circular gold boss
    bx, by, br = 15, 12, 3
    for y in range(by - br, by + br + 1):
        for x in range(bx - br, bx + br + 1):
            if (x - bx) ** 2 + (y - by) ** 2 <= br * br + br:
                s = (x - bx) + (y - by)
                col = GOLD_L if s <= -2 else (GOLD_D if s >= 2 else GOLD_M)
                field_c.set(x, y, col)
    c.blit(field_c, 0, 0)
    return c

# ---------- battle axe ----------
def make_axe():
    c = new_canvas(CELL, CELL)
    blade_pts = [(20, 7), (15, 4), (11, 5), (9, 8), (8, 13), (9, 17), (11, 20), (15, 21), (20, 18)]
    bl = new_canvas(CELL, CELL)
    bl.poly(blade_pts, STEEL_M)
    for y, (a, b) in enumerate(row_spans(bl)):
        if a is None:
            continue
        bl.set(a, y, STEEL_L)
        if a + 1 < b:
            bl.set(a + 1, y, STEEL_L)
        bl.set(b, y, STEEL_D)
        if b - 1 > a + 1:
            bl.set(b - 1, y, STEEL_D)
    for x in range(15, 22):
        bl.set(x, 5, STEEL_L)
    # top edge catches the light
    am = alpha_of(bl)
    for y in range(1, 32):
        for x in range(32):
            if am.get(bl.get(x, y), 0) > 0 and am.get(bl.get(x, y - 1), 0) == 0:
                bl.set(x, y, STEEL_L)
    c.blit(bl, 0, 0)
    # haft
    for y in range(2, 30):
        c.set(21, y, WOOD_L)
        c.set(22, y, WOOD_M)
        c.set(23, y, WOOD_D)
    # collar under the head
    for x in (21, 22, 23):
        c.set(x, 22, GOLD_M)
    c.set(21, 22, GOLD_L)
    c.set(23, 22, GOLD_D)
    # grip
    for y in range(23, 29):
        band = LEATHER_D if y in (25, 27) else LEATHER
        c.set(21, y, LEATHER_L)
        c.set(22, y, band)
        c.set(23, y, LEATHER_D)    # pommel
    c.set(21, 29, GOLD_L)
    c.set(22, 29, GOLD_M)
    c.set(23, 29, GOLD_D)
    return c


def build():
    sword = outline_layer(make_sword())
    bow = add_string(outline_layer(make_bow()))
    shield = outline_layer(make_shield())
    axe = outline_layer(make_axe())
    res = new_canvas(64, 64, name='weapon_set')
    res.blit(sword, 0, 0)
    res.blit(bow, 32, 0)
    res.blit(shield, 0, 32)
    res.blit(axe, 32, 32)
    return res, sword, bow, shield, axe


res, sword, bow, shield, axe = build()
print(res.stats_text())
print('AXE')
print(axe.matrix_text(region=(0, 32, 31, 63)))
save('weapon_set', res)
finish(res)
