import math
from pixelbench_api import *

W, H = 256, 256

# ---------------------------------------------------------------------------
# palette registration (on the background canvas, which shares the drawing palette)
bg = new_canvas(W, H, background=None, name='bg')

def hexcol(s):
    return bg.color(s)

# background gradient stops
def _lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))

TOP = (7, 16, 9)
BOT = (19, 35, 24)
BG_STOPS = [_lerp(TOP, BOT, i / 11.0) for i in range(12)]

TREE_SIL = '#0d1710'
GROUND = '#182619'
GROUND_DARK = '#0f1a12'

RAY_BRIGHT = '#f2f7c855'   # alpha 0x55 = 85
RAY_DIM    = '#d4e6a03c'   # alpha 0x3c = 60

BARK_BASE   = '#4a3322'
BARK_DARK   = '#2c1f15'
BARK_DARKER = '#1e140d'
BARK_LIGHT  = '#6b4a30'
BARK_HL     = '#8f6a44'
OUTLINE     = '#0a0c0a'

MOSS1 = '#3d5c28'
MOSS2 = '#527d35'
MOSS3 = '#6d9c45'
MOSS4 = '#8fc05b'

VINE1 = '#334d1e'
VINE2 = '#47682a'

EYE_SOCKET = '#0a0c0a'
EYE_DIM    = '#2c8f38'
EYE_GLOW   = '#4fe23a'
EYE_CORE   = '#d9ffb0'

# ---------------------------------------------------------------------------
# background layer

# vertical atmospheric gradient (stylised hard bands, softened by dithering)
band = 22
for i in range(12):
    y0 = i * band
    y1 = min((i + 1) * band, H)
    bg.rect(0, y0, W, y1 - y0, BG_STOPS[i])
    # dither the boundary between bands with the two neighbouring stops
    if i < 11 and y1 < H:
        bg.dither(0, y1 - 1, W, 2, [BG_STOPS[i], BG_STOPS[i + 1]], pattern='checker')

# forest floor
bg.rect(0, 208, W, H - 208, GROUND)
bg.dither(0, 206, W, 4, [BG_STOPS[-1], GROUND], pattern='checker')
# darker soil patches
for gx, gw in [(20, 60), (120, 40), (196, 48)]:
    bg.rect(gx, 232, gw, 24, GROUND_DARK)
    bg.dither(gx, 230, gw, 3, [GROUND, GROUND_DARK], pattern='checker')

# dark forest silhouettes on both sides of the clearing
def side_tree(x, w, top=0, bottom=208):
    bg.rect(x, top, w, bottom - top, TREE_SIL)
    # small branch stubs
    bg.rect(x - 4, top + 26, w + 8, 5, TREE_SIL)
    bg.rect(x - 7, top + 60, w + 14, 6, TREE_SIL)
    bg.rect(x - 3, top + 120, w + 6, 5, TREE_SIL)
    bg.rect(x - 6, top + 164, w + 12, 6, TREE_SIL)

side_tree(8, 22)
side_tree(40, 9)
side_tree(208, 20)
side_tree(238, 8)

