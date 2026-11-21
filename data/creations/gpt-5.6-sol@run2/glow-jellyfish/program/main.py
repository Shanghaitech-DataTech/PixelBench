# 16x16 glowing jellyfish enemy sprite
result = new_canvas(16, 16, background=None, name="glow-jellyfish")

colors = {
    "D": "#101a3d",   # deep-water outline
    "N": "#243664",   # inner shadow
    "C": "#38bfc8",   # cyan body
    "L": "#75f1df",   # luminous aqua
    "W": "#d9fff2",   # hot glow
    "P": "#a68bf0",   # lavender translucency
    "M": "#5f62bd",   # violet shadow
    "g": "#58e6dc42", # soft outer glow
    "h": "#a2fff27a", # bright outer glow
}

# Sparse aura pixels around the creature; the field remains transparent.
halo = {
    1:  ".......gg.......",
    2:  ".....g....g.....",
    3:  "....g......g....",
    4:  "..g..........g..",
    5:  ".g............g.",
    7:  "..g..........g..",
    9:  "..g..........g..",
    11: "...g........g...",
    13: "...g........g...",
    15: ".....g..g.......",
}
for y, row in halo.items():
    for x, key in enumerate(row):
        if key != ".":
            result.set(x, y, colors[key])

# Domed bell with a dark readable contour and a scalloped lower rim.
bell = {
    2:  "......DDDD......",
    3:  ".....DCLWPD.....",
    4:  "....DCLLWPPD....",
    5:  "...DCCLLWPPPD...",
    6:  "...DCLLWWPPPD...",
    7:  "...DCCLLPPMPD...",
    8:  "...DCCDNPDMPD...",
    9:  "....DDD.D.DD....",
}
for y, row in bell.items():
    for x, key in enumerate(row):
        if key != ".":
            result.set(x, y, colors[key])

# Glassy pinpricks and broken internal reflections.
for x, y, key in [
    (6, 4, "W"), (7, 3, "W"), (5, 6, "L"),
    (8, 5, "W"), (10, 6, "P"), (4, 7, "L"),
    (12, 6, "h"),
]:
    result.set(x, y, colors[key])

# Four short, curved tentacles. Dark roots retain the enemy-sprite contour.
tentacle_dark = [
    [(5, 9), (5, 11), (4, 12), (4, 13)],
    [(7, 9), (7, 13), (6, 14)],
    [(9, 9), (9, 12), (10, 13)],
    [(11, 9), (11, 11), (12, 12)],
]
for points in tentacle_dark:
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        result.line(x0, y0, x1, y1, colors["D"])

# Lit cores make the tentacles feel emissive without weakening their outline.
for x, y, key in [
    (5, 10, "C"), (4, 12, "L"),
    (7, 10, "L"), (7, 11, "P"), (7, 12, "P"), (6, 14, "M"),
    (9, 10, "P"), (9, 11, "P"), (10, 13, "M"),
    (11, 10, "P"), (12, 12, "M"),
]:
    result.set(x, y, colors[key])

finish(result)
