from pixelbench_api import *

def C(rgba):
    return input_canvas.color(rgba)

BLACK   = C((16, 16, 16, 255))
WHITE   = C((255, 255, 255, 255))
CREAM   = C((255, 227, 140, 255))
STEEL   = C((133, 128, 134, 255))
DARKA   = C((51, 45, 50, 255))
MAIL    = C((90, 86, 90, 255))
GRIP    = C((115, 74, 41, 255))
HILTG   = C((209, 181, 99, 255))
GOLD   = C((255, 204, 67, 255))
LEGDARK = C((47, 16, 16, 255))
SHADOW  = C((23, 0, 53, 153))
GREY   = C((169, 165, 171, 255))
CAPE   = C((63, 0, 22, 255))     # h
CAPE2  = C((85, 0, 42, 255))     # L

f1 = input_canvas.copy(name="f1")
f2 = input_canvas.copy(name="f2")

# ---------------- surgical erasure of the old raised arm & hanging sword ----
f2.clear(29, 9, 14, 5)     # upraised blade above/behind head: x29-42, rows 9-13
f2.clear(24, 14, 19, 20)   # old arm + hand: x24-42, rows 14-33
f2.clear(17, 34, 22, 21)   # old hanging sword over lower body: x17-38, rows 34-54

# ---------------- cape / torso right edge (rows 34-47) -------------------
cape_rows = [
    (34, 23, 28, [BLACK, CAPE2, CAPE, CAPE2, CAPE, BLACK]),
    (35, 23, 28, [BLACK, CAPE, CAPE2, CAPE, CAPE, BLACK]),
    (36, 23, 28, [BLACK, CAPE2, CAPE, CAPE2, CAPE, BLACK]),
    (37, 23, 28, [BLACK, CAPE, CAPE2, CAPE, CAPE, BLACK]),
    (38, 23, 28, [BLACK, CAPE2, CAPE, CAPE, CAPE, BLACK]),
    (39, 23, 28, [BLACK, CAPE, CAPE2, CAPE, CAPE, BLACK]),
    (40, 23, 28, [BLACK, CAPE2, CAPE, CAPE, CAPE, BLACK]),
    (41, 23, 28, [BLACK, CAPE, CAPE2, CAPE, CAPE, BLACK]),
    (42, 23, 28, [BLACK, CAPE2, CAPE, CAPE, CAPE, BLACK]),
    (43, 23, 28, [BLACK, CAPE, CAPE2, CAPE, CAPE, BLACK]),
    (44, 23, 28, [BLACK, CAPE2, CAPE, CAPE, CAPE, BLACK]),
    (45, 23, 28, [BLACK, CAPE, CAPE, CAPE, CAPE, BLACK]),
    (46, 22, 27, [BLACK, CAPE2, CAPE, CAPE, BLACK]),
    (47, 22, 26, [CAPE, CAPE, CAPE, CAPE, BLACK]),
]
for (y, x0, x1, cols) in cape_rows:
    for k, ck in enumerate(cols):
        f2.set(x0 + k, y, ck)

# ---------------- right (back) leg, braced ---------------------------------
rleg = [
    (44, 15, 23, [BLACK, MAIL, MAIL, MAIL, MAIL, GREY, MAIL, BLACK]),
    (45, 15, 23, [BLACK, MAIL, GREY, MAIL, GREY, MAIL, GREY, BLACK]),
    (46, 16, 23, [MAIL, GREY, GREY, MAIL, GREY, MAIL, GREY]),
    (47, 16, 23, [MAIL, GREY, STEEL, GREY, STEEL, GREY, BLACK]),
    (48, 18, 23, [BLACK, MAIL, MAIL, MAIL, GREY, BLACK]),
    (49, 18, 24, [BLACK, MAIL, MAIL, GREY, GREY, MAIL, BLACK]),
    (50, 18, 24, [BLACK, MAIL, GREY, GREY, GREY, GREY, BLACK]),
    (51, 19, 25, [BLACK, GREY, STEEL, GREY, STEEL, GREY, BLACK]),
    (52, 19, 25, [BLACK, GREY, STEEL, GREY, STEEL, GREY, BLACK]),
    (53, 20, 24, [BLACK, GREY, GREY, GREY, GREY, BLACK]),
    (54, 21, 25, [BLACK, GREY, GREY, GREY, BLACK]),
    (55, 22, 25, [BLACK, GREY, GREY, BLACK]),
    (56, 23, 26, [BLACK, GREY, GREY, BLACK]),
    (57, 24, 26, [BLACK, GREY, BLACK]),
]
for (y, x0, x1, cols) in rleg:
    for k, ck in enumerate(cols):
        f2.set(x0 + k, y, ck)

