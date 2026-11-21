from pixelbench_api import *
import math

c = new_canvas(48, 48, name="polar_researcher")

# ==================== palette ====================
OUT    = '#151c2c'   # outline / darkest
PK_L   = '#f58a55'   # parka light
PK_M   = '#dc5a30'   # parka mid
PK_D   = '#a83a21'   # parka dark
PK_X   = '#7a2a18'   # parka deepest
FUR_L  = '#fbf2dc'
FUR_M  = '#dfcba5'
FUR_D  = '#a9906a'
MASK   = '#39425a'   # balaclava
MASK_L = '#5b6784'
SKIN   = '#eab88d'
SKIN_D = '#bd8560'
PANT_L = '#51658a'
PANT_M = '#3b4c68'
PANT_D = '#28344a'
BOOT_L = '#4a5060'
BOOT_M = '#31353f'
BOOT_D = '#1e2129'
MITT_L = '#59677a'
MITT_M = '#3b4655'
MITT_D = '#252c38'
GOG_F  = '#26374b'   # goggle frame
GOG_L  = '#9ad4f0'   # pale blue lens
GOG_M  = '#63a3c9'
GOG_H  = '#e8f8ff'   # reflection
CASE_L = '#f2c255'
CASE_M = '#d29a2e'
CASE_D = '#96651c'
MET_L  = '#d6dfe9'
MET_M  = '#9aa6b4'
MET_D  = '#6b7684'
SCF_L  = '#5cc7b6'
SCF_M  = '#31998c'
SCF_D  = '#1f6d64'
ICE    = '#cfe4f4'
SNOW   = '#eef7fd'
GLASS  = '#bfe6f7'

# ==================== helpers ====================
def limb(p0, p1, w0, w1):
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    def o(p, w):
        return (int(round(p[0] + nx * w / 2.0)), int(round(p[1] + ny * w / 2.0)))
    return [o(p0, w0), o(p1, w1), o(p1, -w1), o(p0, -w0)]

def shp(pts, dx=0, dy=0):
    return [(x + dx, y + dy) for x, y in pts]

def draw_shape(kind, args, col, dx=0, dy=0):
    if kind == 'poly':
        c.poly(shp(args, dx, dy), col, fill=True)
    elif kind == 'ell':
        cx, cy, rx, ry = args
        c.ellipse(cx + dx, cy + dy, rx, ry, col, fill=True)
    elif kind == 'rect':
        x, y, w, h = args
        c.rect(x + dx, y + dy, w, h, col, fill=True)

def render(shapes, outline=OUT):
    """All outlines first (8-way dilation), then all fills in list order."""
    if outline is not None:
        for kind, args, col in shapes:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    draw_shape(kind, args, outline, dx, dy)
    for kind, args, col in shapes:
        draw_shape(kind, args, col)

def P(pts, col):   return ('poly', pts, col)
def E(cx, cy, rx, ry, col): return ('ell', (cx, cy, rx, ry), col)
def R(x, y, w, h, col):     return ('rect', (x, y, w, h), col)
def L(p0, p1, w0, w1, col): return ('poly', limb(p0, p1, w0, w1), col)

def px(x, y, col):
    if 0 <= x < 48 and 0 <= y < 48:
        c.set(x, y, col)

def hline(x0, x1, y, col):
    for x in range(min(x0, x1), max(x0, x1) + 1):
        px(x, y, col)

def vline(x, y0, y1, col):
    for y in range(min(y0, y1), max(y0, y1) + 1):
        px(x, y, col)

# ==================== wind streaks + snow (back) ====================
streaks = [
    (1, 4, 8), (11, 3, 16), (0, 8, 5), (8, 8, 12), (2, 12, 7),
    (0, 16, 6), (1, 20, 5), (0, 25, 4), (1, 31, 5), (0, 36, 4),
    (2, 42, 8), (0, 45, 5),
    (40, 5, 46), (42, 9, 47), (41, 14, 46), (43, 19, 47), (44, 24, 47),
]
for x0, y, x1 in streaks:
    hline(x0, x1, y, ICE)
    if (x1 - x0) > 4:
        hline(x0 + 1, x1 - 1, y, SNOW)

