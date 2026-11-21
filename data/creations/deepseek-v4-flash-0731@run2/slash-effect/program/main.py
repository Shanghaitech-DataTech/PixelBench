from pixelbench_api import *
import math

W = H = 48
c = new_canvas(W, H, name="slash")
white = c.color("#ffffff")


def sample(points, n=140):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = points
    out = []
    for i in range(n + 1):
        t = i / n
        mt = 1.0 - t
        x = mt**3 * x0 + 3 * mt * mt * t * x1 + 3 * mt * t * t * x2 + t**3 * x3
        y = mt**3 * y0 + 3 * mt * mt * t * y1 + 3 * mt * t * t * y2 + t**3 * y3
        out.append((x, y))
    return out


def brush(points, thick, n=140):
    s = sample(points, n)
    prev = None
    for i, (x, y) in enumerate(s):
        t = i / n
        r = max(1.2, thick * math.sin(math.pi * t))
        c.circle(round(x), round(y), r, white, fill=True)
        if prev is not None:
            # connect consecutive discs so the stroke core is solid
            c.line(prev[0], prev[1], round(x), round(y), white)
        prev = (round(x), round(y))


# Main sweeping slash arc, tapered from rounded tip to rounded tip.
brush([(5, 6), (1, 27), (20, 48), (37, 40)], 3.6)

# Trailing streak: shorter tapering tail beyond the lower-right tip.
brush([(37, 40), (41, 41), (45, 43), (44, 46)], 2.2, n=60)

# Secondary short motion streak behind the upper tip.
brush([(6, 6), (12, 4), (16, 5), (19, 10)], 1.9, n=60)

print(c.stats_text())
print(c.matrix_text())
finish(c)
