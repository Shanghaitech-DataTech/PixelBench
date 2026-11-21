import random
random.seed(7)

# ---------- canvas ----------
c = new_canvas(128, 128, background='#232447', name='village')

# ---------- sky: 12-band sunrise gradient with dithered joins ----------
SKY = ['#232447', '#2e2b57', '#3d3265', '#52406e', '#6d4f74', '#8a5c74',
       '#a96a70', '#c97d66', '#e7945c', '#f7ad5e', '#ffc97a', '#ffe3a3']
y = 0
heights = [6, 6] + [5] * 10          # 62 px of sky
for i, col in enumerate(SKY):
    c.rect(0, y, 128, heights[i], col)
    y += heights[i]
y = 0
for i in range(len(SKY) - 1):
    y += heights[i]
    c.dither(0, y - 1, 128, 2, [SKY[i], SKY[i + 1]], pattern='bayer4')

# stars high in the sky (2x2 blocks, so no colour ever sits as a lone pixel)
for _ in range(9):
    sx, sy = random.randint(2, 123), random.randint(2, 10)
    c.set(sx, sy, '#fff3c4'); c.set(sx + 1, sy, '#fff3c4')
    c.set(sx, sy + 1, '#fff3c4'); c.set(sx + 1, sy + 1, '#fff3c4')
# star clusters near the sun glow
for sx, sy in [(50, 42), (76, 41)]:
    c.set(sx, sy, '#fff3c4'); c.set(sx + 1, sy, '#fff3c4')
    c.set(sx, sy + 1, '#ffe3a3'); c.set(sx + 1, sy + 1, '#ffe3a3')

# clouds: warm-lit thin streaks
def cloud(cx, cy, rx, ry, top, bot):
    c.ellipse(cx, cy, rx, ry, top)
    c.ellipse(cx, cy + ry, rx - 2, 1, bot)
cloud(28, 21, 14, 2, '#f2a182', '#ffc9a3')
cloud(100, 14, 11, 2, '#f2a182', '#ffc9a3')
cloud(72, 32, 9, 1, '#c97d66', '#f2a182')

# birds (compact chevrons, keep out of the star band)
for bx, by in [(46, 28), (86, 30)]:
    c.set(bx, by, '#232447'); c.set(bx + 1, by - 1, '#232447'); c.set(bx + 2, by, '#232447')

# ---------- sun (low, centered -> focal axis) ----------
c.circle(64, 49, 10, '#ffb95c')
c.circle(64, 49, 8, '#ffd166')
c.circle(64, 49, 5, '#fff3c4')

# ---------- mountain layers ----------
# far range (lightest, snow caps)
c.poly([(0, 50), (14, 42), (26, 47), (38, 37), (52, 46), (64, 50), (78, 47),
        (92, 38), (106, 46), (120, 43), (127, 47), (127, 62), (0, 62)], '#9678a8')
for px, py in [(14, 42), (38, 37), (92, 38), (120, 43)]:
    c.poly([(px, py), (px - 4, py + 4), (px + 4, py + 4)], '#ffd9c9')
# mid range
c.poly([(0, 58), (18, 50), (34, 56), (50, 49), (66, 57), (84, 50), (100, 56),
        (116, 51), (127, 55), (127, 70), (0, 70)], '#6d5285')
# foothills
c.poly([(0, 66), (22, 62), (44, 66), (64, 63), (88, 66), (110, 62),
        (127, 65), (127, 76), (0, 76)], '#41566b')

# ---------- ground ----------
c.rect(0, 70, 128, 58, '#4e7a44')
c.rect(0, 70, 128, 7, '#476f3e')
c.dither(0, 75, 128, 3, ['#476f3e', '#4e7a44'], pattern='bayer4')
c.rect(0, 114, 128, 14, '#3f6738')
c.dither(0, 111, 128, 3, ['#4e7a44', '#3f6738'], pattern='bayer4')
# sunlit patch around focal axis
c.ellipse(64, 104, 26, 10, '#7a9a4a')
c.ellipse(64, 103, 15, 6, '#87a853')

# distant tree row on the foothill line
for tx in [6, 15, 25, 35, 45, 84, 94, 104, 113, 122]:
    h = random.randint(5, 8)
    c.poly([(tx, 71 - h), (tx - 3, 71), (tx + 3, 71)], '#2f3f54')

