from math import sqrt

W = H = 48
c = new_canvas(W, H, name="magic-staff")

OUTLINE = "#2b1508"
WOOD_DARK = "#4a2a13"
WOOD_MID = "#7c4520"
WOOD_LIGHT = "#a9632e"
WOOD_CORE = "#c9823f"
GRAIN = "#5c3318"

GEM_DARK = "#3d1d78"
GEM_MID = "#6a3bd0"
GEM_LIT = "#9d6cff"
GEM_HI = "#c9a8ff"
WHITE = "#ffffff"

def cubic(p0, p1, p2, p3, n):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts

# --- staff centerline: straight shaft + curved hooked head ---
shaft = [(24.0, float(y)) for y in range(45, 15, -1)]
arch = cubic((24, 16), (24, 4), (38, 4), (38, 16), 40)
curl = cubic((38, 16), (38, 22), (34, 24), (31.5, 25.5), 16)
line = shaft + arch[1:] + curl[1:]
radii = [2.0] * (len(shaft) - 1) + [2.0] * (len(arch) - 1) + [2.0 - i * 1.9 / 15.0 for i in range(16)]

# --- wood (layered circles build a smooth band) ---
for p, r in zip(line, radii):
    c.circle(int(round(p[0])), int(round(p[1])), max(0, int(round(r))), OUTLINE)
for p, r in zip(line, radii):
    c.circle(int(round(p[0])), int(round(p[1])), max(0, int(round(r)) - 1), WOOD_MID)
for p, r in zip(line, radii):
    c.circle(int(round(p[0])), int(round(p[1])), max(0, int(round(r)) - 2), WOOD_LIGHT)
    c.circle(int(round(p[0])), int(round(p[1])), max(0, int(round(r)) - 3), WOOD_CORE)

# --- grip bands + grain ---
for yy in (31, 36, 41):
    c.rect(22, yy, 5, 2, GRAIN)
for (xx, yy) in [(23, 27), (25, 27), (23, 45), (25, 45)]:
    c.set(xx, yy, GRAIN)

# --- magic aura around the curved tip ---
c.circle(32, 25, 11, (96, 54, 190, 34))
c.circle(32, 25, 7, (122, 84, 240, 66))
c.circle(32, 25, 4, (150, 110, 255, 108))

# --- purple crystal at the hook end ---
c.circle(32, 25, 3, GEM_DARK)
c.circle(32, 25, 2, GEM_MID)
c.circle(32, 25, 1, GEM_LIT)
c.set(31, 23, WHITE)
c.set(30, 24, GEM_HI)
c.set(32, 23, GEM_HI)
c.set(33, 26, GEM_DARK)

# --- magic wisps (curling trails) ---
c.path("M 38 19 q 5 -2 7 -10", (157, 118, 255, 110))
c.path("M 35 21 q -3 -3 -7 -1", (122, 84, 240, 90))
c.path("M 41 22 q 4 1 5 -1", (122, 84, 240, 70))

# --- particles ---
parts = [
    (36, 20, GEM_MID), (37, 15, GEM_LIT), (34, 12, GEM_HI), (30, 10, GEM_MID),
    (28, 14, GEM_LIT), (36, 13, GEM_HI), (39, 21, GEM_MID), (44, 15, GEM_LIT),
    (42, 11, GEM_HI), (30, 6, GEM_MID), (33, 4, GEM_LIT), (25, 8, GEM_HI),
    (22, 13, GEM_MID), (20, 20, GEM_LIT), (24, 24, GEM_HI), (27, 29, GEM_LIT),
    (29, 22, GEM_HI), (37, 25, GEM_MID), (43, 26, GEM_LIT), (46, 19, GEM_HI),
    (40, 8, GEM_HI), (25, 2, GEM_LIT), (20, 27, GEM_HI), (17, 22, GEM_MID),
    (36, 33, GEM_MID), (41, 30, GEM_LIT), (44, 32, GEM_HI), (33, 30, GEM_HI),
]
for (x, y, col) in parts:
    c.set(x, y, col)
for (x, y, col) in [(38, 17, GEM_LIT), (39, 13, GEM_HI), (41, 17, GEM_HI), (44, 12, WHITE)]:
    c.set(x, y, col)

# --- sparkles ---
def sparkle(x, y):
    for dx, dy, col in [(-2, 0, GEM_LIT), (2, 0, GEM_LIT), (0, -2, GEM_LIT), (0, 2, GEM_LIT),
                       (-1, -1, GEM_HI), (1, -1, GEM_HI), (-1, 1, GEM_HI), (1, 1, GEM_HI),
                       (0, 0, WHITE)]:
        c.set(x + dx, y + dy, col)

sparkle(41, 9)
sparkle(27, 3)
c.set(45, 21, WHITE); c.set(44, 21, GEM_LIT); c.set(46, 21, GEM_LIT); c.set(45, 20, GEM_LIT); c.set(45, 22, GEM_LIT)

print(c.stats_text())
finish(c)
