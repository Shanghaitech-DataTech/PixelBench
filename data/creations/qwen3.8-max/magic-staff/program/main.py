import math
try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 48

# ---------------- palette ----------------
WOOD_OUT   = "#20130a"
WOOD_DARK  = "#4b2d16"
WOOD_MID   = "#7d4d26"
WOOD_LIGHT = "#ac753b"
WOOD_HI    = "#d6a45f"

MET_DARK   = "#332f4a"
MET_MID    = "#5f5a80"
MET_LIGHT  = "#948db8"
MET_HI     = "#cfcae8"

LEA_DARK   = "#2e1c11"
LEA_MID    = "#54331c"
LEA_LIGHT  = "#7d4f2a"
LEA_HI     = "#a67139"

GEM_OUT    = "#22103a"
GEM_DARK   = "#4a1c85"
GEM_MID    = "#7730c0"
GEM_LIGHT  = "#a45cef"
GEM_HI     = "#cd97fb"
GEM_SPEC   = "#f4e9ff"

FX_D = "#6f34c4"
FX_M = "#9a55e8"
FX_L = "#c693fb"
FX_W = "#f2e6ff"

# light comes from the upper right
LX, LY = 0.5547, -0.8321

# ---------------- geometry ----------------
C  = (30.0, 15.0)      # centre of the curled head
RR = 8.0               # centreline radius of the curl
TH0 = math.radians(194.5)          # where the shaft meets the curl
TH1 = math.radians(472.0)          # tapered tip of the curl (112 deg)
A = (C[0] + RR * math.cos(TH0), C[1] + RR * math.sin(TH0))
B = (13.5, 46.0)                   # bottom of the shaft

pts = []
N1 = 64
for i in range(N1 + 1):
    t = i / N1
    pts.append((B[0] + (A[0] - B[0]) * t, B[1] + (A[1] - B[1]) * t))
N2 = 170
for i in range(1, N2 + 1):
    th = TH0 + (TH1 - TH0) * i / N2
    pts.append((C[0] + RR * math.cos(th), C[1] + RR * math.sin(th)))

cum = [0.0] * len(pts)
for i in range(len(pts) - 1):
    cum[i + 1] = cum[i] + math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
TOTAL   = cum[-1]
S_SHAFT = cum[N1]
ARC_LEN = TOTAL - S_SHAFT


def smooth(t):
    return t * t * (3.0 - 2.0 * t)


def radius_at(s):
    r = None
    if s < 1.7:                                   # blunt metal tip
        r = 0.72 + (1.05 - 0.72) * (s / 1.7)
    elif s < S_SHAFT - 9.5:                       # straight shaft
        r = 1.05
    elif s < S_SHAFT:                             # swell into the head
        r = 1.05 + (2.0 - 1.05) * smooth((s - (S_SHAFT - 9.5)) / 9.5)
    else:
        sa = s - S_SHAFT
        if sa < ARC_LEN - 9.5:                    # head
            r = 2.0
        else:                                     # tapered tip
            r = 2.0 + (0.42 - 2.0) * smooth((sa - (ARC_LEN - 9.5)) / 9.5)
    if S_SHAFT - 3.4 <= s < S_SHAFT - 1.2:        # raised metal ferrule
        r += 0.35
    return r


radii = [radius_at(s) for s in cum]

GRAIN = [(6.5, 9.0), (19.5, 22.0), (24.0, 25.4),
         (S_SHAFT + 4.0, S_SHAFT + 7.5), (S_SHAFT + 13.0, S_SHAFT + 16.0),
         (S_SHAFT + 22.0, S_SHAFT + 25.0)]


def pick(s, f, r):
    if s < 5.2:
        pal = (MET_DARK, MET_MID, MET_LIGHT, MET_HI)
    elif 10.5 <= s < 18.5:
        stripe = (s % 2.6) < 0.85
        pal = (LEA_DARK,
               LEA_DARK if stripe else LEA_MID,
               LEA_MID if stripe else LEA_LIGHT,
               LEA_LIGHT if stripe else LEA_HI)
    elif S_SHAFT - 3.4 <= s < S_SHAFT - 1.2:
        pal = (MET_DARK, MET_MID, MET_LIGHT, MET_HI)
    else:
        pal = (WOOD_DARK, WOOD_MID, WOOD_LIGHT, WOOD_HI)

    if r >= 1.5 and f >= 0.82:
        idx = 3
    elif f >= 0.28:
        idx = 2
    elif f >= -0.42:
        idx = 1
    else:
        idx = 0
    if idx > 0 and any(a <= s <= b for a, b in GRAIN):
        idx -= 1
    return pal[idx]


