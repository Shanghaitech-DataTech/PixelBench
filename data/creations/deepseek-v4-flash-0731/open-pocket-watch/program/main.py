import math
from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, background="#080706")

gold = ["#221605","#36270c","#4a3310","#604114","#795117","#93631e","#ae7728","#c98d34","#e0a544","#f2bf5e","#ffd980"]
spec = "#fff3c0"
hot  = "#fffbe0"
cream = ["#bfb387","#d6c9a0","#e8dbb4","#f4e9c8"]
tk = "#2e240e"
st = ["#161c28","#2c3a52","#5a7196"]
hole = "#0d0a05"

def P(v):
    return max(0, min(63, int(round(v))))

def metal_disc(cx, cy, r, cols, light=(-0.5, -0.62), rim=0.45):
    lx, ly = light
    ll = math.hypot(lx, ly)
    n = len(cols)
    x0 = max(0, int(cx - r) - 1); x1 = min(W, int(cx + r) + 2)
    y0 = max(0, int(cy - r) - 1); y1 = min(H, int(cy + r) + 2)
    for y in range(y0, y1):
        for x in range(x0, x1):
            dx = x - cx; dy = y - cy
            d = math.hypot(dx, dy)
            if d > r + 1e-9:
                continue
            if d < 1e-9:
                diff = 1.0
            else:
                diff = (dx * lx + dy * ly) / (d * ll)
                if diff < 0: diff = 0.0
            b = diff * (1.0 - rim * (d / r))
            idx = min(n - 1, int(b * (n - 1)))
            c.set(x, y, cols[idx])

def ring_circle(cx, cy, rr, col, step=0.22):
    steps = int(2 * math.pi / step) + 1
    for i in range(steps):
        a = i * step
        c.set(P(cx + math.cos(a) * rr), P(cy + math.sin(a) * rr), col)

def annulus(cx, cy, r0, r1, cols, light=(-0.5, -0.62)):
    n = len(cols)
    x0 = max(0, int(cx - r1) - 1); x1 = min(W, int(cx + r1) + 2)
    y0 = max(0, int(cy - r1) - 1); y1 = min(H, int(cy + r1) + 2)
    for y in range(y0, y1):
        for x in range(x0, x1):
            dx = x - cx; dy = y - cy
            d = math.hypot(dx, dy)
            if d < r0 or d > r1:
                continue
            if d < 1e-9:
                diff = 1.0
            else:
                diff = (dx * (-0.5) + dy * (-0.62)) / (d * math.hypot(0.5, 0.62))
                if diff < 0: diff = 0.0
            b = 0.30 + 0.70 * diff
            idx = min(n - 1, int(b * (n - 1)))
            c.set(x, y, cols[idx])

def gear(cx, cy, r, teeth, rot=0.0):
    body = r * 0.8
    for i in range(teeth):
        a = rot + i * 2 * math.pi / teeth
        c.set(P(cx + math.cos(a) * r * 1.18), P(cy + math.sin(a) * r * 1.18), gold[6])
        for off in (-0.5, 0.5):
            c.set(P(cx + math.cos(a + off) * r * 1.28), P(cy + math.sin(a + off) * r * 1.28), gold[5])
    metal_disc(cx, cy, body, gold, light=(-0.5, -0.62), rim=0.5)
    ring_circle(cx, cy, body * 0.82, gold[1], 0.22)
    for i in range(teeth):
        a = rot + (i + 0.5) * 2 * math.pi / teeth
        c.set(P(cx + math.cos(a) * body * 0.55), P(cy + math.sin(a) * body * 0.55), hole)
    c.set(P(cx), P(cy), gold[8])

def hand(cx, cy, ang, length, width):
    a = math.radians(ang)
    dx = math.cos(a); dy = math.sin(a)
    px = -dy * width * 0.5; py = dx * width * 0.5
    x0 = cx + dx * 1.6; y0 = cy + dy * 1.6
    x1 = cx + dx * length; y1 = cy + dy * length
    c.line(P(x0), P(y0), P(x1), P(y1), st[1])
    c.line(P(x0 + px), P(y0 + py), P(x1 + px * 0.5), P(y1 + py * 0.5), st[1])
    c.line(P(x0 - px), P(y0 - py), P(x1 - px * 0.5), P(y1 - py * 0.5), st[1])
    c.set(P(x1), P(y1), st[2])

def add_link(x, y):
    c.set(P(x), P(y + 1), "#050403")
    for dx in (-1, 0, 1):
        c.set(P(x + dx), P(y - 1), gold[7])
        c.set(P(x + dx), P(y + 1), gold[4])
    for dx in (-1, 1):
        c.set(P(x + dx), P(y), gold[5])
    c.set(P(x), P(y), gold[6])
    c.set(P(x - 1), P(y - 1), hot)

# ---- background vignette ----
c.circle(34, 30, 30, "#0e0b07")
c.circle(33, 29, 23, "#151009")
c.circle(33, 29, 17, "#1c150b")

