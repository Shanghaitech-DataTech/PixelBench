from pixelbench_api import *

W = H = 128

# ----- palette colours -----
SKY      = (126, 200, 242)      # clear blue sky
SKY_UP   = (116, 190, 238)
CLOUD    = (255, 255, 255)
SUN      = (255, 226, 84)
SUN_CORE = (255, 240, 160)
SEA_DEEP = (24, 90, 168)
SEA_M1   = (42, 122, 196)
SEA_M2   = (58, 152, 216)
SEA_L    = (84, 182, 228)
SEA_TQ   = (96, 204, 218)
SEA_TEA  = (66, 196, 196)
FOAM     = (246, 250, 253)
SAND     = (244, 208, 140)
SAND_DK  = (230, 190, 112)
SAND_WET = (214, 192, 130)
UMB_RED  = (221, 44, 54)
UMB_WH   = (250, 250, 250)
POLE     = (128, 84, 46)
TOWEL_A  = (244, 120, 120)      # coral
TOWEL_B  = (255, 248, 240)
FLIP_A   = (232, 60, 72)
FLIP_B   = (255, 250, 245)
BOAT     = (255, 250, 245)
HULL     = (190, 70, 50)

c = new_canvas(W, H, name="summer-seaside")

# ---- sky ----
c.rect(0, 0, W, 52, SKY)
# subtle sky gradient band at very top
c.rect(0, 0, W, 8, SKY_UP)

# ---- sun ----
SCX, SCY, SR = 104, 22, 12
c.circle(SCX, SCY, SR, SUN)
c.circle(SCX, SCY, SR - 3, SUN_CORE)

# ---- gulls ----
def gull(cv, x, y, col):
    # body horizontal, wings lifted
    cv.line(x, y, x + 6, y, col)
    cv.line(x, y,   x - 1, y - 3, col)
    cv.line(x + 5, y, x + 7, y - 2, col)
gull(c, 56, 28, CLOUD)
gull(c, 82, 16, CLOUD)

# ---- clouds (soft white blobs) ----
def cloud(cv, x, y, s):
    r = 4 * s
    cv.circle(x, y, r, CLOUD)
    cv.circle(x - 3 * s, y + s, r - 1, CLOUD)
    cv.circle(x + 3 * s, y + 1, r - 1, CLOUD)
    cv.circle(x, y - s, r - 1, CLOUD)
cloud(c, 20, 20, 2)
cloud(c, 40, 34, 1)
cloud(c, 70, 42, 2)
cloud(c, 102, 38, 1)

# ---- sea ----
# horizon at y=52, shore at y=88
c.rect(0, 52, W, 6,  SEA_DEEP)   # deep blue at horizon
c.rect(0, 58, W, 6,  SEA_M1)
c.rect(0, 64, W, 6,  SEA_M2)
c.rect(0, 70, W, 6,  SEA_L)
c.rect(0, 76, W, 6,  SEA_TQ)
c.rect(0, 82, W, 8,  SEA_TEA)    # teal near shore

# subtle wave lines in the sea
c.line(0, 60, W-1, 60, (70, 160, 220))
c.line(0, 67, W-1, 67, (78, 172, 226))
c.line(0, 74, W-1, 74, (90, 190, 224))
c.line(0, 80, W-1, 80, (88, 206, 216))

# ---- sailboat far out ----
bx, base = 26, 70
c.line(bx, 60, bx, base, POLE)
c.poly([(bx, 59), (bx, base - 2), (bx + 7, base - 3)], BOAT, fill=True)
c.poly([(bx, 59), (bx, base - 2), (bx - 5, base - 3)], CLOUD, fill=True)
c.rect(bx - 5, base - 2, 12, 3, HULL)

# reflection glint
c.line(bx + 2, base + 3, bx + 5, base + 5, (120, 210, 235))

# ---- sand ----
c.rect(0, 88, W, 40, SAND)
# wet sand band near shore
c.rect(0, 88, W, 5, SAND_WET)
# speckles
for (sx, sy) in [(12, 100), (50, 96), (90, 122), (20, 118), (112, 126), (66, 124), (100, 106)]:
    c.set(sx, sy, SAND_DK)

# ---- foam waves rolling onto sand ----
foam_pts = [(0, 87), (8, 89), (18, 86), (28, 89), (40, 87), (52, 90),
           (62, 87), (72, 89), (84, 86), (95, 90), (106, 87), (116, 90),
           (124, 87)]
for i in range(len(foam_pts) - 1):
    x, y = foam_pts[i]
    c.circle(x, y, 3, FOAM)
    c.line(x, y, foam_pts[i+1][0], y + 1, FOAM)
# a few foam flecks further up the sand
c.set(34, 92, FOAM); c.set(78, 93, FOAM); c.set(110, 93, FOAM)

# ---- beach umbrella ----
# canopy fan of alternating red / white wedges from apex
ax, ay = 96, 80
bases = []
n = 7
for i in range(n + 1):
    t = i / n
    bx2 = 72 + t * 46          # x from 72..118
    by2 = 95 + int(11 * (1 - abs(t - 0.5) * 2) ** 0.6)  # curved bottom
    bases.append((bx2, by2))
for i in range(n):
    col = UMB_RED if i % 2 == 0 else UMB_WH
    base_pt = [(ax, ay), bases[i], bases[i+1]]
    c.poly(base_pt, col, fill=True)
# canopy dome top cap
c.circle(ax, ay, 8, UMB_RED)
c.line(ax - 8, ay, ax + 8, ay, UMB_RED)
# pole
c.line(ax, ay + 6, ax, 122, POLE)

# ---- striped towel ----
tx, ty, tw = 26, 100, 46
tow_h = 20
c.rect(tx, ty, tw, tow_h, TOWEL_B)
stripes = tw // 7
for i in range(0, tw, 2 * 7):
    if i + 7 > tw:
        c.rect(tx + i, ty, tw - i, tow_h, TOWEL_A)
    else:
        c.rect(tx + i, ty, 7, tow_h, TOWEL_A)
# towel shadow
c.rect(tx + 2, ty + tow_h, tw - 4, 3, SAND_DK)

# ---- flip-flops ----
def flipflop(cv, x, y, s=1):
    # sole
    cv.scale = 1
    cv.ellipse(x, y, 5 * s, 3 * s, FLIP_A)
    # strap (y shape)
    cv.line(x - 2, y - 1, x, y - 3, FLIP_B)
    cv.line(x + 2, y - 1, x, y - 3, FLIP_B)
    cv.line(x, y - 3, x, y - 2, FLIP_B)
flipflop(c, 68, 106)
flipflop(c, 76, 110)

# a small sand castle hint by the towel
c.poly([(12, 122), (12, 110), (22, 122)], SAND_DK, fill=True)
c.poly([(23, 122), (23, 114), (31, 122)], SAND_DK, fill=True)

print(c.stats_text())
finish(c)
