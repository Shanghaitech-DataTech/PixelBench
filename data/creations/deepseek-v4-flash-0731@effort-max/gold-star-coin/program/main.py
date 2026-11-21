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

c = new_canvas(16, 16, name="coin")

OUT = '#5C3A10'   # dark brown outline
RIM = '#B07E12'   # darker gold ring
GOLD = '#D9A520'  # main gold
LGOLD = '#F0C855' # light gold inner disc
STAR = '#FFF0A0'  # bright star
WHITE = '#FFFFFF' # sparkle

# Coin body: concentric discs for a beveled look
c.circle(7, 7, 7, OUT)     # outer rim
c.circle(7, 7, 6, RIM)     # dark gold edge
c.circle(7, 7, 5, GOLD)    # main gold
c.circle(6, 6, 4, LGOLD)   # lighter inner disc, offset up-left

# Five-pointed star in the middle
fill_poly(c, star_pts(7.5, 7.5, 4.2, 2.2), STAR)

# Small sparkles on the rim
c.set(3, 4, WHITE)
c.set(12, 11, WHITE)

print(c.stats_text())
print(c.matrix_text())
finish(c)
