# 16x16 magnifying glass icon - detective game pixel art.
#
# Layout: a 10px lens in the upper-left (dark outline, 1px silver rim lit from
# the top-left, blue glass with a white glint upper-left and a deeper blue
# inner shadow along the right/bottom), and a wooden grip running diagonally
# to the bottom-right corner.
#
# The lens ring is a true circle raster (row widths 4,8,8,10,10,10,10,8,8,4)
# centred between pixels 5/6, so the 45-degree handle axis lines up with the
# lens centre. The handle is a fully outlined 4px band ('o l b o': outline,
# lit wood, wood, outline) so no wood pixel ever touches transparency, and its
# first outline pixel is shared with the ring's bottom edge so the joint is
# seamless.

GRID = [
    "................",
    "....oooo........",
    "..oommmmoo......",
    "..omwwgeno......",
    ".omwggggeno.....",
    ".omwggggeno.....",
    ".omgggggeno.....",
    ".omeggggeno.....",
    "..oneeeeno......",
    "..oonnnnooo.....",
    "....oooo........",
]

PALETTE = [
    ("o", "outline",    "#1a1c2c"),
    ("m", "rim-light",  "#c3ccdb"),
    ("n", "rim-shade",  "#7e8ca3"),
    ("g", "glass",      "#a8dff5"),
    ("e", "glass-deep", "#6cb6dd"),
    ("w", "glint",      "#ffffff"),
    ("l", "wood-light", "#bf8143"),
    ("b", "wood",       "#9a5f2b"),
]

c = new_canvas(16, 16, background=None, name="magnifying-glass")

idx = {}
for ch, name, hexv in PALETTE:
    idx[ch] = c.color(hexv, name=name)

for y, row in enumerate(GRID):
    if len(row) != 16:
        raise ValueError("row %d has %d chars" % (y, len(row)))
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, idx[ch])

# Wooden grip: a 4px-wide diagonal band from the lens down to the corner.
# Row y spans x = y-3 .. y as: outline, lit wood, wood, outline.
for i in range(6):
    y = 10 + i
    c.set(7 + i, y, idx["o"])   # left edge (shares a pixel with the ring)
    c.set(8 + i, y, idx["l"])   # lit side, facing the top-left light
    c.set(9 + i, y, idx["b"])   # core wood
    c.set(10 + i, y, idx["o"])  # right edge

print(c.stats_text())
print(c.matrix_text())

save("magnifying-glass", c)
finish(c)
