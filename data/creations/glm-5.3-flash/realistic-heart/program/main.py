import math

W = H = 64
cv = new_canvas(W, H, name="heart")

# ---------------------------------------------------------------- palette
RAMPS = {}
def deframp(name, cols):
    RAMPS[name] = list(cols)
    return cols

MUSCLE = deframp("muscle", [
    (34,5,8),(47,8,11),(60,11,14),(74,15,18),(89,20,23),(105,26,29),(121,33,36),
    (137,42,45),(153,53,56),(169,66,68),(185,82,83),(199,98,96),(212,114,110),
    (224,132,128),(235,152,148),(244,174,170)])
AORTA = deframp("aorta", [
    (60,8,10),(78,12,14),(97,18,19),(116,26,26),(135,36,35),(153,48,46),(170,62,59),
    (186,78,73),(200,95,89),(213,114,106),(225,134,125),(236,156,146)])
VEIN = deframp("vein", [
    (14,26,40),(20,36,53),(27,48,67),(36,61,81),(47,76,95),(60,91,109),(76,107,123),
    (94,124,137),(114,141,151),(136,158,165),(160,176,180),(186,194,196)])
PULM = deframp("pulm", [
    (30,22,46),(40,30,60),(52,39,74),(65,50,88),(80,63,101),(96,78,113),(114,95,124),
    (133,114,135),(153,134,146),(173,155,157),(193,177,169),(214,201,184)])
ART = deframp("art", [
    (96,16,20),(118,24,26),(140,34,34),(162,47,45),(183,63,58),(202,82,73),
    (219,104,90),(233,128,110)])
FAT = deframp("fat", [
    (140,100,44),(163,124,56),(184,148,70),(203,171,88),(219,192,110),(233,211,136)])
OUTLINE = (24,5,8)

for _c in [c for cols in RAMPS.values() for c in cols]:
    cv.color(_c)
cv.color(OUTLINE)

IDX2RGB = {e["index"]: (e["rgba"][0], e["rgba"][1], e["rgba"][2]) for e in cv.palette()}
LOOK = {}
for _nm, _cols in RAMPS.items():
    for _i, _c in enumerate(_cols):
        LOOK.setdefault(_c, (_nm, _i))

# ---------------------------------------------------------------- lights
def norm3(x, y, z):
    m = math.sqrt(x*x + y*y + z*z)
    if m < 1e-9:
        return 0.0, 0.0, 1.0
    return x/m, y/m, z/m

L  = norm3(-0.55, -0.65, 0.30)     # key light, upper left, grazing
L2 = norm3(0.62, 0.18, 0.42)       # cool fill, lower right
HV = norm3(L[0], L[1], L[2] + 1.0) # half vector for specular

# ---------------------------------------------------------------- noise
def _h(ix, iy, seed):
    n = (ix*374761393 + iy*668265263 + seed*1442695041) & 0x7fffffff
    n = ((n ^ (n >> 13)) * 1274126177) & 0x7fffffff
    n ^= (n >> 16)
    return (n & 0xffff) / 65535.0

def vnoise(x, y, seed=0):
    ix = math.floor(x); iy = math.floor(y)
    fx = x - ix; fy = y - iy
    sx = fx*fx*(3 - 2*fx); sy = fy*fy*(3 - 2*fy)
    a = _h(ix, iy, seed); b = _h(ix+1, iy, seed)
    c_ = _h(ix, iy+1, seed); d_ = _h(ix+1, iy+1, seed)
    top = a + (b - a)*sx
    bot = c_ + (d_ - c_)*sx
    return top + (bot - top)*sy

def smooth(t):
    t = 0.0 if t < 0.0 else (1.0 if t > 1.0 else t)
    return t*t*(3 - 2*t)

# ---------------------------------------------------------------- geometry
def closest_on_poly(px, py, pts):
    bd = 1e18; btc = 0.0; bseg = 0; bend = False; bcx = 0.0; bcy = 0.0
    n = len(pts)
    for i in range(n - 1):
        ax, ay = pts[i]; bx, by = pts[i+1]
        dx = bx - ax; dy = by - ay
        s2 = dx*dx + dy*dy
        if s2 < 1e-12:
            t = 0.0; cx = ax; cy = ay
        else:
            t = ((px - ax)*dx + (py - ay)*dy) / s2
            tc = 0.0 if t < 0.0 else (1.0 if t > 1.0 else t)
            cx = ax + dx*tc; cy = ay + dy*tc
        ddx = px - cx; ddy = py - cy
        dd = math.sqrt(ddx*ddx + ddy*ddy)
        if dd < bd:
            bd = dd; btc = tc; bseg = i; bcx = cx; bcy = cy
            bend = (i == 0 and t < 0.0) or (i == n - 2 and t > 1.0)
    return bd, btc, bseg, bend, bcx, bcy

