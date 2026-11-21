import math, random
from pixelbench_api import *

rng = random.Random(20261107)

W, H = 144, 256
out = input_canvas.copy(name="output")

# ---------------------------------------------------------------- palette ----
GREEN_SH = "#122a16"
GREEN_D  = "#1d4023"
GREEN_M  = "#2c5c31"
GREEN_L  = "#437a3a"
GREEN_B  = "#5f9a48"
GREEN_HI = "#8abe62"
OLIVE    = "#7d8c3d"

CLOAK_D  = "#1f182c"
CLOAK_B  = "#36304f"
CLOAK_H  = "#4d4569"
RIM      = "#b8863f"
K        = "#120d18"
WOOD_D   = "#3d2817"
WOOD_L   = "#6d4a28"
GLOVE_D  = "#241e33"
BOOT_D   = "#191426"
BOOT_L   = "#332c46"
CRY_M    = "#e8b64a"
CRY_C    = "#fff6d0"

# ---------------------------------------------------------------- helpers ----
_RGBA = {}
def rgba_index(cv, idx):
    v = _RGBA.get(idx)
    if v is None:
        v = cv.palette()[idx]['rgba']
        _RGBA[idx] = v
    return v

def rgba_at(cv, x, y):
    return rgba_index(cv, cv.get(x, y))

def S(cv, x, y, col):
    if 0 <= x < W and 0 <= y < H:
        cv.set(x, y, col)

