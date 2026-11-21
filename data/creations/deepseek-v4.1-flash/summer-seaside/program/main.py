from math import sqrt, sin, cos, pi

W = H = 128
c = new_canvas(W, H, background="#2f7fd0", name="result")

# ---------------- palette ----------------
SKY = ["#2f7fd0", "#3f96dd", "#63b3e8", "#92d0f2", "#bfe6f8"]
CLOUD, CLOUDSH, CLOUDSH2 = "#ffffff", "#d7ecfa", "#b7dcf3"
SUNGLOW, SUNDISC, SUNCORE, SUNRAY = "#ffeaa0", "#ffd76b", "#fff6c8", "#ffdf7a"
DEEP1, DEEP2, SEA3, SEA4, SEA5 = "#0d4c86", "#0f639f", "#137fb0", "#17a0b2", "#2ec2ae"
FOAMSH = "#a6e6e0"
WETSAND, SAND, SANDL, SANDD = "#d8ae70", "#efca88", "#f8e0b0", "#dcb072"
RED, REDD, CANWHITE = "#e63946", "#b32a38", "#fff8ef"
POLE, POLED = "#c8a878", "#a8875c"
TEAL, CREAM, TEALD = "#1fa9a2", "#fdf4d9", "#16837e"
PINK, PINKD = "#ff7a8a", "#d95a6c"
BLUE, BLUED = "#4fc3d9", "#2f9db4"
GULL, HULL, SAILSH = "#3a4a5a", "#35556e", "#e9dfc8"

# ---------------- sky ----------------
bands = [(0, 12), (12, 24), (24, 36), (36, 47), (47, 58)]
for i, (y0, y1) in enumerate(bands):
    c.rect(0, y0, W, y1 - y0, SKY[i])
for i in range(len(bands) - 1):
    yb = bands[i][1]
    c.dither(0, yb - 1, W, 2, [SKY[i], SKY[i + 1]], pattern="checker")

# ---------------- sun ----------------
SX, SY = 104, 16
for k in range(8):
    a = k * pi / 4 + 0.2
    c.line(int(round(SX + cos(a) * 12)), int(round(SY + sin(a) * 12)),
           int(round(SX + cos(a) * 15)), int(round(SY + sin(a) * 15)), SUNRAY)
c.circle(SX, SY, 10, SUNGLOW)
c.circle(SX, SY, 7, SUNDISC)
c.circle(SX, SY, 3, SUNCORE)

# ---------------- clouds ----------------
def cloud(puffs, base, sh=2):
    for (x, y, rx, ry) in puffs:
        c.ellipse(x + sh, y + sh, rx, ry, CLOUDSH)
    x0, y0, w, h = base
    c.rect(x0 + sh, y0 + sh, w, h, CLOUDSH)
    for (x, y, rx, ry) in puffs:
        c.ellipse(x, y, rx, ry, CLOUD)
    c.rect(x0, y0, w, h, CLOUD)
    if w >= 40:
        c.dither(x0 + 3, y0 + h - 1, w - 6, 1, [CLOUD, CLOUDSH2], pattern="checker")

# big soft cloud high over the middle sky
cloud([(48, 19, 12, 8), (62, 14, 14, 10), (76, 18, 10, 7), (40, 21, 9, 6)],
      (36, 19, 48, 7))
# small cloud top-left corner
cloud([(8, 10, 6, 4), (15, 9, 6, 5), (22, 11, 5, 3)], (4, 10, 22, 3), sh=1)

# ---------------- gulls ----------------
def gull(x, y, col):
    d = (f"M {x-5} {y+1} L {x-4} {y-1} L {x-2} {y-3} L {x} {y+1} "
         f"L {x+2} {y-3} L {x+4} {y-1} L {x+5} {y+1}")
    c.path(d, col, fill=False)

gull(26, 31, GULL)
gull(76, 36, GULL)

# ---------------- sea ----------------
seab = [(DEEP1, 58, 61), (DEEP2, 61, 68), (SEA3, 68, 75), (SEA4, 75, 80), (SEA5, 80, 93)]
for col, y0, y1 in seab:
    c.rect(0, y0, W, y1 - y0, col)
for i in range(len(seab) - 1):
    yb = seab[i][2]
    c.dither(0, yb - 1, W, 2, [seab[i][0], seab[i + 1][0]], pattern="checker")
c.rect(0, 58, W, 1, DEEP1)

def wave(y, amp=3, step=16):
    d = f"M 0 {y}"
    x, sign = 0, -1
    while x < W - 1:
        nx = min(x + step, W - 1)
        d += f" Q {(x+nx)//2} {y+sign*amp} {nx} {y}"
        sign = -sign
        x = nx
    return d

c.path(wave(63, 2, 16), "#8fd4e8", fill=False)
c.path(wave(69, 2, 16), "#a9e0ee", fill=False)
c.path(wave(75, 2, 21), CLOUD, fill=False)
c.path(wave(79, 3, 26), CLOUD, fill=False)

# sun shimmer on the water
for (x, y, w) in [(96, 60, 8), (103, 62, 6), (98, 64, 5), (107, 59, 5), (94, 66, 4)]:
    c.rect(x, y, w, 1, "#bfe6f8")

