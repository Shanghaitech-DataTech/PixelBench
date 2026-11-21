import math, random
from pixelbench_api import new_canvas, finish, save

random.seed(20261107)
W = H = 128
c = new_canvas(W, H, None, name="magic-forest-cottage")

# ---------------- helpers ----------------
def clamp(v, a, b):
    return max(a, min(b, v))

def wispy(cx, cy, r, colour, soft=2.2, cap=1.0):
    """Ragged-edged soft disc, used for smoke / mist / glows."""
    for y in range(int(cy - r) - 1, int(cy + r) + 2):
        for x in range(int(cx - r) - 1, int(cx + r) + 2):
            if x < 0 or y < 0 or x >= W or y >= H:
                continue
            d = math.hypot(x - cx, y - cy)
            p = clamp((r - d) / soft, 0.0, 1.0)
            if cap < 1.0:
                p = min(cap, p)
            if p > 0 and random.random() < p:
                c.set(x, y, colour)

def mist_band(x0, x1, y, r, colour, soft=3.0, step=3, cap=1.0, skip=()):
    x = x0
    while x <= x1:
        if any(a <= x < b for a, b in zip(skip[::2], skip[1::2])):
            x += step
            continue
        wispy(x + random.uniform(-1.5, 1.5), y + random.uniform(-1.5, 1.5),
              max(1.5, r + random.uniform(-1.2, 1.2)), colour, soft, cap)
        x += step

def sprinkle(x0, y0, x1, y1, colour, p):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if random.random() < p:
                c.set(x, y, colour)

def tline(x0, y0, x1, y1, col, w=2):
    c.line(x0, y0, x1, y1, col)
    if w > 1:
        c.line(x0 + 1, y0, x1 + 1, y1, col)

def limb(pts, radii, col, wiggle=0.0):
    """Tapered, optionally twisting limb built as one closed polygon."""
    n = len(pts)
    L_, R_ = [], []
    for i, (x, y) in enumerate(pts):
        if i == 0:
            dx, dy = pts[1][0] - x, pts[1][1] - y
        elif i == n - 1:
            dx, dy = x - pts[i - 1][0], y - pts[i - 1][1]
        else:
            dx, dy = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        r = radii[i] + (wiggle * math.sin(i * 1.35) if wiggle else 0.0)
        L_.append((x + nx * r, y + ny * r))
        R_.append((x - nx * r, y - ny * r))
    c.poly(L_ + R_[::-1], col, fill=True)

LEAF = {'red':   ('#4a1f28', '#5f2833', '#7a3542'),
        'purple':('#3a2145', '#4c2b58', '#63386f'),
        'brown': ('#3c2a1e', '#4f382a', '#654836')}

def cluster(cx, cy, r, kind):
    """Leaf cluster, lit from the upper right (moon side)."""
    base, mid, light = LEAF[kind]
    c.circle(int(cx), int(cy), int(r), base)
    c.circle(int(cx + r * 0.18), int(cy - r * 0.22), max(1, int(r * 0.72)), mid)
    c.circle(int(cx + r * 0.34), int(cy - r * 0.38), max(1, int(r * 0.42)), light)
    for _ in range(int(r * r * 0.9)):
        a = random.random() * 6.28318
        rr = r * math.sqrt(random.random())
        x = int(cx + rr * math.cos(a))
        y = int(cy + rr * math.sin(a))
        if (x - cx) - (y - cy) > 0:
            c.set(x, y, light if random.random() < 0.45 else mid)
        else:
            c.set(x, y, base if random.random() < 0.6 else mid)

# ---------------- sky ----------------
SKY = ['#0a0618', '#120a26', '#1a1036', '#231645', '#2c1d54', '#362563', '#402d72']
B = [0, 14, 28, 42, 56, 70, 84, 96]
for i in range(7):
    c.rect(0, B[i], W, B[i + 1] - B[i], SKY[i])
for i in range(6):
    c.dither(0, B[i + 1] - 1, W, 2, [SKY[i], SKY[i + 1]], pattern='checker')

# stars
for _ in range(90):
    x = random.randint(0, 127)
    y = random.randint(0, 82)
    if math.hypot(x - 93, y - 25) < 21:
        continue
    if random.random() < 0.18:
        c.set(x, y, '#ffffff')
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            c.set(x + dx, y + dy, '#cbb8ff')
    else:
        c.set(x, y, '#cbb8ff' if random.random() < 0.7 else '#ffffff')

