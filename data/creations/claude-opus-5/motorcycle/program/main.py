import math

c = new_canvas(128, 128, name="output")

BLK = c.color("#141418", "blk")
BLK2 = c.color("#23242b", "blk2")
BLK3 = c.color("#0b0b0e", "blk3")
DG = c.color("#2f3138", "dg")
DG2 = c.color("#43454f", "dg2")
DG3 = c.color("#565a66", "dg3")
SIL = c.color("#b9bec6", "sil")
SIL2 = c.color("#8d939c", "sil2")
SIL3 = c.color("#e4e8ec", "sil3")
RED = c.color("#c8202a", "red")
RED2 = c.color("#ff4a46", "red2")
WHT = c.color("#f2f4f6", "wht")
GRY = c.color("#6b7079", "gry")

RWX, RWY = 30, 92
FWX, FWY = 102, 92
R = 16


def hub(cx, cy):
    c.circle(cx, cy, 11, GRY)
    for i in range(12):
        a = i * math.pi / 6 + 0.26
        c.line(cx, cy, int(round(cx + 10 * math.cos(a))),
               int(round(cy + 10 * math.sin(a))), WHT)
    c.circle(cx, cy, 4, SIL2)
    c.circle(cx, cy, 2, SIL)
    c.set(cx - 1, cy - 1, SIL3)


def wheel(cx, cy):
    c.circle(cx, cy, R, BLK3)
    c.circle(cx, cy, R - 1, BLK2)
    c.circle(cx, cy, 12, BLK)
    hub(cx, cy)


def arcband(cx, cy, a0, a1, radii, col):
    for d in range(a0 * 4, a1 * 4 + 1):
        a = math.radians(d / 4.0)
        for r in radii:
            c.set(int(round(cx + r * math.cos(a))),
                  int(round(cy + r * math.sin(a))), col)


wheel(RWX, RWY)
wheel(FWX, FWY)

# ---- rear hugger ----
arcband(RWX, RWY, 232, 300, (17, 18), DG)

# ---- chain + sprocket ----
c.line(34, 88, 58, 78, DG2)
c.line(34, 90, 58, 80, DG)
c.circle(30, 92, 6, DG2, fill=False)

# ---- swingarm ----
c.poly([(56, 79), (59, 81), (33, 93), (31, 91)], SIL2)
c.line(56, 80, 32, 92, SIL)
c.circle(30, 92, 2, SIL)

# ---- exhaust: compact can tucked under the tail ----
c.poly([(50, 75), (53, 77), (45, 81), (43, 79)], DG2)
c.poly([(45, 76), (48, 79), (41, 83), (38, 80)], SIL2)
c.poly([(39, 78), (43, 80), (39, 84), (36, 81)], SIL)
c.set(36, 82, SIL3)
c.set(36, 83, GRY)

# ---- silver tubular frame ----
c.poly([(92, 54), (96, 58), (60, 78), (56, 74)], SIL2)
c.poly([(92, 55), (94, 58), (59, 77), (57, 75)], SIL)
c.poly([(52, 64), (58, 64), (59, 80), (53, 80)], SIL2)
c.line(54, 66, 55, 78, SIL)
c.poly([(44, 62), (49, 64), (47, 78), (42, 76)], SIL2)
c.poly([(45, 66), (48, 67), (46, 74), (43, 73)], RED)

# ---- engine ----
c.poly([(60, 64), (84, 62), (92, 74), (84, 86), (64, 86), (56, 76)], DG)
c.poly([(62, 67), (82, 65), (88, 74), (80, 83), (66, 83)], BLK2)
for i in range(4):
    c.line(66 + i * 4, 64, 64 + i * 4, 71, DG3)
# round silver gray engine cover
c.circle(73, 75, 7, SIL2)
c.circle(73, 75, 5, SIL)
c.circle(73, 75, 2, SIL2)
c.set(71, 73, SIL3)
c.set(72, 72, SIL3)

# ---- belly pan ----
c.poly([(58, 79), (76, 88), (92, 84), (99, 75), (99, 86), (78, 93), (60, 87)], DG)
c.poly([(63, 84), (78, 89), (92, 85), (92, 88), (78, 90), (65, 87)], BLK2)
c.poly([(66, 86), (80, 88), (91, 85), (91, 87), (80, 89), (67, 87)], RED)

