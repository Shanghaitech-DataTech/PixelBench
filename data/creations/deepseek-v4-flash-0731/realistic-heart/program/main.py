import math
from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="heart")

def clamp(x, a, b):
    if x < a:
        return a
    if x > b:
        return b
    return x

def norm3(x, y, z):
    l = math.sqrt(x * x + y * y + z * z)
    if l < 1e-12:
        return (0.0, 0.0, 1.0)
    return (x / l, y / l, z / l)

HEART_SHADES = [
    (36, 6, 10),
    (64, 10, 15),
    (90, 14, 20),
    (116, 18, 25),
    (141, 23, 30),
    (165, 30, 36),
    (188, 40, 43),
    (208, 54, 52),
    (225, 74, 66),
    (239, 100, 86),
    (248, 135, 112),
    (253, 178, 150),
    (255, 224, 194),
]
AORTA_SHADES = [
    (118, 44, 46),
    (144, 60, 58),
    (170, 80, 72),
    (195, 102, 88),
    (215, 128, 106),
    (232, 158, 128),
    (244, 190, 154),
    (252, 220, 185),
]
BLUE_SHADES = [
    (56, 46, 96),
    (76, 64, 120),
    (100, 86, 148),
    (128, 112, 178),
    (160, 144, 206),
    (194, 180, 228),
]
WHITE = (255, 240, 228)

def heart_f(u, v):
    return (u * u + v * v - 1.0) ** 3 - u * u * v * v * v

def tube_info(px, py, pts, radii):
    best = 1e9
    best_t = 0.0
    best_s = 0.0
    best_r = radii[0]
    n = len(pts)
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        seg2 = dx * dx + dy * dy
        if seg2 == 0:
            tt = 0.0
        else:
            tt = ((px - x0) * dx + (py - y0) * dy) / seg2
        tt = clamp(tt, 0.0, 1.0)
        qx = x0 + dx * tt
        qy = y0 + dy * tt
        d = math.hypot(px - qx, py - qy)
        if d < best:
            best = d
            best_t = (tt + i) / (n - 1)
            if seg2 > 0:
                le = math.sqrt(seg2)
                nx = -dy / le
                ny = dx / le
                best_s = (px - qx) * nx + (py - qy) * ny
            else:
                best_s = 0.0
            best_r = radii[i] + (radii[i + 1] - radii[i]) * tt
    return best, best_t, best_s, best_r

# --- soft ground shadow ------------------------------------------------
c.ellipse(32, 57, 15, 3, (24, 8, 13, 110))

# --- heart body -------------------------------------------------------
CX = 31.5
SX = 19.0
CY = 34.0
SY = 23.0

for py in range(H):
    for px in range(W):
        u = (px - CX) / SX
        v = (py - CY) / SY
        f0 = heart_f(u, v)
        # the implicit heart formula leaves a cleft at the bottom centre;
        # add a cone so rows below the formula merge into one blunt apex
        wedge = (v > 1.0) and (abs(u) < clamp(0.62 - 2.6 * (v - 1.0), 0.0, 1.0))
        if py >= 62:
            hw = max(0.0, 7.5 - 2.7 * (py - 62))
            if abs(px - 31.5) < hw:
                wedge = True
        if f0 < 0.02 or wedge:
            if f0 < 0.02:
                t = clamp(-f0 / 0.5, 0.0, 1.0)
            else:
                t = 0.0
            t = t ** 0.55
            d = 0.045
            zxp = clamp(-heart_f(u + d, v) / 0.5, 0.0, 1.0) ** 0.55
            zxm = clamp(-heart_f(u - d, v) / 0.5, 0.0, 1.0) ** 0.55
            zyp = clamp(-heart_f(u, v + d) / 0.5, 0.0, 1.0) ** 0.55
            zym = clamp(-heart_f(u, v - d) / 0.5, 0.0, 1.0) ** 0.55
            n = norm3(-(zxp - zxm) / (2 * d), -(zyp - zym) / (2 * d), 1.0)
            L = norm3(-0.5, -0.62, 0.66)
            diff = max(0.0, n[0] * L[0] + n[1] * L[1] + n[2] * L[2])
            mo = math.sin(px * 0.9 + py * 1.3) * math.sin(py * 0.7 - px * 0.4)
            spec = 0.5 * max(0.0, n[2]) ** 24 * (0.45 + 0.55 * mo)
            bright = 0.42 + 0.60 * diff + spec
            # lower heart naturally darker
            if v > 0.45:
                bright -= 0.10 * clamp((v - 0.45) / 0.55, 0.0, 1.0)
            # dark rim near silhouette (subsurface falloff)
            if t < 0.10:
                bright -= 0.38 * (0.10 - t) / 0.10
            bright = clamp(bright, 0.0, 1.0)
            idx = int(round(bright * (len(HEART_SHADES) - 1)))
            c.set(px, py, HEART_SHADES[idx])

