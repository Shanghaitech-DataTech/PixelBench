"""Tile the exported stone 2x2 and print the seams as text."""
from pixelbench_api import load, new_canvas

src = load("exports/stone_cracked.pixelart.json", add=False)
print("loaded:", src.size)

tile = load("exports/stone_cracked.pixelart.json", add=True)
big = new_canvas(32, 32, background=None, name="tiled")
for ox in (0, 16):
    for oy in (0, 16):
        big.blit(tile, ox, oy)

# horizontal seam: column 15 vs column 16 (rows 0..15)
print("H seam (col15 | col16):")
for y in range(16):
    l = tile.get(15, y)
    r = tile.get(0, y)
    print(f"  y={y:2d}  {l:3d} | {r:3d}  {'DIFF' if l != r else ''}")

# vertical seam: row 15 vs row 0
print("V seam (row15 | row0):")
for x in range(16):
    t = tile.get(x, 15)
    b = tile.get(x, 0)
    print(f"  x={x:2d}  {t:3d} | {b:3d}  {'DIFF' if t != b else ''}")

print(big.stats_text())
print(big.matrix_text())
