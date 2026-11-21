from pixelbench_api import *

# Let's test standard pixel art circle shapes
# Dimensions: 16x16
grid = [
    "................", # 0
    ".....######.....", # 1 (x: 5..10, 6 px)
    "...##......##...", # 2 (x: 3,4 and 11,12)
    "..#..........#..", # 3 (x: 2 and 13)
    ".#............#.", # 4 (x: 1 and 14)
    ".#............#.", # 5
    "#..............#", # 6 (x: 0 and 15) -> wait, does it go to 0 and 15?
]
