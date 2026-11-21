c = new_canvas(32, 32, background=None, name="dim_sum_chef")

# Register the palette (colour names travel with the drawing state)
W = c.color((245, 244, 240), "white")
C = c.color((196, 176, 150), "apron_cream")
S = c.color((238, 176, 142), "skin")
B = c.color((52, 44, 48), "dark")
T = c.color((210, 154, 90), "bamboo")
D = c.color((158, 108, 60), "bamboo_shadow")
U = c.color((240, 226, 204), "bun")

cmap = {'W': W, 'C': C, 'S': S, 'B': B, 'T': T, 'D': D, 'U': U}

rows = [
    "................................",
    "..........WWWWWWWWWWWW..........",
    ".........WWWWWWWWWWWWWW.........",
    "........WWWWWWWWWWWWWWWW........",
    "........WWWWWWWWWWWWWWWW........",
    ".........WWWWWWWWWWWWWW.........",
    "..........CCCCCCCCCCCC..........",
    "..........SSSSSSSSSSSS..........",
    "..........SSSSSSSSSSSS..........",
    "..........SSSSSSSSSSSS..........",
    "..........SSBBSSSSBBSS..........",
    "..........SSSSSSSSSSSS..........",
    "...........SSSSSSSSSS...........",
    "...........SSSBBBBSSS...........",
    "............SSSSSSSS............",
    ".............SSSSSS.............",
    ".....WWWWCCCUUCCCCUUCCCWWWW.....",
    ".....WWWWCCUUUUCCUUUUCCWWWW.....",
    "..SSSWWWWCCUUUUCCUUUUCCWWWWSSS..",
    "..SSSTTTTTTTTTTTTTTTTTTTTTTSSS..",
    "..SSSTTTTTTTTTTTTTTTTTTTTTTSSS..",
    "..SSSDDDDDDDDDDDDDDDDDDDDDDSSS..",
    "..SSSTTTTTTTTTTTTTTTTTTTTTTSSS..",
    "..SSSDDDDDDDDDDDDDDDDDDDDDDSSS..",
    ".....WWWWCCCCCCCCCCCCCCWWWW.....",
    ".....WWWWCCCCCCCCCCCCCCWWWW.....",
    ".....WWWWCCCCCCCCCCCCCCWWWW.....",
    ".......WWWCCCCCCCCCCCCWWW.......",
    ".......WWWCCCCCCCCCCCCWWW.......",
    "..........BBBBBBBBBBBB..........",
    ".........BBBBB..BBBBB...........",
    "................................",
]

for y, row in enumerate(rows):
    assert len(row) == 32, (y, len(row))
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, cmap[ch])

# Flour dusting on the cream apron (white specks)
flour = [
    (10, 16), (15, 16), (21, 16),
    (9, 17), (15, 17), (21, 17),
    (9, 18), (16, 18), (21, 18),
    (11, 24), (17, 24), (21, 24),
    (13, 25), (19, 25),
    (10, 26), (15, 26), (22, 26),
    (12, 27), (18, 27),
    (11, 28), (17, 28),
]
for x, y in flour:
    c.set(x, y, W)

# Thumbs wrapping over the bamboo rim so hands clearly grip the steamer
for x, y in [(5, 20), (26, 20)]:
    c.set(x, y, S)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))

finish(c)
