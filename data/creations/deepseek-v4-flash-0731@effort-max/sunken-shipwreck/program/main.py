import math
from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

def h2(a, b):
    x = (a * 374761393 + b * 668265263) & 0xffffffff
    x = ((x ^ (x >> 13)) * 1274126177) & 0xffffffff
    return ((x ^ (x >> 16)) & 0xffffffff) / 4294967295.0

def inside_poly(px, py, poly):
    n = len(poly); j = n - 1; ins = False
    for i in range(n):
        xi, yi = poly[i]; xj, yj = poly[j]
        if (yi > py) != (yj > py):
            if px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                ins = not ins
        j = i
    return ins

def put(x, y, col):
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, col)

def fill_poly(q, col):
    xs = [p[0] for p in q]; ys = [p[1] for p in q]
    for y in range(max(0, min(ys)), min(64, max(ys)) + 1):
        for x in range(max(0, min(xs)), min(64, max(xs)) + 1):
            if inside_poly(x, y, q):
                put(x, y, col)

# --- water: vertical depth gradient ---
WATER = ["#5eaad6", "#4d99cb", "#3d88c0", "#3179b6", "#286cac", "#2261a4",
         "#1e589c", "#1a5095", "#18498e", "#164389", "#143d83", "#12377d",
         "#113278", "#0f2e73", "#0e2a6e", "#0c2669"]
