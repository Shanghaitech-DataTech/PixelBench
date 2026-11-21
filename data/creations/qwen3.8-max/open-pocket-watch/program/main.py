import math

c = new_canvas(64, 64, name="pocketwatch")

# ============================ palette ============================
GOLD  = ["#241604", "#3d2708", "#5c3c0e", "#7d5514", "#a3741f",
         "#c69433", "#e2b451", "#f5d17c", "#fdeaae", "#fffbe4"]
DIAL  = ["#5b564a", "#7d7666", "#a29a88", "#c6bfb0", "#e2dccb", "#f6f3ea"]
STEEL = ["#141b24", "#232f3d", "#36475a", "#4d657e", "#758ea8",
         "#a6b9cf", "#dfeaf5"]
BLUED = ["#0b1119", "#16202c", "#243446", "#3a5069", "#63809c",
         "#9db4cb", "#d7e4f2"]
PLATE = ["#0d0904", "#171006", "#241b0d", "#352915", "#483720", "#5c482b"]
RUBY  = ["#4f0e19", "#861625", "#bb283a", "#e0657a"]
BG    = ["#03050a", "#070b11", "#0c1219", "#121a24", "#1a232e",
         "#22292b", "#2b2921", "#372f1e"]
INK   = "#100c06"
SHAD  = "#010204"
GLARE = "#e9f2ff"

LDIR = math.radians(-135.0)          # light comes from the upper-left
LX, LY = math.cos(LDIR), math.sin(LDIR)
PX, PY = -LY, LX                     # perpendicular

CX, CY = 39, 36                      # case centre
R_OUT = 23.4
R_BAND_IN = 19.6
R_GROOVE = 18.4
R_DIAL_IN = 14.2

# ============================ helpers ============================
def pick(ramp, v):
    v = 0.0 if v < 0.0 else (1.0 if v > 1.0 else v)
    return ramp[int(round(v * (len(ramp) - 1)))]


def px(x, y, col):
    x = int(x); y = int(y)
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, col)


def arc(cx, cy, r, a0, a1, col, width=1):
    """a0,a1 in degrees, drawn increasing (may exceed 360)."""
    n = max(10, int(abs(a1 - a0) * math.radians(1) * r * 3))
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        ca, sa = math.cos(a), math.sin(a)
        for w in range(width):
            rr = r - w
            if rr <= 0:
                continue
            px(cx + rr * ca, cy + rr * sa, col)


def shade_ring(cx, cy, r_in, r_out, ramp, mid=0.5, amp=0.9, band=0.0):
    ro = int(math.ceil(r_out)) + 1
    for y in range(cy - ro, cy + ro + 1):
        for x in range(cx - ro, cx + ro + 1):
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy)
            if d < r_in or d > r_out:
                continue
            a = math.atan2(dy, dx)
            t = math.cos(a - LDIR)
            v = mid + amp * 0.5 * t
            if band:
                u = (d - r_in) / max(1e-6, r_out - r_in)
                v += band * (1 - abs(2 * u - 1))
            c.set(x, y, pick(ramp, v))


def shade_disc(cx, cy, r, ramp, mid=0.42, amp=0.85, edge=0.30, spec=0.15):
    ri = int(math.ceil(r)) + 1
    for y in range(int(cy) - ri, int(cy) + ri + 1):
        for x in range(int(cx) - ri, int(cx) + ri + 1):
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy)
            if d > r:
                continue
            t = (dx * LX + dy * LY) / max(r, 1e-6)
            v = mid + amp * 0.5 * t
            if edge:
                v -= edge * max(0.0, (d / r - 0.55)) / 0.45
            if spec and t > 0.5 and d < r * 0.9:
                v += spec * (t - 0.5) / 0.5
            px(x, y, pick(ramp, v))


def soft_shadow(cx, cy, rx, ry):
    for y in range(64):
        for x in range(64):
            d = math.hypot((x - cx) / rx, (y - cy) / ry)
            if d <= 1.0:
                c.set(x, y, SHAD)
            elif d <= 1.12 and (x + y) % 2 == 0:
                c.set(x, y, SHAD)
            elif d <= 1.26 and (x + y) % 4 == 0:
                c.set(x, y, SHAD)


