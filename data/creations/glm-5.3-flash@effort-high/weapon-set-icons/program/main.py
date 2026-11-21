# Weapon icon set: 64x64, 2x2 grid of 32x32 icons
# sword (top-left), bow (top-right), shield (bottom-left), battle axe (bottom-right)

c = new_canvas(64, 64, background=None, name="weapon-icons")

PALETTE = [
    ("outline", "#232331"),
    ("steel_light", "#e9edf4"),
    ("steel", "#b7c0cd"),
    ("steel_dark", "#7c8598"),
    ("wood", "#9a6430"),
    ("wood_light", "#c08544"),
    ("wood_dark", "#6e441d"),
    ("gold", "#e3b341"),
    ("gold_dark", "#a87c1f"),
    ("red", "#c23b4a"),
    ("red_dark", "#8a2434"),
    ("bowstring", "#d9cbb2"),
]
I = {}
for name, hexv in PALETTE:
    I[name] = c.color(hexv, name=name)

O = I["outline"]; L = I["steel_light"]; S = I["steel"]; D = I["steel_dark"]
W = I["wood"]; w = I["wood_light"]; d = I["wood_dark"]
G = I["gold"]; g = I["gold_dark"]
R = I["red"]; r = I["red_dark"]; T = I["bowstring"]

CH = {'O': O, 'L': L, 'S': S, 'D': D, 'W': W, 'w': w, 'd': d,
      'G': G, 'g': g, 'R': R, 'r': r, 'T': T}


def stamp(ox, oy, rows):
    for y, row in enumerate(rows):
        if len(row) != 32:
            raise ValueError("row %d has length %d" % (y, len(row)))
        for x, ch in enumerate(row):
            if ch != '.':
                c.set(ox + x, oy + y, CH[ch])


# ---------------------------------------------------------------- SWORD -----
SWORD = (
    ['...............OO...............',
     '..............OLDO..............']
    + ['.............OLSDO..............'] * 16
    + ['.............ODDDO..............',
       '.........OOOOOOOOOOOOOO.........',
       '.........OwGGGGRrGGGGgO.........',
       '.........OOOOOOOOOOOOOO.........',
       '..............OddO..............',
       '..............OdwO..............',
       '..............OwwO..............',
       '..............OdwO..............',
       '..............OwdO..............',
       '..............OddO..............',
       '.............OOOOOO.............',
       '.............OGggGO.............',
       '.............OOOOOO.............']
)

# ------------------------------------------------------------------- BOW ----
def draw_bow(ox, oy):
    import math
    # wooden limb: arc bulging left, tips at (20,3) and (20,28)
    for y in range(3, 29):
        t = (y - 3) / 25.0
        xi = int(round(20 - 11 * math.sin(math.pi * t)))
        c.set(ox + xi - 2, oy + y, O)
        c.set(ox + xi - 1, oy + y, w)
        c.set(ox + xi,     oy + y, W)
        c.set(ox + xi + 1, oy + y, d)
        c.set(ox + xi + 2, oy + y, O)
    # leather grip wrap on the limb
    for y in range(14, 18):
        t = (y - 3) / 25.0
        xi = int(round(20 - 11 * math.sin(math.pi * t)))
        c.set(ox + xi - 1, oy + y, R)
        c.set(ox + xi,     oy + y, r)
        c.set(ox + xi + 1, oy + y, R)
    # bowstring, tip to tip
    for y in range(3, 29):
        c.set(ox + 20, oy + y, T)
    # arrow shaft (y=16), skipping behind the limb
    for x in range(3, 26):
        if 7 <= x <= 11:
            continue
        c.set(ox + x, oy + 16, W)
    # arrowhead (steel, pointing left)
    c.set(ox + 5, oy + 14, O); c.set(ox + 6, oy + 14, L); c.set(ox + 7, oy + 14, O)
    c.set(ox + 4, oy + 15, O); c.set(ox + 5, oy + 15, L); c.set(ox + 6, oy + 15, S); c.set(ox + 7, oy + 15, O)
    c.set(ox + 2, oy + 16, O); c.set(ox + 3, oy + 16, L); c.set(ox + 4, oy + 16, S)
    c.set(ox + 5, oy + 16, S); c.set(ox + 6, oy + 16, D); c.set(ox + 7, oy + 16, O)
    c.set(ox + 4, oy + 17, O); c.set(ox + 5, oy + 17, D); c.set(ox + 6, oy + 17, D); c.set(ox + 7, oy + 17, O)
    c.set(ox + 5, oy + 18, O); c.set(ox + 6, oy + 18, D); c.set(ox + 7, oy + 18, O)
    # fletching (feathers above and below the shaft)
    c.set(ox + 26, oy + 12, O); c.set(ox + 27, oy + 12, L); c.set(ox + 28, oy + 12, O)
    c.set(ox + 25, oy + 13, O); c.set(ox + 26, oy + 13, L); c.set(ox + 27, oy + 13, L); c.set(ox + 28, oy + 13, O)
    c.set(ox + 24, oy + 14, O); c.set(ox + 25, oy + 14, L); c.set(ox + 26, oy + 14, L); c.set(ox + 27, oy + 14, L); c.set(ox + 28, oy + 14, O)
    c.set(ox + 24, oy + 15, O); c.set(ox + 25, oy + 15, L); c.set(ox + 26, oy + 15, L); c.set(ox + 27, oy + 15, O)
    c.set(ox + 24, oy + 17, O); c.set(ox + 25, oy + 17, L); c.set(ox + 26, oy + 17, L); c.set(ox + 27, oy + 17, O)
    c.set(ox + 24, oy + 18, O); c.set(ox + 25, oy + 18, L); c.set(ox + 26, oy + 18, L); c.set(ox + 27, oy + 18, L); c.set(ox + 28, oy + 18, O)
    c.set(ox + 25, oy + 19, O); c.set(ox + 26, oy + 19, L); c.set(ox + 27, oy + 19, L); c.set(ox + 28, oy + 19, O)
    c.set(ox + 26, oy + 20, O); c.set(ox + 27, oy + 20, L); c.set(ox + 28, oy + 20, O)


