from pixelbench_api import *
import random

out = input_canvas.copy(name='output')
out.clear()

def C(rgb, name=None):
    return out.color(rgb, name)

SKY_TOP = (6, 5, 16)
SKY_BOT = (30, 18, 44)
GLOW   = C((70, 12, 22), 'glow')
GLOW2  = C((100, 16, 28), 'glow2')
MOON_D = C((84, 12, 22), 'moon_d')
MOON_CR= C((130, 18, 32), 'moon_cr')
MOON   = C((190, 30, 42), 'moon')
MOON_L = C((255, 100, 90), 'moon_l')
CASTLE= C((9, 8, 16), 'castle')
CASTLE2=C((20, 16, 32), 'castle2')
GATE  = C((22, 8, 16), 'gate')
GATEA = C((120, 22, 30), 'gatea')
WIN   = C((255, 176, 62), 'win')
WIN2  = C((255, 92, 44), 'win2')
GROUND=C((12, 8, 19), 'ground')
FOG   = C((50, 30, 62), 'fog')
FOG2  = C((34, 20, 46), 'fog2')
STAR  = C((190, 198, 230), 'star')
BAT   = C((6, 4, 10), 'bat')

# --- sky gradient (2px bands) ---
for y in range(0, 128, 2):
    t = y / 127.0
    col = tuple(int(SKY_TOP[k] + (SKY_BOT[k] - SKY_TOP[k]) * t) for k in range(3))
    out.rect(0, y, 256, 2, col)

# --- stars ---
random.seed(42)
stars = []
for _ in range(46):
    x = random.randint(0, 255); y = random.randint(2, 96)
    stars.append((x, y))
for (x, y) in stars:
    out.set(x, y, STAR)
    if random.randint(0, 9) < 3:
        out.set(x + 1, y, STAR)

# --- hanging blood moon ---
out.circle(176, 66, 46, GLOW)
out.circle(176, 66, 42, GLOW2)
out.circle(176, 66, 36, MOON_D)
out.circle(173, 63, 32, MOON)          # crescent shading toward right/bottom
out.circle(160, 50, 3, MOON_L)
out.circle(167, 45, 2, MOON_L)
for (cx, cy, r) in [(166, 54, 5), (176, 47, 4), (158, 62, 4), (170, 58, 3), (162, 60, 2), (168, 64, 2)]:
    out.circle(cx, cy, r, MOON_CR)
# blood-red cloud streaks at the moon's flanks
for (sx, sy, sl) in [(128, 52, 18), (100, 60, 12), (222, 48, 16), (206, 86, 14)]:
    out.rect(sx, sy, sl, 3, MOON_D)
    out.rect(sx + 2, sy - 2, sl - 4, 2, C((60, 10, 18), 'streak'))

# --- horizon glow ---
out.rect(0, 96, 256, 14, C((46, 12, 26), 'hor'))
out.rect(148, 96, 40, 6, GLOW2)

# --- castle silhouette ---
def crenellated(x, y, w, h, tooth=4, color=CASTLE):
    out.rect(x, y + tooth, w, h - tooth, color)
    i = 0
    while i < w:
        out.rect(x + i, y, min(tooth, w - i), tooth, color)
        i += tooth * 2

def banner(tx, ty, dirn, color=C((120, 14, 26), 'banner')):
    if dirn > 0:
        out.poly([(tx, ty), (tx + 11, ty + 3), (tx, ty + 6)], color)
    else:
        out.poly([(tx, ty), (tx - 11, ty + 3), (tx, ty + 6)], color)

# flanking walls
crenellated(24, 96, 28, 16)
crenellated(204, 96, 28, 16)
# mid-left tower
out.rect(52, 80, 18, 32, CASTLE)
out.poly([(61, 60), (52, 84), (70, 84)], CASTLE)
# left tower
out.rect(72, 64, 22, 48, CASTLE)
out.poly([(83, 46), (72, 70), (94, 70)], CASTLE)
banner(84, 42, 1)
# keep
out.rect(100, 56, 56, 56, CASTLE)
for i in range(6):
    out.rect(100 + i * 10, 52, 6, 4, CASTLE)
