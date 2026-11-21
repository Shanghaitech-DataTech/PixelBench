import math
from pixelbench_api import new_canvas, finish

S = 64
c = new_canvas(S, S)

PAL = {}
def col(h):
    if h not in PAL:
        PAL[h] = c.color(h)
    return PAL[h]

BG = ["#050505", "#0a0805", "#100d07", "#181209", "#20180d", "#281f12"]
G  = ["#1d1505", "#2f240b", "#413310", "#574316", "#6e561d", "#876b26",
      "#a18132", "#b89540", "#cda94e", "#dfbc5e", "#ecce72", "#f5dd86",
      "#fae99c", "#fdf2b4"]
D  = ["#40350f", "#66551c", "#8f7b33", "#b6a054", "#d6c07c", "#ecd89c",
      "#f6e6b4", "#fbf0cc"]
H  = ["#04050a", "#0e1119", "#1c2130", "#2e3646", "#47526b", "#6b7a9c"]
R  = ["#5f1020", "#8c1e30"]
WL = "#fffee8"

cx, cy = 32, 33

def arc(rx, ry, r, a0, a1, hi, w=1):
    n = max(2, int((a1 - a0) * r / 1.0))
    r0 = int(round(r))
    for k in range(n + 1):
        a = a0 + (a1 - a0) * k / n
        for rr in range(r0, r0 - w, -1):
            c.set(round(rx + rr * math.cos(a)), round(ry + rr * math.sin(a)), col(hi))

