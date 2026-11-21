from pixelbench_api import new_canvas, finish

# 16x16 RPG chibi: female lab researcher, black hair, brown eyes, white lab coat.
rows = [
    "....HHHHHHHH....",
    "...HHHHLLHHHH...",
    "..HHHHHHHHHHHH..",
    "..HHSSSSSSSSHH..",
    "..HHHHSSSSHHHH..",
    "..HHSEESSEESHH..",
    "..HHSSSSSSSSHH..",
    "..HHSSSSPPSSHH..",
    "..HHSSSSSSSSHH..",
    "...WWBBBBBBWW...",
    "..WWWBBBBBBWWW..",
    "..WWWWWWWWWWWW..",
    "..WWWWrrWWWWWW..",
    "..SSWWWWWWWWSS..",
    "..SSwwwwwwwwSS..",
    "...bbbbbbbbbb...",
]

cmap = {
    ".": None,
    "H": "#2b2b33",   # black hair
    "L": "#4d4d5c",   # hair shine
    "S": "#f6c89a",   # skin
    "E": "#5f3d1e",   # brown eyes
    "P": "#e0707a",   # mouth
    "W": "#f2f2f2",   # white lab coat
    "w": "#c9c9c9",   # coat shading
    "B": "#5d84bd",   # blue shirt
    "r": "#d05050",   # pocket pen
    "b": "#4e4e5a",   # shoes
}

c = new_canvas(16, 16)

for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row), row)
    for x, ch in enumerate(row):
        col = cmap[ch]
        if col is not None:
            c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text())
finish(c)
