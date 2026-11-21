from math import cos, sin, radians, degrees, atan2, hypot, sqrt, pi
import random

random.seed(7)
W = H = 64
c = new_canvas(W, H, background="#050302", name="open-pocket-watch")

# ------------------------------------------------------------------ palette
P = {}
def reg(name, hexv):
    P[name] = c.color(hexv, name=name)

reg("bg0", "#030201"); reg("bg1", "#100a04"); reg("bg2", "#201305"); reg("bg3", "#34200a")
reg("g_hl", "#fff8d8"); reg("g1", "#f4d67e"); reg("g2", "#d9aa45"); reg("g3", "#a4761e")
reg("g4", "#5f400e"); reg("g5", "#33220a")
reg("p1", "#cda34b"); reg("p2", "#a87e2a"); reg("p3", "#71500f")
reg("b1", "#ffe9a4"); reg("b2", "#e8bd55"); reg("b3", "#9a6d15")
reg("s0", "#f4f8fb"); reg("s2", "#9fabb8"); reg("s3", "#5f6b78"); reg("s4", "#2e3641")
reg("j1", "#ff7a5e"); reg("j2", "#c62b28"); reg("j3", "#5e0f16")
reg("d1", "#f8f1dc"); reg("d2", "#e2d6b4"); reg("d3", "#b6a983"); reg("d4", "#8d8163")
reg("ink", "#1d150c")
reg("hb", "#27406b"); reg("hbh", "#7fa0d4"); reg("white", "#ffffff")

CX, CY = 40.0, 36.0
BAYER2 = [[0, 2], [3, 1]]

# ------------------------------------------------------------------ helpers
def px(x, y, col):
    xi, yi = int(round(x)), int(round(y))
    if 0 <= xi < W and 0 <= yi < H:
        c.set(xi, yi, col)

def paint(fn):
    for y in range(H):
        for x in range(W):
            col = fn(x, y)
            if col is not None:
                c.set(x, y, col)

def dist(x, y, cx=CX, cy=CY):
    return hypot(x - cx, y - cy)

def ang(x, y, cx=CX, cy=CY):
    return degrees(atan2(y - cy, x - cx)) % 360.0

def spiral(cx, cy, r0, r1, turns, col):
    n = max(18, int(turns * 36))
    for i in range(n + 1):
        t = i / float(n)
        a = 2 * pi * turns * t
        r = r0 + (r1 - r0) * t
        px(cx + r * cos(a), cy + r * sin(a), col)

def blob(cx, cy, rx, ry, core, halo):
    for dy in range(-int(ry) - 1, int(ry) + 2):
        for dx in range(-int(rx) - 1, int(rx) + 2):
            d = sqrt((dx / rx) ** 2 + (dy / ry) ** 2)
            if d < 1.0:
                px(cx + dx, cy + dy, core if d < 0.45 else halo)

# ------------------------------------------------------------------ background
BGS = [P["bg0"], P["bg1"], P["bg2"], P["bg3"]]
def bg_pixel(x, y):
    d = hypot(x - 33, y - 27) / 49.0
    v = (1.0 - min(d, 1.0)) * 3.5
    b = int(v); f = v - b
    lvl = b + (1 if f > BAYER2[y % 2][x % 2] / 4.0 else 0)
    return BGS[max(0, min(3, lvl))]
paint(bg_pixel)

# cast shadow thrown down-right
def shadow(x, y):
    if y > 58:
        return None
    d1 = hypot(x - 42.5, y - 39.0) - 22.0
    el = sqrt(((x - 12.5) / 9.5) ** 2 + ((y - 39.0) / 20.5) ** 2)
    d = min(d1, (el - 1.0) * 13.0)
    if d < 0.8:
        return P["bg0"]
    if d < 2.6:
        return P["bg0"] if BAYER2[y % 2][x % 2] >= 2 else P["bg1"]
    if d < 4.6:
        return P["bg1"] if BAYER2[y % 2][x % 2] >= 2 else None
    return None
paint(shadow)

