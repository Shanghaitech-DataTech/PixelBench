result = new_canvas(16, 16, name='mushroomling')
palette = {'#': '#282334', 'R': '#dc424b', 'W': '#fff1d2', 'T': '#c99368'}
rows = [
'................',
'.....######.....',
'...##RRRRRR##...',
'..#RRWWRRRRRR#..',
'.#RRRWWRRRWWRR#.',
'.#RWRRRRRRWWRR#.',
'.#RRRRRWWRRRRR#.',
'..############..',
'....#WWWWWW#....',
'..###W#WW#W###..',
'..#TW#WWWW#WT#..',
'..###WWWWWW###..',
'....#TWWWWT#....',
'....#TT##TT#....',
'....###..###....',
'................',
]
for y, row in enumerate(rows):
    assert len(row) == 16
    for x, ch in enumerate(row):
        if ch != '.':
            result.set(x, y, palette[ch])
view(result, scale=24)
finish(result)
