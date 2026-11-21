# Fast food combo meal on a tray - 64x64 pixel art, 45 degree top-down view
# Items: cheeseburger, fries in red carton, chicken nuggets, cola cup, 2 sauce cups

# ---------------- palette ----------------
DARK      = "#2a1a20"
TRAY      = "#a8402f"
TRAY_HI   = "#c8604a"
TRAY_SH   = "#7d2a1e"
RECESS    = "#8b3426"
LINER     = "#f7f0e3"
LINER_SH  = "#e4dac7"
SHADOW    = "#ded2bc"

BUN       = "#e8a95d"
BUN_HI    = "#f9cd8d"
BUN_SH    = "#c9853d"
BUN_DK    = "#a76a2e"
BUN2      = "#dc9c50"
SEED      = "#fdf0d0"

LETTUCE   = "#77b93a"
LET_HI    = "#a6d75d"
LET_SH    = "#4e8a27"

CHEESE    = "#f8c33f"
CHE_HI    = "#ffd970"
CHE_SH    = "#dfa226"

PATTY     = "#6d3b23"
PATTY_HI  = "#8b5334"
PATTY_SH  = "#4a2415"

FRY       = "#f3c452"
FRY_HI    = "#ffdd8b"
FRY_SH    = "#d09a2e"

CARTON    = "#d43c2c"
CARTON_HI = "#ef5f4a"
CARTON_SH = "#a52a1e"
CARTON_IN = "#6d1a12"
BAND_W    = "#f8f1e5"

CUP       = "#f4f1e9"
CUP_HI    = "#ffffff"
CUP_SH    = "#d3ccbf"
CUP_SH2   = "#b3ab9e"
BAND_R    = "#cf3a30"
BAND_R_HI = "#e8604f"
COLA      = "#3a1d13"
COLA_HI   = "#6b3a22"
ICE       = "#dcecf4"
ICE_SH    = "#a7c5d3"
STRAW_R   = "#d9403a"
STRAW_W   = "#f7f5ef"

NUG       = "#d9922f"
NUG_HI    = "#f2b451"
NUG_SH    = "#a86a20"
NUG_DK    = "#7c4a17"

SAUCE_W   = "#f5f2ea"
SAUCE_SH  = "#d5cec0"
KETCHUP   = "#c8342a"
KETCH_HI  = "#e2564a"
MUSTARD   = "#edc53f"
MUST_HI   = "#f7dd86"


# ---------------- helpers ----------------
def rrect(x0, y0, x1, y1, r):
    return (f"M{x0+r} {y0} H{x1-r} A{r} {r} 0 0 1 {x1} {y0+r} V{y1-r}"
            f" A{r} {r} 0 0 1 {x1-r} {y1} H{x0+r} A{r} {r} 0 0 1 {x0} {y1-r}"
            f" V{y0+r} A{r} {r} 0 0 1 {x0+r} {y0} Z")


def paste(base, art, dark=DARK):
    """Blit art onto base, first drawing a 1px dark outline around its silhouette."""
    w, h, data = art.to_rgba()
    m = [[False] * w for _ in range(h)]
    for y in range(h):
        ro = y * w * 4
        for x in range(w):
            if data[ro + x * 4 + 3] > 0:
                m[y][x] = True
    for y in range(h):
        for x in range(w):
            if m[y][x]:
                continue
            touch = False
            for dy in (-1, 0, 1):
                ny = y + dy
                if ny < 0 or ny >= h:
                    continue
                for dx in (-1, 0, 1):
                    nx = x + dx
                    if 0 <= nx < w and m[ny][nx]:
                        touch = True
            if touch:
                base.set(x, y, dark)
    base.blit(art, 0, 0)


def fry(cv, x, y, dx, ln, w=3, body=FRY, hi=FRY_HI, sh=FRY_SH):
    x2 = x + w - 1
    cv.poly([(x - 1, y + 1), (x2 + 1, y + 1), (x2 + dx + 1, y - ln - 1), (x + dx - 1, y - ln - 1)], DARK)
    cv.poly([(x, y), (x2, y), (x2 + dx, y - ln), (x + dx, y - ln)], body)
    cv.line(x, y, x + dx, y - ln, hi)
    cv.line(x2, y, x2 + dx, y - ln, sh)