# ---- chain ----
for (x, y) in [(45,10),(48,8),(51,6),(54,5),(57,5),(60,6),(61,8),(60,10),(63,12),(63,15),(61,18)]:
    add_link(x, y)

# hanging chain (bottom-left, below lid)
for (x, y) in [(24,48),(24,52),(23,56),(22,60)]:
    add_link(x, y)
c.circle(23, 62, 1, gold[7])
c.set(24, 61, gold[8])
c.set(22, 63, gold[5])

# hanging chain (bottom-right, below movement)
for (x, y) in [(57,47),(58,50),(59,53),(59,56),(58,59)]:
    add_link(x, y)
c.set(57, 62, gold[6])
c.set(58, 61, gold[8])
c.set(59, 63, gold[4])

# ---- lid (open) ----
metal_disc(16, 33, 13.5, gold, rim=0.42)
metal_disc(16, 33, 11.8, gold[1:], rim=0.34)
ring_circle(16, 33, 8.6, gold[0], 0.2)
ring_circle(16, 33, 8.3, gold[7], 0.2)
ring_circle(16, 33, 1.5, gold[5], 0.3)
c.circle(16, 33, 3.0, gold[8])
c.circle(16, 32, 2.0, gold[3])
c.set(15, 31, hot)
for a in (-40, 120, 250):
    ga = math.radians(a)
    c.circle(P(16 + math.cos(ga) * 8.4), P(33 + math.sin(ga) * 8.4), 1, gold[6])
    c.set(P(16 + math.cos(ga) * 8.4), P(33 + math.sin(ga) * 8.4), gold[2])
c.line(8, 21, 19, 32, gold[8])
c.line(7, 22, 18, 33, gold[9])
c.set(7, 23, gold[8])
c.set(6, 24, gold[7])

# ---- hinge ----
for y in range(24, 41):
    c.rect(29, y, 3, 1, gold[6] if y % 3 == 1 else gold[3])
for y in (26, 30, 34, 38):
    c.circle(31, y, 1, gold[8])
    c.set(30, y, gold[1])

# ---- watch movement ----
metal_disc(44, 33, 13.5, gold, rim=0.42)
c.circle(44, 33, 10.2, hole)
ring_circle(44, 33, 10.4, gold[2], 0.18)
gear(38, 28, 5.5, 9, rot=0.25)
gear(47, 36, 4.5, 8, rot=0.55)
gear(42, 40, 3.0, 7, rot=1.0)
gear(51, 29, 2.4, 6, rot=1.1)

# ---- dial ----
annulus(44, 33, 10.5, 12.2, cream)
ring_circle(44, 33, 10.6, gold[2], 0.2)
ring_circle(44, 33, 12.1, gold[4], 0.2)
for i in range(12):
    a = math.radians(-90 + i * 30)
    ca = math.cos(a); sa = math.sin(a)
    x0 = 44 + ca * 10.8; y0 = 33 + sa * 10.8
    x1 = 44 + ca * 12.0; y1 = 33 + sa * 12.0
    c.line(P(x0), P(y0), P(x1), P(y1), tk)
    if i % 3 == 0:
        pa = -sa; pb = ca
        c.line(P(x0 + pa * 0.5), P(y0 + pb * 0.5), P(x1 + pa * 0.5), P(y1 + pb * 0.5), tk)

# ---- hands ----
hand(44, 33, -62, 6.8, 1.8)
hand(44, 33, -54, 4.6, 2.2)
c.circle(44, 33, 2, gold[7])
c.circle(44, 33, 1, gold[2])
c.set(43, 32, hot)

# ---- glare / reflections ----
for a in (-125, -112, -99, -86, -73, -60):
    ga = math.radians(a)
    c.set(P(44 + math.cos(ga) * 6.6), P(33 + math.sin(ga) * 6.6), spec)
for a in (-118, -95, -72):
    c.set(P(44 + math.cos(math.radians(a)) * 7.8), P(33 + math.sin(math.radians(a)) * 7.8), hot)
for a in (-140, -118, -96, -72, -50):
    ga = math.radians(a)
    c.set(P(16 + math.cos(ga) * 12.8), P(33 + math.sin(ga) * 12.8), spec)
    c.set(P(44 + math.cos(ga) * 12.8), P(33 + math.sin(ga) * 12.8), spec)

# ---- crown ----
c.rect(42, 12, 7, 4, gold[5])
c.rect(42, 12, 7, 1, gold[9])
c.rect(42, 15, 7, 1, gold[3])
for x in (43, 45, 47):
    c.rect(x, 12, 1, 4, gold[6])
c.rect(43, 16, 3, 2, gold[4])
c.rect(43, 16, 3, 1, gold[7])
c.rect(44, 11, 3, 1, gold[7])
c.set(45, 11, hot)

print(c.stats_text())
print(c.matrix_text(region=(2, 2, 61, 47)))
finish(c)
