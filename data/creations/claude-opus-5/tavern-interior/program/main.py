c = new_canvas(64, 64, name="output")

# ---------- palette ----------
OL      = '#17100f'
CEIL    = '#241614'
CEIL_D  = '#1a1012'
WALL    = '#3b2420'
WALL_D  = '#2c1a17'
WALL_L  = '#4a2e27'
SMOKE   = '#4d3330'
RECESS  = '#271917'
SHELF_L = '#8a5630'
SHELF   = '#6b4024'
SHELF_D = '#49281a'
COUNT_L = '#ab6f3a'
COUNT   = '#7d4b27'
COUNT_T = '#8a5630'
COUNT_F = '#5e3620'
COUNT_FD= '#3a2014'
FLOOR   = '#2b1c18'
FLOOR_D = '#211411'
FLOOR_L = '#3a2620'
STOOL_L = '#8a5a30'
STOOL   = '#6b4526'
STOOL_D = '#452a15'
BAR_W   = '#7a4a28'
BAR_D   = '#4e2d18'
BAND    = '#9a9aa2'
BAND_D  = '#5c5c64'
CORD    = '#241a14'
LAMP_M  = '#4a3426'
LAMP_L  = '#6d4c30'
BULB    = '#ffe9a8'
BULB_C  = '#fff6d8'
GLOW_A  = '#e8ab54'
GLASS   = '#c3d4cc'
GLASS_D = '#8ba39c'
BEER    = '#d08a2a'
FOAM    = '#f4ecd6'

BOTTLES = [
    ('#3f7a4a', '#27573a'),
    ('#2f6b52', '#1d4a38'),
    ('#b4722c', '#7d4818'),
    ('#8c3030', '#5c1d20'),
    ('#35557a', '#223a56'),
    ('#9aa8a0', '#67756e'),
]
CAPS = ['#d9b24a', '#8a2f2a']


def bottle(cv, x, yb, h, idx, cap=0):
    col, dark = BOTTLES[idx % len(BOTTLES)]
    cv.rect(x, yb - h + 1, 3, h, col)
    cv.line(x + 2, yb - h + 1, x + 2, yb, dark)
    cv.set(x + 1, yb - h, col)
    cv.set(x + 1, yb - h - 1, col)
    cv.set(x + 1, yb - h - 2, CAPS[cap % len(CAPS)])


# ---------- ceiling ----------
c.rect(0, 0, 64, 3, CEIL)
c.rect(0, 3, 64, 1, CEIL_D)

# ---------- back wall ----------
c.rect(0, 4, 64, 34, WALL)
for x in range(5, 64, 8):
    c.line(x, 4, x, 37, WALL_D)
    c.line(x + 1, 4, x + 1, 37, WALL_L)
# ceiling beams
for x in range(2, 64, 10):
    c.rect(x, 0, 2, 3, CEIL_D)

# ---------- shelving behind the bar ----------
c.rect(3, 15, 58, 22, RECESS)
c.rect(1, 14, 2, 24, SHELF_D)
c.rect(61, 14, 2, 24, SHELF_D)
c.rect(1, 13, 62, 1, SHELF)
c.rect(1, 14, 62, 1, SHELF_D)
for ys in (27, 36):
    c.rect(3, ys, 58, 1, SHELF_L)
    c.rect(3, ys + 1, 58, 1, SHELF_D)

row_a = [(5, 6, 0), (9, 5, 2), (13, 7, 1), (17, 5, 3), (22, 6, 4),
         (26, 5, 5), (30, 7, 2), (35, 5, 0), (39, 6, 3), (43, 5, 1),
         (48, 7, 4), (52, 5, 2), (56, 6, 5)]
