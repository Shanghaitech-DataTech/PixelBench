# main.py - 64x64 pixel art: fast food combo meal on a tray (45-degree top-down)
DIAG = False

# ------------------------------------------------------------------ palette
INK = "#1a1310"
TRAY_RIM = "#3a414d"; TRAY_TOP = "#4d5563"; TRAY_HI = "#5f6a7c"; TRAY_SH = "#2b303b"
BUN = "#e5a44a"; BUN_LIGHT = "#f4c87e"; BUN_MID = "#d18a34"; BUN_SH = "#b06d24"
SEED = "#fbe9c0"
LET = "#71c13f"; LET_LIGHT = "#93dd5e"; LET_DARK = "#4c9427"
CH = "#ffc73d"; CH_LIGHT = "#ffe07e"; CH_DARK = "#ef9f26"
PATTY = "#6f3f22"; PATTY_L = "#8f5530"; PATTY_D = "#512c16"
FRY = "#ffd45e"; FRY_LIGHT = "#ffeda6"; FRY_DARK = "#e3a636"
CART = "#d93a2b"; CART_D = "#a82318"; CART_L = "#f2604e"; CART_IN = "#7e1a12"
NUG = "#e9b25c"; NUG_L = "#f8d898"; NUG_D = "#c08434"; NUG_DOT = "#a5671f"
CUP = "#eef1f5"; CUP_SH = "#c6ccd8"; CUP_D = "#a6adbd"; CUP_HI = "#ffffff"
COLA = "#41200f"; COLA_L = "#5f3318"
ICE = "#cfe9f4"; ICE_L = "#eef9fd"; ICE_D = "#9cc6da"
STRAW = "#e8453c"; STRAW_D = "#b82f28"; STRAW_L = "#ff9d8f"
KETCH = "#cf2f22"; KETCH_L = "#f26a52"
MUST = "#f7c22e"; MUST_L = "#ffe07a"

CMAP = [
    (INK, "#"), (TRAY_RIM, "B"), (TRAY_TOP, "C"), (TRAY_HI, "D"), (TRAY_SH, "E"),
    (BUN, "F"), (BUN_LIGHT, "G"), (BUN_MID, "H"), (BUN_SH, "I"), (SEED, "J"),
    (LET, "K"), (LET_LIGHT, "L"), (LET_DARK, "M"),
    (CH, "N"), (CH_LIGHT, "O"), (CH_DARK, "P"),
    (PATTY, "Q"), (PATTY_L, "R"), (PATTY_D, "S"),
    (FRY, "T"), (FRY_LIGHT, "U"), (FRY_DARK, "V"),
    (CART, "W"), (CART_D, "X"), (CART_L, "Y"), (CART_IN, "Z"),
    (NUG, "a"), (NUG_L, "b"), (NUG_D, "c"), (NUG_DOT, "d"),
    (CUP, "e"), (CUP_SH, "f"), (CUP_D, "g"), (CUP_HI, "h"),
    (COLA, "i"), (COLA_L, "j"),
    (ICE, "k"), (ICE_L, "l"), (ICE_D, "m"),
    (STRAW, "n"), (STRAW_D, "o"), (STRAW_L, "p"),
    (KETCH, "q"), (KETCH_L, "r"), (MUST, "s"), (MUST_L, "t"),
]


# ------------------------------------------------------------------ helpers
def rrect(cv, x, y, w, h, r, colour):
    cv.rect(x + r, y, w - 2 * r, h, colour)
    cv.rect(x, y + r, w, h - 2 * r, colour)
    cv.circle(x + r, y + r, r, colour)
    cv.circle(x + w - 1 - r, y + r, r, colour)
    cv.circle(x + r, y + h - 1 - r, r, colour)
    cv.circle(x + w - 1 - r, y + h - 1 - r, r, colour)
    return cv


def grow_outline(cv, colour=INK):
    """Paint `colour` on every transparent pixel that touches opaque ones."""
    w, h, rgba = cv.to_rgba()

    def op(x, y):
        return 0 <= x < w and 0 <= y < h and rgba[(y * w + x) * 4 + 3] != 0

    pts = []
    for y in range(h):
        for x in range(w):
            if not op(x, y) and any(op(x + dx, y + dy)
                                    for dx in (-1, 0, 1)
                                    for dy in (-1, 0, 1) if dx or dy):
                pts.append((x, y))
    for x, y in pts:
        cv.set(x, y, colour)
    return cv


def sprite(w, h, name, fn):
    """Draw art on a w x h canvas, then pad by 1 px and grow a dark outline."""
    art = new_canvas(w, h, background=None, name=name)
    fn(art)
    s = new_canvas(w + 2, h + 2, background=None, name=name + "_o")
    s.blit(art, 1, 1)
    grow_outline(s)
    return s