# warm reflection of the case on the surface
def reflect(x, y):
    if not (59 <= y <= 63):
        return None
    dx2 = (x - 40.5) ** 2
    if dx2 > 470:
        return None
    dd = abs(y - (117.0 - (36.0 + sqrt(470 - dx2))))
    if dd < 1.1:
        return P["bg3"] if BAYER2[y % 2][x % 2] >= 2 else P["bg2"]
    if dd < 2.2 and BAYER2[y % 2][x % 2] >= 2:
        return P["bg2"]
    return None
paint(reflect)

# ------------------------------------------------------------------ open lid
LX, LY, LRX, LRY = 10.5, 36.0, 9.5, 20.5
def lid_pixel(x, y):
    ex = (x - LX) / LRX
    ey = (y - LY) / LRY
    e = ex * ex + ey * ey
    if e > 1.0:
        return None
    t = sqrt(e)
    a = atan2(ey, ex)
    ld = cos(a + radians(135))
    if t > 0.93:                                  # outer rim
        if ld > 0.80: return P["g_hl"]
        if ld > 0.35: return P["g1"]
        if ld > -0.25: return P["g3"]
        if ld > -0.70: return P["g4"]
        return P["g5"]
    if t > 0.86:                                  # bevel
        if 0.15 < a < 1.25: return P["g1"]        # bounce light
        if ld > 0.70: return P["g1"]
        if ld > -0.35: return P["g2"]
        return P["g3"]
    if abs(t - 0.55) < 0.030 and -0.60 < a < 1.05:
        return P["g3"]                            # engraved ring
    if ld > 0.78: return P["g_hl"]
    if ld > 0.30: return P["g1"]
    if ld > -0.25: return P["g2"]
    if ld > -0.70: return P["g3"]
    return P["g4"]
paint(lid_pixel)

blob(6, 26, 2.2, 4.2, P["white"], P["g_hl"])       # main specular
blob(14, 47, 1.3, 2.8, P["g_hl"], P["g1"])         # bounce light
px(3, 31, P["g_hl"]); px(16, 21, P["g1"]); px(17, 43, P["g1"])
px(2, 40, P["g_hl"]); px(9, 51, P["g1"])

# ------------------------------------------------------------------ movement plate
def plate_pixel(x, y):
    d = dist(x, y)
    if d > 19.5 or y < 39:
        return None
    if d > 18.6:
        return P["p3"]
    dm = hypot(x - 40, y - 46)
    band = int(dm / 2.4) % 2
    ld = cos(radians(ang(x, y)) + radians(135))
    if ld < -0.55:
        return P["p3"] if band else P["p2"]
    return P["p2"] if band else P["p1"]
paint(plate_pixel)

def dial_shadow(x, y):
    if y == 39 and dist(x, y) <= 18.6:
        return P["p3"]
    return None
paint(dial_shadow)

for i in range(46):
    x = random.randint(21, 60); y = random.randint(39, 57)
    if dist(x, y) <= 18.5 and y >= 39:
        px(x, y, random.choice([P["p1"], P["p2"], P["p3"]]))

