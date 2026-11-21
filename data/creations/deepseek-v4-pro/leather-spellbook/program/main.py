from pixelbench_api import *

W, H = 32, 32

# 8 visible colours max; transparent background is free.
PAL = {
    'O': (26, 15, 8),      # dark outline
    'D': (46, 26, 13),     # deep shadow / hinge / emboss line
    'S': (69, 37, 17),     # spine dark leather
    'L': (107, 58, 30),    # leather base
    'H': (148, 89, 44),    # leather highlight
    'K': (124, 92, 24),    # metal dark
    'M': (195, 154, 60),   # metal mid
    'G': (240, 216, 120),  # metal light
}

PREFIX = "...O"       # x0-2 transparent, x3 outline
SPINE  = "SHHS"       # x4-7 rounded spine bands
HINGE  = "D"          # x8 hinge shadow
SUFFIX = "O.."        # x29 outline, x30-31 transparent

def cov(seg):
    assert len(seg) == 20, len(seg)
    return PREFIX + SPINE + HINGE + seg + SUFFIX

top_out = "..." + "O" * 27 + ".."
dots = "." * 32

cover = []
# y5-8: top metal corner brackets
cover.append("GGGG" + "L" * 12 + "GGGG")
cover.append("GMMK" + "L" * 12 + "KMMG")
cover.append("GMKK" + "L" * 12 + "KKMG")
cover.append("GKKK" + "L" * 12 + "KKKG")
# y9-11: leather body top + stitched panel border
cover.append("D" + "L" * 18 + "D")
cover.append("D" + "L" + "D" * 16 + "L" + "D")
cover.append("D" + "L" + "D" + "H" * 14 + "D" + "L" + "D")

# y12-20: central embossed diamond emblem
diamonds = [
    "....D....",
    "...DHD...",
    "..DHHHD..",
    ".DHHHHHD.",
    "DHHHHHHHD",
    ".DHHHHHD.",
    "..DHHHD..",
    "...DHD...",
    "....D....",
]
for d in diamonds:
    cover.append("D" + "L" + "D" + "H" + "L" + d + "LL" + "H" + "D" + "L" + "D")

# y21-23: leather body bottom + stitched panel border
cover.append("D" + "L" + "D" + "H" * 14 + "D" + "L" + "D")
cover.append("D" + "L" + "D" * 16 + "L" + "D")
cover.append("D" + "L" * 18 + "D")
# y24-27: bottom metal corner brackets
cover.append("GGGG" + "L" * 12 + "GGGG")
cover.append("GMMK" + "L" * 12 + "KMMG")
cover.append("GMKK" + "L" * 12 + "KKMG")
cover.append("GKKK" + "L" * 12 + "KKKG")

rows = []
rows += [dots] * 4
rows.append(top_out)
rows += [cov(s) for s in cover]
rows.append(top_out)
rows += [dots] * 3

assert len(rows) == 32, len(rows)
for r in rows:
    assert len(r) == 32, (len(r), r)

c = new_canvas(W, H, background=None, name="spellbook")

for y, r in enumerate(rows):
    for x, ch in enumerate(r):
        if ch != '.':
            c.set(x, y, PAL[ch])

print(c.stats_text())
print(c.matrix_text(indices=False))
finish(c)
