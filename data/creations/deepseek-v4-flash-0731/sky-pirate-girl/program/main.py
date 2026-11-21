import math
from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="sky_pirate_girl")

SKIN    = c.color((255, 224, 200), "skin")
SKIN_SH = c.color((236, 194, 164), "skin_sh")
BLUSH   = c.color((255, 164, 144), "blush")
HAIR    = c.color((122, 74, 34), "hair")
HAIR_SH = c.color((88, 50, 20), "hair_sh")
HAIR_HI = c.color((202, 142, 80), "hair_hi")
EYE     = c.color((38, 104, 158), "eye")
EYE_DRK = c.color((22, 42, 74), "eye_drk")
WHITE   = c.color((255, 255, 255), "white")
GOLD    = c.color((226, 178, 76), "gold")
GOLD_DRK= c.color((158, 118, 44), "gold_drk")
LENS    = c.color((122, 182, 218), "lens")
LENS_DRK= c.color((70, 124, 172), "lens_drk")
FRAME   = c.color((198, 156, 76), "frame")
FRAME_DRK= c.color((142, 106, 48), "frame_drk")
COAT    = c.color((36, 60, 112), "coat")
COAT_SH = c.color((20, 36, 74), "coat_sh")
COAT_HI = c.color((88, 124, 180), "coat_hi")
SHIRT   = c.color((242, 238, 230), "shirt")
SHIRT_SH= c.color((204, 198, 186), "shirt_sh")
SCARF   = c.color((206, 58, 58), "scarf")
SCARF_SH= c.color((142, 30, 34), "scarf_sh")
SCARF_HI= c.color((246, 110, 94), "scarf_hi")
MOUTH   = c.color((156, 60, 70), "mouth")

g = [[None] * W for _ in range(H)]

def paint(x, y, co):
    if 0 <= x < W and 0 <= y < H:
        g[y][x] = co

def rect(x0, y0, x1, y1, co):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            paint(x, y, co)

def ell(cx, cy, rx, ry, co):
    for y in range(cy - ry, cy + ry + 1):
        for x in range(cx - rx, cx + rx + 1):
            dx = (x - cx) / rx
            dy = (y - cy) / ry
            if dx * dx + dy * dy <= 1.0:
                paint(x, y, co)

def poly(pts, co):
    ys = [p[1] for p in pts]
    y0, y1 = min(ys), max(ys)
    n = len(pts)
    for y in range(y0, y1 + 1):
        xs = []
        for i in range(n):
            xa, ya = pts[i]
            xb, yb = pts[(i + 1) % n]
            if (ya <= y < yb) or (yb <= y < ya):
                xs.append(xa + (y - ya) * (xb - xa) / (yb - ya))
        xs.sort()
        for k in range(0, len(xs) - 1, 2):
            a = math.ceil(xs[k])
            b = math.floor(xs[k + 1])
            for x in range(a, b + 1):
                paint(x, y, co)

def line(x0, y0, x1, y1, co):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steps = max(dx, dy)
    for i in range(steps + 1):
        x = round(x0 + (x1 - x0) * i / steps)
        y = round(y0 + (y1 - y0) * i / steps)
        paint(x, y, co)

# ---------------- back hair ----------------
ell(30, 24, 16, 16, HAIR)          # big hair mass behind face
ell(30, 11, 13, 6, HAIR)           # top volume
ell(19, 27, 5, 7, HAIR)            # back left puff
poly([(44, 10), (58, 14), (61, 22), (57, 30), (46, 25), (45, 17)], HAIR)  # wind tail upper
poly([(45, 24), (55, 29), (57, 37), (51, 42), (44, 35)], HAIR)            # wind tail lower
line(46, 16, 56, 21, HAIR_HI)
line(48, 26, 54, 31, HAIR_HI)
# bridge between head mass and wind tail
poly([(41, 9), (51, 11), (50, 15), (43, 13)], HAIR)
# lock tip at tail end
paint(60, 24, HAIR); paint(62, 28, HAIR); paint(57, 42, HAIR); paint(60, 40, HAIR)
line(50, 18, 56, 20, HAIR_HI)

# ---------------- coat ----------------
ell(31, 47, 22, 8, COAT)           # shoulders
poly([(9, 46), (53, 46), (46, 63), (19, 63)], COAT)
poly([(24, 46), (40, 46), (42, 63), (22, 63)], SHIRT)
line(11, 44, 20, 47, COAT_HI)
line(42, 44, 50, 43, COAT_HI)

# ---------------- neck ----------------
rect(27, 37, 33, 43, SKIN)
rect(30, 37, 33, 43, SKIN_SH)

