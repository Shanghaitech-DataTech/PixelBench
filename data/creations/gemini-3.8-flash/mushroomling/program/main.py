c = new_canvas(16, 16, name="mushroomling")

DARK = "#22121e"
RED = "#dc2626"
WHITE = "#ffffff"
TAN = "#f0ca9c"

sprite = [
    "................", # 0
    ".....DDDDDD.....", # 1  cap top outline
    "...DDRRWWRRDD...", # 2  cap dome top
    "..DRRRWWWWRRRD..", # 3  cap dome with center spot
    ".DWWRRWWWWRRWWD.", # 4  cap dome with center & side spots
    ".DWWRRRWWRRRWWD.", # 5  cap dome with center & side spots
    ".DRRRRRRRRRRRRD.", # 6  cap dome base
    "..DDDDDDDDDDDD..", # 7  cap bottom rim
    "...DTTTTTTTTD...", # 8  face forehead
    "...DTWDTTWDTD...", # 9  round glossy eyes
    "..DDRDDTTDDRDD..", # 10 cheeks, eyes bot, arm top outline
    ".DTTTTTDDTTTTTD.", # 11 stubby arms (shoulder attached), cute open mouth
    ".DTTDTTTTTTDTTD.", # 12 stubby arms (crease), belly
    ".DDDTTDDDDTTDDD.", # 13 arm bot outline, crotch, leg top
    "...DTTD..DTTD...", # 14 stubby legs standing
    "...DDDD..DDDD...", # 15 feet ground outline
]

cmap = {
    '.': None,
    'D': DARK,
    'R': RED,
    'W': WHITE,
    'T': TAN,
}

for y, line in enumerate(sprite):
    for x, ch in enumerate(line):
        col = cmap.get(ch)
        if col is not None:
            c.set(x, y, col)

finish(c)