def poly_side(pts, px, py):
    dd, tc, seg, endpt, cx, cy = closest_on_poly(px, py, pts)
    ax, ay = pts[seg]; bx, by = pts[seg+1]
    dx = bx - ax; dy = by - ay
    ln = math.hypot(dx, dy) or 1.0
    return dd, ((px - cx)*(-dy) + (py - cy)*dx) / ln

def draw_tube(pts, r, ramp, root_fade=0.0, amb=0.16, kd=0.95, kf=0.10,
              ks=1.0, sp=26.0, rim=0.0):
    """Cylinder-shaded tube along a polyline; clamped ends give round caps."""
    nr = len(ramp)
    imap = (nr - 1) / 1.35
    rs = list(r) if isinstance(r, (list, tuple)) else [r]*len(pts)
    cum = [0.0]
    for i in range(len(pts) - 1):
        cum.append(cum[-1] + math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1]))
    rmax = max(rs)
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    x0 = max(0, int(math.floor(min(xs) - rmax - 2)))
    x1 = min(W-1, int(math.ceil(max(xs) + rmax + 2)))
    y0 = max(0, int(math.floor(min(ys) - rmax - 2)))
    y1 = min(H-1, int(math.ceil(max(ys) + rmax + 2)))
    painted = set()
    for py in range(y0, y1 + 1):
        for px in range(x0, x1 + 1):
            dd, tc, seg, endpt, cx, cy = closest_on_poly(px, py, pts)
            if dd > rmax + 0.01:
                continue
            rr = rs[seg] + (rs[seg+1] - rs[seg])*tc
            if dd > rr:
                continue
            lat = dd / rr
            if dd > 1e-6:
                ux = (px - cx)/dd; uy = (py - cy)/dd
            else:
                ux = uy = 0.0
            nx = ux*lat; ny = uy*lat
            nz = math.sqrt(max(0.0, 1.0 - lat*lat))
            dl = nx*L[0] + ny*L[1] + nz*L[2]
            hl = (dl*0.5 + 0.5)**2
            dl2 = nx*L2[0] + ny*L2[1] + nz*L2[2]
            hl2 = (dl2*0.5 + 0.5)**2
            dh = nx*HV[0] + ny*HV[1] + nz*HV[2]
            spv = (dh if dh > 0 else 0.0)**sp
            I = amb + kd*hl + kf*hl2 + ks*spv + rim*lat*lat
            if root_fade > 0:
                sa = cum[seg] + tc*(cum[seg+1] - cum[seg])
                if sa < root_fade:
                    I *= (0.38 + 0.62*smooth(sa/root_fade))
            j = int(I*imap)
            j = 0 if j < 0 else (nr - 1 if j >= nr else j)
            cv.set(px, py, ramp[j])
            painted.add((px, py))
    return painted

def contact_shadow(foot, dx=1, dy=1, steps=2):
    for (x, y) in foot:
        tx = x + dx; ty = y + dy
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        rgb = IDX2RGB.get(cv.get(tx, ty))
        info = LOOK.get(rgb) if rgb is not None else None
        if not info or info[0] != "muscle":
            continue
        ns = info[1] - steps
        cv.set(tx, ty, MUSCLE[0] if ns < 0 else MUSCLE[ns])

def fat_blob(cx, cy, r, seed=5, allow=("muscle",)):
    nf = len(FAT)
    for y in range(int(cy - r - 2), int(cy + r + 3)):
        for x in range(int(cx - r - 2), int(cx + r + 3)):
            if x < 0 or x >= W or y < 0 or y >= H:
                continue
            d = math.hypot(x - cx, y - cy)
            if d > r:
                continue
            vn = vnoise(x*0.9, y*0.9, seed)
            if d > r*0.55 and vn < (d - r*0.55)/(r*0.45):
                continue
            rgb = IDX2RGB.get(cv.get(x, y))
            info = LOOK.get(rgb) if rgb is not None else None
            if not info or info[0] not in allow:
                continue
            t = 1.0 - d/max(r, 1e-6)
            j = int((t*0.6 + vn*0.4)*(nf - 1))
            j = 0 if j < 0 else (nf - 1 if j > nf - 1 else j)
            cv.set(x, y, FAT[j])

# ---------------------------------------------------------------- anatomy data
MASS_D = ("M 19 15 C 26 11 36 11 43 14 "
          "C 51 17 57 24 57 32 "
          "C 57 40 52 47 45 52 "
          "C 38 57 31 60 25 60 "
          "C 24 56 21 52 19 47 "
          "C 16 42 13 36 12 30 "
          "C 11 25 13 20 16 17 "
          "C 17 15.5 18 15 19 15 Z")