out.rect(124, 42, 8, 16, CASTLE)
out.poly([(128, 22), (122, 48), (134, 48)], CASTLE)
out.poly([(128, 14), (126, 26), (130, 26)], CASTLE)
banner(129, 16, -1)
# right tower
out.rect(162, 64, 22, 48, CASTLE)
out.poly([(173, 46), (162, 70), (184, 70)], CASTLE)
banner(172, 42, 1)
# mid-right tower
out.rect(186, 80, 18, 32, CASTLE)
out.poly([(195, 60), (186, 84), (204, 84)], CASTLE)
# curtain walls
crenellated(70, 92, 6, 20)
crenellated(94, 80, 6, 32)
crenellated(156, 80, 6, 32)
crenellated(184, 92, 6, 20)

# --- arched gate ---
out.rect(120, 94, 12, 13, GATE)
out.poly([(120, 94), (126, 86), (132, 94)], GATE)
out.line(120, 94, 120, 107, GATEA)
out.line(131, 94, 131, 107, GATEA)
out.line(126, 86, 126, 90, GATEA)

# --- lit windows ---
out.rect(80, 78, 6, 10, WIN2); out.rect(80, 96, 6, 10, WIN)
out.rect(168, 78, 6, 10, WIN2); out.rect(168, 96, 6, 10, WIN)
out.rect(110, 68, 8, 10, WIN2); out.rect(138, 68, 8, 10, WIN2)
out.rect(124, 66, 8, 10, WIN)
out.rect(58, 88, 6, 8, WIN); out.rect(192, 88, 6, 8, WIN)
out.rect(35, 102, 8, 8, WIN2); out.rect(215, 102, 8, 8, WIN2)

# --- ground, fog, spike fence ---
out.rect(0, 108, 256, 20, GROUND)
out.rect(0, 108, 256, 4, FOG2)
out.rect(0, 112, 256, 16, FOG)
for x in range(6, 254, 10):
    out.poly([(x, 107), (x + 3, 98), (x + 6, 107)], CASTLE)

# --- dead trees (kept inside canvas) ---
def dead_tree(tx, ty, h, color=CASTLE2):
    out.line(tx, ty, tx, ty - h, color)
    out.line(tx, ty - h + 3, tx - 6, ty - h - 6, color)
    out.line(tx, ty - h + 5, tx + 6, ty - h - 7, color)
    out.line(tx - 6, ty - h - 6, tx - 3, ty - h - 11, color)
    out.line(tx + 6, ty - h - 7, tx + 8, ty - h - 12, color)

dead_tree(18, 116, 28)
dead_tree(240, 116, 26)
dead_tree(10, 118, 14)
dead_tree(247, 118, 14)

# --- bats crossing the moon ---
def bat(x, y, s=1.0, color=BAT):
    pts = [(x, y), (x - 6 * s, y - 3 * s), (x - 4 * s, y), (x - 2 * s, y - 1 * s),
           (x, y), (x + 2 * s, y - 1 * s), (x + 4 * s, y), (x + 6 * s, y - 3 * s), (x, y)]
    out.poly(pts, color)

bat(158, 78, 1.15)
bat(192, 72, 0.95)
bat(171, 52, 0.8)
bat(146, 56, 0.75)
bat(206, 84, 0.8)
bat(120, 34, 0.7)
bat(226, 56, 0.7)
bat(58, 30, 0.6)

print(out.stats_text())
checks = [(176,50),(176,66),(130,70),(158,70),(192,70),(120,100),(240,100),(20,110),(60,100)]
for (x,y) in checks:
    idx = out.get(x,y)
    print((x,y), out.palette()[idx]['rgba'], out.color_name(idx))
print("done")
