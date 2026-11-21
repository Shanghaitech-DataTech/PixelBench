result = new_canvas(16, 16, name="mushroomling")
colors = {
    '#': '#292333',
    'r': '#d94b4b',
    'w': '#fff0d0',
    't': '#d5a16d',
}
rows = [
    '................',
    '.....######.....',
    '...##rrrrrr##...',
    '..#rrwwrrrrrr#..',
    '.#rrrwwrrrwwrr#.',
    '.#rrrrrrrwwwrr#.',
    '.#rrwwrrrrrrrr#.',
    '.##############.',
    '....#wwwwww#....',
    '...#w##ww##w#...',
    '..##w##ww##w##..',
    '.#wtwwwwwwwwtw#.',
    '..###twwwwt###..',
    '....#wt##tw#....',
    '....###..###....',
    '................',
]
for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, p in enumerate(row):
        if p != '.':
            result.set(x, y, colors[p])
view(result, scale=24, margin=0)
finish(result)