SVC_PTS = [(4.5,1),(6,5),(8,9.5),(10,14),(11.5,18.5),(12.5,23),(12.8,26)]
SVC_R   = [2.4,2.3,2.2,2.15,2.1,2.05,2.0]

BR1 = [(41.5,8),(40.5,5),(40.2,2.5)]
BR2 = [(45.5,5.5),(45.2,3.5),(45,2)]
BR3 = [(50.5,6),(52,4),(53,2.5)]

AORTA_PTS = [(39.5,15),(40,11),(41.5,7.5),(45,5),(49,4.8),(52,7),(53.5,11),(54,16),(53.5,21)]
AORTA_R   = [3.3,3.25,3.2,3.15,3.1,3.05,3.0,2.95,2.9]

PT_PTS = [(41,16.5),(39.5,13),(36.5,10),(32.5,8),(28,7),(24,6.5)]
PT_R   = [3.6,3.5,3.3,3.1,2.9,2.7]

LPA_PTS = [(25.5,6.2),(21,4.4),(16.5,2.6),(12.5,1.2)]
LPA_R   = [1.9,1.75,1.6,1.5]

LAD_PTS = [(33.5,17),(31.5,23),(29.5,29),(28,35),(26.5,41),(25.5,47),(24.8,52),(24.3,57)]
LAD_R   = [1.15,1.1,1.05,1.0,0.95,0.9,0.85,0.8]

DIAGS = [
    ([(31.8,21.5),(35,25),(37.5,28)], 0.75),
    ([(30,29.5),(33.5,33.5),(36,37)], 0.70),
    ([(28.5,37.5),(32,41.5),(34.5,45)], 0.65),
    ([(27,45.5),(30,49.5),(32,53)], 0.60),
]
RCA_PTS = [(33,16.5),(28,17.5),(23,19.5),(18.5,23),(15,27.5),(12.8,32.5)]
RCA_R   = [1.05,1.0,0.95,0.9,0.85,0.8]
RCA_BR  = [(16.5,26),(18.5,30.5),(20,35)]

GROOVE_AV  = [(34,16),(28,17.5),(22,20),(17,24),(13.5,29),(12,34.5)]
GROOVE_LAD = LAD_PTS
BUMPS = [(18,21,9,0.50),(45,33,14,0.42),(27,34,12,0.30)]

# ---------------------------------------------------------------- 1. back vessels
draw_tube(SVC_PTS, SVC_R, VEIN)
draw_tube(BR1, 1.30, AORTA)
draw_tube(BR2, 1.15, AORTA)
draw_tube(BR3, 1.15, AORTA)
draw_tube(AORTA_PTS, AORTA_R, AORTA)

# ---------------------------------------------------------------- 2. mass fill
cv.path(MASS_D, (255,0,255), fill=True)

w_, h_, buf = cv.to_rgba()
mask = [[False]*W for _ in range(H)]
for y in range(H):
    row = y*W
    for x in range(W):
        o = (row + x)*4
        if buf[o+3] > 0 and buf[o] == 255 and buf[o+1] == 0 and buf[o+2] == 255:
            mask[y][x] = True