# long morning shadows
c.poly([(20, 101), (41, 101), (48, 105), (8, 107)], '#355a30')
c.poly([(90, 103), (111, 103), (124, 108), (94, 107)], '#355a30')
c.poly([(52, 97), (59, 97), (54, 103), (44, 103)], '#355a30')
c.poly([(69, 97), (76, 97), (84, 103), (74, 103)], '#355a30')
c.ellipse(10, 114, 9, 2, '#355a30')
c.ellipse(122, 116, 9, 2, '#355a30')

# ---------- stone path (leads to main house door) ----------
c.poly([(60, 96), (68, 96), (82, 127), (46, 127)], '#57534c')
c.poly([(61, 96), (67, 96), (78, 127), (50, 127)], '#76726b')
for yv, n, rx, ry in [(100, 2, 1, 1), (105, 2, 1, 1), (111, 3, 2, 1),
                      (118, 3, 2, 2), (125, 3, 3, 2)]:
    hw = 3 + (yv - 96) * 0.28
    for i in range(n):
        fx = 64 - hw + 2 * hw * (i + 0.5) / n + random.uniform(-0.5, 0.5)
        col = '#8f8b82' if (i + yv) % 2 == 0 else '#a5a097'
        c.ellipse(int(fx), yv, rx, ry, col)
        if rx >= 2:
            c.set(int(fx) - 1, yv - 1, '#bdb7ab')

# fences along the path
posts_l, posts_r = [], []
for t in [0.22, 0.5, 0.8]:
    yv = int(100 + t * 26)
    off = 3 + (yv - 96) * 0.28 + 3
    for sgn, posts in ((-1, posts_l), (1, posts_r)):
        px = int(64 + sgn * off)
        c.rect(px, yv - 5, 2, 5, '#5a3d28')
        posts.append((px + 1, yv - 4))
for posts in (posts_l, posts_r):
    for a, b in zip(posts, posts[1:]):
        c.line(a[0], a[1] + 1, b[0], b[1] + 1, '#5a3d28')

