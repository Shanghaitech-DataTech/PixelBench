import random
random.seed(7)

out = input_canvas.copy(name="output")
pal = {p['index']: p['rgba'] for p in out.palette()}

def warm(x, y):
    r, g, b, a = pal[out.get(x, y)]
    return r > b + 25 and r > 60

# ---------------------------------------------------------------- 1. rebuild vending machine
BODY = '#1e1a53'; FRAME = '#251e5b'; EDGE = '#16133d'
WHITE = '#fceae3'; WARMW = '#f1e2d9'; SHELF = '#858e8f'; SHELF2 = '#6e757e'
RIM = '#ba90c2'; RIM2 = '#b591bd'

X0, X1 = 83, 109          # region occluded by the character
out.rect(X0, 56, X1 - X0 + 1, 62, BODY)      # y 56..117
out.rect(X0, 56, 3, 62, FRAME)               # left frame pillar
out.set(X0 - 0, 56, EDGE)

# glass window
out.rect(86, 58, X1 - 86 + 1, 46, WHITE)     # y 58..103
out.rect(86, 58, X1 - 86 + 1, 1, RIM)
out.rect(86, 103, X1 - 86 + 1, 1, RIM2)
for x in range(86, X1 + 1):
    out.set(86, 58 + (x - x), RIM)
out.rect(86, 58, 1, 46, RIM2)                # left glass rim

# shelves
for sy in (65, 76, 88, 100):
    out.rect(86, sy, X1 - 86 + 1, 1, SHELF)
    out.rect(86, sy + 1, X1 - 86 + 1, 1, SHELF2)

# stocked bottles / cans in each compartment
BOT = ['#a570db', '#75d47c', '#c36a38', '#75bfd0', '#c42f0f', '#605ce4', '#f7b28b']
comps = [(59, 64), (67, 75), (78, 87), (90, 99)]
ci = 0
for (ty, by) in comps:
    x = 88
    while x <= X1 - 2:
        col = BOT[ci % len(BOT)]; ci += 1
        h = by - ty + 1
        bh = max(3, h - 2)
        y0 = by - bh + 1
        out.rect(x, y0, 3, bh, col)
        out.rect(x, y0, 1, bh, '#ffeae3')          # specular edge
        out.set(x + 2, y0, col)
        if bh >= 5:
            out.rect(x, y0, 3, 1, '#e8e5d3')
        x += 5

# lower front: dispensing flap and coin slot
out.rect(87, 106, 22, 12, EDGE)
out.rect(87, 106, 22, 1, FRAME)
out.rect(89, 108, 18, 8, '#122634')
out.rect(89, 108, 18, 1, '#35275e')
out.rect(103, 96, 5, 1, FRAME)

# ---------------------------------------------------------------- 2. inpaint leftover character pixels
targets = [(x, y) for y in range(104, 150) for x in range(80, 122) if warm(x, y)]
targets += [(x, y) for y in range(56, 104) for x in range(76, 83) if warm(x, y)]
tset = set(targets)
for (x, y) in targets:
    src = None
    for d in range(1, 30):
        for (nx, ny) in ((x, y + d), (x, y - d), (x + d, y), (x - d, y)):
            if 0 <= nx < 170 and 0 <= ny < 170 and (nx, ny) not in tset and not warm(nx, ny):
                r, g, b, a = pal[out.get(nx, ny)]
                if r < 90 and b < 110:
                    src = (r, g, b, a); break
        if src: break
    out.set(x, y, src or '#122634')

# ---------------------------------------------------------------- 3. lightning in the background
BOLT = '#eef6ff'; BOLT2 = '#bcd8f5'

def bolt(pts, w=1):
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i + 1]
        out.line(x0, y0, x1, y1, BOLT)
        if w > 1:
            out.line(x0 + 1, y0, x1 + 1, y1, BOLT2)

