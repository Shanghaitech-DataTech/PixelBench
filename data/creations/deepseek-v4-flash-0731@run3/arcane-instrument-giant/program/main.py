from pixelbench_api import *
import math, random
random.seed(1207)

W = H = 256
CX, CY = 128, 112
RF = 0.55
OUT = (2, 1, 0)

# ---------------------------------------------------------------- palette
BG_BASE = (4, 5, 9)
ARC_C = (24, 27, 46)
ST_D = (12, 13, 20)
ST_C = (22, 25, 36)
ST_M = (34, 38, 52)
ST_L = (48, 54, 72)
ST_H = (62, 70, 92)
ST_B = (84, 94, 120)
ST_DK = (28, 32, 45)
PLATE = (38, 28, 17)
BRASS = (150, 112, 56)
BRD = (88, 66, 38)
BRL = (206, 164, 92)
GOLD = (238, 198, 124)
GRO = (54, 40, 22)
COP = (128, 80, 48)
RUNE = (96, 235, 195)
RUNED = (42, 140, 122)

# ================================================================ BACKGROUND
bg = new_canvas(W, H, name="bg")
bg.rect(0, 0, W, H, BG_BASE)
steps = 22
for i in range(steps, 0, -1):
    r = int(188 * i / steps)
    t = (steps - i) / steps
    bg.circle(CX, CY - 4, r, (int(4 + 16 * t), int(5 + 18 * t), int(9 + 32 * t)))
bg.rect(0, 214, W, 42, (7, 9, 15))
bg.ellipse(CX, 254, 158, 252, ARC_C, fill=False)
bg.line(CX - 158, 254, CX - 158, 30, ARC_C)
bg.line(CX + 158, 254, CX + 158, 30, ARC_C)
for px in (16, 206):
    bg.rect(px, 0, 34, H, (13, 15, 27))
    bg.rect(px + 3, 0, 28, H, (19, 22, 37))
    bg.rect(px + 9, 0, 16, H, (27, 30, 51))
    bg.rect(px + 12, 0, 8, H, (35, 39, 64))
for sx in range(26, 240, 40):
    bg.line(sx, 222, sx, 256, (6, 7, 13))
    bg.line(sx, 222, sx + 40, 222, (6, 7, 13))

# ================================================================ PEDESTAL
ped = new_canvas(W, H, name="ped")
ped.ellipse(CX, 182, 88, 15, ST_D)                 # floating shadow
ped.rect(88, 178, 80, 8, ST_M)
ped.rect(90, 180, 76, 3, ST_H)
ped.rect(80, 186, 96, 30, ST_L)
ped.rect(86, 192, 84, 24, ST_H)
ped.rect(93, 197, 70, 19, ST_B)
ped.rect(82, 214, 92, 18, ST_C)
ped.rect(70, 228, 116, 14, ST_L)
ped.rect(60, 240, 136, 16, ST_DK)
for yy in (200, 210):
    ped.line(94, yy, 162, yy, ST_C)
    ped.line(95, yy + 1, 161, yy + 1, ST_L)
for gx in (104, 128, 152):
    ped.line(gx, 214, gx, 219, (60, 150, 150))
ped.line(126, 214, 130, 218, (60, 150, 150))

# ================================================================ INSTRUMENT
inst = new_canvas(W, H, name="inst")

def el(rx, col, fill=True):
    inst.ellipse(CX, CY, rx, int(rx * RF), col, fill=fill)

def band(ro, ri):
    el(ro, BRASS)
    el(ri, PLATE)
    el(ro, OUT, fill=False)
    el(ro - 1, BRL, fill=False)
    el(ri + 1, BRD, fill=False)

def ticks(ro, ri, n):
    rm = (ro + ri) // 2
    for i in range(n):
        a = 2 * math.pi * i / n
        ca = math.cos(a); sa = math.sin(a)
        x0 = CX + ca * ri; y0 = CY + sa * ri * RF
        x1 = CX + ca * rm; y1 = CY + sa * rm * RF
        inst.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), GRO)

