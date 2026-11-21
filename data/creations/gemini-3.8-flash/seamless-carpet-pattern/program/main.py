# Seamless Carpet Pattern - 32x32 Pixel Art
tile = new_canvas(32, 32, name='carpet_pattern')

# Rich authentic Persian carpet palette (19 colors)
C_DARK       = '#130e12' # knot shadow
C_RED_DARK   = '#4a1017' # deep madder outline
C_RED_SHADE  = '#761821' # madder red weft shadow
C_RED_BASE   = '#8c1f2a' # classic madder red
C_RED_WARM   = '#ab2b32' # warm ruby red
C_RED_BRIGHT = '#d44738' # vermilion / bright coral

C_NAVY_DARK  = '#0e1422' # deep night navy shadow
C_NAVY_SHADE = '#172238' # navy weft shadow
C_NAVY_BASE  = '#1f2e4c' # classic indigo navy
C_BLUE_ACC   = '#4a6d9e' # persian turquoise / soft blue accent

C_GOLD_DARK  = '#5e370e' # dark bronze gold
C_GOLD_BASE  = '#b87c26' # warm antique gold
C_GOLD_LIGHT = '#e3a435' # bright saffron gold
C_GOLD_PALE  = '#f8d16d' # radiant yellow gold

C_IVORY_SHADE= '#baae9a' # ivory weft shadow
C_IVORY_BASE = '#ded4bf' # warm ivory wool
C_IVORY_LIGHT= '#eee5d3' # bright cream wool
C_WHITE_ACC  = '#fcf9f2' # pure wool knot highlight

C_GRN_BASE   = '#265236' # forest green
C_GRN_LIGHT  = '#447f57' # sage leaf green

def set4(c, x, y, col):
    c.set(x, y, col)
    c.set(31 - x, y, col)
    c.set(x, 31 - y, col)
    c.set(31 - x, 31 - y, col)

def set8(c, x, y, col):
    set4(c, x, y, col)
    set4(c, y, x, col)

# 1. Base diamond zones
for y in range(16):
    for x in range(16):
        dc = (15.5 - x) + (15.5 - y)
        if dc < 13:
            col = C_RED_BASE
        elif dc == 13:
            col = C_GOLD_DARK
        elif dc < 18:
            col = C_IVORY_LIGHT
        elif dc == 18:
            col = C_GOLD_DARK
        else:
            col = C_NAVY_BASE
        set4(tile, x, y, col)

# 2. Floral border detailing (dc=13 to 18)
# Diagonal rosettes:
set8(tile, 7, 7, C_RED_WARM)
set8(tile, 8, 8, C_RED_WARM)
set8(tile, 7, 8, C_GOLD_PALE)
set8(tile, 8, 7, C_GOLD_LIGHT)
set8(tile, 6, 8, C_GRN_BASE)
set8(tile, 8, 6, C_GRN_BASE)
set8(tile, 9, 7, C_GRN_BASE)
set8(tile, 7, 9, C_GRN_BASE)
set8(tile, 6, 7, C_IVORY_BASE)
set8(tile, 7, 6, C_IVORY_BASE)

# Floral buds halfway down diagonal:
set8(tile, 11, 4, C_RED_BRIGHT)
set8(tile, 12, 4, C_GOLD_LIGHT)
set8(tile, 11, 5, C_GRN_BASE)
set8(tile, 10, 5, C_GRN_LIGHT)
set8(tile, 12, 3, C_IVORY_BASE)

# Connecting vine nodes:
set8(tile, 13, 2, C_GRN_BASE)
set8(tile, 9, 6, C_GRN_LIGHT)
set8(tile, 10, 6, C_IVORY_BASE)

# Apex floral clasp connecting the diamond borders seamlessly across edges:
set8(tile, 15, 0, C_GOLD_PALE)
set8(tile, 14, 0, C_RED_BRIGHT)
set8(tile, 15, 1, C_RED_WARM)
set8(tile, 14, 1, C_GRN_BASE)
set8(tile, 13, 1, C_IVORY_BASE)
set8(tile, 15, 2, C_GOLD_DARK)

# Inner serrated frame of floral border (dc=13):
for p in [(15, 3), (13, 5), (11, 7), (9, 9), (7, 11), (5, 13), (3, 15)]:
    set8(tile, p[0], p[1], C_GOLD_BASE)
for p in [(14, 4), (12, 6), (10, 8), (8, 10), (6, 12), (4, 14)]:
    set8(tile, p[0], p[1], C_RED_DARK)

# Outer serrated frame of floral border (dc=18):
for p in [(13, 0), (11, 2), (9, 4), (7, 6), (5, 8), (3, 10), (1, 12)]:
    set8(tile, p[0], p[1], C_GOLD_BASE)
