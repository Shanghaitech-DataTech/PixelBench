"""Blue-cloak girl mage, 64x64 pixel art, front-facing RPG sprite."""

# ---------------------------------------------------------------- palette
NAVY_D   = "#0c1530"
NAVY     = "#1d2f5e"
NAVY_L   = "#2f4c8c"
NAVY_LL  = "#4a6cb5"
GOLD     = "#e8b04a"
GOLD_D   = "#a9792a"
SKIN     = "#f7d4b0"
SKIN_D   = "#dfae86"
SKIN_DD  = "#b8825f"
HAIR     = "#e3dbf5"
HAIR_L   = "#f8f3ff"
HAIR_D   = "#b4a7d7"
HAIR_DD  = "#8b7cb4"
WHITE    = "#f9fafe"
WHITE_D  = "#ccd3e4"
WHITE_DD = "#98a1bd"
EYE      = "#ffb733"
EYE_D    = "#c07a14"
LASH     = "#2b2242"
MOUTH    = "#c6736b"
TIGHTS   = "#232b47"
WOOD     = "#7d5433"
WOOD_D   = "#573b23"
A_CORE   = "#fff8cc"
A_L      = "#ffd45e"
A_M      = "#ffa418"
A_D      = "#c46f0a"

c = new_canvas(64, 64, name="mage")


def R(x, y, w, h, col):
    c.rect(x, y, w, h, col)


def E(cx, cy, rx, ry, col):
    c.ellipse(cx, cy, rx, ry, col)


def P(pts, col):
    c.poly(pts, col)


def L(x0, y0, x1, y1, col):
    c.line(x0, y0, x1, y1, col)


def span(y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)


def edge(y, pts):
    for i in range(len(pts) - 1):
        y0, x0 = pts[i]
        y1, x1 = pts[i + 1]
        if y0 <= y <= y1:
            if y1 == y0:
                return x0
            return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    return pts[0][1] if y < pts[0][0] else pts[-1][1]


# ---------------------------------------------------------------- glow + orb
c.circle(13, 11, 8, (255, 180, 50, 26))
c.circle(13, 11, 6, (255, 196, 80, 64))
c.circle(13, 11, 5, (255, 214, 140, 120))
c.circle(13, 11, 4, A_D)
c.circle(13, 11, 3, A_M)
c.circle(13, 11, 2, A_L)
c.set(12, 10, A_CORE)
c.set(12, 11, A_CORE)
c.set(11, 11, A_CORE)
for cx, cy in [(21, 4), (5, 18)]:
    c.set(cx, cy, A_L)
    c.set(cx - 1, cy, A_L)
    c.set(cx + 1, cy, A_L)
    c.set(cx, cy - 1, A_L)
    c.set(cx, cy + 1, A_L)
    c.set(cx, cy, A_CORE)

# ---------------------------------------------------------------- staff
R(12, 16, 2, 45, WOOD_D)
R(13, 16, 1, 45, WOOD)
R(11, 15, 4, 2, GOLD)
R(11, 58, 4, 3, GOLD_D)

# ---------------------------------------------------------------- legs + boots
R(27, 44, 5, 9, TIGHTS)
R(35, 44, 5, 9, TIGHTS)
R(26, 52, 6, 8, WHITE)
R(35, 52, 6, 8, WHITE)
R(25, 59, 7, 3, WHITE)
R(34, 59, 7, 3, WHITE)
R(25, 61, 7, 1, WHITE_DD)
R(34, 61, 7, 1, WHITE_DD)
R(30, 53, 2, 6, WHITE_D)
R(39, 53, 2, 6, WHITE_D)
R(30, 59, 2, 2, WHITE_D)
R(39, 59, 2, 2, WHITE_D)
R(26, 52, 6, 1, GOLD)
R(35, 52, 6, 1, GOLD)

# ---------------------------------------------------------------- cloak body
XL = [(22, 25), (26, 23), (31, 22), (36, 21), (41, 18), (47, 16)]
XR = [(22, 41), (26, 43), (31, 44), (36, 45), (41, 48), (47, 50)]
for y in range(22, 48):
    xl = int(round(edge(y, XL)))
    xr = int(round(edge(y, XR)))
    span(y, xl, xr, NAVY)
    span(y, xl, min(xl + 2, xr), NAVY_L)
    span(y, max(xr - 2, xl), xr, NAVY_D)
    c.set(xl, y, NAVY_LL)
    if 39 <= y <= 44:
        c.set(xl + 8, y, NAVY_D)
        c.set(xr - 8, y, NAVY_D)

# white shirt V at the neck
P([(30, 24), (36, 24), (34, 31), (32, 31)], WHITE)
P([(35, 24), (36, 24), (34, 31), (34, 29)], WHITE_D)

# belt
for y in (36, 37):
    xl = int(round(edge(y, XL)))
    xr = int(round(edge(y, XR)))
    span(y, xl + 1, xr - 1, GOLD_D)
R(31, 36, 4, 2, GOLD)
c.set(32, 36, A_CORE)
# hem
for y in (45, 46, 47):
    xl = int(round(edge(y, XL)))
    xr = int(round(edge(y, XR)))
    span(y, xl, xr, NAVY_D if y == 45 else (GOLD if y == 46 else GOLD_D))

# ---------------------------------------------------------------- sleeves + hands
P([(24, 24), (29, 25), (23, 38), (14, 36)], NAVY)
L(24, 24, 14, 36, NAVY_L)
L(29, 25, 23, 38, NAVY_D)
P([(40, 24), (44, 26), (47, 38), (41, 38)], NAVY)
L(44, 26, 47, 38, NAVY_D)
L(40, 24, 41, 38, NAVY_D)
# hands
R(14, 33, 4, 4, SKIN)
R(14, 36, 4, 1, SKIN_D)
R(12, 34, 2, 1, SKIN)
R(12, 36, 2, 1, SKIN)
R(43, 37, 4, 3, SKIN)
R(43, 39, 4, 1, SKIN_D)

# ---------------------------------------------------------------- head
R(28, 10, 11, 12, HAIR)
E(33, 9, 6, 6, HAIR)
E(33, 13, 6, 5, HAIR_D)
R(37, 11, 2, 10, HAIR_D)
R(28, 16, 2, 5, HAIR_D)
# neck
R(31, 18, 4, 4, SKIN_D)
# face
E(33, 13, 4, 5, SKIN)
R(29, 11, 9, 6, SKIN)
R(30, 17, 7, 2, SKIN)
# bangs
R(28, 8, 11, 4, HAIR)
R(28, 11, 2, 1, HAIR)
R(37, 8, 2, 4, HAIR_D)
R(28, 8, 1, 4, HAIR_D)
# eyes
R(29, 12, 3, 1, LASH)
R(35, 12, 3, 1, LASH)
R(30, 13, 2, 1, EYE)
R(35, 13, 2, 1, EYE)
c.set(30, 13, A_CORE)
c.set(35, 13, A_CORE)
R(30, 14, 2, 1, EYE_D)
R(35, 14, 2, 1, EYE_D)
c.set(33, 16, MOUTH)

# collar
P([(27, 21), (39, 21), (40, 24), (26, 24)], NAVY_D)
c.circle(33, 22, 1, GOLD)

# side locks in front
R(27, 11, 2, 14, HAIR)
R(38, 11, 2, 14, HAIR)
R(27, 12, 1, 12, HAIR_D)
R(39, 12, 1, 12, HAIR_D)

finish(c)