# ---------- houses ----------
def window(x, y, s=5):
    c.rect(x - 1, y - 1, s + 2, s + 2, '#4a2c1a')
    c.rect(x, y, s, s, '#ffd75e')
    m = x + s // 2
    c.line(m, y, m, y + s - 1, '#4a2c1a')
    c.line(x, y + s // 2, x + s - 1, y + s // 2, '#4a2c1a')
    c.set(x, y, '#ffedb0'); c.set(m + 1, y, '#ffedb0')

# left house
c.rect(20, 84, 21, 17, '#96683f')
c.rect(20, 84, 3, 17, '#7c5133')
c.rect(20, 99, 21, 2, '#7c5133')
c.poly([(16, 86), (30, 73), (44, 86)], '#6e4634')
c.line(30, 73, 44, 85, '#b05a3a')
c.rect(24, 67, 3, 11, '#5d3a2e')
c.rect(23, 66, 5, 2, '#4a2c1a')
window(23, 89, 4)
c.rect(32, 89, 7, 12, '#4a2c1a'); c.rect(33, 90, 5, 11, '#5a3520')

# right house
c.rect(90, 86, 21, 17, '#96683f')
c.rect(90, 86, 2, 17, '#a9734a')
c.rect(108, 86, 3, 17, '#7c5133')
c.rect(90, 101, 21, 2, '#7c5133')
c.poly([(86, 88), (100, 75), (114, 88)], '#5d3a2e')
c.line(100, 75, 86, 87, '#8a3f2e')
c.rect(104, 69, 3, 11, '#6e4634')
c.rect(103, 68, 5, 2, '#4a2c1a')
window(93, 91, 4)
c.rect(102, 91, 7, 12, '#4a2c1a'); c.rect(103, 92, 5, 11, '#5a3520')

# main house (center, largest, brightest windows = focal point)
c.rect(52, 78, 25, 19, '#a9734a')
c.rect(52, 78, 3, 19, '#7c5133')
c.rect(74, 78, 3, 19, '#c08a50')
c.rect(52, 95, 25, 2, '#7c5133')
c.poly([(48, 80), (64, 64), (80, 80)], '#8a3f2e')
c.line(64, 64, 80, 79, '#b05a3a')
c.line(48, 79, 64, 64, '#6e4634')
c.rect(70, 59, 4, 12, '#6e4634')
c.rect(69, 58, 6, 2, '#4a2c1a')
window(55, 84); window(69, 84)
c.rect(60, 86, 8, 11, '#4a2c1a'); c.rect(61, 87, 6, 10, '#5a3520')
c.set(65, 91, '#ffd75e')
c.set(62, 98, '#e8c85a'); c.set(66, 98, '#e8c85a')   # warm light spill

# ---------- pine trees ----------
def pine(cx, yb, h, sun_right=True):
    tk = max(2, h // 8)
    c.ellipse(cx, yb, 4, 1, '#355a30')
    c.rect(cx - 1, yb - tk, 2, tk, '#5a3d28')
    top = yb - h
    layers = max(3, min(6, h // 8))
    sgn = 1 if sun_right else -1
    for i in range(layers):
        y0 = top + i * (h - tk) // layers
        y1 = top + (i + 1) * (h - tk) // layers + 2
        half = int((i + 1.5) / layers * h * 0.30)
        c.poly([(cx, y0), (cx - half, y1), (cx + half, y1)], '#1f4a32')
        if sun_right:
            c.poly([(cx, y0), (cx, y1), (cx + half, y1)], '#2e6b40')
        else:
            c.poly([(cx, y0), (cx - half, y1), (cx, y1)], '#2e6b40')
        c.line(cx, y0, cx + sgn * half, y1, '#47904c')
        for px in range(cx - half + 1, cx + half, 3):
            c.set(px, y1 + 1, '#1f4a32')
        if h >= 30 and y1 + 2 < 128:
            c.set(cx + sgn * (half - 1), y1, '#c9854e')
            c.set(cx + sgn * (half - 2), y1, '#c9854e')

pine(45, 94, 16, True)
pine(83, 95, 17, False)
pine(27, 86, 9, True)
pine(101, 88, 9, False)
pine(10, 112, 46, True)      # big foreground left
pine(122, 114, 40, False)    # big foreground right

# ---------- bushes, flowers, grass ----------
c.circle(30, 116, 3, '#35683a'); c.circle(35, 120, 2, '#35683a')
c.circle(99, 118, 3, '#35683a'); c.circle(94, 122, 2, '#35683a')
for bx, by in [(29, 114), (31, 115), (35, 119), (98, 116), (100, 117), (94, 120)]:
    c.set(bx, by, '#47904c')
for fx, fy in [(28, 113), (37, 121), (96, 120), (93, 124), (50, 110), (78, 112)]:
    c.set(fx, fy, '#e8c85a'); c.set(fx + 1, fy, '#e8c85a')
for i in range(20):
    x = random.randint(2, 124); yy = random.randint(82, 124)
    if 42 < x < 86 and yy > 92:
        continue
    col = '#355a30' if (x + yy) % 2 == 0 else '#87a853'
    c.set(x, yy, col); c.set(x + 1, yy - 1, col)

# ---------- chimney smoke (last, over sky) ----------
def smoke(x, y):
    seq = [(0, 0, 1, '#b3a6a8'), (1, -4, 1, '#b3a6a8'), (2, -8, 2, '#cfc0b8'),
           (4, -13, 2, '#cfc0b8'), (6, -19, 2, '#e8ded2'), (8, -25, 3, '#e8ded2')]
    for dx, dy, r, col in seq:
        c.circle(x + dx, y + dy, r, col)
smoke(72, 56)
smoke(25, 64)
smoke(105, 66)

# ---------- outliner pass: no visible colour may survive as a lone pixel ----------
_flat = c.px                     # live flat list of palette indices, row-major
W = H = 128
import collections as _cl

def lone_count(f):
    n = 0
    for yy in range(H):
        for xx in range(W):
            v = f[yy * W + xx]
            if v < 0:
                continue
            if not any(0 <= xx + dx < W and 0 <= yy + dy < H and
                       f[(yy + dy) * W + xx + dx] == v
                       for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                n += 1
    return n

def clean(f):
    orig = list(f)
    n = 0
    for yy in range(H):
        base = yy * W
        for xx in range(W):
            v = orig[base + xx]
            if v < 0:
                continue
            if any(0 <= xx + dx < W and 0 <= yy + dy < H and
                   orig[(yy + dy) * W + xx + dx] == v
                   for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                continue
            n += 1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = xx + dx, yy + dy
                if 0 <= nx < W and 0 <= ny < H and orig[ny * W + nx] >= 0:
                    f[base + xx] = orig[ny * W + nx]
                    break
            else:
                f[base + xx] = -1
    return n

for _it in range(6):
    if clean(_flat) == 0:
        break
cnt = _cl.Counter(v for v in _flat if v >= 0)
print('lone pixels:', lone_count(_flat), '| visible colours:', len(cnt),
      '| iterations used:', _it + 1)

view(c)
finish(c)
