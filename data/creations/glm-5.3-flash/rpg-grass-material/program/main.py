"""rpg-grass-material: a 16x16 seamless RPG-style grass material tile.

Design
------
* mid-green field with interleaved dark / light speckles; no two speckles of
  the same tone touch orthogonally, even across the tile seam
* three tiny yellow flowers: one plus-shaped with an orange centre, two 2x2
* five small darker grass tufts drawn as three-pixel carets
* two sparse bare-dirt patches with a darker shadow pixel on the corner
* the tuft at the right edge wraps onto the left edge, so the pattern
  repeats without a seam
"""

W = H = 16

# --- palette -------------------------------------------------------------
BASE   = "#4e9c3f"   # mid grass green (field)
LIGHT  = "#7ecb58"   # light green speckle
DARK   = "#37782b"   # dark green speckle
TUFT   = "#265a1f"   # darker grass tufts
YELLOW = "#f4d84a"   # flower petals
CENTER = "#d99b2e"   # flower centre
DIRT   = "#9c7a52"   # bare dirt
DIRTD  = "#71532f"   # dirt shadow corner

CHAR = {".": BASE, "l": LIGHT, "d": DARK, "t": TUFT,
        "y": YELLOW, "o": CENTER, "D": DIRT, "E": DIRTD}

# --- grid ----------------------------------------------------------------
grid = [["." for _ in range(W)] for _ in range(H)]


def put(x, y, ch):
    x, y = x % W, y % H
    assert grid[y][x] == ".", f"overwrite at {(x, y)}: {grid[y][x]} -> {ch}"
    grid[y][x] = ch


def tuft(x, y):
    """Three-pixel caret: apex on top, two legs below."""
    put(x - 1, y + 1, "t")
    put(x, y, "t")
    put(x + 1, y + 1, "t")


def flower(x, y):
    """Plus-shaped blossom with a darker centre pixel."""
    put(x, y - 1, "y")
    put(x - 1, y, "y")
    put(x, y, "o")
    put(x + 1, y, "y")
    put(x, y + 1, "y")


def cluster(x, y):
    """2x2 pair of tiny blossoms."""
    for dx in (0, 1):
        for dy in (0, 1):
            put(x + dx, y + dy, "y")


def patch(x, y):
    """2x3 bare-dirt patch, darker at its lower-right corner."""
    for dx in range(3):
        put(x + dx, y, "D")
        put(x + dx, y + 1, "E" if dx == 2 else "D")


# --- features ------------------------------------------------------------
tuft(9, 1)
tuft(2, 4)
tuft(14, 6)
tuft(5, 10)
tuft(15, 12)          # legs at (14,13) and (16,13) -> wraps to (0,13)

flower(6, 7)
cluster(1, 8)
cluster(12, 9)

patch(5, 2)
patch(10, 12)

# --- speckles ------------------------------------------------------------
LIGHTS = [
    (5, 0), (0, 1), (12, 1), (2, 2), (0, 3), (6, 4), (13, 4), (5, 5),
    (11, 5), (3, 6), (12, 6), (1, 7), (4, 8), (5, 9), (8, 10), (1, 11),
    (12, 11), (5, 12), (3, 13), (8, 13), (4, 14), (10, 14), (0, 15), (9, 15),
]
DARKS = [
    (2, 0), (10, 0), (4, 1), (12, 2), (9, 3), (0, 4), (10, 4), (8, 5),
    (0, 6), (9, 6), (3, 7), (0, 8), (9, 8), (8, 9), (15, 9), (1, 10),
    (10, 10), (9, 11), (15, 11), (2, 12), (8, 12), (6, 13), (1, 14),
    (7, 14), (5, 15), (12, 15),
]
for x, y in LIGHTS:
    put(x, y, "l")
for x, y in DARKS:
    put(x, y, "d")

# --- checks --------------------------------------------------------------
def contacts():
    """Orthogonally adjacent same-symbol pairs, wrapping at the edges."""
    bad = []
    for y in range(H):
        for x in range(W):
            here = grid[y][x]
            if here == "." or here in "Dy":
                continue
            for nx, ny, tag in (((x + 1) % W, y, "H"), (x, (y + 1) % H, "V")):
                if grid[ny][nx] == here:
                    bad.append((tag, x, y, here))
    return bad

problems = contacts()
print("same-tone orthogonal contacts (should be []):", problems)
assert not problems, problems

counts = {}
for row in grid:
    for ch in row:
        counts[ch] = counts.get(ch, 0) + 1
print("symbol counts:", dict(sorted(counts.items())))

# --- draw ----------------------------------------------------------------
tile = new_canvas(W, H, background=None, name="rpg-grass-material")
for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        tile.set(x, y, CHAR[ch])

print(tile.stats_text())
print(tile.matrix_text())

# --- seamless tiling check (inspection only) -----------------------------
big = new_canvas(W * 3, H * 3, background=None, name="tiled-check")
for ty in range(3):
    for tx in range(3):
        big.blit(tile, tx * W, ty * H)
for label, region in [
    ("vertical seam x=16", (12, 8, 21, 14)),
    ("horizontal seam y=16", (8, 12, 14, 21)),
    ("corner (16,16)", (13, 13, 20, 20)),
]:
    print(f"--- 3x3 tiling, {label} ---")
    print(big.matrix_text(region=region))

written = save("rpg-grass-material", tile)
print("saved:", written)
print("palette:", [(e["index"], e["name"], e["rgba"]) for e in tile.palette()])

finish(tile)
