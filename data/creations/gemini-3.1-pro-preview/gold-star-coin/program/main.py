import sys
from pixelbench_api import *

def draw_coin():
    c = new_canvas(16, 16)
    
    palette = {
        ' ': None,
        'O': '#3A2618',
        'S': '#8A4A00',
        'D': '#D97D00',
        'L': '#F5A105',
        'H': '#FED62F',
        'W': '#FFF8CC'
    }
    
    art = [
        "      OOOO      ",
        "    OOHHHHOO    ",
        "   OHLLLLLLSO   ",
        "  OHLLDDDDDDSO  ",
        "  OHLLDWWDSDSO  ",
        " OHLDDWWWWSDDSO ",
        " OHLWWWWWWWWSSO ",
        " OHLDWWWWWWSDSO ",
        " OHLDDWWWWSDDSO ",
        " OHLDWWSDWWSDSO ",
        " OHLWSDDDDDWSSO ",
        "  OHSSDDDDDSSO  ",
        "  OSDDDDDDDDSO  ",
        "   OSSSSSSSSO   ",
        "    OOOOOOOO    ",
        "      OOOO      "
    ]
    
    for y, row in enumerate(art):
        for x, char in enumerate(row):
            color = palette[char]
            if color is not None:
                c.set(x, y, color)
                
    return c

if __name__ == "__main__":
    result = draw_coin()
    finish(result)
