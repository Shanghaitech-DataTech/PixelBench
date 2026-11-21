import math
from pixelbench_api import new_canvas, view, save, finish

# 48x48 canvas, transparent background.
# Two frames stacked vertically (sprite-sheet style):
#   frame 1 (top,    y 0..23): small white arc slash
#   frame 2 (bottom, y 24..47): larger arc slash + trailing streak
c = new_canvas(48, 48, background=None, name="slash_effect")

WHITE = c.color("#ffffff", name="white")
COOL  = c.color("#cfe2ff", name="cool_rim")
ST1   = c.color("#e2e2e2", name="trail_hi")
ST2   = c.color("#b8b8b8", name="trail_mid")
ST3   = c.color("#8a8a8a", name="trail_lo")


def arc_pixels(T1, T2, h, thick):
    """Tapered crescent (arc band) from tip T1 to tip T2, bowing out by h.

    Returns (dict (x,y)->(u,dist,t), (ox,oy,R,apex_x,apex_y)).
    u=1 at the arc's apex, 0 at the tips; thickness tapers with u.
    """
    x1, y1 = T1
    x2, y2 = T2
    mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux                      # perpendicular = bulge side
    a = L / 2.0
    R = (h * h + a * a) / (2.0 * h)       # circle through tips with sagitta h
    ox, oy = mx + px * (h - R), my + py * (h - R)
    ax, ay = mx + px * h, my + py * h     # apex point on the arc
    ang_apex = math.atan2(ay - oy, ax - ox)
    ang_t1 = math.atan2(y1 - oy, x1 - ox)
    half = abs((ang_t1 - ang_apex + math.pi) % (2 * math.pi) - math.pi)
    res = {}
    pad = thick / 2.0 + 2
    xa = int(min(x1, x2, ax) - pad); xb = int(max(x1, x2, ax) + pad) + 1
    ya = int(min(y1, y2, ay) - pad); yb = int(max(y1, y2, ay) + pad) + 1
    for y in range(ya, yb + 1):
        for x in range(xa, xb + 1):
            th = math.atan2(y - oy, x - ox)
            d = abs((th - ang_apex + math.pi) % (2 * math.pi) - math.pi)
            if d > half:
                continue
            u = 1.0 - d / half
            t = thick * (u ** 0.7)
            if t < 1.0:
                t = 1.0
            dist = math.hypot(x - ox, y - oy)
            if abs(dist - R) <= t / 2.0:
                res[(x, y)] = (u, dist, t)
    return res, (ox, oy, R, ax, ay)


def paint_arc(T1, T2, h, thick, rim=False):
    res, geom = arc_pixels(T1, T2, h, thick)
    R = geom[2]
    for (x, y), (u, dist, t) in res.items():
        c.set(x, y, WHITE)
    if rim:  # subtle cool rim on the outer edge for depth
        for (x, y), (u, dist, t) in res.items():
            if u > 0.15 and dist >= R + t / 2.0 - 1.0:
                c.set(x, y, COOL)
    return geom


# Frame 1 (top half): small white arc slash
paint_arc((18, 16), (30, 8), 2.5, 3.0)

# Frame 2 (bottom half): larger arc slash
ox, oy, R, ax, ay = paint_arc((8, 44), (40, 28), 6.0, 5.0, rim=True)

# Trailing streak: fading segments continuing past the lower-left tip
# along the arc tangent.
tx, ty = 8 - ox, 44 - oy
tl = math.hypot(tx, ty)
tx, ty = tx / tl, ty / tl
cand = [(-ty, tx), (ty, -tx)]
away = (8 - ax, 44 - ay)                  # past the tip, away from apex
if cand[0][0] * away[0] + cand[0][1] * away[1] > 0:
    dx_, dy_ = cand[0]
else:
    dx_, dy_ = cand[1]
px_, py_ = 8 + dx_ * 0.5, 44 + dy_ * 0.5
for ln, col in [(3, ST1), (3, ST2), (1.5, ST3)]:
    nx_, ny_ = px_ + dx_ * ln, py_ + dy_ * ln
    c.line(round(px_), round(py_), round(nx_), round(ny_), col)
    px_, py_ = nx_, ny_

print(c.stats_text())
print(c.matrix_text(region=(14, 4, 36, 20)))
view(c)
finish(c)
