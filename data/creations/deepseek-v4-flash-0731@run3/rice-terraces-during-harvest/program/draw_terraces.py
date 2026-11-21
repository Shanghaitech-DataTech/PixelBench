from pixelbench_api import new_canvas
import math

N = 9

def lrp(a, b, t):
    return a + (b - a) * t

def params(i):
    t = i / (N - 1)
    cx, cy = 31, 25
    R = lrp(29.5, 11.0, t)
    return cx, cy, R

def rmult(th):
    return 1 + 0.07 * math.sin(2 * th + 0.9) + 0.045 * math.sin(5 * th + 0.4)

def contour_pts(i, step=6):
    cx, cy, R = params(i)
    pts = []
    for deg in range(0, 360, step):
        th = math.radians(deg)
        m = rmult(th)
        pts.append((cx + R * m * math.cos(th), cy + R * m * math.sin(th)))
    return pts

def ring_point(i, deg):
    cx, cy, R = params(i)
    th = math.radians(deg)
    m = rmult(th)
    return round(cx + R * m * math.cos(th)), round(cy + R * m * math.sin(th))

def band_col(i):
    t = i / (N - 1)
    r = lrp(196, 232, t)
    g = lrp(152, 205, t)
    b = lrp(78, 150, t)
    if i % 2 == 0:
        r -= 22; g += 6; b += 10      # greener, newer paddy
    else:
        r += 16; g -= 10; b -= 14     # warmer, ripe gold
    return (max(0, min(255, round(r))), max(0, min(255, round(g))), max(0, min(255, round(b))))

def farmer(c, x, y, big):
    shadow = (96, 60, 28)
    pants = (124, 92, 54)
    shirt = (184, 72, 50)
    hat = (234, 194, 104)
    if big:
        c.rect(x, y + 2, 3, 1, shadow)
        c.rect(x, y, 2, 2, pants)
        c.rect(x - 1, y - 2, 3, 2, shirt)
        c.set(x, y - 3, (218, 170, 130))
        c.rect(x - 1, y - 4, 3, 2, hat)
    else:
        c.rect(x, y + 1, 2, 1, shadow)
        c.rect(x, y - 1, 2, 2, pants)
        c.rect(x - 1, y - 2, 3, 2, shirt)
        c.rect(x - 1, y - 3, 3, 2, hat)

def house(c, x, y, pale):
    if pale:
        roof = (152, 100, 62)
        lit = (174, 120, 76)
    else:
        roof = (114, 68, 42)
        lit = (170, 114, 72)
    c.rect(x + 1, y + 2, 4, 1, (90, 58, 30))
    c.rect(x, y, 4, 2, roof)
    c.rect(x, y, 4, 1, lit)

def build():
    c = new_canvas(64, 64, background=(180, 172, 128), name="terraces")

    for i in range(N):
        c.poly(contour_pts(i), band_col(i))

    for i in range(N):
        c.poly(contour_pts(i), (84, 54, 24), fill=False)

    # Slightly different-ripeness patches inside bands (layered light)
    patch = (172, 132, 60)
    for i, degs in ((1, (30, 140, 250)), (3, (70, 200)), (5, (120, 300)), (7, (40, 210))):
        for d in degs:
            ax, ay = ring_point(i, d)
            bx, by = ring_point(i + 1, d)
            c.ellipse((ax + bx) // 2, (ay + by) // 2, 1, 1, patch)

    # Village houses on the upper terraces / meadow (distance)
    houses = [(8, 3, True), (18, 2, True), (28, 3, True), (40, 2, True), (50, 4, True),
              (58, 5, True), (12, 9, False), (22, 8, False), (33, 9, False),
              (45, 7, False), (5, 10, False), (53, 8, False)]
    for hx, hy, pale in houses:
        house(c, hx, hy, pale)

    # Trees / bushes on meadow and along ridges
    trees = [(4, 1), (9, 0), (15, 5), (23, 0), (34, 0), (46, 1), (56, 9), (3, 7),
            (19, 13), (30, 12), (40, 13), (6, 16), (13, 17), (28, 18), (60, 2),
            (0, 21), (8, 22), (24, 20), (36, 20), (48, 21), (58, 22), (1, 27), (60, 27)]
    for tx, ty in trees:
        c.rect(tx, ty, 2, 1, (56, 86, 38))
        c.rect(tx, ty + 1, 2, 1, (42, 66, 30))

    # Footpaths winding from the village down onto the terraces
    path_col = (200, 158, 94)
    c.line(20, 11, 18, 16, path_col)
    c.line(18, 16, 15, 21, path_col)
    c.line(14, 21, 12, 27, path_col)
    c.line(30, 12, 29, 18, path_col)
    c.line(29, 18, 27, 24, path_col)
    c.line(42, 11, 44, 16, path_col)
    c.line(44, 16, 46, 22, path_col)
    c.line(4, 17, 3, 22, path_col)

    # Two farmers on narrow ridges
    fx1, fy1 = ring_point(1, 78)
    fx2, fy2 = ring_point(4, 140)
    farmer(c, fx1, fy1, True)
    farmer(c, fx2, fy2, False)
    return c
