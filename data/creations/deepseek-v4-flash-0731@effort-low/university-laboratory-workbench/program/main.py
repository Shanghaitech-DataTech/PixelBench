from pixelbench_api import *

c = new_canvas(64, 64, name="lab")
W = c.color((224, 232, 238), name="wall")
WOOD = c.color((166, 120, 74), name="wood")
WOODL = c.color((196, 150, 100), name="wood_light")
WOODD = c.color((116, 78, 48), name="wood_dark")
METAL = c.color((205, 210, 216), name="metal")
METALD = c.color((120, 126, 133), name="metal_dark")
BLK = c.color((28, 30, 34), name="black")
INK = c.color((60, 40, 40), name="ink")
WHITE = c.color((246, 247, 248), name="white")
RED = c.color((205, 62, 60), name="red")
BLUE = c.color((62, 92, 178), name="blue")
GREEN = c.color((76, 148, 92), name="green")
YEL = c.color((232, 188, 62), name="yellow")
AMBER = c.color((214, 148, 66), name="amber")
GLASS = c.color((170, 205, 224), name="glass")
RUB = c.color((66, 64, 74), name="rubber")
SHAD = c.color((150, 152, 160), name="shadow")

# ---- Background + desk ----
c.rect(0, 0, 64, 64, W)
c.rect(0, 47, 64, 2, WOOD)       # desk surface y47-48
c.rect(0, 49, 64, 1, WOODL)      # front trim
c.rect(0, 50, 64, 14, WOODD)     # desk front y50-63
c.rect(0, 50, 64, 1, WOOD)       # top front band
c.rect(0, 61, 64, 1, WOOD)
for x in range(2, 63, 12):
    c.rect(x, 52, min(6, 64 - x), 1, WOOD)

# shadows under standing objects (rows 46)
c.rect(3, 46, 15, 1, SHAD)
c.rect(21, 46, 13, 1, SHAD)
c.rect(35, 46, 15, 1, SHAD)
c.rect(52, 46, 11, 1, SHAD)

# ---------------- Microscope (x3-18, bottom y46) ----------------
c.rect(3, 40, 15, 6, METALD)        # base y40-46
c.rect(3, 40, 15, 1, METAL)
c.rect(6, 22, 4, 18, METAL)         # pillar
c.rect(6, 22, 1, 18, METALD)
c.rect(9, 22, 5, 5, METAL)          # arm
c.rect(9, 22, 1, 5, METALD)
c.rect(13, 15, 5, 19, METAL)        # body tube y15-33
c.rect(13, 15, 1, 19, METALD)
c.rect(17, 15, 1, 19, METALD)
c.rect(14, 11, 3, 4, BLK)           # eyepiece
c.rect(14, 11, 3, 1, METALD)
c.rect(15, 34, 3, 5, METALD)        # objective head
c.rect(15, 35, 1, 4, BLK)
c.rect(17, 35, 1, 4, BLK)
c.rect(10, 36, 11, 2, METAL)        # stage y36-37
c.rect(10, 36, 11, 1, METALD)
c.circle(10, 26, 2, METALD)         # coarse focus knob
c.rect(9, 30, 2, 1, METALD)         # fine knob

# ---------------- Test tube rack (x21-33) ----------------
c.rect(21, 40, 13, 4, WOOD)         # top rail y40-43
c.rect(21, 40, 13, 1, WOODL)
c.rect(21, 44, 2, 2, WOOD)          # legs y44-45
c.rect(32, 44, 2, 2, WOOD)
c.rect(21, 45, 13, 2, WOOD)         # base y45-46
c.rect(21, 45, 13, 1, WOODL)
c.rect(28, 36, 5, 4, WOOD)          # handle
c.rect(29, 35, 3, 2, WOOD)

def tube(x, liq, fill_h):
    c.rect(x, 33, 3, 12, GLASS)     # glass y33-44, sits on base(y45)
    c.rect(x, 41, 3, fill_h, liq)
    c.rect(x, 41, 3, 1, WHITE)
    c.rect(x, 33, 3, 12, BLK, fill=False)

tube(22, RED, 3)
tube(26, BLUE, 4)
tube(30, GREEN, 3)

# ---------------- Bottles ----------------
# Amber bottle x35-42
c.rect(37, 37, 2, 3, AMBER)         # neck
c.rect(36, 35, 4, 2, BLK)           # stopper
c.rect(35, 40, 8, 6, AMBER)         # body y40-46
c.rect(36, 42, 6, 3, WHITE)         # label
c.rect(36, 42, 6, 1, INK)
c.rect(35, 40, 8, 6, INK, fill=False)

# Blue bottle x44-50
c.rect(46, 36, 2, 4, BLUE)          # neck
c.rect(45, 34, 4, 2, BLK)           # stopper
c.rect(44, 40, 7, 6, BLUE)          # body y40-46
c.rect(45, 42, 5, 3, WHITE)         # label
c.rect(45, 42, 5, 1, INK)
c.rect(44, 40, 7, 6, INK, fill=False)

# ---------------- Open notebook (x52-63, y29-44) ----------------
c.rect(52, 29, 11, 15, WOODD)       # cover y29-43
c.rect(53, 30, 5, 13, WHITE)        # left page x53-57 y30-42
c.rect(59, 30, 4, 13, WHITE)        # right page x59-62 y30-42
c.rect(58, 29, 1, 15, WOODD)        # binding
c.rect(53, 30, 5, 13, INK, fill=False)
c.rect(59, 30, 4, 13, INK, fill=False)
c.rect(53, 29, 10, 1, INK)          # cover top
for py in (32, 34, 36):
    c.rect(54, py, 3, 1, INK)
    c.rect(60, py, 2, 1, INK)

# ---------------- Lying items on desk surface y47-48 ----------------
# Dropper lying in front of bottles (x35-44)
c.ellipse(33, 47, 3, 1, RUB)        # bulb x30-36 y46-48
c.rect(36, 47, 9, 2, GLASS)         # shaft x36-44
c.rect(36, 47, 9, 1, RUB)           # rubber grip half
c.rect(44, 47, 2, 1, GLASS)         # nozzle tip
# Pen lying on desk (x52-59)
c.rect(52, 48, 8, 1, RED)
c.rect(52, 48, 2, 1, INK)
# Pencil lying on desk (x20-27)
c.rect(20, 48, 8, 1, YEL)
c.rect(20, 48, 2, 1, INK)

finish(c)
print(c.stats_text())