# ---------------------------------------------------------------- SHIELD ----
SHIELD_SPANS = (
    [(4, 6, 25), (5, 5, 26)]
    + [(y, 4, 27) for y in range(6, 17)]
    + [(17, 5, 26), (18, 5, 26), (19, 6, 25), (20, 6, 25),
       (21, 7, 24), (22, 7, 24), (23, 8, 23), (24, 8, 23),
       (25, 9, 22), (26, 10, 21), (27, 12, 19), (28, 13, 18), (29, 15, 16)]
)


def draw_shield(ox, oy):
    # top outline
    for x in range(7, 25):
        c.set(ox + x, oy + 3, O)
    for y, x0, x1 in SHIELD_SPANS:
        # fill the whole row, then lay the rim shading over the edges
        for x in range(x0 + 1, x1):
            c.set(ox + x, oy + y, R)
        c.set(ox + x0 + 1, oy + y, S)
        c.set(ox + x1 - 1, oy + y, D)
        if x1 - x0 >= 6:
            c.set(ox + x0 + 2, oy + y, S)
            c.set(ox + x1 - 2, oy + y, D)
    # gold cross: vertical band, carried down into the point
    for y in range(5, 29):
        c.set(ox + 15, oy + y, G)
        c.set(ox + 16, oy + y, g)
    # horizontal band
    for x in range(7, 25):
        c.set(ox + x, oy + 11, G)
        c.set(ox + x, oy + 12, g)


# ------------------------------------------------------------- BATTLE AXE ---
AXE_HEAD = [(2, 11, 20), (3, 9, 22), (4, 7, 24), (5, 6, 25),
            (6, 6, 25), (7, 7, 24), (8, 9, 22), (9, 11, 20)]


def draw_axe(ox, oy):
    # double-bit head: lens shape, bright cutting edges left and right
    for y, x0, x1 in AXE_HEAD:
        for x in range(x0, x1 + 1):
            c.set(ox + x, oy + y, O)
    for y, x0, x1 in AXE_HEAD:
        for x in range(x0 + 1, x1):
            c.set(ox + x, oy + y, S)
        c.set(ox + x0 + 1, oy + y, L)
        c.set(ox + x1 - 1, oy + y, L)
    # haft
    for y in range(3, 30):
        c.set(ox + 14, oy + y, O)
        c.set(ox + 15, oy + y, w)
        c.set(ox + 16, oy + y, W)
        c.set(ox + 17, oy + y, W)
        c.set(ox + 18, oy + y, d)
        c.set(ox + 19, oy + y, O)
    for x in range(14, 20):
        c.set(ox + x, oy + 29, O)
    # gold collar where head meets haft
    c.set(ox + 15, oy + 10, G); c.set(ox + 16, oy + 10, G)
    c.set(ox + 17, oy + 10, g); c.set(ox + 18, oy + 10, g)
    # leather grip wrap
    for y in range(22, 25):
        c.set(ox + 15, oy + y, R)
        c.set(ox + 16, oy + y, r)
        c.set(ox + 17, oy + y, R)


# ----------------------------------------------------------------- LAYOUT ---
stamp(0, 0, SWORD)        # top-left: sword
draw_bow(32, 0)           # top-right: bow
draw_shield(0, 32)        # bottom-left: shield
draw_axe(32, 32)          # bottom-right: battle axe

print(c.stats_text())
print("--- sword ---");  print(c.matrix_text(region=(0, 0, 31, 31)))
print("--- bow ---");    print(c.matrix_text(region=(32, 0, 63, 31)))
print("--- shield ---"); print(c.matrix_text(region=(0, 32, 31, 63)))
print("--- axe ---");    print(c.matrix_text(region=(32, 32, 63, 63)))

finish(c)
