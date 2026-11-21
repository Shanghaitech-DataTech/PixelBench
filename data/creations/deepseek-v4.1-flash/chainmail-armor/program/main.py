import math

W = H = 32
c = new_canvas(W, H, background=None, name="chainmail")

# 0 = specular highlight ... 7 = deepest shadow (ring holes)
LEVELS = [
    "#eef6fb",
    "#d3e2ee",
    "#b6c9da",
    "#98adc2",
    "#7b8fa4",
    "#5f7285",
    "#455263",
    "#2a3140",
]
OUTLINE = "#101620"

# ---------------- silhouette: broad shoulders, short sleeves, hem ----------------
SPANS = {
    5: [(11, 20)],
    6: [(8, 23)],
    7: [(5, 26)],
    8: [(3, 28)],
    9: [(2, 29)],
    10: [(2, 29)],
    11: [(2, 29)],
    12: [(2, 29)],
    13: [(3, 28)],
    14: [(3, 28)],
    15: [(4, 27)],
    16: [(4, 27)],
    17: [(5, 26)],
    18: [(9, 22)],
    19: [(9, 22)],
    20: [(9, 22)],
    21: [(9, 22)],
    22: [(9, 22)],
    23: [(9, 22)],
    24: [(9, 22)],
    25: [(9, 22)],
    26: [(8, 23)],
    27: [(8, 23)],
}

mask = [[False] * W for _ in range(H)]
for y, spans in SPANS.items():
    for x0, x1 in spans:
        for x in range(x0, x1 + 1):
            mask[y][x] = True

# shallow collar dip at the top centre
mask[5][15] = False
mask[5][16] = False


def inside(x, y):
    return 0 <= x < W and 0 <= y < H and mask[y][x]


# ---------------- 4x4 link stamp, lit from the upper left ----------------
#  4 0 0 4      dark corners, bright top arc
#  1 7 7 2      bright left wall, 2x2 hole, mid right wall
#  2 7 7 4
#  5 4 5 6      shaded underside
STAMP = [
    [(0, 0, 4), (1, 0, 0), (2, 0, 0), (3, 0, 4)],
    [(0, 1, 1), (3, 1, 2)],
    [(0, 2, 2), (3, 2, 4)],
    [(0, 3, 5), (1, 3, 4), (2, 3, 5), (3, 3, 6)],
]
HOLE = [(1, 1), (2, 1), (1, 2), (2, 2)]

SX, SY, OFF = 4, 4, 2

level = [[None] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if mask[y][x]:
            level[y][x] = 6

row = 0
cy = 1
while cy < H + 2:
    off = OFF if row % 2 else 0
    cx = off - 5
    while cx < W + 2:
        for line in STAMP:
            for i, j, lv in line:
                x, y = cx + i, cy + j
                if inside(x, y):
                    level[y][x] = lv
        for i, j in HOLE:
            x, y = cx + i, cy + j
            if inside(x, y):
                level[y][x] = 7
        cx += SX
    cy += SY
    row += 1

# ---------------- lighting, rim light, dark outline ----------------
pixels = {}
for y in range(H):
    for x in range(W):
        lv = level[y][x]
        if lv is None:
            continue
        rim = 9
        for dy in (-2, -1, 0, 1, 2):
            for dx in (-2, -1, 0, 1, 2):
                if not inside(x + dx, y + dy):
                    d = max(abs(dx), abs(dy))
                    if d < rim:
                        rim = d
        if rim == 1:
            pixels[(x, y)] = OUTLINE
            continue

        shift = 0
        # gentle global falloff, light from the upper left
        if y <= 9:
            shift -= 1
        if y >= 23:
            shift += 1
        if x >= 25:
            shift += 1
        if x <= 5:
            shift -= 1
        # directional inner rim: lit on top, shaded underneath
        if rim == 2:
            if not inside(x, y - 2):
                shift -= 2
            elif not inside(x, y + 2):
                shift += 3
            elif not inside(x - 2, y):
                shift -= 1
            elif not inside(x + 2, y):
                shift += 2

        idx = min(7, max(0, lv + shift))
        pixels[(x, y)] = LEVELS[idx]

for (x, y), col in pixels.items():
    c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text())
print("brightness map: # light, + mid, - dark metal, , hole, O outline")
for y in range(H):
    line = ""
    for x in range(W):
        col = pixels.get((x, y))
        if col is None:
            line += " "
        elif col == OUTLINE:
            line += "O"
        else:
            i = LEVELS.index(col)
            line += "#" if i <= 2 else ("+" if i <= 5 else ("-" if i == 6 else ","))
    print("  " + line)

saved = save("chainmail", c)
print("saved:", saved)
finish(c)