# ---------------- moon ----------------
MX, MY, MR = 93, 25, 11
c.circle(MX, MY, 19, '#2a1c4a')
c.circle(MX, MY, 17, '#35255c')
c.circle(MX, MY, 15, '#42306e')
c.circle(MX, MY, 13, '#4f3a80')
c.circle(MX, MY, MR, '#ffe9ae')
c.circle(MX, MY, MR - 2, '#fff6d8')
c.circle(89, 22, 2, '#ecd9a0')
c.circle(97, 28, 2, '#ecd9a0')
c.circle(93, 31, 1, '#ecd9a0')
c.circle(98, 20, 1, '#ecd9a0')
for _ in range(26):  # bright limb, upper right
    a = random.uniform(-1.9, 0.3)
    x = int(MX + (MR - 1) * math.cos(a))
    y = int(MY + (MR - 1) * math.sin(a))
    c.set(x, y, '#fffdf0')

# ---------------- ground ----------------
G_RIM, G1, G2, G3 = '#453074', '#2e2052', '#281c47', '#322456'
def ground_top(x):
    return 88 + round(1.6 * math.sin(x * 0.075) + 1.1 * math.sin(x * 0.21 + 1.3))

for x in range(W):
    t = ground_top(x)
    for y in range(t, H):
        if y < t + 2:
            col = G_RIM
        elif y < t + 3:
            col = G_RIM if random.random() < 0.5 else G1
        elif y < t + 15:
            col = G1
        elif y < t + 16:
            col = G1 if random.random() < 0.5 else G2
        elif y < t + 29:
            col = G2
        elif y < t + 30:
            col = G2 if random.random() < 0.5 else G3
        else:
            col = G3
        c.set(x, y, col)

# horizon mist (behind everything that stands on the ground)
mist_band(-4, 132, 87, 4, '#5a4390', soft=3.4, step=3)
mist_band(10, 120, 91, 3, '#6b53a0', soft=3.6, step=4)

# distant silhouette trees
DIST = '#1e1436'
def distant_tree(bx, h):
    by = ground_top(bx)
    c.rect(bx, by - h, 2, h, DIST)
    c.circle(bx, by - h, 4, DIST)
    c.circle(bx - 4, by - h + 4, 3, DIST)
    c.circle(bx + 4, by - h + 3, 3, DIST)
distant_tree(22, 15)
distant_tree(84, 12)
distant_tree(46, 11)

# ---------------- left ancient tree (behind cottage) ----------------
TRUNK_D, TRUNK_L = '#251a33', '#33244a'
limb([(12, 112), (13, 100), (14, 90), (16, 80), (18, 70), (19, 58), (20, 46)],
     [7, 6.2, 5.6, 5.0, 4.4, 3.8, 3.2], TRUNK_D, wiggle=0.9)
limb([(18, 72), (25, 64), (30, 56)], [3.0, 2.2, 1.5], TRUNK_D)
limb([(19, 60), (21, 50), (22, 42)], [2.6, 2.0, 1.4], TRUNK_D)
limb([(18, 64), (13, 54), (10, 46)], [2.6, 2.0, 1.4], TRUNK_D)
limb([(20, 50), (18, 40), (16, 32)], [2.2, 1.7, 1.2], TRUNK_D)
limb([(20, 48), (24, 38), (28, 30)], [2.2, 1.7, 1.2], TRUNK_D)
limb([(16, 70), (10, 62), (6, 56)], [2.4, 1.8, 1.2], TRUNK_D)
c.line(12, 108, 5, 113, TRUNK_D); c.line(13, 108, 6, 114, TRUNK_D)
c.line(13, 108, 20, 113, TRUNK_D); c.line(14, 108, 21, 114, TRUNK_D)
for x, y, r, k in [(30, 50, 9, 'red'), (22, 40, 10, 'purple'), (10, 44, 9, 'brown'),
                   (4, 54, 7, 'purple'), (16, 30, 9, 'red'), (28, 28, 8, 'purple'),
                   (4, 34, 7, 'brown'), (36, 38, 6, 'red'), (0, 44, 6, 'purple'),
                   (14, 20, 6, 'purple')]:
    cluster(x, y, r, k)