# ------------------------------------------------------------------ gear train
def gear(cx, cy, rb, teeth, th, body, light, shadow_c, notch, hub_r=1, spokes=0):
    cx, cy = int(round(cx)), int(round(cy))
    ro = rb + th
    c.circle(cx, cy, int(round(ro)) + 1, notch)
    step = 2 * pi / teeth
    pts = []
    for i in range(teeth):
        a = i * step
        pts.append((cx + rb * cos(a - 0.32 * step), cy + rb * sin(a - 0.32 * step)))
        pts.append((cx + ro * cos(a - 0.18 * step), cy + ro * sin(a - 0.18 * step)))
        pts.append((cx + ro * cos(a + 0.18 * step), cy + ro * sin(a + 0.18 * step)))
        pts.append((cx + rb * cos(a + 0.32 * step), cy + rb * sin(a + 0.32 * step)))
    c.poly(pts, body, fill=True)
    rr = rb - 0.9
    for i in range(360):
        aa = radians(i)
        if 195 <= i <= 295:
            px(cx + rr * cos(aa), cy + rr * sin(aa), light)
        elif 15 <= i <= 115:
            px(cx + rr * cos(aa), cy + rr * sin(aa), shadow_c)
    for i in range(teeth):
        a = i * step
        dg = degrees(a) % 360
        if 190 <= dg <= 300:
            px(cx + ro * cos(a), cy + ro * sin(a), light)
    for k in range(spokes):
        a = 2 * pi * k / spokes + 0.4
        c.line(int(round(cx + (hub_r + 0.6) * cos(a))), int(round(cy + (hub_r + 0.6) * sin(a))),
               int(round(cx + (rb - 1.3) * cos(a))), int(round(cy + (rb - 1.3) * sin(a))), shadow_c)
        a2 = a + 0.22
        c.line(int(round(cx + (hub_r + 0.6) * cos(a2))), int(round(cy + (hub_r + 0.6) * sin(a2))),
               int(round(cx + (rb - 1.3) * cos(a2))), int(round(cy + (rb - 1.3) * sin(a2))), body)
    c.circle(cx, cy, hub_r, notch)
    px(cx, cy, light)

def escape_wheel(cx, cy, rb, teeth, th, body, light, notch, hub_r=1):
    cx, cy = int(round(cx)), int(round(cy))
    ro = rb + th
    c.circle(cx, cy, int(round(ro)) + 1, notch)
    step = 2 * pi / teeth
    pts = []
    for i in range(teeth):
        a = i * step
        pts.append((cx + rb * cos(a), cy + rb * sin(a)))
        pts.append((cx + ro * cos(a + 0.45 * step), cy + ro * sin(a + 0.45 * step)))
    c.poly(pts, body, fill=True)
    for i in range(360):
        aa = radians(i)
        if 195 <= i <= 295:
            px(cx + (rb - 0.4) * cos(aa), cy + (rb - 0.4) * sin(aa), light)
    c.circle(cx, cy, hub_r, notch)
    px(cx, cy, light)

# barrel (mainspring drum) with the spring coiled inside
gear(28, 44, 4.2, 16, 1.1, P["b2"], P["b1"], P["b3"], P["g5"], hub_r=2)
c.circle(28, 44, 3, P["g5"], fill=False)
c.circle(28, 44, 2, P["g1"])
spiral(28, 44, 0.6, 2.4, 1.7, P["g4"])
c.circle(28, 44, 1, P["s4"])
px(28, 44, P["s2"])

# centre wheel, third wheel, escape wheel
gear(38, 42, 3.5, 14, 1.0, P["b2"], P["b1"], P["b3"], P["g5"], hub_r=1, spokes=3)
gear(45, 46, 2.4, 12, 0.9, P["b2"], P["b1"], P["b3"], P["g5"], hub_r=1, spokes=3)
escape_wheel(42, 52, 1.8, 9, 0.9, P["s2"], P["s0"], P["s4"], hub_r=1)

# pallet fork
c.line(40, 52, 37, 50, P["s3"])
px(40, 51, P["s4"]); px(40, 53, P["s4"]); px(36, 49, P["s3"]); px(36, 51, P["s3"])

# balance wheel + hairspring
bx, by = 35, 50
c.circle(bx, by, 4, P["s4"])
c.circle(bx, by, 3, P["p3"])
c.line(bx - 3, by, bx + 3, by, P["s4"])
c.line(bx, by - 3, bx, by + 3, P["s4"])
spiral(bx, by, 0.5, 2.4, 2.0, P["s4"])
for i in range(200, 290, 6):
    aa = radians(i)
    px(bx + 3.6 * cos(aa), by + 3.6 * sin(aa), P["s2"])
c.circle(bx, by, 1, P["s4"])
px(bx, by, P["s0"])

