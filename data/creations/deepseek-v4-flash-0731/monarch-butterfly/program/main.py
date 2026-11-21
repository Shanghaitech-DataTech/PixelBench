from pixelbench_api import *

W = H = 32
c = new_canvas(W, H)
ORANGE = c.color("#ED7A1E")
BLACK = c.color("#161616")
WHITE = c.color("#FFFFFF")


def inset(poly, d):
    n = len(poly)
    cx = sum(x for x, y in poly) / n
    cy = sum(y for x, y in poly) / n
    out = []
    for x, y in poly:
        dx = x - cx
        dy = y - cy
        L = (dx * dx + dy * dy) ** 0.5
        if L < 1e-6:
            out.append((x, y))
            continue
        out.append((round(x - dx / L * d), round(y - dy / L * d)))
    return out


# ---- body ----
c.circle(16, 7, 2, BLACK)          # head
c.rect(15, 9, 3, 5, BLACK)         # thorax
c.ellipse(16, 20, 2, 7, BLACK)     # abdomen
# antenna (right)
c.line(16, 6, 13, 3, BLACK)
c.circle(13, 2, 1, BLACK)

# ---- right wings ----
FW = [(16, 8), (30, 3), (29, 14), (25, 19), (16, 16)]
HW = [(16, 16), (28, 18), (29, 26), (26, 27), (16, 27)]
c.poly(FW, BLACK)
c.poly(inset(FW, 2), ORANGE)
c.poly(HW, BLACK)
c.poly(inset(HW, 2), ORANGE)

# veins
for a, b in [((16, 9), (26, 5)), ((16, 11), (28, 9)), ((16, 13), (27, 13)),
            ((16, 15), (24, 17)), ((16, 17), (26, 18)), ((16, 19), (27, 22)),
            ((16, 21), (25, 26))]:
    c.line(a[0], a[1], b[0], b[1], BLACK)
for a, b in [((22, 7), (22, 10)), ((24, 11), (24, 14)), ((24, 13), (24, 18))]:
    c.line(a[0], a[1], b[0], b[1], BLACK)

# white spots on black border (right side)
for x, y in [(29, 4), (28, 7), (29, 10), (27, 12), (26, 15),
            (27, 20), (28, 24), (24, 27), (20, 27), (18, 26)]:
    c.set(x, y, WHITE)

# ---- mirror to left ----
m = c.copy()
m.mirror("h")
c.blit(m, 0, 0)

print(c.stats_text())
print(c.matrix_text())
finish(c)
