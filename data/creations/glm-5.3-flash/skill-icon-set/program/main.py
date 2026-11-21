import numpy as np

W = H = 64
c = new_canvas(W, H, background=None, name="skill_icons")

# ------------------------------------------------------------------ palette
# one shared ink + a deep/mid/light/pale ramp per element
iINK = c.color("#1e1a2e")
iFD = c.color("#8f1d24"); iFR = c.color("#cf3b2a"); iFO = c.color("#f2821f")
iFL = c.color("#ffa62b"); iFY = c.color("#ffd23f"); iFP = c.color("#fff0a8")
iID = c.color("#2b6a9b"); iIM = c.color("#57a8d8"); iIL = c.color("#9fd8f0"); iIP = c.color("#e2f6ff")
iW  = c.color("#ffffff")
iHD = c.color("#1e8a4a"); iHM = c.color("#3ec46a"); iHL = c.color("#8ce8a0"); iHP = c.color("#dcffe4")
iLD = c.color("#e08e1b"); iLM = c.color("#ffcf3f"); iLL = c.color("#fff4a8")


def grid():
    w, h, rgba = c.to_rgba()
    a = np.frombuffer(rgba, dtype=np.uint8).reshape(h, w, 4)
    alpha = a[:, :, 3] > 0
    idx = np.full((h, w), -1, dtype=np.int32)
    ys, xs = np.nonzero(alpha)
    for y, x in zip(ys.tolist(), xs.tolist()):
        idx[y, x] = c.get(x, y)
    return alpha, idx


def shade(bases, light, dark, box):
    """Bevel every pixel of `bases` inside box: dark on down/right edges, light on up/left."""
    alpha, idx = grid()
    x0, y0, x1, y1 = box
    bases = set(bases)
    todo = []

    def same(xx, yy):
        return 0 <= xx < W and 0 <= yy < H and bool(alpha[yy, xx]) and int(idx[yy, xx]) in bases

    for y in range(max(0, y0), min(H - 1, y1) + 1):
        for x in range(max(0, x0), min(W - 1, x1) + 1):
            if idx[y, x] not in bases:
                continue
            if not same(x, y + 1) or not same(x + 1, y):
                todo.append((x, y, dark))
            elif not same(x, y - 1) or not same(x - 1, y):
                todo.append((x, y, light))
    for x, y, col in todo:
        c.set(x, y, col)


def outline():
    """1px dark outline around every opaque shape."""
    alpha, _ = grid()
    p = np.pad(alpha, 1)
    d = np.zeros_like(alpha)
    for dy in (0, 1, 2):
        for dx in (0, 1, 2):
            if dx == 1 and dy == 1:
                continue
            d |= p[dy:dy + H, dx:dx + W]
    ys, xs = np.nonzero(d & ~alpha)
    for y, x in zip(ys.tolist(), xs.tolist()):
        c.set(x, y, iINK)


def sparkle(cx, cy, arm, core):
    c.set(cx, cy, core)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        c.set(cx + dx, cy + dy, arm)


# ---------------------------------------------------------------- fireball
def fireball(ox, oy):
    tail = [(4, 10, 11), (5, 9, 12), (6, 8, 13), (7, 7, 14), (8, 7, 15), (9, 6, 16),
            (10, 6, 17), (11, 5, 18), (12, 6, 19), (13, 7, 20), (14, 8, 21),
            (15, 10, 22), (16, 12, 23)]
    for y, a, b in tail:
        for x in range(a, b + 1):
            c.set(ox + x, oy + y, iFR)
    shade({iFR}, iFO, iFD, (ox + 3, oy + 3, ox + 24, oy + 17))
    cx, cy = ox + 19, oy + 20
    c.circle(cx, cy, 8, iFD)
    c.circle(cx, cy, 7, iFR)
    c.circle(cx, cy, 6, iFO)
    c.circle(cx - 1, cy - 1, 4, iFL)
    c.circle(cx - 1, cy - 1, 3, iFY)
    c.circle(cx - 2, cy - 2, 2, iFP)
    # detached ember drifting below the tail
    c.set(ox + 5, oy + 21, iFO); c.set(ox + 6, oy + 21, iFR)
    c.set(ox + 5, oy + 22, iFR); c.set(ox + 6, oy + 22, iFD)


# ------------------------------------------------------------------ shield
def shield(ox, oy):
    outer = [(9, 4), (22, 4), (24, 6), (26, 9), (26, 15), (24, 20), (20, 25), (16, 28),
             (15, 28), (11, 25), (7, 20), (5, 15), (5, 9), (7, 6)]
    inner = [(11, 6), (20, 6), (22, 8), (23, 10), (23, 14), (22, 17), (19, 22), (16, 25),
             (15, 25), (12, 22), (9, 17), (8, 14), (8, 10), (9, 8)]
    c.poly([(ox + x, oy + y) for x, y in outer], iID)
    c.poly([(ox + x, oy + y) for x, y in inner], iIM)
    shade({iIM}, iIL, iID, (ox + 4, oy + 3, ox + 27, oy + 28))
    for y in range(9, 23):
        c.set(ox + 15, oy + y, iIP)
        c.set(ox + 16, oy + y, iIP)
    for x in range(10, 22):
        c.set(ox + x, oy + 14, iIP)
        c.set(ox + x, oy + 15, iIP)
    c.rect(ox + 15, oy + 14, 2, 2, iW)


# -------------------------------------------------------------------- heal
def heal(ox, oy):
    plus = [(12, 4), (20, 4), (20, 12), (28, 12), (28, 20), (20, 20), (20, 28),
            (12, 28), (12, 20), (4, 20), (4, 12), (12, 12)]
    c.poly([(ox + x, oy + y) for x, y in plus], iHM)
    shade({iHM}, iHL, iHD, (ox + 3, oy + 3, ox + 29, oy + 29))
    c.rect(ox + 14, oy + 6, 2, 2, iHP)
    c.rect(ox + 6, oy + 14, 2, 2, iHP)


# -------------------------------------------------------------------- bolt
def bolt(ox, oy):
    pts = [(20, 3), (6, 17), (15, 17), (12, 28), (26, 12), (18, 12)]
    c.poly([(ox + x, oy + y) for x, y in pts], iLM)
    shade({iLM}, iLL, iLD, (ox + 4, oy + 2, ox + 27, oy + 29))


fireball(0, 0)
shield(32, 0)
heal(0, 32)
bolt(32, 32)
sparkle(6, 38, iHM, iHL)     # heal, upper-left notch
sparkle(26, 58, iHM, iHL)    # heal, lower-right notch
sparkle(58, 37, iLM, iLL)    # bolt, off the upper tip
outline()

print(c.stats_text())
for r in ((0, 0, 31, 31), (32, 0, 63, 31), (0, 32, 31, 63), (32, 32, 63, 63)):
    print(c.matrix_text(region=r))
finish(c)