# ---------------- cottage ----------------
APEX = (54, 28)
for y in range(28, 76):
    hw = (y - 28) * 0.75
    x0 = int(round(54 - hw)); x1 = int(round(54 + hw))
    c.rect(x0, y, x1 - x0 + 1, 1, '#2a4a33')
    if (y - 28) % 6 == 5:
        c.rect(x0, y, x1 - x0 + 1, 1, '#1f3826')
    for _ in range(3):
        x = random.randint(x0, x1)
        if x >= 54 and random.random() < 0.7:
            c.set(x, y, '#3a6244')
        elif random.random() < 0.5:
            c.set(x, y, '#1f3826')
for y in range(28, 32):  # ridge cap
    hw = (y - 28) * 0.75
    a = int(round(54 - hw)) - 1; b = int(round(54 + hw)) + 1
    c.rect(a, y, b - a + 1, 1, '#4b7a52')
c.rect(int(round(54 - 34.5)), 74, int(round(2 * 34.5)) + 1, 2, '#16281c')  # shaded eave
c.rect(18, 76, 73, 2, '#2b1c14')                                          # fascia
for _ in range(46):                                                       # shaggy moss over edge
    x = random.randint(18, 90)
    if random.random() < 0.55:
        c.set(x, 76, '#2a4a33'); c.set(x, 77, '#1f3826')
    else:
        c.set(x, 77, '#2a4a33')

# wall
c.rect(32, 78, 45, 23, '#4a4059')
sprinkle(33, 79, 75, 92, '#554a66', 0.10)
sprinkle(33, 79, 75, 92, '#3c3449', 0.10)
c.rect(32, 78, 45, 2, '#3c3449')          # under-eave shadow
# stone base
c.rect(32, 93, 45, 8, '#565170')
for yy in (96, 99):
    c.rect(32, yy, 45, 1, '#332e47')
for xx in (38, 44, 50, 56, 62, 68):
    c.set(xx, 94, '#332e47'); c.set(xx, 95, '#332e47')
for xx in (35, 41, 47, 53, 59, 65, 71):
    c.set(xx, 97, '#332e47'); c.set(xx, 98, '#332e47')
for xx in (38, 44, 50, 56, 62, 68):
    c.set(xx, 100, '#332e47')
sprinkle(33, 94, 75, 100, '#6a6584', 0.12)
sprinkle(33, 94, 60, 100, '#3f3a56', 0.10)
# timber framing
c.rect(32, 78, 3, 15, '#3a2415')
c.rect(74, 78, 3, 15, '#3a2415')
c.rect(32, 92, 45, 1, '#3a2415')
sprinkle(33, 78, 75, 78, '#4a301d', 0.3)
c.line(35, 91, 43, 81, '#3a2415'); c.line(36, 91, 44, 81, '#3a2415')
c.line(73, 91, 65, 81, '#3a2415'); c.line(72, 91, 64, 81, '#3a2415')
c.set(74, 80, '#4a301d'); c.set(75, 82, '#4a301d'); c.set(76, 84, '#4a301d')

# windows (warm)
for wx in (36, 62):
    c.rect(wx, 80, 11, 11, '#241609')
    c.rect(wx + 1, 81, 9, 9, '#f08a2a')
    c.rect(wx + 2, 82, 7, 7, '#ffc45c')
    c.rect(wx + 3, 83, 5, 5, '#fff3c0')
    c.rect(wx + 5, 81, 1, 9, '#241609')
    c.rect(wx + 1, 85, 9, 1, '#241609')
    c.rect(wx - 1, 91, 13, 1, '#6a6584')
    c.rect(wx - 1, 92, 13, 1, '#3f3a56')
    sprinkle(wx, 93, wx + 11, 95, '#7a4a2a', 0.30)
    sprinkle(wx - 2, 79, wx + 12, 79, '#7a4a2a', 0.20)

# door
c.circle(54, 90, 6, '#33210f')
c.circle(54, 90, 5, '#4a2f1a')
c.rect(49, 90, 11, 11, '#4a2f1a')
c.rect(48, 90, 1, 11, '#33210f'); c.rect(60, 90, 1, 11, '#33210f')
c.rect(52, 88, 1, 13, '#33210f'); c.rect(57, 88, 1, 13, '#33210f')
sprinkle(57, 88, 59, 100, '#4a301d', 0.25)
c.set(58, 94, '#8a6b45'); c.set(57, 94, '#8a6b45')
c.rect(50, 100, 9, 1, '#ffc45c')

