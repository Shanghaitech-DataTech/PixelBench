from pixelbench_api import new_canvas, finish, save, view

c = new_canvas(16, 16, name="lab_researcher")

# palette
K = c.color("#2a2a2a")   # outline dark
H = c.color("#333338")   # black hair
F = c.color("#ffd9b8")   # skin
B = c.color("#6b3b1f")   # brown eyes
M = c.color("#d16a5a")   # mouth
C = c.color("#f4f4f4")   # white lab coat
S = c.color("#c9c9c9")   # coat shadow
N = c.color("#4b5a7a")   # navy pants/shoes

rows = [
    ".....HHHHHH.....",
    "...HHHHHHHHHH...",
    "...HHFFFFFFHH...",
    "...HFBFFFFBFH...",
    "...HFFFMMFFFH...",
    "...HHFFFFFFHH...",
    "...CCCCCCCCCC...",
    "...SCCCCCCCCS...",
    "...SLCCCCCCLS...",
    "...SLCCCCCCLS...",
    "...SCCCCCCCCS...",
    "....NNNNNNNN....",
    "....NNNNNNNN....",
    ".....KKKKKK.....",
    "................",
    "................",
]

L = c.color("#ffffff")   # coat highlight
colormap = {"H": H, "F": F, "B": B, "M": M, "C": C, "S": S, "K": K, "N": N, "L": L}

for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, colormap[ch])

# extra shading on sleeves (subtle darker on coat sides already via S)

print(c.stats_text())
print(c.matrix_text())
save("lab_researcher", c)
finish(c)
