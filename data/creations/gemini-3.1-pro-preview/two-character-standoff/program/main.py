import sys
from pixelbench_api import *

c = new_canvas(128, 128)

# SKY
sky_colors = ['#0a0514', '#100820', '#1a0b2e', '#25123a', '#301644', '#3b1a4a', '#4a1e50', '#5a2455']
for y in range(96):
    idx = int((y / 96) ** 1.5 * (len(sky_colors) - 1))
    c.line(0, y, 127, y, c.color(sky_colors[idx]))

# STARS
stars = [(10, 20), (25, 10), (40, 30), (80, 15), (100, 25), (115, 10), (120, 40), (5, 45)]
for sx, sy in stars:
    c.set(sx, sy, c.color('#ffffff'))
    if (sx + sy) % 2 == 0:
        c.set(sx+1, sy, c.color('#aaaaaa'))
        c.set(sx, sy+1, c.color('#aaaaaa'))
        c.set(sx-1, sy, c.color('#aaaaaa'))
        c.set(sx, sy-1, c.color('#aaaaaa'))

# SUN
sun_colors = ['#aa2222', '#cc3322', '#ee4422', '#ff6622', '#ff8833', '#ffaa44', '#ffcc55', '#ffee66']
radii = [32, 28, 24, 20, 16, 12, 8, 4]
for r, col in zip(radii, sun_colors):
    c.circle(64, 72, r, c.color(col))

# GROUND
ground_colors = ['#15081a', '#100514', '#0a030c', '#050106']
for y in range(96, 128):
    idx = int(((y - 96) / 32) * (len(ground_colors) - 1))
    c.line(0, y, 127, y, c.color(ground_colors[idx]))

# HILLS
c.path("M 0 96 Q 20 85 40 96 Z", c.color('#15081a'))
c.path("M 90 96 Q 110 80 128 96 Z", c.color('#15081a'))
c.path("M 30 96 Q 60 90 80 96 Z", c.color('#100514'))

# SHADOWS
c.ellipse(35, 112, 16, 3, c.color('#000000'))
c.ellipse(93, 112, 16, 3, c.color('#000000'))

# PALETTES
K_DARK = c.color('#330000')
K_MID = c.color('#660000')
K_RIM = c.color('#ff5522')

M_DARK = c.color('#111122')
M_MID = c.color('#333344')
M_RIM = c.color('#ffeeaa')

R_DARK = c.color('#001a0a')
R_MID = c.color('#004411')
R_RIM = c.color('#88ff44')

L_DARK = c.color('#1a0f05')
L_MID = c.color('#331a00')
L_RIM = c.color('#ffaa33')

# KNIGHT (Left)
# Cape
c.path("M 35 55 C 20 50 5 70 10 95 C 20 90 25 85 35 80 Z", K_DARK)
c.path("M 35 55 C 25 55 15 70 18 95 C 25 90 28 85 35 80 Z", K_MID)
# Back Arm
c.poly([(38, 52), (48, 60), (45, 65), (35, 57)], K_DARK)
# Back Leg
c.poly([(38, 75), (44, 75), (46, 110), (38, 110)], M_DARK)
c.poly([(42, 75), (44, 75), (46, 110), (44, 110)], M_RIM)
# Front Leg
c.poly([(28, 75), (36, 75), (34, 112), (24, 112)], M_MID)
c.poly([(34, 75), (36, 75), (34, 112), (32, 112)], M_RIM)
# Torso
c.poly([(28, 50), (42, 50), (38, 80), (28, 80)], K_MID)
c.poly([(38, 50), (42, 50), (38, 80), (36, 80)], K_RIM)
c.line(32, 60, 40, 60, K_DARK)
c.line(34, 70, 42, 70, K_DARK)
# Belt
c.rect(28, 75, 14, 4, L_DARK)
c.rect(34, 75, 4, 4, c.color('#ddaa22'))
# Head
c.rect(28, 35, 14, 16, M_MID)
c.rect(38, 35, 4, 16, M_RIM)
c.circle(35, 35, 7, M_MID)
c.circle(38, 35, 4, M_RIM)
c.rect(30, 40, 12, 3, c.color('#000000'))
c.rect(38, 40, 2, 3, c.color('#ffffff'))
# Plume
c.path("M 35 30 C 35 15 20 10 10 20 C 20 25 25 30 35 30 Z", K_MID)
c.path("M 35 30 C 35 15 25 13 18 20 C 25 25 28 30 35 30 Z", K_RIM)
# Front Arm
c.poly([(28, 52), (40, 65), (35, 70), (25, 57)], K_MID)
c.poly([(36, 58), (40, 65), (35, 70), (31, 63)], K_RIM)
# Shoulder Pad
c.circle(32, 52, 7, K_MID)
c.poly([(32, 45), (39, 52), (37, 54), (32, 47)], K_RIM)
# Sword
c.poly([(37, 69), (41, 65), (55, 85), (51, 89)], M_MID)
c.poly([(39, 67), (41, 65), (55, 85), (53, 87)], M_RIM)
c.poly([(34, 72), (44, 62), (46, 64), (36, 74)], c.color('#ddaa22'))
c.poly([(42, 64), (44, 62), (46, 64), (44, 66)], c.color('#ffffff'))
c.poly([(33, 63), (39, 69), (37, 71), (31, 65)], c.color('#885511'))
c.line(55, 85, 58, 88, M_RIM)
# Hand
c.circle(38, 68, 4, M_MID)
c.circle(40, 68, 2, M_RIM)

