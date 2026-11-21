from pixelbench_api import new_canvas, finish

# 16x16 mushroom monster: red cap, white spots, round eyes, stubby arms/legs,
# dark outline, transparent background. Up to 4 visible colours.
W = H = 16
grid = [
    "................",  # 0
    "......OOOO......",  # 1  cap top
    ".....ORRRO......",  # 2
    "....ORRRRRO.....",  # 3
    "...ORRRRRRRO....",  # 4
    "...ORWRRRWRO....",  # 5  white spots
    "...ORRWWRRRO....",  # 6  spot on cap
    "....OBBBBBBO....",  # 7  cap lip / stem top
    "...OBWWBWWBO....",  # 8  eyes
    "...OBWOBOWBO....",  # 9  eyes with pupils
    ".OBBOBBOOBBOBBO.",  # 10 arms + mouth
    "....OBB..BBO....",  # 11 legs
    "..OBBBO..OBBBO..",  # 12 feet
    "................",  # 13
    "................",  # 14
    "................",  # 15
]

assert all(len(r) == W for r in grid), [len(r) for r in grid]

palette = {
    "O": (22, 18, 20),      # dark outline / pupils / mouth
    "R": (204, 40, 44),     # red cap
    "W": (250, 248, 242),   # white spots / eyes
    "B": (238, 208, 158),   # cream body
}

c = new_canvas(W, H, name="mushroomling")
for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, palette[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
