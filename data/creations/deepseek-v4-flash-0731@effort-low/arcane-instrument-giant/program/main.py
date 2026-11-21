from pixelbench_api import *
import math

W = H = 256
OUT = "#0a0a0f"

# ---------------------------------------------------------------------------
# BASE / BACKGROUND : dark hall
# ---------------------------------------------------------------------------
bg = new_canvas(W, H, background="#06070d", name="bg")
c = bg
c.rect(0, 0, W, H, "#06070d")

# vignette corners (darker)
for (x0, y0, x1, y1) in [(0, 0, 60, 60), (W - 60, 0, 60, 60), (0, H - 60, 60, 60), (W - 60, H - 60, 60, 60)]:
    c.rect(x0, y0, x1, y1, "#030409")

# distant arch lines / architecture (very faint)
arch_col = "#0c0f1a"
# vertical pillars
c.rect(14, 0, 8, H, "#090b14")
c.rect(W - 22, 0, 8, H, "#090b14")
# arch hint
c.path("M 10 256 L 10 120 Q 128 30 246 120 L 246 256", arch_col, fill=False)
c.rect(10, 120, 8, 136, arch_col)
c.rect(238, 120, 8, 136, arch_col)

# floor line / perspective shadow floor
c.rect(30, 235, 196, 21, "#050609")
c.poly([(60, 235), (128, 246), (196, 235), (222, 256), (34, 256)], "#04050a", fill=True)

# faint misty glow pool rising behind instrument (opaque dim so still dark-ish)
c.path("M 60 235 C 70 150 186 150 196 235 Z", "#0a0e1a", fill=True)

# ---------------------------------------------------------------------------
# GLOW LAYER : halos & light shafts (semi-transparent, flattened later)
# ---------------------------------------------------------------------------
gl = new_canvas(W, H, name="glow")
g = gl

# big teal back-halo behind instrument (semitransparent blend)
g.circle(128, 102, 120, (5, 28, 42, 70), fill=True)
g.circle(128, 102, 106, (18, 62, 78, 60), fill=True)
g.circle(128, 102, 92, (24, 112, 128, 55), fill=True)
g.circle(128, 102, 76, (30, 148, 162, 60), fill=True)
g.circle(128, 102, 60, (40, 190, 200, 70), fill=True)

# light shafts from above
g.poly([(96, 0), (150, 0), (168, 180), (60, 200)], (12, 22, 40, 90), fill=True)
g.poly([(170, 0), (205, 0), (178, 150), (146, 170)], (12, 22, 40, 80), fill=True)
# warm light from core casting down
g.poly([(108, 118), (148, 118), (176, 235), (92, 235)], (150, 120, 30, 22), fill=True)

# ---------------------------------------------------------------------------
# PEDESTAL : stone
# ---------------------------------------------------------------------------
pd = new_canvas(W, H, name="pedestal")
p = pd
stone_d = "#1d1d26"
stone_m = "#3a3a45"
stone_l = "#55555f"
stone_hl = "#6e6e79"
stone_dk = "#101017"

# base tiers
p.rect(52, 244, 152, 12, "#0b0b12")
p.rect(66, 234, 124, 10, "#14141c")
# column
p.rect(88, 208, 80, 26, stone_m)
p.rect(88, 208, 80, 2, stone_hl)
p.rect(88, 232, 80, 2, stone_dk)
# top platform
p.rect(70, 200, 116, 8, stone_l)
p.rect(70, 200, 116, 2, stone_hl)
p.rect(70, 207, 116, 2, stone_dk)
# pedestal ring grooves
p.rect(88, 216, 80, 2, "#0d0d13")
p.rect(88, 222, 80, 2, stone_d)
# glowing symbol on pedestal face
for (dx, dy) in [(0, 2), (0, 0), (0, -2), (-4, 3), (4, -3)]:
    p.set(128 + dx, 226 + dy, "#0c4250")
p.circle(128, 226, 7, "#0c4250", fill=False)

# small glow on pedestal top catching light
p.poly([(74, 202), (182, 202), (178, 208), (78, 208)], "#13192a", fill=True)

# ---------------------------------------------------------------------------
# INSTRUMENT LAYER : brass astrolabe-orrery
# ---------------------------------------------------------------------------
it = new_canvas(W, H, name="instrument")
i = it
CX, CY = 128, 100

# brass palette
b_dark = "#241a07"    # dark brass
b_deep = "#3a2b0e"
b_base = "#6b4a12"
b_mid  = "#9c6f1d"
b_lig  = "#c8932b"
b_hi   = "#e2b24a"
b_bri  = "#f2d47c"
b_whi  = "#fbeeb8"
eng_d  = "#2a2008"    # engraving dark
eng_l  = "#e0c06a"    # engraving light
teal   = "#0e5a6b"
tea_c  = "#2fb7c7"
tea_b  = "#a2f2f6"
tea_h  = "#e4ffff"
goldw  = "#fff6d0"

# ---- outer mechanic scaffold / floating stand arms from pedestal up
i.line(CX, 200, CX, 206, eng_d)
i.line(CX - 3, 202, CX + 3, 202, b_base)
i.circle(CX, 208, 6, b_deep, fill=False)

