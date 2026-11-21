import math
from pixelbench_api import *

W = H = 48
c = new_canvas(W, H, name="slash")
white = c.color((255, 255, 255), name="white")


def quad_pts(p0, ctrl, p1, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        pts.append((u * u * p0[0] + 2 * u * t * ctrl[0] + t * t * p1[0],
                    u * u * p0[1] + 2 * u * t * ctrl[1] + t * t * p1[1]))
    return pts


def band(pts, half, taper=True):
    n = len(pts)
    ring = []
    for i, p in enumerate(pts):
        j0 = max(0, i - 1)
        j1 = min(n - 1, i + 1)
        tx = pts[j1][0] - pts[j0][0]
        ty = pts[j1][1] - pts[j0][1]
        L = math.hypot(tx, ty) or 1.0
        f = 0.15 + 0.85 * math.sin(math.pi * i / (n - 1)) if taper else 1.0
        ring.append((p[0] - ty / L * half * f, p[1] + tx / L * half * f))
    for i in range(n - 1, -1, -1):
        p = pts[i]
        j0 = max(0, i - 1)
        j1 = min(n - 1, i + 1)
        tx = pts[j1][0] - pts[j0][0]
        ty = pts[j1][1] - pts[j0][1]
        L = math.hypot(tx, ty) or 1.0
        f = 0.15 + 0.85 * math.sin(math.pi * i / (n - 1)) if taper else 1.0
        ring.append((p[0] + ty / L * half * f, p[1] - tx / L * half * f))
    c.poly(ring, white)


# --- Frame 2: large arc slash: thick tapered crescent, bottom-left -> top-right ---
band(quad_pts((6, 37), (1, 19), (42, 8)), 4.6)

# Trailing streak: thin tail continuing beyond the lower-left end + fading dashes
band([(9, 39), (12, 45), (2, 47)], 0.9, taper=False)
c.line(6, 41, 1, 44, white)
c.line(3, 38, 0, 40, white)

# --- Frame 1: small arc slash nested inside the big arc's hollow ---
band(quad_pts((29, 42), (17, 30), (38, 21)), 1.5)

print(c.stats_text())
finish(c)
