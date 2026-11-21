# A little abyssal jelly: cool bioluminescence inside an ink-dark silhouette.
result = new_canvas(16, 16, name="glow-jellyfish")
colors = {
    'O': '#10243d',       # crisp midnight-blue outline
    'D': '#183553',       # small eyes
    'b': '#25658fdf',     # transparent blue edge of the bell
    'B': '#389bbddc',
    'C': '#47dcded6',     # translucent cyan membrane
    'h': '#8cfbe9ef',
    'H': '#dcfff6',       # reflected glint
    'p': '#78bde5df',     # lilac inner organ
    'P': '#a8dbf3ef',
    'M': '#42bfbfdc',
    'g': '#3de7ec30',     # restrained one-pixel aura
}
for key, value in colors.items():
    result.color(value, name=key)
# Only the bell casts a soft, sparse halo; the background is otherwise empty.
halo = {0: range(6,10), 1: [4,5,10,11], 2:[3,12], 3:[2,13],
        4:[2,13], 5:[1,14], 6:[1,14], 7:[1,14], 8:[1,14], 9:[2,13]}
for y, xs in halo.items():
    for x in xs:
        result.set(x,y,'g')
rows = [
    '................',
    '......OOOO......',
    '....OOHHHCOO....',
    '...OHhCCCCBbO...',
    '...OhCCppCCbO...',
    '..ObhCCPPCCbbO..',
    '..ObCDCCCCDCbO..',
    '..ObCDCCCCDCbO..',
    '..ObMhhMMhhMbO..',
    '...ObOOhbOObO...',
]
for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, key in enumerate(row):
        if key != '.':
            result.set(x,y,key)
# Three short, curling tentacles.  Their pale cores have a one-pixel dark edge.
tentacles = {
    10: {3:'O',4:'h',5:'O',6:'O',7:'P',8:'O',10:'O',11:'h',12:'O'},
    11: {2:'O',3:'h',4:'O',7:'O',8:'P',9:'O',10:'O',11:'h',12:'O'},
    12: {2:'O',3:'h',4:'O',7:'O',8:'P',9:'O',11:'O',12:'h',13:'O'},
    13: {3:'O',4:'O',6:'O',7:'P',8:'O',11:'O',12:'O'},
    14: {7:'O'},
}
for y, pixels in tentacles.items():
    for x, key in pixels.items():
        result.set(x,y,key)
print(result.stats_text())
print(result.matrix_text())
finish(result)
