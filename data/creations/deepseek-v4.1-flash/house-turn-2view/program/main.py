import math

# ------------------------------------------------------------------ palette
NAVY = 'c3'; ORANGE = 'c5'; YEL = 'c6'; CREAM = 'c9'; GREY = 'c8'
DBROWN = 'c0'; TAN = 'c2'; BROWN = 'c1'; MBROWN = 'c4'; SHADOW = 'c10'

def blend(a, b, t):
    return tuple(int(round(a[i] * (1.0 - t) + b[i] * t)) for i in range(3))

WALL_DK = input_canvas.color(blend((225, 220, 163), (22, 28, 46), 0.22), name='walldk')
ROOF_DK = input_canvas.color(blend((220, 170, 70), (22, 28, 46), 0.20), name='roofdk')

# ------------------------------------------------------------------ model
WC, HC = 112, 157

W = 56.0     # wall width  (x)
D = 54.0     # wall depth  (z)
HP = 5.0     # stone plinth
HOW = 34.0   # eave / wall top
OVX, OVZ = 6.0, 5.0
HWX, HDZ = W / 2, D / 2
RX, RZ = HWX + OVX, HDZ + OVZ
HR = HOW + RX                    # 45 degree roof pitch
SX, SZ = 11.0, 27.0              # ground shadow offset
ELEV = math.radians(45.0)
CE, SE = math.cos(ELEV), math.sin(ELEV)
CAM = (0.0, SE, CE)              # direction towards the camera (ortho)

def xf(p, th):
    x, y, z = p
    c, s = math.cos(th), math.sin(th)
    return (x * c + z * s, y, -x * s + z * c)

# face builders ------------------------------------------------------------
def wall_front():
    return [(-HWX, 0, HDZ), (HWX, 0, HDZ), (HWX, HOW, HDZ), (0, HR, HDZ), (-HWX, HOW, HDZ)]

def wall_back():
    return [(HWX, 0, -HDZ), (-HWX, 0, -HDZ), (-HWX, HOW, -HDZ), (0, HR, -HDZ), (HWX, HOW, -HDZ)]

def wall_right():
    return [(HWX, 0, HDZ), (HWX, 0, -HDZ), (HWX, HOW, -HDZ), (HWX, HOW, HDZ)]

def wall_left():
    return [(-HWX, 0, -HDZ), (-HWX, 0, HDZ), (-HWX, HOW, HDZ), (-HWX, HOW, -HDZ)]

def slope_right():
    return [(RX, HOW, -RZ), (0, HR, -RZ), (0, HR, RZ), (RX, HOW, RZ)]

def slope_left():
    return [(-RX, HOW, RZ), (0, HR, RZ), (0, HR, -RZ), (-RX, HOW, -RZ)]

def ridge_cap():
    return [(-2.6, HR + 0.8, -RZ), (2.6, HR + 0.8, -RZ), (2.6, HR + 0.8, RZ), (-2.6, HR + 0.8, RZ)]

# rectangles on the two working wall planes ---------------------------------
def fq(x0, x1, y0, y1):
    z = HDZ + 0.01
    return [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)]

def sq(z0, z1, y0, y1):
    x = HWX + 0.01
    return [(x, y0, z0), (x, y0, z1), (x, y1, z1), (x, y1, z0)]

# ------------------------------------------------------------------ details
def front_details():
    d = []
    d.append(dict(pts=fq(-HWX, HWX, 0, HP), col=DBROWN))               # plinth
    d.append(dict(pts=fq(-HWX, HWX, HP, HP + 1.3), col=TAN))           # plinth cap
    d.append(dict(pts=fq(-HWX, HWX, HOW - 1.4, HOW), col=BROWN))       # floor beam
    # door
    d.append(dict(pts=fq(-9.5, 9.5, HP + 1.3, 27.0), col=NAVY))
    d.append(dict(pts=fq(-7.6, 7.6, HP + 2.6, 26.0), col=ORANGE))
    d.append(dict(pts=fq(-5.4, -2.6, HP + 4.6, 24.6), col=YEL))
    d.append(dict(pts=fq(4.2, 5.8, 15.4, 17.0), col=GREY))
    # two slim windows
    for a, b in ((-26.0, -18.0), (18.0, 26.0)):
        d.append(dict(pts=fq(a, b, 15.0, 27.5), col=NAVY))
        d.append(dict(pts=fq(a + 1.2, b - 1.2, 16.2, 26.3), col=GREY))
        d.append(dict(pts=fq(a + 1.2, b - 1.2, 20.6, 21.9), col=NAVY))
        d.append(dict(pts=fq((a + b) / 2 - 0.7, (a + b) / 2 + 0.7, 16.2, 26.3), col=NAVY))
        d.append(dict(pts=fq(a + 1.8, b - 3.0, 22.5, 25.6), col=CREAM))
    # gable shadow band just under the rakes
    d.append(dict(pts=[(0, HR - 0.2, HDZ + 0.01), (-HWX, HOW - 0.2, HDZ + 0.01),
                       (-HWX, HOW + 2.6, HDZ + 0.01), (0, HR + 2.4, HDZ + 0.01)], col=WALL_DK))
    d.append(dict(pts=[(0, HR - 0.2, HDZ + 0.01), (HWX, HOW - 0.2, HDZ + 0.01),
                       (HWX, HOW + 2.6, HDZ + 0.01), (0, HR + 2.4, HDZ + 0.01)], col=WALL_DK))
    return d

