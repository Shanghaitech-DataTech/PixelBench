from pixelbench_api import *
import math

W = H = 48
c = new_canvas(W, H, name="slash")
WHITE = c.color((255, 255, 255))


def quad_bezier(p0, p1, p2, t):
    mt = 1.0 - t
    x = mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0]
    y = mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]
    return (x, y)


def slash(p0, p1, p2, r0, r1, tmin, tmax, steps, colour):
    for i in range(steps + 1):
        t = tmin + (tmax - tmin) * (i / steps)
        x, y = quad_bezier(p0, p1, p2, t)
        r = r0 + (r1 - r0) * ((t - tmin) / (tmax - tmin)) if tmax != tmin else r0
        c.circle(round(x), round(y), max(0, round(r)), colour)


# ---- Frame 1 (left half): small white arc slash ----
slash((5, 42), (4, 20), (19, 7), 1.4, 1.6, 0.0, 1.0, 40, WHITE)

# ---- Frame 2 (right half): larger arc slash with trailing streak ----
slash((25, 39), (21, 13), (44, 5), 1.9, 2.2, 0.0, 1.0, 52, WHITE)
# trailing streak: thin continuation past the bottom tip (t < 0), tapering off
slash((24, 38), (22, 12), (45, 4), 1.5, 0.3, -0.12, 0.0, 14, WHITE)

print(c.stats_text())
finish(c)
