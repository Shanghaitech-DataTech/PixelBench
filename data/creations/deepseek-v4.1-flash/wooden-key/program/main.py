from pixelbench_api import *

c = new_canvas(16, 16, name="wooden-key")

# 5 colours only (limit is 6)
pal = {
    'k': '#2a1a12',  # near-black brown outline
    'd': '#6b4226',  # dark wood
    'm': '#b0722f',  # mid wood
    'l': '#dfa964',  # light wood
    'h': '#f7dcab',  # highlight
}

grid = [
    ".....kkkkk......",   # 0  bow top edge
    "....khllmdk.....",   # 1
    "...khllmmddk....",   # 2
    "...klm...ddk....",   # 3  hole starts
    "...klm...ddk....",   # 4
    "...kmm...ddk....",   # 5
    "...kmmmddddk....",   # 6
    "....kmmddk......",   # 7
    ".....kkkkk......",   # 8  bow bottom edge
    "......klkkkk....",   # 9  shaft + top of tooth 1
    "......klkddk....",   # 10 tooth 1
    "......klkddk....",   # 11
    "......kmkkkk....",   # 12 notch
    "......kmkddk....",   # 13 tooth 2
    "......kmkddk....",   # 14
    "......kkkkkk....",   # 15 bottom edge
]

for y, row in enumerate(grid):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, pal[ch])

print(c.stats_text())
print(c.matrix_text())
save("wooden-key", c)
finish(c)
