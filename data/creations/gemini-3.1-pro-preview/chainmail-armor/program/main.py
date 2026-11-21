import pixelbench_api as api

c = api.new_canvas(32, 32)

shape = [
    "                                ", # 0
    "                                ", # 1
    "                                ", # 2
    "         MMMMMMMMMMMMMM         ", # 3
    "       MMMMMMMMMMMMMMMMMM       ", # 4
    "      MMMM            MMMM      ", # 5
    "     MMMM              MMMM     ", # 6
    "    MMMMM              MMMMM    ", # 7
    "   MMMMMMMMMMMMMMMMMMMMMMMMMM   ", # 8
    "  MMMMMMMMMMMMMMMMMMMMMMMMMMMM  ", # 9
    " MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ", # 10
    " MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ", # 11
    " MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ", # 12
    " MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ", # 13
    " MMMMMM   MMMMMMMMMMMMMM   MMMMMM", # 14
    "  MMMMM   MMMMMMMMMMMMMM   MMMMM ", # 15
    "   MMMM   MMMMMMMMMMMMMM   MMMM  ", # 16
    "    MMM   MMMMMMMMMMMMMM   MMM   ", # 17
    "     MM   MMMMMMMMMMMMMM   MM    ", # 18
    "          MMMMMMMMMMMMMM         ", # 19
    "          MMMMMMMMMMMMMM         ", # 20
    "          MMMMMMMMMMMMMM         ", # 21
    "          MMMMMMMMMMMMMM         ", # 22
    "          MMMMMMMMMMMMMM         ", # 23
    "          MMMMMMMMMMMMMM         ", # 24
    "          MMMMMMMMMMMMMM         ", # 25
    "          MMMMMMMMMMMMMM         ", # 26
    "          MMMMMM  MMMMMM         ", # 27
    "          MMMMM    MMMMM         ", # 28
    "          MMMM      MMMM         ", # 29
    "          MMM        MMM         ", # 30
    "                                ", # 31
]

outline_color = '#181a1f'

chain_palettes = [
    {'high': '#baced1', 'base': '#8b9bb4', 'shad': '#5a6988'},
    {'high': '#9ba5b5', 'base': '#6b7485', 'shad': '#424959'},
    {'high': '#6b7485', 'base': '#424959', 'shad': '#2a2f3a'},
    {'high': '#424959', 'base': '#2a2f3a', 'shad': '#181a1f'},
]

belt_base = '#5c3a21'
belt_high = '#825433'
belt_shad = '#382110'

buckle_gold = '#e6b800'
buckle_high = '#ffdb4d'
buckle_hole = '#1a1a1a'

trim_high = '#6d4c41'
trim_base = '#4e342e'
trim_shad = '#301b16'

def get_shade(x, y):
    shade = 1
    if y <= 7: shade = 0
    if 10 <= x <= 23 and y >= 14:
        if x in (10, 11, 22, 23): shade += 1
        if x in (10, 23): shade += 1
    if 10 <= x <= 23 and 14 <= y <= 18:
        shade += 1
        if 14 <= y <= 16 and x in (10, 11, 22, 23): shade += 1
    if y >= 14 and (x < 10 or x > 23):
        if y >= 16: shade += 1
        if y >= 17: shade += 1
    if y >= 25: shade += 1
    if y >= 28: shade += 1
    if 10 <= x <= 23 and 8 <= y <= 10:
        shade += 1
    return min(shade, 3)

for y in range(32):
    for x in range(32):
        if shape[y][x] == 'M':
            shade_level = get_shade(x, y)
            pal = chain_palettes[shade_level]
            if (x + y) % 2 == 0:
                color = pal['high'] if x % 2 == 0 else pal['shad']
            else:
                color = pal['base']
            c.set(x, y, color)

for y in range(32):
    for x in range(32):
        if shape[y][x] == 'M':
            is_neck = False
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < 32 and 0 <= ny < 32:
                    if shape[ny][nx] == ' ' and 5 <= ny <= 7 and 9 <= nx <= 22:
                        is_neck = True
            
            is_sleeve_bottom = False
            if y < 31 and shape[y+1][x] == ' ' and (x < 10 or x > 23):
                is_sleeve_bottom = True
                
            is_hem_bottom = False
            if y < 31 and shape[y+1][x] == ' ' and 10 <= x <= 23:
                is_hem_bottom = True
            
            is_split = False
            if y >= 27 and 14 <= x <= 19:
                for dx, dy in [(-1,0), (1,0)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 32 and 0 <= ny < 32:
                        if shape[ny][nx] == ' ' and 15 <= nx <= 18:
                            is_split = True

            if is_neck or is_sleeve_bottom or is_hem_bottom or is_split:
                t_shade = get_shade(x, y)
                if t_shade >= 2:
                    c.set(x, y, trim_base if (x + y) % 2 == 0 else trim_shad)
                else:
                    c.set(x, y, trim_high if (x + y) % 2 == 0 else trim_base)

for x in range(10, 24):
    for y in (20, 21):
        if shape[y][x] == 'M':
            if x in (10, 11, 22, 23): color = belt_shad
            elif y == 20: color = belt_high
            else: color = belt_base
            c.set(x, y, color)

for x in range(14, 18):
    for y in range(19, 22):
        if x in (14, 17) or y in (19, 21):
            color = buckle_high if y == 19 and x in (14, 15, 16) else buckle_gold
            c.set(x, y, color)
        else:
            c.set(x, y, buckle_hole)

for y in range(32):
    for x in range(32):
        if shape[y][x] == ' ':
            borders_m = False
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < 32 and 0 <= ny < 32:
                    if shape[ny][nx] == 'M':
                        borders_m = True
            if borders_m:
                c.set(x, y, outline_color)

api.finish(c)
