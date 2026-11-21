from pixelbench_api import *

c = new_canvas(64, 64, background="#8ec9e8", name="terraces")

# palette
SKY = c.color("#9fd4ee")
SKY2 = c.color("#c8e8f5")
MT = c.color("#7a9e8f")
MT2 = c.color("#94b8a5")
VIL = c.color("#8a5a3b")
VILR = c.color("#c9884a")
GOLD1 = c.color("#e8c25a")   # bright terrace
GOLD2 = c.color("#d4a83e")
GOLD3 = c.color("#b8882e")
GOLD4 = c.color("#96691f")
RIDGE = c.color("#6e4a1a")
FARM = c.color("#2b3a6b")
HAT = c.color("#e8d9a0")

# sky gradient
c.rect(0, 0, 64, 10, SKY)
c.rect(0, 8, 64, 4, SKY2)
# clouds
c.rect(10, 3, 6, 1, "#ffffff")
c.rect(12, 2, 3, 1, "#ffffff")
c.rect(40, 5, 7, 1, "#ffffff")

# distant mountains
c.poly([(0, 22), (8, 12), (18, 20), (26, 11), (36, 21), (46, 13), (56, 20), (63, 15), (63, 26), (0, 26)], MT)
c.poly([(0, 26), (10, 18), (22, 25), (32, 17), (44, 25), (54, 19), (63, 24), (63, 30), (0, 30)], MT2)

# village houses on mid slope
def house(x, y, w=5, h=3):
    c.rect(x, y, w, h, VIL)
    c.rect(x - 1, y - 2, w + 2, 2, VILR)

house(14, 24)
house(22, 23, 6, 3)
house(31, 24)
house(40, 23, 5, 3)
house(48, 25, 4, 3)

# terraces: stacked golden bands with wavy contour ridges
# each band: y range, colour
bands = [
    (28, 32, GOLD1),
    (32, 36, GOLD2),
    (36, 41, GOLD1),
    (41, 46, GOLD3),
    (46, 52, GOLD2),
    (52, 58, GOLD4),
    (58, 64, GOLD3),
]
for y0, y1, col in bands:
    c.rect(0, y0, 64, y1 - y0, col)

# contour ridge lines (wavy darker lines separating terraces)
for i, y in enumerate([28, 32, 36, 41, 46, 52, 58]):
    for x in range(64):
        wy = y + int(2 * ((x * 7 + i * 13) % 5 == 0)) + (1 if (x + i * 3) % 9 == 0 else 0)
        c.set(x, wy, RIDGE)

# water sheen highlights on some terraces (harvest stubble sparkle)
for x in range(0, 64, 3):
    c.set(x, 30, "#f5e08a")
    c.set((x + 1) % 64, 38, "#f5e08a")
    c.set((x + 2) % 64, 49, "#e8c86a")

# diagonal light shading for depth on lower terraces
for x in range(64):
    for y in range(52, 64):
        if (x + y) % 7 == 0:
            c.set(x, y, "#7d5518")

# two farmers on a narrow ridge (around y=46 ridge line)
def farmer(x, y):
    c.set(x, y - 1, HAT)          # conical hat
    c.set(x, y - 2, HAT)
    c.set(x, y, FARM)             # body
    c.set(x, y + 1, FARM)         # legs

farmer(20, 45)
farmer(26, 45)
# tiny bundles of harvested rice near farmers
c.set(23, 45, "#f0d060")
c.set(18, 46, "#f0d060")

print(c.stats_text())
save("rice-terraces-harvest", c)
finish(c)