def render_tube(cv, pts, radii, pick, outline):
    n = len(pts)
    boxes = []
    for i in range(n - 1):
        ax, ay = pts[i]
        bx, by = pts[i + 1]
        m = max(radii[i], radii[i + 1]) + 1.6
        boxes.append((min(ax, bx) - m, max(ax, bx) + m, min(ay, by) - m, max(ay, by) + m))
    data = [[None] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            bd = None
            bi = bt = 0
            bpx = bpy = bdx = bdy = 0.0
            for i in range(n - 1):
                x0, x1, y0, y1 = boxes[i]
                if x < x0 or x > x1 or y < y0 or y > y1:
                    continue
                ax, ay = pts[i]
                bx, by = pts[i + 1]
                dx, dy = bx - ax, by - ay
                L2 = dx * dx + dy * dy
                if L2 <= 0:
                    continue
                t = ((x - ax) * dx + (y - ay) * dy) / L2
                if t < 0.0:
                    t = 0.0
                elif t > 1.0:
                    t = 1.0
                px = ax + t * dx
                py = ay + t * dy
                d2 = (x - px) * (x - px) + (y - py) * (y - py)
                if bd is None or d2 < bd:
                    bd, bi, bt, bpx, bpy, bdx, bdy = d2, i, t, px, py, dx, dy
            if bd is None:
                continue
            d = math.sqrt(bd)
            r = radii[bi] + bt * (radii[bi + 1] - radii[bi])
            if d > r + 1.4 or r <= 0.2:
                continue
            s = cum[bi] + bt * (cum[bi + 1] - cum[bi])
            tl = math.hypot(bdx, bdy) or 1.0
            nx, ny = -bdy / tl, bdx / tl
            if nx * LX + ny * LY < 0:
                nx, ny = -nx, -ny
            f = ((x - bpx) * nx + (y - bpy) * ny) / max(r, 0.35)
            data[y][x] = (d, r, s, f)

    solid = [[False] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            v = data[y][x]
            if v is None:
                continue
            d, r, s, f = v
            if d <= r + 0.25:
                cv.set(x, y, pick(s, f, r))
                solid[y][x] = True
    for y in range(H):
        for x in range(W):
            if solid[y][x]:
                continue
            v = data[y][x]
            if v is None:
                continue
            d, r, s, f = v
            if d <= r + 1.25:
                cv.set(x, y, outline)
    return solid


wood = new_canvas(W, H, name="wood")
render_tube(wood, pts, radii, pick, WOOD_OUT)

# ---------------- gem ----------------
GEM_ROWS = {11: (29, 31), 12: (27, 33), 13: (26, 34), 14: (26, 34),
            15: (26, 34), 16: (26, 34), 17: (26, 34), 18: (27, 33), 19: (29, 31)}


def in_gem(x, y):
    if y not in GEM_ROWS:
        return False
    a, b = GEM_ROWS[y]
    return a <= x <= b


def gem_shade(x, y):
    u = x - 30.0
    v = 15.0 - y
    d = math.hypot(u, v) / 4.3
    b = 0.72 - 0.45 * d + 0.22 * (u + v) / 4.2
    if b > 0.80:
        return GEM_SPEC
    if b > 0.66:
        return GEM_HI
    if b > 0.52:
        return GEM_LIGHT
    if b > 0.38:
        return GEM_MID
    return GEM_DARK


geml = new_canvas(W, H, name="gem")
for y in range(11, 20):
    for x in range(26, 35):
        if not in_gem(x, y):
            continue
        edge = any(not in_gem(x + dx, y + dy)
                   for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))
        geml.set(x, y, GEM_OUT if edge else gem_shade(x, y))
for (x, y, c) in [(31, 13, GEM_SPEC), (32, 13, GEM_HI), (31, 14, GEM_HI), (30, 13, GEM_HI)]:
    if in_gem(x, y):
        geml.set(x, y, c)

# ---------------- glow ----------------
def fdisc(cv, cx, cy, r, col):
    for y in range(max(0, int(cy - r - 1)), min(H, int(cy + r + 2))):
        for x in range(max(0, int(cx - r - 1)), min(W, int(cx + r + 2))):
            if math.hypot(x - cx, y - cy) <= r:
                cv.set(x, y, col)


glow = new_canvas(W, H, name="glow")
fdisc(glow, 30, 15, 15.0, "#8f45d807")
fdisc(glow, 30, 15, 13.5, "#8f45d80a")
fdisc(glow, 30, 15, 12.0, "#8f45d80e")
fdisc(glow, 30, 15, 10.5, "#9a55e814")
fdisc(glow, 30, 15, 9.0, "#9a55e81c")
fdisc(glow, 30, 15, 7.4, "#a45cef26")
fdisc(glow, 30, 15, 5.8, "#a45cef34")

# ---------------- particles ----------------
fx = new_canvas(W, H, name="fx")


def mote(x, y, col, size=0):
    x = int(round(x))
    y = int(round(y))
    if not (0 <= x < W and 0 <= y < H):
        return
    if size >= 1:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + dx < W and 0 <= y + dy < H:
                fx.set(x + dx, y + dy, FX_D)
    fx.set(x, y, col)


def sparkle(x, y, arm, core, armc):
    for i in range(1, arm + 1):
        c = core if i == 1 else armc
        for dx, dy in ((i, 0), (-i, 0), (0, i), (0, -i)):
            if 0 <= x + dx < W and 0 <= y + dy < H:
                fx.set(x + dx, y + dy, c)
    fx.set(x, y, core)
    if arm >= 2:
        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            if 0 <= x + dx < W and 0 <= y + dy < H:
                fx.set(x + dx, y + dy, armc)


# inner wisp: energy curling out of the opening, hugging the gem
for (x, y, c) in [(29, 20, FX_W), (28, 20, FX_W), (27, 19, FX_L),
                  (26, 18, FX_L), (25, 17, FX_M), (25, 16, FX_M)]:
    mote(x, y, c, 0)

# main stream: leaves the head and swirls around the outside of the curl
for i in range(26):
    t = i / 25.0
    if i % 9 == 4:
        continue
    ang = math.radians(150 + 320 * t + 5.0 * math.sin(t * 23.0))
    rad = 12.6 + 4.2 * smooth(t) + 1.3 * math.sin(t * 19.0 + 0.8)
    x = 30 + rad * math.cos(ang)
    y = 15 + rad * math.sin(ang)
    if t < 0.30:
        c = FX_L
    elif t < 0.62:
        c = FX_M
    else:
        c = FX_D
    mote(x, y, c, 1 if i % 7 == 0 else 0)
    if i % 6 == 2:
        px, py = math.cos(ang + 1.5708), math.sin(ang + 1.5708)
        mote(x + 2.1 * px, y + 2.1 * py, FX_D if t > 0.5 else FX_M, 0)

# sparks just off the ring, in the opening
for (x, y, c) in [(18, 18, FX_L), (17, 20, FX_M)]:
    mote(x, y, c, 0)

# a few free-floating motes, kept off the staff silhouette
for (x, y, c, s) in [(9, 20, FX_M, 0), (11, 15, FX_L, 1), (16, 8, FX_M, 0),
                     (44, 12, FX_M, 0), (45, 18, FX_D, 0), (41, 33, FX_M, 1),
                     (33, 40, FX_D, 0), (26, 43, FX_M, 0), (8, 33, FX_D, 0),
                     (20, 33, FX_L, 0), (18, 36, FX_M, 0), (37, 4, FX_L, 0),
                     (22, 3, FX_M, 0), (46, 40, FX_D, 0)]:
    mote(x, y, c, s)

sparkle(12, 9, 2, FX_W, FX_L)
sparkle(43, 27, 2, FX_W, FX_M)
sparkle(35, 37, 1, FX_L, FX_M)
sparkle(19, 21, 1, FX_W, FX_L)

# ---------------- compose ----------------
result = flatten([wood, glow, geml, fx], name="result")
view(result)
save("magic_staff", result)
print(result.stats_text())
finish(result)
