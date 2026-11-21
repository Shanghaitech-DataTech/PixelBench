W, H = 128, 64

result = new_canvas(W, H, background="#151a24", name="chart")
c = result

GRID = c.color("#202939", name="grid")
AXIS = c.color("#3b475c", name="axis")

LEAF = c.color("#3aa757", name="leaf")
LEAF_D = c.color("#256e39", name="leaf_dark")
STEM = c.color("#8a5a34", name="stem")

FRUIT = [
    ("apple", 10, "#e5383b", "#ff7b7b", "#9d1a20"),
    ("banana", 5, "#f2c53d", "#ffe98a", "#b07c14"),
    ("orange", 7, "#f57c1f", "#ffb45e", "#a94a12"),
    ("lemon", 14, "#dfe85a", "#f7ffa3", "#8f9a2a"),
    ("grape", 2, "#8e5cf6", "#bda4ff", "#4f37a0"),
]

BASE_Y = 51      # bottom row of every bar column
UNIT = 3         # pixels per unit of value
BAR_W = 14
PITCH = 22
BX0 = 18

ART = {
    "apple": [
        ".........",
        ".....gg..",
        "....sgG..",
        "..rrrrr..",
        ".rrRrrrr.",
        "rrRRrrrrd",
        "rrRrrrrrd",
        ".rrrrrdd.",
        "..rrrrd..",
    ],
    "banana": [
        ".........",
        ".......yd",
        "......yyy",
        ".....yyy.",
        "....yyy..",
        "...yyy...",
        "..yyy....",
        ".dyy.....",
        ".dy......",
    ],
    "orange": [
        "....gg...",
        "...gG....",
        "..ooooo..",
        ".ooooooo.",
        "oOOoooooo",
        "oOoooooOd",
        ".oooooOd.",
        "..oooOd..",
        "...ood...",
    ],
    "lemon": [
        ".........",
        ".........",
        "......gG.",
        "...llll..",
        ".lLlllll.",
        "llLllllld",
        ".llllldd.",
        "...llld..",
        ".........",
    ],
    "grape": [
        ".........",
        "....s.gG.",
        ".pLppppd.",
        ".pLppppd.",
        "..pLppd..",
        "..ppppd..",
        "...ppd...",
        "....p....",
        ".........",
    ],
}


def draw_icon(cv, art, ox, oy, base, light, dark):
    for row, line in enumerate(art):
        assert len(line) == 9, (line, len(line))
        for col, ch in enumerate(line):
            if ch == ".":
                continue
            if ch == "r" or ch == "p" or ch == "l" or ch == "o" or ch == "y":
                idx = base
            elif ch in "RLY":
                idx = light
            elif ch == "d":
                idx = dark
            elif ch == "g":
                idx = LEAF
            elif ch == "G":
                idx = LEAF_D
            elif ch == "s":
                idx = STEM
            else:
                continue
            cv.set(ox + col, oy + row, idx)


# ---- background gridlines (5 and 10 units above the baseline) ----
for k in (5, 10):
    y = BASE_Y + 1 - k * UNIT
    for x in range(11, 122):
        c.set(x, y, GRID)

# ---- axes ----
for x in range(8, 124):
    c.set(x, 52, AXIS)
for y in range(10, 53):
    c.set(8, y, AXIS)
for k in (5, 10):
    y = BASE_Y + 1 - k * UNIT
    for x in range(6, 9):
        c.set(x, y, AXIS)

# ---- bars + icons ----
for i, (name, val, base_hex, light_hex, dark_hex) in enumerate(FRUIT):
    base = c.color(base_hex, name=name)
    light = c.color(light_hex, name=name + "_light")
    dark = c.color(dark_hex, name=name + "_dark")

    x = BX0 + i * PITCH
    h = val * UNIT
    top = BASE_Y - h + 1

    c.rect(x, top, BAR_W, h, base)
    c.rect(x + BAR_W - 1, top, 1, h, dark)
    cap = 2 if h >= 9 else 1
    c.rect(x, top, BAR_W - 1, cap, light)

    icon_x = x + BAR_W // 2 - 4
    draw_icon(c, ART[name], icon_x, 54, base, light, dark)

print(c.stats_text())
print(c.matrix_text(region=(0, 50, 127, 63)))

finish(result)
