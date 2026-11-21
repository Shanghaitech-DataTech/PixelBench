import math

W = H = 20

SPANS = {
    5: [(6, 13)],
    6: [(4, 15)],
    7: [(2, 17)],
    8: [(1, 18)],
    9: [(1, 18)],
    10: [(2, 17)],
    11: [(2, 17)],
    12: [(3, 16)],
    13: [(3, 16)],
    14: [(4, 15)],
    15: [(5, 14)],
    16: [(5, 14)],
}

mask = [[False] * W for _ in range(H)]
for y, spans in SPANS.items():
    for x0, x1 in spans:
        for x in range(x0, x1 + 1):
            mask[y][x] = True


def inside(x, y):
    return 0 <= x < W and 0 <= y < H and mask[y][x]


def variant_4x4():
    """4x4 links, sx=4 sy=4 off 2, dark corners."""
    stamp = [
        [(0, 0, 5), (1, 0, 0), (2, 0, 1), (3, 0, 5)],
        [(0, 1, 1), (3, 1, 3)],
        [(0, 2, 2), (3, 2, 4)],
        [(0, 3, 6), (1, 3, 4), (2, 3, 5), (3, 3, 6)],
    ]
    holes = [(1, 1), (2, 1), (1, 2), (2, 2)]
    return paint(stamp, holes, 4, 4, 2)


def variant_5x5():
    """5x5 round links, sx=5 sy=4 off 2, 2x2 hole."""
    stamp = [
        [(1, 0, 0), (2, 0, 0), (3, 0, 2)],
        [(0, 1, 1), (3, 1, 3)],
        [(0, 2, 3), (3, 2, 4)],
        [(0, 3, 5), (3, 3, 6)],
        [(1, 4, 5), (2, 4, 6), (3, 4, 6)],
    ]
    holes = [(1, 1), (2, 1), (1, 2), (2, 2)]
    return paint(stamp, holes, 5, 4, 2)


def paint(stamp, holes, sx, sy, off):
    level = [[None] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if mask[y][x]:
                level[y][x] = 6
    row = 0
    cy = 1
    while cy < H + 2:
        o = off if row % 2 else 0
        cx = o - 5
        while cx < W + 2:
            for line in stamp:
                for i, j, lv in line:
                    x, y = cx + i, cy + j
                    if inside(x, y):
                        level[y][x] = lv
            for i, j in holes:
                x, y = cx + i, cy + j
                if inside(x, y):
                    level[y][x] = 7
            cx += sx
        cy += sy
        row += 1
    return level


def show(name, level):
    print("==", name)
    for y in range(H):
        line = ""
        for x in range(W):
            lv = level[y][x]
            if lv is None:
                line += "."
            else:
                line += str(lv) if lv < 5 else "ABCDEFG"[lv - 5] * 1
        print("  " + line)


show("4x4 links", variant_4x4())
show("5x5 links", variant_5x5())