# ---------------- boat (far out) ----------------
c.rect(89, 44, 2, 15, "#4a5a6a")
c.poly([(89, 46), (89, 58), (83, 58)], CANWHITE)
c.poly([(91, 47), (91, 58), (96, 58)], SAILSH)
c.poly([(82, 59), (99, 59), (96, 63), (85, 63)], HULL)
c.rect(81, 63, 20, 1, "#bfe6f8")

# ---------------- wet sand / foam / dry sand ----------------
c.rect(0, 88, W, 10, WETSAND)

foam = ("M0 85 Q 8 81 16 84 Q 24 87 32 84 Q 40 81 48 84 Q 56 87 64 84 "
        "Q 72 81 80 84 Q 88 87 96 84 Q 104 81 112 84 Q 120 87 127 85 "
        "L127 90 L0 90 Z")
c.path(foam, CLOUD, fill=True)
c.path("M0 90 Q 8 87 16 90 Q 24 92 32 89 Q 40 87 48 90 Q 56 92 64 89 "
       "Q 72 87 80 90 Q 88 92 96 90 Q 104 87 112 90 Q 120 92 127 90", FOAMSH, fill=False)

dry = ("M0 96 Q 16 94 32 96 Q 48 98 64 96 Q 80 94 96 96 Q 112 98 127 96 "
       "L127 127 L0 127 Z")
c.path(dry, SAND, fill=True)
c.dither(0, 95, W, 2, [WETSAND, SAND], pattern="checker")

# sand grain
_st = [987654321]
def rnd():
    _st[0] = (_st[0] * 1103515245 + 12345) & 0x7fffffff
    return _st[0] >> 8

for y in range(96, H):
    for x in range(W):
        r = rnd()
        if r % 37 == 0:
            c.set(x, y, SANDL)
        elif r % 41 == 0:
            c.set(x, y, SANDD)

# ---------------- umbrella shadow ----------------
c.ellipse(28, 99, 23, 6, SANDD)
c.ellipse(32, 98, 15, 4, WETSAND)

# ---------------- umbrella ----------------
CX, CY, RX, RY = 40, 50, 23, 17

def dome_y(x):
    dx = max(-1.0, min(1.0, (x - CX) / RX))
    return CY - RY * sqrt(1.0 - dx * dx)

n = 8
xs = [CX - RX + 2 * RX * i / n for i in range(n + 1)]
for i in range(n):
    x0, x1 = xs[i], xs[i + 1]
    pts = []
    x = x0
    while x < x1:
        pts.append((int(round(x)), int(round(dome_y(x)))))
        x += 0.5
    pts.append((int(round(x1)), int(round(dome_y(x1)))))
    pts.append((int(round(x1)), CY + 1))
    pts.append((int(round(x0)), CY + 1))
    c.poly(pts, RED if i % 2 == 0 else CANWHITE)

for x0, x1 in ((17, 36), (44, 64)):
    c.path("M " + f"{x0} {int(round(dome_y(x0)))} " +
           " ".join(f"L {x} {int(round(dome_y(x)))}" for x in range(x0 + 1, x1)), REDD, fill=False)
c.rect(17, 51, 47, 1, REDD)

c.rect(39, 50, 2, 46, POLE)
c.rect(41, 50, 1, 46, POLED)
c.rect(39, 29, 2, 5, POLED)

# ---------------- towel ----------------
P0 = (68, 100)
P1 = (114, 106)
P3 = (64, 119)
P2 = (110, 125)

def bl(t, s):
    ax = P0[0] + (P1[0] - P0[0]) * t
    ay = P0[1] + (P1[1] - P0[1]) * t
    bx = P3[0] + (P2[0] - P3[0]) * t
    by = P3[1] + (P2[1] - P3[1]) * t
    return (ax + (bx - ax) * s, ay + (by - ay) * s)

c.poly([(P0[0] + 2, P0[1] + 2), (P1[0] + 2, P1[1] + 2), (P2[0] + 2, P2[1] + 2),
        (P3[0] + 2, P3[1] + 2)], SANDD)

STR = 9
for i in range(STR):
    t0, t1 = i / STR, (i + 1) / STR
    quad = [bl(t0, 0), bl(t1, 0), bl(t1, 1), bl(t0, 1)]
    c.poly([(int(round(x)), int(round(y))) for x, y in quad], TEAL if i % 2 == 0 else CREAM)
c.path(f"M {P0[0]} {P0[1]} L {P1[0]} {P1[1]}", TEALD, fill=False)
c.path(f"M {P3[0]} {P3[1]} L {P2[0]} {P2[1]}", TEALD, fill=False)

# ---------------- flip-flops ----------------
def flipflop(cx, cy, sole, dark):
    c.ellipse(cx + 1, cy + 2, 5, 3, SANDD)
    c.ellipse(cx, cy, 5, 3, dark)
    c.ellipse(cx, cy - 1, 4, 2, sole)
    c.line(cx - 3, cy - 2, cx, cy - 3, CREAM)
    c.line(cx + 3, cy - 2, cx, cy - 3, CREAM)

flipflop(23, 110, PINK, PINKD)
flipflop(39, 118, BLUE, BLUED)

print(c.stats_text())
finish(c)
