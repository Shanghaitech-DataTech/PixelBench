from pixelbench_api import *

c = input_canvas
out = c.copy(name="output")
# Rebuild the same transformation (reuse logic by exec from main? simpler: re-run steps)
pal = {p['index']: tuple(p['rgba']) for p in c.palette()}
BLUE_TO_PURPLE = {
    (47, 117, 152, 255): (63, 28, 118, 255),
    (116, 184, 207, 255): (111, 63, 174, 255),
    (119, 183, 206, 255): (143, 99, 204, 255),
    (118, 183, 209, 255): (168, 132, 224, 255),
    (123, 181, 203, 255): (191, 163, 238, 255),
    (40, 39, 53, 255):    (46, 17, 82, 255),
}
for y in range(24, 62):
    for x in range(0, 64):
        rgba = pal.get(out.get(x, y))
        if rgba in BLUE_TO_PURPLE:
            out.set(x, y, BLUE_TO_PURPLE[rgba])
BUB = (216, 196, 247, 255)
BUB2 = (238, 227, 252, 255)
def bubble(bx, by, r):
    out.circle(bx, by, r, BUB, fill=False)
    out.set(bx - r, by - r, BUB2)
bubbles = [(31, 58, 2), (26, 55, 1), (35, 53, 2), (29, 50, 1),
           (23, 47, 1), (37, 46, 1), (31, 39, 1), (27, 36, 1),
           (33, 33, 1), (29, 30, 2), (25, 28, 1), (31, 26, 1)]
for (bx, by, r) in bubbles:
    bubble(bx, by, r)
for (dx, dy) in [(20, 54), (41, 50), (15, 49), (26, 44), (39, 41), (22, 38), (35, 28)]:
    out.set(dx, dy, BUB2)
def sparkle(sx, sy):
    out.set(sx, sy, BUB2)
    out.set(sx - 1, sy, BUB)
    out.set(sx + 1, sy, BUB)
    out.set(sx, sy - 1, BUB)
    out.set(sx, sy + 1, BUB)
for (sx, sy) in [(14, 23), (39, 21), (24, 18), (43, 15), (31, 21)]:
    sparkle(sx, sy)
for (vx, vy) in [(20, 25), (24, 24), (35, 24), (28, 23), (33, 25), (37, 25), (18, 25)]:
    out.set(vx, vy, (170, 140, 232, 255))
out.set(26, 26, (191, 163, 238, 255))
out.set(30, 26, (216, 196, 247, 255))

print(out.matrix_text(region=(4, 14, 59, 62)))