# ---------------- scarf ----------------
rect(17, 38, 43, 44, SCARF)
rect(17, 42, 43, 44, SCARF_SH)
poly([(32, 45), (46, 46), (54, 50), (50, 54), (37, 48), (33, 47)], SCARF)
poly([(33, 48), (47, 52), (53, 58), (47, 61), (37, 53), (33, 49)], SCARF_SH)
line(36, 46, 50, 49, SCARF_HI)
rect(26, 43, 35, 47, SCARF)        # knot
rect(30, 45, 35, 47, SCARF_SH)
line(37, 45, 45, 48, SCARF_HI)
# coat collar over scarf
poly([(10, 40), (18, 42), (17, 48), (10, 46)], COAT_SH)
poly([(42, 40), (50, 42), (50, 46), (42, 47)], COAT_SH)
line(18, 42, 17, 48, COAT_HI)
line(42, 42, 50, 43, COAT_HI)

# ---------------- face ----------------
face = {
    17: (25, 33), 18: (23, 35), 19: (22, 36), 20: (22, 36), 21: (21, 37),
    22: (21, 37), 23: (21, 37), 24: (21, 37), 25: (21, 37), 26: (22, 37),
    27: (22, 36), 28: (23, 36), 29: (23, 35), 30: (24, 35), 31: (25, 34),
    32: (26, 33), 33: (27, 32), 34: (28, 31), 35: (28, 30), 36: (29, 30),
    37: (30, 31), 38: (31, 32), 39: (32, 33),
}
for y, (a, b) in face.items():
    for x in range(a, b + 1):
        paint(x, y, SKIN)

# ---------------- features ----------------
for (x, y) in [(22, 22), (23, 21), (24, 21), (25, 22)]:
    paint(x, y, HAIR_SH)
for (x, y) in [(32, 22), (33, 21), (34, 21), (35, 22)]:
    paint(x, y, HAIR_SH)
rect(22, 24, 26, 26, EYE_DRK)
rect(23, 24, 25, 26, EYE)
rect(31, 24, 35, 26, EYE_DRK)
rect(32, 24, 34, 26, EYE)
paint(23, 24, WHITE); paint(25, 25, WHITE)
paint(32, 24, WHITE); paint(34, 25, WHITE)
paint(26, 28, SKIN_SH)
paint(36, 26, SKIN_SH); paint(36, 27, SKIN_SH); paint(36, 28, SKIN_SH); paint(36, 29, SKIN_SH)
paint(22, 27, BLUSH); paint(23, 28, BLUSH)
paint(34, 27, BLUSH); paint(35, 28, BLUSH)
for (x, y) in [(21, 31), (22, 31), (23, 31), (24, 31), (25, 31), (26, 30),
              (26, 31), (27, 31), (28, 31), (29, 31), (30, 31), (30, 32)]:
    paint(x, y, MOUTH)

# ---------------- bangs / locks ----------------
poly([(19, 15), (24, 14), (26, 20), (23, 22), (19, 20)], HAIR)
poly([(23, 14), (30, 13), (32, 19), (28, 21), (24, 20)], HAIR)
poly([(29, 13), (37, 16), (36, 21), (32, 20)], HAIR)
poly([(36, 17), (40, 23), (41, 30), (38, 35), (35, 31), (34, 25)], HAIR)
poly([(18, 17), (21, 20), (21, 28), (19, 34), (17, 31), (16, 24)], HAIR)
# wind-side lock covering the left brow and eye corner
poly([(20, 14), (24, 15), (24, 20), (21, 19)], HAIR)
line(25, 15, 27, 18, HAIR_HI)
line(30, 16, 32, 18, HAIR_HI)
line(38, 21, 37, 27, HAIR_HI)
line(22, 15, 24, 18, HAIR_HI)
line(20, 9, 28, 8, HAIR_HI)
line(47, 27, 53, 32, HAIR_HI)
paint(26, 7, HAIR); paint(25, 5, HAIR)

# ---------------- goggles ----------------
line(16, 15, 21, 14, FRAME_DRK)
line(36, 13, 42, 15, FRAME_DRK)
rect(21, 13, 27, 17, FRAME)
rect(31, 13, 36, 17, FRAME)
rect(22, 14, 26, 16, LENS)
rect(32, 14, 35, 16, LENS)
rect(22, 16, 26, 16, LENS_DRK)
rect(32, 16, 35, 16, LENS_DRK)
paint(23, 14, WHITE)
paint(24, 15, WHITE)
paint(33, 14, WHITE)
paint(34, 15, WHITE)

# ---------------- coat details ----------------
paint(30, 48, GOLD); paint(30, 52, GOLD); paint(30, 56, GOLD)
paint(31, 49, GOLD_DRK); paint(31, 53, GOLD_DRK); paint(31, 57, GOLD_DRK)
line(11, 46, 15, 51, COAT_HI)
line(46, 47, 50, 45, COAT_HI)
line(12, 55, 16, 61, COAT_SH)
line(42, 55, 45, 61, COAT_SH)

# ---------------- commit ----------------
for y in range(H):
    for x in range(W):
        if g[y][x] is not None:
            c.set(x, y, g[y][x])

print(c.stats_text())
print(c.matrix_text())
finish(c)