for p in [(12, 1), (10, 3), (8, 5), (6, 7), (4, 9), (2, 11), (0, 13)]:
    set8(tile, p[0], p[1], C_NAVY_DARK)

# 3. CENTER RED DIAMOND MOTIFS:
# Central 8-pointed star / medallion:
set8(tile, 15, 15, C_GOLD_PALE)
set8(tile, 14, 15, C_GOLD_LIGHT)
set8(tile, 15, 14, C_GOLD_LIGHT)
set8(tile, 14, 14, C_RED_DARK)

set8(tile, 13, 15, C_WHITE_ACC)
set8(tile, 15, 13, C_WHITE_ACC)
set8(tile, 13, 14, C_RED_BRIGHT)
set8(tile, 14, 13, C_RED_BRIGHT)

set8(tile, 13, 13, C_GOLD_LIGHT)
set8(tile, 12, 14, C_RED_DARK)
set8(tile, 14, 12, C_RED_DARK)

# Medallion stepped frame (dc=5 to 6):
set8(tile, 12, 15, C_GOLD_BASE)
set8(tile, 15, 12, C_GOLD_BASE)
set8(tile, 12, 13, C_WHITE_ACC)
set8(tile, 13, 12, C_WHITE_ACC)
set8(tile, 11, 14, C_RED_DARK)
set8(tile, 14, 11, C_RED_DARK)
set8(tile, 11, 15, C_RED_DARK)
set8(tile, 15, 11, C_RED_DARK)

# Floating floral sprigs in red field:
set8(tile, 10, 10, C_BLUE_ACC)
set8(tile, 11, 10, C_WHITE_ACC)
set8(tile, 10, 11, C_WHITE_ACC)
set8(tile, 11, 11, C_GRN_BASE)
set8(tile, 10, 9, C_RED_BRIGHT)
set8(tile, 9, 10, C_RED_BRIGHT)

# Cypress / palmette:
set8(tile, 15, 8, C_GOLD_LIGHT)
set8(tile, 15, 7, C_WHITE_ACC)
set8(tile, 14, 8, C_GRN_BASE)
set8(tile, 14, 7, C_RED_DARK)

# 4. CORNER NAVY DIAMOND MOTIFS:
# Corner star medallion (combines across tile corners when tiled):
set8(tile, 0, 0, C_GOLD_PALE)
set8(tile, 1, 0, C_GOLD_LIGHT)
set8(tile, 0, 1, C_GOLD_LIGHT)
set8(tile, 1, 1, C_RED_BRIGHT)
set8(tile, 2, 0, C_WHITE_ACC)
set8(tile, 0, 2, C_WHITE_ACC)
set8(tile, 2, 1, C_IVORY_LIGHT)
set8(tile, 1, 2, C_IVORY_LIGHT)
set8(tile, 2, 2, C_GOLD_LIGHT)
set8(tile, 3, 0, C_GOLD_BASE)
set8(tile, 0, 3, C_GOLD_BASE)
set8(tile, 3, 1, C_NAVY_DARK)
set8(tile, 1, 3, C_NAVY_DARK)

# Floating floral motifs in navy field:
set8(tile, 4, 4, C_RED_BRIGHT)
set8(tile, 5, 4, C_GOLD_LIGHT)
set8(tile, 4, 5, C_GOLD_LIGHT)
set8(tile, 5, 5, C_GRN_BASE)
set8(tile, 3, 4, C_WHITE_ACC)
set8(tile, 4, 3, C_WHITE_ACC)

set8(tile, 0, 5, C_RED_WARM)
set8(tile, 0, 6, C_GOLD_LIGHT)
set8(tile, 1, 5, C_GRN_BASE)

set8(tile, 5, 0, C_RED_WARM)
set8(tile, 6, 0, C_GOLD_LIGHT)
set8(tile, 5, 1, C_GRN_BASE)

# 5. Global continuous woven texture (warp/weft knotting effect)
# Guarantees mathematical continuity across all tile edges (x%32, y%32)
idx_red = tile.color(C_RED_BASE)
idx_navy = tile.color(C_NAVY_BASE)
idx_ivory = tile.color(C_IVORY_LIGHT)

for y in range(32):
    for x in range(32):
        c_idx = tile.get(x, y)
        is_weft = ((x + y) % 2 == 1)
        if is_weft:
            if c_idx == idx_red:
                tile.set(x, y, C_RED_SHADE)
            elif c_idx == idx_navy:
                tile.set(x, y, C_NAVY_SHADE)
            elif c_idx == idx_ivory:
                tile.set(x, y, C_IVORY_SHADE)

view(tile)
finish(tile)