# top canopy, leaving a clearing gap above the treant's head
def canopy_poly(x0, x1):
    pts = [(x0, 0)]
    y = 0
    x = x0
    step = 18
    while x < x1:
        pts.append((x + step // 2, 10 + 9 * math.sin(x * 0.11)))
        pts.append((x + step, 0 + 7 * math.sin(x * 0.17 + 1.3)))
        x += step
    pts.append((x1, 0))
    pts.append((x1, 26))
    pts.append((x0, 26))
    bg.poly(pts, TREE_SIL)

canopy_poly(0, 94)
canopy_poly(162, 256)

# ---------------------------------------------------------------------------
# god rays layer
rays = new_canvas(W, H, background=None, name='rays')

def beam(topx, topw, botx, botw, colour):
    rays.poly([
        (topx - topw / 2, -4),
        (topx + topw / 2, -4),
        (botx + botw / 2, 238),
        (botx - botw / 2, 238),
    ], colour)

beam(128, 14, 128, 76, RAY_BRIGHT)
beam(108, 8, 74, 62, RAY_DIM)
beam(148, 8, 182, 62, RAY_DIM)
beam(90, 6, 36, 52, RAY_DIM)
beam(166, 6, 220, 52, RAY_DIM)

# ---------------------------------------------------------------------------
# treant layer
tr = new_canvas(W, H, background=None, name='treant')

# ---- gnarled trunk profile ----------------------------------------------
_keys = [
    (40, 9), (48, 15), (56, 22), (64, 26), (72, 25), (80, 23),
    (88, 22), (96, 24), (104, 27), (112, 30), (120, 29), (128, 28),
    (136, 29), (144, 31), (152, 33), (160, 35), (168, 37), (176, 40),
    (184, 43), (192, 46), (200, 49), (208, 52), (216, 53), (224, 54),
]

def radius(y):
    if y <= _keys[0][0]:
        return _keys[0][1]
    if y >= _keys[-1][0]:
        return _keys[-1][1]
    for (y0, r0), (y1, r1) in zip(_keys, _keys[1:]):
        if y0 <= y <= y1:
            t = (y - y0) / float(y1 - y0)
            return r0 + (r1 - r0) * t
    return 20.0

def pert_l(y):
    return 4.0 * math.sin(y / 6.0) + 2.5 * math.sin(y / 2.7 + 1.0)

def pert_r(y):
    return 4.0 * math.sin(y / 6.0 + 2.1) + 2.5 * math.sin(y / 2.3 + 0.4)

def left_edge(y):
    return 128 - (radius(y) + pert_l(y))

def right_edge(y):
    return 128 + (radius(y) + pert_r(y))

ys = list(range(40, 225, 2))
trunk_pts = [(128, 38)]
for y in ys:
    trunk_pts.append((left_edge(y), y))
trunk_pts.append((128 - 55, 224))
trunk_pts.append((128 + 55, 224))
for y in reversed(ys):
    trunk_pts.append((right_edge(y), y))
trunk_pts.append((128, 38))
tr.poly(trunk_pts, BARK_BASE)

# ---- tapered branch helper ----------------------------------------------
def tapered_branch(c, pts, widths, colour):
    left, right = [], []
    n = len(pts)
    for i, p in enumerate(pts):
        if n == 1:
            dx, dy = 1.0, 0.0
        elif i == 0:
            dx, dy = pts[1][0] - p[0], pts[1][1] - p[1]
        elif i == n - 1:
            dx, dy = p[0] - pts[-2][0], p[1] - pts[-2][1]
        else:
            dx, dy = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        w = widths[i] / 2.0
        left.append((p[0] + nx * w, p[1] + ny * w))
        right.append((p[0] - nx * w, p[1] - ny * w))
    c.poly(left + right[::-1], colour)

def mirror_pts(pts):
    return [(W - x, y) for (x, y) in pts]

# ---- roots rising from the base -----------------------------------------
roots = [
    ([(102, 218), (80, 234), (60, 248), (48, 252)], [18, 13, 9, 6]),
    ([(118, 222), (108, 240), (102, 252), (100, 256)], [17, 12, 8, 6]),
    ([(138, 222), (148, 240), (156, 252), (158, 256)], [17, 12, 8, 6]),
    ([(156, 218), (178, 234), (198, 248), (210, 252)], [18, 13, 9, 6]),
    ([(128, 224), (126, 244), (124, 256)], [16, 10, 6]),
]
for pts, wds in roots:
    tapered_branch(tr, pts, wds, BARK_BASE)

# ---- branch arms ----------------------------------------------------------
left_arm = [(102, 128), (76, 112), (52, 98), (38, 82), (28, 68)]
left_arm_w = [18, 14, 10, 8, 6]
tapered_branch(tr, left_arm, left_arm_w, BARK_BASE)
tapered_branch(tr, mirror_pts(left_arm), left_arm_w, BARK_BASE)

# claw-like twigs at the hands
left_claws = [
    ([(28, 68), (18, 56), (12, 46)], [5, 3, 2]),
    ([(28, 68), (16, 64), (8, 60)], [5, 3, 2]),
    ([(28, 68), (22, 52), (16, 42)], [5, 3, 2]),
    ([(28, 68), (24, 78), (20, 88)], [5, 3, 2]),
]
for pts, wds in left_claws:
    tapered_branch(tr, pts, wds, BARK_BASE)
    tapered_branch(tr, mirror_pts(pts), wds, BARK_BASE)

# ---- small crown branches at the top --------------------------------------
crown = [
    ([(128, 52), (128, 34), (126, 20)], [12, 8, 5]),
    ([(114, 54), (98, 42), (84, 32)], [10, 7, 5]),
    ([(142, 54), (158, 42), (172, 32)], [10, 7, 5]),
]
for pts, wds in crown:
    tapered_branch(tr, pts, wds, BARK_BASE)

# ---- bark texture: dark grooves -------------------------------------------
def wavy_line(c, x0, y0, y1, amp, phase, colour, n=18):
    d = f"M {x0} {y0}"
    for i in range(1, n + 1):
        y = y0 + (y1 - y0) * i / float(n)
        x = x0 + amp * math.sin(i * 2.0 * math.pi / (n * 0.62) + phase)
        d += f" L {x:.2f} {y:.2f}"
    c.path(d, colour, fill=False)

# centre grooves
for x0, ph in [(118, 0.0), (128, 2.1), (138, 4.2)]:
    wavy_line(tr, x0, 74, 196, 2.4, ph, BARK_DARK)
# short cracks
for x0, y0, y1, ph in [(122, 90, 150, 1.1), (134, 84, 138, 3.4), (124, 160, 210, 2.7)]:
    wavy_line(tr, x0, y0, y1, 1.6, ph, BARK_DARKER)

# light ridges near the silhouette edges
for y0, y1 in [(84, 192), (96, 200)]:
    pts = []
    for y in range(y0, y1, 3):
        pts.append((left_edge(y) + 4, y))
    if len(pts) >= 2:
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for (x, y) in pts)
        tr.path(d, BARK_LIGHT, fill=False)
    pts = []
    for y in range(y0, y1, 3):
        pts.append((right_edge(y) - 4, y))
    if len(pts) >= 2:
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for (x, y) in pts)
        tr.path(d, BARK_LIGHT, fill=False)