def nugget(cv, cx, cy, rx=4, ry=3):
    pts = [(cx - rx, cy), (cx - rx + 2, cy - ry), (cx + 1, cy - ry), (cx + rx - 1, cy - ry + 1),
           (cx + rx, cy + 1), (cx + rx - 2, cy + ry), (cx - 1, cy + ry), (cx - rx + 1, cy + ry - 1)]
    cv.poly(pts, NUG)
    cv.poly([(cx - rx + 2, cy - ry + 1), (cx + 1, cy - ry + 1), (cx - 1, cy - 1), (cx - rx + 2, cy - 1)], NUG_HI)
    cv.set(cx - rx + 2, cy - ry, NUG_HI)
    cv.set(cx, cy - ry, NUG_HI)
    for (dx, dy) in [(2, 1), (-2, 2), (3, -1), (-3, 1), (0, 2), (1, -1), (-1, -1), (2, 2)]:
        cv.set(cx + dx, cy + dy, NUG_SH)
    for (dx, dy) in [(2, -1), (-1, 1), (2, 1), (-2, -1), (1, 2)]:
        cv.set(cx + dx, cy + dy, NUG_DK)


def sauce_cup(cv, cx, cy, r, sauce, hi):
    # tub body
    cv.rect(cx - 5, cy + 2, 11, 1, SAUCE_W)
    cv.rect(cx - 5, cy + 3, 10, 1, SAUCE_W)
    cv.rect(cx - 4, cy + 4, 8, 1, SAUCE_W)
    cv.rect(cx + 4, cy + 2, 1, 2, SAUCE_SH)
    cv.set(cx + 3, cy + 4, SAUCE_SH)
    # rim
    cv.rect(cx - 3, cy - 2, 7, 1, SAUCE_W)
    cv.rect(cx - 5, cy - 1, 11, 1, SAUCE_W)
    cv.rect(cx - 6, cy, 13, 1, SAUCE_W)
    cv.rect(cx - 5, cy + 1, 11, 1, SAUCE_W)
    # sauce surface
    cv.rect(cx - 4, cy - 1, 9, 1, sauce)
    cv.rect(cx - 5, cy, 11, 1, sauce)
    cv.rect(cx - 4, cy + 1, 9, 1, sauce)
    cv.set(cx - 3, cy - 1, hi)
    cv.set(cx - 2, cy - 1, hi)
    cv.set(cx - 3, cy, hi)
    cv.set(cx + 3, cy + 1, hi)


