import math

W = H = 128
c = new_canvas(W, H, name="seaside")

# ---------------- palette ----------------
SKY    = ["#3d9de0", "#5aaee8", "#7ac2ee", "#99d3f4", "#bae2f8", "#d8eefb"]
HAZE   = "#e9f6fd"
SUN_C  = "#fffdf0"; SUN_I = "#fff3ad"; SUN_D = "#ffdf4f"; SUN_G = "#ffe89a"
CLD    = "#ffffff"; CLD_S = "#cfe4f4"
SEA    = ["#16447e", "#1a5c98", "#1e77b2", "#2592c4", "#2eaecc", "#45c5cf", "#73dbd6"]
SPARK  = "#bfe9f4"; GLIT = "#fdf0b8"
FOAM   = "#ffffff"; FOAM2 = "#dcf1f7"; FOAM3 = "#a5daea"
WET    = "#bd8b4f"; WET2 = "#cd9c5c"
SAND   = ["#e0b469", "#eec981", "#f7d99b", "#fbe6b4"]
SAND_D = "#d3a35c"; SAND_L = "#fdeec4"
SHADE  = "#dcae66"; SHADE2 = "#cf9d55"
GULL   = "#4a5c6e"
HULL   = "#2b3d52"; SAIL = "#fdfaf2"; SAIL2 = "#dfe9f0"
POLE   = "#a8763f"; POLE_L = "#cfa269"
URED   = "#d93a2b"; URED_D = "#b32a20"; UWHI = "#fdf7ec"; UWHI_D = "#ddd2be"
SOLE   = "#f2637a"; SOLE_D = "#c9435c"; STRAP = "#fff5e8"
TW     = ["#f8f2e4", "#e0503c", "#2fa8b8", "#f0c24a"]
STAR   = "#ef7f52"; STAR_D = "#cf5f3c"
SHELL  = "#f6e3c8"; SHELL_D = "#d9a06a"


def hash2(x, y):
    v = (x * 374761393 + y * 668265263) & 0xFFFFFFFF
    v = ((v ^ (v >> 13)) * 1274126177) & 0xFFFFFFFF
    return (v ^ (v >> 16)) & 0x7FFFFFFF


# ---------------- sky ----------------
bands = [(0, 7, SKY[0]), (9, 16, SKY[1]), (18, 25, SKY[2]),
         (27, 34, SKY[3]), (36, 43, SKY[4]), (45, 50, SKY[5])]
for y0, y1, col in bands:
    c.rect(0, y0, W, y1 - y0 + 1, col)
for i in range(len(bands) - 1):
    ya, ca = bands[i][1], bands[i][2]
    yb, cb = bands[i + 1][0], bands[i + 1][2]
    for y in range(ya + 1, yb):
        c.dither(0, y, W, 1, [ca, cb], pattern="checker")
c.rect(0, 51, W, 1, HAZE)

# ---------------- sun ----------------
sx, sy = 24, 18
for y in range(sy - 18, sy + 19):
    for x in range(sx - 18, sx + 19):
        if not (0 <= x < W and 0 <= y < H):
            continue
        d = math.hypot(x - sx, y - sy)
        if d <= 3.4:
            c.set(x, y, SUN_C)
        elif d <= 6.8:
            c.set(x, y, SUN_I)
        elif d <= 9.8:
            c.set(x, y, SUN_D)
        elif d <= 11.6:
            c.set(x, y, SUN_G)
        elif d <= 14.4:
            if (x + y) % 2 == 0:
                c.set(x, y, SUN_G)
        elif d <= 17.4:
            if (x + y) % 2 == 0 and hash2(x, y) % 3 == 0:
                c.set(x, y, SUN_G)

# ---------------- clouds ----------------
def cloud(cx, cy, s):
    parts = [(0, 0, 14, 5), (-8, -3, 7, 5), (7, -4, 8, 6), (-1, -7, 7, 5), (12, -1, 5, 3)]
    for dx, dy, rx, ry in parts:
        c.ellipse(int(round(cx + dx * s)), int(round(cy + (dy + 2) * s)),
                  max(1, int(round(rx * s))), max(1, int(round(ry * s))), CLD_S)
    for dx, dy, rx, ry in parts:
        c.ellipse(int(round(cx + dx * s)), int(round(cy + dy * s)),
                  max(1, int(round(rx * s))), max(1, int(round(ry * s))), CLD)


cloud(88, 14, 1.0)
cloud(113, 31, 0.62)
cloud(28, 40, 0.5)

# ---------------- gulls ----------------
def gull(x, y, s, col=GULL):
    w = int(round(7 * s)); h = int(round(4 * s)); t = int(round(1 * s))
    d = ("M %d %d Q %d %d %d %d Q %d %d %d %d" %
         (x - w, y + t, x - int(round(3.5 * s)), y - h, x, y,
          x + int(round(3.5 * s)), y - h, x + w, y + t))
    c.path(d, col, fill=False)


