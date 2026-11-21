import sys
from pixelbench_api import new_canvas, view, save, finish

c = new_canvas(32, 32)

palette = {
    '.': None,
    'O': c.color('#1A301D'),
    'S': c.color('#2C4C2B'),
    'M': c.color('#42783B'),
    'H': c.color('#6B9E56'),
    'B': c.color('#98C97A'),
    'E': c.color('#F7FFA6'),
    'G': c.color('#D1E866'),
    'A': c.color('#73563F'),
    'D': c.color('#4A3525'),
    'R': c.color('#D93838'),
    'r': c.color('#8F2424'),
    'W': c.color('#E8E3D8'),
    'w': c.color('#B0A99A')
}

MUSHROOM = [
    ".............OOOOOO.............",
    "............ORRRRRRO............",
    "...........ORRWRRRRRO...........",
    "..........ORRRRRRWRRRO..........",
    "..........ORWRRRRRRRWO..........",
    "...........ORRRRRRRRO...........",
    "............OrrrrrrO............",
    ".............OwwwWO.............",
    ".............OwwwWO.............",
    ".............OwwwWO.............",
    ".............OwwwWO............."
]

SLIME = [
    "........OOOOOOOOOOOOOOOO........",
    ".......OOSSSSSSSSSSSSSSOO.......",
    "......OSMMMMMMMMMMMMMMMMSO......",
    ".....OSMMMMHHHHHMMMMMMMMMSO.....",
    "....OSMMMMHBBBBHMMMMMMMMMMSO....",
    "...OSMMMMHBBBBHMMMMMMMMMMMMSO...",
    "...OSMMMMHHHHHHMMMMMMMMMMMMSO...",
    "...OSMMMMMMMMMMMMMMMMMMHHMMSO...",
    "...OSMMMMMGGGGMMMMGGGGMMBMMSO...",
    "...OSMMMMMGEEGMMMMGEEGMMMMMSO...",
    "...OSMMSMMGEEGMMMMGEEGMMSMMSO...",
    "...OSMMMMMGGGGSMMSGGGGMMMMMSO...",
    "...OSMMMMMMMMMMSSMMMMMMMMMMSO...",
    "...OSMMMMSMMMMMMMMMMMMSMMMMSO...",
    "....OSMMSSMMMMMMMMMMMMSSMMSO....",
    "....OOSSSSSSSSSSSSSSSSSSSSOO....",
    "......OOOOOOOOOOOOOOOOOOOO......"
]

ANTLERS = [
    "........O..............O........",
    ".......OAO............OAO.......",
    "......OADO............ODAO......",
    ".....OADO.OAO......OAO.ODAO.....",
    ".....OADO.OADO....ODAO.ODAO.....",
    "......OADODO........ODODAO......",
    ".......OADO..........ODAO.......",
    "........ODO..........ODO........",
    "........O..............O........"
]

def draw_sprite(sprite, start_y):
    for y, row in enumerate(sprite):
        for x, char in enumerate(row):
            if char in palette and palette[char] is not None:
                c.set(x, start_y + y, palette[char])

draw_sprite(MUSHROOM, 4)
draw_sprite(SLIME, 13)
draw_sprite(ANTLERS, 6)

finish(c)