def right_details():
    d = []
    d.append(dict(pts=sq(-HDZ, HDZ, 0, HP), col=DBROWN))
    d.append(dict(pts=sq(-HDZ, HDZ, HP, HP + 1.3), col=TAN))
    d.append(dict(pts=sq(-HDZ, HDZ, HOW - 3.6, HOW), col=WALL_DK))     # eave shadow
    # the window
    d.append(dict(pts=sq(-13.0, 13.0, 9.5, 28.0), col=NAVY))
    d.append(dict(pts=sq(-11.6, 11.6, 10.9, 26.6), col=GREY))
    d.append(dict(pts=sq(-1.1, 1.1, 10.9, 26.6), col=NAVY))
    d.append(dict(pts=sq(-11.6, 11.6, 18.1, 19.3), col=NAVY))
    d.append(dict(pts=sq(-10.4, -2.2, 19.6, 25.4), col=CREAM))
    d.append(dict(pts=sq(2.4, 10.4, 11.8, 17.0), col=blend((225, 220, 163), (22, 28, 46), 0.12)))
    d.append(dict(pts=sq(-14.6, 14.6, 7.6, 9.5), col=BROWN))           # sill
    return d

def blank_details():
    d = []
    d.append(dict(pts=sq(-HDZ, HDZ, 0, HP), col=DBROWN))
    d.append(dict(pts=sq(-HDZ, HDZ, HP, HP + 1.3), col=TAN))
    return d

def left_details():
    d = []
    x = -HWX - 0.01
    d.append(dict(pts=[(x, 0, -HDZ), (x, 0, HDZ), (x, HP, HDZ), (x, HP, -HDZ)], col=DBROWN))
    d.append(dict(pts=[(x, 0, -HDZ), (x, 0, HDZ), (x, HP + 1.3, HDZ), (x, HP + 1.3, -HDZ)], col=TAN))
    return d

def back_details():
    d = []
    z = -HDZ - 0.01
    d.append(dict(pts=[(-HWX, 0, z), (HWX, 0, z), (HWX, HP, z), (-HWX, HP, z)], col=DBROWN))
    d.append(dict(pts=[(-HWX, HP, z), (HWX, HP, z), (HWX, HP + 1.3, z), (-HWX, HP + 1.3, z)], col=TAN))
    return d

def slope_details(side):
    d = []
    for t in (0.18, 0.38, 0.58, 0.78):
        xx = RX * (1.0 - t) * (1 if side == 'r' else -1)
        yy = HOW + t * (HR - HOW) + 0.15
        d.append(dict(pts=[(xx, yy, -RZ), (xx, yy, RZ), (xx, yy + 0.9, RZ), (xx, yy + 0.9, -RZ)],
                      col=ROOF_DK))
    return d

FACES = [
    dict(pts=wall_front(),  n=(0, 0, 1),  col=CREAM,  det=front_details()),
    dict(pts=wall_back(),   n=(0, 0, -1), col=CREAM,  det=back_details()),
    dict(pts=wall_right(),  n=(1, 0, 0),  col=CREAM,  det=right_details()),
    dict(pts=wall_left(),   n=(-1, 0, 0), col=CREAM,  det=left_details()),
    dict(pts=slope_right(), n=(HR - HOW, RX, 0), col=ORANGE, det=slope_details('r')),
    dict(pts=slope_left(),  n=(-(HR - HOW), RX, 0), col=BROWN, det=slope_details('l')),
    dict(pts=ridge_cap(),   n=(0, 1, 0),  col=TAN,    det=[], last=True),
]

# ------------------------------------------------------------------ raster
CX = CY = 0.0
S = 1.0

def sc(p3, th):
    x, y, z = xf(p3, th)
    return (CX + x * S, CY + (SE * z - CE * y) * S)

