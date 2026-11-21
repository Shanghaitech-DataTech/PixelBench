import math
import house3d as H
from house3d import (DARK, WOODD, WOOD, WOODL, SH, SHM, SHD, GLOW, GLOW2,
                     PL, PLM, PLD, SHADOW, W, D, HW, WR, ZE, ZR, YN, YF, arch)

ANGLES = [45.0, 90.0]
AR_FB = W / HW           # arch aspect helper, front/back walls
AR_LR = D / HW           # ... side walls


# ---------- one shared camera frame for both turns ----------
def frame():
    KEY = [(0, YN, ZR), (0, YF, ZR)]
    for sx in (-1, 1):
        KEY += [(sx * WR, YN, ZE), (sx * WR, YF, ZE),
                (sx * W / 2, -D / 2, 0), (sx * W / 2, D / 2, 0)]
    for i in range(24):
        a = 2 * math.pi * i / 24
        KEY.append(((WR + 4) * math.cos(a), (D / 2 + 14) * math.sin(a), 0))
    xs, ys = [], []
    for th in ANGLES:
        t = math.radians(th)
        for p in KEY:
            x, y = H.raw(p, t)
            xs.append(x)
            ys.append(y)
    m = 6
    return (int(math.ceil(max(xs) - min(xs))) + 2 * m,
            int(math.ceil(max(ys) - min(ys))) + 2 * m,
            -min(xs) + m, -min(ys) + m)


CW, CH, CX, CY = frame()

SHINGLE_LIT = [SH, WOODL, SHM, SH, '#d3a04a', WOODL, SHM]
SHINGLE_DIM = [SHD, WOODD, '#7e5c3a', SHD, WOODD, '#8a6540', WOODD]


def shingles(r, side, lit):
    """Courses run parallel to the eave (v axis = ridge->eave)."""
    q = H.roof_quad(side)
    tones = SHINGLE_LIT if lit else SHINGLE_DIM
    r.patch(q, 0, 0, 1, 1, tones[0])
    NC, NU = 7, 11                     # courses down the slope, tiles across
    for i in range(NC):
        v0, v1 = i / NC, (i + 1) / NC
        off = (0.5 / NU) if i % 2 else 0.0
        for j in range(-1, NU + 1):
            u0 = max(0.0, j / NU + off)
            u1 = min(1.0, (j + 1) / NU + off)
            if u1 - u0 < 1e-6:
                continue
            r.patch(q, u0, v0, u1, v1, tones[(i * 3 + j) % len(tones)])
            if 0.0 < u0 < 1.0:
                r.seg(H.bil(q, u0, v0 + 0.012), H.bil(q, u0, v1 - 0.012), DARK)
        if i:
            r.seg(H.bil(q, 0, v0), H.bil(q, 1, v0), DARK)
    r.patch(q, 0, 0.955, 1, 1.0, DARK)          # eave shadow line


def roof_trim(r, th):
    # ridge cap
    r.face([(0, YF, ZR + 2), (0, YN, ZR + 2), (2.5, YN, ZR - 1), (2.5, YF, ZR - 1)], WOODL)
    r.face([(0, YF, ZR + 2), (0, YN, ZR + 2), (-2.5, YN, ZR - 1), (-2.5, YF, ZR - 1)], WOOD)
    r.seg((0, YN, ZR + 2), (0, YF, ZR + 2), WOODL)
    # eave fascia on whichever long side faces us
    for sx in (-1, 1):
        if H.visible((sx, 0, 0), th):
            r.face([(sx * WR, YN, ZE), (sx * WR, YF, ZE),
                    (sx * WR, YF, ZE - 5), (sx * WR, YN, ZE - 5)],
                   WOODL if H.bright((sx, 0, 0), th) > 0 else WOODD)
    # barge boards following the rake of whichever gable faces us
    for kind in ('front', 'back'):
        n = H.WALL_N[kind]
        if H.visible(n, th):
            y = -D / 2 if kind == 'front' else D / 2
            r.face(H.gable_band(kind), WOOD if H.bright(n, th) > 0 else WOODD)
            r.seg((-WR, y, ZE), (0, y, ZR + 3), WOODL)
            r.seg((0, y, ZR + 3), (WR, y, ZE), WOODL)