def jewel(x, y, ring=False):
    if ring:
        for i in range(0, 360, 5):
            a = radians(i)
            px(x + 2 * cos(a), y + 2 * sin(a), P["g3"])
    c.circle(x, y, 1, P["j3"])
    px(x, y, P["j2"])
    px(x - 1, y - 1, P["j1"])
    px(x + 1, y + 1, P["j3"])

jewel(38, 42, ring=True)
jewel(45, 46)
jewel(42, 52)
jewel(35, 50, ring=True)
jewel(24, 48)

def screw(x, y, horiz=True):
    c.circle(x, y, 1, P["s3"])
    px(x - 1, y - 1, P["s0"])
    if horiz:
        c.line(x - 1, y, x + 1, y, P["s4"])
    else:
        c.line(x, y - 1, x, y + 1, P["s4"])

screw(23, 41); screw(52, 41); screw(56, 47); screw(49, 53); screw(41, 56, False); screw(30, 56)

# ------------------------------------------------------------------ dial
def dial_pixel(x, y):
    d = dist(x, y)
    if d > 19.5 or y > 38:
        return None
    a = ang(x, y)
    ld = cos(radians(a) + radians(135))
    if y == 38:
        return P["d4"]
    if d > 18.6:
        return P["d4"] if ld < -0.10 else P["d3"]
    if d > 17.4:
        return P["d3"]
    if ld > 0.45:
        return P["d1"]
    if ld > -0.35:
        return P["d1"] if ld > -0.05 else P["d2"]
    return P["d2"]
paint(dial_pixel)

# minute track + hour batons (upper arc)
for m in range(31):
    a = radians(180 + m * 6)
    ca, sa = cos(a), sin(a)
    if m % 5 == 0:
        for k in range(26, 36):
            t = k * 0.5
            px(CX + t * ca, CY + t * sa, P["ink"])
            px(CX + t * ca - sa, CY + t * sa + ca, P["ink"])
    else:
        for k in range(32, 36):
            t = k * 0.5
            px(CX + t * ca, CY + t * sa, P["ink"])

# ------------------------------------------------------------------ hands
def hand(angle_deg, length, w0, w1, col, col_hl):
    a = radians(angle_deg)
    dx, dy = cos(a), sin(a)
    ux, uy = -dy, dx
    if ux * (-0.7) + uy * (-0.7) < 0:
        ux, uy = -ux, -uy
    mid = length * 0.78
    pts = [
        (CX + ux * w0 / 2, CY + uy * w0 / 2),
        (CX - ux * w0 / 2, CY - uy * w0 / 2),
        (CX - ux * w1 / 2 + dx * mid, CY - uy * w1 / 2 + dy * mid),
        (CX + dx * length, CY + dy * length),
        (CX + ux * w1 / 2 + dx * mid, CY + uy * w1 / 2 + dy * mid),
    ]
    c.poly(pts, col, fill=True)
    c.line(int(round(CX + ux * w0 * 0.30)), int(round(CY + uy * w0 * 0.30)),
           int(round(CX + ux * w1 * 0.35 + dx * mid)), int(round(CY + uy * w1 * 0.35 + dy * mid)), col_hl)

hand(-150, 11.0, 2.8, 1.1, P["hb"], P["hbh"])
hand(-30, 16.0, 2.2, 0.9, P["hb"], P["hbh"])
c.circle(40, 36, 1, P["s4"])
px(40, 36, P["s0"])

# glass glints on the dial
px(26, 22, P["white"]); px(29, 19, P["white"]); px(24, 26, P["g1"]); px(31, 22, P["g1"])

# ------------------------------------------------------------------ bezel
def bezel_pixel(x, y):
    d = dist(x, y)
    if d > 22 or d < 19:
        return None
    a = ang(x, y)
    ld = cos(radians(a) + radians(135))
    if d > 21.6:
        if ld > 0.55: return P["g4"]
        return P["g5"]
    if d > 20.8:
        if ld > 0.60: return P["g2"]
        if ld > -0.40: return P["g3"]
        return P["g4"]
    if d > 20.0:
        if ld > 0.72: return P["g_hl"]
        if ld > 0.15: return P["g1"]
        if ld > -0.45: return P["g2"]
        return P["g3"]
    if ld > 0.50: return P["g1"]
    if ld > -0.30: return P["g2"]
    return P["g3"]
