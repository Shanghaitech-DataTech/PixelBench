from pixelbench_api import *

# Palette: 6 colors for an antique carved wooden key in a detective game
# 1. Dark outline / carved deep crevice: #1e0f07
# 2. Dark walnut / core shadow: #4a220e
# 3. Mid warm chestnut: #7d3e18
# 4. Golden oak: #b36327
# 5. Honey grain highlight: #de8d3f
# 6. Raw carved wood / edge highlight: #f5be74

pal = {
    '#': '#1e0f07',
    'd': '#4a220e',
    'm': '#7d3e18',
    'l': '#b36327',
    'h': '#de8d3f',
    'b': '#f5be74',
}

grid = [
    "...###..###.....", # 0
    "..#bbb##bbb#....", # 1
    ".#bhh####hhb#...", # 2
    ".#h#..##..#lm#..", # 3
    ".#h#......#dm#..", # 4
    "..#ll#..#dd#....", # 5
    "...#mm##dd#.....", # 6
    "....#bhhb#......", # 7
    "....#mddm#......", # 8
    ".....#hl#.......", # 9
    ".....#hl######..", # 10
    ".....#hl#bhhbm#.", # 11
    ".....#hl####....", # 12
    ".....#hl#bhhbm#.", # 13
    ".....#md######..", # 14
    "......##........", # 15
]

c = new_canvas(16, 16, name="wooden_key")
for y, line in enumerate(grid):
    for x, ch in enumerate(line):
        col = pal.get(ch)
        if col:
            c.set(x, y, col)

finish(c)