# ------------------------------------------------------------------ cup
def _cup(s):
    # rounded base first, so the body overlaps it
    s.ellipse(9, 26, 6, 2, CUP_D)
    # tapered body
    s.poly([(1, 13), (17, 13), (15, 26), (3, 26)], CUP)
    s.poly([(11, 13), (17, 13), (15, 26), (10, 26)], CUP_SH)
    s.line(3, 15, 4, 24, CUP_HI)
    # rim
    s.ellipse(9, 13, 8, 4, CUP)
    for (x, y) in ((7, 9), (5, 10), (3, 11), (2, 12), (1, 13)):
        s.set(x, y, CUP_HI)
    for (x, y) in ((13, 9), (15, 10), (16, 11), (17, 12)):
        s.set(x, y, CUP_SH)
    # cola
    s.ellipse(9, 13, 6, 3, COLA)
    for (x, y) in ((9, 10), (7, 11), (5, 12), (4, 13)):
        s.set(x, y, COLA_L)
    # ice cubes
    s.rect(5, 11, 4, 3, ICE)
    s.set(5, 11, ICE_L); s.set(6, 11, ICE_L); s.set(5, 12, ICE_L)
    s.set(8, 12, ICE_D)
    s.rect(7, 13, 4, 3, ICE)
    s.set(7, 13, ICE_L); s.set(8, 13, ICE_L)
    s.set(10, 15, ICE_D); s.set(9, 15, ICE_D)
    # straw
    s.line(10, 14, 12, 0, STRAW_L)
    s.line(11, 14, 13, 0, STRAW)
    s.line(12, 14, 14, 0, STRAW_D)


# ------------------------------------------------------------------ fries
def _fries(s):
    # dark inside of the carton (drawn first)
    s.ellipse(10, 11, 9, 3, CART_IN)
    # fries, rooted below the front lip
    for (bx, tx, ty) in ((1, 0, 5), (5, 4, 2), (9, 9, 0), (13, 14, 2), (17, 18, 5)):
        s.line(bx, 14, tx, ty, FRY_LIGHT)
        s.line(bx + 1, 14, tx + 1, ty, FRY)
        s.line(bx + 2, 14, tx + 2, ty, FRY_DARK)
    # carton front (covers the fry bottoms)
    s.poly([(0, 12), (20, 12), (18, 24), (2, 24)], CART)
    s.poly([(13, 12), (20, 12), (18, 24), (12, 24)], CART_D)
    s.poly([(0, 12), (2, 12), (4, 24), (2, 24)], CART_L)
    s.line(0, 12, 20, 12, CART_L)
    # golden arch motif
    s.path("M 4 23 Q 10 11 16 23 Z M 6 23 Q 10 16 14 23 Z", MUST, fill=True)


# ------------------------------------------------------------------ burger
def _burger(s):
    # bottom bun (rows 22-25)
    s.rect(2, 22, 18, 1, BUN_MID)
    s.rect(1, 23, 20, 3, BUN_MID)
    s.line(2, 25, 19, 25, BUN_SH)
    # patty (rows 18-21)
    s.rect(1, 18, 20, 4, PATTY)
    s.line(1, 18, 20, 18, PATTY_L)
    s.line(1, 21, 20, 21, PATTY_D)
    for (x, y) in ((4, 20), (8, 19), (12, 20), (16, 19)):
        s.set(x, y, PATTY_D)
    # melted cheese (rows 14-17) + drips over the patty
    s.rect(1, 14, 20, 4, CH)
    s.line(1, 14, 20, 14, CH_LIGHT)
    s.line(1, 17, 20, 17, CH_DARK)
    s.rect(3, 18, 2, 2, CH); s.line(3, 19, 4, 19, CH_DARK)
    s.rect(10, 18, 2, 2, CH); s.line(10, 19, 11, 19, CH_DARK)
    s.rect(16, 18, 2, 2, CH); s.line(16, 19, 17, 19, CH_DARK)
    # ruffled lettuce (rows 11-14)
    s.rect(0, 11, 22, 3, LET)
    s.line(0, 11, 21, 11, LET_LIGHT)
    for cx in (0, 4, 8, 12, 16, 20):
        s.rect(cx, 13, 2, 2, LET)
        s.line(cx, 14, cx + 1, 14, LET_DARK)
    for gx in (2, 6, 10, 14, 18):
        s.set(gx, 13, LET_DARK)
    # bun side (rows 9-10)
    s.rect(1, 9, 20, 2, BUN_MID)
    s.line(1, 10, 20, 10, BUN_SH)
    # sesame dome (rows 0-8)
    for (y, x0, w) in ((0, 9, 4), (1, 7, 8), (2, 6, 10), (3, 5, 12),
                       (4, 4, 14), (5, 3, 16), (6, 2, 18), (7, 1, 20), (8, 1, 20)):
        s.rect(x0, y, w, 1, BUN)
    s.rect(8, 1, 3, 1, BUN_LIGHT)
    s.rect(7, 2, 4, 1, BUN_LIGHT)
    s.rect(6, 3, 4, 1, BUN_LIGHT)
    s.rect(5, 4, 4, 1, BUN_LIGHT)
    s.rect(4, 5, 4, 1, BUN_LIGHT)
    for (x, y) in ((11, 2), (15, 4), (7, 4), (13, 6), (5, 6), (9, 7), (17, 7)):
        s.set(x, y, SEED); s.set(x + 1, y, SEED)


