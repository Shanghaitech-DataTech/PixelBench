from pixelbench_api import new_canvas, finish

W, H = 16, 16
c = new_canvas(W, H, name="lab_researcher_chibi")

pal = {
    "H": (0x22, 0x26, 0x2B),  # black hair
    "h": (0x3F, 0x45, 0x4D),  # hair highlight
    "S": (0xF6, 0xCB, 0xA6),  # skin
    "s": (0xDF, 0xA8, 0x7F),  # skin shadow / blush
    "E": (0x6B, 0x3F, 0x23),  # brown eyes
    "M": (0xA3, 0x4F, 0x33),  # mouth
    "W": (0xF4, 0xF4, 0xF4),  # white lab coat
    "w": (0xC9, 0xC9, 0xC9),  # coat shadow
    "B": (0x3B, 0x6E, 0xA5),  # badge/pen blue
    "K": (0x33, 0x36, 0x3C),  # leggings / shoes
}

rows = [
    "..HHHHHHHHHH....",
    "..HHhHHHHhHH....",
    ".HHHHHHHHHHHH...",
    ".HHSSSSSSSSHH...",
    ".HHSEESSEESSHH..",
    ".HHSSSMMSSSHH...",
    ".HHsSSSSSSsHH...",
    ".HHHHSSHHHHH....",
    "..WWWWWWWWWW....",
    "..WwWWWWWWwW....",
    "..WwWWBBWWwW....",
    "..WSWWWWWWWS....",
    "..WWWWWWWWWW....",
    "..KKKKKKKKKK....",
    ".KKKKKKKKKKKK...",
    ".KKKKKKKKKKKK...",
]

for y, row in enumerate(rows):
    assert len(row) == 16, (y, row, len(row))
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, pal[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
