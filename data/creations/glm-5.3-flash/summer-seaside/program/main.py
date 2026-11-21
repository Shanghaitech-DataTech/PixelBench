import math

W = H = 128

# ---------------- palette ----------------
SKY = ['#2F87DB', '#4198E5', '#63B0EE', '#86C7F4', '#A6DAF8']
SUN_GLOW, SUN_MID, SUN_CORE = '#FFF4BE', '#FFE066', '#FFF9D6'
WHITE = '#FFFFFF'
CLOUD_SHADE = '#DCEBF5'
HORIZON_C = '#1A4788'
SEA = ['#1D4F9C', '#2060AC', '#2371BA', '#2583C0', '#2895C0', '#2CA7B9', '#33B8AE']
FOAM_SHADE = '#D7EDF4'
SAND, SAND_WET, SAND_DARK, SAND_LIGHT = '#F2D48A', '#E5C37B', '#DDB36A', '#F9E7B8'
UMB_RED, UMB_DARK, POLE, POLE_DARK = '#E23B3B', '#B02626', '#8A5A33', '#6B4423'
DARK = '#33475B'

c = new_canvas(W, H, background=None, name='summer-seaside')

# ---------------- sky (rows 0-57) ----------------
sky_rows = [(0, 16), (17, 28), (29, 40), (41, 49), (50, 57)]
for (y0, y1), col in zip(sky_rows, SKY):
    c.rect(0, y0, W, y1 - y0 + 1, col)
for i in range(1, len(sky_rows)):
    y = sky_rows[i][0]
    c.dither(0, y - 1, W, 2, [SKY[i - 1], SKY[i]], pattern='checker')

# ---------------- sun ----------------
SX, SY = 24, 20
c.circle(SX, SY, 11, SUN_GLOW)
c.circle(SX, SY, 8, SUN_MID)
c.circle(SX, SY, 5, SUN_CORE)
for k in range(8):
    a = math.radians(k * 45 + 22.5)
    c.line(int(round(SX + 12 * math.cos(a))), int(round(SY + 12 * math.sin(a))),
           int(round(SX + 15 * math.cos(a))), int(round(SY + 15 * math.sin(a))), SUN_GLOW)

