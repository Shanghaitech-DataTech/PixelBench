# Minecraft-style cracked stone block, 16x16, seamless tile, 6 colours.

PAL = {
    '.': '#7e7e7e',  # base stone
    'l': '#8c8c8c',  # light patch
    'L': '#999999',  # highlight
    'd': '#6f6f6f',  # dark patch
    'D': '#5c5c5c',  # darkest patch
    'k': '#3f3f3f',  # crack
}

# 16 rows x 16 cols. The main crack runs diagonally from the top edge
# down-right, exits the right edge, re-enters at the left edge and exits
# the bottom edge exactly where it enters at the top -> seamless wrap.
# A branch fork exits right/left the same way.
ROWS = [
    "d..k..d...lLLldd",
    ".d..k.d...lLLld.",
    "..d..kk....lLld.",
    "...d...k..d...dd",
    ".lk.d..kk..ll...",
    "lkL..d..kk.....l",
    "k...dd...kk...lk",
    "...l.dDd..k...k.",
    "..lL.dDd...k.k..",
    "....d.d..lLl.k..",
    ".....dddlLl..k..",
    "..d...d..ll..d.k",
    "k....dd..ll....k",
    ".k..d..lLl...dd.",
    "d.k....ll..d.dDd",
    "d..k.d.l..d.dd..",
]

assert all(len(r) == 16 for r in ROWS) and len(ROWS) == 16

c = new_canvas(16, 16, name="stone_cracked")
for y, row in enumerate(ROWS):
    for x, ch in enumerate(row):
        c.set(x, y, PAL[ch])

print(c.stats_text())
print(c.matrix_text())
save("stone_cracked_16", c)
finish(c)
