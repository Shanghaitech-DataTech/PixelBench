from pixelbench_api import *

BLACK = (0, 0, 0)
CHAR = (26, 26, 30)
DG = (46, 46, 52)
MG = (92, 94, 102)
SV = (168, 172, 182)
BR = (214, 219, 228)
HUB = (124, 128, 136)
RED = (222, 30, 36)
BRED = (255, 70, 80)
W = (242, 244, 248)
TR = (74, 76, 84)

c = new_canvas(128, 128)


def wheel(cx, cy):
    c.circle(cx, cy, 20, BLACK)
    c.circle(cx, cy, 13, SV)
    c.line(cx - 12, cy, cx + 12, cy, W)
    c.line(cx, cy - 12, cx, cy + 12, W)
    c.line(cx - 9, cy - 9, cx + 9, cy + 9, W)
    c.line(cx - 9, cy + 9, cx + 9, cy - 9, W)
    c.circle(cx, cy, 7, HUB)
    c.circle(cx, cy, 2, CHAR)
    c.path(f"M {cx - 14},{cy - 6} A 17,17 0 0 1 {cx + 7},{cy - 14}", TR, fill=False)


wheel(44, 92)
wheel(97, 92)

# swingarm (behind body)
c.poly([(54, 78), (63, 83), (47, 95), (40, 89)], CHAR)
c.line(46, 88, 60, 80, MG)

# front fork uppers (behind body, visible above fairing)
c.poly([(92, 92), (100, 91), (90, 41), (83, 40)], SV)
# handlebar + mirror
c.poly([(83, 35), (95, 40), (93, 45), (88, 41)], BLACK)
c.rect(81, 31, 4, 6, BLACK)
# front fender
c.ellipse(95, 64, 14, 4, BLACK)

# main fairing body
c.poly([(95, 44), (103, 49), (106, 58), (104, 69), (95, 79), (76, 85), (52, 85),
       (40, 78), (31, 66), (23, 53), (17, 44), (18, 40), (27, 46), (36, 52),
       (49, 55), (62, 53), (78, 49), (89, 45)], DG)

# windscreen (black, tilted)
c.poly([(84, 33), (95, 38), (98, 47), (89, 44)], BLACK)

# seat
c.poly([(31, 50), (48, 54), (46, 57), (29, 53)], BLACK)

# red swoosh accent
c.poly([(96, 59), (92, 66), (76, 71), (58, 73), (40, 67), (33, 61),
        (36, 55), (50, 57), (66, 62), (84, 60)], RED)

# dark lower cowl
c.poly([(94, 69), (78, 77), (56, 79), (40, 71), (34, 64), (38, 60),
        (46, 63), (62, 68), (82, 70)], CHAR)

# round engine cover
c.circle(58, 72, 9, MG)
c.circle(58, 72, 5, BR)
c.circle(58, 72, 2, CHAR)

# silver tubular frame rails
c.line(86, 46, 57, 57, SV)
c.line(84, 47, 55, 58, SV)
c.line(88, 49, 60, 78, SV)
c.line(86, 50, 58, 79, SV)
c.line(58, 56, 38, 67, MG)

# exhaust stub
c.line(56, 76, 52, 81, MG)
c.rect(20, 78, 10, 4, MG)
c.line(20, 78, 30, 78, BR)

# tail light
c.poly([(13, 37), (19, 36), (19, 44), (14, 45)], RED)
c.poly([(15, 38), (18, 37), (18, 43), (15, 44)], BRED)

# nose headlight (front)
c.poly([(98, 46), (106, 51), (105, 59), (97, 53)], CHAR)
c.poly([(100, 49), (104, 53), (103, 57), (99, 53)], BR)

# rear muffler (silver canister along bottom)
c.poly([(24, 79), (40, 82), (42, 87), (27, 85)], SV)
c.poly([(24, 79), (29, 80), (29, 85), (27, 85)], CHAR)
c.rect(22, 81, 3, 3, MG)
c.line(22, 82, 41, 83, BR)
# tank dark edge + red pinstripe
c.line(62, 52, 76, 49, RED)
c.poly([(76, 48), (88, 45), (87, 47), (75, 50)], BLACK)
# top highlights
c.line(88, 45, 70, 49, BR)
c.line(70, 49, 52, 54, MG)

print(c.stats_text())
finish(c)
