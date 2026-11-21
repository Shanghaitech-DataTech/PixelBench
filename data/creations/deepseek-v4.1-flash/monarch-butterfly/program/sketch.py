from collections import deque

ORANGE   = "#EF7C13"
ORANGE_L = "#FFA53C"
ORANGE_D = "#C2560B"
BLACK    = "#1E1712"
WHITE    = "#F7F3EA"

W, H = 32, 32

FORE = {
    1: (5, 7), 2: (4, 9), 3: (3, 11), 4: (2, 12), 5: (2, 13), 6: (2, 14),
    7: (2, 14), 8: (3, 14), 9: (4, 14), 10: (5, 14), 11: (7, 14),
    12: (9, 14), 13: (11, 14), 14: (13, 14),
}
HIND = {
    15: (11, 14), 16: (9, 14), 17: (7, 14), 18: (5, 14), 19: (4, 14),
    20: (3, 14), 21: (2, 14), 22: (2, 14), 23: (3, 14), 24: (3, 14),
    25: (4, 14), 26: (6, 14), 27: (8, 14), 28: (10, 14),
}
print("    " + "".join(str(x % 10) for x in range(16)))
for y in range(1, 29):
    row = ""
    for x in range(16):
        f = any(x in range(a, b + 1) for yy, (a, b) in FORE.items() if yy == y)
        h = any(x in range(a, b + 1) for yy, (a, b) in HIND.items() if yy == y)
        row += ("#" if f and not h else "F" if f else "H" if h else ".")
    print("%2d  %s" % (y, row))