paint(bezel_pixel)

# rim light along the lower-right edge (studio bounce)
def rim(x, y):
    d = dist(x, y); a = ang(x, y)
    if 21.2 <= d <= 21.9 and 95 <= a <= 165:
        return P["g3"]
    if 20.3 <= d <= 21.4 and 15 <= a <= 70:
        return P["g1"]
    return None
paint(rim)
px(25, 21, P["white"]); px(24, 24, P["g_hl"]); px(28, 18, P["white"])
px(57, 48, P["g1"]); px(59, 44, P["g_hl"]); px(55, 52, P["g2"])

# hinge knuckles joining lid to case
for hy in (30, 41):
    c.rect(18, hy, 4, 3, P["g3"])
    c.rect(18, hy, 4, 1, P["g1"])
    px(21, hy + 2, P["g4"])
    px(18, hy + 1, P["g2"])

# ------------------------------------------------------------------ crown + bow
c.rect(37, 12, 6, 3, P["g3"])
c.rect(37, 12, 6, 1, P["g1"])
px(37, 14, P["g4"]); px(42, 14, P["g4"])
c.ellipse(40, 5, 4, 4, P["g3"], fill=False)
c.ellipse(40, 5, 3, 3, P["g4"], fill=False)
px(37, 2, P["g1"]); px(36, 5, P["g2"]); px(44, 7, P["g4"]); px(43, 2, P["g1"])
c.rect(36, 9, 9, 4, P["g2"])
for xx in (37, 39, 41, 43):
    c.line(xx, 9, xx, 12, P["g3"])
c.line(36, 9, 44, 9, P["g1"])
c.line(36, 12, 44, 12, P["g4"])
px(36, 10, P["g_hl"]); px(44, 11, P["g4"])

# ------------------------------------------------------------------ chain
def link(x, y, horiz, alt):
    xi, yi = int(round(x)), int(round(y))
    if horiz:
        px(xi - 2, yi, P["g2"]); px(xi + 2, yi, P["g3"])
        px(xi - 1, yi - 1, P["g1"] if alt else P["g2"])
        px(xi,     yi - 1, P["g1"] if alt else P["g2"])
        px(xi + 1, yi - 1, P["g2"])
        px(xi - 1, yi + 1, P["g3"] if alt else P["g4"])
        px(xi,     yi + 1, P["g4"])
        px(xi + 1, yi + 1, P["g4"])
    else:
        px(xi, yi - 2, P["g2"]); px(xi, yi + 2, P["g3"])
        px(xi - 1, yi - 1, P["g1"] if alt else P["g2"])
        px(xi - 1, yi,     P["g1"] if alt else P["g2"])
        px(xi - 1, yi + 1, P["g2"])
        px(xi + 1, yi - 1, P["g3"] if alt else P["g4"])
        px(xi + 1, yi,     P["g4"])
        px(xi + 1, yi + 1, P["g4"])

def chain(pts, spacing=4):
    dense = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i + 1]
        n = max(1, int(round(hypot(x1 - x0, y1 - y0))))
        for t in range(n + 1):
            dense.append((x0 + (x1 - x0) * t / n, y0 + (y1 - y0) * t / n))
    k = 0
    for i in range(0, len(dense), spacing):
        x, y = dense[i]
        if 0 < i < len(dense) - 1:
            dx = dense[i + 1][0] - dense[i - 1][0]
            dy = dense[i + 1][1] - dense[i - 1][1]
        else:
            dx, dy = 1.0, 0.0
        link(x, y, abs(dx) >= abs(dy), k % 2 == 0)
        k += 1

chain([(35, 6), (28, 6), (20, 8), (12, 11), (4, 13), (0, 14)])
chain([(45, 6), (52, 6), (59, 9), (63, 12)])

print(c.stats_text())
finish(c)