inst.ellipse(CX, CY, 112, int(112 * RF), PLATE)
# lit-from-above warm highlight: thin crescent near top only
inst.ellipse(CX, CY - 10, 104, 40, (110, 88, 52, 62))
inst.ellipse(CX, CY - 22, 84, 22, (146, 118, 72, 52))
inst.ellipse(CX, CY - 30, 64, 12, (176, 144, 92, 46))
band(112, 105); ticks(112, 105, 36)
band(97, 91);   ticks(97, 91, 24)
band(83, 77)
band(69, 63)
band(56, 50);   ticks(56, 50, 18)
band(43, 38);   ticks(43, 38, 14)
band(30, 25)
ticks(25, 16, 12)

# engraved radial spokes
for i in range(12):
    a = 2 * math.pi * i / 12 + math.pi / 12
    ca = math.cos(a); sa = math.sin(a)
    inst.line(int(round(CX + ca * 10)), int(round(CY + sa * 10 * RF)),
             int(round(CX + ca * 97)), int(round(CY + sa * 97 * RF)), GRO)
# etched arcs crossing the plate (ornament)
for rr in (58, 47, 36, 24):
    inst.ellipse(CX, CY, rr, int(rr * 0.5), (70, 52, 30, 90), fill=False)
# top-lit highlights on upper arcs
for rr in (110, 95, 81, 67, 54, 41):
    inst.ellipse(CX, CY - 3, rr, int(rr * 0.5), (228, 200, 148, 60), fill=False)

# rivets around rim band
for i in range(12):
    a = 2 * math.pi * i / 12
    ca = math.cos(a); sa = math.sin(a)
    rm = 108
    inst.set(int(round(CX + ca * rm)), int(round(CY + sa * rm * RF)), GOLD)

# alchemical dots on band(83,77)
for i in range(6):
    a = 2 * math.pi * i / 6
    px = CX + math.cos(a) * 80; py = CY + math.sin(a) * 80 * RF
    inst.circle(int(round(px)), int(round(py)), 2, GOLD)

# runes along ringC (r=66)
RUNES = [
    [(0, 0, 0, 4), (0, 0, 2, 1), (1, 1, 1, 4), (0, 4, 2, 4)],
    [(0, 0, 2, 0), (0, 4, 2, 4), (2, 0, 2, 4), (2, 4, 0, 1)],
    [(0, 1, 2, 1), (1, 1, 1, 4), (1, 4, 1, 5)],
    [(1, 0, 1, 4), (1, 0, 2, 0), (1, 2, 2, 4), (1, 4, 0, 3)],
    [(0, 0, 0, 4), (0, 4, 2, 2), (0, 0, 2, 2)],
    [(0, 1, 2, 1), (0, 1, 1, 4), (2, 1, 1, 4)],
    [(2, 0, 0, 2), (0, 2, 2, 4), (2, 2, 1, 4), (1, 2, 1, 4)],
    [(0, 0, 2, 0), (0, 0, 0, 4), (0, 4, 2, 4)],
]
for i, rr in enumerate(RUNES):
    a = 2 * math.pi * i / 8
    px = CX + math.cos(a) * 66; py = CY + math.sin(a) * 66 * RF
    bx = int(round(px - 1)); by = int(round(py - 2))
    for (x0, y0, x1, y1) in rr:
        inst.line(bx + x0, by + y0, bx + x1, by + y1, RUNE)
for i in range(8):
    a = 2 * math.pi * i / 8 + math.pi / 8
    px = CX + math.cos(a) * 44
    py = CY + math.sin(a) * 44 * RF
    inst.set(int(round(px)), int(round(py)), RUNED)

# top finial
inst.line(CX - 4, CY - 62, CX - 4, CY - 70, BRD)
inst.line(CX + 4, CY - 62, CX + 4, CY - 70, BRD)
inst.circle(CX, CY - 72, 3, BRASS)
inst.circle(CX, CY - 72, 3, OUT, fill=False)
inst.circle(CX, CY - 73, 1, GOLD)

# gears
def gear(cx, cy, r, teeth):
    n = teeth
    for i in range(n):
        a = 2 * math.pi * i / n
        x0 = cx + math.cos(a) * (r - 1); y0 = cy + math.sin(a) * (r - 1)
        x1 = cx + math.cos(a) * (r + 2); y1 = cy + math.sin(a) * (r + 2)
        inst.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), BRD)
    inst.circle(cx, cy, r, BRD)
    inst.circle(cx, cy, r, OUT, fill=False)
    inst.circle(cx, cy, r - 3, BRL, fill=False)
    inst.circle(cx, cy, r - 5, BRASS)
    inst.circle(cx, cy, r - 5, OUT, fill=False)
    inst.circle(cx, cy, 2, OUT)
    inst.circle(cx, cy, 1, GOLD)

