from pixelbench_api import *
import math

def fill_poly(c, pts, color):
    ys = [p[1] for p in pts]
    ymin = int(math.floor(min(ys)))
    ymax = int(math.ceil(max(ys)))
    n = len(pts)
    for y in range(ymin, ymax):
        yy = y + 0.5
        xs = []
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + 1) % n]
            if (y1 <= yy < y2) or (y2 <= yy < y1):
                xs.append(x1 + (yy - y1) * (x2 - x1) / (y2 - y1))
        xs.sort()
        for k in range(0, len(xs) - 1, 2):
            xa = int(math.ceil(xs[k] - 0.5))
            xb = int(math.floor(xs[k + 1] + 0.5))
            for x in range(xa, xb + 1):
                c.set(x, y, color)

def star_pts(cx, cy, R, r):
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        rad = R if i % 2 == 0 else r
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return pts

for R, r in ((4.2, 2.2), (4.2, 2.5)):
    c = new_canvas(16, 16, name="star_%s" % r)
    c.circle(7, 7, 7, '#5C3A10')
    c.circle(7, 7, 6, '#B07E12')
    c.circle(7, 7, 5, '#D9A520')
    c.circle(6, 6, 4, '#F0C855')
    fill_poly(c, star_pts(7.5, 7.5, R, r), '#FFF0A0')
    print("r=%s" % r)
    print(c.matrix_text())