# ---- outer rim annulus
i.circle(CX, CY, 104, OUT, fill=True)
i.circle(CX, CY, 102, b_deep, fill=True)
i.circle(CX, CY, 97, b_base, fill=True)
# engraved outer band (97..89)
i.circle(CX, CY, 93, eng_d, fill=False)
i.circle(CX, CY, 92, b_lig, fill=False)
i.circle(CX, CY, 90, eng_d, fill=False)
i.circle(CX, CY, 89, b_hi, fill=False)
# rim light rims
i.circle(CX, CY, 98, eng_l, fill=False)
i.circle(CX, CY, 102, b_lig, fill=False)

# ---- outer tick marks / engraved scale between 84..78
for k in range(36):
    a0 = 2 * math.pi * k / 36
    for t in (1, 2):
        a = a0 + t * 0.008
    r0 = 86
    i.line(int(CX + math.cos(a0) * r0), int(CY + math.sin(a0) * r0),
           int(CX + math.cos(a0 + 0.06) * 78), int(CY + math.sin(a0 + 0.06) * 78), eng_d)
# bright running point on scale
i.circle(int(CX + math.cos(-1.1) * 82), int(CY + math.sin(-1.1) * 82), 2, tea_b, fill=True)

# ---- second big engraved band (72..60)
i.circle(CX, CY, 74, eng_d, fill=False)
i.circle(CX, CY, 72, b_base, fill=True)
i.circle(CX, CY, 67, b_mid, fill=False)
i.circle(CX, CY, 66, eng_d, fill=False)
i.circle(CX, CY, 65, b_hi, fill=False)
i.circle(CX, CY, 63, b_mid, fill=True)
i.circle(CX, CY, 61, eng_l, fill=False)

# ---- nested rings (52..44)
i.circle(CX, CY, 56, eng_d, fill=False)
i.circle(CX, CY, 53, b_deep, fill=True)
i.circle(CX, CY, 50, eng_l, fill=False)
i.circle(CX, CY, 48, b_mid, fill=False)
i.circle(CX, CY, 46, eng_d, fill=False)
i.circle(CX, CY, 44, b_hi, fill=False)

# ---- alchemical dial-ish rings inner (40..30)
i.circle(CX, CY, 41, eng_d, fill=False)
i.circle(CX, CY, 39, b_lig, fill=False)
i.circle(CX, CY, 37, b_deep, fill=True)
i.circle(CX, CY, 33, eng_d, fill=False)
i.circle(CX, CY, 31, tea_c, fill=False)

# ---- spokes / cross arms connecting rings
for k in range(8):
    a = 2 * math.pi * k / 8 + 0.35
    i.line(CX, CY, int(CX + math.cos(a) * 95), int(CY + math.sin(a) * 95), eng_d)
    i.line(int(CX + math.cos(a) * 40), int(CY + math.sin(a) * 40),
           int(CX + math.cos(a) * 80), int(CY + math.sin(a) * 80), b_lig)

# ---- pivot ring connecting inner to frame at 4 cardinal points
for (ax, ay) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    i.circle(CX + int(ax * 72), CY + int(ay * 72), 6, b_base, fill=True)
    i.circle(CX + int(ax * 72), CY + int(ay * 72), 4, b_hi, fill=False)
    i.circle(CX + int(ax * 88), CY + int(ay * 88), 3, b_deep, fill=True)

# ---- crystal spheres orbiting (or-peer ring at radius ~90)
def sphere(ax, ay, r):
    for rr in range(int(r * 2.4), 0, -1):
        i.circle(CX + int(ax * r), CY + int(ay * r), rr, g.color("#0e5a6b"))
    for rr in range(int(r * 1.5), 0, -1):
        i.circle(CX + int(ax * r), CY + int(ay * r), rr, tea_c)
    i.circle(CX + int(ax * r), CY + int(ay * r), int(r * 0.85), tea_b, fill=True)
    i.circle(CX + int(ax * r) - int(r * 0.3), CY + int(ay * r) - int(r * 0.35), int(r * 0.35), tea_h, fill=True)

sphere(math.cos(0.7), math.sin(0.7), 7)
sphere(math.cos(-1.6), math.sin(-1.6), 6)
sphere(math.cos(2.7), math.sin(2.7), 5)
# small moons
sphere(math.cos(1.9), math.sin(1.9), 3)

# ---- gears
def gear(gx, gy, r, teeth):
    for k in range(teeth):
        a = 2 * math.pi * k / teeth
        i.circle(int(gx + math.cos(a) * (r + 1)), int(gy + math.sin(a) * (r + 1)), 1, b_lig, fill=True)
    i.circle(gx, gy, r, eng_d, fill=True)
    i.circle(gx, gy, r - 1, b_mid, fill=True)
    i.circle(gx, gy, r - 3, b_hi, fill=False)
    i.circle(gx, gy, int(r * 0.6), eng_d, fill=True)
    i.circle(gx, gy, int(r * 0.5), b_base, fill=True)
    i.circle(gx, gy, 2, eng_d, fill=True)
    for k in range(4):
        a = 2 * math.pi * k / 4
        i.line(int(gx + math.cos(a) * 4), int(gy + math.sin(a) * 4),
               int(gx + math.cos(a) * int(r * 0.72)), int(gy + math.sin(a) * int(r * 0.72)), eng_d)

