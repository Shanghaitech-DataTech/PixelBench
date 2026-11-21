try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 32

# ---------------- palette ----------------
OUT     = "#1b2b1f"
BODY_D  = "#22554a"
BODY_M  = "#3b8f6a"
BODY_L  = "#5fb884"
BODY_H  = "#9fdca6"
MOSS_D  = "#35651f"
MOSS_M  = "#548d26"
MOSS_L  = "#7cb237"
MOSS_H  = "#a8d64c"
ANT_D   = "#43301a"
ANT_M   = "#7a5831"
ANT_L   = "#a8834c"
MR_D    = "#8f1f26"
MR_M    = "#d63a3a"
MR_L    = "#ef6f63"
MUS_W   = "#fff4e2"
STEM    = "#dccfa8"
STEM_D  = "#ab9668"
SOCKET  = "#14322a"
GLOW    = "#7bf7d0"
EYE_W   = "#effff9"
BLUSH   = "#e08a7a"

SYM = {
    OUT: "#", BODY_D: "d", BODY_M: "m", BODY_L: "l", BODY_H: "H",
    MOSS_D: "M", MOSS_M: "w", MOSS_L: "W", MOSS_H: "X",
    ANT_D: "a", ANT_M: "A", ANT_L: "T",
    MR_D: "r", MR_M: "R", MR_L: "Q", MUS_W: "o", STEM: "s", STEM_D: "S",
    SOCKET: "k", GLOW: "g", EYE_W: "e", BLUSH: "b",
}