def front_wall(r, th, kind):
    q = H.wall_quad(kind)
    b = H.bright(H.WALL_N[kind], th)
    base = PL if b > 0.25 else (PLM if b > -0.1 else PLD)
    r.face(H.wall_silhouette(kind), base)
    r.patch(q, 0.0, 0.0, 1.0, 0.055, WOODL)         # top plate
    r.patch(q, 0.0, 0.0, 0.10, 1.0, WOOD)           # corner posts
    r.patch(q, 0.90, 0.0, 1.0, 1.0, WOOD)
    r.patch(q, 0.10, 0.0, 0.13, 1.0, WOODD)
    r.patch(q, 0.87, 0.0, 0.90, 1.0, WOODD)
    r.patch(q, 0.0, 0.945, 1.0, 1.0, WOOD)          # sill beam
    r.seg(H.bil(q, 0.0, 0.945), H.bil(q, 1.0, 0.945), DARK)
    # arched doorway
    r.uvpoly(q, arch(0.5, 0.27, 0.20, 1.0, AR_FB), GLOW2)
    r.uvpoly(q, arch(0.5, 0.235, 0.25, 1.0, AR_FB), base)
    r.uvpoly(q, arch(0.5, 0.205, 0.29, 1.0, AR_FB), WOOD)
    r.uvpoly(q, arch(0.5, 0.175, 0.33, 1.0, AR_FB), DARK)
    r.uvpoly(q, arch(0.5, 0.15, 0.36, 0.95, AR_FB), SH)
    for v in (0.49, 0.59, 0.69, 0.79, 0.89):
        r.seg(H.bil(q, 0.355, v), H.bil(q, 0.645, v), SHD)
    r.seg(H.bil(q, 0.5, 0.365), H.bil(q, 0.5, 0.945), SHD)
    r.uvpoly(q, arch(0.5, 0.15, 0.36, 0.42, AR_FB), WOODD)   # lintel band
    hx, hy = r.P(H.bil(q, 0.60, 0.70))                       # handle
    r.c.set(hx, hy, DARK)
    r.uvpoly(q, arch(0.5, 0.15, 0.36, 0.95, AR_FB), DARK, fill=False)


def side_wall(r, th, kind):
    q = H.wall_quad(kind)
    b = H.bright(H.WALL_N[kind], th)
    base = PL if b > 0.25 else (PLM if b > -0.1 else PLD)
    r.face(H.wall_silhouette(kind), base)
    r.patch(q, 0.0, 0.0, 1.0, 0.055, WOODL)
    r.patch(q, 0.0, 0.0, 0.085, 1.0, WOOD)
    r.patch(q, 0.915, 0.0, 1.0, 1.0, WOOD)
    r.patch(q, 0.085, 0.0, 0.11, 1.0, WOODD)
    r.patch(q, 0.89, 0.0, 0.915, 1.0, WOODD)
    r.patch(q, 0.0, 0.945, 1.0, 1.0, WOOD)
    r.seg(H.bil(q, 0.0, 0.945), H.bil(q, 1.0, 0.945), DARK)
    r.seg(H.bil(q, 0.13, 0.93), H.bil(q, 0.29, 0.52), WOOD)   # braces
    r.seg(H.bil(q, 0.87, 0.93), H.bil(q, 0.71, 0.52), WOOD)
    # arched window
    r.uvpoly(q, arch(0.5, 0.235, 0.22, 0.70, AR_LR), WOOD)
    r.uvpoly(q, arch(0.5, 0.205, 0.26, 0.665, AR_LR), DARK)
    r.uvpoly(q, arch(0.5, 0.17, 0.30, 0.63, AR_LR), GLOW)
    r.uvpoly(q, arch(0.5, 0.17, 0.30, 0.43, AR_LR), GLOW2)
    r.seg(H.bil(q, 0.5, 0.30), H.bil(q, 0.5, 0.625), DARK)
    r.seg(H.bil(q, 0.335, 0.46), H.bil(q, 0.665, 0.46), DARK)
    r.patch(q, 0.28, 0.655, 0.72, 0.705, WOODD)               # sill
    r.seg(H.bil(q, 0.27, 0.705), H.bil(q, 0.73, 0.705), DARK)


def build(th_deg, name):
    th = math.radians(th_deg)
    ground = new_canvas(CW, CH, name=name + '_g')
    house = new_canvas(CW, CH, name=name + '_h')
    rg = H.Render(ground, th, CX, CY)
    r = H.Render(house, th, CX, CY)

    pts = []
    for i in range(28):
        a = 2 * math.pi * i / 28
        pts.append(((WR - 1) * math.cos(a) + 4, (D / 2 + 10) * math.sin(a) + 5, 0))
    rg.face(pts, SHADOW)

    walls = []
    for kind in ('front', 'back', 'left', 'right'):
        n = H.WALL_N[kind]
        if H.visible(n, th):
            q = H.wall_quad(kind)
            walls.append((sum(H.depth(p, th) for p in q) / 4, kind))
    for _, kind in sorted(walls, reverse=True):
        (front_wall if kind in ('front', 'back') else side_wall)(r, th, kind)

    planes = [(H.bright(H.roof_n(s), th), s) for s in ('left', 'right')
              if H.visible(H.roof_n(s), th)]
    for b, side in sorted(planes):
        shingles(r, side, b >= max(p[0] for p in planes) - 1e-9)
    roof_trim(r, th)

    house.outline(DARK)
    return flatten([ground, house], name=name)


f1 = build(ANGLES[0], 'frame45')
f2 = build(ANGLES[1], 'frame90')
print('canvas', CW, CH)
view(f1)
view(f2)
finish([f1, f2])