gear(128, 128, 15, 12)
gear(96, 108, 10, 8)
gear(160, 108, 10, 8)
gear(128, 158, 7, 9)
gear(110, 150, 6, 7)
gear(146, 150, 6, 7)

# ---- alchemical dials
def dial(gx, gy, r):
    i.circle(gx, gy, r + 2, eng_d, fill=True)
    i.circle(gx, gy, r, b_deep, fill=True)
    i.circle(gx, gy, r - 1, b_mid, fill=False)
    for k in range(5):
        a = 2 * math.pi * k / 5
        i.line(gx, gy, int(gx + math.cos(a) * (r - 2)), int(gy + math.sin(a) * (r - 2)), eng_d)
    i.circle(gx, gy, 2, b_bri, fill=True)
dial(78, 128, 9)
dial(178, 128, 9)
dial(128, 62, 8)

# small screws on outer frame
for k in range(6):
    a = 2 * math.pi * k / 6 + 0.5
    i.circle(int(CX + math.cos(a) * 93), int(CY + math.sin(a) * 93), 2, b_lig, fill=True)
    i.circle(int(CX + math.cos(a) * 93), int(CY + math.sin(a) * 93), 1, eng_d, fill=True)

# ---- glowing runes along the rings
def stamp_rune(gx, gy, glyph, radius, ang):
    bx = CX + math.cos(ang) * radius
    by = CY + math.sin(ang) * radius
    for (dx, dy) in glyph:
        ca, sa = math.cos(ang), math.sin(ang)
        rx, ry = dx * ca - dy * sa, dx * sa + dy * ca
        X, Y = int(round(bx + rx)), int(round(by + ry))
        for (ox, oy) in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            i.set(X + ox, Y + oy, "#0d3f4e")
        i.set(X, Y, tea_b)

G1 = [(0, -3), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (0, 3), (2, 3), (3, 4), (1, 4)]
G2 = [(-3, -3), (3, -3), (-3, 0), (3, 0), (-3, 3), (3, 3), (-3, -1), (3, 1)]
G3 = [(0, -3), (0, 3), (-3, -2), (3, 2), (-1, 2), (1, -2), (0, 0)]
G4 = [(0, -4), (-1, -1), (1, -1), (-1, 1), (1, 1), (0, 2), (0, 3), (0, -2)]
G5 = [(-1, -4), (1, -2), (-1, 0), (1, 2), (-1, 4), (0, -3), (0, 1)]
G6 = [(-2, -3), (2, -3), (-2, 3), (2, 3), (-2, -1), (2, 1), (0, -2), (0, 0), (0, 2)]
runes = [G1, G2, G3, G4, G5, G6]
n = len(runes)
for k in range(n):
    stamp_rune(CX, CY, runes[k], 90, 2 * math.pi * k / n + 0.2)

# inner rune band (ring 66)
for k in range(8):
    a = 2 * math.pi * k / 8 + 0.9
    stamp_rune(CX, CY, [G2, G3, G5][k % 3], 66, a)

# ---- central radiant core
i.circle(CX, CY, 30, eng_d, fill=True)
i.circle(CX, CY, 26, b_mid, fill=True)
i.circle(CX, CY, 24, b_hi, fill=False)
i.circle(CX, CY, 20, tea_c, fill=True)
i.circle(CX, CY, 16, g.color("#eaff9f"), fill=True)
i.circle(CX, CY, 12, g.color("#fff3a6"), fill=True)
i.circle(CX, CY, 8, g.color("#fff8d8"), fill=True)
i.circle(CX, CY, 5, g.color("#ffffff"), fill=True)
# rays
for k in range(12):
    a = 2 * math.pi * k / 12
    i.line(int(CX + math.cos(a) * 22), int(CY + math.sin(a) * 22),
           int(CX + math.cos(a) * 34), int(CY + math.sin(a) * 34), eng_d)
    i.line(int(CX + math.cos(a) * 23), int(CY + math.sin(a) * 23),
           int(CX + math.cos(a) * 31), int(CY + math.sin(a) * 31), b_bri)
# inner engraved sun-dial hands
i.line(CX, CY, int(CX + 40), CY, eng_d)
i.line(int(CX + 6), CY, int(CX + 38), CY, b_hi)
# cross guard
i.line(CX - 34, int(CY + 30), CX + 34, int(CY + 30), eng_d)
i.line(CX, CY + 32, CX, int(CY + 40), b_lig)

# ---- dark outline over whole instrument for crisp engraved silhouette
i.outline(OUT)

# ---------------------------------------------------------------------------
# Compose
# ---------------------------------------------------------------------------
result = flatten([bg, gl, pd, it], name="result")

# final composite generally; dark outline already on instrument layer.
print("colors:", result.stats()["colors_used"])
finish(result)
