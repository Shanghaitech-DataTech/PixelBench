# Skeleton grunt - 32x32 RPG enemy
# facing left, hunched, short sword + small wooden shield, dark joint shading

PAL = {
    '.': None,            # transparent background
    'K': '#241c28',       # dark outline
    'B': '#ece0cc',       # bone light
    'D': '#b8a088',       # bone shade
    'J': '#4a3448',       # dark joint shading
    'E': '#0c0810',       # eye socket
    'T': '#f8f0e0',       # tooth
    'g': '#7c8c9c',       # steel dark (blade edge / shield boss)
    'G': '#c8d4e0',       # steel light (blade)
    'h': '#50301c',       # sword grip
    'W': '#a07040',       # wood light
    'w': '#5c3820',       # wood dark
}

ROWS = [
    "................................",
    "................................",
    ".........KKKKKK.................",
    "..gG....KKBBBBKK................",
    "..gG...KKBBBBBBKK...............",
    "..gG...KBEEBBEEBK...............",
    "..gG...KBBBEEBBBK...............",
    "..gG...KBTBBBBTBK...............",
    "..gG....KKKKKKKK................",
    "..gG.....KJBBJK.................",
    "..gG..KJBBBBBBBBJK..............",
    ".gggggBKBBBBBBBBKB..............",
    "..hhhBBKBBBBBBBBKBB.............",
    "..ggBBBKBBBBBBBBKBBwwwwwwww.....",
    ".......KDDDDDDDDKBBwWWWWWWw.....",
    ".......KBBBBBBBBKBBwWWggWWw.....",
    ".......KDDDDDDDDKBBwWWWWWWw.....",
    ".......KBBBBBBBBKBBwWWWWWWw.....",
    "........KBBBBBBKBBBwWWWWWWw.....",
    "........KJBBBBJKBBBwwwwwwww.....",
    "........KBBBBBBKBBBwwwwwwww.....",
    "........KBK.KBK.................",
    "........KDK.KDK.................",
    "........JJ..JJ..................",
    ".......KBK..KBK.................",
    ".......KBK..KBK.................",
    ".......KBK..KBK.................",
    "......KBK...KBK.................",
    "....KBBBK.KBBBK.................",
    "....KKKKK.KKKKK.................",
    "................................",
    "................................",
]

c = new_canvas(32, 32, background=None, name="skeleton_grunt")

SHIFT = 2  # center the sprite horizontally in the 32x32 canvas

for y, row in enumerate(ROWS):
    assert len(row) == 32, f"row {y} length {len(row)}"
    if SHIFT:
        row = "." * SHIFT + row[:-SHIFT]
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, PAL[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
