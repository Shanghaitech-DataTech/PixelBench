from pixelbench_api import *
import math
import random

W = H = 48
c = new_canvas(W, H)
cx = cy = W // 2

# ---- palette ----
dark_violet   = c.color((22, 6, 36))
deep_purple   = c.color((46, 14, 66))
mid_purple    = c.color((99, 48, 148))
bright_purple = c.color((150, 76, 218))
lavender      = c.color((207, 140, 255))
pale          = c.color((243, 219, 255))
white         = c.color((255, 252, 255))
halo_faint    = c.color((198, 140, 255, 110))
halo_bright   = c.color((226, 176, 255, 200))

# ---- glowing halo (outer rings) ----
c.circle(cx, cy, 23, halo_faint, fill=False)
c.circle(cx, cy, 22, halo_bright, fill=False)

# ---- portal rim ----
c.circle(cx, cy, 21, lavender, fill=False)
c.circle(cx, cy, 20, bright_purple, fill=False)

# ---- inner dark opening ----
c.circle(cx, cy, 19, deep_purple)
c.circle(cx, cy, 15, dark_violet)

# ---- spiral energy vortex ----
arms = 3
turns = 2.2
r0, r1 = 2.0, 17.0
steps = 300
max_t = turns * 2 * math.pi


def arm_points(offset):
    pts = []
    for i in range(steps + 1):
        t = max_t * i / steps
        r = r0 + (r1 - r0) * (t / max_t)
        a = t + offset
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def arm_colour(r):
    if r < 4.0:
        return pale
    if r < 8.0:
        return lavender
    if r < 13.0:
        return bright_purple
    return mid_purple


for arm in range(arms):
    pts = arm_points(arm * 2 * math.pi / arms)
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        r = math.hypot((x0 + x1) / 2 - cx, (y0 + y1) / 2 - cy)
        c.line(round(x0), round(y0), round(x1), round(y1), arm_colour(r))
    # thicken the swirl near the hub
    for p in pts:
        r = math.hypot(p[0] - cx, p[1] - cy)
        if r < 9.0:
            c.circle(round(p[0]), round(p[1]), 1, arm_colour(r))

# ---- bright core ----
c.circle(cx, cy, 4, lavender)
c.circle(cx, cy, 2, pale)
c.set(cx, cy, white)

# ---- sparkles on the halo ----
random.seed(7)
for k in range(14):
    ang = random.uniform(0, 2 * math.pi)
    rr = random.uniform(21.5, 23.0)
    x = round(cx + rr * math.cos(ang))
    y = round(cy + rr * math.sin(ang))
    c.set(x, y, white if k % 3 == 0 else pale)

print(c.stats_text())
finish(c)
