# 16x16 seamless RPG grass material tile
# Features: interleaved dark/light green speckles, tiny yellow flowers,
# small darker grass tufts, sparse bare-dirt patches. All shapes are kept
# complete within the tile (no half-shapes at borders) so it tiles seamlessly.

PALETTE = {
    "G": "#58a03c",  # base grass green
    "d": "#3d7a27",  # dark green speckle
    "l": "#7cc24e",  # light green speckle
    "t": "#2e5c1c",  # darker grass tuft
    "D": "#8a6238",  # bare dirt
    "X": "#6b4526",  # dark dirt centre
    "y": "#f2d23e",  # yellow flower
    "Y": "#ffe97a",  # flower highlight
}

GRID = [
    "GlGGdGGGlGGdGGlG",
    "GGdGGGyYGtdGGGGG",
    "GGtGlGGGtttGGdGG",
    "GtttGdGGGGGlGGGG",
    "GGGyGGGlGGGGGtGG",
    "lGGGGdGGGGGdtttG",
    "GGdGGGGGGDDGGGGG",
    "GGGGGtGGDXDGlGGG",
    "GdGlGtGGDDGGGGyY",
    "GGGGGGdGGGGtGGGG",
    "GGyGGGGGlGGtGGdG",
    "GtGGdGGGGGGGGGGG",
    "tttGGGlGGdGDDGGG",
    "GGdGGGGGyGGGlGGG",
    "GlGGGtGGGGdGGGGG",
    "GGGdGGGlGGGGGdGG",
]

result = new_canvas(16, 16, background=PALETTE["G"], name="grass_tile")
for y, row in enumerate(GRID):
    assert len(row) == 16, (y, row)
    for x, ch in enumerate(row):
        if ch != "G":
            result.set(x, y, PALETTE[ch])

# 3x3 tiled preview to verify seamlessness (working canvas, not submitted)
tiled = new_canvas(48, 48, name="tiled_preview")
for ty in range(3):
    for tx in range(3):
        tiled.blit(result, tx * 16, ty * 16)

print(result.stats_text())
view(result, scale=16)
view(tiled, scale=8)
finish(result)
