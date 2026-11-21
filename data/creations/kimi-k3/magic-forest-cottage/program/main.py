import random
from pixelbench_api import *

c = new_canvas(128, 128, '#140a24', name='magic-forest-cottage')
random.seed(11)

def rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def mix(a, b, t):
    A, B = rgb(a), rgb(b)
    return '#%02x%02x%02x' % tuple(round(A[i] + (B[i] - A[i]) * t) for i in range(3))

# ================= SKY =================
for y0, y1, col in [(0, 15, '#120920'), (15, 30, '#190d2f'), (30, 46, '#211239'),
                    (46, 62, '#2a1745'), (62, 80, '#341d50')]:
    c.rect(0, y0, 128, y1 - y0, col)
for a, b, y in [('#120920', '#190d2f', 15), ('#190d2f', '#211239', 30),
                ('#211239', '#2a1745', 46), ('#2a1745', '#341d50', 62)]:
    c.dither(0, y, 128, 3, [a, b], 'checker')

# stars
for i in range(70):
    x = random.randint(1, 126); y = random.randint(1, 58)
    if (x - 94) ** 2 + (y - 24) ** 2 < 441:
        continue
    c.set(x, y, random.choice(['#e9e2f7', '#cfc0ec', '#ffe9b0']))
for x, y in [(12, 8), (40, 18), (66, 10), (118, 44), (30, 40), (58, 34)]:
    for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        c.set(x + dx, y + dy, '#ffe9b0')

# ================= MOON =================
c.circle(94, 24, 16, mix('#f5e9c4', '#1a0e30', 0.86))
c.circle(94, 24, 14, mix('#f5e9c4', '#1a0e30', 0.72))
c.circle(94, 24, 12, mix('#f5e9c4', '#1a0e30', 0.52))
c.circle(94, 24, 11, '#f2e6bd')
c.circle(97, 28, 6, '#e6d5a8')           # lower-right shading
c.circle(95, 27, 3, '#e2d1a2')           # craters
c.circle(91, 30, 2, '#e2d1a2')
c.circle(98, 19, 2, '#e2d1a2')
c.set(88, 20, '#fbf2d2'); c.set(89, 19, '#fbf2d2'); c.set(90, 22, '#fbf2d2')

