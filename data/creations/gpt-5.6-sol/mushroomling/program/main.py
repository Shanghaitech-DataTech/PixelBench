from pixelbench_api import new_canvas, view, finish

# Four-colour mushroomling sprite; periods are transparent pixels.
result = new_canvas(16, 16, name="mushroomling")
colors = {
    "D": "#211820",  # outline and pupils
    "R": "#c93b45",  # cap
    "W": "#f5e8c8",  # spots and eye whites
    "T": "#b9794f",  # stem body
}

sprite = [
    "................",
    "......DDDD......",
    "....DDRRRRDD....",
    "...DRRWWRRRRD...",
    "..DRRRWWRRWWRD..",
    ".DRRRRRRRRWWRRD.",
    ".DRRRRWWRRRRRRD.",
    "..DRRRRRRRRRRD..",
    ".....DTTTTD.....",
    "....DDWWTWWDD...",
    "...DTDWDTDWDTD..",
    "...DTDTTTTDTD...",
    ".....DTTTTD.....",
    "....DDTDDTDD....",
    "....DD....DD....",
    "................",
]

assert all(len(row) == 16 for row in sprite)
for y, row in enumerate(sprite):
    for x, token in enumerate(row):
        if token != ".":
            result.set(x, y, colors[token])

assert result.stats()["colors_used"] <= 4
view(result, scale=24, margin=1, edges="all")
finish(result)
