from pixelbench_api import new_canvas, finish

OUT = (18, 18, 22)
BASE = (142, 144, 152)
LIGHT = (210, 214, 224)
DARK = (56, 58, 66)
HOOD = (20, 20, 24)
EYE = (196, 216, 236)
BELT = (66, 44, 30)
GOLD = (214, 172, 86)
GOLDD = (56, 40, 18)

c = new_canvas(32, 32)
base_idx = c.color(BASE, "base")

# Silhouette: mail coif + hauberk (symmetric around column 15.5)
pts = [(16, 0), (12, 2), (9, 5), (9, 8), (7, 10), (5, 13), (5, 17), (7, 21),
       (8, 24), (7, 28), (10, 30), (16, 31), (21, 30), (24, 28), (23, 24),
       (24, 21), (26, 17), (26, 13), (24, 10), (22, 8), (22, 5), (19, 2)]
c.poly(pts, BASE)

# hood face opening (dark)
c.poly([(16, 2), (13, 3), (12, 5), (13, 8), (16, 9), (19, 8), (20, 5), (19, 3)], HOOD)
c.color(LIGHT, "light")
c.color(DARK, "dark")


def ring(cx, cy):
    px = [(-2, 0, DARK), (2, 0, DARK),
          (-1, -1, LIGHT), (0, -1, LIGHT), (1, -1, LIGHT),
          (-1, 1, DARK), (0, 1, DARK), (1, 1, DARK)]
    for dx, dy, col in px:
        x, y = cx + dx, cy + dy
        if 0 <= x < 32 and 0 <= y < 32 and c.get(x, y) == base_idx:
            c.set(x, y, col)


row = 0
for y in range(10, 30, 2):
    off = 2 if row % 2 else 0
    for x in range(5 + off, 27, 4):
        ring(x, y)
    row += 1

# chain rim around the coif at eye level
for rx in (9, 21):
    ring(rx, 6)
# arm cuffs
c.rect(5, 18, 3, 4, DARK)
c.rect(24, 18, 3, 4, DARK)
# belt
c.rect(8, 23, 17, 3, BELT)
c.rect(14, 23, 5, 3, GOLD)
c.rect(15, 24, 3, 1, GOLDD)
# gold-hem band
c.rect(10, 29, 12, 2, GOLD)
# dark outline
c.poly(pts, OUT, fill=False)
# eyes (symmetric around column 15.5)
c.set(14, 5, EYE)
c.set(17, 5, EYE)

print(c.stats_text())
print(c.matrix_text())
finish(c)