# chimney
c.rect(68, 36, 9, 22, '#565170')
c.rect(67, 34, 11, 3, '#3f3a56')
c.rect(68, 42, 9, 1, '#332e47'); c.rect(68, 49, 9, 1, '#332e47')
c.rect(68, 45, 1, 4, '#332e47'); c.rect(73, 50, 1, 4, '#332e47')
sprinkle(69, 36, 76, 56, '#6a6584', 0.18)
sprinkle(68, 36, 71, 56, '#3f3a56', 0.14)
# smoke
wispy(72, 31, 3, '#5c4f8a', 2.0)
wispy(75, 26, 4, '#6f61a0', 2.2)
wispy(78, 21, 5, '#8477b5', 2.6)
wispy(81, 15, 6, '#9a8ec9', 3.0)

# ---------------- right ancient tree (behind well) ----------------
limb([(126, 120), (125, 106), (124, 94), (123, 82), (122, 70), (120, 58), (119, 48)],
     [7, 6.5, 6.0, 5.5, 5.0, 4.5, 4.0], TRUNK_D, wiggle=0.9)
limb([(120, 58), (113, 48), (107, 40), (102, 34)], [3.0, 2.4, 1.8, 1.2], TRUNK_D)
limb([(120, 52), (116, 42), (112, 32)], [2.6, 2.0, 1.4], TRUNK_D)
limb([(120, 50), (122, 38), (123, 26), (124, 16)], [2.6, 2.0, 1.5, 1.0], TRUNK_D)
limb([(122, 74), (114, 64), (106, 56), (100, 50)], [3.0, 2.4, 1.8, 1.2], TRUNK_D)
c.line(126, 116, 119, 121, TRUNK_D); c.line(125, 116, 118, 122, TRUNK_D)
for x, y, r, k in [(100, 32, 7, 'purple'), (110, 24, 7, 'brown'), (120, 20, 8, 'purple'),
                   (127, 30, 7, 'red'), (124, 10, 6, 'red'), (112, 12, 6, 'purple'),
                   (118, 40, 8, 'purple'), (127, 44, 6, 'brown'), (100, 48, 6, 'red'),
                   (104, 16, 5, 'purple')]:
    cluster(x, y, r, k)
sprinkle(120, 50, 127, 110, TRUNK_L, 0.10)

# ---------------- well with wooden winch ----------------
c.ellipse(109, 98, 11, 10, '#565170')
c.ellipse(109, 90, 11, 4, '#6a6584')
c.ellipse(109, 90, 8, 2, '#120d22')
c.rect(99, 94, 21, 1, '#332e47')
c.rect(99, 100, 21, 1, '#332e47')
c.rect(99, 104, 21, 1, '#332e47')
for xx in (104, 114):
    c.set(xx, 95, '#332e47'); c.set(xx, 96, '#332e47')
for xx in (101, 109, 117):
    c.set(xx, 101, '#332e47'); c.set(xx, 102, '#332e47')
for xx in (105, 113):
    c.set(xx, 105, '#332e47'); c.set(xx, 106, '#332e47')
sprinkle(112, 92, 119, 106, '#6a6584', 0.20)
sprinkle(100, 96, 108, 107, '#3f3a56', 0.16)
c.ellipse(109, 108, 12, 2, '#221740')
# winch
c.rect(101, 68, 3, 22, '#4a3020')
c.rect(115, 68, 3, 22, '#4a3020')
c.rect(103, 68, 1, 22, '#5f4028'); c.rect(117, 68, 1, 22, '#5f4028')
c.rect(99, 66, 23, 3, '#4a3020')
c.rect(106, 65, 8, 5, '#5f4028')
c.rect(106, 67, 8, 1, '#3a2415')
c.line(121, 67, 125, 62, '#4a3020'); c.line(122, 67, 126, 62, '#4a3020')
c.set(126, 61, '#8a6b45'); c.set(125, 61, '#8a6b45')
c.rect(109, 70, 1, 13, '#8a6b45')
c.rect(105, 82, 9, 2, '#5f4028')
c.rect(106, 84, 7, 5, '#3a2a1c')
c.rect(106, 86, 7, 1, '#4a3020')
# little roof over the winch
c.poly([(109, 50), (121, 64), (97, 64)], '#2b1c14', fill=True)
c.rect(97, 64, 25, 2, '#2b1c14')
for y in range(50, 64):
    hw = (y - 50) * 12.0 / 14.0
    a = int(round(109 - hw)); b = int(round(109 + hw))
    if random.random() < 0.7:
        c.set(b, y, '#2a4a33')
    if random.random() < 0.4:
        c.set(a + 1, y, '#1f3826')