flecks = [(9, 6), (4, 10), (14, 15), (6, 18), (3, 28), (7, 34), (12, 39),
          (19, 5), (46, 12), (45, 22), (10, 44), (16, 9), (2, 22), (13, 25),
          (18, 45), (42, 27), (39, 8), (24, 3), (30, 1)]
for x, y in flecks:
    px(x, y, SNOW)

# ==================== body union ====================
U = []
# coat tails flapping back into the wind
U.append(P([(26, 25), (17, 25), (10, 28), (6, 31), (9, 34), (17, 32), (26, 30)], PK_D))
U.append(P([(26, 30), (18, 32), (12, 35), (10, 39), (15, 40), (21, 37), (27, 34)], PK_X))
# scarf streaming back
U.append(P([(31, 18), (22, 15), (14, 16), (9, 19), (14, 22), (22, 21), (31, 22)], SCF_M))
U.append(P([(29, 21), (22, 23), (17, 26), (16, 29), (21, 28), (26, 25), (30, 23)], SCF_D))
# far arm + mitten
U.append(L((25, 24), (20, 29), 8, 7, PK_X))
U.append(P([(13, 29), (20, 28), (22, 32), (18, 35), (13, 33)], MITT_D))
# back leg + boot
U.append(L((26, 30), (21, 37), 10, 8, PANT_D))
U.append(L((21, 37), (18, 42), 8, 7, PANT_D))
U.append(P([(13, 41), (21, 41), (22, 44), (20, 46), (13, 46), (11, 43)], BOOT_D))
# front leg + boot
U.append(L((29, 31), (31, 37), 11, 9, PANT_M))
U.append(L((31, 37), (31, 42), 9, 8, PANT_M))
U.append(P([(25, 41), (35, 41), (37, 44), (35, 46), (25, 46), (23, 43)], BOOT_L))
# torso (leaning right, into the wind)
U.append(P([(28, 18), (37, 19), (39, 25), (36, 33), (23, 33), (20, 26), (23, 19)], PK_M))
# hood
U.append(E(32, 11, 8, 8, PK_M))
# near arm
U.append(L((35, 21), (40, 24), 9, 8, PK_L))
U.append(L((40, 24), (42, 27), 8, 7, PK_M))

render(U)

# ==================== sample case (in front) ====================
CASE = [
    R(35, 29, 12, 12, CASE_M),
]
render(CASE)
# handle
c.poly([(37, 29), (37, 26), (38, 25), (44, 25), (45, 26), (45, 29),
        (43, 29), (43, 27), (39, 27), (39, 29)], MET_D, fill=True)
# near mitten gripping the handle
MIT = [P([(38, 24), (45, 24), (46, 28), (44, 31), (39, 31), (37, 27)], MITT_L)]
render(MIT)