gear(70, 96, 9, 8)
gear(186, 96, 9, 8)
gear(128, 158, 10, 9)
gear(96, 70, 7, 6)
gear(160, 70, 7, 6)
gear(52, 134, 6, 6)
gear(204, 134, 6, 6)
gear(128, 60, 5, 5)

# alchemical dials
def dial(cx, cy, r, ang):
    inst.circle(cx, cy, r + 1, OUT, fill=False)
    inst.circle(cx, cy, r, COP)
    inst.circle(cx, cy, r, OUT, fill=False)
    for i in range(8):
        a = 2 * math.pi * i / 8
        x0 = cx + math.cos(a) * (r - 1); y0 = cy + math.sin(a) * (r - 1)
        x1 = cx + math.cos(a) * (r - 4); y1 = cy + math.sin(a) * (r - 4)
        inst.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), GRO)
    inst.line(cx, cy, int(round(cx + math.cos(ang) * (r - 3))), int(round(cy + math.sin(ang) * (r - 3))), GOLD)
    inst.line(cx, cy, int(round(cx - math.cos(ang) * 2)), int(round(cy - math.sin(ang) * 2)), GOLD)
    inst.circle(cx, cy, 3, BRASS)
    inst.circle(cx, cy, 1, GOLD)

dial(62, 62, 11, 0.9)
dial(194, 62, 11, 2.3)

# core mount ring
inst.circle(CX, CY, 14, BRL)
inst.circle(CX, CY, 13, OUT, fill=False)

# ================================================================ SPHERES
sph = new_canvas(W, H, name="sph")

def sphere(cx, cy, r):
    sph.circle(cx, cy, r + 2, (150, 205, 250, 40))
    sph.circle(cx, cy, r + 1, (150, 205, 250, 80), fill=False)
    sph.ellipse(cx, cy, r + 1, int((r + 1) * 0.62), (64, 132, 205, 80), fill=False)
    sph.ellipse(cx, cy, r, int(r * 0.66), (64, 132, 205, 60), fill=False)
    sph.circle(cx, cy, r, (100, 168, 235, 128))
    sph.circle(cx, cy, r - 1, (62, 128, 200, 100))
    sph.circle(cx, cy, r + 1, (168, 214, 250, 60), fill=False)
    sph.circle(cx - 2, cy - 2, max(1, int(r * 0.45)), (198, 234, 255, 170))
    sph.circle(cx - 2, cy - 2, max(1, int(r * 0.26)), (236, 250, 255, 235))
    sph.circle(cx, cy, r + 1, (210, 235, 255, 100), fill=False)
    sph.circle(cx, cy, 1, (255, 255, 255, 250))
    sph.ellipse(cx + 2, cy + 3, max(1, int(r * 0.5)), max(1, int(r * 0.2)), (24, 46, 92, 70))

# support arms (arms on inst below spheres, spheres drawn after inst)
for a in (0.9, 2.3, 4.2):
    ca = math.cos(a); sa = math.sin(a)
    x0 = CX + ca * 66; y0 = CY + sa * 66 * RF
    inst.line(int(round(x0)), int(round(y0)), int(round(x0 + ca * 30)), int(round(y0 + sa * 20)), BRL)

sphere(128, 84, 8)
sphere(64, 128, 7)
sphere(192, 128, 7)
sphere(128, 148, 8)
sphere(96, 66, 5)
sphere(160, 66, 5)

# ================================================================ CORE
core = new_canvas(W, H, name="core")
core.circle(CX, CY, 9, (255, 244, 212))
core.circle(CX, CY, 7, (255, 232, 168))
core.circle(CX, CY, 5, (255, 250, 236))
core.circle(CX, CY, 3, (255, 255, 255))
core.circle(CX, CY, 2, (255, 255, 255), fill=False)
# orbit ring around core
core.circle(CX, CY, 17, (170, 220, 255, 90), fill=False)
core.circle(CX, CY, 18, (120, 200, 250, 60), fill=False)

