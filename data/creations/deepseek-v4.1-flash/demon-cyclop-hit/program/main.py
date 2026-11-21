src = input_canvas
SW, SH = src.stats()["size"]

W, H = 48, 40
OX, OY = 2, 6

A, YEL, GRN, DGR, SKN, LGT = 1, 2, 3, 4, 5, 6


def lean_dx(y):
    if y >= 30:
        return 0
    return int(0.30 * (30 - y) + 0.5)


def off(y, shift):
    return OX + lean_dx(y) + shift


def build(shift, dy, name):
    c = new_canvas(W, H, name=name)
    for y in range(SH):
        ox = off(y, shift)
        for x in range(SW):
            idx = src.get(x, y)
            if idx:
                c.set(ox + x, OY + y + dy, idx)
    return c


# ===================== frame 1 : original picture =====================
f1 = new_canvas(W, H, name="f1")
f1.blit(src, OX, OY)

# ===================== frame 2 : recoil pose ==========================
SHIFT = 2
DY = -3
f2 = build(SHIFT, DY, "f2")
MOUTH = f2.color("#4a1014")
TONGUE = f2.color("#cc4b3a")

# standing (image-right) leg : rebuilt straight down to the ground line
f2.clear(27, 32, 11, 8)
for y in range(32, 38):
    f2.set(29, y, A)
    f2.rect(30, y, 4, 1, DGR)
    f2.set(34, y, A)
f2.set(30, 38, A)
f2.set(31, 38, YEL)
f2.set(32, 38, DGR)
f2.set(33, 38, YEL)
f2.set(34, 38, A)

# lifted (image-left) leg : pulled up, angled outwards, clear of the ground
f2.clear(8, 32, 10, 4)
f2.set(10, 32, A); f2.rect(11, 32, 5, 1, DGR); f2.set(16, 32, A)
f2.set(8, 33, A);  f2.rect(9, 33, 6, 1, DGR);  f2.set(15, 33, A)
f2.set(7, 34, A);  f2.set(8, 34, YEL); f2.rect(9, 34, 3, 1, DGR)
f2.set(12, 34, YEL); f2.set(13, 34, A)

# ---------------- face : eye rolled up + mouth wide open --------------
pts = [(x, y) for y in range(H) for x in range(W) if f2.get(x, y) in (SKN, LGT)]
ex0 = min(p[0] for p in pts); ex1 = max(p[0] for p in pts)
ey0 = min(p[1] for p in pts); ey1 = max(p[1] for p in pts)
print("old eye bbox", (ex0, ey0, ex1, ey1))

f2.rect(19, 18, 15, 8, GRN)                       # wipe the old eye
for y, (a, b) in {18: (22, 30), 19: (21, 31), 20: (20, 32), 21: (20, 32),
                  22: (20, 32), 23: (21, 31), 24: (22, 30)}.items():
    f2.rect(a, y, b - a + 1, 1, SKN)              # lid / socket
for y, (a, b) in {19: (22, 30), 20: (21, 31), 21: (21, 31),
                  22: (21, 31), 23: (22, 30)}.items():
    f2.rect(a, y, b - a + 1, 1, LGT)              # sclera
f2.rect(24, 19, 5, 2, A)                          # pupil rolled up under the lid

# open mouth
f2.rect(21, 26, 11, 5, A)
for cx, cy in ((21, 26), (31, 26), (21, 30), (31, 30)):
    f2.set(cx, cy, GRN)
f2.rect(22, 27, 9, 3, MOUTH)
f2.rect(23, 29, 7, 1, TONGUE)

# ===================== frame 3 : impact flash =========================
f3 = f2.copy(name="f3")
pal = {p["index"]: p["rgba"] for p in f3.palette()}
cache = {}
for y in range(H):
    for x in range(W):
        i = f3.get(x, y)
        if i == 0:
            continue
        if i not in cache:
            r, g, b, a = pal[i]
            cache[i] = f3.color((min(255, int(r * 0.5 + 110)),
                                 int(g * 0.35), int(b * 0.30), 255))
        f3.set(x, y, cache[i])

# ------------------------- verification -------------------------------
bad = 0
for y in range(SH):
    for x in range(SW):
        want = src.get(x, y)
        got = f1.get(OX + x, OY + y)
        if want != got:
            bad += 1
print("frame1 mismatched pixels:", bad)
print("eye row 24:", [f2.color_name(f2.get(x, 24)) for x in range(18, 35)])
print("leg check left:", [(x, f2.get(x, 34)) for x in range(6, 16)])
for c in (f1, f2, f3):
    print(c.stats_text())

save("demon-cyclop-hit-f1", f1)
save("demon-cyclop-hit-f2", f2)
save("demon-cyclop-hit-f3", f3)
finish([f1, f2, f3])
