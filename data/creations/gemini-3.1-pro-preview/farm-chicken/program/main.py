from pixelbench_api import new_canvas, finish

def draw_chicken():
    palette = {
        'O': '#4a2e15',
        'w': '#fceec9',
        's': '#d6b88b',
        'S': '#b08d5c',
        'R': '#d94c36',
        'r': '#a62b1a',
        'Y': '#f0a524',
        'y': '#c27115',
        'e': '#1f150d',
        'W': '#ffffff',
        'P': '#f0b1a8',
        ' ': None
    }

    grid = [
        "                                ",
        "                                ",
        "                                ",
        "                                ",
        "                     rR         ",
        "                    rRRR        ",
        "           O       OrRRO        ",
        "          OwO      OwwwwwO      ",
        "         OwwwO    OwwwwwwsO     ",
        "        OwwwwwO O OweWwwsOYY    ",
        "       OwwwwwwwOwOOwwwwwwOYYy   ",
        "      OwwwwwwwwwwOOwPwwwwsORR   ",
        "     OwwwwwwwwwwwOwwwwwwwwrrO   ",
        "    OwwwwwwwwwwwwwwwwwwwwwrO    ",
        "    OwwwwwwwwwwwwwwwwwwwwwOO    ",
        "   OwwwwwwwwwwwwwwwwwwwwwwO     ",
        "   OwwwwwwwwwwOOOwwwwwwwwwO     ",
        "   OwwwwwwwwwOwwwOOwwwwwwwO     ",
        "   OwwwwwswwwOwwwwwOwwwwwwO     ",
        "   OwwwwsswwwOwwwwwOwwwwwsO     ",
        "    OwwssswwwwOwwssOwwwwssO     ",
        "    OwwssssssssOOOOsssssssO     ",
        "     OOssssssssssssssssssO      ",
        "       OOSSSSSSSSSSSSSSSO       ",
        "         OOOOOOOOOOOOOOO        ",
        "            Y    Y              ",
        "           YYY  YYY             ",
        "                                ",
        "                                ",
        "                                ",
        "                                ",
        "                                "
    ]

    c = new_canvas(32, 32)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            color = palette.get(char)
            if color:
                c.set(x, y, color)
    
    finish(c)

if __name__ == '__main__':
    draw_chicken()