# ---- upswept tail + seat (one mass over the rear wheel) ----
c.poly([(24, 54), (33, 54), (48, 59), (60, 62), (69, 64), (69, 73),
        (56, 72), (42, 68), (30, 63), (25, 60)], BLK)
c.poly([(27, 56), (33, 56), (47, 61), (58, 64), (64, 66), (62, 68),
        (49, 65), (35, 61), (27, 58)], DG)
c.poly([(28, 57), (33, 57), (47, 62), (56, 64), (57, 66), (47, 64),
        (34, 60), (28, 58)], RED)
c.line(30, 58, 38, 60, RED2)
# tail light on the rear face
c.poly([(21, 54), (25, 55), (26, 61), (22, 60)], RED2)
c.poly([(22, 56), (24, 56), (25, 58), (22, 58)], SIL3)
c.set(21, 59, RED)
c.set(25, 54, RED)
# undertail skirt, filling over the rear wheel
c.poly([(30, 62), (46, 68), (60, 72), (58, 78), (44, 72), (31, 66)], BLK2)
c.poly([(35, 65), (48, 70), (55, 73), (54, 76), (45, 71), (36, 67)], DG)
# seat pad
c.poly([(50, 59), (66, 60), (70, 65), (56, 64)], BLK)
c.poly([(52, 60), (64, 61), (66, 63), (55, 62)], BLK2)

# ---- tank ----
c.poly([(64, 59), (76, 53), (88, 52), (97, 57), (98, 65), (80, 68), (66, 64)], BLK)
c.poly([(70, 55), (86, 54), (93, 58), (82, 61), (68, 60)], BLK2)
c.poly([(72, 56), (87, 56), (89, 59), (76, 60)], RED)
c.line(74, 57, 86, 57, RED2)

# ---- front fork ----
c.poly([(88, 55), (94, 53), (99, 74), (93, 76)], SIL2)
c.poly([(89, 56), (92, 55), (97, 74), (94, 75)], SIL)
c.poly([(93, 72), (99, 70), (104, 90), (98, 92)], SIL)
c.poly([(94, 74), (97, 73), (101, 88), (98, 88)], SIL3)
c.poly([(98, 86), (104, 85), (105, 92), (99, 93)], SIL2)
# front brake disc, then hub back on top
c.circle(102, 92, 9, SIL2)
hub(102, 92)

# ---- front fender ----
arcband(FWX, FWY, 198, 334, (17, 18, 19), DG)
arcband(FWX, FWY, 208, 314, (19,), DG2)

# ---- wide dark gray fairing ----
c.poly([(92, 50), (104, 51), (112, 58), (114, 68), (110, 80), (100, 84),
        (91, 79), (89, 62), (90, 53)], DG)
c.poly([(94, 52), (103, 53), (110, 59), (111, 65), (98, 61), (91, 58)], DG2)
c.poly([(95, 53), (102, 54), (106, 58), (96, 57), (92, 55)], DG3)
# red accent flash
c.poly([(91, 64), (106, 67), (107, 74), (92, 72)], RED)
c.poly([(93, 66), (103, 69), (103, 71), (93, 69)], RED2)
# lower vent
c.poly([(95, 76), (106, 77), (103, 82), (96, 80)], BLK2)
# headlight
c.poly([(109, 56), (114, 61), (115, 68), (109, 63)], SIL3)
c.poly([(110, 58), (113, 62), (113, 65), (110, 61)], WHT)
c.set(114, 66, SIL2)

# ---- tilted small black windscreen ----
c.poly([(98, 44), (103, 42), (110, 52), (105, 54)], BLK2)
c.poly([(100, 45), (103, 44), (108, 52), (105, 53)], BLK)
c.line(99, 45, 106, 53, DG3)
c.line(96, 46, 99, 44, DG2)
c.set(101, 43, DG3)

# handlebar
c.line(87, 51, 93, 50, SIL2)
c.set(86, 51, SIL)

# footpeg
c.line(65, 86, 69, 88, SIL2)
c.set(70, 89, SIL)

c.shift(-3, -12)
print(c.stats_text())
view(c)
finish(c)