for y in range(64):
    for x in range(64):
        put(x, y, WATER[y // 4])

# --- god rays: soft two-tone light bands ---
fill_poly([(10, 0), (26, 0), (42, 62), (2, 62)], "#bfdcec")
fill_poly([(13, 0), (23, 0), (36, 58), (8, 58)], "#d6eafa")
fill_poly([(30, 0), (45, 0), (62, 58), (44, 62)], "#b0d0e4")
fill_poly([(33, 0), (42, 0), (57, 54), (47, 54)], "#cde4f4")
fill_poly([(49, 0), (60, 0), (63, 36), (56, 58)], "#cfe6f2")
fill_poly([(51, 0), (58, 0), (60, 34), (55, 56)], "#e2f2fb")

# --- ship hull silhouette (bow up-right, stern buried at left) ---
P = [(16, 40), (34, 26), (50, 16), (57, 38), (42, 48), (22, 53)]

# --- hull body: longitudinal planks, weathering, rust, algae ---
for y in range(12, 56):
    for x in range(6, 60):
        if inside_poly(x, y, P):
            d = (y - 40) + 0.7059 * (x - 16)
            if d < 0:
                d = 0.0
            i = int(d // 3)
            col = ["#6e4a2a", "#7e5630", "#8e6238", "#a07044", "#8e6238", "#7e5630"][min(5, i)]
            r = h2(x, y); r3 = h2(x // 3, y // 3)
            if r3 < 0.045:
                col = "#9a4c24"
            elif r3 < 0.10:
                col = "#b45c2c"
            elif r3 > 0.955:
                col = "#3e8044"
            if r < 0.02:
                col = "#c8703c"
            if d < 1.3:
                col = "#b07a4c"
            put(x, y, col)

# --- ribs ---
for t in (0.15, 0.32, 0.49, 0.66, 0.83):
    bx = 16 + 32 * t; by = 40 - 24 * t
    for k in range(13):
        px = bx + 0.567 * k; py = by + 0.825 * k
        for ox in (0, 1):
            ix = round(px + ox); iy = round(py)
            if inside_poly(ix, iy, P):
                put(ix, iy, "#5e3a20")

# --- jagged gash in the side ---
G = [(26, 26), (33, 21), (39, 24), (41, 31), (35, 36), (28, 34), (24, 31)]
c.poly(G, "#b45c2c", fill=False)
for y in range(21, 37):
    for x in range(24, 42):
        if inside_poly(x, y, G):
            put(x, y, "#141a36" if h2(x, y) < 0.45 else "#0a0d24")
for (sx, sy) in [(25, 27), (28, 22), (27, 21), (38, 23), (40, 27), (41, 30), (35, 33), (28, 33)]:
    if inside_poly(sx, sy, P):
        put(sx, sy, "#c8905e")

# --- portholes ---
for (cx_, cy_) in [(44, 27), (46, 26)]:
    c.circle(cx_, cy_, 2, "#b45c2c", fill=False)
    c.circle(cx_, cy_, 1, "#0a0d24")
for bx in range(40, 50):
    for by in range(23, 31):
        if (bx - 44) ** 2 + (by - 27) ** 2 == 4 or (bx - 46) ** 2 + (by - 26) ** 2 == 4:
            put(bx, by, "#b45c2c")

# --- broken mast, rigging, broken bowsprit ---
c.line(38, 21, 35, 8, "#5e3a20"); c.line(39, 21, 36, 8, "#5e3a20")
c.set(35, 8, "#c8905e"); c.set(34, 7, "#c8905e"); c.set(36, 8, "#c8905e")
c.line(36, 9, 28, 13, "#5e3a20")
c.line(50, 15, 58, 7, "#5e3a20"); c.line(51, 15, 59, 8, "#5e3a20"); c.set(58, 7, "#c8905e")

# --- sand (drawn after the hull so the wreck looks half-buried) ---
SAND = ["#ddc28a", "#c7a86f", "#b08f56", "#99794a", "#82663e"]
for y in range(40, 64):
    for x in range(64):
        ty = 44 + int(3.5 * math.sin(x * 0.30) + 1.5 * math.sin(x * 0.11 + 2.1))
        if y < ty:
            continue
        col = SAND[min(4, (y - 46) // 4)]
        if y - ty <= 1:
            col = "#f0dcb0"
        if (x + int(2.0 * math.sin(y * 0.6))) % 7 == 0 and y > ty + 1:
            col = "#8a6e42"
        put(x, y, col)

# --- shadow cast on the sand under the hull ---
for y in range(48, 59):
    for x in range(12, 52):
        if ((x - 32) / 20) ** 2 + ((y - 53) / 5.5) ** 2 <= 1:
            put(x, y, "#4a5680" if ((x + y) % 2) else "#3d4770")

# --- seaweed swaying strands ---
def seaweed(x0, y0, hgt, ph):
    for i in range(1, hgt + 1):
        y = y0 - i
        x = x0 + int(2.2 * math.sin(i * 0.5 + ph))
        put(x, y, "#3a8a44" if (i // 2) % 2 == 0 else "#4a9c52")
        if x + 1 < 64:
            put(x + 1, y, "#4a9c52")

seaweed(3, 62, 18, 0.2)
seaweed(6, 61, 15, 1.4)
seaweed(9, 60, 12, 2.3)
seaweed(24, 58, 11, 0.5)
seaweed(28, 57, 9, 1.7)
seaweed(60, 61, 10, 1.0)
seaweed(63, 62, 12, 2.2)

# --- coral ---
for (x0, y0, x1, y1) in [(10, 59, 11, 47), (11, 58, 7, 43), (11, 50, 15, 46),
                        (11, 54, 15, 49), (11, 59, 14, 51), (11, 49, 9, 45)]:
    c.line(x0, y0, x1, y1, "#b04c5e")
for (cx_, cy_) in [(7, 43), (15, 46), (15, 51)]:
    c.circle(cx_, cy_, 1, "#e890a4")
for (cx_, cy_) in [(11, 44), (13, 47)]:
    c.circle(cx_, cy_, 1, "#d86074")
c.circle(10, 59, 2, "#b04c5e")
for (x0, y0, x1, y1) in [(53, 53, 53, 45), (52, 51, 56, 46), (55, 51, 58, 47)]:
    c.line(x0, y0, x1, y1, "#c05c28")
for (cx_, cy_) in [(53, 45), (56, 46), (58, 47)]:
    c.circle(cx_, cy_, 1, "#e88240")
c.circle(53, 52, 2, "#c05c28")

# --- starfish and shell on the sand ---
cx0, cy0 = 59, 56
pts = []
for k in range(10):
    rr = 4 if k % 2 == 0 else 1.8
    aa = k * math.pi / 5 - math.pi / 2
    pts.append((round(cx0 + rr * math.cos(aa)), round(cy0 + rr * math.sin(aa))))
c.poly(pts, "#e87a4c")
c.set(59, 53, "#7c3418"); c.set(62, 55, "#7c3418"); c.set(56, 55, "#7c3418")
c.poly([(34, 51), (37, 51), (36, 54)], "#f2d8b8")

# --- fish ---
def sfish(x, y):
    c.rect(x, y, 3, 2, "#e89a3c")
    c.set(x - 1, y, "#c87830"); c.set(x - 1, y + 1, "#c87830"); c.set(x + 2, y, "#5e3418")

def bfish(x, y):
    c.rect(x, y, 5, 3, "#e89a3c")
    c.set(x - 1, y, "#c87830"); c.set(x - 2, y + 1, "#c87830"); c.set(x + 4, y, "#5e3418")

for t in range(18):
    x = round(52 - 2.35 * t)
    y = round(10 + 4 * math.sin(t * 1.15) + 0.15 * t) + (1 if t % 2 else 0)
    sfish(x, y)
sfish(29, 26)
bfish(22, 32)

# --- bubbles and drifting particles ---
def bubble(x, y, r):
    for yy in range(y - r, y + r + 1):
        for xx in range(x - r, x + r + 1):
            if (xx - x) ** 2 + (yy - y) ** 2 <= r * r:
                put(xx, yy, "#cfe7f5")

for (bx_, by_, br_) in [(46, 13, 2), (50, 9, 1), (38, 7, 1), (55, 17, 1),
                       (30, 10, 1), (17, 20, 1), (12, 26, 1)]:
    bubble(bx_, by_, br_)
for k in range(12):
    put(int(h2(k, 3) * 62) + 1, int(h2(k, 9) * 26) + 2, "#d9ecf8")

print(c.stats_text())
finish(c)
