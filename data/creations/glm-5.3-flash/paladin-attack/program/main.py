import math

IN = input_canvas
W, H = 48, 64

# palette indices present in the input drawing
WHITE, PALE, GLOW = 31, 36, 32          # #ffffff, #ffefc6, #f3d887
LT, MID, DKST = 18, 5, 15               # #dccaca, #a9a5ab, #858086
DKR, DARK, BROWN = 16, 21, 7            # #5a565a, #332d32, #512a13
GOLD, YEL = 10, 25                      # #af7a18, #ffe38c
OUTL, SHADOW = 1, 41


def dump(c, x0, y0, x1, y1, title):
    print(f"--- {title} ---")
    print('     ' + ''.join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ''
        for x in range(x0, x1 + 1):
            i = c.get(x, y)
            row += '.' if not i else ('_' if i == 41 else
                   "abcdefghijklmnopqrstuvwxyz"[i - 1] if i <= 26 else
                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i - 27])
        print(f"{y:3d} {row}")


# ================= FRAME 1 : the original picture =================
f1 = new_canvas(W, H, background=None, name='f1_guard')
f1.blit(IN, 0, 0)

# ================= FRAME 2 : heavy downward smash =================
f2 = new_canvas(W, H, background=None, name='f2_smash')
f2.blit(IN, 0, 0)

# --- 1. take the old weapon out of the hand, keep the sword arm ---
keep = {11: (32, 34), 12: (31, 35), 13: (30, 35), 14: (29, 31), 15: (30, 33),
        16: (31, 33), 17: (30, 34), 18: (30, 36), 19: (29, 36),
        20: (28, 36), 21: (28, 36)}
for y in range(8, 22):
    lo, hi = keep.get(y, (0, -1))
    for x in range(25, W):
        if f2.get(x, y) == 0:
            continue
        if y <= 11:
            if x <= 34 and not (lo <= x <= hi):
                f2.set(x, y, None)
        elif x >= 30 and not (lo <= x <= hi):
            f2.set(x, y, None)

# --- 2. white motion trail: the arc the blade has already swept ---
Ax, Ay, Cx, Cy, Bx, By = 28.0, 3.0, 45.0, 4.0, 44.0, 20.0
N = 36
for i in range(N + 1):
    t = i / N
    if t < 0.30 and i % 2:          # ragged fade at the far end
        continue
    x = (1 - t) ** 2 * Ax + 2 * t * (1 - t) * Cx + t * t * Bx
    y = (1 - t) ** 2 * Ay + 2 * t * (1 - t) * Cy + t * t * By
    tx = 2 * (1 - t) * (Cx - Ax) + 2 * t * (Bx - Cx)
    ty = 2 * (1 - t) * (Cy - Ay) + 2 * t * (By - Cy)
    L = math.hypot(tx, ty) or 1.0
    px, py = -ty / L, tx / L
    w = 1.0 + 2.2 * t
    for k in range(-3, 4):
        if abs(k) > w:
            continue
        xx = int(round(x + k * px)); yy = int(round(y + k * py))
        if 0 <= xx < W and 0 <= yy < H and f2.get(xx, yy) == 0:
            f2.set(xx, yy, WHITE if abs(k) <= w - 0.8 else PALE)
for (x, y, c) in [(28, 1, PALE), (29, 1, GLOW), (27, 2, PALE), (30, 2, GLOW),
                  (29, 6, GLOW), (30, 7, PALE)]:
    f2.set(x, y, c)

# --- 3. the blade, hinged down in front of the paladin ---
spine = [(36 + i, 13 + i) for i in range(9)]
for (dx, dy), col in [((0, 1), LT), ((0, 0), MID), ((1, 0), DKST),
                      ((2, 0), BROWN), ((3, 0), GOLD)]:
    for (sx, sy) in spine:
        f2.set(sx + dx, sy + dy, col)
f2.set(45, 22, LT); f2.set(46, 23, WHITE)                 # tip
f2.set(33, 15, YEL); f2.set(34, 14, GOLD); f2.set(35, 13, GOLD)
f2.set(36, 12, GOLD); f2.set(37, 11, YEL)                 # crossguard
f2.set(34, 12, BROWN); f2.set(35, 12, BROWN)              # grip
f2.set(33, 11, DARK); f2.set(34, 11, DARK); f2.set(35, 11, DKR)   # cuff

# --- 4. the left foot steps forward (toe now points into the attack) ---
blk = [[f2.get(x, y) for x in range(9, 18)] for y in range(50, 59)]
for y in range(50, 59):
    for x in range(9, 18):
        f2.set(x, y, None)
for j in range(9):
    for i in range(9):
        v = blk[j][8 - i]
        if v:
            f2.set(13 + i, 51 + j, v)
for x, c in [(13, DARK), (14, DKR), (15, DKR), (16, DARK), (17, DKR)]:
    f2.set(x, 50, c)                                      # ankle bridge
f2.set(21, 56, OUTL); f2.set(21, 57, OUTL); f2.set(13, 55, OUTL)
f2.set(13, 58, OUTL); f2.set(14, 58, DARK)

# --- 5. re-ground the cast shadow under the new stance ---
for x in range(5, 13):
    f2.set(x, 59, None)
for x in range(7, 11):
    f2.set(x, 60, None)
for x in range(9, 13):
    f2.set(x, 57, SHADOW); f2.set(x, 58, SHADOW)
for x in range(13, 16):
    f2.set(x, 59, SHADOW)
for x in range(21, 24):
    f2.set(x, 59, SHADOW)
for x in range(15, 23):
    f2.set(x, 60, SHADOW)

print(f1.stats_text())
print(f2.stats_text())
dump(f2, 24, 0, 47, 26, "FRAME2 weapon + trail")
dump(f2, 4, 44, 30, 62, "FRAME2 footing")
finish([f1, f2])