glow = new_canvas(170, 170, name='glow')
main_bolt = [(36, 2), (33, 14), (39, 22), (31, 36), (38, 47), (32, 60), (37, 74), (30, 88), (34, 100), (28, 118), (31, 132)]
branch = [(31, 36), (22, 45), (25, 55), (17, 68)]
branch2 = [(32, 60), (44, 72), (40, 82), (49, 96)]
far = [(150, 6), (146, 18), (152, 28), (145, 44), (149, 58), (143, 72)]

for pts in (main_bolt, branch, branch2, far):
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i + 1]
        glow.line(x0, y0, x1, y1, '#9fc6f0aa')
for rad, col in ((5, '#79a6d426'), (3, '#9cc4ef3c')):
    for pts in (main_bolt, far):
        for (x, y) in pts:
            glow.circle(x, y, rad, col)
out = flatten([out, glow], name='output')

bolt(main_bolt, 2); bolt(branch); bolt(branch2); bolt(far)

# ---------------------------------------------------------------- 4. rain (semi-transparent droplets)
rain = new_canvas(170, 170, name='rain')
for _ in range(900):
    x = random.randint(-4, 172); y = random.randint(0, 169)
    L = random.choice([2, 2, 3, 3, 4, 5])
    a = random.choice(['55', '66', '77', '8c', 'a0'])
    col = random.choice(['#c8dcf2', '#aac4e0', '#dce9fa']) + a
    rain.line(x, y, x - 1, y + L, col)
    if L >= 4:
        rain.set(x - 1, y + L + 1, '#e4f0ff' + a)
for _ in range(90):   # fat foreground droplets
    x = random.randint(0, 169); y = random.randint(0, 169)
    rain.rect(x, y, 1, 2, '#dcecffb4')
    rain.set(x - 1, y + 2, '#dcecff8c')
out = flatten([out, rain], name='output')

# ---------------------------------------------------------------- 5. wet ground with clinging droplets
def rgb_at(c, x, y):
    n = c.color_name(c.get(x, y))
    if not n.startswith('#'):
        return (0, 0, 0, 255)
    n = n[1:]
    if len(n) == 3:
        n = ''.join(ch * 2 for ch in n)
    v = [int(n[i:i + 2], 16) for i in range(0, min(8, len(n)), 2)]
    while len(v) < 4:
        v.append(255)
    return tuple(v)

def ground_top(x):
    for y in range(138, 170):
        r, g, b, a = rgb_at(out, x, y)
        if r > b + 8 and r > 45:
            return y
    return 150

sheen = new_canvas(170, 170, name='sheen')
for x in range(170):
    gt = ground_top(x)
    for y in range(gt, 170):
        t = (y - gt) / max(1.0, 169 - gt)
        if random.random() < 0.30 + 0.25 * t:
            sheen.set(x, y, random.choice(['#6a8aa83c', '#8fb0c84b', '#4d6c8a55']))
# puddles reflecting the lightning
for (px, py, rx, ry) in ((38, 158, 14, 4), (96, 164, 20, 5), (140, 152, 11, 3), (66, 150, 8, 2)):
    sheen.ellipse(px, py, rx, ry, '#7ea4c88c')
    sheen.ellipse(px, py, max(1, rx - 4), max(1, ry - 1), '#a7c8e8a0')
    sheen.rect(px - 1, py - ry, 2, ry * 2, '#e2f0ffa0')
out = flatten([out, sheen], name='output')

# clinging droplets / splash beads on the ground
pal2 = None
for _ in range(260):
    x = random.randint(0, 169); y = random.randint(140, 169)
    r, g, b, a = rgb_at(out, x, y)
    if b > r + 40:
        continue
    out.set(x, y, random.choice(['#cfe3f5', '#aac6dd', '#e8f3ff']))
    if random.random() < 0.3:
        out.set(x, y + 1, '#52708c')
for _ in range(70):   # splash rings
    x = random.randint(0, 169); y = random.randint(144, 168)
    out.set(x - 1, y, '#bcd6ec'); out.set(x + 1, y, '#bcd6ec')
    out.set(x, y - 1, '#e8f3ff')

view(out)
finish(out)
