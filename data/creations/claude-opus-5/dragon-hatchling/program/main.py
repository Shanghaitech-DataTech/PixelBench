import math

# ---------------- palette ----------------
OUT  = "#16281c"
S1   = "#3f8a45"   # mid scale
S2   = "#2c6433"   # dark scale
S3   = "#1d4525"   # deep shadow
S4   = "#63b055"   # highlight
BEL  = "#e9dca8"   # pale belly
BEL2 = "#c6b47c"   # belly shade
MEM  = "#8c5a44"   # wing membrane
MEM2 = "#6b3f31"   # membrane dark / bones
MEM3 = "#a8724f"   # membrane light
BONE = "#efe7cf"   # horns, teeth, claws
BON2 = "#b6a98a"
EYE  = "#ffc23a"
MTH  = "#6a2330"
TNG  = "#bf5560"

C = new_canvas(64, 64, name="dragon")


def bez(p0, p1, p2, n):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# ---------------- wings (behind body) ----------------
W = new_canvas(64, 64, name="wing")
wpts = [(26, 33), (19, 24), (12, 16), (9, 12),
        (3, 18), (7, 21), (5, 26), (9, 29), (8, 34), (13, 36), (13, 42), (19, 39), (25, 37)]
W.poly(wpts, MEM)
# finger bones radiating from the wrist
W.line(26, 33, 9, 12, MEM2)
W.line(25, 33, 10, 13, MEM2)
for tip in ((3, 18), (5, 26), (8, 34), (13, 42)):
    W.line(9, 12, tip[0], tip[1], MEM2)
# membrane light near the leading edge
W.line(13, 18, 20, 27, MEM3)
W.line(10, 24, 16, 31, MEM3)
# wrist claw
W.poly([(9, 12), (6, 8), (12, 11)], BONE)
W.outline(OUT)

C.blit(W, 0, 0)
W2 = W.copy(name="wing_r")
W2.mirror("h")
C.blit(W2, 0, 0)

# ---------------- tail (behind body) ----------------
tp = bez((33, 46), (52, 56), (58, 32), 30)
for i, (x, y) in enumerate(tp):
    r = 4.0 * (1 - i / len(tp))
    C.circle(int(round(x)), int(round(y)), max(0, int(round(r))), S2)

for idx, h in ((8, 4), (14, 4), (20, 3)):
    x, y = tp[idx]
    px, py = tp[idx - 1]
    nx2, ny2 = tp[idx + 1]
    dx, dy = nx2 - px, ny2 - py
    L = math.hypot(dx, dy) or 1
    nx, ny = dy / L, -dx / L
    if (x + nx - 32) ** 2 + (y + ny - 40) ** 2 < (x - nx - 32) ** 2 + (y - ny - 40) ** 2:
        nx, ny = -nx, -ny
    tx, ty = dx / L, dy / L
    C.poly([(int(round(x + tx * 2)), int(round(y + ty * 2))),
            (int(round(x - tx * 2)), int(round(y - ty * 2))),
            (int(round(x + nx * h)), int(round(y + ny * h)))], S3)
tx_, ty_ = tp[-1]
C.poly([(int(tx_) - 2, int(ty_) + 3), (int(tx_) + 3, int(ty_) - 4), (int(tx_) + 3, int(ty_) + 3)], S3)

# ---------------- hind legs ----------------
for sx in (-1, 1):
    cx = 32 + sx * 9
    C.ellipse(cx, 45, 5, 6, S2)
    C.rect(cx - 2 + (1 if sx < 0 else -2), 49, 4, 5, S2)
    C.poly([(cx - 4, 53), (cx + 4, 53), (cx + 4, 56), (cx - 4, 56)], S1)
    for k in (-3, 0, 3):
        C.poly([(cx + k, 55), (cx + k + 1, 55), (cx + k + (1 if k >= 0 else 0), 58)], BONE)

# ---------------- torso ----------------
C.ellipse(32, 40, 9, 11, S1)
C.ellipse(32, 35, 10, 6, S1)
C.ellipse(32, 42, 6, 8, BEL)
for y in range(37, 50, 3):
    C.line(27, y, 36, y, BEL2)

# ---------------- arms ----------------
for sx in (-1, 1):
    sh = 32 + sx * 8
    C.poly([(sh, 34), (sh + sx * 4, 37), (sh + sx * 4, 42), (sh + sx * 1, 41), (sh - sx * 1, 37)], S2)
    C.ellipse(sh + sx * 3, 43, 2, 2, S1)
    for k in (-1, 1, 3):
        C.poly([(sh + sx * (2 + k), 44), (sh + sx * (3 + k), 44), (sh + sx * (2 + k), 47)], BONE)

# scale speckle on the flanks
for y in range(32, 49, 3):
    for x in range(23, 42, 3):
        off = 0 if (y // 3) % 2 == 0 else 1
        if abs(x + off - 32) > 6:
            C.set(x + off, y, S2)

# ---------------- neck ----------------
C.poly([(28, 22), (36, 22), (38, 35), (26, 35)], S1)
C.poly([(30, 28), (34, 28), (35, 35), (29, 35)], BEL)
# shoulder spikes
C.poly([(26, 31), (22, 29), (26, 34)], S3)
C.poly([(38, 31), (42, 29), (38, 34)], S3)

# ---------------- head ----------------
C.ellipse(32, 14, 9, 6, S1)                              # skull
C.poly([(28, 16), (36, 16), (35, 21), (29, 21)], S1)     # muzzle
C.poly([(30, 17), (34, 17), (33, 20), (31, 20)], S4)     # muzzle top plane
C.set(30, 19, S3)                                        # nostrils
C.set(34, 19, S3)

# growling mouth: dark wedge under the lip line
C.poly([(27, 21), (37, 21), (35, 27), (29, 27)], MTH)
C.poly([(30, 24), (34, 24), (33, 26), (31, 26)], TNG)
# two prominent upper fangs plus two small inner ones
for x in (28, 36):
    C.line(x, 21, x, 24, BONE)
C.set(31, 21, BONE)
C.set(33, 21, BONE)
C.set(30, 22, BONE)
C.set(34, 22, BONE)

# lower jaw
C.poly([(28, 27), (36, 27), (35, 31), (29, 31)], S1)
C.poly([(30, 28), (34, 28), (33, 30), (31, 30)], BEL)
C.set(30, 26, BONE)                                      # lower fangs
C.set(34, 26, BONE)

# eyes, wide-set and hatchling-big
for sx in (-1, 1):
    ex = 32 + sx * 5
    C.rect(ex - 1, 12, 3, 3, EYE)
    C.set(ex, 12, OUT)
    C.set(ex, 13, OUT)
    C.line(ex - sx * 2, 10, ex + sx * 1, 9, S3)           # angry brow

# horns: short, thick, swept back-outward
for sx in (-1, 1):
    bx = 32 + sx * 6
    C.poly([(bx, 10), (bx + sx * 1, 7),
            (bx + sx * 5, 3), (bx + sx * 6, 5),
            (bx + sx * 4, 8), (bx + sx * 4, 11)], BONE)
    C.line(bx + sx * 2, 9, bx + sx * 5, 5, BON2)
    C.line(bx + sx * 3, 10, bx + sx * 4, 8, BON2)
# crown spikes
C.poly([(29, 8), (30, 5), (32, 8)], BON2)
C.poly([(35, 8), (34, 5), (32, 8)], BON2)

C.outline(OUT)

# eye glints, after the outline pass so they stay bright
C.set(26, 12, BONE)
C.set(38, 12, BONE)

print(C.stats_text())
view(C)
save("dragon", C)
finish(C)