# distance field (inside -> nearest outside)
INF = 1e9
dist = [[0.0]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        dist[y][x] = INF if mask[y][x] else 0.0
for y in range(H):
    for x in range(W):
        v = dist[y][x]
        if x > 0 and dist[y][x-1] + 1 < v: v = dist[y][x-1] + 1
        if y > 0:
            if dist[y-1][x] + 1 < v: v = dist[y-1][x] + 1
            if x > 0 and dist[y-1][x-1] + 1.4142 < v: v = dist[y-1][x-1] + 1.4142
            if x < W-1 and dist[y-1][x+1] + 1.4142 < v: v = dist[y-1][x+1] + 1.4142
        dist[y][x] = v
for y in range(H-1, -1, -1):
    for x in range(W-1, -1, -1):
        v = dist[y][x]
        if x < W-1 and dist[y][x+1] + 1 < v: v = dist[y][x+1] + 1
        if y < H-1:
            if dist[y+1][x] + 1 < v: v = dist[y+1][x] + 1
            if x < W-1 and dist[y+1][x+1] + 1.4142 < v: v = dist[y+1][x+1] + 1.4142
            if x > 0 and dist[y+1][x-1] + 1.4142 < v: v = dist[y+1][x-1] + 1.4142
        dist[y][x] = v

# ---------------------------------------------------------------- 3. shade mass
TILT = (-0.15, -0.19)
for y in range(H):
    for x in range(W):
        if not mask[y][x]:
            continue
        d = dist[y][x]
        gx = dist[y][min(x+1, W-1)] - dist[y][max(x-1, 0)]
        gy = dist[min(y+1, H-1)][x] - dist[max(y-1, 0)][x]
        gl = math.hypot(gx, gy)
        if gl > 1e-6:
            ox, oy = -gx/gl, -gy/gl
        else:
            ox = oy = 0.0
        k = 0.12 + 0.88*math.exp(-d/6.5)
        nx = ox*k + TILT[0]
        ny = oy*k + TILT[1]
        for (bx, by, br, bs) in BUMPS:
            ddx = x - bx; ddy = y - by
            dd = math.hypot(ddx, ddy)
            if dd < br and dd > 1e-6:
                wgt = bs*(1 - (dd/br)**2)**2
                nx += ddx/dd*wgt
                ny += ddy/dd*wgt
        m2 = nx*nx + ny*ny
        if m2 > 0.96:
            sc = 0.98/math.sqrt(m2)
            nx *= sc; ny *= sc
            m2 = nx*nx + ny*ny
        nz = math.sqrt(max(0.04, 1.0 - m2))
        nx, ny, nz = norm3(nx, ny, nz)
        dl = nx*L[0] + ny*L[1] + nz*L[2]
        hl = (dl*0.5 + 0.5)**2
        dl2 = nx*L2[0] + ny*L2[1] + nz*L2[2]
        hl2 = (dl2*0.5 + 0.5)**2
        dh = nx*HV[0] + ny*HV[1] + nz*HV[2]
        I = 0.11 + 0.90*hl + 0.13*hl2 + (dh if dh > 0 else 0.0)**44
        # back-right rim light keeps the dark silhouette readable
        rimr = max(0.0, nx)**1.5 * (1.0 - nz)**1.2
        rimb = max(0.0, ny)**2.0 * (1.0 - nz)**1.2
        I += 0.42*rimr + 0.22*rimb
        I *= (0.62 + 0.38*smooth(d/2.2))
        dg1 = closest_on_poly(x, y, GROOVE_AV)[0]
        dg2 = closest_on_poly(x, y, GROOVE_LAD)[0]
        for dg in (dg1, dg2):
            if dg < 2.6:
                I *= (0.42 + 0.58*smooth(dg/2.6))
        if poly_side(GROOVE_AV, x, y)[1] > 0:
            I *= 0.86
        I += (vnoise(x*0.55 + y*0.25, y*0.9, 3) - 0.5)*0.13
        I += (vnoise(x*0.32, y*0.32, 11) - 0.5)*0.08
        j = int(I*11.0)
        j = 0 if j < 0 else (15 if j > 15 else j)
        cv.set(x, y, MUSCLE[j])
# ---------------------------------------------------------------- 4. front vessels
pt_foot = draw_tube(PT_PTS, PT_R, PULM, root_fade=4.0, rim=0.18)
lpa_foot = draw_tube(LPA_PTS, LPA_R, PULM, rim=0.14)
contact_shadow(pt_foot, 1, 1, 2)
contact_shadow(lpa_foot, 1, 1, 1)

# ---------------------------------------------------------------- 6. fat
for (fx, fy, fr, sd) in [(31,17.2,2.2,1),(26.5,18.8,2.4,2),(21.5,20.8,2.6,3),
                         (17,24.5,2.4,4),(14,28.5,2.0,5),(33.5,20,1.8,6),
                         (30.5,24.5,1.7,7),(45.5,18,2.2,8),(43.5,23,1.9,9),
                         (24,22.5,1.6,10),(27.5,27.5,1.5,11),(25.5,33,1.4,12),
                         (23.5,38.5,1.3,13),(12.5,33,1.5,14)]:
    fat_blob(fx, fy, fr, seed=sd)

# ---------------------------------------------------------------- 5b. coronaries on top of fat
draw_tube(LAD_PTS, LAD_R, ART, ks=0.5, sp=40.0)
for dpts, dr in DIAGS:
    draw_tube(dpts, dr, ART, ks=0.5, sp=40.0)
draw_tube(RCA_PTS, RCA_R, ART, ks=0.5, sp=40.0)
draw_tube(RCA_BR, 0.60, ART, ks=0.5, sp=40.0)

# ---------------------------------------------------------------- 7. contour
cv.outline(OUTLINE)

# ---------------------------------------------------------------- inspect
print(cv.stats_text())
w2, h2, b2 = cv.to_rgba()
left = 0
for i in range(W*H):
    if b2[i*4+3] > 0 and b2[i*4] == 255 and b2[i*4+1] == 0 and b2[i*4+2] == 255:
        left += 1
print("sentinel pixels left:", left)

save("heart", cv)
finish(cv)
