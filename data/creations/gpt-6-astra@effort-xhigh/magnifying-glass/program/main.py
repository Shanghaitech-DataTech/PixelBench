result = new_canvas(16, 16, name="magnifying_glass")

# A compact brass magnifier, with a reflected light in the blue lens.
palette = {
    '.': None,
    'o': '#242934',  # continuous dark silhouette
    'b': '#91603c',  # shaded brass
    'a': '#d6a45e',  # brass
    'h': '#ffe2a0',  # polished upper edge
    's': '#518c9c',  # glass edge
    'l': '#83bdca',  # glass
    'g': '#bce4e5',  # illuminated glass
    'w': '#f4f8ec',  # reflection
    'd': '#523c3e',  # handle shadow
    'm': '#92604b',  # warm leather
    'n': '#c68a5d',  # handle highlight
}
rows = [
    '................',
    '....ooooo.......',
    '..oohhhhhoo.....',
    '..ohgggggao.....',
    '.ohgwwlllsao....',
    '.ohgwglllsao....',
    '.ohglllllsao....',
    '.oaglllllsbo....',
    '.oalllllssbo....',
    '..oasssssbo.....',
    '..oobbbbbaoo....',
    '....oooooonmo...',
    '..........onmo..',
    '...........onmo.',
    '............odo.',
    '.............o..',
]
for y, row in enumerate(rows):
    assert len(row) == 16
    for x, key in enumerate(row):
        if key != '.':
            result.set(x, y, palette[key])
view(result, scale=24, margin=1, edges="all")
save("magnifying-glass", result)
finish(result)