# bright highlight ticks on the upper left of the trunk
for y in range(86, 180, 9):
    x = left_edge(y) + 6
    tr.line(x, y, x + 3, y + 3, BARK_HL)

# extra gnarled grooves
for x0, ph in [(112, 1.4), (122, 3.0), (134, 4.6), (144, 0.8)]:
    wavy_line(tr, x0, 80, 200, 2.2, ph, BARK_DARK)

# knot holes (old wounds)
for kx, ky in [(120, 132), (136, 162), (117, 186)]:
    tr.circle(kx, ky, 3, BARK_DARKER)
    tr.circle(kx - 1, ky - 1, 1, BARK_HL)
    tr.line(kx - 4, ky, kx - 2, ky, BARK_DARK)
    tr.line(kx + 2, ky, kx + 4, ky, BARK_DARK)

# short horizontal bark cracks
for cy in range(96, 190, 14):
    tr.line(116, cy, 120, cy + 1, BARK_DARKER)
    tr.line(140, cy + 2, 144, cy + 1, BARK_DARKER)

# ---- glowing eyes ----------------------------------------------------------
for ex in (116, 140):
    tr.circle(ex, 72, 9, EYE_DIM)      # soft glow halo on the bark
    tr.circle(ex, 72, 7, EYE_SOCKET)
    tr.circle(ex, 72, 6, EYE_DIM)
    tr.circle(ex, 71, 4, EYE_GLOW)
    tr.circle(ex, 71, 2, EYE_CORE)

# ---- extra twigs sprouting from the arms ------------------------------------
for pts, wds in [
    ([(52, 98), (44, 86), (38, 78)], [5, 3, 2]),
    ([(76, 112), (70, 100), (66, 90)], [5, 3, 2]),
    ([(38, 82), (30, 74), (22, 68)], [5, 3, 2]),
]:
    tapered_branch(tr, pts, wds, BARK_BASE)
    tapered_branch(tr, mirror_pts(pts), wds, BARK_BASE)

# ---- moss clusters ----------------------------------------------------------
def moss_cluster(cx, cy, seed=0):
    tr.circle(cx, cy, 5, MOSS2)
    tr.circle(cx - 5, cy + 1, 4, MOSS1)
    tr.circle(cx + 5, cy + 1, 4, MOSS2)
    tr.circle(cx - 2, cy - 4, 3, MOSS3)
    tr.circle(cx + 3, cy - 3, 3, MOSS3)
    tr.circle(cx + 1, cy - 5, 2, MOSS4)

# top of head / crown
moss_cluster(128, 44)
moss_cluster(114, 50)
moss_cluster(142, 50)
moss_cluster(104, 58, 1)
moss_cluster(152, 58, 2)
# shoulders
moss_cluster(98, 112, 3)
moss_cluster(158, 112, 4)
# arm forks
moss_cluster(74, 112, 5)
moss_cluster(182, 112, 6)
moss_cluster(54, 100, 7)
moss_cluster(202, 100, 8)
# root shoulders
moss_cluster(94, 206, 9)
moss_cluster(162, 206, 10)
# trunk sides and arm midpoints
moss_cluster(110, 150, 11)
moss_cluster(146, 150, 12)
moss_cluster(86, 122, 13)
moss_cluster(170, 122, 14)
moss_cluster(48, 92, 15)
moss_cluster(208, 92, 16)
moss_cluster(104, 184, 17)
moss_cluster(152, 184, 18)

# ---- hanging vines ----------------------------------------------------------
def vine(c, x0, y0, length, colour=VINE1, leaf=VINE2):
    c.line(x0, y0, x0, y0 + length, colour)
    for i in range(1, length // 7):
        y = y0 + i * 7
        c.set(x0, y, colour)
        c.set(x0 - 1, y + 2, leaf)
        c.set(x0 + 1, y + 3, leaf)

# from arms
for sx, sy, ln in [(78, 118, 40), (60, 104, 34), (44, 88, 30), (34, 72, 22)]:
    vine(tr, sx, sy, ln)
    vine(tr, W - sx, sy, ln)
# from crown
for sx, sy, ln in [(110, 44, 22), (146, 44, 22)]:
    vine(tr, sx, sy, ln)

# ---- dark outline -----------------------------------------------------------
tr.outline(OUTLINE)

# ---------------------------------------------------------------------------
# composite everything: background, god rays, then the treant on top
result = flatten([bg, rays, tr], name='ancient-treant-boss')

print(result.stats_text())
print('visible colors:', result.stats()['colors_used'])

finish(result)
