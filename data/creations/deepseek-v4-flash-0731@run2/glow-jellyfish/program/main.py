from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16, name="glow-jellyfish")

# Palette
O = (8, 14, 34, 255)          # dark navy outline
G = (96, 200, 255, 92)        # outer glow (faint)
B = (70, 160, 235, 175)       # translucent bell mid
W = (150, 225, 255, 215)      # translucent bell bright
H = (235, 250, 255, 235)      # soft highlight
T = (168, 182, 255, 200)      # translucent tentacles

P = (42, 100, 180, 70)        # faint water particles

rows = [
    ".p...GGGGGG.....",
    "....GGOOOOGG....",
    "...GOBBBBBBOG...",
    "..GOBWWWWWWBOG..",
    "..OBWHHWWWWWBO..",
    "..OBWWWWWWWWBO..",
    "..OBWWHHWWWWBO..",
    "..p.OBWWWWWWBO..",
    "....OBBBBBBO....",
    ".....OOOOOO.....",
    "....TTTTTTTT....",
    "...T..T..T.T....",
    "...T..T...T.....",
    "....T..T........",
    ".....T..........",
    "................",
]

for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, {"O": O, "G": G, "B": B, "W": W, "H": H, "T": T, "p": P}[ch])

print(c.stats_text())
print(c.matrix_text())

finish(c)
