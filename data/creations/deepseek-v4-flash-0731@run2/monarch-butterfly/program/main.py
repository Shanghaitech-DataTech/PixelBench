from pixelbench_api import *

ORANGE = (235, 128, 34)
DARK   = (178, 88, 10)
BLACK  = (18, 14, 18)
WHITE  = (246, 242, 232)

rows16 = [
    "."*7 + "k" + "."*8,
    "."*7 + "k" + "."*8,
    "."*7 + "k" + ".." + "kkk" + "...",
    "."*8 + "kkkkk" + "...",
    "."*5 + "kkkkkkkkk" + "..",
    "...." + "kk" + "oooooo" + "kk" + "..",
    ".." + "kkk" + "ooooooo" + "kk" + "..",
    ".." + "kkk" + "ooooooo" + "kk" + "..",
    ".." + "kkkk" + "oooooo" + "k" + "o" + "kk",
    ".." + "kkkk" + "ooooo" + "kkkkk",
    ".." + "kkkk" + "ooooo" + "kkkkk",
    ".." + "kkk" + "oooooo" + "kkkkk",
    ".." + "kkk" + "ooooo" + "kkkkkk",
    ".." + "kk" + "oooooo" + "kkkkkk",
    ".." + "kk" + "ooooo" + "kkkkkkk",
    ".." + "kk" + "ooooo" + "kkkkkkk",
    "...." + "kk" + "oooooo" + "kk" + "kk",
    "....." + "kk" + "ooooo" + "kk" + "kk",
    "......" + "kk" + "oooo" + "kk" + "kk",
    "......." + "kk" + "ooo" + "kk" + "kk",
    "........" + "kk" + "o" + "kkkkk",
    "........." + "k" + "o" + "kkkkk",
    ".........." + "kkkk" + "kk",
    "..........." + "kkk" + "kk",
    ".............." + "kk",
    "..............." + "k",
    "."*16,
    "."*16,
    "."*16,
    "."*16,
    "."*16,
    "."*16,
]
assert len(rows16) == 32, ("row count", len(rows16))
for i, s in enumerate(rows16):
    assert len(s) == 16, (i, s, len(s))

c = new_canvas(32, 32)
cmap = {"o": ORANGE, "k": BLACK, "w": WHITE, "d": DARK, ".": None}
for y, lr in enumerate(rows16):
    row = lr + lr[::-1]
    for x, ch in enumerate(row):
        col = cmap[ch]
        if col is not None:
            c.set(x, y, col)

# antenna + veins through the upper wing (left-side coords, mirrored)
for x, y in [(9,5),(10,6),(11,7),(8,9),(7,11),(6,13),(8,7),(9,10)]:
    c.set(x, y, BLACK)
    c.set(31 - x, y, BLACK)
# white spots in the black wing margins
for x, y in [(4,5),(3,7),(4,9),(3,6),(2,8),(5,17),(7,19),(6,18)]:
    c.set(x, y, WHITE)
    c.set(31 - x, y, WHITE)
# abdomen dots
for x, y in [(13,17),(13,19),(14,20)]:
    c.set(x, y, WHITE)
    c.set(31 - x, y, WHITE)
# dark shading on the orange
for x, y in [(6,10),(7,9),(8,7),(9,13),(8,15),(5,8),(6,8),(5,11)]:
    c.set(x, y, DARK)
    c.set(31 - x, y, DARK)

c.shift(0, 3)

print(c.stats_text())
print(c.matrix_text())

finish(c)