def gear(cx, cy, r, nteeth, ramp, holes=0, hole_r=1, hub=2, jewel=True, sunburst=False):
    rr = r - 1.2                      # rim / root radius
    # ---- teeth ----
    for i in range(nteeth):
        a = 2 * math.pi * i / nteeth
        ca, sa = math.cos(a), math.sin(a)
        lit = 0.55 + 0.40 * math.cos(a - LDIR)
        for k in range(4):
            rad = rr - 0.2 + (r - rr + 0.2) * k / 3.0
            w = 0.75 * (1 - k / 4.0)
            px(cx + rad * ca - sa * w, cy + rad * sa + ca * w, pick(ramp, lit))
            px(cx + rad * ca + sa * w, cy + rad * sa - ca * w, pick(ramp, lit - 0.12))
    # ---- body ----
    shade_disc(cx, cy, rr, ramp, mid=0.40, amp=0.85, edge=0.32, spec=0.18)
    arc(cx, cy, rr, 168, 292, pick(ramp, 0.96))
    arc(cx, cy, rr, 348, 112, pick(ramp, 0.08))
    arc(cx, cy, rr - 1.4, 175, 285, pick(ramp, 0.80))
    if sunburst:
        for k in range(6):
            a = 2 * math.pi * k / 6 + 0.35
            ca, sa = math.cos(a), math.sin(a)
            c.line(int(cx + (hub + 0.6) * ca), int(cy + (hub + 0.6) * sa),
                   int(cx + (rr - 1.2) * ca), int(cy + (rr - 1.2) * sa), ramp[4])
        arc(cx, cy, rr - 0.6, 165, 295, ramp[6])
    # ---- lightening holes ----
    if holes:
        for k in range(holes):
            a = 2 * math.pi * k / holes + 0.35
            hx = cx + 0.60 * rr * math.cos(a)
            hy = cy + 0.60 * rr * math.sin(a)
            c.circle(int(round(hx)), int(round(hy)), hole_r, PLATE[0])
            arc(hx, hy, hole_r, 320, 420, pick(ramp, 0.85))
            arc(hx, hy, hole_r, 140, 260, PLATE[0])
    # ---- hub + jewel ----
    if hub >= 2:
        c.circle(cx, cy, hub, pick(ramp, 0.30))
        arc(cx, cy, hub, 160, 300, pick(ramp, 0.90))
        arc(cx, cy, hub, 340, 120, pick(ramp, 0.06))
    if jewel:
        c.circle(cx, cy, 1, RUBY[1])
        px(cx - 1, cy - 1, RUBY[3]); px(cx, cy - 1, RUBY[2]); px(cx - 1, cy, RUBY[2])
        px(cx + 1, cy + 1, RUBY[0]); px(cx + 1, cy, RUBY[0]); px(cx, cy + 1, RUBY[0])
    else:
        c.circle(cx, cy, max(1, hub - 1), pick(ramp, 0.25))
        px(cx, cy, pick(ramp, 0.75))


def hand(cx, cy, ang, length, tail, w, ramp):
    a = math.radians(ang)
    ux, uy = math.cos(a), math.sin(a)
    vx, vy = -uy, ux
    sh = length * 0.30
    tip = (cx + ux * length, cy + uy * length)
    bl = (cx + vx * w - ux * sh, cy + vy * w - uy * sh)
    br = (cx - vx * w - ux * sh, cy - vy * w - uy * sh)
    tp = (cx - ux * tail, cy - uy * tail)
    quad = [(int(round(p[0])), int(round(p[1]))) for p in (tip, bl, tp, br)]
    shq = [(p[0] + 1, p[1] + 2) for p in quad]
    c.poly(shq, PLATE[0])
    c.poly(quad, ramp[2])
    c.poly(quad, ramp[0], fill=False)
    c.line(quad[0][0], quad[0][1], quad[1][0], quad[1][1], ramp[5])
    c.line(quad[1][0], quad[1][1], quad[2][0], quad[2][1], ramp[4])
    px(int(round(tip[0])), int(round(tip[1])), ramp[6])