def straw(cv, x0, y0, x1, y1, w=2, seg=3):
    n = max(abs(x1 - x0), abs(y1 - y0))
    for i in range(n + 1):
        t = i / n
        x = int(round(x0 + (x1 - x0) * t))
        y = int(round(y0 + (y1 - y0) * t))
        col = STRAW_W if (i // seg) % 2 == 0 else STRAW_R
        for j in range(w):
            cv.set(x + j, y, col)


# ---------------- canvas + tray ----------------
c = new_canvas(64, 64, name="combo")

c.path(rrect(0, 1, 63, 62, 7), DARK, fill=True)
c.path(rrect(1, 2, 62, 61, 6), TRAY, fill=True)
c.path("M 2 26 V 9 A 6 6 0 0 1 8 3 H 34", TRAY_HI, fill=False)
c.path("M 61 20 V 54 A 6 6 0 0 1 55 60 H 30", TRAY_SH, fill=False)
c.path(rrect(3, 4, 60, 59, 4), RECESS, fill=True)
c.path(rrect(4, 5, 60, 59, 4), LINER, fill=True)

# liner creases / crumbs
for d in ["M 32 9 L 35 7", "M 33 13 L 36 11", "M 31 26 L 34 28", "M 33 33 L 36 31",
          "M 8 34 L 11 36", "M 56 55 L 59 57"]:
    c.path(d, LINER_SH, fill=False)
for (x, y) in [(34, 16), (33, 22), (32, 40), (30, 50), (58, 46), (7, 30)]:
    c.set(x, y, LINER_SH)

# contact shadows
c.ellipse(18, 29, 10, 2, SHADOW)     # fries carton
c.ellipse(49, 32, 8, 2, SHADOW)      # cola cup
c.ellipse(16, 58, 12, 2, SHADOW)     # burger
for (cx, cy) in [(39, 41), (49, 41), (57, 45), (44, 48)]:
    c.ellipse(cx, cy, 5, 2, SHADOW)
c.ellipse(37, 57, 6, 1, SHADOW)
c.ellipse(52, 57, 6, 1, SHADOW)


# ---------------- fries in red carton ----------------
fr = new_canvas(64, 64, name="fries")
fr.ellipse(18, 18, 10, 4, CARTON)
fr.ellipse(18, 17, 9, 3, CARTON_HI)
fr.ellipse(18, 18, 8, 3, CARTON_IN)
# back row of fries
fry(fr, 9, 19, -2, 12)
fry(fr, 13, 19, 0, 14)
fry(fr, 17, 19, 1, 13)
fry(fr, 21, 19, 2, 12)
fry(fr, 24, 19, 3, 10)
# front row
fry(fr, 11, 20, -1, 9, body=FRY_SH)
fry(fr, 15, 20, 1, 10)
fry(fr, 19, 20, -1, 8, body=FRY_SH)
fry(fr, 22, 20, 1, 9)
# carton front face
fr.path("M 8 18 Q 18 24 28 18 L 26 29 Q 18 32 10 29 Z", CARTON, fill=True)
fr.path("M 23 20 Q 26 20 28 18 L 26 29 Q 24 30 23 30.4 Z", CARTON_SH, fill=True)
fr.path("M 8 18 Q 10 19.5 11 20.3 L 12 29.6 Q 10.6 29.3 10 29 Z", CARTON_HI, fill=True)
fr.path("M 9 22 Q 18 26.5 27 22 L 27 25 Q 18 29.5 9 25 Z", BAND_W, fill=True)
fr.path("M 8 18 Q 18 24 28 18", DARK, fill=False)
paste(c, fr)


# ---------------- cola cup ----------------
cup = new_canvas(64, 64, name="cup")
cup.path("M 38 13 L 41 31 Q 48 34 55 31 L 58 13 Z", CUP, fill=True)
cup.poly([(40, 15), (42, 15), (44, 31), (42, 31)], CUP_HI)
cup.poly([(54, 15), (57, 15), (54, 31), (52, 31)], CUP_SH)
cup.path("M 42 30 Q 48 33 54 30", CUP_SH2, fill=False)
# red band
cup.path("M 39 19 Q 48 22 57 19 L 56 25 Q 48 28 40 25 Z", BAND_R, fill=True)
cup.path("M 39 19 Q 43 20.4 47 21 L 46 27 Q 42 26.4 40 25 Z", BAND_R_HI, fill=True)
cup.path("M 40 22 Q 48 25 56 22", BAND_W, fill=False)
# rim + drink
cup.ellipse(48, 13, 10, 4, CUP_HI)
cup.ellipse(48, 13, 9, 3, CUP_SH)
cup.ellipse(48, 14, 8, 3, COLA)
# ice cubes + straw (back cube, straw, front cubes)
def ice_cube(cv, x, y, h=3):
    cv.rect(x, y, 4, h, ICE)
    cv.rect(x, y, 3, 1, CUP_HI)
    cv.rect(x, y + h - 1, 4, 1, ICE_SH)
    for i in range(h):
        cv.set(x + 3, y + i, ICE_SH)
    cv.set(x + 3, y, ICE_SH)

ice_cube(cup, 42, 12)
straw(cup, 47, 15, 41, 6)
ice_cube(cup, 49, 12)
ice_cube(cup, 45, 15, 2)
cup.set(53, 14, COLA_HI); cup.set(54, 15, COLA_HI); cup.set(41, 14, COLA_HI)
paste(c, cup)


# ---------------- cheeseburger ----------------
bg = new_canvas(64, 64, name="burger")
# top bun
bg.path("M 4 47 C 4 37 9 35 16 35 C 23 35 28 37 28 47 Z", BUN, fill=True)
bg.path("M 7 45 C 7 38 11 36 17 36 C 12 37 9 40 9 45 Z", BUN_HI, fill=True)
bg.path("M 28 47 C 28 41 25 37 20 36 C 25 38 26 42 26 47 Z", BUN_SH, fill=True)
bg.rect(16, 45, 11, 2, BUN_SH)
bg.path("M 4 47 C 4 43 5 40 7 38", BUN_HI, fill=False)
# sesame seeds
for (sx, sy, vert) in [(10, 39, 0), (14, 37, 0), (19, 38, 0), (23, 40, 1),
                       (8, 43, 0), (13, 42, 1), (18, 43, 0), (24, 44, 0),
                       (11, 46, 0), (21, 46, 0), (16, 40, 1)]:
    if vert:
        bg.rect(sx, sy, 1, 2, SEED)
    else:
        bg.rect(sx, sy, 2, 1, SEED)
# lettuce
d = "M 3 46 H 29 V 48"
xs = list(range(29, 2, -3))
for i in range(len(xs) - 1):
    x0, x1 = xs[i], xs[i + 1]
    d += f" Q {(x0 + x1) / 2} 52 {x1} 48"
d += " L 3 48 Z"
bg.path(d, LETTUCE, fill=True)
bg.rect(4, 46, 24, 1, LET_HI)
for x in xs[1:]:
    bg.set(x, 48, LET_SH)
    bg.set(x, 49, LET_SH)
bg.set(5, 48, LET_HI); bg.set(11, 48, LET_HI); bg.set(17, 48, LET_HI); bg.set(23, 48, LET_HI)
# cheese
bg.path("M 4 48 H 28 V 51 L 25 51 L 24 54 L 22 51 L 18 51 L 17 55 L 15 51 L 10 51 L 9 54 L 7 51 L 4 51 Z",
        CHEESE, fill=True)
bg.rect(5, 48, 22, 1, CHE_HI)
bg.set(24, 52, CHE_SH); bg.set(24, 53, CHE_SH); bg.set(17, 53, CHE_SH)
bg.set(17, 54, CHE_SH); bg.set(9, 52, CHE_SH); bg.set(9, 53, CHE_SH)
bg.set(27, 49, CHE_SH); bg.set(27, 50, CHE_SH)
# patty
bg.path("M 6 51 H 26 Q 28 51 28 52 V 54 Q 28 55 26 55 H 6 Q 4 55 4 54 V 52 Q 4 51 6 51 Z", PATTY, fill=True)
for (px, py) in [(7, 52), (11, 53), (15, 52), (20, 53), (24, 52), (9, 54), (18, 54), (26, 53)]:
    bg.set(px, py, PATTY_HI)
for (px, py) in [(8, 53), (13, 54), (22, 54), (25, 54), (6, 54), (16, 53)]:
    bg.set(px, py, PATTY_SH)
# lettuce frill tips peeking over the patty
for fx in (6, 13, 20, 27):
    bg.set(fx, 51, LETTUCE)
    bg.set(fx, 52, LET_SH)
# bottom bun
bg.path("M 6 55 H 26 V 57 Q 26 59 23 59 H 9 Q 6 59 6 57 Z", BUN2, fill=True)
bg.rect(7, 55, 19, 1, BUN_HI)
bg.path("M 7 58 H 25", BUN_DK, fill=False)
bg.path("M 23 56 H 26 V 57 Q 26 59 23 59 Z", BUN_SH, fill=True)
paste(c, bg)


# ---------------- nuggets ----------------
for (cx, cy, rx, ry) in [(38, 38, 5, 3), (48, 37, 5, 4), (56, 42, 4, 3), (43, 45, 5, 3)]:
    ng = new_canvas(64, 64, name="nug")
    nugget(ng, cx, cy, rx, ry)
    paste(c, ng)


# ---------------- dipping sauce cups ----------------
s1 = new_canvas(64, 64, name="sauce1")
sauce_cup(s1, 37, 51, 6, KETCHUP, KETCH_HI)
paste(c, s1)
s2 = new_canvas(64, 64, name="sauce2")
sauce_cup(s2, 52, 51, 6, MUSTARD, MUST_HI)
paste(c, s2)


view(c)
save("combo", c)
print(c.stats_text())
finish(c)