gull(58, 25, 1.0)
gull(74, 35, 0.72)

# ---------------- sea ----------------
sbands = [(52, 56, 0), (58, 64, 1), (66, 72, 2), (74, 80, 3),
          (82, 88, 4), (90, 96, 5), (98, 105, 6)]
for y0, y1, i in sbands:
    c.rect(0, y0, W, y1 - y0 + 1, SEA[i])
for k in range(len(sbands) - 1):
    ya, ia = sbands[k][1], sbands[k][2]
    yb, ib = sbands[k + 1][0], sbands[k + 1][2]
    for y in range(ya + 1, yb):
        c.dither(0, y, W, 1, [SEA[ia], SEA[ib]], pattern="checker")

# sun glitter on the water
for y in range(53, 74):
    span = 2 + (y - 53) // 4
    x = sx - span
    while x <= sx + span:
        if hash2(x, y) % 4 == 0:
            n = 2 if hash2(x + 1, y) % 2 == 0 else 1
            for k in range(n):
                if 0 <= x + k < W:
                    c.set(x + k, y, GLIT if y < 64 else SPARK)
            x += 3
        else:
            x += 1

# sparkles
for y in range(54, 92):
    for x in range(W):
        if hash2(x * 3 + 11, y * 7 + 5) % 260 == 0:
            n = 1 + hash2(x, y) % 3
            for k in range(n):
                if x + k < W:
                    c.set(x + k, y, SPARK)

# ---------------- sailboat ----------------
bx = 46
c.path("M %d %d L %d %d L %d %d L %d %d Z" % (bx - 8, 49, bx + 8, 49, bx + 6, 52, bx - 6, 52), HULL)
c.rect(bx - 7, 49, 15, 1, SAIL2)
c.line(bx, 39, bx, 49, HULL)
c.path("M %d %d L %d %d L %d %d Z" % (bx + 1, 40, bx + 1, 48, bx + 8, 48), SAIL)
c.path("M %d %d L %d %d L %d %d Z" % (bx - 1, 41, bx - 1, 48, bx - 7, 48), SAIL2)
for k in range(4):
    c.set(bx - 6 + k * 4, 53 + (k % 2), SPARK)

# ---------------- wave foam in the sea ----------------
def foam_streak(ybase, amp, phase, thick, col, gapfreq, gapthresh):
    for x in range(W):
        y = int(round(ybase + amp * math.sin(x / 15.0 + phase) + 0.8 * math.sin(x / 5.3 + phase)))
        g = math.sin(x / gapfreq + phase * 2.0)
        if g > gapthresh:
            continue
        for t in range(thick):
            if 0 <= y + t < H:
                c.set(x, y + t, col)


foam_streak(66, 1.4, 0.4, 1, FOAM3, 9.0, 0.55)
foam_streak(74, 1.8, 2.1, 1, FOAM2, 7.0, 0.35)
foam_streak(75, 1.8, 2.1, 1, FOAM, 11.0, 0.72)
foam_streak(83, 2.2, 4.2, 2, FOAM2, 6.0, 0.1)
foam_streak(83, 2.2, 4.2, 1, FOAM, 9.0, 0.5)


# ---------------- shoreline + sand ----------------
def shore(x):
    return int(round(94 + 3.2 * math.sin(x / 17.0 + 0.7) + 1.3 * math.sin(x / 6.1 + 2.0)))


for x in range(W):
    y0 = shore(x)
    seg = [(y0 + 3, y0 + 8, WET), (y0 + 10, y0 + 18, SAND[0]),
           (y0 + 20, y0 + 30, SAND[1]), (y0 + 32, H - 1, SAND[2])]
    for a, b, col in seg:
        for y in range(max(a, 0), min(b, H - 1) + 1):
            c.set(x, y, col)
    for dy, ca, cb in ((9, WET, SAND[0]), (19, SAND[0], SAND[1]), (31, SAND[1], SAND[2])):
        y = y0 + dy
        if 0 <= y < H:
            c.set(x, y, ca if x % 2 == 0 else cb)

# brightest dry sand in the foreground
for x in range(W):
    for y in range(122, H):
        if hash2(x, y) % 3 != 0:
            c.set(x, y, SAND[3])

# sand speckle texture
for y in range(92, H):
    for x in range(W):
        h = hash2(x + 3, y * 5 + 1) % 100
        if h < 3:
            c.set(x, y, SAND_D)
        elif h < 6:
            c.set(x, y, SAND_L)

