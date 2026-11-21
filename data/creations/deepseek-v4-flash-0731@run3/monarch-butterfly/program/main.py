import math
from pixelbench_api import new_canvas, finish

W = H = 32
c = new_canvas(W, H, name="monarch")

ORANGE = (238, 125, 26)
ORANGE2 = (250, 168, 64)
BLACK = (18, 11, 7)
WHITE = (247, 241, 231)


def fore(x, y):
    return ((x - 8.3) / 7.6) ** 2 + ((y - 11.2) / 8.0) ** 2 <= 1.0


def hind(x, y):
    return ((x - 9.6) / 5.9) ** 2 + ((y - 21.8) / 6.6) ** 2 <= 1.0


def wing(x, y):
    return fore(x, y) or hind(x, y)


def near_outside(x, y, r):
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if dx == 0 and dy == 0:
                continue
            if not wing(x + dx, y + dy):
                return True
    return False


def circ(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


FORE_RAYS = [168, 186, 204, 222, 240]
HIND_RAYS = [110, 126, 142]


def vein(x, y):
    if fore(x, y):
        a = math.degrees(math.atan2(y - 11.5, x - 15.0)) % 360
        return min(circ(a, rr) for rr in FORE_RAYS) <= 3.2
    if hind(x, y):
        a = math.degrees(math.atan2(y - 22.0, x - 15.0)) % 360
        return min(circ(a, rr) for rr in HIND_RAYS) <= 3.2
    return False


SPOTS = [(2.5, 7), (2, 10), (3.3, 13), (5.2, 16.2), (8.2, 17.8), (11, 5.2), (13, 7.5),
         (4.8, 19.5), (4.4, 22.5), (5.6, 25.2), (7.2, 26.6), (9.6, 27.4), (12.2, 26.6), (13.6, 24.2),
         (14.3, 11.5), (14.3, 15.5), (14.3, 19.5), (14.3, 22.4)]


def is_spot(x, y):
    for (sx, sy) in SPOTS:
        if (x - sx) ** 2 + (y - sy) ** 2 <= 1.6:
            return True
    return False


def seg_dist(x, y, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    t = ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(x - (x1 + t * dx), y - (y1 + t * dy))


for y in range(H):
    for x in range(16):
        col = None
        if (x - 10.5) ** 2 + (y - 1.5) ** 2 <= 2.2 or (x - 11.7) ** 2 + (y - 2.7) ** 2 <= 1.3:
            col = BLACK
        elif seg_dist(x, y, 13.4, 4.0, 10.9, 2.0) <= 0.7:
            col = BLACK
        elif is_spot(x, y) and wing(x, y):
            col = WHITE
        elif 15 <= x <= 16 and 24 <= y <= 27:
            col = BLACK
        elif 14 <= x <= 15 and 2 <= y <= 24:
            col = BLACK
        elif wing(x, y):
            if vein(x, y) or near_outside(x, y, 1):
                col = BLACK
            elif near_outside(x, y, 2):
                col = ORANGE
            else:
                col = ORANGE2
        if col is not None:
            c.set(x, y, col)
            if x != 31 - x:
                c.set(31 - x, y, col)

print(c.stats_text())
print(c.matrix_text())
finish(c)
