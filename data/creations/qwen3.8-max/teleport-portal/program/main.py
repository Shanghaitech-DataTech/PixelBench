import math

W = H = 48
c = new_canvas(W, H, name="portal")

# two animation frames side by side in one 48x48 sheet: 24x48 cells
CENTERS = [(11.5, 23.5), (35.5, 23.5)]
ROTS = [0.35, 1.45]          # frame 2 = vortex rotated
HALO_ON = [False, True]     # frame 2 carries the glowing halo

ARMS = 3
TW = 2.7                    # swirl (radians) core -> rim
R_IN = 8.8                  # inner edge of rim ring
R_OUT = 10.8                # outer edge of rim ring
R_HALO = 11.8               # glow reach (frame 2)
R_C = (R_IN + R_OUT) / 2.0
HW = (R_OUT - R_IN) / 2.0

# --- palettes -------------------------------------------------------------
INTERIOR = [
    "#150428", "#2a0845", "#41106b", "#5c1893", "#7b24bd",
    "#9c38e0", "#c063f8", "#e2aaff", "#ffffff",
]
CORE = ["#c063f8", "#d9f4ff", "#eafaff", "#ffffff"]   # hot cyan-white heart
RIM = ["#5a17a8", "#9b3df0", "#c86ffb", "#eedcff"]
HALO = ["#7c3aed66", "#9659ff99", "#b98affc4", "#e3ccfff0"]

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def thr(x, y):
    return (BAYER[y & 3][x & 3] + 0.5) / 16.0


def pick(ramp, t, x, y):
    """Ordered-dither a 0..1 value into an index of ramp."""
    n = len(ramp)
    t = 0.0 if t < 0.0 else (1.0 if t > 1.0 else t)
    f = t * (n - 1)
    i0 = int(math.floor(f))
    i = i0 if (f - i0) < thr(x, y) else i0 + 1
    if i < 0:
        i = 0
    if i > n - 1:
        i = n - 1
    return ramp[i]


def pick_halo(t, x, y):
    n = len(HALO)
    if t <= 0.0:
        return None
    f = t * n - 0.5
    i0 = int(math.floor(f))
    i = i0 if (f - i0) < thr(x, y) else i0 + 1
    if i < 0:
        return None
    if i > n - 1:
        i = n - 1
    return HALO[i]


def pick_solid(ramp, t):
    n = len(ramp)
    t = 0.0 if t < 0.0 else (1.0 if t > 1.0 else t)
    i = int(t * (n - 1) + 0.5)
    return ramp[min(i, n - 1)]


def swirl(r):
    return TW * (min(r, R_IN) / R_IN) ** 1.15


def paint(cx, cy, rot, halo):
    r_max = R_HALO if halo else R_OUT
    for y in range(H):
        for x in range(W):
            dx = x - cx
            dy = y - cy
            r = math.hypot(dx, dy)
            if r > r_max:
                continue
            a = math.atan2(dy, dx)
            arm = (0.5 + 0.5 * math.cos(ARMS * (a + rot - swirl(r)))) ** 1.5

            if r <= R_IN:
                rad = 1.0 - r / (R_IN + 1.0)
                t = (rad ** 0.80) * (0.22 + 0.78 * arm) + 0.06 * arm + 0.04
                col = pick(INTERIOR, t, x, y)
                if r < 2.9:
                    k = (1.0 - r / 2.9) ** 1.4
                    col = pick(CORE, k * 1.05, x, y) if k > 0.12 else col
                c.set(x, y, col)

            elif r <= R_OUT:
                q = 1.0 - abs(r - R_C) / HW
                q = q if q > 0.0 else 0.0
                m = 0.82 + 0.18 * arm
                t = (q ** 0.60) * m
                c.set(x, y, pick_solid(RIM, t))

            else:
                q = 1.0 - (r - R_OUT) / (R_HALO - R_OUT)
                w = 0.80 + 0.20 * arm
                col = pick_halo(q * w, x, y)
                if col is not None:
                    c.set(x, y, col)

    if halo:  # a few bright motes flung out of the spinning ring
        for k in range(4):
            ang = rot + k * (math.pi / 2) + 0.4
            rad = 11.2
            mx = int(round(cx + rad * math.cos(ang)))
            my = int(round(cy + rad * math.sin(ang)))
            if 0 <= mx < W and 0 <= my < H:
                c.set(mx, my, "#ffffff")


for (cx, cy), rot, halo in zip(CENTERS, ROTS, HALO_ON):
    paint(cx, cy, rot, halo)

print(c.stats_text())
view(c, scale=10, margin=1)
save("portal", c)
finish(c)