# shore foam edge
for x in range(W):
    y0 = shore(x)
    top = y0 - 2 - (1 if (x // 6) % 2 == 0 else 0)
    for y in range(top, y0 + 2):
        c.set(x, y, FOAM)
    c.set(x, y0 + 2, FOAM2)
    if hash2(x, 7) % 4 == 0:
        c.set(x, y0 - 4 - hash2(x, 3) % 2, FOAM2)
    if hash2(x, 13) % 9 == 0:
        c.set(x, y0 - 6 - hash2(x, 9) % 3, FOAM)

# thin receding water line
for x in range(W):
    y0 = shore(x)
    if hash2(x, 21) % 3 != 0:
        c.set(x, y0 + 3, FOAM3)

# ---------------- umbrella shadow ----------------
UCX, UAY, UR, UH = 100, 56, 26, 13
c.ellipse(UCX + 3, 114, 26, 5, SHADE)
c.ellipse(UCX + 3, 114, 19, 3, SHADE2)

# ---------------- towel ----------------
P0 = (12, 100); P1 = (54, 94); P3 = (22, 118)
Ax, Ay = P1[0] - P0[0], P1[1] - P0[1]
Bx, By = P3[0] - P0[0], P3[1] - P0[1]
det = Ax * By - Ay * Bx
for y in range(88, 126):
    for x in range(4, 72):
        rx, ry = x - P0[0], y - P0[1]
        u = (rx * By - ry * Bx) / det
        v = (Ax * ry - Ay * rx) / det
        if -0.002 <= u <= 1.002 and -0.002 <= v <= 1.002:
            if v < 0.07 or v > 0.93:
                col = TW[2]
            else:
                n = int(u * 12) % 4
                col = [TW[1], TW[0], TW[0], TW[3]][n]
            c.set(x, y, col)
# towel shadow along lower and right edges
for i in range(43):
    u = i / 42.0
    ex = int(round(P3[0] + u * Ax)); ey = int(round(P3[1] + u * Ay))
    for t in (1, 2):
        c.set(ex, ey + t, SHADE2 if t == 1 else SHADE)
for i in range(25):
    v = i / 24.0
    ex = int(round(P1[0] + v * Bx)); ey = int(round(P1[1] + v * By))
    for t in (1, 2):
        if ex + t < W:
            c.set(ex + t, ey, SHADE2 if t == 1 else SHADE)

# ---------------- flip flops ----------------
def flipflop(x, y):
    c.ellipse(x + 1, y + 2, 5, 7, SHADE2)
    c.ellipse(x, y, 4, 7, SOLE_D)
    c.ellipse(x, y, 3, 6, SOLE)
    c.line(x, y - 3, x - 3, y + 1, STRAP)
    c.line(x, y - 3, x + 3, y + 1, STRAP)
    c.set(x, y - 4, STRAP)
    c.set(x - 3, y + 2, STRAP)
    c.set(x + 3, y + 2, STRAP)


flipflop(69, 113)
flipflop(82, 119)

# ---------------- shells / starfish ----------------
c.ellipse(96, 106, 3, 2, SHELL_D)
c.ellipse(96, 106, 2, 1, SHELL)
c.set(95, 106, SHELL_D); c.set(97, 106, SHELL_D); c.set(96, 105, SHELL_D)
stx, sty = 112, 121
pts = []
for k in range(10):
    a = math.radians(-78 + k * 36)
    r = 6 if k % 2 == 0 else 2.0
    pts.append((stx + r * math.cos(a), sty + r * math.sin(a)))
c.poly(pts, STAR)
for k in range(5):
    a = math.radians(-78 + k * 72)
    c.set(int(round(stx + 4 * math.cos(a))), int(round(sty + 4 * math.sin(a))), STAR_D)
c.set(stx, sty, STAR_D)

# ---------------- umbrella ----------------
c.rect(UCX - 1, UAY - 2, 2, 116 - (UAY - 2), POLE)
c.rect(UCX - 1, UAY - 2, 1, 116 - (UAY - 2), POLE_L)
c.set(UCX, UAY - 4, POLE_L); c.set(UCX, UAY - 3, URED_D)

PHIMAX = math.atan2(UR, UH + 5 - 0)
NS = 9
for x in range(UCX - UR, UCX + UR + 1):
    dx = x - UCX
    t = abs(dx) / UR
    if t > 1.0:
        continue
    top = UAY + int(round(UH * (1 - math.sqrt(max(0.0, 1 - t * t)))))
    bot = UAY + UH + 5 - int(round(5 * t * t))
    dy_ref = max(bot - UAY, 1)
    phi = math.atan2(dx, dy_ref)
    f = min(max((phi / 1.107 + 1) * 0.5, 0.0), 0.9999)
    idx = int(f * NS)
    frac = f * NS - idx
    bot += int(round(2.2 * math.sin(math.pi * frac)))
    dark = dx > 7
    for y in range(top, min(bot, H - 1) + 1):
        if idx % 2 == 0:
            col = UWHI_D if dark else UWHI
        else:
            col = URED_D if dark else URED
        c.set(x, y, col)
    # rim shade line
    if top <= bot < H:
        c.set(x, bot, URED_D if idx % 2 else UWHI_D)
    if top <= bot - 1 < H and dx < -6:
        c.set(x, top, UWHI if idx % 2 == 0 else "#e8574a")

c.set(UCX, UAY, URED_D)

view(c)
print(c.stats_text())
save("seaside", c)
finish(c)
