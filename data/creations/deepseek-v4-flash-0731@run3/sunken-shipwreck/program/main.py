import math, random
from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H)
rng = random.Random(20240615)

def setp(x, y, col):
    if 0 <= x < W and 0 <= y < H:
        c.set(x, y, col)

# ---- palette ----
water = [(148,208,232),(112,180,215),(82,154,198),(58,128,178),(40,105,158),
         (28,85,136),(20,68,114),(16,54,94),(14,45,80),(12,38,68)]
s0=(224,206,158); s1=(202,182,134); s2=(178,158,114); s3=(148,130,94)
wl=(150,112,72); wm=(118,84,52); wd=(90,60,38); ww=(116,90,62)
cor1=(84,90,70); cor2=(106,114,82)
fb=(236,132,62); ft=(188,92,40); fe=(40,30,30)
bub=(226,242,252)
beam=(166,216,238)
ca=(240,116,130); cb=(196,76,96); ch=(252,176,184)
ga=(96,168,92); gd=(50,122,70)
star=(228,140,106)
cw=(122,80,44); gold=(230,192,66); gold2=(250,216,120)

# ---- water gradient ----
for y in range(H):
    col = water[min(9, y // 5)]
    for x in range(W):
        c.set(x, y, col)

def thick_line(x0, y0, x1, y1, w, col):
    n = int(max(abs(x1 - x0), abs(y1 - y0))) + 1
    for i in range(n + 1):
        x = round(x0 + (x1 - x0) * i / n)
        yy = round(y0 + (y1 - y0) * i / n)
        c.rect(x - w // 2, yy - w // 2, w, w, col)

# ---- light shafts ----
thick_line(11, 0, 23, 49, 3, beam)
thick_line(38, 0, 49, 49, 3, beam)
thick_line(29, 0, 35, 30, 2, beam)

# ---- hull mask ----
hull_poly = [(8,42),(9,35),(16,29),(30,26),(46,27),(56,32),(62,40),(61,48),(54,52),(35,53),(14,53),(10,50)]
def in_poly(px, py, poly):
    inside = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]; xj, yj = poly[j]
        if (yi > py) != (yj > py):
            if px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                inside = not inside
        j = i
    return inside
hull_mask = [[in_poly(x, y, hull_poly) for x in range(W)] for y in range(H)]

for y in range(H):
    for x in range(W):
        if hull_mask[y][x] and y < 49:
            c.set(x, y, wm)

# ---- broken mast ----
thick_line(35, 25, 21, 5, 3, wd)
setp(22, 3, wd); setp(19, 4, wd); setp(20, 6, wd)
thick_line(26, 10, 31, 13, 2, wd)   # broken yardarm stump

# ---- planks ----
for yy in [30, 33, 36, 39, 42, 45]:
    for x in range(40):
        if hull_mask[yy][x] and yy < 49:
            c.set(x, yy, wd)
for x in range(W):
    for yy in range(24, 49):
        if hull_mask[yy][x]:
            c.set(x, yy, wl)
            break

# ---- gaping holes / portholes ----
for (hx, hy, hr) in [(22, 39, 1), (35, 40, 2), (47, 41, 1)]:
    c.circle(hx, hy, hr, cor1)
    c.circle(hx, hy, max(0, hr - 1), (20,16,14))

# ---- corrosion ----
for k in range(16):
    x = rng.randint(12, 58); y = rng.randint(31, 47)
    if hull_mask[y][x]:
        col = cor1 if rng.random() < 0.55 else cor2
        c.set(x, y, col)
        if rng.random() < 0.65 and y + 1 < 49 and hull_mask[y + 1][x]:
            c.set(x, y + 1, col)
for k in range(7):
    x = rng.randint(14, 56); y = rng.randint(32, 44)
    if hull_mask[y][x]:
        for j in range(4):
            if y + j < 49 and hull_mask[y + j][x]:
                c.set(x, y + j, ww)

# ---- seabed ----
for y in range(49, H):
    base = s0 if y < 53 else (s1 if y < 57 else (s2 if y < 61 else s3))
    for x in range(W):
        c.set(x, y, base)
for y in range(49, H):
    for x in range(W):
        r = rng.random()
        if r < 0.10:
            c.set(x, y, s1 if y < 57 else s2)
        elif r < 0.16:
            c.set(x, y, s3)
for x in range(W):
    if hull_mask[49][x]:
        c.set(x, 49, s3)

# ---- seaweed ----
def seaweed(x, h, col):
    pat = [0, 1, 2, 1]
    for i in range(h):
        yy = 62 - i
        setp(x + pat[(i // 2) % 4], yy, col)
        setp(x + pat[(i // 2) % 4] + 1, yy, col)
seaweed(4, 18, ga)
seaweed(7, 13, gd)
seaweed(59, 15, ga)
seaweed(62, 19, gd)
seaweed(52, 9, gd)
seaweed(14, 8, ga)

# ---- coral ----
def coral(cx, cy, h):
    trunk_top = cy - h
    c.rect(cx, trunk_top, 3, h + 1, ca)
    c.rect(cx - 2, trunk_top + 3, 2, 3, cb)
    c.rect(cx + 3, trunk_top + 5, 2, 3, cb)
    c.circle(cx + 1, trunk_top + 2, 1, ch)
    c.circle(cx + 4, trunk_top + 6, 0, ch)
    c.circle(cx - 1, trunk_top + 2, 1, ch)
coral(4, 63, 15)
coral(59, 62, 12)
coral(49, 63, 9)

# ---- starfish ----
def starfish(cx, cy, col):
    for dx, dy in [(0,0),(-2,0),(2,0),(0,-2),(0,2),(-1,-1),(1,-1),(-1,1),(1,1)]:
        setp(cx + dx, cy + dy, col)
starfish(30, 56, star)
starfish(18, 60, star)

# ---- treasure chest spilling gold ----
c.rect(49, 50, 9, 5, cw)          # body
c.rect(50, 49, 7, 2, gold)        # open lid
c.rect(51, 50, 2, 5, wd)          # strap
c.rect(55, 50, 2, 5, wd)          # strap
setp(48, 49, gold2); setp(48, 50, gold); setp(57, 50, gold)
setp(58, 49, gold2); setp(47, 51, gold); setp(49, 53, gold2)

# ---- fish ----
def fish(x, y, body, tail, eyec):
    setp(x - 1, y, tail)
    for dx, dy in [(0, 0), (1, -1), (1, 0), (1, 1), (2, 0)]:
        setp(x + dx, y + dy, body)
    setp(x + 3, y, eyec)
for i in range(16):
    t = i / 15
    x = 5 + int(t * 47)
    y = 21 + int(4.2 * math.sin(t * math.pi * 2.0)) + rng.randint(0, 1)
    fish(x, y, fb, ft, fe)
for i in range(7):
    x = 34 + int(i * 2.6)
    y = 13 + int(2.2 * math.sin(i * 0.9)) + rng.randint(0, 1)
    fish(x, y, fb, ft, fe)
for (fx, fy) in [(23, 34), (31, 32), (40, 30)]:
    fish(fx, fy, fb, ft, fe)

# ---- bubbles ----
for (bx, by) in [(26,38),(27,33),(26,28),(28,24),(27,19),(29,15),(28,11),(37,33),(36,27),(38,22),(37,17),(39,13),(44,20),(33,10)]:
    setp(bx, by, bub)
c.circle(27, 24, 1, bub)
c.circle(37, 22, 1, bub)

# ---- diagnostics ----
keys = [('.', (60,120,170)), ('~', (150,200,225)), ('S', (200,180,130)), ('#', (150,130,95)),
       ('H', (120,85,55)), ('h', (90,60,38)), ('C', (220,100,115)), ('F', (235,130,60)),
       ('G', (75,140,75)), ('o', (226,242,252)), ('*', (230,192,66)), ('!', (228,140,106))]
pal = c.palette()
def nearest(rgba):
    best = keys[0]; bd = 1e9
    for ch, krgb in keys:
        d = (rgba[0]-krgb[0])**2 + (rgba[1]-krgb[1])**2 + (rgba[2]-krgb[2])**2
        if d < bd:
            bd = d; best = ch
    return best
lines = []
for y in range(H):
    row = []
    for x in range(W):
        idx = c.get(x, y)
        rgba = pal[idx]['rgba']
        row.append(nearest(rgba))
    lines.append(''.join(row))
print("\n".join(lines))
print(c.stats_text())

print("--- exact check: left rows 44-50 x0-14 ---")
for y in range(44, 51):
    print(y, [pal[c.get(x, y)]['rgba'] for x in range(0, 14)])
print("--- chest rows 48-54 x45-60 ---")
for y in range(48, 55):
    print(y, [pal[c.get(x, y)]['rgba'] for x in range(45, 61)])
print("--- top edge rows 24-35 x10-50 step2 ---")
for y in range(24, 36):
    print(y, [pal[c.get(x, y)]['rgba'] for x in range(10, 52, 2)])
print("palette size:", len(pal))

finish(c)
