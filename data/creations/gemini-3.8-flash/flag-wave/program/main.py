# Flag-wave animation (3 frames)
# Frame 1: Original input (fly end at highest point)
# Frame 2: Mid-wave (crest in middle, fly end midway)
# Frame 3: Wave at lowest point (fly end at lowest point)

import numpy as np

# Palette mapping:
# 0: transparent
# 1: black #141b1b
# 2: red #d14b34
# 3: orange #e46d3a
# 4: purple #8f3e56
# 5: dark purple #543c52

char_map = {'.': 0, '#': 1, 'R': 2, 'O': 3, 'P': 4, 'p': 5}

def make_canvas(full_rows, name=None):
    c = new_canvas(48, 56, name=name)
    for y in range(14):
        row = full_rows[y]
        for x in range(12):
            val = char_map[row[x]]
            if val != 0:
                c.rect(x*4, y*4, 4, 4, val)
    return c

# Frame 1 is input_canvas
f1 = input_canvas.copy(name="frame1")

# Frame 2 (Midpoint):
# Crest at cols 8, 9; fly end at col 11 rows 3..9
f2_rows = [
    "............", # 0
    ".......###..", # 1: crest top outline at cols 7, 8, 9
    "......#OOO#.", # 2: outline at 6, 10; highlight on crest at 7, 8, 9
    ".######OOOR#", # 3: pole top & hoist at 1..6; crest 7..9; col 10 R; col 11 #
    ".#PP#RRROOR#", # 4: strap; cloth 5..7 R; crest 8..9 O; col 10 R; col 11 #
    "#RORRRRROOR#", # 5: strap; cloth 5..7 R; crest 8..9 O; col 10 R; col 11 #
    ".#pp#RRRRRR#", # 6: pole; cloth 5..10 R; col 11 #
    ".#PP#RRRRRR#", # 7: pole; cloth 5..10 R; col 11 #
    "#RORR####RR#", # 8: strap; bottom outline 5..8; cloth 9..10 R; col 11 #
    ".#pp#....###", # 9: pole; bottom outline 9..11
    ".#PP#.......", # 10
    ".#PP#.......", # 11
    ".#PP#.......", # 12
    ".#PP#.......", # 13
]
f2 = make_canvas(f2_rows, name="frame2")

# Frame 3 (Lowest point):
# Fly end swings to lowest point (col 11 rows 6..12)
f3_rows = [
    "............", # 0
    "............", # 1
    "............", # 2
    ".######.....", # 3: pole top 1..4, hoist top outline 5..6
    ".#PP#RR#....", # 4: pole, cloth 5..6 R, top outline 7 #
    "#RORRRRR#...", # 5: strap, cloth 5..7 R, top outline 8 #
    ".#pp#RRRR###", # 6: pole, cloth 5..8 R, top outline 9..11
    ".#PP#RRROOR#", # 7: pole, cloth 5..8 R, highlight 9..10 O, col 11 #
    "#RORR##ROOR#", # 8: strap, bottom outline 5..6, cloth 7 R, highlight 8..10 O, col 11 #
    ".#pp#..#OOR#", # 9: pole, bottom outline 7 #, highlight 8..10 O/R, col 11 #
    ".#PP#...#RR#", # 10: pole, bottom outline 8 #, cloth 9..10 R, col 11 #
    ".#PP#....#R#", # 11: pole, bottom outline 9 #, cloth 10 R, col 11 #
    ".#PP#.....##", # 12: pole, bottom outline 10..11
    ".#PP#.......", # 13
]
f3 = make_canvas(f3_rows, name="frame3")

# Preview
view(f1)
view(f2)
view(f3)

# Submit all 3 frames
finish([f1, f2, f3])
