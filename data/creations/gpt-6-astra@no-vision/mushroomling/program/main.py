result = new_canvas(16, 16, name="mushroomling")
palette = {'#': '#302237', 'R': '#dc414b', 'W': '#fff2d5', 'C': '#dfaf78'}
rows = [
    '................',
    '.....######.....',
    '...##RRRRRR##...',
    '..#RRWWRRRRRR#..',
    '.#RRRWWRRRWWRR#.',
    '.#RWRRRRRRWWRR#.',
    '#RRRRRRWWRRRRRR#',
    '#RRRRRRWWRRRRRR#',
    '.####CCCCCC####.',
    '...#CWWWWWWC#...',
    '..#CW##WW##WC#..',
    '..#CW##WW##WC#..',
    '...##CWWWWC##...',
    '.....#CCCC#.....',
    '....#CC##CC#....',
    '....###..###....',
]
for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, symbol in enumerate(row):
        if symbol in palette:
            result.set(x, y, palette[symbol])
print(result.stats_text())
print(result.matrix_text())
finish(result)
