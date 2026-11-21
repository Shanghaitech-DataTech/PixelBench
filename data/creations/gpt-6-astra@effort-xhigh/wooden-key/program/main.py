result = new_canvas(16, 16, name="wooden_key")
colors = {
    'O': '#35251f',
    's': '#62402c',
    'g': '#865636',
    'm': '#ad7c4e',
    'l': '#d0a36c',
    'h': '#edcc92',
}
rows = [
    '................',
    '...OOOO.........',
    '..OhhllO........',
    '.OlOOOOlO.......',
    '.OlO..OgO.......',
    '.OmO..OmO.......',
    '.OlgOOsmO.......',
    '..OmgmllOO.OO...',
    '...OOOOsmlOlmO..',
    '.......OsglmO...',
    '........OsmO.O..',
    '.........OmlOmO.',
    '..........OgllO.',
    '...........OsOO.',
    '............O...',
    '................',
]
for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, symbol in enumerate(row):
        if symbol != '.':
            result.set(x, y, colors[symbol])
view(result, scale=24, margin=0)
finish(result)
