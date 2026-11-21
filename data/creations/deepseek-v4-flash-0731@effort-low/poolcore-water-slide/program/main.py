from pixelbench_api import *

W = H = 128
back = (222, 230, 240)
c = new_canvas(W, H, background=back, name="pool")

def C(spec, name=None):
    return c.color(spec, name=name)

# ================= COLORS =================
BLK = C(back, "cell")
SKY  = C((196, 204, 216), "ceiling")
WALL_A = C((210, 222, 232), "wall_a")
WALL_B = C((200, 212, 224), "wall_b")
WALL_C = C((188, 202, 216), "wall_dark")
TRIM   = C((214, 226, 238), "trim")
PILLAR = C((186, 200, 214), "pillar")
PILLAR_D = C((170, 186, 202), "pillar_dark")
LIGHT  = C((224, 234, 246), "light")
LIGHTW = C((238, 245, 252), "lightw")
GLOW   = C((214, 228, 244), "glow")

WAT0 = C((158, 196, 220), "wat0")
WAT1 = C((146, 188, 214), "wat1")
WAT2 = C((132, 178, 208), "wat2")
WAT3 = C((118, 168, 200), "wat3")
WAT4 = C((104, 156, 190), "wat4")
GRIDL= C((172, 204, 226), "grid")
RIPPL= C((206, 226, 244), "ripple")
REFL = C((226, 240, 250), "refl")

SLIDE   = C((238, 242, 246), "slide")
SLIDE_S = C((206, 214, 224), "slide_shadow")
SLIDE_L = C((250, 253, 255), "slide_light")
SLIDE_D = C((180, 192, 206), "slide_dark")

YELLOW = C((246, 200, 60), "ring")
YEL_D  = C((214, 160, 40), "ring_dark")
YEL_L  = C((255, 226, 120), "ring_light")
RING_SHAD = C((120, 160, 192), "ring_shadow")

HAIR  = C((74, 56, 48), "hair")
SKIN  = C((238, 200, 170), "skin")
SUIT  = C((40, 60, 84), "suit")

WATers = [WAT0, WAT1, WAT2, WAT3, WAT4]

# ================= CEILING =================
c.rect(0, 0, W, 14, SKY)
# fluorescent light fixtures
for lx in (10, 34, 58, 82, 106):
    c.rect(lx, 1, 6, 3, LIGHT)
    c.rect(lx+1, 2, 4, 1, LIGHTW)

# ================= UPPER WALL =================
tile = 8
for ty in range(2, 8):
    for tx in range(16):
        x0 = tx * tile
        y0 = 14 + ty * tile
        col = WALL_A if (tx + ty) % 2 == 0 else WALL_B
        c.rect(x0, y0, tile, tile, col)
# trim / coping at water edge
c.rect(0, 62, W, 3, TRIM)

# ================= FLOOR (visible only at edges? water covers) =================
# implied pool walls sloped - we show side coping
# draw water surface
WATER_TOP = 66
bands = [66, 78, 90, 102, 114]
for i in range(len(bands)):
    y0 = bands[i]
    y1 = (bands[i+1] if i+1 < len(bands) else H)
    c.rect(0, y0, W, y1-y0, WATers[i])

# ================= TILED COLUMNS =================
def column(cx, top, bottom, w=12):
    c.rect(cx, top, w, bottom-top, PILLAR)
    for yy in range(top+6, bottom-2, 14):
        c.line(cx, yy, cx+w-1, yy, PILLAR_D)
    c.line(cx+3, top, cx+3, bottom-1, PILLAR_D)
    c.line(cx+7, top, cx+7, bottom-1, PILLAR_D)
    c.rect(cx, top, w, 2, PILLAR_D)

column(8, 14, H-8, 12)
column(108, 14, H-8, 12)
# farther columns clipped by foreground
column(34, 20, 66, 9)
column(84, 20, 66, 9)

# ================= LIGHT REFLECTIONS =================
for lx, wd in ((11,3),(36,3),(60,3),(84,3),(108,3)):
    col = lx
    for row in range(WATER_TOP, 96):
        w = (row // 2) % 2
        if w:
            c.rect(col, row, wd, 1, REFL)

# ================= RIPPLE LINES =================
for yy in (70, 78, 86, 94, 102, 110, 118, 126):
    off = (yy % 16)
    c.line(0, yy, W-1, yy, RIPPL)

# ================= WATER SPARKLES =================
spark = C((240, 248, 254), "spark")
spark_pts = [(24,70),(40,74),(52,72),(90,76),(66,80),(100,84),(120,74),(14,86),(30,82),(108,90)]
for sx, sy in spark_pts:
    c.rect(sx, sy, 1, 1, spark)

# ================= WATER SLIDE =================
# curving white slide from top-right descending into water
pts = [(102, 20), (99, 30), (94, 42), (88, 54), (82, 66), (78, 76)]
rad = [7, 7, 6.5, 6, 5.5, 5]
# platform at top
c.rect(96, 12, 24, 8, SLIDE)
c.rect(96, 18, 24, 2, SLIDE_D)
for i, (px, py) in enumerate(pts):
    r = rad[i]
    c.circle(px, py, r, SLIDE)
# draw outer tube with darker inner line for depth, and light top on left
for (px, py), r in zip(pts, rad):
    # outline
    c.circle(px, py, r, SLIDE_D, fill=False)
    # top-left highlight
    c.circle(px-1, py-1, max(1, r-3), SLIDE_L, fill=True)
# slide entering water: splash/opening ellipse in water
c.ellipse(78, 78, 10, 3, SLIDE_S, fill=True)
c.ellipse(78, 78, 8, 2, SLIDE, fill=True)

# ================= LIGHT BEAMS =================
beam = C((224, 236, 248, 46), "beam")
for lx in (10, 34, 58, 82, 106):
    c.poly([(lx+2, 4), (lx+4, 4), (lx+4, WATER_TOP+4), (lx+2, WATER_TOP+4)], beam)


# ================= GIRL IN SWIM RING =================
# ring floating in middle, seen from behind
rx, ry = 58, 100   # ring center
c.ellipse(rx, ry, 13, 6, RING_SHAD, fill=True)  # shadow on water
c.ellipse(rx, ry, 12, 5, YELLOW, fill=True)
c.ellipse(rx, ry, 8, 3, YEL_D, fill=True)       # inner hole (on water)
c.ellipse(rx, ry, 8, 3, WAT2, fill=True)
# ring highlight
c.line(rx-9, ry-2, rx+2, ry-3, YEL_L)
# girl seen from behind
# body / shoulders
c.ellipse(rx, ry-6, 7, 8, SUIT, fill=True)
# arms resting on ring
c.ellipse(rx-9, ry-3, 3, 2, SKIN, fill=True)
c.ellipse(rx+9, ry-3, 3, 2, SKIN, fill=True)
# head from behind
c.circle(rx, ry-15, 6, HAIR)
c.circle(rx, ry-15, 6, HAIR, fill=True)
# hair highlight
c.circle(rx-2, ry-17, 2, (104,86,74), fill=True)
C((104,86,74), "hair_h")
# braid/hair
c.circle(rx, ry-12, 4, HAIR, fill=True)

# reflections under ring
c.ellipse(rx, ry+7, 9, 2, YEL_D, fill=True)
c.ellipse(rx, ry+10, 7, 2, (176,196,216), fill=True)
C((176,196,216), "refl2")

# ================= PILLAR COLUMNS IN FOREGROUND again (in front of water/slide) =================
column(8, 14, H-8, 12)
column(108, 14, H-8, 12)

print(c.stats_text())
print("palette:", len(c.palette()))
finish(c)
