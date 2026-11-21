from pixelbench_api import *

SRC = input_canvas
W, H = 66, 119

HAIR = (1, 2, 3, 4, 5, 6)
SKIN = (7, 8, 15)
RED = (10,)

def hairtex(x, y):
    t = (x * 2 + y * 3) % 9
    if t == 0:
        return 2
    if t == 4:
        return 4
    if t == 7:
        return 5
    return 3

def three_quarter(side):
    f = SRC.copy(name="f_" + side)
    y0, y1 = 23, 42
    xa, xb = 9, 49
    for y in range(y0, y1 + 1):
        row = [SRC.get(x, y) for x in range(xa, xb + 1)]
        for x in range(xa, xb + 1):
            if side == "right":
                s = xb - int(round((xb - x) * 1.25))
            else:
                s = xa + int(round((x - xa) * 1.25))
            if xa <= s <= xb and row[s - xa] != 0:
                f.set(x, y, row[s - xa])
            else:
                f.set(x, y, hairtex(x, y))
    return f

def rear():
    f = SRC.copy(name="f_back")
    f.mirror("h")
    for y in range(23, 58):
        for x in range(0, W):
            i = f.get(x, y)
            if i in SKIN or i in RED:
                f.set(x, y, hairtex(x, y) if y <= 52 else 17)
            elif i in (11, 12, 13, 14) and y <= 47:
                f.set(x, y, hairtex(x, y))
    for x0 in (18, 30, 42):
        for y in range(25, 51):
            dx = 1 if (y // 6) % 2 else 0
            f.set(x0 + dx, y, 2)
    for x0 in (24, 36):
        for y in range(24, 49):
            dx = 1 if ((y + 3) // 6) % 2 else 0
            f.set(x0 + dx, y, 4)
    return f

f1 = three_quarter("right")
f2 = three_quarter("left")
f3 = rear()

print(view(f1, scale=4, margin=0))
print(view(f2, scale=4, margin=0))
print(view(f3, scale=4, margin=0))

finish([f1, f2, f3])
