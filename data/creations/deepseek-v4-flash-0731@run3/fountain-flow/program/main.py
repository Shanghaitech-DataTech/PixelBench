from pixelbench_api import *

out = input_canvas.copy(name="output")

w_main = out.color("#2f8fe0", "water")
w_light = out.color("#7cc4f2", "water_light")
foam = out.color("#ffffff", "foam")


def fill_row(y, x0, x1, c):
    for x in range(x0, x1 + 1):
        out.set(x, y, c)


# ---------------- top basin water ----------------
top = {
    13: (26, 35), 14: (23, 39), 15: (22, 41), 16: (22, 41), 17: (24, 38),
    18: (25, 37), 19: (26, 36), 20: (26, 36), 21: (25, 37), 22: (25, 37),
    23: (26, 37), 24: (27, 37), 25: (26, 38), 26: (25, 38), 27: (28, 36),
    28: (29, 35),
}
for y, (a, b) in top.items():
    fill_row(y, a, b, w_main)
for y in (13, 14, 15, 16):
    fill_row(y, top[y][0], top[y][1], w_light)

# ---------------- water jet from the fountain top ----------------
for y in range(0, 14):
    out.set(31, y, w_light)
    out.set(32, y, w_light)
for y in range(2, 11):
    out.set(30, y, w_light)
    out.set(33, y, w_light)
for (x, y) in [(29, 3), (34, 3), (29, 4), (34, 4), (29, 5), (34, 5),
               (28, 4), (35, 4), (28, 6), (35, 6), (27, 5), (36, 5)]:
    out.set(x, y, w_light)
# foam crown at the spray
for (x, y) in [(30, 0), (31, 0), (32, 0), (33, 0), (29, 1), (34, 1),
               (28, 2), (35, 2), (27, 1), (36, 1), (28, 3), (35, 3)]:
    out.set(x, y, foam)
# splashes where the jet meets the top water
for (x, y) in [(27, 11), (36, 11), (26, 12), (37, 12), (26, 13), (37, 13)]:
    out.set(x, y, foam)

# ---------------- overflow cascades: top bowl -> middle bowl ----------------
sheetL = {
    14: (15, 17), 15: (15, 17), 16: (15, 17), 17: (15, 17), 18: (15, 17),
    19: (16, 18), 20: (16, 18), 21: (16, 18), 22: (16, 18), 23: (16, 18),
    24: (16, 18), 25: (16, 18), 26: (16, 18), 27: (17, 19), 28: (16, 18),
    29: (16, 18), 30: (16, 18), 31: (16, 18), 32: (15, 18), 33: (14, 18),
}
for y, (a, b) in sheetL.items():
    fill_row(y, a, b, w_main)
    fill_row(y, 63 - b, 63 - a, w_main)

# ---------------- middle basin water ----------------
mid = {
    34: (22, 40), 35: (21, 42), 36: (21, 43), 37: (21, 43), 38: (21, 43),
    39: (21, 43), 40: (21, 44), 41: (21, 44), 42: (22, 44), 43: (22, 44),
    44: (23, 44), 45: (23, 43), 46: (23, 42), 47: (24, 42), 48: (24, 42),
    49: (25, 41), 50: (26, 40), 51: (26, 39), 52: (27, 39), 53: (28, 38),
}
for y, (a, b) in mid.items():
    fill_row(y, a, b, w_main)
for y in (34, 35):
    fill_row(y, mid[y][0], mid[y][1], w_light)
# shimmer lines on the middle water
for x in range(24, 31):
    out.set(x, 40, w_light)
for x in range(33, 40):
    out.set(x, 40, w_light)
for x in range(25, 32):
    out.set(x, 44, w_light)
for x in range(35, 40):
    out.set(x, 44, w_light)
out.set(27, 36, w_light)
out.set(36, 36, w_light)
out.set(28, 39, w_light)
out.set(35, 39, w_light)
# foam where the cascades land
for (x, y) in [(16, 33), (17, 34), (46, 33), (47, 34), (15, 35), (48, 35)]:
    out.set(x, y, foam)

finish(out)
