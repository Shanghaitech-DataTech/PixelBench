from pixelbench_api import new_canvas, view, save, finish

MAP = [
    "..BBBBBBBBBBBB..",
    ".BBBBBBBBBBBBBB.",
    ".BBBBBBBBBBBBBB.",
    ".BBSSSSSSSSSSBB.",
    ".BBSSEESSEESSBB.",
    ".BBSSSSMMSSSSBB.",
    ".BBBSSSSSSSSBBB.",
    "..BBSSSSSSSSBB..",
    "..WWTTWWWWWWTWW..",
    "..WWWWWWWWWWWW..",
    "..DWWWWWWWWWWD..",
    "..DWWWWKWKWWWWD..",
    "..DWWWWWWWWWWD..",
    "..WWWLLWWLLWWW..",
    "..WWLL....LLWW..",
    "....KK....KK....",
]

COLS = {
    "B": "#26262e", "S": "#ffd9b3", "E": "#2f1d10", "M": "#c2564f",
    "W": "#f5f5f7", "D": "#c7cbd1", "T": "#2a9d8f", "K": "#33333c",
    "L": "#4b4b58",
}

c = new_canvas(16, 16)
for y, row in enumerate(MAP):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, COLS[ch])

BROWN = "#7a4a24"; PINK = "#f2a9a0"; SHINE = "#555466"
c.set(6, 4, BROWN); c.set(10, 4, BROWN)
c.set(4, 6, PINK); c.set(10, 6, PINK)
c.set(5, 1, SHINE); c.set(6, 1, SHINE)

print(c.matrix_text())
view(c)
save("lab_researcher_preview", c)
finish(c)