# ============================ 1. background ============================
for y in range(64):
    for x in range(64):
        dl = math.hypot(x - 20, y - 14) / 58.0
        dw = math.hypot(x - CX, y - CY) / 36.0
        v = 0.45 * (1 - min(1.0, dl)) + 0.72 * (1 - min(1.0, dw))
        c.set(x, y, pick(BG, v ** 1.7))

# ============================ 2. shadows ============================
soft_shadow(CX + 5, CY + 6, 25.5, 24.5)
soft_shadow(13, 38, 13.0, 23.0)

# ============================ 3. open lid (behind case) =================
LXc, LYc, LRX, LRY = 11, 34, 12, 23
for y in range(LYc - LRY - 1, LYc + LRY + 2):
    for x in range(-2, LXc + LRX + 2):
        dx, dy = (x - LXc) / LRX, (y - LYc) / LRY
        d = math.hypot(dx, dy)
        if d > 1.0:
            continue
        a = math.atan2(dy, dx)
        t = math.cos(a - LDIR)
        if d > 0.90:
            v = 0.52 + 0.46 * t
            col = pick(GOLD, v)
        elif d > 0.83:
            col = pick(GOLD, 0.14 + 0.12 * t)
        else:
            lin = dx * LX + dy * LY
            v = 0.40 + 0.34 * lin - 0.16 * (1 - d / 0.83)
            col = pick(GOLD, v)
        px(x, y, col)
# inner polished panel of the lid
for y in range(LYc - LRY, LYc + LRY + 1):
    for x in range(-2, LXc + LRX + 1):
        dx, dy = (x - LXc) / (LRX * 0.62), (y - LYc) / (LRY * 0.66)
        d = math.hypot(dx, dy)
        if d > 1.0:
            continue
        lin = dx * LX + dy * LY
        px(x, y, pick(GOLD, 0.30 + 0.30 * lin - 0.10 * d))
# bright rim light on the lid's outer edge
for a in range(165, 275):
    aa = math.radians(a)
    px(LXc + LRX * math.cos(aa), LYc + LRY * math.sin(aa), GOLD[9])
for a in range(150, 300):
    aa = math.radians(a)
    px(LXc + (LRX - 1) * math.cos(aa), LYc + (LRY - 1) * math.sin(aa), GOLD[7])
# specular streak on the lid face
for k in range(-13, 14):
    yy = LYc + k
    xx = LXc - 4.5 + abs(k) * 0.28
    px(xx, yy, GOLD[8])
    px(xx + 1, yy, GOLD[6])
    px(xx - 1, yy, GOLD[4])
# hinge knuckles
for hy in (18, 50):
    c.rect(LXc + 6, hy, 6, 4, GOLD[3])
    shade_disc(LXc + 8, hy + 2, 2.4, GOLD, mid=0.5, amp=0.8, edge=0.2)
    px(LXc + 7, hy, GOLD[8])

# ============================ 4. case body ============================
c.circle(CX, CY, 24, INK)

