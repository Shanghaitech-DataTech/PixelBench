result = new_canvas(16, 16, name='mushroomling')
palette = {'.': None, 'X': '#282338', 'R': '#df4650', 'W': '#fff1d6', 'T': '#c89668'}
rows = [
'................',
'.....XXXXXX.....',
'...XXRRRRRRXX...',
'..XRRWWRRRRRRX..',
'.XRRWWWRRRWWRRX.',
'.XRRRRRRRRWWRRX.',
'.XRRWWRRRRRRRRX.',
'..XXXXXXXXXXXX..',
'....XWWWWWWX....',
'...XWXXWWXXWX...',
'..XXWXXWWXXWXX..',
'..XTWWWWWWWWTX..',
'...XXWTWWTWXX...',
'....XTXXXXTX....',
'....XXX..XXX....',
'................',
]
for y, row in enumerate(rows):
    assert len(row) == 16
    for x, pixel in enumerate(row):
        if pixel != '.':
            result.set(x, y, palette[pixel])
view(result, scale=24, margin=0)
finish(result)