# ================= DISTANT TREELINE =================
x = 0
while x < 128:
    w = random.randint(6, 12); h = random.randint(4, 11)
    c.poly([(x, 84), (x + w // 2, 84 - h), (x + w, 84)], '#1c112e')
    x += w - 2

# background tree behind cottage (right of roof)
c.poly([(86, 68), (88, 50), (84, 40), (90, 30), (94, 42), (92, 68)], '#1c112e')
c.circle(90, 26, 7, '#3a1830'); c.circle(83, 33, 5, '#3a1830'); c.circle(97, 35, 4, '#3a1830')
c.circle(88, 24, 3, '#57223f'); c.circle(96, 33, 2, '#57223f')

# ================= GROUND =================
c.rect(0, 78, 128, 50, '#241a3a')
for i in range(9):
    x = random.randint(0, 118); y = random.randint(82, 122)
    w = random.randint(6, 16); h = random.randint(3, 8)
    c.dither(x, y, w, h, ['#241a3a', '#2b2146'], 'checker')
c.ellipse(100, 92, 18, 5, mix('#241a3a', '#8f86b0', 0.18))   # moonlit patch
c.ellipse(100, 90, 10, 3, mix('#241a3a', '#8f86b0', 0.10))
for i in range(60):
    c.set(random.randint(0, 127), random.randint(80, 127), '#3a2c57')

# horizon mist
m1 = mix('#a894cf', '#281a42', 0.28); m2 = mix('#a894cf', '#281a42', 0.15)
m3 = mix('#a894cf', '#281a42', 0.42)
c.ellipse(30, 74, 28, 3, m1); c.ellipse(88, 72, 26, 3, m1)
c.ellipse(58, 69, 30, 2, m2); c.ellipse(118, 78, 12, 2, m1)

# ================= COTTAGE =================
# chimney (roof covers its base)
c.rect(74, 32, 8, 18, '#5a5266')
c.line(74, 37, 81, 37, '#453e52'); c.line(74, 42, 81, 42, '#453e52'); c.line(74, 47, 81, 47, '#453e52')
c.set(77, 34, '#6f6880'); c.set(79, 40, '#6f6880'); c.set(76, 45, '#6f6880')
c.rect(72, 29, 10, 3, '#463f52')
c.rect(74, 29, 6, 1, '#17111f')
# smoke
s1 = mix('#c9bdd6', '#1a0e30', 0.45); s2 = mix('#c9bdd6', '#1a0e30', 0.7)
c.circle(78, 24, 3, s1); c.circle(83, 20, 2, s1); c.circle(88, 15, 2, s2); c.circle(92, 11, 1, s2)

# wood upper walls
c.rect(38, 68, 44, 16, '#5b3f2e')
for yy in (72, 76, 80):
    c.line(38, yy, 81, yy, '#493021')
c.rect(38, 68, 2, 16, '#3a261b'); c.rect(58, 68, 2, 16, '#3a261b'); c.rect(80, 68, 2, 16, '#3a261b')
# stone lower walls
c.rect(36, 84, 47, 16, '#615a70')
c.line(36, 89, 82, 89, '#4b4559'); c.line(36, 94, 82, 94, '#4b4559')
for vx, vy in [(44, 84), (58, 84), (72, 84), (50, 89), (66, 89), (42, 94), (60, 94), (76, 94)]:
    c.line(vx, vy, vx, vy + 4, '#4b4559')
for i in range(12):
    c.set(random.randint(37, 81), random.randint(85, 98), '#736c82')

# roof
c.poly([(24, 69), (58, 30), (94, 69)], '#33482e')
c.poly([(24, 69), (58, 30), (58, 69)], mix('#33482e', '#101c12', 0.4))
c.ellipse(40, 57, 6, 3, '#4c6c3b'); c.ellipse(72, 50, 7, 3, '#4c6c3b'); c.ellipse(52, 42, 4, 2, '#597a43')
c.ellipse(84, 61, 4, 2, '#597a43'); c.ellipse(30, 65, 4, 2, '#597a43'); c.ellipse(64, 63, 5, 2, '#4c6c3b')
for i in range(8):
    xx = random.randint(60, 90)
    ys = 30 + (xx - 58) * 39 / 36
    yy = int(ys) + random.randint(1, 4)
    if yy < 68:
        c.set(xx, yy, '#597a43')
c.line(24, 69, 58, 30, '#1d2c1a'); c.line(58, 30, 94, 69, '#1d2c1a'); c.line(24, 69, 94, 69, '#1d2c1a')
c.line(60, 33, 91, 66, mix('#f2e6bd', '#33482e', 0.30))   # moonlit rim on right slope
# hanging moss
c.line(28, 70, 28, 72, '#4c6c3b'); c.line(34, 70, 34, 71, '#597a43')
c.line(86, 70, 86, 72, '#4c6c3b'); c.line(91, 70, 91, 71, '#597a43')

# attic round window
c.circle(58, 52, 3, '#241a12'); c.circle(58, 52, 2, '#ff9d34')
c.line(56, 52, 60, 52, '#241a12'); c.line(58, 50, 58, 54, '#241a12')

# glowing windows
wg1 = mix('#5b3f2e', '#ff9d34', 0.45); wg2 = mix('#5b3f2e', '#ff9d34', 0.22)
sg2 = mix('#615a70', '#ff9d34', 0.22); sg1 = mix('#615a70', '#ff9d34', 0.45)
for x0 in (41, 66):
    y0, y1 = 72, 82; x1 = x0 + 9
    c.rect(x0, y0, 10, 11, '#241a12')
    c.rect(x0 + 1, y0 + 1, 8, 9, '#ff9d34')
    c.rect(x0 + 2, y0 + 2, 3, 3, '#ffd98a')
    c.line(x0 + 5, y0 + 1, x0 + 5, y1 - 1, '#241a12')
    c.line(x0 + 1, y0 + 5, x1 - 1, y0 + 5, '#241a12')
    c.line(x0 - 1, y0 - 1, x1 + 1, y0 - 1, wg1)
    c.line(x0 - 1, y0, x0 - 1, y1, wg1); c.line(x1 + 1, y0, x1 + 1, y1, wg1)
    c.line(x0 - 1, y1 + 1, x1 + 1, y1 + 1, wg1)
    c.line(x0 - 2, y0 - 2, x1 + 2, y0 - 2, wg2)
    c.line(x0 - 2, y0 - 1, x0 - 2, y1 + 1, wg2); c.line(x1 + 2, y0 - 1, x1 + 2, y1 + 1, wg2)
    c.line(x0 - 2, y1 + 2, x1 + 2, y1 + 2, sg2)

# door
c.rect(54, 84, 11, 16, '#241a12')
c.rect(55, 85, 9, 15, '#4a2d1d')
for xx in (57, 59, 61):
    c.line(xx, 85, xx, 99, '#372114')
c.set(55, 85, '#241a12'); c.set(63, 85, '#241a12')
c.rect(57, 87, 3, 4, '#ff9d34'); c.line(57, 89, 59, 89, '#372114'); c.set(58, 88, '#ffd98a')
c.set(62, 93, '#d9a44f')
c.line(53, 86, 53, 98, sg2); c.line(65, 86, 65, 98, sg2)

# lantern by the door
c.set(50, 85, '#241a12'); c.set(50, 86, '#241a12')
c.rect(49, 87, 4, 5, '#241a12'); c.rect(50, 88, 2, 3, '#ff9d34'); c.set(50, 88, '#ffd98a')
c.set(48, 88, sg1); c.set(53, 88, sg1); c.set(48, 90, sg1); c.set(53, 90, sg1)
c.set(50, 92, sg2); c.set(51, 92, sg2)

# warm light pools on the ground
p1 = mix('#241a3a', '#ff9d34', 0.35); p2 = mix('#241a3a', '#ff9d34', 0.18)
c.ellipse(58, 101, 17, 4, p2); c.ellipse(58, 101, 11, 3, p1)
c.ellipse(45, 100, 6, 2, p2); c.ellipse(71, 100, 6, 2, p2)

# ================= PATH =================
c.poly([(52, 100), (66, 100), (94, 128), (28, 128)], '#1f1732')
c.rect(53, 100, 12, 2, '#6f6880'); c.line(53, 100, 64, 100, '#857e98')

def slab(x, y, w, h, warm):
    c.rect(x, y, w, h, '#443e56')
    c.rect(x + 1, y + 1, w - 2, h - 2, mix('#6d6680', '#ff9d34', warm))
    c.line(x + 1, y + 1, x + w - 2, y + 1, '#857e98')

slab(55, 101, 6, 3, .25); slab(62, 101, 6, 3, .25)
slab(50, 105, 7, 3, .25); slab(59, 105, 7, 3, .18); slab(68, 105, 6, 3, .18)
slab(45, 110, 8, 4, .12); slab(55, 110, 9, 4, .12); slab(66, 110, 8, 4, .12)
slab(38, 116, 10, 5, .06); slab(50, 116, 11, 5, .06); slab(63, 116, 10, 5, .06); slab(75, 116, 9, 5, .06)
slab(32, 123, 12, 5, .03); slab(46, 123, 13, 5, .03); slab(61, 123, 12, 5, .03); slab(75, 123, 11, 5, .03)

# low mist wisps (trees and well drawn on top of these)
c.ellipse(14, 118, 16, 3, m1); c.ellipse(100, 117, 20, 3, m1)
c.ellipse(32, 108, 9, 2, m3); c.ellipse(96, 110, 10, 2, m1)

# ================= RIGHT TREE =================
c.poly([(128, 40), (118, 50), (112, 62), (116, 78), (110, 92), (114, 108), (112, 128), (128, 128)], '#2a1626')
c.line(118, 50, 112, 62, '#47263b'); c.line(112, 62, 116, 78, '#47263b'); c.line(110, 92, 114, 108, '#47263b')
c.line(119, 51, 113, 61, '#5b3550')
c.poly([(128, 26), (116, 32), (110, 30), (106, 33), (112, 35), (122, 34), (128, 34)], '#2a1626')
c.poly([(126, 52), (112, 58), (104, 56), (110, 62), (124, 62)], '#2a1626')
c.line(109, 33, 105, 29, '#2a1626'); c.line(106, 56, 100, 52, '#2a1626')

def cluster(cx, cy, r, base, acc):
    c.circle(cx, cy, r, base)
    c.circle(cx - r + 2, cy + 1, max(2, r - 3), base)
    c.circle(cx + r - 2, cy + 2, max(2, r - 3), base)
    c.circle(cx, cy - r + 2, max(2, r - 3), base)
    c.circle(cx - 1, cy - 1, max(1, r - 3), acc)
    for i in range(r * 2):
        dx = random.randint(-r, r); dy = random.randint(-r, 0)
        if dx * dx + dy * dy <= r * r and random.random() < 0.4:
            c.set(cx + dx, cy + dy, '#a64650')

cluster(118, 14, 9, '#4d1e38', '#6b2438')
cluster(124, 27, 7, '#6b2438', '#83303f')
cluster(110, 6, 4, '#4d1e38', '#83303f')
cluster(121, 40, 5, '#4d1e38', '#6b2438')

# ================= WELL =================
c.rect(91, 81, 3, 17, '#4c3426'); c.rect(107, 81, 3, 17, '#4c3426')
c.line(92, 82, 92, 96, '#5f4230'); c.line(108, 82, 108, 96, '#5f4230')
c.rect(89, 83, 20, 3, '#5d4030'); c.line(89, 83, 108, 83, '#70503a')
c.set(89, 84, '#3d2a1e'); c.set(108, 84, '#3d2a1e')
c.line(109, 85, 111, 87, '#70503a'); c.set(111, 88, '#3d2a1e')
c.rect(89, 97, 24, 11, '#615a70')
c.line(89, 101, 112, 101, '#4b4559'); c.line(89, 105, 112, 105, '#4b4559')
c.line(96, 97, 96, 100, '#4b4559'); c.line(104, 101, 104, 104, '#4b4559')
c.line(108, 97, 108, 100, '#4b4559'); c.line(93, 105, 93, 107, '#4b4559')
c.set(94, 98, '#736c82'); c.set(100, 103, '#736c82'); c.set(107, 106, '#736c82'); c.set(91, 104, '#736c82')
c.ellipse(101, 96, 13, 5, '#6f6880')
c.ellipse(101, 95, 8, 3, '#17111f')
c.line(92, 99, 110, 99, '#857e98')
c.set(95, 94, '#3d3450'); c.set(107, 95, '#3d3450')
c.line(101, 86, 101, 92, '#8a7350')          # rope
c.rect(98, 93, 7, 5, '#3f2b1f')              # bucket
c.line(98, 93, 104, 93, '#5d4030'); c.line(98, 95, 104, 95, '#2b2433'); c.set(99, 94, '#5f4230')

# ================= LEFT TREE =================
c.poly([(0, 128), (2, 100), (4, 80), (3, 62), (8, 48), (6, 38), (10, 32),
        (16, 40), (14, 52), (20, 64), (16, 80), (20, 96), (26, 128)], '#2a1626')
c.poly([(12, 52), (30, 42), (44, 40), (38, 48), (16, 60)], '#2a1626')
c.poly([(36, 44), (48, 34), (46, 44)], '#2a1626')
c.poly([(8, 40), (6, 24), (12, 18), (14, 30), (12, 42)], '#2a1626')
c.poly([(16, 68), (34, 60), (38, 64), (18, 74)], '#2a1626')
c.line(20, 96, 16, 80, '#47263b'); c.line(14, 52, 18, 62, '#47263b')
c.line(24, 122, 20, 100, '#47263b'); c.line(10, 48, 8, 60, '#47263b')
c.poly([(20, 126), (30, 122), (26, 128)], '#2a1626')

cluster(8, 16, 10, '#4d1e38', '#6b2438')
cluster(24, 10, 8, '#6b2438', '#83303f')
cluster(38, 20, 7, '#4d1e38', '#83303f')
cluster(48, 34, 6, '#6b2438', '#a64650')
cluster(4, 34, 6, '#6b2438', '#83303f')
cluster(28, 30, 5, '#83303f', '#a64650')
cluster(54, 44, 4, '#4d1e38', '#83303f')

# small bush between cottage and well
c.circle(85, 95, 4, '#33482e'); c.circle(88, 96, 3, '#33482e')
c.set(83, 93, '#4c6c3b'); c.set(86, 92, '#4c6c3b'); c.set(88, 94, '#597a43'); c.set(84, 95, '#a64650')

# falling leaves
for x, y in [(60, 58), (72, 86), (20, 90), (100, 62), (86, 44), (44, 96), (108, 66)]:
    c.set(x, y, '#83303f')

# ================= MUSHROOMS & FIREFLIES =================
c.rect(30, 110, 1, 2, '#c9b59a'); c.rect(29, 109, 3, 1, '#a83a44')
c.set(30, 108, '#a83a44'); c.set(29, 109, '#ffd98a')
c.rect(118, 112, 1, 2, '#c9b59a'); c.rect(117, 111, 3, 1, '#a83a44')
c.set(118, 110, '#a83a44'); c.set(119, 111, '#ffd98a')
c.rect(8, 112, 1, 1, '#c9b59a'); c.rect(7, 111, 3, 1, '#a83a44')

for x, y in [(36, 96), (70, 95), (90, 86), (22, 104), (112, 72), (60, 114),
             (98, 106), (14, 90), (48, 118), (80, 78), (104, 44), (30, 60)]:
    c.set(x, y, '#e6f487')

print(c.stats_text())
print('palette entries:', len(c.palette()))
view(c)
finish(c)
