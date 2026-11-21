import math

W = H = 48

c = new_canvas(W, H, name="staff")

WOOD_D = '#2a1710'   # outline
WOOD_S = '#40281a'   # shadow side
WOOD_M = '#5c3a22'   # body
WOOD_L = '#8d5c34'   # lit
WOOD_H = '#c1935f'   # highlight

MAGIC_D = '#3d1566'
MAGIC_M = '#7a3fc0'
MAGIC_L = '#a868ec'
MAGIC_XL = '#d9b8ff'
WHITE = '#f4ebff'

GLOW_1 = '#5c2596'
GLOW_2 = '#3a1363'


# ---------------------------------------------------------------- helpers
def sample_path(pts, samples=26):
    """Catmull-Rom through pts, returned as a dense polyline."""
    P = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for s in range(samples):
            t = s / samples
            t2 = t * t
            t3 = t2 * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t
                       + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                       + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t
                       + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                       + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    out.append(P[-2])
    return out


def segments(line):
    segs = []
    for (x0, y0), (x1, y1) in zip(line, line[1:]):
        dx, dy = x1 - x0, y1 - y0
        l2 = dx * dx + dy * dy
        if l2 < 1e-9:
            continue
        segs.append((x0, y0, dx, dy, l2))
    return segs


def path_len(line):
    return sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(line, line[1:]))


def tube(g, line, radius_fn):
    """Round wooden tube from a distance field, lit from the upper-left."""
    segs = []
    total = path_len(line) or 1.0
    acc = 0.0
    for (x0, y0), (x1, y1) in zip(line, line[1:]):
        dx, dy = x1 - x0, y1 - y0
        l2 = dx * dx + dy * dy
        if l2 < 1e-9:
            continue
        s0 = acc / total
        acc += math.sqrt(l2)
        segs.append((x0, y0, dx, dy, l2, s0, acc / total))
    xs = [p[0] for p in line]
    ys = [p[1] for p in line]
    rmax = 3.2
    x0 = max(0, int(min(xs) - rmax - 2))
    x1 = min(W - 1, int(max(xs) + rmax + 2))
    y0 = max(0, int(min(ys) - rmax - 2))
    y1 = min(H - 1, int(max(ys) + rmax + 2))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            best = 1e9
            bpx = bpy = 0.0
            bs = 0.0
            for (sx, sy, dx, dy, l2, s0, s1) in segs:
                t = ((x - sx) * dx + (y - sy) * dy) / l2
                if t < 0.0:
                    t = 0.0
                elif t > 1.0:
                    t = 1.0
                px = x - (sx + dx * t)
                py = y - (sy + dy * t)
                d2 = px * px + py * py
                if d2 < best:
                    best = d2
                    bpx, bpy = px, py
                    bs = s0 + (s1 - s0) * t
            d = math.sqrt(best)
            radius = radius_fn(bs)
            if d > radius:
                continue
            edge = min(0.95, radius * 0.42)
            if d > radius - edge:
                col = WOOD_D
            else:
                q = -(bpx + bpy) * 0.7071
                if q > 0.95:
                    col = WOOD_H
                elif q > 0.20:
                    col = WOOD_L
                elif q > -0.55:
                    col = WOOD_M
                else:
                    col = WOOD_S
            g.set(x, y, col)


def is_empty(x, y):
    if not (0 <= x < W and 0 <= y < H):
        return False
    pal = {e['index']: e['rgba'] for e in c.palette()}
    rgba = pal.get(c.get(x, y))
    return rgba is None or rgba[3] == 0


def band(g, line, i, col, half=2, thick=1):
    x, y = line[i]
    j = min(i + 1, len(line) - 1)
    k = max(i - 1, 0)
    dx = line[j][0] - line[k][0]
    dy = line[j][1] - line[k][1]
    m = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / m, dx / m
    for s in range(-half, half + 1):
        for t in range(thick):
            g.set(int(round(x + nx * s + dx / m * t)),
                  int(round(y + ny * s + dy / m * t)), col)