# movement plate (inside the opening)
shade_disc(CX, CY, R_DIAL_IN + 0.6, PLATE, mid=0.48, amp=0.60, edge=0.45, spec=0.0)
# plate speckle / perlage
for y in range(CY - 15, CY + 16):
    for x in range(CX - 15, CX + 16):
        if math.hypot(x - CX, y - CY) > R_DIAL_IN:
            continue
        h = (x * 7 + y * 13 + ((x * x + y * y) // 3) * 5) % 11
        if h == 0:
            c.set(x, y, PLATE[4])
        elif h == 1:
            c.set(x, y, PLATE[1])
# engraved arcs on the plate
arc(CX, CY, 12.6, 200, 250, PLATE[4])
arc(CX, CY, 11.4, 20, 70, PLATE[4])
arc(CX, CY, 9.6, 300, 372, PLATE[4])
arc(CX, CY, 8.2, 250, 320, PLATE[3])

# ============================ 5. gear train ============================
gear(36, 43, 7.6, 22, GOLD,  holes=5, hole_r=1, hub=2, jewel=True)
gear(30, 34, 5.6, 17, GOLD,  holes=4, hole_r=1, hub=2, jewel=True)
gear(40, 28, 3.9, 12, STEEL, holes=0, hub=2, jewel=True, sunburst=True)
gear(46, 33, 3.0, 10, STEEL, holes=0, hub=1, jewel=False, sunburst=True)
gear(45, 46, 4.2, 13, GOLD,  holes=0, hub=2, jewel=True)
gear(27, 41, 2.3, 8,  STEEL, holes=0, hub=1, jewel=False)

# extra plate jewels in the gaps
for (jx, jy) in ((34, 25), (44, 41)):
    c.circle(jx, jy, 2, GOLD[4])
    arc(jx, jy, 2, 160, 300, GOLD[8])
    c.circle(jx, jy, 1, RUBY[1])
    px(jx - 1, jy - 1, RUBY[3]); px(jx, jy - 1, RUBY[2])
    px(jx + 1, jy + 1, RUBY[0])

# movement bridges and screws
arc(36, 43, 9.2, 200, 330, GOLD[6])
arc(36, 43, 9.2, 205, 265, GOLD[8])
arc(30, 34, 7.0, 150, 265, GOLD[5])
arc(45, 46, 5.6, 180, 330, GOLD[6])
for (sx, sy) in ((32, 48), (43, 39), (34, 27)):
    c.circle(sx, sy, 1, GOLD[7])
    px(sx - 1, sy - 1, GOLD[9])
    px(sx, sy, GOLD[2])
    px(sx + 1, sy + 1, GOLD[0])

# ============================ 6. dial chapter ring ============================
shade_ring(CX, CY, R_DIAL_IN, R_GROOVE, DIAL, mid=0.44, amp=0.60, band=0.10)
# inner edge shadow cast by the dial onto the movement
arc(CX, CY, R_DIAL_IN + 0.2, 0, 360, DIAL[0])
arc(CX, CY, R_DIAL_IN + 1.0, 150, 300, DIAL[1])
arc(CX, CY, R_GROOVE - 0.4, 0, 360, DIAL[1])
arc(CX, CY, R_GROOVE - 0.4, 320, 440, DIAL[5])

# tick marks
for h in range(12):
    a = math.radians(-90 + h * 30)
    ca, sa = math.cos(a), math.sin(a)
    card = (h % 3 == 0)
    ro = R_GROOVE - 0.7
    ri = ro - (3.2 if card else 2.0)
    x0, y0 = CX + ro * ca, CY + ro * sa
    x1, y1 = CX + ri * ca, CY + ri * sa
    c.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), INK)
    # faint lume highlight beside each tick
    px(x0 + sa, y0 - ca, DIAL[4])
# half-hour dots
for h in range(12):
    a = math.radians(-90 + h * 30 + 15)
    px(CX + (R_DIAL_IN + 1.4) * math.cos(a), CY + (R_DIAL_IN + 1.4) * math.sin(a), DIAL[0])

# ============================ 7. bezel + case band ============================
shade_ring(CX, CY, R_GROOVE, R_BAND_IN, GOLD, mid=0.16, amp=-0.42, band=0.0)
shade_ring(CX, CY, R_BAND_IN, R_OUT, GOLD, mid=0.50, amp=1.00, band=0.16)
# brushed concentric lines
arc(CX, CY, 22.4, 150, 330, GOLD[8], 1)
arc(CX, CY, 21.2, 160, 320, GOLD[3], 1)
arc(CX, CY, 20.4, 170, 310, GOLD[7], 1)
arc(CX, CY, 22.6, 350, 470, GOLD[2], 1)
arc(CX, CY, 20.6, 10, 120, GOLD[4], 1)
# blazing rim light upper-left, bounce light lower-right
arc(CX, CY, R_OUT - 0.3, 178, 268, GOLD[9], 2)
arc(CX, CY, R_OUT - 0.3, 268, 292, GOLD[8], 1)
arc(CX, CY, R_OUT - 0.3, 0, 70, GOLD[5], 1)
arc(CX, CY, R_OUT - 1.6, 10, 60, GOLD[6], 1)
arc(CX, CY, R_OUT + 0.4, 290, 380, INK, 1)
arc(CX, CY, R_OUT + 0.4, 160, 270, GOLD[2], 1)