def q8(v):
    v = int(v)
    if v < 0:
        v = 0
    if v > 255:
        v = 255
    return (v // 8) * 8 + 4

def lighten(cv, x, y, col, t):
    if not (0 <= x < W and 0 <= y < H) or t <= 0.0:
        return
    r, g, b, a = rgba_at(cv, x, y)
    ar = min(255.0, col[0] * t)
    ag = min(255.0, col[1] * t)
    ab = min(255.0, col[2] * t)
    nr = 255.0 - (255.0 - r) * (255.0 - ar) / 255.0
    ng = 255.0 - (255.0 - g) * (255.0 - ag) / 255.0
    nb = 255.0 - (255.0 - b) * (255.0 - ab) / 255.0
    cv.set(x, y, (q8(nr), q8(ng), q8(nb)))

def glow(cv, cx, cy, radius, col, strength, power=1.6):
    r2 = radius + 1
    for y in range(int(cy - r2), int(cy + r2) + 1):
        for x in range(int(cx - r2), int(cx + r2) + 1):
            d = math.hypot(x - cx, y - cy)
            if d > radius:
                continue
            t = (1.0 - d / radius) ** power * strength
            lighten(cv, x, y, col, t)

def darken(cv, x, y, t):
    if not (0 <= x < W and 0 <= y < H) or t <= 0.0:
        return
    r, g, b, a = rgba_at(cv, x, y)
    cv.set(x, y, (q8(r * (1.0 - t)), q8(g * (1.0 - t)), q8(b * (1.0 - t))))

# ------------------------------------------------------------------ vines ----
V = {'stem': GREEN_D, 'stem2': GREEN_M, 'stem_d': GREEN_SH,
     'leaf_d': GREEN_D, 'leaf_m': GREEN_M, 'leaf_l': GREEN_L, 'leaf_hi': GREEN_B}

def leaf(cv, x, y, d, main, hi, big=False):
    S(cv, x + d, y, main)
    S(cv, x + d, y + 1, main)
    S(cv, x + 2 * d, y, hi)
    S(cv, x + 3 * d, y + 1, hi)
    if big:
        S(cv, x, y + 1, main)
        S(cv, x + d, y + 2, main)

def strand(x0, y0, length, amp=1.7, period=16.0, phase=0.0,
           leaf_every=4, thick=True, cols=None, cv=None):
    if cv is None:
        cv = out
    cols = cols or V
    for t in range(length):
        y = y0 + t
        if y < 0 or y >= H:
            continue
        x = int(round(x0 + amp * math.sin(2 * math.pi * t / period + phase)
                      + 0.45 * amp * math.sin(1.7 * t + phase * 2.0)))
        if x < 0 or x >= W:
            continue
        stem_col = cols['stem'] if (t // 4) % 2 == 0 else cols['stem2']
        S(cv, x, y, stem_col)
        if thick and t % 5 == 0:
            S(cv, x + 1, y, cols['stem_d'])
        if t >= 2 and t % leaf_every == 0:
            d = 1 if ((t // leaf_every) % 2 == 0) else -1
            mc = cols['leaf_m'] if rng.random() < 0.55 else cols['leaf_l']
            leaf(cv, x, y, d, mc, cols['leaf_hi'], big=(rng.random() < 0.3))
            if rng.random() < 0.30:
                leaf(cv, x, y + 1, -d, cols['leaf_d'], cols['leaf_m'])

def blob(cx, cy, rx, ry, n):
    cols = [GREEN_D, GREEN_M, GREEN_L, GREEN_B, GREEN_M]
    for _ in range(n):
        x = int(round(cx + rng.uniform(-rx, rx)))
        y = int(round(cy + rng.uniform(-ry, ry)))
        S(out, x, y, rng.choice(cols))
        if rng.random() < 0.55:
            S(out, x + 1, y, rng.choice([GREEN_L, GREEN_B, GREEN_M]))
        if rng.random() < 0.30:
            S(out, x, y + 1, rng.choice([GREEN_D, GREEN_M]))
        if rng.random() < 0.12:
            S(out, x + 1, y - 1, GREEN_HI)

# --- left wall curtain ---
for lx, ly in [(1, 36), (5, 26), (9, 44), (13, 32), (17, 50),
               (21, 38), (25, 54), (29, 42), (7, 70), (19, 78), (27, 96)]:
    strand(lx + rng.randint(-1, 1), ly + rng.randint(-6, 6),
           rng.randint(80, 165), rng.uniform(1.2, 2.0),
           rng.uniform(12, 22), rng.uniform(0, 6.3), 4, True)

# --- top curtain over the tower face ---
for i in range(16):
    x = 30 + i * 5 + rng.randint(-1, 1)
    strand(x, rng.randint(14, 46), rng.randint(45, 125),
           rng.uniform(1.3, 2.4), rng.uniform(13, 24),
           rng.uniform(0, 6.3), 4, True)

# --- right side ---
for rx, ry, rl in [(96, 56, 92), (101, 66, 70), (106, 50, 108), (111, 72, 62),
                   (135, 58, 84), (140, 46, 112), (128, 74, 56), (122, 84, 46),
                   (117, 96, 40), (131, 110, 34)]:
    strand(rx + rng.randint(-1, 1), ry + rng.randint(-5, 5), rl,
           rng.uniform(1.2, 2.0), rng.uniform(12, 20),
           rng.uniform(0, 6.3), 4, True)

# --- canopy strands from the very top edge ---
for tx in [0, 6, 12, 18, 24, 98, 106, 114, 126, 134, 141]:
    strand(tx, 0, rng.randint(12, 34), rng.uniform(1.0, 1.8),
           rng.uniform(11, 18), rng.uniform(0, 6.3), 4, False)

# --- strands hugging the archway pillars ---
for ax, ay, al in [(31, 148, 58), (34, 156, 48), (37, 164, 40),
                   (65, 150, 56), (68, 156, 46), (71, 166, 34)]:
    strand(ax, ay, al, 1.1, rng.uniform(12, 18), rng.uniform(0, 6.3), 3, False)

# --- dense ivy mats ---
blob(15, 62, 11, 18, 150)
blob(40, 58, 12, 15, 150)
blob(107, 82, 9, 15, 90)
blob(86, 122, 7, 12, 60)

# --- creeping ivy along the base of the right-hand wall ---
yy = 216
for i in range(0, 70):
    x = 72 + i
    yy = 215 + int(round(2.4 * math.sin(i / 9.0) + 1.2 * math.sin(i / 3.7)))
    S(out, x, yy, GREEN_D if i % 3 else GREEN_M)
    if i % 4 == 0:
        d = 1 if (i // 4) % 2 == 0 else -1
        leaf(out, x, yy, d, GREEN_M, GREEN_L, big=(i % 8 == 0))

# ------------------------------------------------------- shadow on ground ----
for y in range(210, 224):
    for x in range(36, 70):
        dx = (x - 53) / 13.0
        dy = (y - 217) / 4.0
        d = dx * dx + dy * dy
        if d < 1.0:
            darken(out, x, y, 0.45 * (1.0 - d) ** 0.7)

# --------------------------------------------------------------- the mage ----
SW, SH = 26, 46
spr = new_canvas(SW, SH, name="mage")

def pset(x, y, col):
    if 0 <= x < SW and 0 <= y < SH:
        spr.set(x, y, col)

def popaque(x, y):
    if not (0 <= x < SW and 0 <= y < SH):
        return False
    return rgba_index(spr, spr.get(x, y))[3] > 0

# staff shaft
spr.rect(18, 4, 2, 33, WOOD_D)
spr.rect(18, 4, 1, 33, WOOD_L)
pset(19, 12, WOOD_D)
pset(19, 21, WOOD_D)

# cloak: flared body
spr.poly([(8, 11), (16, 11), (21, 30), (22, 37), (4, 37), (3, 30)], CLOAK_B)
# shoulders
spr.ellipse(12, 13, 6, 4, CLOAK_B)
# hood (back of hood, no face visible)
spr.ellipse(12, 9, 5, 6, CLOAK_B)
# neck / hood-to-shoulder shadow
spr.ellipse(12, 14, 4, 2, CLOAK_D)
pset(12, 3, CLOAK_H)
pset(11, 4, CLOAK_H)
pset(10, 5, CLOAK_H)
pset(13, 4, CLOAK_B)
# folds
spr.line(10, 17, 8, 36, CLOAK_D)
spr.line(14, 17, 17, 36, CLOAK_D)
spr.line(12, 20, 13, 36, CLOAK_D)
spr.line(9, 16, 7, 34, CLOAK_H)
spr.line(11, 17, 10, 33, CLOAK_H)
# hem shading
spr.rect(4, 36, 18, 1, CLOAK_D)
# boots
spr.rect(6, 37, 5, 4, BOOT_D)
spr.rect(14, 37, 5, 4, BOOT_D)
spr.rect(6, 37, 5, 1, BOOT_L)
spr.rect(14, 37, 5, 1, BOOT_L)
# gripping hand on the staff
spr.rect(17, 18, 2, 3, GLOVE_D)
pset(16, 19, CLOAK_H)

# crisp dark silhouette edge
spr.outline(K)

# warm rim light along the lit (right) side
for y in range(SH):
    for x in range(SW):
        if popaque(x, y) and not popaque(x + 1, y):
            spr.set(x, y, RIM)

# the glowing crystal (drawn after the outline so it stays bright)
spr.poly([(19, 1), (22, 5), (19, 9), (16, 5)], CRY_M)
spr.poly([(19, 3), (20, 5), (19, 7), (18, 5)], CRY_C)
spr.set(19, 5, "#ffffff")

OX, OY = 42, 176
out.blit(spr, OX, OY)

# ------------------------------------------------------------------ glow ----
CX, CY = OX + 19, OY + 5
glow(out, CX, CY, 26, (255, 186, 92), 0.20, 1.8)
glow(out, CX, CY, 14, (255, 204, 124), 0.34, 1.6)
glow(out, CX, CY, 7, (255, 236, 190), 0.72, 1.5)
# pool of warm light on the threshold
glow(out, 55, 216, 17, (255, 168, 84), 0.16, 2.0)

# ---------------------------------------------------------------- report ----
print(out.stats_text())
print(out.matrix_text(region=(36, 172, 70, 222)))
save("big-144-256", out)
finish(out)