# ---------------- left (forward) leg, stepped forward ----------------------
f2.clear(3, 48, 17, 12)   # erase old lower-left leg, x3-19, rows 48-59
lleg = [
    (48, 5, 11, [BLACK, LEGDARK, LEGDARK, LEGDARK, BLACK]),
    (49, 4, 10, [BLACK, LEGDARK, LEGDARK, LEGDARK, BLACK]),
    (50, 3, 10, [BLACK, LEGDARK, LEGDARK, LEGDARK, LEGDARK, BLACK]),
    (51, 2, 9,  [BLACK, GREY, LEGDARK, LEGDARK, LEGDARK, BLACK]),
    (52, 1, 9,  [BLACK, GREY, LEGDARK, GOLD, LEGDARK, GOLD, GREY, BLACK]),
    (53, 1, 9,  [BLACK, GOLD, GOLD, GOLD, CREAM, GOLD, GREY, BLACK]),
    (54, 1, 9,  [BLACK, GOLD, GOLD, GOLD, GOLD, GOLD, GREY, BLACK]),
    (55, 1, 8,  [BLACK, GOLD, GOLD, GOLD, GOLD, GREY, BLACK]),
    (56, 0, 7,  [BLACK, GOLD, GOLD, GREY, GREY, BLACK]),
    (57, 0, 6,  [BLACK, GREY, GREY, GREY, GREY, BLACK]),
    (58, 0, 5,  [BLACK, GREY, GREY, GREY, BLACK]),
]
for (y, x0, x1, cols) in lleg:
    for k, ck in enumerate(cols):
        f2.set(x0 + k, y, ck)

# ---------------- arm coming down beside the body --------------------------
arm = [
    (26, 20, 27, [BLACK, DARKA, DARKA, DARKA, DARKA, DARKA, BLACK]),
    (27, 19, 27, [BLACK, DARKA, DARKA, DARKA, DARKA, DARKA, DARKA, BLACK]),
    (28, 20, 27, [BLACK, DARKA, DARKA, DARKA, DARKA, DARKA, BLACK]),
    (29, 20, 27, [BLACK, DARKA, DARKA, DARKA, DARKA, DARKA, BLACK]),
    (30, 20, 27, [BLACK, DARKA, DARKA, MAIL, DARKA, DARKA, BLACK]),
    (31, 20, 26, [BLACK, MAIL, MAIL, MAIL, MAIL, BLACK]),
    (32, 20, 26, [BLACK, MAIL, CREAM, CREAM, MAIL, BLACK]),
    (33, 19, 26, [BLACK, MAIL, CREAM, CREAM, MAIL, BLACK]),
    (34, 19, 25, [BLACK, GRIP, GRIP, GRIP, GRIP, BLACK]),
    (35, 18, 25, [BLACK, GRIP, GRIP, GRIP, GRIP, BLACK]),
    (36, 18, 24, [BLACK, HILTG, HILTG, HILTG, BLACK]),
]
for (y, x0, x1, cols) in arm:
    for k, ck in enumerate(cols):
        f2.set(x0 + k, y, ck)

# ---------------- sword in hand, blade pointing down to the ground -----------
blade = [
    (37, 17, 21, [WHITE, STEEL, STEEL, BLACK]),
    (38, 16, 20, [WHITE, STEEL, STEEL, BLACK]),
    (39, 16, 20, [WHITE, STEEL, STEEL, BLACK]),
    (40, 15, 19, [WHITE, STEEL, STEEL, BLACK]),
    (41, 15, 19, [WHITE, STEEL, STEEL, BLACK]),
    (42, 14, 18, [WHITE, STEEL, STEEL, BLACK]),
    (43, 14, 18, [WHITE, STEEL, STEEL, BLACK]),
    (44, 13, 16, [WHITE, STEEL, STEEL]),
    (45, 13, 16, [WHITE, STEEL, STEEL]),
    (46, 12, 15, [WHITE, STEEL, STEEL]),
    (47, 12, 15, [WHITE, STEEL, STEEL]),
    (48, 11, 14, [WHITE, STEEL]),
    (49, 11, 14, [WHITE, STEEL]),
    (50, 10, 13, [WHITE, STEEL]),
    (51, 10, 13, [WHITE]),
    (52, 9, 12,  [WHITE]),
    (53, 9, 12,  [WHITE]),
    (54, 8, 8,   [WHITE]),
    (55, 8, 8,   [WHITE]),
]
for (y, x0, x1, cols) in blade:
    for k, ck in enumerate(cols):
        f2.set(x0 + k, y, ck)

# ---------------- white motion trail streaming out behind the swing ----------
trail = [
    (9,  41, 40, [WHITE]),
    (11, 39, 38, [WHITE]),
    (13, 37, 36, [WHITE, CREAM]),
    (15, 35, 34, [WHITE, CREAM]),
    (17, 33, 32, [WHITE, CREAM]),
    (19, 31, 30, [WHITE, CREAM]),
    (21, 29, 28, [WHITE, CREAM]),
    (23, 27, 26, [WHITE, CREAM]),
    (25, 26, 25, [WHITE, CREAM]),
    (27, 25, 24, [WHITE, CREAM]),
    (29, 24, 23, [WHITE, CREAM]),
    (31, 23, 22, [WHITE, CREAM]),
    (33, 21, 20, [WHITE]),
]
for (y, x1, x0, cols) in trail:
    for k, ck in enumerate(cols):
        f2.set(x0 + k, y, ck)
for (y, xs) in [(8, [42]), (10, [38, 36]), (12, [35, 34]), (14, [33]), (16, [31]), (18, [29])]:
    for x in xs:
        f2.set(x, y, WHITE)

# ---------------- ground shadow under the forward foot ----------------------
for y in range(56, 61):
    for x in range(0, 13):
        f2.set(x, y, SHADOW)

print("== F2 full ==")
print(f2.matrix_text(region=(0, 0, 42, 60)))

finish([f1, f2])

