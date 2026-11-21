from pixelbench_api import *

W = H = 48

# ---------------- palette ----------------
OUT    = '#0d0d13'
BODY   = '#2b2b3a'
BODY_D = '#191922'
BODY_L = '#4b4b62'
BODY_H = '#6d6d88'
GOLD   = '#d3a13f'
GOLD_L = '#f3d68f'
SILV   = '#a9afbd'
SILV_D = '#6c7180'
SILV_L = '#dfe4ee'
WHEEL_S = '#3f4450'
WOOD   = '#8a5a2c'
WOOD_D = '#5a3819'
WOOD_L = '#b98349'
RED    = '#bf3a2b'
RED_D  = '#87231a'
RED_L  = '#e0604a'
CREAM  = '#f0e5cb'

BODY_PATH = ("M 9,13 C 9,10 11,9 14,9 L 39,9 C 42,9 44,11 44,14 L 44,30 "
             "C 44,33 42,34 39,34 L 32,34 C 29,34 28,32 28,29 L 27,23 "
             "C 26,21 25,20 22,20 L 18,20 C 17,20 16,21 16,23 L 16,25 "
             "C 16,27 15,27 13,27 L 11,27 C 9,27 9,25 9,23 Z")


def amap(cv):
    w, h, d = cv.to_rgba()
    return [[d[(y * w + x) * 4 + 3] for x in range(w)] for y in range(h)]


def paint_rim(dest, a, dx, dy, color):
    """Pixels of mask `a` not covered by `a` shifted (dx,dy) -> rim band."""
    for y in range(H):
        for x in range(W):
            if a[y][x]:
                sx, sy = x - dx, y - dy
                if not (0 <= sx < W and 0 <= sy < H and a[sy][sx]):
                    dest.set(x, y, color)


c = new_canvas(W, H, name="sewing_machine")

# ---------------- wooden base ----------------
c.rect(2, 41, 45, 5, WOOD)
c.rect(3, 41, 43, 1, WOOD_L)
c.rect(3, 45, 43, 1, WOOD_D)
for x in (6, 13, 21, 30, 39):
    c.set(x, 43, WOOD_D)
    c.set(x + 1, 43, WOOD_D)
c.rect(2, 41, 45, 5, OUT, fill=False)

# ---------------- bed (top face + front face) ----------------
c.poly([(6, 33), (43, 33), (45, 37), (4, 37)], BODY)
c.poly([(4, 37), (45, 37), (45, 41), (4, 41)], BODY_D)
c.line(6, 33, 43, 33, BODY_L)
c.line(4, 37, 45, 37, BODY_L)
c.line(6, 39, 43, 39, GOLD)
c.line(5, 40, 44, 40, OUT)
c.poly([(6, 33), (43, 33), (45, 37), (45, 41), (4, 41), (4, 37)], OUT, fill=False)

# ---------------- red fabric lying on the bed ----------------
c.poly([(5, 33), (27, 32), (31, 36), (29, 37), (5, 37)], RED)
c.poly([(5, 33), (27, 32), (27, 33), (5, 34)], RED_L)
c.line(9, 35, 26, 34, RED_D)
c.line(13, 36, 28, 35, RED_D)
for x in (16, 18, 20, 22, 24):
    c.set(x, 33, CREAM)

# ---------------- machine body ----------------
bs = new_canvas(W, H, name="bodyshape")
bs.path(BODY_PATH, BODY)
ba = amap(bs)
paint_rim(bs, ba, -2, -2, BODY_D)
paint_rim(bs, ba, 2, 2, BODY_L)
paint_rim(bs, ba, 1, 1, BODY_H)
bs.path(BODY_PATH, OUT, fill=False)
c.blit(bs, 0, 0)

# body panel shading: darker under the arm
c.line(18, 21, 26, 21, BODY_D)
c.line(28, 24, 28, 30, BODY_D)

# ---------------- gold decals ----------------
c.path("M 19,13 C 23,10 26,16 30,13 C 33,11 36,15 39,13", GOLD, fill=False)
c.path("M 21,17 C 24,15 27,19 30,17", GOLD_L, fill=False)
c.set(33, 30, GOLD)
c.set(35, 31, GOLD)
c.set(37, 30, GOLD)
c.line(11, 25, 14, 25, GOLD)

# ---------------- face plate + tension dial ----------------
c.rect(13, 12, 3, 11, SILV_D)
c.rect(13, 12, 1, 11, SILV)
c.rect(15, 12, 1, 11, OUT)
c.rect(10, 16, 3, 3, SILV)
c.set(10, 16, SILV_L)
c.set(11, 17, SILV_D)
c.set(12, 18, SILV_D)
c.rect(10, 21, 3, 1, SILV_L)
c.rect(10, 23, 2, 1, SILV)

# ---------------- hand wheel ----------------
c.circle(36, 22, 7, OUT, fill=True)
c.circle(36, 22, 6, SILV_D)
c.circle(36, 22, 5, BODY_D)
for (ex, ey) in [(36, 18), (36, 26), (32, 22), (40, 22)]:
    c.line(36, 22, ex, ey, WHEEL_S)
c.circle(36, 22, 2, SILV)
c.set(35, 21, SILV_L)
c.set(37, 23, SILV_D)
c.set(36, 24, SILV_D)
c.path("M 31,19 A 7,7 0 0 1 36,15", SILV_L, fill=False)
c.set(41, 18, SILV)
c.set(42, 18, SILV_D)

# ---------------- spool pin + thread spool ----------------
c.rect(33, 2, 1, 8, SILV_D)
c.set(33, 2, SILV_L)
c.rect(31, 4, 5, 5, RED)
c.rect(31, 4, 5, 1, WOOD_L)
c.rect(31, 8, 5, 1, WOOD_L)
c.rect(31, 5, 1, 3, RED_L)
c.rect(35, 5, 1, 3, RED_D)

# ---------------- thread ----------------
c.path("M 31,5 C 24,2 16,2 12,7 C 10,9 10,11 11,13", CREAM, fill=False)
c.path("M 11,19 L 11,22 L 12,24", CREAM, fill=False)

# ---------------- needle bar, needle, presser foot ----------------
c.rect(11, 25, 3, 5, SILV)
c.rect(11, 25, 1, 5, SILV)
c.rect(13, 25, 1, 5, SILV_D)
c.rect(10, 29, 5, 2, SILV_D)
c.set(12, 30, SILV_L)
c.rect(15, 26, 2, 6, SILV_D)
c.rect(15, 26, 1, 6, SILV)
c.poly([(10, 32), (19, 32), (19, 34), (10, 34)], SILV)
c.line(10, 32, 19, 32, SILV_L)
c.line(10, 34, 19, 34, SILV_D)
c.set(12, 30, SILV)
c.set(12, 31, SILV)
c.set(12, 32, SILV_D)
c.set(12, 33, SILV_D)
c.set(12, 34, SILV_D)
c.set(12, 35, SILV)
c.set(12, 36, SILV_D)

# ---------------- fabric drape over the front-left edge ----------------
DRAPE = "M 5,35 L 12,36 C 12,39 11,41 10,43 L 5,42 C 4,40 4,37 5,35 Z"
c.path(DRAPE, RED)
c.path("M 5,35 L 12,36 C 12,37 12,38 12,39 L 5,38 C 4,37 4,36 5,35 Z", RED_L)
c.line(7, 39, 7, 42, RED_D)
c.line(10, 39, 10, 42, RED_D)
c.path(DRAPE, RED_D, fill=False)

view(c)
head = c.select(4, 6, 26, 34).preview()
view(head, scale=12)
save("sewing_machine", c)
finish(c)