for x, h, idx in row_a:
    bottle(c, x, 26, h, idx, (x // 4) % 2)

row_b = [(5, 4, 3), (9, 5, 1), (13, 4, 5), (17, 5, 0), (22, 4, 2),
         (26, 5, 4), (30, 4, 1), (34, 5, 3), (39, 4, 0), (43, 5, 2),
         (47, 4, 4), (52, 5, 5), (56, 4, 1)]
for x, h, idx in row_b:
    bottle(c, x, 35, h, idx, (x // 5) % 2)

# ---------- bar counter ----------
c.rect(0, 37, 64, 1, OL)
c.rect(0, 38, 64, 1, COUNT_L)
c.rect(0, 39, 64, 2, COUNT)
c.rect(0, 41, 64, 1, COUNT_T)
c.rect(0, 42, 64, 7, COUNT_F)
for x in range(6, 64, 12):
    c.line(x, 42, x, 48, COUNT_FD)
c.rect(0, 48, 64, 1, OL)

# ---------- floor ----------
c.rect(0, 49, 64, 15, FLOOR)
for y in (52, 56, 60):
    c.line(0, y, 63, y, FLOOR_D)
c.dither(0, 49, 64, 15, [FLOOR, FLOOR_L], pattern="bayer4")
c.rect(0, 49, 64, 1, FLOOR_D)

# ---------- bar stools ----------
for cx in (18, 32, 46):
    c.rect(cx - 4, 45, 9, 2, STOOL_L)
    c.rect(cx - 4, 47, 9, 1, STOOL_D)
    c.rect(cx - 4, 44, 9, 1, OL)
    c.set(cx - 5, 45, OL)
    c.set(cx + 5, 45, OL)
    c.set(cx - 5, 46, OL)
    c.set(cx + 5, 46, OL)
    c.rect(cx - 1, 48, 2, 9, STOOL)
    c.line(cx - 2, 48, cx - 2, 56, OL)
    c.line(cx + 2, 48, cx + 2, 56, OL)
    c.rect(cx - 3, 57, 7, 1, STOOL_D)
    c.rect(cx - 3, 58, 7, 1, OL)

# ---------- barrel, foreground left ----------
c.poly([(1, 44), (11, 44), (12, 50), (11, 60), (1, 60), (0, 50)], BAR_W)
c.ellipse(6, 44, 5, 2, BAR_W)
c.ellipse(6, 44, 3, 1, BAR_D)
c.ellipse(6, 44, 5, 2, OL, fill=False)
for x in (3, 6, 9):
    c.line(x, 46, x, 59, BAR_D)
c.rect(0, 47, 13, 2, BAND)
c.rect(0, 48, 13, 1, BAND_D)
c.rect(0, 56, 13, 2, BAND)
c.rect(0, 57, 13, 1, BAND_D)
c.poly([(1, 44), (11, 44), (12, 50), (11, 60), (1, 60), (0, 50)], OL, fill=False)

# ---------- small keg on the counter, right ----------
c.rect(53, 31, 9, 7, BAR_W)
c.line(53, 31, 61, 31, BAR_D)
c.rect(55, 31, 1, 7, BAR_D)
c.rect(59, 31, 1, 7, BAR_D)
c.rect(53, 33, 9, 1, BAND)
c.rect(53, 35, 9, 1, BAND_D)
c.rect(52, 31, 1, 7, OL)
c.rect(62, 31, 1, 7, OL)
c.rect(53, 30, 9, 1, OL)

# ---------- mugs and glasses on the counter ----------
def mug(cv, x, yb):
    cv.rect(x, yb - 4, 4, 5, GLASS)
    cv.rect(x, yb - 3, 4, 4, BEER)
    cv.rect(x, yb - 4, 4, 1, FOAM)
    cv.line(x + 3, yb - 4, x + 3, yb, GLASS_D)
    cv.set(x + 4, yb - 3, GLASS)
    cv.set(x + 4, yb - 2, GLASS)
    for dy in range(-4, 1):
        cv.set(x - 1, yb + dy, OL)

mug(c, 11, 37)
mug(c, 25, 37)

c.rect(40, 33, 3, 5, GLASS)
c.rect(40, 35, 3, 3, BEER)
c.line(42, 33, 42, 37, GLASS_D)
c.line(39, 33, 39, 37, OL)
c.line(43, 33, 43, 37, OL)

# ---------- hanging lamps ----------
LAMPS = (12, 32, 52)
for cx in LAMPS:
    c.line(cx, 0, cx, 5, CORD)
    c.poly([(cx - 4, 10), (cx + 4, 10), (cx + 2, 6), (cx - 2, 6)], LAMP_M)
    c.line(cx - 2, 7, cx + 1, 7, LAMP_L)
    c.poly([(cx - 4, 10), (cx + 4, 10), (cx + 2, 6), (cx - 2, 6)], OL, fill=False)
    c.rect(cx - 2, 11, 5, 2, BULB)
    c.set(cx - 1, 11, BULB_C)
    c.set(cx, 11, BULB_C)
    c.set(cx - 2, 13, GLOW_A)
    c.set(cx + 2, 13, GLOW_A)
    c.set(cx, 13, BULB)

# ---------- warm light falloff ----------
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
pal = {p['index']: p['rgba'] for p in c.palette()}
LIT = {c.color(x) for x in (WALL, WALL_D, WALL_L, CEIL, CEIL_D, RECESS,
                            SHELF, SHELF_D, SHELF_L, COUNT, COUNT_L, COUNT_T,
                            COUNT_F, COUNT_FD, FLOOR, FLOOR_D, FLOOR_L)}
cache = {}


def tint(x, y, amount=0.3):
    i = c.get(x, y)
    if i not in LIT:
        return
    rgba = pal[i]
    if i not in cache:
        tr, tg, tb = 255, 196, 104
        cache[i] = (int(rgba[0] + (tr - rgba[0]) * amount),
                    int(rgba[1] + (tg - rgba[1]) * amount),
                    int(rgba[2] + (tb - rgba[2]) * amount),
                    rgba[3])
    c.set(x, y, cache[i])


for cx in LAMPS:
    for y in range(3, 52):
        for x in range(cx - 12, cx + 13):
            if not (0 <= x < 64):
                continue
            dx = abs(x - cx) / 11.0
            dy = (y - 11) / 24.0 if y > 11 else (11 - y) / 8.0
            d = (dx * dx + dy * dy) ** 0.5
            if d >= 1.0:
                continue
            if (1.0 - d) * 20 > BAYER[y % 4][x % 4]:
                tint(x, y)
    # compact glow right under the shade
    for i, y in enumerate((13, 14)):
        half = 3 - i
        for x in range(cx - half, cx + half + 1):
            if 0 <= x < 64 and (x + y) % 2 == 0:
                c.set(x, y, GLOW_A)
    c.rect(cx - 2, 11, 5, 2, BULB)
    c.set(cx - 1, 11, BULB_C)
    c.set(cx, 11, BULB_C)
    c.set(cx - 1, 13, BULB)
    c.set(cx, 13, BULB)

# ---------- second barrel, foreground right ----------
c.poly([(53, 47), (62, 47), (63, 53), (62, 62), (53, 62), (52, 53)], BAR_W)
c.ellipse(57, 47, 4, 2, BAR_W)
c.ellipse(57, 47, 2, 1, BAR_D)
c.ellipse(57, 47, 4, 2, OL, fill=False)
for x in (55, 58, 61):
    c.line(x, 49, x, 61, BAR_D)
c.rect(52, 50, 12, 1, BAND)
c.rect(52, 51, 12, 1, BAND_D)
c.rect(52, 58, 12, 1, BAND)
c.rect(52, 59, 12, 1, BAND_D)
c.poly([(53, 47), (62, 47), (63, 53), (62, 62), (53, 62), (52, 53)], OL, fill=False)

# smoky haze near the ceiling, sparse wisps
c.dither(0, 4, 64, 3, [SMOKE, WALL], pattern="bayer4")
for x in range(0, 64):
    if (x * 7) % 11 < 4:
        c.set(x, 7 + (x // 9) % 2, SMOKE)

# corner vignette
DARK = '#1d1210'
for y in range(64):
    for x in range(64):
        e = min(x, 63 - x, y, 63 - y)
        if e <= 1 and (x + y) % (2 if e == 0 else 4) == 0:
            if c.get(x, y) != c.color(OL):
                c.set(x, y, DARK)

print(c.stats_text())
view(c)
finish(c)
