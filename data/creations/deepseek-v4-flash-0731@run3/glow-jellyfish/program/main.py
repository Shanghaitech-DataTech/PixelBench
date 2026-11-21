from pixelbench_api import new_canvas, finish

W = H = 16
c = new_canvas(W, H, name="glow-jellyfish")

# Palette (cyan jellyfish glowing in deep water, transparent background)
colors = {
    '.': None,
    'O': (6, 16, 34, 255),      # dark navy outline
    'D': (16, 82, 116, 190),    # deep interior of the bell
    'M': (38, 150, 182, 205),   # mid bell (translucent)
    'L': (96, 214, 232, 215),   # light bell
    'H': (208, 250, 255, 255),  # bright highlight
    'T': (84, 204, 224, 230),   # tentacles
    't': (168, 244, 255, 245),  # glowing tentacle tips
    'G': (110, 200, 225, 110),  # soft outer glow
    'S': (190, 240, 250, 170),  # bubbles / sparkles
}

rows = [
    "................",
    "......OLLO......",
    ".....OLHLLO.....",
    "....OMLHLMMO....",
    "...OMLLHLMMMO...",
    "...OMMLLLMMMO...",
    "...OMMLLLMMMO...",
    "....ODDDDDDO....",
    "....T.T.T.T.....",
    "...T..T..T.T....",
    "....TT.TT.T.....",
    "....T..T.T.T....",
    "...t..t.t.t.....",
    ".....t.t.t......",
    "......t....t....",
    "................",
]

glow = [(5, 0), (10, 0), (3, 2), (12, 2), (2, 4), (13, 4),
        (2, 6), (13, 6), (5, 8), (11, 8)]
bubbles = [(1, 1), (14, 4), (1, 9), (13, 13)]

for y, row in enumerate(rows):
    assert len(row) == W, (y, len(row), row)
    for x, ch in enumerate(row):
        col = colors[ch]
        if col is not None:
            c.set(x, y, col)
for x, y in glow:
    c.set(x, y, colors['G'])
for x, y in bubbles:
    c.set(x, y, colors['S'])

print(c.stats_text())
print(c.matrix_text())

finish(c)
