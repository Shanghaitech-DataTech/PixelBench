from pixelbench_api import *

c = new_canvas(128, 128, background="#cfe8f0", name="poolcore")

TILE_A = "#e8f4f8"   # near-white tile
TILE_B = "#b8dce8"   # pale blue tile
GROUT  = "#9cc4d4"
WALL_HI = "#dceef4"
WATER_1 = "#bfe6f2"
WATER_2 = "#a8d8ec"
WATER_3 = "#8fc6e2"
WATER_D = "#7ab4d6"
SLIDE_W = "#f8fbfc"
SLIDE_S = "#d8e8f0"
SLIDE_E = "#c0d4e0"
RING_Y  = "#f2d43c"
RING_Y2 = "#d9b520"
SKIN   = "#e8c4a8"
HAIR   = "#5a3a28"
LIGHT  = "#ffffff"
LIGHT2 = "#eef8fc"
CEIL   = "#d4e6ee"

# ---------- ceiling (y 0..17) ----------
c.rect(0, 0, 128, 18, CEIL)
# fluorescent light panels
for lx in (6, 38, 70, 102):
    c.rect(lx, 4, 20, 7, LIGHT)
    c.rect(lx, 11, 20, 2, LIGHT2)
# ceiling grid lines
for x in range(0, 128, 16):
    c.line(x, 0, x, 17, "#b8d2dc")
c.line(0, 17, 127, 17, "#a8c4d0")

