from pixelbench_api import new_canvas, finish, save

c = new_canvas(16, 16, background=None, name="mushroomling")

OUT = c.color("#2a1a24", name="outline")
RED = c.color("#d13b2e", name="cap")
WHT = c.color("#f7f0e0", name="spot")
TAN = c.color("#e8b877", name="stalk")

PAL = {"O": OUT, "R": RED, "W": WHT, "B": TAN}

rows = [
    ".....OOOOOO.....",  # 0  cap crown
    "...OORRRRRROO...",  # 1
    "..ORWWRRRRWWRO..",  # 2  upper side spots
    ".ORRWWRRRRWWRRO.",  # 3
    ".ORRRRRWWRRRRRO.",  # 4  centre spot
    "..ORRRRWWRRRRO..",  # 5
    "..ORRRRRRRRRRO..",  # 6
    "..OOOOOOOOOOOO..",  # 7  cap underside / rim
    "....OBBBBBBO....",  # 8  stalk
    "....OBOBBOBO....",  # 9  round eyes
    "...OOBOBBOBOO...",  # 10 eyes + shoulders
    "..OBBBBBBBBBBO..",  # 11 stubby arms
    "..OOBBBBBBBBOO..",  # 12 arm undersides
    "...OBBBBBBBBO...",  # 13 hips
    "...OBBO..OBBO...",  # 14 legs
    "...OOOO..OOOO...",  # 15 feet
]

for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row), row)
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, PAL[ch])

print(c.stats_text())
print(c.matrix_text())
save("mushroomling", c)
finish(c)