def gear(gx, gy, r_tip, r_root, nteeth, body, dark, light, hole, jewel=False):
    step = 2 * math.pi / nteeth
    pts = []
    tips = []
    for i in range(nteeth):
        a = i * step
        pts.append((gx + r_root * math.cos(a - step / 2), gy + r_root * math.sin(a - step / 2)))
        p1 = (gx + r_tip * math.cos(a - step / 4), gy + r_tip * math.sin(a - step / 4))
        p2 = (gx + r_tip * math.cos(a + step / 4), gy + r_tip * math.sin(a + step / 4))
        pts.append(p1); pts.append(p2)
        pts.append((gx + r_root * math.cos(a + step / 2), gy + r_root * math.sin(a + step / 2)))
        tips.append(((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2))
    c.poly(pts, col(body))
    for (tx, ty) in tips:
        a = math.atan2(ty - gy, tx - gx)
        if -2.5 < a < -0.5:
            c.set(round(tx), round(ty), col(light))
        elif 0.6 < a < 2.5:
            c.set(round(tx), round(ty), col(dark))
    for i in range(3):
        a = i * 2 * math.pi / 3 + 0.7
        r0 = r_root * 0.45
        c.line(gx + r0 * math.cos(a), gy + r0 * math.sin(a),
               gx + r_root * math.cos(a), gy + r_root * math.sin(a), col(dark))
    c.circle(gx, gy, max(1, int(r_root * 0.5)), col(hole))
    if jewel:
        c.circle(gx, gy, max(1, int(r_root * 0.32)), col(R[1]))
        c.circle(gx, gy, max(1, int(r_root * 0.18)), col(R[0]))

# ---- background: dark vignette behind the macro shot ----
for y in range(S):
    for x in range(S):
        d = math.hypot(x - cx, y - cy)
        sh = 5 if d < 17 else 4 if d < 22 else 3 if d < 29 else 2 if d < 38 else 1 if d < 48 else 0
        c.set(x, y, col(BG[sh]))

# ---- cast shadow (light from top-left) ----
c.circle(cx + 1, cy + 2, 21, col("#000000"))

# ---- case ----
c.circle(cx, cy, 21, col(G[0]))
c.circle(cx, cy, 20, col(G[4]))
c.circle(cx, cy, 19, col(G[2]))
arc(cx, cy, 19, math.radians(-165), math.radians(-20), G[11], 2)
arc(cx, cy, 20, math.radians(-150), math.radians(-30), G[8])
arc(cx, cy, 20, math.radians(30), math.radians(160), G[1], 2)
c.circle(cx, cy, 16, col(G[4]))
arc(cx, cy, 16.2, math.radians(-145), math.radians(-35), G[8])
arc(cx, cy, 17.4, math.radians(-135), math.radians(-45), G[3])
# screws on the band
for (sx, sy) in [(20, 21), (44, 21), (20, 45), (44, 45)]:
    c.circle(sx, sy, 2, col(G[8]))
    c.set(sx, sy, col(G[0]))

# ---- dial ----
c.circle(cx, cy, 15, col(D[6]))
c.circle(cx, cy, 12, col(G[1]))
arc(cx, cy, 12, math.radians(-155), math.radians(-35), G[6])
arc(cx, cy, 11.4, math.radians(-155), math.radians(-40), G[8])
for i in range(60):
    a = math.radians(i * 6 - 90)
    r1 = 13.1 if i % 5 == 0 else 13.5
    r2 = 14.7
    c.line(cx + r1 * math.cos(a), cy + r1 * math.sin(a),
           cx + r2 * math.cos(a), cy + r2 * math.sin(a), col(H[1] if i % 5 else H[3]))
    if i % 5 == 0:
        c.line(cx + 14.1 * math.cos(a), cy + 14.1 * math.sin(a),
               cx + 14.9 * math.cos(a), cy + 14.9 * math.sin(a), col(G[8]))
# tiny hour-numeral dots
for i in range(12):
    a = math.radians(i * 30 - 90)
    c.set(round(cx + 14.9 * math.cos(a)), round(cy + 14.9 * math.sin(a)), col(H[4]))
# skeleton opening: dark well where the gear train shows through
c.circle(cx, cy, 11, col(G[0]))

# ---- movement gears (skeleton dial, gear train through the face) ----
# balance wheel (top-left)
gear(28, 27, 5.5, 3.5, 6, G[6], G[1], G[11], G[0])
arc(28, 27, 4.6, math.radians(-160), math.radians(-20), G[10], 1)
# main gear
gear(29, 36, 8, 5.5, 8, G[6], G[1], G[11], G[0], jewel=True)
# wheel meshing (bottom-right)
gear(38, 42, 5.5, 3.5, 7, G[5], G[0], G[10], G[0])
# small pinion
gear(33, 41, 4.2, 2.8, 6, G[6], G[1], G[11], G[0])
# bridge cock over the main wheel
c.line(23, 31, 35, 41, col(G[4]))
c.line(23, 32, 35, 42, col(G[2]))
c.circle(24, 32, 1, col(G[9]))

# ---- hands (10:08) ----
def hand(dirx, diry, length, thick, base, hi):
    pxv, pyv = -diry, dirx
    tx = dirx * length; ty = diry * length
    bx = -dirx * 1.3; by = -diry * 1.3
    c.poly([(cx + pxv * thick / 2 + bx, cy + pyv * thick / 2 + by),
           (cx + pxv * thick / 2 + tx, cy + pyv * thick / 2 + ty),
           (cx - pxv * thick / 2 + tx, cy - pyv * thick / 2 + ty),
           (cx - pxv * thick / 2 + bx, cy - pyv * thick / 2 + by)], col(base))
    c.line(cx + pxv * thick / 2 + bx, cy + pyv * thick / 2 + by,
           cx + pxv * thick / 2 + tx, cy + pyv * thick / 2 + ty, col(hi))

th = math.radians(304)
hand(math.sin(th), -math.cos(th), 5.0, 2.6, H[1], H[3])
tm = math.radians(48)
hand(math.sin(tm), -math.cos(tm), 8.6, 1.8, H[0], H[3])
ts = math.radians(180)
hand(math.sin(ts), -math.cos(ts), 10.2, 0.7, G[12], G[13])
# centre cap
c.circle(cx, cy, 2, col(G[9]))
c.circle(cx, cy, 1, col(G[12]))
c.circle(cx, cy, 1, col(H[1]))
c.set(cx - 1, cy, col(G[12]))

# ---- crown (winding stem) ----
c.rect(27, 9, 11, 5, col(G[3]))
c.rect(28, 8, 9, 7, col(G[7]))
c.rect(29, 9, 7, 5, col(G[5]))
c.rect(30, 10, 5, 3, col(G[11]))
c.rect(30, 12, 5, 1, col(G[13]))
c.ellipse(32, 7, 3, 2, col(G[9]))
c.ellipse(32, 7, 1.6, 1, col(G[12]))

# ---- hinge + open lid (thrown back to the upper-left) ----
c.ellipse(15, 15, 10, 6.5, col("#000000"))
c.ellipse(13, 13, 10, 7, col(G[5]))
c.ellipse(13, 13, 8.2, 5.4, col(G[6]))
c.ellipse(13, 13, 7.4, 4.6, col(G[8]))
arc(13, 13, 7.0, math.radians(-175), math.radians(-60), G[12], 2)
arc(13, 13, 6.0, math.radians(-165), math.radians(-45), G[11])
arc(13, 13, 5.0, math.radians(-150), math.radians(-40), G[13], 1)
arc(13, 13, 7.8, math.radians(25), math.radians(155), G[2], 2)
arc(13, 13, 7.0, math.radians(45), math.radians(135), G[1], 1)
arc(13, 13, 6.2, math.radians(50), math.radians(120), G[0], 1)
c.circle(13, 13, 2.4, col(G[9]))
c.set(13, 13, col(G[3]))
c.rect(21, 12, 8, 6, col(G[3]))
c.rect(22, 13, 6, 4, col(G[7]))
c.rect(23, 14, 3, 2, col(G[0]))
c.rect(24, 14, 2, 2, col(G[11]))

# ---- chain running up-right from the crown ----
for (lx, ly) in [(33.0, 6.5), (38.0, 5.5), (43.2, 5.0), (48.0, 4.0), (53.0, 3.0), (57.0, 2.2)]:
    c.ellipse(lx, ly, 2.4, 1.7, col(G[7]))
    c.ellipse(lx, ly, 1.2, 0.8, col(G[0]))
    c.ellipse(lx + 0.7, ly - 0.8, 1.1, 0.6, col(G[11]))
c.ellipse(32, 7, 1.6, 1, col(G[12]))

# ---- glass glare / specular streaks ----
arc(cx, cy, 13.6, math.radians(-145), math.radians(-60), G[13], 1)
arc(cx, cy, 12.4, math.radians(-135), math.radians(-75), WL, 1)
c.line(21, 30, 25, 34, col(G[13]))
c.line(20, 26, 24, 30, col(WL))
c.line(31, 45, 34, 48, col(G[11]))
c.set(32, 15, col(WL))
c.set(30, 14, col(G[13]))
# re-draw the case rim on top of everything so the watch outline stays crisp
arc(cx, cy, 19, math.radians(-165), math.radians(-20), G[11], 2)
arc(cx, cy, 20, math.radians(-150), math.radians(-30), G[8])
arc(cx, cy, 20, math.radians(30), math.radians(160), G[1], 2)

print(c.stats_text())

finish(c)