# ==================== internal shading / detail ====================
# --- parka torso shading: light from upper-right, wind-blown snow from left
c.poly([(20, 26), (23, 19), (28, 18), (27, 22), (23, 25), (22, 33), (20, 30)], PK_D, fill=True)
c.poly([(37, 19), (39, 25), (36, 33), (33, 33), (36, 25), (34, 20)], PK_L, fill=True)
# hem band
c.poly([(22, 31), (36, 31), (36, 33), (23, 33)], PK_X, fill=True)
# belt + buckle
hline(21, 37, 28, PK_X)
hline(21, 37, 29, PK_D)
c.rect(29, 27, 4, 4, MET_D, fill=True)
c.rect(30, 28, 2, 2, MET_L, fill=True)
# chest strap (harness)
for i in range(7):
    px(25 + i, 24 - i // 2, PK_X)
# zipper
for y in range(23, 31):
    px(34 - (y - 23) // 4, y, PK_D)
# pocket
c.poly([(28, 25), (33, 25), (33, 27), (28, 27)], PK_D, fill=True)
hline(28, 33, 25, PK_X)

# --- hood shell shading
c.ellipse(30, 13, 6, 6, PK_D, fill=True)
c.ellipse(33, 9, 5, 4, PK_M, fill=True)
c.ellipse(35, 7, 3, 2, PK_L, fill=True)
# snow load on the windward (left) top of the hood
for a in range(115, 200, 9):
    t = math.radians(a)
    px(int(round(32 + 7.4 * math.cos(t))), int(round(11 + 7.4 * math.sin(t))), SNOW)
hline(26, 30, 4, SNOW)
px(25, 5, SNOW); px(31, 4, ICE)

# --- fur ruff
c.ellipse(33, 12, 6, 6, FUR_M, fill=True)
c.ellipse(34, 11, 5, 5, FUR_L, fill=True)
c.ellipse(31, 14, 4, 4, FUR_M, fill=True)
c.ellipse(30, 15, 3, 3, FUR_D, fill=True)
# ragged fur tufts around the ruff
for a in range(0, 360, 18):
    t = math.radians(a)
    r = 6.6 + (1.1 if (a // 18) % 2 else 0.0)
    x = int(round(33 + r * math.cos(t)))
    y = int(round(12 + r * math.sin(t)))
    px(x, y, FUR_L if 200 < a < 360 else FUR_D)
    px(int(round(33 + (r - 1) * math.cos(t))), int(round(12 + (r - 1) * math.sin(t))), FUR_M)
# frost on the windward fur
for a in range(120, 215, 14):
    t = math.radians(a)
    px(int(round(33 + 5.6 * math.cos(t))), int(round(12 + 5.6 * math.sin(t))), SNOW)

# --- face opening (balaclava) ---
c.ellipse(34, 13, 4, 4, MASK, fill=True)
c.ellipse(35, 15, 3, 2, MASK_L, fill=True)
# small patch of skin: nose / cheek
px(36, 16, SKIN); px(37, 16, SKIN); px(36, 17, SKIN_D); px(35, 16, SKIN)

# --- goggles: pale blue reflections ---
c.poly([(28, 9), (36, 8), (38, 9), (39, 11), (38, 13), (36, 14), (29, 13), (27, 11)], GOG_F, fill=True)
c.poly([(29, 10), (35, 9), (37, 10), (38, 11), (37, 12), (35, 13), (30, 12), (28, 11)], GOG_L, fill=True)
c.poly([(29, 12), (37, 12), (35, 13), (30, 13)], GOG_M, fill=True)
# reflection streaks
for i in range(3):
    px(30 + i, 11 - i, GOG_H)
for i in range(3):
    px(33 + i, 11 - i, GOG_H)
px(36, 10, GOG_H); px(31, 12, GOG_M); px(34, 12, GOG_M)
# goggle strap over the hood
c.poly([(24, 9), (28, 10), (28, 12), (24, 11)], GOG_F, fill=True)
px(25, 10, MET_D); px(26, 11, MET_D)
# masked chin below the goggles
c.ellipse(34, 15, 3, 2, MASK, fill=True)
c.ellipse(35, 15, 2, 1, MASK_L, fill=True)
px(36, 15, SKIN); px(37, 15, SKIN); px(36, 16, SKIN_D); px(35, 16, SKIN)
hline(32, 36, 17, MASK)

# --- scarf around the neck (over torso, under hood ruff) ---
c.poly([(25, 19), (37, 19), (38, 22), (30, 24), (24, 22)], SCF_M, fill=True)
hline(26, 37, 19, SCF_L)
hline(25, 37, 20, SCF_L)
c.poly([(24, 22), (38, 22), (37, 23), (30, 24), (25, 23)], SCF_D, fill=True)
# knot
c.poly([(27, 20), (31, 20), (31, 23), (27, 23)], SCF_L, fill=True)
c.poly([(27, 22), (31, 22), (31, 23), (27, 23)], SCF_D, fill=True)

# --- legs ---
c.poly([(29, 32), (33, 32), (35, 37), (34, 42), (31, 42), (32, 37)], PANT_L, fill=True)
c.poly([(26, 32), (29, 32), (29, 37), (28, 42), (26, 42), (27, 37)], PANT_D, fill=True)
c.poly([(19, 37), (23, 37), (20, 42), (17, 42)], PANT_D, fill=True)
hline(17, 21, 40, PANT_D)
# gaiters / snow cuffs
hline(27, 34, 40, ICE); hline(27, 34, 41, SNOW)
hline(17, 21, 40, ICE)
# boots detail
hline(24, 36, 45, BOOT_D); hline(24, 36, 46, OUT)
hline(12, 21, 45, OUT); hline(12, 21, 46, OUT)
hline(25, 35, 42, BOOT_M)
hline(28, 33, 43, MET_D)
hline(14, 20, 42, BOOT_M)
# crampon spikes
for x in (25, 29, 33):
    px(x, 46, MET_M)
for x in (13, 17, 20):
    px(x, 46, MET_D)

# --- case detail ---
c.rect(35, 29, 12, 3, CASE_L, fill=True)          # lit top
vline(46, 29, 40, CASE_D)                          # right edge shade
c.rect(35, 37, 12, 4, CASE_D, fill=True)           # shaded bottom
c.rect(36, 30, 1, 10, CASE_L, fill=True)
hline(35, 46, 32, CASE_D); hline(35, 46, 33, OUT)  # lid seam
# latches
c.rect(37, 31, 2, 3, MET_L, fill=True); px(37, 33, MET_D)
c.rect(43, 31, 2, 3, MET_L, fill=True); px(43, 33, MET_D)
# label plate with sample vials
c.rect(38, 35, 7, 4, MET_M, fill=True)
c.rect(38, 35, 7, 1, MET_L, fill=True)
c.rect(39, 36, 2, 3, GLASS, fill=True); px(39, 36, GOG_L); px(39, 38, GOG_M)
c.rect(42, 36, 2, 3, GLASS, fill=True); px(42, 36, GOG_L); px(42, 38, GOG_M)
# corner bumpers
for (x, y) in [(35, 29), (46, 29), (35, 40), (46, 40)]:
    px(x, y, OUT)
# frost on the windward edge of the case
vline(35, 30, 36, ICE)
px(36, 34, SNOW); px(35, 38, SNOW)

# --- mitten detail (near hand) ---
hline(39, 44, 30, MITT_M)
px(41, 25, MITT_M); px(43, 25, MITT_M)
c.poly([(38, 24), (45, 24), (45, 26), (38, 26)], MITT_L, fill=True)
px(39, 27, MITT_D); px(41, 28, MITT_D); px(43, 27, MITT_D)
# thumb
c.poly([(37, 27), (39, 27), (39, 30), (37, 30)], MITT_M, fill=True)

# --- far mitten detail ---
c.poly([(14, 30), (20, 29), (21, 31), (15, 32)], MITT_M, fill=True)
hline(15, 20, 33, MITT_D)
px(14, 30, MITT_L); px(15, 30, MITT_L); px(13, 31, MITT_L)

# --- separation lines between overlapping masses ---
# coat hem over legs
hline(23, 36, 33, OUT)
hline(24, 35, 34, PK_X)
# front leg against back leg
c.line(25, 34, 23, 41, OUT)
# far arm against coat tail
c.poly([(23, 26), (25, 25), (22, 30), (20, 32)], OUT, fill=False)
# hood against torso
for x in range(26, 39):
    dy = int(round(11 + math.sqrt(max(0, 64 - (x - 32) ** 2))))
    px(x, dy + 1, OUT)

# --- wind-driven snow off the boots and case ---
for (x, y) in [(20, 44), (17, 43), (14, 45), (10, 42), (24, 44), (38, 44), (41, 43), (44, 45)]:
    px(x, y, SNOW)
for (x, y) in [(8, 40), (6, 43), (11, 46), (30, 47), (36, 47), (2, 39)]:
    px(x, y, ICE)

print(c.stats_text())
view(c)
save('polar_researcher', c, indexed=True)
finish(c)