def dump(canvas, x0=0, y0=0, x1=31, y1=31):
    w, h, data = canvas.to_rgba()
    print("   " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            i = (y * w + x) * 4
            if data[i + 3] == 0:
                row += "."
            else:
                key = "#%02x%02x%02x" % (data[i], data[i + 1], data[i + 2])
                row += SYM.get(key, "?")
        print("%2d %s" % (y, row))


def grow_outline(layer, colour=OUT):
    w, h, data = layer.to_rgba()
    om = [[data[(y * w + x) * 4 + 3] > 0 for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            if om[y][x]:
                continue
            for (nx, ny) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < w and 0 <= ny < h and om[ny][nx]:
                    layer.set(x, y, colour)
                    break


BAYER = ((0.0, 0.5), (0.75, 0.25))


def dither(lo, hi, frac, x, y):
    return hi if frac > BAYER[y % 2][x % 2] else lo


# ---------------- body silhouette ----------------
spans = [
    (8, 15, 16), (9, 13, 18), (10, 12, 19), (11, 11, 20), (12, 10, 21),
    (13, 9, 22), (14, 8, 23), (15, 7, 24), (16, 6, 25), (17, 5, 26),
    (18, 5, 26), (19, 4, 27), (20, 4, 27), (21, 4, 27), (22, 3, 28),
    (23, 3, 28), (24, 3, 28), (25, 3, 28), (26, 3, 28), (27, 3, 28),
    (28, 4, 27), (29, 6, 25),
]
bodypx = set()
for (y, x0, x1) in spans:
    for x in range(x0, x1 + 1):
        bodypx.add((x, y))


def edge_set(px, r):
    out = set()
    for (x, y) in px:
        hit = False
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                if (x + dx, y + dy) not in px:
                    hit = True
                    break
            if hit:
                break
        if hit:
            out.add((x, y))
    return out


edge1 = edge_set(bodypx, 1)
edge2 = edge_set(bodypx, 2)

# ---------------- moss cap: smooth wavy fringe ----------------
fringe = {
    6: 11, 7: 12, 8: 12, 9: 13, 10: 13, 11: 14, 12: 14, 13: 13,
    14: 13, 15: 12, 16: 12, 17: 12, 18: 13, 19: 13, 20: 14, 21: 14,
    22: 13, 23: 13, 24: 12, 25: 12,
}
moss = set()
for (x, y) in bodypx:
    if x in fringe and y <= fringe[x]:
        moss.add((x, y))


def tone(x, y):
    return (x - 16) * 0.45 + (y - 18) * 0.45 + max(0, y - 25) * 2.2


col = {}
for (x, y) in bodypx:
    if (x, y) in moss:
        continue
    t = tone(x, y)
    if t < -3.2:
        col[(x, y)] = BODY_L
    elif t < 0.2:
        col[(x, y)] = dither(BODY_L, BODY_M, (t + 3.2) / 3.4, x, y)
    elif t < 4.0:
        col[(x, y)] = BODY_M
    elif t < 8.6:
        col[(x, y)] = dither(BODY_M, BODY_D, (t - 4.0) / 4.6, x, y)
    else:
        col[(x, y)] = BODY_D

for (x, y) in moss:
    m = (x - 11) * 1.0 + (y - 9) * 1.4
    if m < 3.0:
        c2 = MOSS_H
    elif m < 6.0:
        c2 = dither(MOSS_H, MOSS_L, (m - 3.0) / 3.0, x, y)
    elif m < 10.0:
        c2 = dither(MOSS_L, MOSS_M, (m - 6.0) / 4.0, x, y)
    else:
        c2 = MOSS_M
    if (x * 7 + y * 5) % 13 == 0 and c2 in (MOSS_L, MOSS_M):
        c2 = MOSS_D
    if y == fringe[x]:
        c2 = MOSS_D
    col[(x, y)] = c2

# rim light, upper-left silhouette
for (x, y) in bodypx:
    inm = (x, y) in moss
    if (x, y) in edge1 and x <= 12 and y <= 24:
        col[(x, y)] = MOSS_H if inm else BODY_H
    elif (x, y) in edge2 and x <= 13 and y <= 24:
        if inm:
            col[(x, y)] = MOSS_L
        elif col[(x, y)] == BODY_M:
            col[(x, y)] = BODY_L

body = new_canvas(W, H, name="body")
for (p, c2) in col.items():
    body.set(p[0], p[1], c2)
grow_outline(body)

# ---------------- tiny antlers ----------------
ant = new_canvas(W, H, name="ant")
left_ant = [
    (11, 11), (12, 11), (11, 10), (12, 10), (11, 9), (12, 9),
    (10, 8), (11, 8), (12, 8), (13, 8),
    (10, 7), (13, 7),
    (9, 6), (13, 6),
]
right_ant = [(31 - x, y) for (x, y) in left_ant]
for p in left_ant + right_ant:
    ant.set(p[0], p[1], ANT_D)
for p in [(11, 11), (11, 10), (11, 9), (10, 8), (10, 7), (9, 6),
          (20, 11), (20, 10), (20, 9), (21, 8), (21, 7), (22, 6)]:
    ant.set(p[0], p[1], ANT_M)
for p in [(9, 6), (13, 6), (18, 6), (22, 6)]:
    ant.set(p[0], p[1], ANT_L)

# ---------------- mushroom on the back ----------------
mush = new_canvas(W, H, name="mush")
mush.rect(24, 12, 3, 7, STEM)
mush.line(26, 12, 26, 18, STEM_D)
cap = {
    8:  [(25, MR_M), (26, MR_M)],
    9:  [(24, MR_L), (25, MR_M), (26, MR_M), (27, MR_M)],
    10: [(23, MR_L), (24, MR_M), (25, MR_M), (26, MR_M), (27, MR_M), (28, MR_D)],
    11: [(22, MR_M), (23, MR_M), (24, MR_M), (25, MR_M), (26, MR_M), (27, MR_D), (28, MR_D), (29, MR_D)],
    12: [(22, MR_M), (23, MR_M), (24, MR_M), (25, MR_M), (26, MR_D), (27, MR_D), (28, MR_D), (29, MR_D)],
    13: [(22, MR_D), (23, MR_D), (24, MR_D), (25, MR_D), (26, MR_D), (27, MR_D), (28, MR_D), (29, MR_D)],
}
for (y, cells) in cap.items():
    for (x, c2) in cells:
        mush.set(x, y, c2)
for p in [(24, 9), (27, 10)]:
    mush.set(p[0], p[1], MUS_W)
grow_outline(mush)

# ---------------- face ----------------
face = new_canvas(W, H, name="face")
for ex in (11, 20):
    # rounded-square socket 5x5
    face.rect(ex - 1, 18 - 2, 3, 1, SOCKET)
    face.rect(ex - 2, 18 - 1, 5, 3, SOCKET)
    face.rect(ex - 1, 18 + 2, 3, 1, SOCKET)
    face.rect(ex - 1, 18 - 1, 3, 3, GLOW)
    face.set(ex, 18, EYE_W)
for (bx, by) in [(8, 21), (9, 21), (22, 21), (23, 21)]:
    face.set(bx, by, BLUSH)
for p in [(13, 22), (18, 22), (14, 23), (17, 23), (15, 24), (16, 24)]:
    face.set(p[0], p[1], SOCKET)

# ---------------- compose ----------------
result = flatten([mush, body, ant, face], name="result")

print(result.stats_text())

save("forest_slime", result)
finish(result)