c.set(109, 50, '#4b7a52'); c.set(108, 51, '#4b7a52'); c.set(110, 51, '#4b7a52')

# ---------------- stone-slab path ----------------
slabs = [(54, 101, 5, '#8a6a4e'), (55, 105, 6, '#7a5c44'), (57, 109, 7, '#8a6a4e'),
         (60, 113, 8, '#6b6078'), (64, 117, 9, '#5e546c'), (69, 120, 10, '#6b6078'),
         (75, 123, 11, '#544b66'), (82, 126, 12, '#4a4260')]
for cx, cy, hw, col in slabs:
    c.poly([(cx - hw, cy), (cx + hw, cy), (cx + hw + 1, cy + 3), (cx - hw - 1, cy + 3)],
           col, fill=True)
    c.rect(cx - hw, cy, 2 * hw + 1, 1, '#9c8a6a' if cy < 112 else '#7d7390')
    c.rect(cx - hw - 1, cy + 3, 2 * hw + 3, 1, '#241a38')
    for _ in range(3):
        c.set(cx + random.randint(-hw, hw), cy + random.randint(0, 2),
              '#9c8a6a' if random.random() < 0.4 else '#241a38')
# warm light spilling from door and windows onto the ground
sprinkle(47, 101, 63, 106, '#7a4a2a', 0.35)
sprinkle(49, 101, 61, 104, '#8a6a4e', 0.25)
sprinkle(33, 101, 47, 104, '#7a4a2a', 0.16)
sprinkle(61, 101, 75, 104, '#7a4a2a', 0.16)

# ---------------- ground detail ----------------
GSET = {c.color(G1), c.color(G2), c.color(G3), c.color(G_RIM)}
def on_ground(x, y):
    return 0 <= x < W and 0 <= y < H and c.get(x, y) in GSET
for _ in range(200):
    x = random.randint(0, 127); y = random.randint(90, 127)
    if not on_ground(x, y):
        continue
    r = random.random()
    if r < 0.45:
        h = random.randint(1, 3)
        for k in range(h):
            c.set(x, y - k, '#3c2b63' if k == h - 1 else '#2e2052')
    elif r < 0.7:
        c.set(x, y, '#3c2b63')
    else:
        c.set(x, y, '#221740')

# ---------------- foreground mist ----------------
mist_band(-4, 44, 100, 4, '#6b53a0', soft=3.4, step=4, cap=0.30)
mist_band(88, 132, 103, 4, '#6b53a0', soft=3.4, step=4, cap=0.30)
mist_band(30, 100, 121, 5, '#7d66b5', soft=4.2, step=5, cap=0.42, skip=range(52, 94))
mist_band(-4, 30, 112, 4, '#6b53a0', soft=3.8, step=4, cap=0.30)

# ---------------- glowing mushrooms ----------------
def mushroom(x, y, s=1):
    wispy(x, y - 1, 2.6 + s, '#2f7d8f', 3.0)
    c.rect(x, y, 1, 2, '#8ce8ec')
    c.rect(x - 1, y - 1, 3, 1, '#49c2d4')
    c.set(x - 1, y - 2, '#49c2d4'); c.set(x + 1, y - 2, '#49c2d4')
    c.set(x, y - 2, '#8ce8ec')
mushroom(16, 106)
mushroom(20, 109)
mushroom(94, 112)
mushroom(124, 108)

# ---------------- fireflies ----------------
for fx, fy in [(44, 74), (70, 76), (90, 84), (30, 92), (100, 76), (120, 92),
               (60, 70), (84, 66), (12, 78), (110, 60)]:
    c.set(fx, fy, '#ffe08a')
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if random.random() < 0.8:
            c.set(fx + dx, fy + dy, '#c9a45a')

# ---------------- foreground framing foliage ----------------
for x, y, r, k in [(2, 120, 9, 'purple'), (10, 126, 8, 'red'), (0, 108, 7, 'brown'),
                   (120, 124, 8, 'purple'), (127, 116, 7, 'red'), (112, 127, 6, 'brown')]:
    cluster(x, y, r, 'purple' if k == 'red' else k)
for x, y, r, k in [(6, 100, 6, 'purple'), (14, 112, 7, 'red'), (124, 104, 6, 'purple')]:
    cluster(x, y, r, k)

print(c.stats_text())
print('palette size:', len(c.palette()))
save('magic-forest-cottage', c)
finish(c)
