W = H = 32

CHARS = {
    ".": None,
    "K": "#141521",   # outline / eye
    "T": "#1e2029",   # tyre
    "q": "#3d4257",   # tyre highlight
    "R": "#8f95b3",   # rim
    "H": "#2b3050",   # hub
    "N": "#2f3450",   # dark metal
    "L": "#3c4263",   # lit metal (deck top / bar)
    "D": "#232840",   # deck underside
    "O": "#ff7a45",   # accent orange
    "o": "#ffb27a",   # accent light
    "c": "#b8491b",   # accent dark
    "S": "#f7c49b",   # skin
    "s": "#d2946b",   # skin shade
    "G": "#1fb8a8",   # helmet
    "g": "#63e8d6",   # helmet highlight
    "m": "#0f7d72",   # helmet dark
    "J": "#e04a34",   # jacket
    "j": "#f5785c",   # jacket highlight
    "k": "#a52c1c",   # jacket dark
    "P": "#4a6ba0",   # pants
    "1": "#5f80b5",   # pants highlight
    "2": "#365080",   # pants shade
    "p": "#33507c",   # far leg
    "W": "#f2f5fb",   # shoe
    "w": "#adb3c9",   # shoe shade
    "u": "#868ca3",   # shoe sole
}

grid = [["."] * W for _ in range(H)]


def P(y, x, s):
    for i, ch in enumerate(s):
        if ch != ".":
            grid[y][x + i] = ch


# ============================================================ scooter
WHEEL = [
    "..qTT..",
    ".TRRRT.",
    "TRTTTRT",
    "TRTHTRT",
    "TRTTTRT",
    ".TRRRT.",
    "..TTT..",
]


def stamp(cx, cy):
    for j, row in enumerate(WHEEL):
        for i, ch in enumerate(row):
            if ch != ".":
                grid[cy - 3 + j][cx - 3 + i] = ch


stamp(7, 26)
stamp(26, 26)

# deck
P(22, 5, "LLLLLLLLLLLLLLLLLLLL")
P(23, 5, "DDDDDDDDDDDDDDDDDDDD")
P(22, 5, "OO")             # tail light
P(23, 5, "O.")

# stem
for y in range(15, 24):
    P(y, 24, "oOc")

# handlebar  (y 13..14)
P(14, 19, "LLLLLLLLLL")
P(13, 19, "Ooo")
P(13, 27, "Ooo")
P(14, 19, "Ooo")
P(14, 27, "Ooo")

# ============================================================ rider
# helmet shell
P(3, 13, "GGGG")
P(4, 12, "GggGGG")
P(5, 11, "GggGGGGG")
P(6, 11, "GGGGGGmm")
P(6, 19, "m")              # brim tip
# face
P(7, 11, "GGGSSSSS")
P(8, 11, "GGSSSSKSS")
P(9, 12, "SSSSSsS")

# torso
P(10, 11, "JJkSSkJ")
P(11, 10, "jjJJJJJk")
P(12, 10, "jJJJJJk")
P(13, 9, "jjJJJJJk")
P(14, 8, "jJJJJJJk")

# arm reaching the bar
P(11, 16, "JJJ")
P(12, 18, "JJJ")
P(13, 18, "JJ")
# hand on the grip
P(12, 20, "SS")
P(13, 20, "Ss")

# legs
for y in (15, 16, 17):
    P(y, 8, "ppp")
    P(y, 12, "1P2")
for y in (18, 19):
    P(y, 8, "ppp")
    P(y, 13, "1P2")
# shoes
P(20, 6, "wwwwww")
P(21, 6, "uuuuuu")
P(20, 13, "WWWWWW")
P(21, 13, "wwwwww")

# ============================================================ render
body = new_canvas(W, H, name="body")
for y in range(H):
    for x in range(W):
        ch = grid[y][x]
        if ch != ".":
            body.set(x, y, CHARS[ch])

pal = {p["index"]: p["rgba"] for p in body.palette()}


def op(x, y):
    if not (0 <= x < W and 0 <= y < H):
        return False
    i = body.get(x, y)
    return i is not None and pal[i][3] > 0


# 1px halo outline drawn *outside* the silhouette (keeps interior detail)
result = new_canvas(W, H, background=None, name="e-scooter-rider")
for y in range(H):
    for x in range(W):
        if not op(x, y):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if op(x + dx, y + dy):
                    result.set(x, y, CHARS["K"])
                    break
result.blit(body, 0, 0)

print(result.stats_text())
print(result.matrix_text())
print("colours:", len(result.palette()))

save("e-scooter-rider", result)
finish(result)