def fill_poly(cv, pts, col):
    n = len(pts)
    ys = [p[1] for p in pts]
    y0 = max(0, int(math.floor(min(ys))))
    y1 = min(HC - 1, int(math.ceil(max(ys))))
    for y in range(y0, y1 + 1):
        yc = y + 0.5
        xs = []
        for i in range(n):
            ax, ay = pts[i]
            bx, by = pts[(i + 1) % n]
            if (ay <= yc < by) or (by <= yc < ay):
                t = (yc - ay) / (by - ay)
                xs.append(ax + t * (bx - ax))
        xs.sort()
        for i in range(0, len(xs) - 1, 2):
            p0 = max(0, int(math.ceil(xs[i] - 0.5)))
            p1 = min(WC - 1, int(math.floor(xs[i + 1] - 0.5)))
            for x in range(p0, p1 + 1):
                cv.set(x, y, col)

def draw_outline(cv, pts, col=NAVY):
    n = len(pts)
    for i in range(n):
        a = pts[i]; b = pts[(i + 1) % n]
        cv.line(int(round(a[0])), int(round(a[1])), int(round(b[0])), int(round(b[1])), col)

def hull(pts):
    pts = sorted(set(pts))
    if len(pts) < 3:
        return pts
    def cr(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo = []
    for p in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cr(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]

FOOT = [(-HWX, -HDZ), (HWX, -HDZ), (HWX, HDZ), (-HWX, HDZ)]
SHADOW_POLY = hull(FOOT + [(x + SX, z + SZ) for x, z in FOOT])

# ------------------------------------------------------------------ bbox
def all_proj(th):
    out = []
    for f in FACES:
        for v in f['pts']:
            out.append(sc0(v, th))
        for dd in f['det']:
            for v in dd['pts']:
                out.append(sc0(v, th))
    for p in SHADOW_POLY:
        out.append(sc0((p[0], 0.0, p[1]), th))
    return out

def sc0(p3, th):
    x, y, z = xf(p3, th)
    return (x, SE * z - CE * y)

TH1 = math.radians(-45.0)
TH2 = math.radians(-90.0)

pts = all_proj(TH1) + all_proj(TH2)
minx = min(p[0] for p in pts); maxx = max(p[0] for p in pts)
miny = min(p[1] for p in pts); maxy = max(p[1] for p in pts)
MARGIN = 7
S = min((WC - 2 * MARGIN) / (maxx - minx), (HC - 2 * MARGIN) / (maxy - miny))
CX = (WC - (maxx - minx) * S) / 2.0 - minx * S
CY = (HC - (maxy - miny) * S) / 2.0 - miny * S
print('bbox', round(minx, 2), round(maxx, 2), round(miny, 2), round(maxy, 2), 'S=', round(S, 3))

# ------------------------------------------------------------------ render
def render(th, name):
    cv = new_canvas(WC, HC, name=name)
    fill_poly(cv, [sc((p[0], 0.0, p[1]), th) for p in SHADOW_POLY], SHADOW)
    vis = []
    for f in FACES:
        n = xf(f['n'], th)
        dot = n[0] * CAM[0] + n[1] * CAM[1] + n[2] * CAM[2]
        if dot <= 1e-6:
            continue
        cz = sum(xf(v, th)[2] for v in f['pts']) / len(f['pts'])
        vis.append((cz + (999.0 if f.get('last') else 0.0), f))
    vis.sort(key=lambda t: t[0])
    for _, f in vis:
        poly = [sc(v, th) for v in f['pts']]
        fill_poly(cv, poly, f['col'])
        for dd in f['det']:
            fill_poly(cv, [sc(v, th) for v in dd['pts']], dd['col'])
        draw_outline(cv, poly)
    return cv

f1 = render(TH1, 'frame45')
f2 = render(TH2, 'frame90')

print('--- frame 45 ---')
print(f1.stats_text())
print('--- frame 90 ---')
print(f2.stats_text())

def dump(cv, step=3):
    letters = '#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij'
    sym = {}
    k = 0
    for p in cv.palette():
        if p['rgba'][3] == 0:
            sym[p['index']] = '.'
            continue
        sym[p['index']] = letters[k]
        k += 1
    print('    ' + ''.join(str((x // step) % 10) for x in range(0, WC, step)))
    for y in range(0, HC, step):
        print('%3d %s' % (y, ''.join(sym.get(cv.get(x, y), '?') for x in range(0, WC, step))))

for p in f1.palette():
    print(p['index'], p['name'], p['rgba'])

print('=== frame45 ===')
dump(f1)
print('=== frame90 ===')
dump(f2)
