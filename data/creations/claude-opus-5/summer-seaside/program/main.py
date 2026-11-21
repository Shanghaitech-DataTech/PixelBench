import math

W = H = 128
c = new_canvas(W, H, name="output")

# ---------------- palette ----------------
SKY_T = "#5bb7e8"
SKY_M = "#7fcdf0"
SKY_B = "#a9e2f7"
CLOUD = "#ffffff"
CLOUD_S = "#d8eef9"
SUN = "#fff38a"
SUN_C = "#fffbd0"
SUN_G = "#ffe25c"

SEA_D = "#123a6e"
SEA_1 = "#1a5490"
SEA_2 = "#1f71ab"
SEA_3 = "#2591bf"
SEA_4 = "#35b2c8"
SEA_5 = "#5fd3cf"
SEA_6 = "#8ee6dd"
FOAM = "#ffffff"
FOAM_S = "#ddf6f7"

SAND_D = "#d8a85f"
SAND = "#f0c87a"
SAND_L = "#f8dfa6"
WET = "#cdac77"

HORIZON = 54

# ---------------- sky ----------------
c.rect(0, 0, W, 20, SKY_T)
c.rect(0, 20, W, 18, SKY_M)
c.rect(0, 38, W, HORIZON - 38, SKY_B)
c.dither(0, 18, W, 3, [SKY_T, SKY_M], pattern="bayer4")
c.dither(0, 36, W, 3, [SKY_M, SKY_B], pattern="bayer4")

# ---------------- sun ----------------
SX, SY = 103, 17
c.circle(SX, SY, 10, SUN_G)
c.circle(SX, SY, 8, SUN)
c.circle(SX, SY, 5, SUN_C)

# ---------------- clouds ----------------
def cloud(cx, cy, s=1.0):
    lobes = [(-10, 1, 4), (-4, -2, 6), (3, -3, 5), (9, 1, 4), (15, 2, 3)]
    for dx, dy, r in lobes:
        rr = max(1, int(round(r * s)))
        c.ellipse(cx + int(dx * s), cy + int(dy * s), rr + 1, rr, CLOUD)
    for dx, dy, r in lobes:
        rr = max(1, int(round(r * s)))
        c.ellipse(cx + int(dx * s), cy + int(dy * s) + rr - 1, rr, 1, CLOUD_S)

cloud(26, 13, 1.0)
cloud(68, 28, 0.75)
cloud(13, 40, 0.6)
cloud(112, 41, 0.5)

# ---------------- shoreline curve ----------------
def shore(x):
    v = (90.0
         + 3.0 * math.sin(x / 21.0 + 0.6)
         + 1.6 * math.sin(x / 7.5 + 2.1))
    return int(round(v))

# ---------------- sea ----------------
sea_bands = [(SEA_D, 5), (SEA_1, 6), (SEA_2, 7), (SEA_3, 8), (SEA_4, 7)]
y = HORIZON
for col, hh in sea_bands:
    c.rect(0, y, W, hh, col)
    y += hh
# shallow water fills down to the shoreline
for x in range(W):
    c.line(x, y, x, shore(x) - 1, SEA_5)
    c.line(x, shore(x) - 4, x, shore(x) - 1, SEA_6)

for (col, hh), nxt in zip(sea_bands, sea_bands[1:] + [(SEA_5, 0)]):
    pass
yy = HORIZON
for i, (col, hh) in enumerate(sea_bands):
    nxt = sea_bands[i + 1][0] if i + 1 < len(sea_bands) else SEA_5
    c.dither(0, yy + hh - 2, W, 2, [col, nxt], pattern="bayer4")
    yy += hh

# thin wavy foam lines out at sea
def wave_line(base, amp, freq, phase, col, x0=0, x1=W):
    for x in range(x0, x1):
        yv = base + amp * math.sin(x / freq + phase)
        c.set(x, int(round(yv)), col)

def dashes(base, amp, freq, phase, col, segs):
    for x0, x1 in segs:
        wave_line(base, amp, freq, phase, col, x0, x1)

dashes(60, 0.8, 9.0, 0.0, FOAM_S, [(4, 20), (30, 46), (60, 74), (92, 110)])
dashes(66, 1.1, 11.0, 1.4, FOAM_S, [(0, 14), (24, 40), (54, 66), (80, 96), (112, 128)])
dashes(72, 1.3, 13.0, 0.5, FOAM, [(10, 30), (44, 62), (78, 92), (104, 124)])
dashes(78, 1.6, 10.0, 2.6, FOAM_S, [(0, 18), (34, 52), (68, 88), (100, 118)])
dashes(84, 1.8, 12.0, 1.1, FOAM, [(6, 26), (40, 58), (72, 90), (106, 126)])

# ---------------- distant sailboat ----------------
BX, BY = 36, 61
c.path("M %d %d L %d %d L %d %d Z" % (BX, BY - 11, BX, BY - 1, BX + 6, BY - 1), FOAM)
c.path("M %d %d L %d %d L %d %d Z" % (BX - 1, BY - 9, BX - 1, BY - 1, BX - 5, BY - 1), "#eef6fa")
c.set(BX, BY - 12, FOAM)
c.line(BX - 5, BY, BX + 5, BY, FOAM)
c.line(BX - 3, BY + 1, BX + 3, BY + 1, "#c9dae6")