# ---------------- clouds ----------------
def cloud(cx, cy, w, h):
    lobes = [(cx - w // 4, cy + h // 6, w // 4 + 1, h // 2),
             (cx + w // 4, cy + h // 6, w // 4 + 1, h // 2),
             (cx, cy - h // 4, w // 3 + 1, h // 2 + 1)]
    for (lx, ly, lrx, lry) in lobes:
        c.ellipse(lx, ly + 1, lrx, lry, CLOUD_SHADE)
    c.rect(cx - w // 2, cy + 1, w, h // 2 + 1, CLOUD_SHADE)
    for (lx, ly, lrx, lry) in lobes:
        c.ellipse(lx, ly, lrx, lry, WHITE)
    c.rect(cx - w // 2, cy, w, h // 2 + 1, WHITE)

cloud(84, 19, 30, 12)
cloud(44, 38, 22, 9)
cloud(106, 40, 17, 8)

# ---------------- sea (rows 58-93) ----------------
c.rect(0, 58, W, 1, HORIZON_C)
sea_rows = [(59, 63), (64, 68), (69, 73), (74, 78), (79, 83), (84, 88), (89, 93)]
for (y0, y1), col in zip(sea_rows, SEA):
    c.rect(0, y0, W, y1 - y0 + 1, col)
for i in range(1, len(sea_rows)):
    y = sea_rows[i][0]
    c.dither(0, y - 1, W, 2, [SEA[i - 1], SEA[i]], pattern='checker')

# rolling wave crests (broken white lines, denser near shore)
for yb, amp, ph, run in [(66, 0.8, 0.0, 7), (71, 1.0, 2.1, 6), (76, 1.3, 4.2, 7),
                         (81, 1.2, 1.2, 5), (85, 1.0, 3.3, 6)]:
    for x in range(W):
        if (x + int(ph * 10)) % 11 < run:
            c.set(x, yb + int(round(amp * math.sin(x / 6.0 + ph))), WHITE)

# ---------------- sand ----------------
c.rect(0, 95, W, 5, SAND_WET)   # rows 95..99 wet sand
c.rect(0, 100, W, 28, SAND)     # rows 100..127 dry sand
for i in range(130):
    x = (i * 37 + 11) % 128
    y = 101 + (i * 29) % 27
    c.set(x, y, SAND_DARK if i % 3 else SAND_LIGHT)

# ---------------- foam shoreline ----------------
def foam_top(x):
    return 89 + int(round(1.6 * math.sin(x / 6.5) + 1.1 * math.sin(x / 2.7 + 1.3)))

for x in range(W):
    top = foam_top(x)
    bot = 95 + (1 if (x // 6) % 2 == 0 else 0)
    for y in range(top, bot + 1):
        c.set(x, y, WHITE)
    if (x * 7 + 3) % 5 == 0:
        c.set(x, bot, FOAM_SHADE)
    if (x * 11 + 1) % 7 == 0:
        c.set(x, bot - 1, FOAM_SHADE)
    if (x * 13 + 5) % 9 == 0:
        c.set(x, top + 1, FOAM_SHADE)

# foam line where the water last reached
for x in range(W):
    yy = 98 + int(round(math.sin(x / 9.0)))
    if (x * 5) % 9 < 6:
        c.set(x, yy, WHITE)

# receding foam arcs drying on the sand
for yb, ph in [(103, 0.0), (108, 2.4)]:
    for x in range(W):
        if (x + int(ph * 5)) % 14 < 9:
            c.set(x, yb + int(round(1.1 * math.sin(x / 7.0 + ph))), WHITE)

# ---------------- umbrella shadow ----------------
c.ellipse(100, 110, 14, 3, SAND_DARK)

# ---------------- towel ----------------
c.poly([(28, 102), (58, 102), (54, 122), (24, 122)], WHITE)

def xl(y):
    return 28 - (y - 102) * 4 / 20.0

def xr(y):
    return 58 - (y - 102) * 4 / 20.0

for (a, b, col) in [(105, 108, SEA[5]), (111, 114, UMB_RED), (117, 120, SEA[5])]:
    c.poly([(int(round(xl(a))), a), (int(round(xr(a))), a),
            (int(round(xr(b))), b), (int(round(xl(b))), b)], col)
c.line(int(round(xr(102))), 102, int(round(xr(121))), 121, CLOUD_SHADE)

# ---------------- flip-flops ----------------
def flipflop(cx, cy):
    c.ellipse(cx, cy, 3, 5, SEA[6])
    c.line(cx - 2, cy - 3, cx, cy + 1, SEA[0])
    c.line(cx + 2, cy - 3, cx, cy + 1, SEA[0])

flipflop(63, 112)
flipflop(74, 117)

# ---------------- beach umbrella ----------------
UX, UY, URX, URY = 88, 62, 22, 10
c.rect(87, 60, 2, 49, POLE)            # pole rows 60..108
c.line(88, 60, 88, 108, POLE_DARK)
c.ellipse(88, 109, 3, 1, POLE_DARK)    # pole base

pts = [(UX + int(round(URX * math.cos(math.radians(t)))),
        UY - int(round(URY * math.sin(math.radians(t))))) for t in range(180, -1, -4)]
c.poly(pts, UMB_RED)                   # canopy half-disc
apex = (UX, UY - URY)
bounds = [66, 71, 77, 83, 88, 93, 99, 105, 110]
for i in (1, 3, 5, 7):                 # alternating white panels
    c.poly([apex, (bounds[i], UY), (bounds[i + 1], UY)], WHITE)
c.poly(pts, UMB_DARK, fill=False)      # rim + outline
c.rect(87, 49, 2, 3, UMB_DARK)         # finial

# ---------------- sailboat far out ----------------
c.poly([(26, 56), (35, 56), (33, 58), (27, 58)], DARK)   # hull on the horizon
c.line(30, 47, 30, 56, DARK)                             # mast
c.poly([(31, 48), (31, 55), (37, 55)], WHITE)            # main sail
c.poly([(29, 50), (29, 55), (25, 55)], WHITE)            # jib

# ---------------- gulls ----------------
def gull(cx, cy, s):
    c.path('M {} {} Q {} {} {} {} Q {} {} {} {}'.format(
        cx - s, cy - 2, cx - s // 2, cy + 2, cx, cy,
        cx + s // 2, cy + 2, cx + s, cy - 2), DARK, fill=False)

gull(47, 24, 6)
gull(62, 31, 5)

# ---------------- report ----------------
print(c.stats_text())
finish(c)
