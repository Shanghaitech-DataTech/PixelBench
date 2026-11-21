# 16x16 RPG enemy: small glowing jellyfish, translucent bell, dark outline
result = new_canvas(16, 16, background=None, name="glow-jellyfish")

OUTLINE = '#1e1b3a'   # dark navy-purple outline
BELL_EDGE = '#58c6f0aa'  # translucent cyan rim fill (a=170)
BELL_MID  = '#8fdff8c0'  # brighter translucent bell (a=192)
CORE      = '#c9f4ffe0'  # glowing inner core (a=224)
HILITE    = '#eafcff'    # white shine
TENT      = '#79d8f2d8'  # glowing tentacle strands (a=216)
SPECK     = '#6fe0f846'  # faint glow motes (a=70)

art = [
    "................",
    "..g..........g..",
    "......####......",
    ".....#bbbb#.....",
    "....#bwBBBb#....",
    "...#bwwBBBBb#...",
    "...#bBccccBb#...",
    "...#bBccccBb#...",
    "...#b#b#b#b#....",
    "....t.t.t.t.....",
    "....t.t.t.t.....",
    "...t..t.t..t....",
    "...t..t.t..t....",
    "...g..g.g..g....",
    "................",
    "................",
]

colors = {
    '#': OUTLINE,
    'b': BELL_EDGE,
    'B': BELL_MID,
    'c': CORE,
    'w': HILITE,
    't': TENT,
    'g': SPECK,
}

for y, row in enumerate(art):
    assert len(row) == 16, (y, row)
    for x, ch in enumerate(row):
        if ch != '.':
            result.set(x, y, colors[ch])

print(result.stats_text())
view(result)
finish(result)