# ------------------------------------------------------------------ nuggets
NUGGET_ART = (
    "..mmmm..",
    ".lmmmmm.",
    "lmmmmmd.",
    "lmmmmdd.",
    ".lmmdd..",
    "..mdd...",
)


def _nugget(s):
    for y, row in enumerate(NUGGET_ART):
        for x, ch in enumerate(row):
            if ch == 'l':
                s.set(x, y, NUG_L)
            elif ch == 'm':
                s.set(x, y, NUG)
            elif ch == 'd':
                s.set(x, y, NUG_D)
    for (x, y) in ((3, 1), (5, 2), (2, 3)):
        s.set(x, y, NUG_DOT)


def _nuggets(s):
    n = sprite(8, 6, "nugget", _nugget)
    s.blit(n, 2, 0)
    s.blit(n, 0, 4)
    s.blit(n, 5, 5)


# ------------------------------------------------------------------ sauces
SAUCE_ART = (
    ".WWWW..",
    "WlsssW.",
    "WlsssW.",
    "WssssW.",
    ".WssW..",
    ".WWWW..",
    "..WWW..",
)


def _sauce_cup(s, sauce, sauce_l):
    m = {'W': CUP, 'l': sauce_l, 's': sauce}
    for y, row in enumerate(SAUCE_ART):
        for x, ch in enumerate(row):
            if ch in m:
                s.set(x, y, m[ch])


def _sauces(s):
    k = sprite(7, 7, "ketchup", lambda cv: _sauce_cup(cv, KETCH, KETCH_L))
    m = sprite(7, 7, "mustard", lambda cv: _sauce_cup(cv, MUST, MUST_L))
    s.blit(k, 5, 0)
    s.blit(m, 0, 4)


# ------------------------------------------------------------------ compose
def compose():
    c = new_canvas(64, 64, background=None, name="fast-food-combo")
    # tray with a dark outline
    rrect(c, 0, 2, 64, 60, 9, INK)
    rrect(c, 1, 3, 62, 58, 8, TRAY_RIM)
    rrect(c, 3, 5, 58, 54, 5, TRAY_TOP)
    c.line(9, 5, 54, 5, TRAY_HI)
    c.line(3, 11, 3, 52, TRAY_HI)
    c.line(9, 58, 54, 58, TRAY_SH)
    c.line(60, 11, 60, 52, TRAY_SH)
    # soft shadows under the items
    c.ellipse(15, 31, 7, 1, TRAY_SH)
    c.ellipse(47, 29, 7, 1, TRAY_SH)
    c.ellipse(32, 54, 8, 1, TRAY_SH)
    c.ellipse(11, 57, 5, 1, TRAY_SH)
    c.ellipse(52, 57, 5, 1, TRAY_SH)
    # items, back to front
    c.blit(sprite(20, 29, "cup", _cup), 4, 1)
    c.blit(sprite(21, 25, "fries", _fries), 36, 3)
    c.blit(sprite(22, 26, "burger", _burger), 20, 27)
    c.blit(sprite(15, 13, "nuggets", _nuggets), 3, 41)
    c.blit(sprite(14, 13, "sauces", _sauces), 44, 41)
    return c


# ------------------------------------------------------------------ run
def dump(cv, label):
    w, h, rgba = cv.to_rgba()
    lut = {}
    for col, ch in CMAP:
        lut[(int(col[1:3], 16), int(col[3:5], 16), int(col[5:7], 16))] = ch
    print(f"--- {label} {w}x{h} ---")
    print("    " + "".join(str(x // 10 % 10) for x in range(w)))
    print("    " + "".join(str(x % 10) for x in range(w)))
    unknown = set()
    for y in range(h):
        row = ""
        for x in range(w):
            o = (y * w + x) * 4
            if rgba[o + 3] == 0:
                row += "."
                continue
            key = (rgba[o], rgba[o + 1], rgba[o + 2])
            ch = lut.get(key)
            if ch is None:
                unknown.add(key)
                ch = "?"
            row += ch
        print(f"{y:3d} " + row)
    if unknown:
        print("UNKNOWN: " + " ".join(f"#{r:02x}{g:02x}{b:02x}"
                                     for (r, g, b) in sorted(unknown)))


if DIAG:
    dump(sprite(20, 29, "cup", _cup), "cup")
    dump(sprite(21, 25, "fries", _fries), "fries")
    dump(sprite(22, 26, "burger", _burger), "burger")
    dump(sprite(15, 13, "nuggets", _nuggets), "nuggets")
    dump(sprite(14, 13, "sauces", _sauces), "sauces")
else:
    c = compose()
    print(c.stats_text())
    print(c.matrix_text())
    finish(c)