# ---------- back wall (y 18..64) grid mosaic ----------
def wall_region(x0, y0, x1, y1):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            checker = ((x // 4) + (y // 4)) % 2 == 0
            c.set(x, y, TILE_A if checker else TILE_B)

wall_region(0, 18, 127, 64)
# grout lines every 8 px
for x in range(0, 128, 8):
    for y in range(18, 65):
        c.set(x, y, GROUT)
for y in range(18, 65, 8):
    for x in range(0, 128):
        c.set(x, y, GROUT)

# wall base / pool edge
c.rect(0, 62, 128, 4, "#e0eef4")
c.line(0, 65, 127, 65, "#88aec0")

# ---------- tiled columns ----------
def column(cx, top, bottom, w=8):
    for y in range(top, bottom + 1):
        for x in range(cx, cx + w):
            checker = ((x // 4) + (y // 4)) % 2 == 0
            base = TILE_A if checker else TILE_B
            if x == cx:
                base = "#f2fafc"
            elif x == cx + w - 1:
                base = "#a8ccd8"
            c.set(x, y, base)
    for y in range(top, bottom + 1, 8):
        for x in range(cx, cx + w):
            c.set(x, y, GROUT)
    c.rect(cx, top, w, 2, "#f4f8fa")
    c.rect(cx, bottom - 1, w, 2, "#9cc0ce")

column(16, 18, 70)
column(104, 18, 70)
column(60, 18, 64, w=6)

# ---------- pool water (y 66..127) ----------
c.rect(0, 66, 128, 62, WATER_1)
# horizontal ripple bands
import random
random.seed(7)
for y in range(66, 128):
    # gentle vertical gradient
    t = (y - 66) / 61.0
    base = WATER_1 if t < 0.35 else (WATER_2 if t < 0.7 else WATER_3)
    for x in range(128):
        c.set(x, y, base)

def ripple(y, x0, x1, col, amp=1, step=6, phase=0):
    x = x0
    while x <= x1:
        yy = y + int(round(amp * ((x + phase) // step % 2)))
        if 66 <= yy <= 127:
            c.set(x, yy, col)
        x += 1

for i, y in enumerate(range(70, 127, 7)):
    ripple(y, 0, 127, WATER_D if i % 2 else "#d6eef8", amp=1, step=6, phase=i * 3)
for y in range(74, 127, 11):
    ripple(y, 10, 118, WATER_3, amp=1, step=9, phase=y)

# light reflections on water (bright dashes)
for (rx, ry, rw) in [(20, 72, 10), (44, 78, 8), (88, 74, 12), (60, 90, 9),
                     (14, 96, 7), (96, 100, 10), (36, 108, 8), (74, 116, 9),
                     (110, 88, 6), (52, 120, 7)]:
    c.line(rx, ry, rx + rw, ry, "#e8f8fc")
    c.line(rx + 2, ry + 1, rx + rw - 2, ry + 1, "#d2ecf6")

# pool edge highlight row
c.line(0, 66, 127, 66, "#f0f8fa")
c.line(0, 67, 127, 67, "#cde8f2")

# ---------- water slide: curving white flume from upper right into pool ----------
# slide tower / support behind wall on right
c.rect(118, 20, 8, 46, "#eef4f6")
for x in range(118, 126):
    for y in range(20, 66):
        if (x + y) % 8 == 0:
            c.set(x, y, "#c8d8e0")
c.line(118, 20, 125, 20, "#f8fcfd")

# slide body: curve from top-right down, sweeping left then into water
pts = []
# use a path: start at (122,22) curve out left and down
d = ("M 121 22 "
     "C 108 26, 96 30, 88 40 "
     "C 80 50, 78 58, 70 64 "
     "C 62 70, 46 72, 34 76")
c.path(d, SLIDE_S, fill=False)
# draw the flume as thick band: draw path twice offset
d2 = ("M 124 22 "
      "C 111 27, 99 31, 91 41 "
      "C 83 51, 81 59, 73 65 "
      "C 65 71, 49 74, 37 79")
c.path(d2, SLIDE_E, fill=False)
# fill band between by drawing thick segments along sampled curve
import math
def bez(p0, p1, p2, p3, n=60):
    out = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3*p0[0] + 3*mt**2*t*p1[0] + 3*mt*t**2*p2[0] + t**3*p3[0]
        y = mt**3*p0[1] + 3*mt**2*t*p1[1] + 3*mt*t**2*p2[1] + t**3*p3[1]
        out.append((x, y))
    return out

curve = bez((122, 23), (100, 28), (84, 36), (76, 48)) + bez((76, 48), (68, 60), (58, 66), (46, 70)) + bez((46, 70), (40, 72), (36, 74), (30, 78))
for (x, y) in curve:
    xi, yi = int(round(x)), int(round(y))
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if 0 <= xi+dx < 128 and 18 <= yi+dy < 127:
                c.set(xi+dx, yi+dy, SLIDE_W)
# slide lip / rails
for (x, y) in curve[::3]:
    xi, yi = int(round(x)), int(round(y))
    if 0 <= xi < 128 and yi-2 >= 0:
        c.set(xi, yi-2, SLIDE_S)
# splash at water entry
c.circle(30, 80, 3, "#eaf8fc")
c.circle(28, 82, 2, "#f4fcfe")
c.set(24, 78, "#eaf8fc"); c.set(36, 77, "#eaf8fc")
c.set(22, 84, "#d8eef8"); c.set(38, 83, "#d8eef8")

# slide shadow on water
c.line(34, 84, 52, 80, "#8ab8d0")

# ---------- girl in yellow swim ring, middle of pool, seen from behind ----------
# ring (ellipse) around (64, 98)
cx, cy = 64, 98
c.ellipse(cx, cy, 11, 6, RING_Y)
# inner hole shows water
c.ellipse(cx, cy, 6, 3, WATER_2)
# ring shading bottom
for x in range(cx-11, cx+12):
    for y in range(cy, cy+7):
        if c.get(x, y) == c.color(RING_Y):
            if (x - cx) ** 2 / 121 + (y - cy) ** 2 / 36 > 0.55:
                c.set(x, y, RING_Y2)
# ring highlight top
c.line(cx-7, cy-4, cx+6, cy-4, "#fbe98a")

# girl: back view, sitting in ring — body above ring center
# torso (skin/back)
c.rect(cx-3, cy-12, 6, 8, SKIN)
# swimsuit dark strap across back
c.line(cx-3, cy-9, cx+2, cy-9, "#3a6a8a")
c.line(cx-3, cy-8, cx+2, cy-8, "#3a6a8a")
# shoulders round
c.set(cx-4, cy-11, SKIN); c.set(cx+3, cy-11, SKIN)
# head (hair from behind)
c.rect(cx-3, cy-18, 6, 6, HAIR)
c.set(cx-4, cy-17, HAIR); c.set(cx+3, cy-17, HAIR)
c.set(cx-4, cy-16, HAIR); c.set(cx+3, cy-16, HAIR)
# hair falls a bit
c.set(cx-4, cy-13, HAIR); c.set(cx+3, cy-13, HAIR)
c.set(cx-4, cy-12, HAIR); c.set(cx+3, cy-12, HAIR)
# hair highlight
c.line(cx-1, cy-17, cx, cy-17, "#7a5238")
# arms resting on ring
c.line(cx-4, cy-10, cx-8, cy-5, SKIN)
c.line(cx+3, cy-10, cx+7, cy-5, SKIN)
c.set(cx-8, cy-4, SKIN); c.set(cx+7, cy-4, SKIN)

# reflection of girl in water below
c.rect(cx-2, cy+8, 4, 6, "#c4a48c")
c.set(cx-2, cy+8, "#b09478"); c.set(cx+1, cy+8, "#b09478")
# ring reflection
c.line(cx-8, cy+9, cx+7, cy+9, "#c8ac30")

# gentle ripple rings around the ring
for (rx, ry, col) in [(cx, cy+2, "#d6eef8"), (cx, cy+3, WATER_3), (cx, cy+4, WATER_D)]:
    pass
c.ellipse(cx, cy+1, 13, 7, "#d6eef8", fill=False)
c.ellipse(cx, cy+2, 15, 8, WATER_3, fill=False)

# ---------- foreground vignette: slightly darker far corners of water ----------
for (x, y) in [(0,127),(1,127),(0,126),(127,127),(126,127),(127,126)]:
    c.set(x, y, WATER_D)

print(c.stats_text())
save("poolcore_water_slide", c, indexed=True)
finish(c)
