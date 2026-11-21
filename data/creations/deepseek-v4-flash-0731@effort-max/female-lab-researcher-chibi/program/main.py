from pixelbench_api import new_canvas, finish

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
    "B": "#26262e",   # black hair
    "S": "#ffd9b3",   # skin
    "E": "#2f1d10",   # eye pupil (dark)
    "M": "#c2564f",   # mouth
    "W": "#f5f5f7",   # white lab coat
    "D": "#c7cbd1",   # coat shadow
    "T": "#2a9d8f",   # teal shirt collar
    "K": "#33333c",   # buttons / shoes
    "L": "#4b4b58",   # pants
}

c = new_canvas(16, 16)
for y, row in enumerate(MAP):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, COLS[ch])

BROWN = "#7a4a24"     # brown iris
PINK = "#f2a9a0"     # cheeks
SHINE = "#555466"     # hair shine

# brown iris pixels
c.set(6, 4, BROWN)
c.set(10, 4, BROWN)
# cheeks
c.set(4, 6, PINK)
c.set(10, 6, PINK)
# hair shine
c.set(5, 1, SHINE)
c.set(6, 1, SHINE)

print(c.stats_text())
finish(c)
