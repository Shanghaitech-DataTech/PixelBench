import math
from pixelbench_api import new_canvas, finish

W = H = 128
c = new_canvas(W, H, name="summer-seaside")

WHITE = "#FFFFFF"
RED = "#E63B3B"
CLSH = "#E9F5FF"

# ---------------- Sky ----------------
SKY = ["#5FB4F0", "#6BBFF3", "#79CBF6", "#8AD6F9", "#9CE0FB",
       "#AEE9FC", "#C1F0FD", "#D2F6FE", "#E0FAFF"]
for (y0, y1), col in zip(
    [(0, 5), (6, 12), (13, 19), (20, 26), (27, 33), (34, 40), (41, 46), (47, 50), (51, 53)],
    SKY,
):
    c.rect(0, y0, W, y1 - y0 + 1, col)

# ---------------- Sun ----------------
c.circle(101, 21, 13, "#FDF3AC")
c.circle(101, 21, 9, "#FFEA4D")

# ---------------- Clouds ----------------
c.ellipse(28, 14, 8, 4, WHITE); c.ellipse(22, 17, 6, 3, WHITE)
c.ellipse(35, 16, 7, 4, WHITE); c.ellipse(28, 18, 8, 2, CLSH)
c.ellipse(58, 9, 7, 3, WHITE); c.ellipse(50, 12, 6, 3, WHITE)
c.ellipse(66, 11, 6, 3, WHITE); c.ellipse(58, 12, 7, 2, CLSH)
c.ellipse(19, 26, 5, 2, WHITE); c.ellipse(13, 28, 4, 2, WHITE)
c.ellipse(25, 28, 4, 2, WHITE); c.ellipse(19, 29, 5, 2, CLSH)

# ---------------- Sea ----------------
SEA = ["#1259A6", "#1969B3", "#217AC0", "#2B8ECC", "#37A3D6",
       "#45B8DE", "#54CBE4", "#64DAE8", "#71E4EA"]
for (y0, y1), col in zip(
    [(54, 61), (62, 68), (69, 75), (76, 81), (82, 86), (87, 91), (92, 95), (96, 98), (99, 99)],
    SEA,
):
    c.rect(0, y0, W, y1 - y0 + 1, col)

# sun sparkle path on the water
for (x, y) in [(94, 66), (98, 70), (102, 64), (100, 74), (97, 78),
              (103, 72), (95, 82), (101, 86), (92, 70), (99, 90)]:
    c.set(x, y, "#FFF3A4")

# wave crest dashes
waves = [
    (73, [(10, 16), (28, 36), (50, 56), (74, 82), (98, 106), (116, 123)]),
    (80, [(4, 10), (20, 26), (42, 48), (64, 70), (88, 92), (110, 116)]),
    (87, [(14, 20), (32, 40), (56, 62), (80, 88), (102, 108)]),
    (93, [(6, 12), (24, 30), (46, 52), (68, 76), (94, 100)]),
    (97, [(2, 6), (18, 24), (36, 42), (58, 64), (84, 90), (110, 116)]),
]
for y, segs in waves:
    for x0, x1 in segs:
        c.rect(x0, y, x1 - x0 + 1, 1, WHITE)

# ---------------- Sailboat ----------------
c.line(30, 50, 30, 62, "#8A5A33")
c.poly([(29, 51), (29, 61), (37, 61)], WHITE)
c.rect(27, 61, 11, 1, WHITE)
c.rect(27, 62, 11, 1, RED)

# ---------------- Gulls ----------------
def gull(x, y):
    c.line(x - 3, y, x, y - 3, WHITE)
    c.line(x, y - 3, x + 3, y, WHITE)
    c.line(x, y - 1, x + 1, y + 1, WHITE)

gull(42, 30)
gull(80, 39)

# ---------------- Sand ----------------
SAND = ["#FBE9A6", "#F7DA8C", "#F2CC77", "#EDC268", "#E5B75E"]
for (y0, y1), col in zip(
    [(100, 103), (104, 109), (110, 116), (117, 122), (123, 127)],
    SAND,
):
    c.rect(0, y0, W, y1 - y0 + 1, col)

# ---------------- Shoreline foam ----------------
for x in range(128):
    m = x % 10
    if m < 3:
        c.set(x, 100, WHITE)
    elif m < 6:
        c.set(x, 101, WHITE)
    if x % 17 == 0:
        c.set(x, 102, WHITE)

# ---------------- Umbrella ----------------
c.ellipse(98, 123, 18, 4, "#E0B45A")            # sand shadow
c.line(96, 102, 96, 126, "#A5673A")             # pole
dome = [(x, round(112 - 10 * math.sqrt(max(0.0, 1 - ((x - 96) / 19) ** 2)))) for x in range(77, 116)]
c.poly(dome, RED)
for k in range(1, 8, 2):
    a = 77 + k * 38.0 / 8
    b = 77 + (k + 1) * 38.0 / 8
    pts = [(96, 102)] + [
        (x, round(112 - 10 * math.sqrt(max(0.0, 1 - ((x - 96) / 19) ** 2))))
        for x in range(math.ceil(a), math.floor(b) + 1)
    ]
    c.poly(pts, WHITE)
c.circle(96, 100, 1, RED)                        # finial

# ---------------- Striped towel ----------------
A = (24, 109); B = (58, 106); C = (64, 122); D = (30, 125)
c.ellipse(44, 124, 22, 3, "#E0B45A")
for i, col in enumerate(["#4D96FF", "#FFFFFF", "#FF6B9A", "#FFFFFF", "#FFD93D"]):
    t0 = i / 5.0; t1 = (i + 1) / 5.0
    c.poly([
        (A[0] + t0 * (D[0] - A[0]), A[1] + t0 * (D[1] - A[1])),
        (B[0] + t0 * (C[0] - B[0]), B[1] + t0 * (C[1] - B[1])),
        (B[0] + t1 * (C[0] - B[0]), B[1] + t1 * (C[1] - B[1])),
        (A[0] + t1 * (D[0] - A[0]), A[1] + t1 * (D[1] - A[1])),
    ], col)

# ---------------- Flip-flops ----------------
c.ellipse(67, 123, 5, 2, "#E0B45A")
c.ellipse(63, 119, 4, 2, WHITE)
c.line(61, 117, 63, 115, "#FFC53D")
c.line(65, 117, 63, 115, "#FFC53D")
c.ellipse(80, 125, 5, 2, "#E0B45A")
c.ellipse(76, 121, 4, 2, WHITE)
c.line(74, 119, 76, 117, "#FFC53D")
c.line(78, 119, 76, 117, "#FFC53D")

# ---------------- Tiny sand texture ----------------
for x, y in [(8, 109), (15, 118), (10, 123), (17, 113), (68, 107), (90, 110),
            (120, 109), (125, 116), (113, 122), (7, 113), (121, 125), (92, 107),
            (3, 115), (119, 112), (70, 114), (85, 119), (12, 121), (123, 110)]:
    c.set(x, y, "#E8BC63")

print(c.stats_text())
finish(c)