# ---------------- sand ----------------
for x in range(W):
    s = shore(x)
    c.line(x, s, x, s + 9, WET)
    c.line(x, s + 10, x, H - 1, SAND)
    # foam crest riding the shoreline
    c.line(x, s - 3, x, s + 1, FOAM)
    c.set(x, s + 2, FOAM_S)

# a second spent-wave line further up the beach
for x in range(W):
    yv = int(round(shore(x) + 8 + 2.0 * math.sin(x / 15.0 + 2.0)))
    c.set(x, yv, FOAM_S)
    c.set(x, yv + 1, "#e8dcc2")

# sand tone transitions
c.dither(0, 104, W, 5, [WET, SAND], pattern="bayer4")
c.rect(0, 117, W, 11, SAND_L)
c.dither(0, 113, W, 5, [SAND, SAND_L], pattern="bayer4")
for sx, sy in [(8, 121), (21, 126), (36, 119), (53, 124), (69, 120), (85, 127),
               (101, 122), (117, 125), (45, 111), (93, 109), (14, 110), (124, 115)]:
    c.set(sx, sy, SAND_D)

# ---------------- beach objects ----------------
UMB_R = "#e03a3a"
UMB_RD = "#b32626"
UMB_W = "#fdfdfd"
UMB_WS = "#e0e0e0"
POLE = "#9a7247"
POLE_D = "#6f5030"
SHADOW = "#c9a068"
TOW_R = "#ef5f6b"
TOW_W = "#fff4ec"
TOW_B = "#3f8fd0"
FLIP_A = "#36b6a6"
FLIP_B = "#1d7f78"
STRAP = "#ffffff"
GULL = "#f7f7f7"
GULL_D = "#3f4b57"

# ---- umbrella (left of centre, planted in dry sand) ----
UX, UY = 32, 101         # UY = canopy centre row
# ground shadow
c.ellipse(UX + 8, 122, 12, 3, SHADOW)
# pole
c.rect(UX, UY + 2, 2, 21, POLE)
c.line(UX + 1, UY + 2, UX + 1, UY + 22, POLE_D)
# canopy: half-ellipse dome, striped by wedge
CXU, RX, RY = UX + 1, 18, 10
for x in range(CXU - RX, CXU + RX + 1):
    t = (x - CXU) / float(RX)
    if abs(t) > 1:
        continue
    top = int(round(UY - RY * math.sqrt(max(0.0, 1 - t * t))))
    wedge = int((x - CXU + RX) // 5)
    col = UMB_R if wedge % 2 == 0 else UMB_W
    c.line(x, top, x, UY, col)
    c.set(x, UY, UMB_RD if col is UMB_R else UMB_WS)
    c.set(x, top, UMB_RD if col is UMB_R else UMB_WS)
c.set(CXU, UY - RY - 1, UMB_WS)

# ---- striped towel laid flat on the sand (trapezoid, stripes across) ----
TX, TY, TH = 72, 108, 14      # top edge centre-left, height in rows
TOP_W, BOT_W = 32, 42
for row in range(TH):
    t = row / float(TH - 1)
    half = (TOP_W + (BOT_W - TOP_W) * t) / 2.0
    cxt = TX + 20
    x0 = int(round(cxt - half))
    x1 = int(round(cxt + half))
    # stripes run across the towel (bands of rows)
    band = row // 3
    if band % 2 == 0:
        col = TOW_R
    else:
        col = TOW_W if band % 4 == 1 else TOW_B
    c.line(x0, TY + row, x1, TY + row, col)
    c.set(x0, TY + row, "#c9a88f")
    c.set(x1, TY + row, "#c9a88f")
# shadow hugging the lower edge
c.line(TX + 20 - BOT_W // 2 + 1, TY + TH, TX + 20 + BOT_W // 2 - 1, TY + TH, SHADOW)

# ---- flip-flops (between umbrella and towel) ----
def flop(x, y, col, dark):
    c.ellipse(x, y, 2, 4, col)
    c.set(x, y - 4, col)
    c.ellipse(x, y + 3, 2, 2, col)
    c.line(x - 1, y - 2, x, y, STRAP)
    c.line(x + 1, y - 2, x, y, STRAP)
    c.set(x, y + 5, dark)

c.ellipse(55, 121, 7, 3, SHADOW)
flop(52, 118, FLIP_A, FLIP_B)
flop(59, 119, FLIP_A, FLIP_B)

# ---- gulls (two, flying, simple M silhouettes) ----
def gull(x, y, span=4):
    # body
    c.set(x, y, GULL_D)
    c.set(x, y + 1, GULL_D)
    # wings sweeping up and out
    pts = [(1, -1), (2, -2), (3, -2), (4, -3)][:span]
    for dx, dy in pts:
        c.set(x - dx, y + dy, GULL_D)
        c.set(x + dx, y + dy, GULL_D)
    c.set(x - 1, y, GULL)
    c.set(x + 1, y, GULL)

gull(57, 23, 4)
gull(79, 15, 3)

# ---- sun glitter on the water ----
for gx, gy in [(100, 58), (104, 62), (97, 65), (107, 69), (101, 72),
               (110, 60), (94, 70), (112, 75), (103, 78), (96, 60)]:
    c.set(gx, gy, FOAM_S)
for gx, gy in [(102, 60), (99, 68), (108, 66), (105, 74)]:
    c.set(gx, gy, FOAM)

print(c.stats_text())

view(c)
finish(c)
