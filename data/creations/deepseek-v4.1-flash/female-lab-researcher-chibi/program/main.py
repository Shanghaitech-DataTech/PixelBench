"""Female lab-researcher chibi, 16x16, two-heads-tall RPG sprite."""

# ---------------------------------------------------------------- palette
PAL = {
    ".": None,             # transparent
    "H": "#1a1622",        # black hair
    "h": "#35303f",        # hair highlight
    "S": "#f6c9a6",        # skin
    "s": "#dda882",        # skin shadow
    "E": "#6b3f1d",        # brown iris
    "e": "#2b1a10",        # eye / lash dark
    "M": "#b9665a",        # mouth
    "W": "#fbfbfd",        # white lab coat
    "w": "#ced3de",        # coat shade / seams
    "T": "#a9c6dc",        # light blue shirt at the collar
    "P": "#2e3444",        # navy trousers
    "K": "#191c26",        # shoes
}

ROWS = [
    ".....HHHHHH.....",
    "....HhhhHHHH....",
    "....HHHHHHHH....",
    "....HHSSSSHH....",
    "....HSeSSSeH....",
    "....HSESSESH....",
    "....HSSMSSSH....",
    ".....HSSSSH.....",
    "....HHWSSWHH....",
    "....hWwsswWh....",
    ".....wWTTWw.....",
    ".....wWWWWw.....",
    "....wWWWWWWw....",
    ".....PP..PP.....",
    ".....PP..PP.....",
    "....KKK..KKK....",
]

c = new_canvas(16, 16, background=None, name="result")

for y, row in enumerate(ROWS):
    assert len(row) == 16, (y, len(row), row)
    for x, ch in enumerate(row):
        col = PAL[ch]
        if col is not None:
            c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text())
save("female-lab-researcher-chibi", c)
finish(c)
