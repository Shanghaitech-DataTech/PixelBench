"""gold-star-coin: 16x16 pixel-art gold coin with a five-point star emblem.

Palette (6 visible colours, limit is 6):
  O  #6b3e0a  dark bronze outline
  L  #ffe9a3  light gold  (top-left rim light)
  G  #f6c445  main gold   (coin face)
  S  #d18f1f  shadow gold (bottom-right rim shade)
  W  #fff6dc  warm cream  (the star)
  H  #ffffff  white       (specular glint on the rim)

Coin: 14px circle, rows of width 6/8/10/12/14.../12/10/8/6.
Star: symmetric about x=7.5, centred on the face, arms on row 7.
"""

try:
    from pixelbench_api import new_canvas, view, save, finish
except Exception:
    pass  # drawing objects are preloaded in the main file

# legend: . transparent | O outline | H glint | L light | G gold | S shade | W star
GRID = [
    "................",  # row 0
    ".....OOOOOO.....",  # row 1  top cap
    "....OHLLLLLO....",  # row 2
    "...OHLLLGGGGO...",  # row 3
    "..OHLLGWWGGGGO..",  # row 4  star tip (7,8)
    ".OLLGGGWWGGGGGO.",  # row 5  star tip (7,8)
    ".OLGGGWWWWGGGGO.",  # row 6  star widens (6-9)
    ".OLGWWWWWWWWGGO.",  # row 7  star arms (4-11)
    ".OGGGWWWWWWGGSO.",  # row 8  star body (5-10)
    ".OGGGGWWWWGGGSO.",  # row 9  star waist (6-9)
    ".OGGGWWGGWWGSSO.",  # row 10 star legs (5,6 / 9,10)
    "..OGGWGGGGWGSO..",  # row 11 star leg tips (5,10)
    "...OGGGGSSSSO...",  # row 12
    "....OSSSSSSO....",  # row 13 bottom cap
    ".....OOOOOO.....",  # row 14
    "................",  # row 15
]

PALETTE = {
    "O": "#6b3e0a",
    "L": "#ffe9a3",
    "G": "#f6c445",
    "S": "#d18f1f",
    "W": "#fff6dc",
    "H": "#ffffff",
}


def validate(grid):
    """Guard against the two mistakes hand-typed grids make: wrong width and
    broken mirror symmetry (the coin and star are both centred on x=7.5)."""
    problems = []
    for y, row in enumerate(grid):
        if len(row) != 16:
            problems.append("row %d has length %d" % (y, len(row)))
    for sym in ("O", "W"):
        for y, row in enumerate(grid):
            xs = {x for x, ch in enumerate(row) if ch == sym}
            for x in xs:
                if 15 - x not in xs:
                    problems.append("%s not mirror-symmetric at (%d,%d)" % (sym, x, y))
    return problems


def star_extents(grid):
    out = []
    for y, row in enumerate(grid):
        xs = [x for x, ch in enumerate(row) if ch == "W"]
        if xs:
            out.append("row %2d: cols %d-%d  %s" % (y, min(xs), max(xs), xs))
    return out


def build():
    c = new_canvas(16, 16, background=None, name="gold-star-coin")
    idx = {ch: c.color(hexv, name=ch) for ch, hexv in PALETTE.items()}
    for y, row in enumerate(GRID):
        if len(row) != 16:
            raise ValueError("row %d has %d chars" % (y, len(row)))
        for x, ch in enumerate(row):
            if ch != ".":
                c.set(x, y, idx[ch])
    return c


c = build()
print(c.stats_text())
print(c.matrix_text())
print("star extents:")
for line in star_extents(GRID):
    print(" ", line)
problems = validate(GRID)
if problems:
    raise SystemExit("VALIDATION FAILED:\n  " + "\n  ".join(problems))
print("validation OK: widths and O/W mirror symmetry hold")
view(c, scale=16)
save("gold-star-coin", c, indexed=True)
finish(c)
