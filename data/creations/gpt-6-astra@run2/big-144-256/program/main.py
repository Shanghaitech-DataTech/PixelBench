import math
import random

result = input_canvas.copy(name='output')
rng = random.Random(39)
ivy = new_canvas(144, 256, name='Climbing ivy')

stem_shadow = '#263f36'
stem = '#53634a'
leaf_dark = '#264638'
leaf_deep = '#315340'
leaf_mid = '#46694b'
leaf_light = '#63815b'
leaf_tip = '#7b9169'


def pixels_on_line(a, b):
    x0, y0 = a
    x1, y1 = b
    n = max(abs(x1 - x0), abs(y1 - y0))
    if not n:
        return [a]
    return [(round(x0 + (x1 - x0) * i / n), round(y0 + (y1 - y0) * i / n)) for i in range(n + 1)]


def leaf(x, y, side=1, small=False, bright=False):
    if small:
        shape = [(0, 0), (1, -1), (2, -1), (2, 1), (1, 1)]
    else:
        shape = [(0, 0), (1, -2), (2, -1), (3, -2), (3, 1), (1, 2)]
    ivy.poly([(x + side * dx, y + dy) for dx, dy in shape], leaf_dark)
    ivy.set(x + side, y, leaf_mid if bright else leaf_deep)
    ivy.set(x + side * 2, y - 1, leaf_light if bright else leaf_mid)
    if not small:
        ivy.set(x + side * 2, y, leaf_mid if bright else leaf_deep)
        ivy.set(x + side * 3, y - 1, leaf_light if bright else leaf_mid)
        if bright and rng.random() < 0.3:
            ivy.set(x + side * 2, y - 1, leaf_tip)


def vine(points, density=0.8, bright=False):
    nodes = []
    for a, b in zip(points, points[1:]):
        ivy.line(a[0] + 1, a[1] + 1, b[0] + 1, b[1] + 1, stem_shadow)
        ivy.line(*a, *b, stem)
        nodes += pixels_on_line(a, b)[:-1]
    for i in range(1, len(nodes), 3):
        if rng.random() > density:
            continue
        x, y = nodes[i]
        side = -1 if rng.random() < 0.5 else 1
        ex, ey = x + side * rng.randint(1, 3), y - rng.randint(0, 2)
        ivy.line(x, y, ex, ey, leaf_deep)
        leaf(ex, ey, side, rng.random() < 0.4, bright or rng.random() < 0.38)
        if rng.random() < 0.23:
            leaf(x - side, y + 1, -side, True, bright)


# The connected root growth follows masonry, with branches along mortar courses.
vine([(35, 218), (36, 205), (35, 192), (38, 180), (37, 168), (41, 156), (40, 145), (43, 134), (41, 124), (43, 114), (41, 103), (44, 93), (43, 84), (49, 77), (52, 70)], 0.94)
vine([(40, 145), (45, 140), (47, 131), (52, 128), (56, 122), (60, 120), (62, 113)], 0.9, True)
vine([(43, 134), (38, 130), (37, 121), (38, 114), (35, 109), (36, 99), (38, 93)], 0.86)
vine([(41, 103), (47, 98), (48, 91), (53, 88), (54, 82), (60, 80), (65, 82), (68, 79)], 0.7)
vine([(47, 131), (53, 136), (61, 136), (65, 132), (67, 128)], 0.76)
vine([(37, 168), (43, 167), (47, 163), (54, 162), (60, 164)], 0.74)
vine([(35, 192), (39, 188), (40, 180), (44, 176)], 0.75)
vine([(36, 205), (32, 201), (33, 195), (31, 191)], 0.84)

# A smaller curtain spills over the roof lip on the right side of the entrance.
vine([(88, 139), (85, 144), (87, 150), (83, 155), (82, 163), (78, 170), (79, 179)], 0.82)
vine([(85, 150), (90, 153), (90, 159), (87, 165), (88, 170)], 0.75)
vine([(83, 155), (77, 157), (74, 160), (70, 159)], 0.67)

# Extra overlapping leaf groups give the ivy patches a dense heart and sparse tips.
for cx, cy, count in [(39, 116, 5), (43, 128, 6), (43, 140, 5), (47, 132, 4), (43, 96, 4), (39, 167, 4), (36, 187, 3), (85, 153, 4), (81, 162, 3)]:
    for k in range(count):
        leaf(cx + rng.randint(-3, 2), cy + rng.randint(-3, 3), rng.choice([-1, 1]), rng.random() < 0.4, rng.random() < 0.45)

vine([(51, 129), (55, 122), (55, 113), (59, 106), (61, 100), (60, 96)], 0.8)
vine([(42, 144), (48, 143), (52, 140), (58, 141)], 0.67)
# Shingled leaf clusters break up the thin runners with patches of coverage.
for cx, cy, rows in [(42, 108, 4), (41, 118, 4), (45, 129, 5), (40, 140, 3), (48, 96, 3), (55, 118, 3), (38, 170, 3), (36, 185, 3), (85, 153, 3), (82, 164, 3)]:
    for row in range(rows):
        yy = cy + row * 2
        spread = 2 if row < rows - 1 else 1
        for column in range(-spread, spread + 1, 2):
            xx = cx + column + (row % 2)
            leaf(xx, yy, -1 if column < 0 else 1, row == rows - 1, rng.random() < 0.4)

result.blit(ivy, 0, 0)

