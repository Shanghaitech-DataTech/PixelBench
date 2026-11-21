# 16x16 "wooden key" item sprite for a detective game.
#
# An aged wooden skeleton key, standing upright, with a paper evidence
# tag tied to the bow by a length of twine - the kind of clue an
# investigator bags and labels at a crime scene.
#
# Light comes from the top-left: the highlight rims the upper-left of the
# lathe-turned bow, the shaft keeps one lit edge, and shadow pools under
# the bow hole and along the bit's lower-right edge.
#
# Grid legend:
#   a = outline (near-black warm brown silhouette)
#   b = wood shadow   c = wood mid   d = wood light   e = wood highlight
#   f = paper / twine (evidence tag + string)
#   . = transparent (free)

GRID = [
    "................",  # y0  margin
    ".........aaaaa..",  # y1  bow, rounded top edge
    "........aeeedca.",  # y2  bow, lit top band
    "........ae...ca.",  # y3  bow sides + top of the hole
    "........ac...ba.",  # y4  bow sides + hole, shaded right rim
    ".......facbbbba.",  # y5  twine on the left rim + shadowed bottom band
    "......f..aaaaa..",  # y6  bow, rounded bottom edge
    ".....f...adca...",  # y7  twine + shaft (lit left edge)
    "....f....adca...",  # y8  twine + shaft
    ".aaaaaa..adca...",  # y9  tag top edge + shaft
    ".affffa..adca...",  # y10 tag, blank paper + shaft
    ".afaafa..aaaaaa.",  # y11 tag, line of writing + bit top edge
    ".affffa..adccba.",  # y12 tag, blank paper + bit body
    ".aaaaaa..ad..ba.",  # y13 tag bottom + bit, notch cut between the teeth
    ".........aa..aa.",  # y14 shaft tip + tooth, notch open between them
    "................",  # y15 margin
]

PALETTE = [
    ("a", "outline",     "#2B190B"),
    ("b", "wood_shadow", "#6B4A2B"),
    ("c", "wood_mid",    "#96683A"),
    ("d", "wood_light",  "#C08C52"),
    ("e", "wood_hi",     "#E2B878"),
    ("f", "paper",       "#EDE6CE"),
]

c = new_canvas(16, 16, name="wooden-key")
idx = {}
for sym, nm, hexv in PALETTE:
    idx[sym] = c.color(hexv, name=nm)

for y, row in enumerate(GRID):
    if len(row) != 16:
        raise ValueError("row %d has %d chars: %r" % (y, len(row), row))
    for x, ch in enumerate(row):
        if ch == ".":
            continue
        if ch not in idx:
            raise ValueError("unknown symbol %r at (%d,%d)" % (ch, x, y))
        c.set(x, y, idx[ch])

print(c.stats_text())
print()
print(c.matrix_text())

save("wooden-key", c)
finish(c)
