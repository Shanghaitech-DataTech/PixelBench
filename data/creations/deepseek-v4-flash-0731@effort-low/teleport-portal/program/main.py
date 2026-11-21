import math
from pixelbench_api import new_canvas, finish

W = H = 48
c = new_canvas(W, H)  # transparent background

cx = cy = 24.0

# Halo glow rings (semi-transparent light purple), radius 16..20
halo_colors = [
    (170, 110, 255, 40),
    (180, 125, 255, 55),
    (195, 145, 255, 75),
    (210, 165, 255, 95),
]
for rad, col in zip([20, 19, 18, 17], halo_colors):
    c.circle(cx, cy, rad, col, fill=False)  # outline ring -> glow band
# outer bright thin ring
c.circle(cx, cy, 16, (220, 185, 255, 160), fill=False)

# Vortex spiral bands, radius 4..15
vortex_palette = [
    (20, 0, 45),     # deep
    (95, 25, 175),   # dark purple
    (160, 85, 235),  # mid purple
    (215, 150, 255), # bright
]

N = 40          # number of arms around
pitch = 5.0     # spiral pitch in px per full turn
r_in = 3.5
r_out = 15.5

for y in range(H):
    for x in range(W):
        dx = x - cx
        dy = y - cy
        rd = math.hypot(dx, dy)
        if rd < r_in or rd > r_out:
            continue
        ang = math.atan2(dy, dx)
        # wrapped angle 0..2pi
        if ang < 0:
            ang += 2 * math.pi
        b = int((ang / (2 * math.pi)) * N - rd / pitch)
        col = vortex_palette[b % len(vortex_palette)]
        # edge darkening at outer rim, quantized to few levels
        if rd > 13.0:
            f = (rd - 13.0) / (r_out - 13.0)
            f = round(f * 3) / 3.0  # 4 levels
            col = tuple(int(channel * (1.0 - 0.45 * f)) for channel in col)
        c.set(x, y, col)

# Core glow
for r, col in [(5, (150, 90, 240)), (3.6, (230, 190, 255)), (2.2, (255, 245, 255))]:
    c.circle(cx, cy, r, col, fill=True)

# bright sweeping arms through the core for rotating energy feel
for k in range(6):
    a0 = (k / 6.0) * 2 * math.pi - 0.5
    pts = []
    for s in range(30):
        t = s / 29.0
        rp = 3.0 + t * 4.0
        a = a0 + t * 1.2
        pts.append((cx + rp * math.cos(a), cy + rp * math.sin(a)))
    c.poly(pts, (255, 220, 255), fill=False)

# Energy spark particles near the rim
sparks = [
    (6, 14), (9, 8), (14, 5), (25, 4), (33, 7), (40, 12), (43, 24),
    (40, 34), (34, 42), (25, 44), (15, 42), (8, 35), (5, 27), (20, 7),
    (42, 18), (30, 43), (10, 20), (36, 13), (13, 31), (31, 9),
]
for (px, py) in sparks:
    if math.hypot(px - cx, py - cy) > 17:
        c.set(px, py, (230, 200, 255, 200))

print(c.stats())
finish(c)
