from pixelbench_api import *

# 16x16 detective-game magnifying glass icon

c = new_canvas(16, 16, background=None, name="magnifying_glass")

# Register the palette
colors = {
    'N': c.color('#262b44', name='outline'),      # dark navy outline
    'G': c.color('#6eb2e0', name='glass'),        # mid glass blue
    'L': c.color('#abd9f5', name='glass_light'),  # light glass blue
    'W': c.color('#ffffff', name='white'),        # specular highlight
    'K': c.color('#2e6fab', name='glass_dark'),   # dark glass blue
    'B': c.color('#f0c260', name='gold_light'),   # handle highlight
    'M': c.color('#c98a3a', name='gold'),         # handle mid brass
    'D': c.color('#8a5520', name='gold_dark'),    # handle shadow
}

rows = [
    "................",
    "................",
    "......N.........",
    "....NNLNN.......",
    "...NWWLGGN......",
    "...NWLLGGN......",
    "..NLLGGKKKN.....",
    "...NGGKKKN......",
    "...NGKKKKNNN....",
    "....NNKNNNBNN...",
    "......N..NMBNN..",
    ".........NDMBNN.",
    ".........NNDMBNN",
    "..........NNDMBN",
    "...........NNDMN",
    "............NNDN",
]

for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, colors[ch])

print(c.stats_text())
print(c.matrix_text())

save('magnifying_glass', c)
finish(c)
