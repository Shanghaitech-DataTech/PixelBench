import math

W = H = 64

# ---------------------------------------------------------------- helpers
def hx(h):
    h = h.lstrip('#')
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def to_hex(rgb):
    return '#%02x%02x%02x' % tuple(max(0, min(255, int(round(v)))) for v in rgb)

def clamp(v, a=0.0, b=1.0):
    return max(a, min(b, v))

def lerp(a, b, t):
    return a + (b - a) * t

def smoothstep(e0, e1, x):
    t = clamp((x - e0) / (e1 - e0))
    return t * t * (3 - 2 * t)

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

def ramp_pick(v, ramp, x, y):
    f = clamp(v) * (len(ramp) - 1)
    i = int(math.floor(f))
    frac = f - i
    thr = (BAYER[y & 3][x & 3] + 0.5) / 16.0
    if frac > thr and i + 1 < len(ramp):
        i += 1
    return ramp[max(0, min(len(ramp) - 1, i))]

# ---------------------------------------------------------------- palette
OUTLINE  = '#07040d'
LASH     = '#0c0618'
BODY     = ['#0d0716', '#170e26', '#22143a', '#301c50', '#42286b',
            '#573789', '#6f4aa8', '#8b62c8', '#ab86e6']
SCLERA   = ['#2b2340', '#453b60', '#625884', '#847aa6', '#a79dc6',
            '#c9c2e0', '#e6e1f4', '#f7f4ff']
IRIS     = ['#100320', '#22083f', '#360e66', '#4c1790', '#6524b8',
            '#8138d8', '#9d55ee', '#b878fb']
GLOW     = ['#0a0514', '#241040', '#45207c', '#6c39b4', '#9663e2',
            '#c39cf6', '#efe6ff']
VEIN     = '#6e2f4a'
SPEC     = '#ffffff'
SPEC2    = '#cdc4ee'
SHC      = (12, 5, 20)

# ---------------------------------------------------------------- geometry
CX, CY = 32.0, 24.0
RX, RYT, RYB = 21.0, 18.5, 16.0
ECX, ECY, ER = 32.0, 25.0, 14.0
ICX, ICY, IR = 32.0, 25.4, 9.6
PCX, PCY, PR = 32.0, 25.4, 5.0

LX, LY, LZ = -0.55, -0.72, 0.42          # light direction (towards light)

def lid_y(px):
    return ECY - 10.6 + 0.048 * (px - ECX) ** 2

def low_y(px):
    return ECY + 11.4 - 0.034 * (px - ECX) ** 2