# Light is composited in discrete pixel bands, keeping the source's hard edges.
glow = new_canvas(144, 256, name='Staff light')
glow.circle(64, 187, 10, '#91eacb0b')
glow.circle(64, 187, 7, '#8be8cb10')
glow.circle(64, 187, 5, '#91edce20')
glow.circle(64, 187, 3, '#b0f8db30')
result.blit(glow, 0, 0)

mage = new_canvas(144, 256, name='Mage entering')
ink = '#222a32'
cloth_dark = '#30374b'
cloth_shadow = '#41465c'
cloth = '#535a72'
cloth_light = '#6b7188'
cloth_rim = '#8a9b9b'
trim = '#a09c7c'

# Contact shadow and the uneven boots establish a step over the sill.
mage.ellipse(52, 219, 8, 2, '#1c3434')
mage.poly([(48, 213), (51, 214), (50, 220), (47, 220), (47, 218)], '#222831')
mage.line(47, 220, 50, 220, '#152a2c')
mage.set(48, 218, '#656c74')
mage.poly([(54, 211), (57, 212), (57, 216), (55, 217), (53, 216)], '#252b34')
mage.line(54, 216, 56, 216, '#74777c')

# Rear-facing robe: a broad back, tapering shoulder mantle and moving hem.
mage.poly([(49, 197), (54, 196), (58, 200), (58, 205), (60, 213), (58, 217), (54, 216), (52, 215), (49, 218), (44, 217), (45, 210), (46, 203)], ink)
mage.poly([(49, 199), (54, 198), (57, 202), (56, 208), (58, 215), (54, 214), (51, 215), (46, 216), (47, 209), (47, 203)], cloth)
mage.poly([(48, 202), (50, 202), (49, 209), (48, 215), (45, 217), (46, 210)], cloth_dark)
mage.poly([(53, 202), (55, 202), (55, 209), (57, 215), (54, 214), (52, 211)], cloth_shadow)
mage.line(51, 204, 50, 211, cloth_light)
mage.line(50, 211, 49, 215, cloth_light)
mage.line(53, 205, 53, 211, cloth_dark)
mage.set(52, 213, cloth_light)
mage.line(46, 216, 49, 216, '#858780')
mage.line(55, 215, 57, 216, '#777d7d')

# The far hand disappears under the cloak; the nearer sleeve reaches the staff.
mage.poly([(47, 200), (49, 202), (47, 208), (45, 210), (44, 208), (45, 203)], cloth_shadow)
mage.line(46, 203, 45, 207, cloth_light)
mage.set(45, 209, '#8b8574')
mage.poly([(55, 200), (58, 200), (59, 202), (62, 203), (62, 206), (59, 206), (56, 204)], ink)
mage.poly([(56, 201), (58, 202), (58, 203), (61, 203), (61, 205), (58, 204), (56, 203)], cloth)
mage.line(58, 202, 60, 203, cloth_rim)
mage.set(60, 204, trim)

# The closed back of the hood is fully visible, with no face opening.
mage.poly([(51, 188), (54, 190), (56, 194), (56, 197), (58, 200), (54, 203), (49, 202), (46, 200), (48, 196), (48, 192)], ink)
mage.poly([(51, 189), (54, 192), (55, 195), (54, 198), (51, 201), (48, 199), (49, 195), (49, 192)], cloth)
mage.poly([(51, 190), (51, 194), (50, 198), (51, 200), (48, 198), (49, 192)], cloth_shadow)
mage.line(52, 191, 54, 194, cloth_light)
mage.line(54, 194, 54, 196, cloth_rim)
mage.line(54, 197, 52, 199, cloth_light)
mage.poly([(48, 198), (51, 200), (54, 199), (56, 198), (57, 200), (53, 203), (49, 202), (47, 200)], cloth_shadow)
mage.line(48, 200, 51, 202, cloth_light)
mage.line(51, 202, 54, 201, cloth_light)
mage.set(55, 200, cloth_rim)
mage.set(52, 203, trim)
mage.set(52, 204, '#747866')

# A crooked wooden staff and a luminous crystal held ahead in his right hand.
mage.line(63, 193, 61, 219, '#273532')
mage.line(64, 192, 62, 218, '#655b46')
mage.line(64, 193, 63, 203, '#b1a678')
mage.line(63, 207, 62, 215, '#8b805a')
mage.set(62, 218, '#b1a678')
mage.line(63, 194, 61, 191, '#736f4e')
mage.line(61, 191, 62, 188, '#aaad7a')
mage.line(63, 194, 66, 190, '#a1b887')
mage.line(66, 190, 66, 187, '#bdd8a6')
mage.poly([(64, 183), (66, 186), (65, 190), (63, 191), (62, 187)], '#66c6b0')
mage.poly([(64, 184), (65, 187), (64, 190), (63, 187)], '#d9f8cb')
mage.line(64, 185, 64, 188, '#f5ffe3')
mage.set(63, 186, '#b6f5ca')
# Fingers wrap over the shaft rather than hovering beside it.
mage.rect(61, 203, 2, 2, '#aa9c7d')
mage.set(62, 203, '#d1c4a0')
mage.set(61, 205, '#776c5b')
mage.set(67, 183, '#9cd9bb')
mage.set(60, 185, '#8fc3b0')

result.blit(mage, 0, 0)
view(result, scale=3, margin=0)
view(result.select(30, 162, 43, 65).preview(), scale=7, margin=0)
finish(result)
