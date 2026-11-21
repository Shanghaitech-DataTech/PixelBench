from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="store")
def col(h): return c.color(h)

SKY = col("#0b1133")
RAIN = col("#7fa8d8")
WALL = col("#77232e")
PARA = col("#4c1420")
SIGN = col("#f5e7c8")
SIGNGLOW = col("#ffeaa0")
INT = col("#ffd06a")
INTD = col("#f0b04e")
FRAME = col("#40141e")
SHELF = col("#7a4a1e")
ITEM_R = col("#e05252")
ITEM_B = col("#4aa3e0")
ITEM_G = col("#3fae5a")
AWN_R = col("#d23b3b")
AWN_W = col("#f2ede0")
AWN_S = col("#a92e2e")
LWALL = col("#5f1a24")
DFRAME = col("#331018")
DGLASS = col("#ffc75c")
RACK = col("#8a8a96")
UPOLE = col("#2a2a36")
COAT = col("#f2c94c")
HOOD = col("#c99a2e")
LEGS = col("#2c2c3e")
BIKE = col("#c9d2de")
TIRE = col("#14141c")
HUB = col("#7a7a88")
CLERK = col("#2c2030")
COUNTER = col("#a5763e")
SIDE = col("#4a4a5e")
CURB = col("#5d5d70")
STREET = col("#1e1e30")
PUD = col("#2a3b5e")
PUDM = col("#455a86")
REFL = col("#e0ae58")
G1 = col("#2a3d70")
G2 = col("#4a5f9a")
G3 = col("#8a86a0")
HEAD = col("#fff7c8")
LPOLE = col("#2e3248")
BIN = col("#5a5a66")
BINL = col("#6e6e7a")
REFL_R = col("#ff5544")
LITEWET = col("#8a6a3e")

# ---------- sky ----------
c.rect(0, 0, 64, 64, SKY)

# ---------- streetlight (glow drawn behind the building) ----------
c.circle(12, 19, 8, G1)
c.circle(12, 19, 6, G2)
c.circle(12, 19, 4, G3)
c.rect(11, 18, 3, 2, HEAD)
c.line(4, 19, 11, 19, LPOLE)
c.rect(4, 19, 1, 24, LPOLE)

# ---------- sidewalk / curb / street ----------
c.rect(0, 44, 64, 5, SIDE)
c.rect(0, 49, 64, 1, CURB)
c.rect(0, 50, 64, 14, STREET)

# warm light pooling on the wet sidewalk
c.rect(22, 44, 15, 4, LITEWET)
c.rect(44, 44, 15, 4, LITEWET)

# ---------- reflective puddles ----------
# puddle under the left window
c.poly([(18, 54), (22, 52), (34, 52), (37, 55), (35, 59), (26, 61), (21, 60), (18, 57)], PUD)
c.poly([(23, 55), (31, 55), (33, 57), (28, 58), (24, 57)], PUDM)
c.line(24, 53, 24, 56, REFL)
c.line(27, 54, 27, 57, REFL)
c.line(30, 54, 30, 58, REFL)
c.line(33, 55, 33, 57, REFL)
# puddle under the right window / door
c.poly([(44, 54), (48, 53), (56, 54), (58, 57), (54, 60), (47, 61), (44, 58)], PUD)
c.poly([(47, 56), (53, 56), (54, 58), (50, 59), (47, 58)], PUDM)
c.line(47, 55, 47, 58, REFL)
c.line(50, 55, 50, 59, REFL)
c.line(53, 55, 53, 58, REFL)
# puddle under the streetlight
c.poly([(8, 57), (14, 55), (18, 57), (16, 60), (10, 61)], PUD)
c.line(12, 56, 12, 59, REFL)

# ---------- building ----------
c.rect(18, 6, 46, 39, WALL)
c.rect(16, 4, 48, 4, PARA)
c.rect(24, 7, 36, 6, SIGNGLOW)
c.rect(26, 8, 32, 4, SIGN)

# left window: bright interior, shelves with goods
c.rect(20, 14, 17, 14, INT)
c.rect(20, 25, 17, 2, INTD)
c.line(20, 18, 36, 18, SHELF)
c.line(20, 23, 36, 23, SHELF)
c.rect(22, 16, 2, 2, ITEM_R)
c.rect(27, 16, 2, 2, ITEM_B)
c.rect(32, 16, 2, 2, ITEM_G)
c.rect(24, 21, 2, 2, ITEM_G)
c.rect(30, 21, 2, 2, ITEM_R)
c.line(28, 14, 28, 27, FRAME)
c.rect(20, 14, 17, 14, FRAME, fill=False)

# right window: clerk behind the counter
c.rect(44, 14, 15, 14, INT)
c.rect(49, 16, 4, 3, CLERK)
c.rect(48, 19, 6, 4, CLERK)
c.rect(45, 23, 13, 4, COUNTER)
c.line(51, 14, 51, 27, FRAME)
c.rect(44, 14, 15, 14, FRAME, fill=False)

# awning (striped canopy)
for i in range(12):
    sx = 18 + i * 4
    w = min(4, 64 - sx)
    c.rect(sx, 30, w, 3, AWN_R if i % 2 == 0 else AWN_W)
c.rect(18, 33, 46, 1, AWN_S)
c.rect(18, 34, 46, 11, LWALL)

# umbrella rack with a few umbrellas
c.rect(28, 35, 8, 1, RACK)
c.rect(28, 36, 1, 7, RACK)
c.rect(35, 36, 1, 7, RACK)
c.rect(27, 42, 10, 1, RACK)
for ux, uc in ((30, ITEM_R), (32, ITEM_B), (34, ITEM_G)):
    c.set(ux, 33, uc)
    c.set(ux - 1, 34, uc)
    c.set(ux + 1, 34, uc)
    c.line(ux, 35, ux, 41, UPOLE)

# door
c.rect(42, 34, 9, 11, DFRAME)
c.rect(43, 35, 7, 9, DGLASS)
c.rect(47, 39, 1, 3, DFRAME)

# trash bin at the side
c.rect(21, 38, 3, 5, BIN)
c.rect(20, 37, 5, 1, BINL)

# person in a raincoat entering the store
c.rect(39, 34, 6, 3, HOOD)
c.set(41, 35, LEGS)
c.rect(39, 37, 6, 6, COAT)
c.rect(40, 43, 2, 2, LEGS)
c.rect(43, 43, 2, 2, LEGS)

# parked bicycle
c.circle(9, 42, 3, TIRE, fill=False)
c.set(9, 42, HUB)
c.circle(16, 42, 3, TIRE, fill=False)
c.set(16, 42, HUB)
c.poly([(12, 37), (16, 38), (16, 42), (11, 42)], BIKE, fill=False)
c.rect(11, 36, 4, 1, BIKE)
c.line(16, 36, 18, 38, BIKE)
c.set(11, 37, REFL_R)

# ---------- rain over everything ----------
for band in range(0, 60, 8):
    off = 3 if (band // 8) % 2 else 0
    for i in range(0, 60, 6):
        c.line(i + off, band, i + off + 4, band + 4, RAIN)

print(c.stats_text())
print("colors used:", len(c.palette()))

finish(c)