# ---------------------------------------------------------------- geometry
shaft = sample_path([(15.0, 49.5), (17.5, 38.0), (21.0, 29.0), (25.0, 21.5)])
head = sample_path([
    (25.0, 21.5), (31.0, 16.5), (33.8, 10.5),
    (30.2, 4.6), (22.6, 3.2), (15.4, 5.0),
    (12.8, 11.0), (14.5, 16.0),
])
staff = shaft + head

shaft_len = path_len(shaft)
frac = shaft_len / (shaft_len + path_len(head))


def lerp_profile(u, prof):
    if u <= prof[0][0]:
        return prof[0][1]
    for (a, ra), (b, rb) in zip(prof, prof[1:]):
        if u <= b:
            return ra + (rb - ra) * (u - a) / (b - a)
    return prof[-1][1]


SHAFT_PROF = [(0.0, 3.15), (0.6, 2.95), (1.0, 2.60)]
HEAD_PROF = [(0.0, 2.62), (0.40, 2.50), (0.80, 2.20), (1.0, 1.55)]


def radius_fn(s):
    if s <= frac:
        return lerp_profile(s / frac, SHAFT_PROF)
    return lerp_profile((s - frac) / (1 - frac), HEAD_PROF)


tube(c, staff, radius_fn)

for i in (16, 23):
    if i < len(shaft):
        band(c, shaft, i, WOOD_D, half=2)

# ---------------------------------------------------------------- orb
ox, oy = 23.0, 11.0

# dithered aura on empty pixels only
for y in range(0, 26):
    for x in range(6, 42):
        d = math.hypot(x - ox, y - oy)
        if d < 4.8 or not is_empty(x, y):
            continue
        if d < 6.2 and (x + y) % 2 == 0:
            c.set(x, y, GLOW_1)
        elif d < 7.4 and (x + y) % 4 == 0:
            c.set(x, y, GLOW_2)

# shaded sphere
MAGIC_XD = '#2a0f4a'
for y in range(int(oy) - 5, int(oy) + 6):
    for x in range(int(ox) - 5, int(ox) + 6):
        px, py = x - ox, y - oy
        d = math.hypot(px, py)
        if d > 4.05:
            continue
        q = -(px + py) / (d * 1.4142) if d > 0.2 else 0.0
        v = 0.55 * q - 0.45 * (d / 4.0) + 0.45
        if d > 3.3:
            col = MAGIC_D
        elif v > 0.63:
            col = MAGIC_XL
        elif v > 0.38:
            col = MAGIC_L
        elif v > -0.02:
            col = MAGIC_M
        elif v > -0.30:
            col = MAGIC_D
        else:
            col = MAGIC_XD
        c.set(x, y, col)

c.set(int(ox) - 2, int(oy) - 2, WHITE)
c.set(int(ox) - 1, int(oy) - 2, MAGIC_XL)

# ---------------------------------------------------------------- particles
def spark(x, y, col=MAGIC_L):
    if is_empty(x, y):
        c.set(x, y, WHITE)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if is_empty(x + dx, y + dy):
                c.set(x + dx, y + dy, col)


def dot(x, y, col):
    if is_empty(x, y):
        c.set(x, y, col)


# upper right of the head
spark(38, 5, MAGIC_L)
dot(42, 9, MAGIC_M)
dot(44, 14, MAGIC_L)
dot(36, 12, MAGIC_XL)
dot(40, 20, GLOW_1)
# upper left
spark(6, 6, MAGIC_XL)
dot(2, 10, MAGIC_M)
dot(9, 2, MAGIC_M)
dot(4, 14, GLOW_1)
# sides
spark(3, 21, MAGIC_M)
dot(8, 25, MAGIC_L)
dot(37, 27, MAGIC_XL)
spark(41, 33, MAGIC_M)
dot(34, 30, GLOW_1)
# trail beside the shaft
dot(24, 30, MAGIC_M)
dot(26, 35, MAGIC_L)
dot(22, 41, MAGIC_M)
dot(20, 45, GLOW_1)
# lower corners
spark(10, 41, MAGIC_M)
dot(6, 36, MAGIC_M)
dot(31, 42, MAGIC_M)
dot(28, 38, GLOW_1)
dot(45, 26, MAGIC_M)

print(c.stats_text())
save("magic_staff", c)
finish(c)