# ROGUE (Right)
# Cape
c.path("M 93 55 C 108 50 123 70 118 95 C 108 90 103 85 93 80 Z", R_DARK)
c.path("M 93 55 C 103 55 113 70 110 95 C 103 90 100 85 93 80 Z", R_MID)
# Back Arm
c.poly([(96, 52), (106, 60), (103, 65), (93, 57)], R_DARK)
# Back Leg
c.poly([(84, 75), (90, 75), (88, 110), (80, 110)], L_DARK)
c.poly([(84, 75), (86, 75), (84, 110), (80, 110)], L_RIM)
# Front Leg
c.poly([(92, 75), (100, 75), (104, 112), (94, 112)], L_MID)
c.poly([(92, 75), (94, 75), (96, 112), (94, 112)], L_RIM)
# Torso
c.poly([(86, 50), (100, 50), (96, 80), (86, 80)], R_MID)
c.poly([(86, 50), (89, 50), (89, 80), (86, 80)], R_RIM)
c.line(90, 60, 96, 65, R_DARK)
c.line(88, 70, 94, 75, R_DARK)
# Belt
c.rect(86, 75, 14, 4, L_DARK)
c.rect(90, 75, 4, 4, M_MID)
# Head
c.poly([(85, 35), (95, 35), (100, 55), (80, 55)], R_MID)
c.poly([(85, 35), (88, 35), (83, 55), (80, 55)], R_RIM)
c.circle(90, 40, 6, R_MID)
c.circle(87, 40, 3, R_RIM)
c.poly([(82, 45), (92, 45), (90, 55), (84, 55)], c.color('#050505'))
c.circle(86, 50, 1, c.color('#00ff00'))
# Scarf
c.poly([(80, 55), (95, 55), (98, 62), (85, 62)], R_DARK)
c.poly([(80, 55), (83, 55), (86, 62), (85, 62)], R_RIM)
c.path("M 95 45 C 105 40 115 45 120 35 C 110 40 105 45 95 45 Z", R_DARK)
c.path("M 95 45 C 100 42 105 45 110 38 C 105 42 100 45 95 45 Z", R_RIM)
# Front Arm
c.poly([(90, 52), (78, 65), (83, 70), (95, 57)], R_MID)
c.poly([(88, 57), (83, 70), (78, 65), (83, 60)], R_RIM)
# Dagger
c.poly([(79, 67), (77, 71), (68, 75), (70, 71)], M_MID)
c.poly([(79, 67), (78, 69), (68, 75), (69, 73)], M_RIM)
c.poly([(76, 66), (82, 72), (80, 74), (74, 68)], c.color('#333333'))
c.poly([(76, 66), (78, 68), (76, 70), (74, 68)], M_RIM)
c.poly([(80, 70), (86, 64), (88, 66), (82, 72)], L_DARK)
c.line(68, 75, 65, 77, M_RIM)
# Hand
c.circle(80, 68, 3, c.color('#ffccaa'))

# SPARKS
sparks = [
    (30, 90), (20, 85), (45, 100), (35, 80), (15, 95), (25, 85), (10, 105),
    (98, 90), (108, 85), (83, 100), (93, 80), (113, 95), (103, 85), (118, 105),
    (50, 60), (78, 55), (60, 50), (68, 40), (55, 45), (73, 65)
]
for px, py in sparks:
    c.set(px, py, K_RIM)
    c.set(px+1, py, c.color('#ffffff'))

finish(c)
