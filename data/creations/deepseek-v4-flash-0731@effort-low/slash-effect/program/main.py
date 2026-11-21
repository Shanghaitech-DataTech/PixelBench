from pixelbench_api import *
import math

W = H = 48
c = new_canvas(W, H, name="slash")
WHITE = (255, 255, 255, 255)
GRAY = (255, 255, 255, 200)
FAINT = (255, 255, 255, 140)

def arc_points(cx, cy, R, t0, t1, n=48):
    pts = []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n
        pts.append((cx + R * math.cos(t), cy + R * math.sin(t)))
    return pts

def crescent(cv, cx, cy, R, r, t0, t1, col, n=48):
    outer = arc_points(cx, cy, R, t0, t1, n)
    inner = arc_points(cx, cy, r, t1, t0, n)
    cv.poly(outer + inner, col, fill=True)

# ---- Slash effect on a single 48x48 canvas ----
# Frame 2 main element: a large arc slash sweeping up and to the right,
# fully inside bounds.
cx, cy = 24, 26
crescent(c, cx, cy, 21, 16, math.radians(200), math.radians(340), WHITE)

# Trailing streak: a thinner tapering wedge behind the slash (comet tail).
crescent(c, cx, cy, 16, 14, math.radians(200), math.radians(250), GRAY)
# lighter trailing fade to suggest motion
crescent(c, cx, cy, 21, 19, math.radians(200), math.radians(235), FAINT)

# Frame 1 element: a small white arc slash lower-left (the earlier swing).
f1x, f1y = 18, 38
crescent(c, f1x, f1y, 9, 6, math.radians(200), math.radians(310), WHITE)
crescent(c, f1x, f1y, 6, 4.5, math.radians(200), math.radians(290), GRAY)

print(c.stats_text())
for y in range(0, H, 3):
    ln = c.matrix_text(region=(0, y, W-1, y+2), indices=False).splitlines()[1]
    print(ln)

view(c)
finish(c)
