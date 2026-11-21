from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="monarch")

BLACK = c.color("#141414", "black")
ORANGE = c.color("#f28c1f", "orange")
DARK = c.color("#c85a0e", "darkorange")
YELLOW = c.color("#f7c843", "yellow")
WHITE = c.color("#fff6e3", "white")
BROWN = c.color("#3a2416", "brown")

def sym(x):
    return 31 - x

def spoly(pts, col, fill=True):
    c.poly(pts, col, fill)
    if fill:
        c.poly([(sym(x), y) for x, y in pts], col, fill)
    else:
        c.poly([(sym(x), y) for x, y in pts], col, False)

def sell(cx, cy, rx, ry, col, fill=True):
    c.ellipse(cx, cy, rx, ry, col, fill)
    s = sym(cx)
    if s != cx:
        c.ellipse(s, cy, rx, ry, col, fill)

def sset(x, y, col):
    c.set(x, y, col)
    s = sym(x)
    if s != x:
        c.set(s, y, col)

def sline(x0, y0, x1, y1, col):
    c.line(x0, y0, x1, y1, col)
    c.line(sym(x0), y0, sym(x1), y1, col)

# ---------- wings: black silhouettes ----------
fore = [(16, 9), (18, 6), (23, 4), (28, 5), (30, 9), (29, 14), (24, 18), (19, 17), (16, 14)]
hind = [(16, 15), (18, 17), (23, 17), (26, 19), (27, 23), (24, 28), (19, 29), (16, 25)]
spoly(fore, BLACK)
spoly(hind, BLACK)

# ---------- orange wing fills ----------
fore_o = [(17, 10), (19, 7), (23, 6), (27, 7), (28, 10), (27, 13), (23, 16), (19, 16), (17, 13)]
hind_o = [(17, 16), (19, 18), (23, 18), (25, 20), (25, 23), (23, 26), (20, 27), (17, 24)]
spoly(fore_o, ORANGE)
spoly(hind_o, ORANGE)

# dark orange shading patches
spoly([(19, 12), (21, 10), (24, 10), (25, 12), (24, 14), (21, 14)], DARK)
spoly([(19, 19), (21, 19), (22, 21), (21, 23), (19, 23)], DARK)
# yellow accent patches
spoly([(23, 8), (25, 8), (26, 10), (24, 11)], YELLOW)
spoly([(20, 20), (22, 21), (20, 22)], YELLOW)

# ---------- black veins ----------
sline(18, 15, 23, 6, BLACK)
sline(19, 16, 27, 8, BLACK)
sline(18, 16, 27, 12, BLACK)
sline(20, 15, 24, 16, BLACK)
sline(18, 19, 25, 20, BLACK)
sline(17, 21, 23, 25, BLACK)
sline(19, 25, 24, 21, BLACK)

# black inner edge lines
sline(17, 12, 17, 15, BLACK)

# ---------- white spots on black borders ----------
for (sx, sy) in [(22, 5), (24, 5), (26, 5), (27, 6), (29, 8), (29, 10), (29, 12), (26, 15), (24, 17), (25, 19), (27, 22), (26, 25), (24, 27), (20, 28)]:
    sset(sx, sy, WHITE)

# ---------- body ----------
# antennae
sline(15, 7, 12, 2, BLACK)
sline(14, 2, 11, 3, BLACK)
sset(11, 3, BLACK)
# head
c.rect(15, 5, 2, 3, BLACK)
sset(15, 5, BLACK)  # not needed; rect covers center
# thorax
c.rect(15, 8, 2, 5, BROWN)
# abdomen
c.rect(15, 13, 2, 11, BROWN)
# abdomen segments (black rings)
c.set(15, 16, BLACK); c.set(16, 16, BLACK)
c.set(15, 19, BLACK); c.set(16, 19, BLACK)
c.set(15, 22, BLACK); c.set(16, 22, BLACK)
# white spots on thorax
sset(15, 9, WHITE)
sset(15, 12, WHITE)

finish(c)
print(c.stats_text())
print(c.matrix_text(indices=True))
