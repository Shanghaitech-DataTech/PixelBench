# wooden key - 16x16 detective-game item sprite

# palette: 5 visible colours (limit 6)
COLORS = {
    "o": "#2a1a0e",   # dark outline / deep grain
    "d": "#70441f",   # shadow wood
    "m": "#9c6a34",   # mid wood
    "l": "#c6974f",   # lit wood
    "h": "#e8c88c",   # highlight
}

GRID = [
    "................",
    "......oooo......",
    "....oohhmmoo....",
    "...oohl..mdoo...",
    "...ohl....mdo...",
    "...ohl....mdo...",
    "...oohl..mdoo...",
    "....oolmmdoo....",
    "......olmdo.....",
    "......olmdo.....",
    "......olmdoooo..",
    "......olmmmmdo..",
    "......olmdoooo..",
    "......olmmdo....",
    "......olmdoo....",
    "......oooo......",
]

result = new_canvas(16, 16, name="wooden-key")
for name, hexv in COLORS.items():
    result.color(hexv, name=name)

for y, row in enumerate(GRID):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch != ".":
            result.set(x, y, ch)

# wood grain: a few darker flecks along shaft and bow
for gx, gy in [(8, 9), (8, 14)]:
    result.set(gx, gy, "d")

view(result)
print(result.stats_text())
print(result.matrix_text())
finish(result)
