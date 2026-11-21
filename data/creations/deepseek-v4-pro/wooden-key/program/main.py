c = new_canvas(16, 16, name="wooden_key")

# Palette: 6 visible colours
O = c.color('#2b1a0e', name='outline')
K = c.color('#0d0703', name='keyhole')
W = c.color('#a9743f', name='wood')
S = c.color('#6f4423', name='shadow')
L = c.color('#d9a968', name='light')
H = c.color('#f2d6a8', name='highlight')

rows = [
    "................",
    "........O.......",
    "......OOOOO.....",
    ".....OLHHHLO....",
    ".....OLKKSSO....",
    "....OHHKKSSSO...",
    ".....OLWWWSO....",
    ".....OWWWSSO....",
    "......OOWOO.....",
    ".......OWO......",
    ".......OWSSO....",
    ".......OWSSO....",
    ".......OWO......",
    ".......OWSSSO...",
    ".......OSSSSO...",
    "................",
]

for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch == '.':
            continue
        col = {'O': O, 'K': K, 'W': W, 'S': S, 'L': L, 'H': H}[ch]
        c.set(x, y, col)

print(c.matrix_text())
print(c.stats_text())

finish(c)