# ============================ 8. hands ============================
hand(CX, CY, 212, 10.2, 3.2, 1.35, BLUED)     # hour  -> ~10
hand(CX, CY, 331, 14.4, 3.6, 1.05, BLUED)     # minute -> ~2
c.circle(CX, CY, 2, GOLD[3])
arc(CX, CY, 2, 160, 300, GOLD[8])
c.circle(CX, CY, 1, GOLD[6])
px(CX - 1, CY - 1, GOLD[9])

# ============================ 9. crown, bow, chain ============================
# collar
c.rect(36, 10, 7, 4, GOLD[3])
shade_disc(39, 12, 3.4, GOLD, mid=0.45, amp=0.9, edge=0.25)
c.rect(36, 10, 7, 1, GOLD[6])
# knurled crown
for i, xx in enumerate(range(36, 43)):
    col = GOLD[7] if i % 2 == 0 else GOLD[3]
    c.rect(xx, 6, 1, 4, col)
c.rect(36, 6, 7, 1, GOLD[8])
c.rect(36, 9, 7, 1, GOLD[1])
px(36, 6, GOLD[9]); px(37, 6, GOLD[9])
# bow ring
c.circle(39, 4, 3, GOLD[5], fill=False)
c.circle(39, 4, 2, GOLD[2], fill=False)
arc(39, 4, 3, 165, 285, GOLD[9], 1)
arc(39, 4, 3, 345, 105, GOLD[1], 1)
px(41, 6, GOLD[8]); px(42, 5, GOLD[7])

# chain
def chain_point(t):
    x = 42.0 + 22.0 * t
    y = 5.0 + 17.0 * (t ** 1.25)
    return x, y

pts = []
acc = 0.0
last = chain_point(0.0)
t = 0.0
while t <= 0.97:
    p = chain_point(t)
    acc += math.hypot(p[0] - last[0], p[1] - last[1])
    if acc >= 2.6:
        pts.append(p)
        acc = 0.0
    last = p
    t += 0.004
for i, (qx, qy) in enumerate(pts):
    if i > 0:
        ox, oy = pts[i - 1]
        c.line(int(round(ox)), int(round(oy)), int(round(qx)), int(round(qy)), GOLD[2])
    c.circle(int(round(qx)), int(round(qy)), 1, GOLD[5])
    px(qx - 1, qy - 1, GOLD[9])
    px(qx, qy - 1, GOLD[7])
    px(qx + 1, qy + 1, GOLD[1])

# ============================ 10. crystal glare ============================
def darc(cx, cy, r, a0, a1, col, step=2, off=0):
    n = max(8, int(abs(a1 - a0) * math.radians(1) * r * 2))
    for i in range(n + 1):
        if (i + off) % step:
            continue
        a = math.radians(a0 + (a1 - a0) * i / n)
        px(cx + r * math.cos(a), cy + r * math.sin(a), col)

arc(CX, CY, 15.6, 192, 262, GLARE, 1)
arc(CX, CY, 14.8, 198, 256, GLARE, 1)
darc(CX, CY, 16.4, 200, 252, GLARE, 2)
darc(CX, CY, 14.0, 204, 250, GLARE, 2, 1)
darc(CX, CY, 8.6, 208, 244, GLARE, 3)
darc(CX, CY, 15.2, 24, 62, GLARE, 2)
darc(CX, CY, 14.4, 30, 56, GLARE, 3, 1)

print(c.stats_text())
view(c)
save("pocket_watch", c)
finish(c)