# ================================================================ GLOWS
glowb = new_canvas(W, H, name="glowb")
glowb.circle(CX, CY, 120, (255, 168, 84, 16))
glowb.circle(CX, CY, 98, (255, 182, 96, 26))
glowb.circle(CX, CY, 76, (255, 198, 118, 40))

glowf = new_canvas(W, H, name="glowf")
# light shafts
glowf.poly([(112, 0), (146, 0), (168, 120), (150, 120)], (255, 236, 192, 13))
glowf.poly([(110, 116), (146, 116), (150, 40), (114, 40)], (255, 240, 200, 10))
# god rays from core
for i in range(12):
    a = 2 * math.pi * i / 12 + 0.2
    for rr in (16, 46):
        glowf.line(int(round(CX + math.cos(a) * rr)), int(round(CY + math.sin(a) * rr)),
                  int(round(CX + math.cos(a) * (rr + 15))), int(round(CY + math.sin(a) * (rr + 15))), (255, 226, 156, 44))
# glow ring around whole instrument
glowf.circle(CX, CY, 117, (255, 192, 128, 34), fill=False)
glowf.circle(CX, CY, 114, (150, 200, 255, 40), fill=False)
# rune halos
for i in range(8):
    a = 2 * math.pi * i / 8
    px = CX + math.cos(a) * 66; py = CY + math.sin(a) * 66 * RF
    glowf.circle(int(round(px)), int(round(py)), 4, (110, 240, 205, 60))
glowf.ellipse(CX, 184, 58, 13, (255, 200, 130, 30))
glowf.line(CX, CY + 12, CX, 158, (255, 234, 200, 24))
# diamond flares
glowf.poly([(128, 40), (140, 128), (128, 196), (116, 128)], (255, 240, 210, 30))

# ================================================================ SPARKLE
spark = new_canvas(W, H, name="spark")
for (sx, sy) in [(128, 40), (44, 58), (212, 60), (30, 142), (226, 146), (70, 192), (186, 192), (128, 210),
                (58, 30), (198, 30), (38, 100), (218, 100)]:
    spark.circle(sx, sy, 1, (255, 255, 246, 96))
    spark.set(sx, sy, (255, 255, 255, 210))
for i in range(26):
    x = random.randint(0, 255); y = random.randint(0, 255)
    if (x, y) not in [(128, 128)]:
        spark.circle(x, y, 1, (232, 250, 255, 66))

# ================================================================ COMPOSE
limit = 136

def reduce_to(cv, lim):
    w, h, rgba = cv.to_rgba()
    d = {}
    order = []
    for y in range(h):
        base = y * w * 4
        for x in range(w):
            o = base + x * 4
            a = rgba[o + 3]
            if a == 0:
                continue
            k = (rgba[o], rgba[o + 1], rgba[o + 2], a)
            if k not in d:
                d[k] = []
                order.append(k)
            d[k].append((x, y))
    keys = order[:]
    it = 0
    while len(keys) > lim:
        it += 1
        bi = bj = -1; bd = None
        for i in range(len(keys)):
            c1 = keys[i]
            for j in range(i + 1, len(keys)):
                c2 = keys[j]
                dd = (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2 + ((c1[3] - c2[3]) ** 2) // 2
                if bd is None or dd < bd:
                    bd = dd; bi = i; bj = j
        if bi < 0:
            break
        c1 = keys[bi]; c2 = keys[bj]
        m = tuple((c1[t] + c2[t]) // 2 for t in range(4))
        pts1 = d.pop(c1); pts2 = d.pop(c2)
        d[m] = d.get(m, []) + pts1 + pts2
        keys = list(d.keys())
        if it > 6000:
            break
    print("reduce iters", it, "final keys", len(keys))
    res = new_canvas(w, h, name=cv.name + "_q")
    for k, pts in d.items():
        for (x, y) in pts:
            res.set(x, y, k)
    return res

final = flatten([bg, ped, glowb, inst, sph, core, glowf, spark], name="final")
print("raw colors:", final.stats()["colors_used"])
final = reduce_to(final, limit)
print(final.stats_text())
finish(final)
