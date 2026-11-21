from pixelbench_api import *

c = new_canvas(16, 16, name="coin")

edge  = c.color("#4a3208", "edge")
dark  = c.color("#a06a10", "dark")
mid   = c.color("#d9a521", "mid")
light = c.color("#f2ce54", "light")
star  = c.color("#fceea4", "star")

# Symmetric 14px coin disc with a 1px transparent margin all around.
outer = {
    1: (7, 8), 2: (4, 11), 3: (3, 12), 4: (2, 13), 5: (2, 13),
    6: (1, 14), 7: (1, 14), 8: (1, 14), 9: (1, 14), 10: (2, 13),
    11: (2, 13), 12: (3, 12), 13: (4, 11), 14: (7, 8),
}
inner = {
    2: (5, 10), 3: (4, 11), 4: (3, 12), 5: (3, 12), 6: (2, 13),
    7: (2, 13), 8: (2, 13), 9: (2, 13), 10: (3, 12), 11: (3, 12),
    12: (4, 11), 13: (5, 10),
}

for y, (a, b) in outer.items():
    for x in range(a, b + 1):
        c.set(x, y, edge)
for y, (a, b) in inner.items():
    for x in range(a, b + 1):
        c.set(x, y, mid)

# 5-pointed star in the middle.
star_rows = [
    ".......ss.......",
    "......ssss......",
    ".....ssssss.....",
    "....ssssssss....",
    ".....ssssss.....",
    "......ssss......",
    ".....ss..ss.....",
    "....ss....ss....",
    "...ss......ss...",
]
for y, row in enumerate(star_rows):
    for x, ch in enumerate(row):
        if ch == "s":
            c.set(x, y + 3, star)

# Dark outline around the star so it reads against the gold body.
outline_px = set()
for y in range(16):
    for x in range(16):
        if c.get(x, y) != star:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 16 and 0 <= ny < 16 and c.get(nx, ny) == star:
                    outline_px.add((x, y))
for x, y in outline_px:
    c.set(x, y, edge)

# Shading on top of the remaining gold body: light from the top-left,
# shadow toward the bottom-right.
light_px = [
    (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
    (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
    (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
    (3, 5), (4, 5), (5, 5), (6, 5),
    (2, 6), (3, 6), (4, 6), (5, 6),
    (2, 7), (3, 7), (4, 7),
    (2, 8), (3, 8),
]
dark_px = [
    (12, 8), (13, 8),
    (11, 9), (12, 9), (13, 9),
    (10, 10), (11, 10), (12, 10),
    (10, 11), (11, 11), (12, 11),
    (8, 12), (9, 12), (10, 12), (11, 12),
    (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13),
]
for x, y in light_px:
    if c.get(x, y) == mid:
        c.set(x, y, light)
for x, y in dark_px:
    if c.get(x, y) == mid:
        c.set(x, y, dark)

print(c.stats_text())
print(c.matrix_text())

finish(c)
