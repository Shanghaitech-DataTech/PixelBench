W = H = 32

c = new_canvas(W, H, background=None, name="e-scooter-rider")

# char -> colour
PALETTE = {
    "K": "#16181f",  # tyre
    "H": "#9aa2ae",  # wheel hub
    "F": "#5c6472",  # stem + handlebar
    "E": "#525b66",  # deck top edge
    "D": "#383e4a",  # deck body
    "G": "#2a2118",  # handlebar grip
    "R": "#d8402f",  # helmet / deck accent
    "r": "#f4705c",  # helmet shine
    "V": "#1b1e26",  # visor
    "v": "#4f7fb5",  # visor glint
    "S": "#f3c69b",  # skin
    "J": "#2f6ecb",  # jacket
    "j": "#24539b",  # jacket shade / sleeve
    "P": "#3a4150",  # pants front leg
    "p": "#2b303b",  # pants back leg
    "B": "#1d2027",  # shoes
    "Y": "#ffd23f",  # headlight
    "y": "#ffe98a",  # light beam
    "L": "#c3ccd8",  # speed lines
    "l": "#8a93a1",  # ground dashes
}

ROWS = []


def r(*segs):
    """Place runs of chars at exact start columns."""
    line = ["."] * W
    for x0, s in segs:
        for i, ch in enumerate(s):
            line[x0 + i] = ch
    ROWS.append("".join(line))


# ---- sky ----
for _ in range(4):
    r()                                                  # y0-y3

# ---- helmet + head (leaning forward, facing right) ----
r((19, "RRR"))                                           # y4  crown
r((18, "RRrrR"))                                         # y5  shine
r((1, "LLL"), (18, "RRVVV"))                             # y6  visor top
r((18, "RVVVv"))                                         # y7  visor + glint
r((18, "RRSSS"))                                         # y8  jaw
r((19, "SS"))                                            # y9  neck

# ---- torso + arm on the handlebars ----
r((16, "JJJJJ"))                                         # y10 shoulders
r((1, "LLLL"), (15, "JJJJ"), (19, "jj"), (21, "SS"))     # y11 arm + fist
r((15, "JJJj"), (20, "G"), (21, "SS"),
  (23, "FFF"), (26, "Y"), (27, "y"))                     # y12 bar+stem+light
r((15, "jjj"), (23, "FF"), (27, "yy"))                   # y13 belly + beam
r((14, "jjj"), (23, "FF"))                               # y14 hips

# ---- legs: front leg forward, back leg trailing ----
r((13, "pp"), (16, "PP"), (23, "FF"))                    # y15
r((13, "pp"), (16, "PP"), (23, "FF"))                    # y16
r((12, "pp"), (17, "PP"), (23, "FF"))                    # y17
r((2, "LLLL"), (12, "pp"), (17, "PP"), (23, "FF"))       # y18
r((11, "pp"), (17, "PP"), (23, "FF"))                    # y19
r((11, "pp"), (17, "PP"), (23, "FF"))                    # y20
r((1, "LLLL"), (10, "BBB"), (16, "BBB"), (23, "FF"))     # y21 shoes
r((10, "BBBB"), (16, "BBBB"), (23, "FF"))                # y22 toes forward

# ---- standing deck + continuous stem/fork ----
r((10, "EEEEEEEEEEEEE"), (23, "FF"))                     # y23 deck top edge
r((7, "KKK"), (10, "RRRDDDDDDDDDD"), (23, "KKK"))        # y24 deck + fender + tyres

# ---- wheels: 7x7 rounds with light hubs ----
r((6, "KKKKK"), (22, "KKKKK"))                           # y25
r((1, "LLL"), (5, "KK"), (7, "HHH"), (10, "KK"),
  (21, "KK"), (23, "HHH"), (26, "KK"))                   # y26 + whoosh
r((5, "KK"), (7, "HHH"), (10, "KK"),
  (21, "KK"), (23, "HHH"), (26, "KK"))                   # y27
r((5, "KK"), (7, "HHH"), (10, "KK"),
  (21, "KK"), (23, "HHH"), (26, "KK"))                   # y28
r((6, "KKKKK"), (22, "KKKKK"))                           # y29

# ---- ground: dashes broken by the contact patches ----
r((1, "lllll"), (7, "KKK"), (10, "llllll"), (17, "lll"),
  (21, "ll"), (23, "KKK"), (26, "lllll"))                # y30
r((3, "ll"), (14, "ll"), (28, "ll"))                     # y31 road texture

idx = {ch: c.color(hexv, name=ch) for ch, hexv in PALETTE.items()}

for y, row in enumerate(ROWS):
    if len(row) != W:
        raise SystemExit("row %d has %d chars" % (y, len(row)))
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, idx[ch])

print(c.stats_text())
print(c.matrix_text())

finish(c)