# --- great vessels -----------------------------------------------------
AORTA_PTS = [
    (31.5, 29, 3.1), (31.5, 24, 2.9), (34, 19, 2.6), (38, 16, 2.4),
    (40, 14, 2.4), (43, 16, 2.2), (45, 19, 1.9), (45, 23, 1.6), (43, 28, 1.3),
]
AORTA_R = [p[2] for p in AORTA_PTS]
AORTA_P = [(p[0], p[1]) for p in AORTA_PTS]
BLUE_PTS = [
    (31.5, 28, 2.4), (30, 22, 2.2), (26, 18, 1.9), (22, 16, 1.6), (19, 17, 1.2),
]
BLUE_R = [p[2] for p in BLUE_PTS]
BLUE_P = [(p[0], p[1]) for p in BLUE_PTS]

for py in range(H):
    for px in range(W):
        da, ta, sa, ra = tube_info(px, py, AORTA_P, AORTA_R)
        db, tb, sb, rb = tube_info(px, py, BLUE_P, BLUE_R)
        if da <= ra and da <= db:
            topg = clamp((30 - py) / 17.0, 0.0, 1.0)
            side = clamp(0.5 - (sa / ra) * 0.5, 0.0, 1.0)
            mo = math.sin(px * 1.1 + py * 0.6) * math.sin(py * 1.2 - px * 0.3)
            bright = 0.28 + 0.30 * topg + 0.26 * side + 0.07 * (1.0 - abs(sa) / ra) + 0.06 * mo
            # distal part of the arch gets a cooler reddish cast
            bright = clamp(bright, 0.0, 1.0)
            idx = int(round(bright * (len(AORTA_SHADES) - 1)))
            c.set(px, py, AORTA_SHADES[idx])
        elif db <= rb:
            topg = clamp((28 - py) / 16.0, 0.0, 1.0)
            side = clamp(0.5 - (sb / rb) * 0.5, 0.0, 1.0)
            mo = math.sin(px * 0.8 + py * 1.4) * math.sin(py * 0.5 - px * 0.9)
            bright = clamp(0.28 + 0.32 * topg + 0.24 * side + 0.06 * mo, 0.0, 1.0)
            idx = int(round(bright * (len(BLUE_SHADES) - 1)))
            c.set(px, py, BLUE_SHADES[idx])

# --- sparkles / sheen -------------------------------------------------
c.set(26, 25, WHITE)
c.set(23, 31, (249, 160, 132))
c.set(40, 12, AORTA_SHADES[6])

# --- coronary surface details (dark vessels on the wall) ---------------
c.line(30, 27, 26, 33, (70, 12, 18))
c.line(26, 33, 29, 41, (70, 12, 18))
c.line(32, 27, 42, 34, (88, 16, 22))
c.line(42, 34, 37, 43, (88, 16, 22))
c.set(45, 30, (110, 20, 26))
c.set(24, 36, (110, 20, 26))

st = c.stats()
print(st)
print(c.stats_text())

finish(c)
