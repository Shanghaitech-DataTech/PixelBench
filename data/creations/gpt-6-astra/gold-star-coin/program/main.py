result = new_canvas(16, 16, name="gold-star-coin")
# Six warm metal tones, from the silhouette to the specular glint.
palette = {
    '.': None,
    'O': '#663515',
    'B': '#ab621c',
    'G': '#e6a52a',
    'Y': '#ffd65a',
    'L': '#fff0a1',
    'S': '#8c4a17',
}
rows = [
    '................',
    '.....OOOOOO.....',
    '...OOLLLLLLOO...',
    '..OLLYYYYYYGBO..',
    '..OLYYYSYYYGBO..',
    '.OLYYYSSSYYYGBO.',
    '.OLYYYSL SYYGBO.'.replace(' ', 'S'),
    '.OLYSSSLLSSSGBO.',
    '.OLYYSSLLSSYGBO.',
    '.OGYYYSLSSYYGBO.',
    '.OGYYSSSSSYYGBO.',
    '..OGYSYYYSYGBO..',
    '..OBGGYYYYGBBO..',
    '...OOBBBBBBOO...',
    '.....OOOOOO.....',
    '................',
]
for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, char in enumerate(row):
        if char != '.':
            result.set(x, y, palette[char])
# Recut the inset as a crisp, balanced five-point star.
for y in range(4, 12):
    for x in range(3, 12):
        if rows[y][x] in ('S', 'L'):
            result.set(x, y, palette['Y'])
star = [
    '....S....',
    '....S....',
    '...SSS...',
    'SSSSSSSSS',
    '.SSSSSSS.',
    '..SSSSS..',
    '..SS.SS..',
    '.SS...SS.',
]
for dy, row in enumerate(star):
    for dx, char in enumerate(row):
        if char == 'S':
            result.set(3 + dx, 4 + dy, palette['S'])
view(result, scale=24)
finish(result)
