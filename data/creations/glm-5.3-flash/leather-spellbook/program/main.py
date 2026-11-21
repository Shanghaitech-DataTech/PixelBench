"""leather-spellbook: 32x32 RPG item portrait, 8 colours, transparent bg.

Closed grimoire, seen front-on, spine on the left:
  * dark outline with rounded corners
  * left spine: bevelled metal caps top + bottom, three raised ribs with
    cast shadows, a hinge line where spine meets cover
  * leather cover: light sheen along the top edge, dark along the bottom
  * embossed diamond sigil centred on the cover: solid dark gem with a
    light bevel along its top edges and a glint
  * cream page fore-edge on the right with two page-layer seams
  * steel L-brackets wrapping the top-right and bottom-right corners
"""

try:
    from pixelbench_api import *  # noqa: F401,F403
except Exception:
    pass

W = H = 32
grid = [["."] * W for _ in range(H)]


def hline(y, x0, x1, ch):
    for x in range(x0, x1 + 1):
        grid[y][x] = ch


def vline(x, y0, y1, ch):
    for y in range(y0, y1 + 1):
        grid[y][x] = ch


def body(y, spec):
    """Fill x=4..27 (24 px) from (char, width) segments."""
    x = 4
    for ch, n in spec:
        for _ in range(n):
            grid[y][x] = ch
            x += 1
    assert x == 28, (y, x)


# ------------------------------------------------------------- outline
hline(4, 4, 27, "O")
hline(28, 4, 27, "O")
vline(3, 5, 27, "O")
vline(28, 5, 27, "O")
# corners (3,4) (28,4) (3,28) (28,28) left transparent -> rounded

# ------------------------------------------------------------- body rows
SPINE_FLAT   = [("H", 1), ("A", 4)]   # flat leather + lit left edge
SPINE_RIB    = [("H", 5)]             # raised rib, catches light
SPINE_GROOVE = [("S", 5)]             # shadow cast under a rib
HINGE        = ("S", 1)               # spine / cover seam
COVER        = ("A", 16)              # cover leather
PAGES        = [("p", 1), ("q", 1)]   # fore-edge + its shade

body(5,  [("m", 5), ("H", 15), ("m", 4)])                    # cap / bracket bar
body(6,  [("m", 1), ("d", 3), ("m", 1), ("H", 15), ("m", 4)])
body(7,  [("d", 5), ("A", 17), ("m", 2)])                    # cap shadow
body(8,  SPINE_FLAT + [HINGE, COVER] + [("m", 2)])
body(9,  SPINE_RIB + [HINGE, COVER] + [("m", 2)])
body(10, SPINE_GROOVE + [HINGE, COVER] + PAGES)              # pages begin
for y in range(11, 15):
    body(y, SPINE_FLAT + [HINGE, COVER] + PAGES)
body(15, SPINE_RIB + [HINGE, COVER] + PAGES)
body(16, SPINE_GROOVE + [HINGE, COVER] + PAGES)
for y in range(17, 21):
    body(y, SPINE_FLAT + [HINGE, COVER] + PAGES)
body(21, SPINE_RIB + [HINGE, COVER] + PAGES)
body(22, SPINE_GROOVE + [HINGE, COVER] + PAGES)              # pages end
body(23, SPINE_FLAT + [HINGE, COVER] + [("m", 2)])
body(24, SPINE_FLAT + [HINGE, COVER] + [("m", 2)])
body(25, [("d", 5), ("A", 17), ("m", 2)])                    # cap shadow
body(26, [("m", 1), ("d", 3), ("m", 1), ("S", 15), ("m", 4)])
body(27, [("m", 5), ("S", 15), ("m", 4)])                    # cap / bracket bar

# ------------------------------------------------------------- sigil
CX, CY, R = 17, 16, 4
for y in range(CY - R, CY + R + 1):
    for x in range(CX - R, CX + R + 1):
        if abs(x - CX) + abs(y - CY) <= R:
            grid[y][x] = "S"                                 # dark gem
for x in range(CX - R, CX + R + 1):                          # top bevel
    for y in range(CY - R, CY + R + 1):
        if abs(x - CX) + abs(y - CY) <= R and abs(x - CX) + abs(y - 1 - CY) > R:
            grid[y][x] = "H"
grid[15][16] = "H"                                           # glint

# cast shadows under / over the right-hand corner brackets
grid[7][24] = grid[7][25] = "d"
grid[25][24] = grid[25][25] = "d"

# fore-edge detail: bracket shadow rows + dark seams between page blocks
for y in (10, 22):
    grid[y][26] = grid[y][27] = "q"
for y in (14, 18):
    grid[y][26] = grid[y][27] = "S"

# ------------------------------------------------------------- palette
PALETTE = [
    ("O", "outline",       "#1b1216"),
    ("H", "leather_light", "#a8623f"),
    ("A", "leather",       "#8a4a32"),
    ("S", "leather_dark",  "#5f2d1e"),
    ("m", "steel",         "#c9ced8"),
    ("d", "steel_dark",    "#79808e"),
    ("p", "page",          "#e8dab2"),
    ("q", "page_shade",    "#c2ae82"),
]


def build():
    global idx
    c = new_canvas(W, H, name="leather-spellbook")
    idx = {ch: c.color(hexv, name=cname) for ch, cname, hexv in PALETTE}
    for y in range(H):
        for x in range(W):
            if grid[y][x] in idx:
                c.set(x, y, idx[grid[y][x]])
    return c


c = build()

# ------------------------------------------------------------- verification
rev = {v: k for k, v in idx.items()}
mismatch = [(x, y, grid[y][x], rev.get(c.get(x, y), "."))
            for y in range(H) for x in range(W)
            if (grid[y][x] if grid[y][x] in idx else ".") != rev.get(c.get(x, y), ".")]
print("MISMATCHES:", mismatch if mismatch else "none - canvas matches design")

used = sorted({grid[y][x] for y in range(H) for x in range(W) if grid[y][x] in idx})
visible = sum(1 for y in range(H) for x in range(W) if grid[y][x] in idx)
print("colours used:", len(used), used, "| visible px:", visible)

print(c.stats_text())
for row in grid:
    print("".join(row))
finish(c)
