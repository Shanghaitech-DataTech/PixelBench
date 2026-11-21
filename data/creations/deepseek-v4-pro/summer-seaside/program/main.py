import math

# ---------- palette ----------
SKY = ["#2f7fc9", "#3f9ad6", "#55b4e6", "#6fc9f0", "#8dd8f7", "#b0e6fb"]
SEA = ["#1a5a94", "#1f6ba6", "#2a85b8", "#3aa5c4", "#5cc5c8", "#7fd9cd"]
SAND_WET = "#d8b26a"
SAND_DRY = "#f0cd8b"
SAND_SHADOW = "#d9a55f"
WHITE = "#ffffff"
HAZE = "#d6ecf9"
GULL = "#3f5266"
SUN_GLOW = "#fff6c9"
SUN = "#ffe14d"
SUN_CORE = "#fff3a0"
UMB_RED = "#e23b3b"
POLE = "#8a5a33"
TOWEL_A = "#ff7b93"
TOWEL_B = "#ffffff"
FLIP = "#ffd23f"
HULL = "#7a4a2b"
MAST = "#5b3a1e"

c = new_canvas(128, 128, name="result")

def band(y0, y1, col):
    c.rect(0, y0, 128, y1 - y0 + 1, col)

# ---------- sky ----------
sky_bands = [
    (0, 9, SKY[0]),
    (10, 18, SKY[1]),
    (19, 27, SKY[2]),
    (28, 36, SKY[3]),
    (37, 45, SKY[4]),
    (46, 55, SKY[5]),
]
for y0, y1, col in sky_bands:
    band(y0, y1, col)

# ---------- sea ----------
sea_bands = [
    (56, 61, SEA[0]),
    (62, 67, SEA[1]),
    (68, 73, SEA[2]),
    (74, 79, SEA[3]),
    (80, 85, SEA[4]),
    (86, 92, SEA[5]),
]
for y0, y1, col in sea_bands:
    band(y0, y1, col)

# soft haze on the horizon
c.rect(0, 56, 128, 1, HAZE)

# ---------- sand ----------
band(93, 98, SAND_WET)
band(99, 127, SAND_DRY)

# ---------- sun ----------
c.circle(104, 18, 16, SUN_GLOW)
c.circle(104, 18, 9, SUN)
c.circle(104, 18, 5, SUN_CORE)

# ---------- clouds ----------
def cloud(cx, cy):
    c.ellipse(cx, cy, 14, 6, WHITE)
    c.ellipse(cx - 12, cy + 2, 8, 4, WHITE)
    c.ellipse(cx + 12, cy + 2, 9, 5, WHITE)
    c.ellipse(cx, cy - 5, 9, 5, WHITE)

cloud(24, 24)
cloud(66, 30)
# small extra puff
c.ellipse(46, 14, 10, 4, WHITE)
c.ellipse(54, 16, 7, 3, WHITE)

# ---------- gulls ----------
def gull(x, y):
    d = f"M {x-6} {y} Q {x-3} {y-5} {x} {y-2} Q {x+3} {y-5} {x+6} {y}"
    c.path(d, GULL, fill=False)

gull(32, 44)
gull(52, 38)

# ---------- sailboat (far out) ----------
c.line(104, 54, 104, 67, MAST)
c.poly([(104, 54), (96, 66), (104, 66)], WHITE, fill=True)   # mainsail
c.poly([(104, 56), (111, 66), (104, 66)], WHITE, fill=True)  # jib
c.poly([(97, 66), (112, 66), (109, 70), (100, 70)], HULL, fill=True)

# ---------- foam / waves ----------
# thin crest lines out in the sea
for y, off in [(74, 0), (81, 4), (87, 8)]:
    for x in range(off, 124, 12):
        c.rect(x, y, 4, 1, WHITE)

# bright foam band at the shoreline with scalloped lower edge
c.rect(0, 89, 128, 3, WHITE)
for x in range(0, 128, 16):
    c.circle(x + 8, 92, 4, WHITE)
# little foam blobs on the wet sand
for x in range(4, 128, 20):
    c.circle(x, 96, 2, WHITE)

# ---------- beach umbrella ----------
CX, CY, R = 44, 84, 18

# red dome (top half circle)
c.path(f"M {CX-R} {CY} A {R} {R} 0 0 1 {CX+R} {CY} Z", UMB_RED, fill=True)

# alternating white wedge stripes
angles = [180, 150, 120, 90, 60, 30, 0]
for i in range(6):
    a0, a1 = angles[i], angles[i + 1]
    if i % 2 == 1:
        continue  # red panels stay red
    x0 = CX + R * math.cos(math.radians(a0))
    y0 = CY - R * math.sin(math.radians(a0))
    x1 = CX + R * math.cos(math.radians(a1))
    y1 = CY - R * math.sin(math.radians(a1))
    d = f"M {CX} {CY} L {x0:.1f} {y0:.1f} A {R} {R} 0 0 1 {x1:.1f} {y1:.1f} Z"
    c.path(d, WHITE, fill=True)

# scalloped bottom edge
for i in range(6):
    a0, a1 = angles[i], angles[i + 1]
    x0 = CX + R * math.cos(math.radians(a0))
    x1 = CX + R * math.cos(math.radians(a1))
    r = (x1 - x0) / 2.0
    col = WHITE if i % 2 == 0 else UMB_RED
    d = f"M {x0:.1f} {CY} A {r:.1f} {r:.1f} 0 0 0 {x1:.1f} {CY} Z"
    c.path(d, col, fill=True)

# top finial and pole
c.circle(CX, CY - R - 2, 2, UMB_RED)
c.line(CX, CY, CX, 104, POLE)

# ---------- striped towel ----------
TX, TY, TW, TH = 66, 104, 35, 19
# soft shadow under the towel (drawn first so it peeks out below)
c.ellipse(TX + TW // 2, TY + TH + 2, TW // 2 + 2, 2, SAND_SHADOW)
c.rect(TX, TY, TW, TH, TOWEL_A)
for i, y in enumerate(range(TY, TY + TH, 4)):
    col = TOWEL_B if i % 2 == 0 else TOWEL_A
    c.rect(TX, y, TW, min(4, TY + TH - y), col)

# ---------- flip-flops ----------
def flipflop(x, y):
    c.ellipse(x, y, 6, 3, FLIP)
    c.line(x, y - 1, x - 4, y + 1, WHITE)
    c.line(x, y - 1, x + 4, y + 1, WHITE)
    c.set(x, y - 2, WHITE)

flipflop(110, 113)
flipflop(121, 116)

print(c.stats_text())
finish(c)
