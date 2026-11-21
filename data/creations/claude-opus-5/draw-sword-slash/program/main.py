import math

W, H = 96, 88

# ---- palette ----------------------------------------------------------
NAVY   = "#454463"   # kimono
NAVYD  = "#231c2c"   # kimono shade / obi
DARK   = "#120d1c"
SKIN   = "#f3a473"
SKIND  = "#71444c"
BROWN  = "#926e6b"   # hakama
BROWND = "#71444c"
HILT   = "#1b0202"
STEEL  = "#eedddd"
STEELD = "#9b938d"
STEELM = "#b2aeb1"
BLACK  = "#070707"

# ---- frame 1: original picture, recentred on the bigger canvas --------
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 6, 14)

# ---- frame 2 ----------------------------------------------------------
OX, OY = 8, 15                      # original (0,0) -> canvas (OX,OY)
f2 = new_canvas(W, H, name="frame2")
f2.blit(input_canvas, OX, OY)


def R(x, y, w, h, col=None, fill=True):
    """rect in original-image coordinates"""
    if col is None:
        f2.clear(x + OX, y + OY, w, h)
    else:
        f2.rect(x + OX, y + OY, w, h, col, fill=fill)


def S(x, y, col):
    f2.set(x + OX, y + OY, col)


# 1. erase what the draw removes: gripping hand, tsuka, and the left
#    forearm that used to cross the belly
R(47, 37, 15, 7)
R(32, 39, 11, 10)

# 2. rebuild the body under the erased forearm
for y in range(39, 49):
    for x in range(32, 43):
        if y <= 40:
            col = NAVY
        elif y <= 43:
            col = NAVYD if y >= 42 else NAVY
        else:
            col = NAVY if x <= 33 + (y - 44) else BROWN
        f2.set(x + OX, y + OY, col)
# fold hints
for x in range(34, 43):
    S(x, 43, NAVYD)
S(36, 46, BROWND)
S(39, 47, BROWND)
S(41, 45, BROWND)
S(33, 41, NAVYD)

# 3. right sleeve now ends in a cuff with the hand hanging free
R(48, 37, 8, 3, NAVY)
for x in range(48, 56):
    S(x, 39, NAVYD)
S(55, 37, NAVYD)
S(55, 38, NAVYD)
R(50, 40, 5, 3, SKIN)
for x in range(50, 55):
    S(x, 42, SKIND)
S(54, 40, SKIND)
S(49, 41, SKIND)

# ---- the slash trail: lower-left sweeping up to the upper right -------
P0, P1, P2 = (8, 76), (44, 71), (74, 27)


def bez(t):
    u = 1 - t
    return (u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0],
            u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1])


ANCHORS = [(0.0, 0.0), (0.3, 0.7), (0.55, 1.4), (0.78, 1.8), (0.92, 1.0), (1.0, 0.0)]


def halfwidth(t):
    for (ta, wa), (tb, wb) in zip(ANCHORS, ANCHORS[1:]):
        if ta <= t <= tb:
            k = (t - ta) / (tb - ta)
            return wa + k * (wb - wa)
    return ANCHORS[-1][1]


steps = 260
for i in range(steps + 1):
    t = i / steps
    x, y = bez(t)
    nx, ny = bez(min(1.0, t + 0.01))
    dx, dy = nx - x, ny - y
    d = math.hypot(dx, dy) or 1.0
    px, py = -dy / d, dx / d
    w = halfwidth(t)
    f2.line(round(x - px * w), round(y - py * w),
            round(x + px * w), round(y + py * w), BLACK)

# thin streaks echoing the sweep
f2.line(14, 72, 27, 69, BLACK)
f2.line(33, 72, 45, 70, BLACK)
f2.line(63, 55, 68, 46, BLACK)
f2.line(72, 38, 77, 29, BLACK)

# ---- raised left arm, finishing high on the right ---------------------
for k in range(-2, 3):
    f2.line(50, 44 + k, 63, 34 + k, NAVY)
f2.line(50, 46, 63, 36, NAVYD)
f2.line(51, 42, 63, 32, NAVYD)
f2.set(49, 44, NAVYD)
f2.set(49, 45, DARK)

for k in range(-1, 2):
    f2.line(62, 34 + k, 68, 30 + k, SKIN)
f2.line(62, 36, 68, 32, SKIND)

f2.rect(67, 28, 4, 4, SKIN)
f2.set(70, 27, SKIN)
f2.set(66, 31, SKIND)
f2.set(70, 31, SKIND)
f2.line(68, 28, 70, 30, SKIND)

# ---- sword -------------------------------------------------------------
f2.line(64, 34, 68, 30, HILT)
f2.line(65, 34, 69, 30, HILT)
f2.line(70, 29, 72, 27, HILT)
f2.line(71, 30, 73, 28, HILT)
f2.line(71, 24, 75, 28, STEELM)
f2.set(73, 26, STEELD)
f2.line(74, 25, 89, 10, STEEL)
f2.line(75, 26, 90, 11, STEELD)
f2.line(74, 24, 88, 10, STEEL)
f2.set(90, 9, STEEL)
f2.set(91, 9, STEELD)

view(f1)
view(f2)
finish([f1, f2])