# ---------------------------------------------------------------- tentacles
def catmull(pts, n=18):
    p = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for j in range(n):
            t = j / float(n)
            t2 = t * t
            t3 = t2 * t
            x = 0.5 * (2*p1[0] + (-p0[0]+p2[0])*t + (2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2
                       + (-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
            y = 0.5 * (2*p1[1] + (-p0[1]+p2[1])*t + (2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2
                       + (-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
            out.append((x, y))
    out.append(tuple(pts[-1]))
    return out

TENTS = [
    ([(16, 33), (12.5, 38), (11.5, 43), (13.5, 47.5)], 4.6, 0.95),
    ([(24, 37), (22, 42), (21.5, 47), (23.5, 51.5)],   5.0, 1.05),
    ([(31, 39), (31, 44), (30, 49), (31.5, 53.5)],     4.8, 1.05),
    ([(39, 38), (41, 43), (42, 48), (40, 52.5)],       4.8, 1.05),
    ([(47, 33), (50.5, 38), (51.5, 43), (49, 47.5)],   4.6, 0.95),
]

TSAMPLES = []
for pts, rb, rt in TENTS:
    curve = catmull(pts)
    acc = [0.0]
    for i in range(1, len(curve)):
        acc.append(acc[-1] + math.hypot(curve[i][0]-curve[i-1][0], curve[i][1]-curve[i-1][1]))
    total = acc[-1]
    TSAMPLES.append([(curve[i][0], curve[i][1],
                      lerp(rb, rt, (acc[i]/total) ** 0.85), acc[i]/total)
                     for i in range(len(curve))])

def tent_field(px, py):
    best = None
    for samples in TSAMPLES:
        for (sx, sy, sr, tp) in samples:
            d = math.hypot(px - sx, py - sy)
            m = (sr + 0.30) - d
            if m > 0 and (best is None or m > best[0]):
                best = (m, sx, sy, sr, d, tp)
    return best

# ---------------------------------------------------------------- body field
SPOTS = [(18, 12, 2.4), (45, 14, 2.0), (22, 37, 2.2), (43, 36, 1.8), (13, 25, 1.7),
         (39, 8, 1.6)]

def body_field(px, py):
    dx = (px - CX) / RX
    dy0 = (py - CY) / RYT
    s = 0.5 + 0.5 * math.tanh(dy0 * 2.2)
    ry = RYT + (RYB - RYT) * s
    dy = (py - CY) / ry
    r = math.hypot(dx, dy)
    if r < 1e-9:
        return None
    th = math.atan2(dy, dx)
    wob = 1.0 + 0.028 * math.sin(3*th + 0.6) + 0.018 * math.sin(5*th + 2.0)
    t = r / wob
    if t > 1.0:
        return None
    nz = math.sqrt(max(0.0, 1.0 - t * t))
    nx = dx / r * t
    ny = dy / r * t
    return (nx, ny, nz, t, px, py)

def flesh_value(nx, ny, nz, t, px, py):
    lam = nx*LX + ny*LY + nz*LZ
    rim = (1.0 - nz) ** 3.0 * (0.45 + 0.55 * clamp((lam + 0.5) / 1.0))
    v = 0.09 + 0.70 * max(0.0, lam) + 0.62 * rim
    # lit-side rim light hugging the silhouette
    v += 0.24 * smoothstep(0.82, 1.0, t) * clamp((lam + 0.15) / 0.8)
    v -= 0.24 * clamp(ny) ** 1.5                     # dark underside
    n = math.sin(px*0.85 + 1.3) * math.sin(py*0.95 - 0.7) * math.sin((px+py)*0.37)
    v += 0.045 * n
    de = math.hypot(px - ECX, py - ECY)
    v -= 0.18 * (1.0 - smoothstep(ER - 0.5, ER + 5.5, de))
    for (sx, sy, sr) in SPOTS:
        d = math.hypot(px - sx, py - sy)
        if d < sr:
            v -= 0.13 * (1.0 - d/sr)
    dp = math.hypot(px - PCX, py - PCY)
    if dp < 22:
        v += 0.05 * (1.0 - smoothstep(6.0, 22.0, dp))
    return clamp(v)

# ---------------------------------------------------------------- build
col = [[None]*W for _ in range(H)]
msk = [[0]*W for _ in range(H)]

# soft ground shadow
for y in range(H):
    for x in range(W):
        px, py = x + 0.5, y + 0.5
        d = math.hypot((px - 32.0)/16.5, (py - 60.0)/3.8)
        if d < 1.0:
            a = int(160 * (1.0 - d) ** 1.5)
            a = max(0, min(160, (a // 16) * 16))
            if a > 0:
                col[y][x] = (SHC[0], SHC[1], SHC[2], a)

# tentacles first (they emerge from behind the body)
for y in range(H):
    for x in range(W):
        px, py = x + 0.5, y + 0.5
        tf = tent_field(px, py)
        if tf is None:
            continue
        m, sx, sy, sr, d, tp = tf
        dd = max(d, 1e-6)
        ux, uy = (px - sx)/dd, (py - sy)/dd
        zn = math.sqrt(max(0.0, 1.0 - min(1.0, (dd/sr) ** 2)))
        lam = ux*LX + uy*LY + zn*LZ
        rim = (1.0 - zn) ** 2.5
        v = 0.05 + 0.62*max(0.0, lam) + 0.42*rim
        v *= lerp(0.98, 0.62, tp)                    # tips fall into darkness
        col[y][x] = ramp_pick(clamp(v), BODY, x, y)
        msk[y][x] = 1

# body over the tentacle roots
for y in range(H):
    for x in range(W):
        px, py = x + 0.5, y + 0.5
        bf = body_field(px, py)
        if bf is None:
            continue
        nx, ny, nz, t, _, _ = bf
        v = flesh_value(nx, ny, nz, t, px, py)
        col[y][x] = ramp_pick(v, BODY, x, y)
        msk[y][x] = 1

# ---------------------------------------------------------------- eye
def in_opening(px, py):
    if math.hypot(px-ECX, py-ECY) > ER:
        return False
    if py <= lid_y(px) or py >= low_y(px):
        return False
    return True

for y in range(H):
    for x in range(W):
        px, py = x + 0.5, y + 0.5
        if msk[y][x] != 1 or not in_opening(px, py):
            continue
        de = math.hypot(px-ECX, py-ECY)
        di = math.hypot(px-ICX, py-ICY)
        th = math.atan2(py-ICY, px-ICX)
        if di <= IR + 0.4:
            u = clamp(di / IR)
            v = 0.66 - 0.30 * u ** 1.3 + 0.09 * math.sin(th)
            v += 0.11 * math.sin(24*th + 2.2*math.sin(4*th + 1.0)) * (0.35 + 0.65*u)
            v += 0.05 * math.sin(11*th - 1.0)
            v -= 0.36 * smoothstep(0.82, 1.0, u)     # limbal ring
            halo = 0.0
            if di > PR:
                halo = 0.70 * (1.0 - smoothstep(PR, PR + 3.6, di)) ** 1.4
            idx = clamp(v) + halo * 0.34
            ii = int(round(idx * (len(IRIS) - 1)))
            cbase = IRIS[max(0, min(len(IRIS)-1, ii))]
            if di <= PR:
                t = clamp(1.0 - di/PR)
                inten = clamp(t * 1.15) ** 1.2
                gi = int(round(inten * (len(GLOW) - 1)))
                col[y][x] = GLOW[gi]
            else:
                col[y][x] = cbase
        else:
            us = de / ER
            nzs = math.sqrt(max(0.0, 1.0 - min(1.0, us*us)))
            nxs = (px-ECX)/max(de, 1e-6)*us
            nys = (py-ECY)/max(de, 1e-6)*us
            lam = nxs*LX + nys*LY + nzs*LZ
            v = 0.34 + 0.62*max(0.0, lam)
            v -= 0.34 * smoothstep(0.66, 1.0, us)
            v *= 0.50 + 0.50 * smoothstep(lid_y(px), lid_y(px) + 6.0, py)
            v *= 0.74 + 0.26 * smoothstep(low_y(px) - 4.0, low_y(px), py)
            col[y][x] = ramp_pick(clamp(v), SCLERA, x, y)

# veins
VEINS = [
    [(19.5, 22.0), (21.8, 23.4), (23.4, 24.2)],
    [(20.0, 30.0), (22.4, 29.0), (24.0, 28.2)],
    [(44.5, 22.0), (42.2, 23.4), (40.6, 24.2)],
    [(44.0, 30.0), (41.6, 29.0), (40.0, 28.2)],
    [(30.5, 37.0), (31.0, 35.2)],
    [(35.0, 14.5), (34.6, 16.2)],
]
def line_pts(a, b):
    n = int(max(abs(b[0]-a[0]), abs(b[1]-a[1])) * 3) + 1
    return [(a[0] + (b[0]-a[0])*i/n, a[1] + (b[1]-a[1])*i/n) for i in range(n+1)]

for vein in VEINS:
    pts = []
    for i in range(len(vein)-1):
        pts += line_pts(vein[i], vein[i+1])
    for (vx, vy) in pts:
        ix, iy = int(math.floor(vx)), int(math.floor(vy))
        if 0 <= ix < W and 0 <= iy < H and msk[iy][ix] == 1:
            px, py = ix+0.5, iy+0.5
            de = math.hypot(px-ECX, py-ECY)
            if in_opening(px, py) and IR + 0.8 < de < ER - 0.8:
                col[iy][ix] = VEIN

# specular highlight
for y in range(H):
    for x in range(W):
        px, py = x + 0.5, y + 0.5
        if msk[y][x] != 1 or not in_opening(px, py):
            continue
        d = math.hypot((px-26.0)/3.6, (py-20.2)/2.8)
        if d < 1.0:
            col[y][x] = SPEC if d < 0.62 else SPEC2
        d2 = math.hypot((px-39.5)/1.5, (py-31.5)/1.2)
        if d2 < 1.0:
            col[y][x] = SPEC2

# ---------------------------------------------------------------- lids
for y in range(H):
    for x in range(W):
        if msk[y][x] != 1:
            continue
        px, py = x + 0.5, y + 0.5
        if in_opening(px, py):
            continue
        if math.hypot(px-ECX, py-ECY) > ER + 1.0:
            continue
        if math.hypot(px-ECX, py-ECY) <= ER:
            bf = body_field(px, py)
            if bf is not None:
                nx, ny, nz, t, _, _ = bf
                v = flesh_value(nx, ny, nz, t, px, py) * 0.92
                col[y][x] = ramp_pick(clamp(v), BODY, x, y)
            else:
                col[y][x] = BODY[2]
        d = lid_y(px) - py
        if 0.0 <= d < 2.2:
            col[y][x] = LASH
        d2 = py - low_y(px)
        if 0.0 <= d2 < 1.4:
            col[y][x] = LASH

# socket line: flesh touching the eye opening
open_mask = [[0]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if msk[y][x] == 1 and in_opening(x+0.5, y+0.5):
            open_mask[y][x] = 1
for y in range(H):
    for x in range(W):
        if msk[y][x] != 1 or open_mask[y][x]:
            continue
        for (dx, dy) in ((1,0),(-1,0),(0,1),(0,-1)):
            nx2, ny2 = x+dx, y+dy
            if 0 <= nx2 < W and 0 <= ny2 < H and open_mask[ny2][nx2]:
                col[y][x] = LASH
                break

# ---------------------------------------------------------------- outline
for y in range(H):
    for x in range(W):
        if msk[y][x] != 1:
            continue
        edge = False
        for (dx, dy) in ((1,0),(-1,0),(0,1),(0,-1)):
            nx2, ny2 = x+dx, y+dy
            if not (0 <= nx2 < W and 0 <= ny2 < H) or msk[ny2][nx2] != 1:
                edge = True
                break
        if edge:
            col[y][x] = OUTLINE

# ---------------------------------------------------------------- paint
c = new_canvas(W, H, name="result")
for y in range(H):
    for x in range(W):
        if col[y][x] is not None:
            c.set(x, y, col[y][x])

print(c.stats_text())
p = view(c)
print("preview:", p)
save("void_eye", c)
finish(c)
