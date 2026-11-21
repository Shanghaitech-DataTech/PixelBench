from pixelbench_api import *
import random

out = input_canvas.copy(name='output')

def col(spec, name=None):
    return out.color(spec, name)

# ---- palette registration ----
VINE_M = col((64, 100, 34), 'vine_mid')
VINE_H = col((102, 148, 56), 'vine_hi')
VINE_L = col((146, 194, 96), 'vine_lt')
STEM  = col((40, 52, 26), 'stem')
CLOAK = col((16, 18, 28), 'cloak')
CLOAK2 = col((44, 52, 74), 'cloak_rim')
CLOAK3 = col((8, 9, 15), 'cloak_dk')
RIM   = col((178, 128, 58), 'warm')
STAFF = col((98, 66, 38), 'staff')
ORB   = col((255, 246, 190), 'orb')
ORB2  = col((255, 216, 108), 'orb2')
ORB3  = col((228, 168, 62), 'orb3')
GLOW  = col((150, 108, 48), 'glow')

# ---- ivy ----
def leaf(cx, cy, rx=3, ry=2, vert=False):
    out.ellipse(cx, cy, rx, ry, VINE_M)
    out.ellipse(cx, cy, max(1, rx - 1), max(1, ry - 1), VINE_H)
    if vert:
        out.set(cx, cy + 1, VINE_L)
    else:
        out.set(cx + 1, cy, VINE_L)

def strand(pts, seed, jit=2, hang=5):
    rnd = random.Random(seed)
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        out.line(x0, y0, x1, y1, STEM)
        seg = max(abs(x1 - x0), abs(y1 - y0))
        t = 0
        while t <= seg:
            f = t / max(1, seg)
            lx = x0 + round((x1 - x0) * f) + rnd.randint(-jit, jit)
            ly = y0 + round((y1 - y0) * f) + rnd.randint(-jit, jit)
            if rnd.random() < 0.85:
                leaf(lx, ly, 3, 2, rnd.random() < 0.3)
            if rnd.random() < 0.42:
                hx = lx + rnd.randint(-1, 1)
                hy = ly + rnd.randint(1, hang)
                out.line(lx, ly, hx, hy, STEM)
                leaf(hx, hy, 2, 2, True)
            t += 3
    for _ in range(4):
        out.line(pts[-1][0], pts[-1][1],
                 pts[-1][0] + rnd.randint(-2, 2), pts[-1][1] + rnd.randint(2, 6), STEM)
        leaf(pts[-1][0] + rnd.randint(-2, 2), pts[-1][1] + rnd.randint(3, 7), 2, 2, True)

# vines on the tower walls
strand([(4, 38), (16, 50), (10, 64), (26, 76), (18, 92), (34, 106), (24, 122), (40, 136), (30, 152), (44, 166)], seed=1)
strand([(2, 118), (14, 136), (30, 148), (44, 164), (36, 180), (50, 194), (38, 208), (26, 220), (14, 228), (4, 233)], seed=2)
strand([(48, 60), (52, 72), (44, 84), (54, 96), (48, 108), (52, 120), (44, 132)], seed=3)
strand([(140, 58), (132, 74), (136, 90), (126, 104), (132, 118), (140, 130), (134, 146), (138, 160)], seed=4)
strand([(140, 168), (132, 182), (138, 196), (128, 210), (134, 224), (142, 232)], seed=5)
strand([(60, 136), (68, 144), (78, 140), (88, 148), (98, 144), (108, 152)], seed=6)
# a few fallen leaves at the base in front of the arch
g = random.Random(9)
for _ in range(14):
    leaf(78 + g.randint(0, 44), 236 + g.randint(0, 10), 2, 2, g.random() < 0.5)

# ---- glow pool at the doorway floor ----
for dy in range(0, 12):
    for dx in range(0, 30):
        if (dx - 13) ** 2 + (dy * 1.4 - 6) ** 2 < 40:
            out.set(96 + dx, 224 + dy, GLOW)
# ---- mage (back view) at the archway ----
# staff
out.line(111, 169, 111, 232, STAFF)
# orb with glow
out.circle(110, 166, 1, ORB)
for px in ((110, 163), (107, 165), (113, 165), (110, 169)):
    out.set(*px, ORB)
for px in ((109, 162), (106, 164), (114, 164), (107, 168), (113, 168), (107, 170), (113, 170)):
    out.set(*px, ORB2)
out.circle(110, 166, 4, ORB3, fill=False)
out.circle(110, 166, 6, GLOW, fill=False)
for px in ((104, 160), (105, 156), (116, 158), (117, 162), (103, 168), (104, 173), (115, 173), (105, 176), (113, 177)):
    out.set(*px, ORB3)
# body rows: hooded back, shoulders, cloak, striding legs
body = {
    190: (98, 104, CLOAK3),
    191: (96, 106, CLOAK),
    192: (95, 107, CLOAK),
    193: (94, 108, CLOAK),
    194: (95, 107, CLOAK),
    195: (95, 107, CLOAK),
    196: (96, 107, CLOAK),
    197: (94, 109, CLOAK),
    198: (92, 110, CLOAK),
    199: (91, 111, CLOAK),
    200: (90, 112, CLOAK),
    201: (90, 112, CLOAK),
    202: (90, 112, CLOAK),
    203: (90, 112, CLOAK),
    204: (90, 112, CLOAK),
    205: (90, 112, CLOAK),
    206: (90, 112, CLOAK),
    207: (90, 113, CLOAK),
    208: (90, 113, CLOAK),
    209: (90, 113, CLOAK),
    210: (90, 113, CLOAK),
    211: (90, 113, CLOAK),
    212: (91, 113, CLOAK),
    213: (91, 113, CLOAK),
    214: (91, 114, CLOAK),
    215: (91, 114, CLOAK),
    216: (92, 114, CLOAK),
    217: (92, 114, CLOAK),
    218: (93, 114, CLOAK),
    219: (92, 115, CLOAK),
    220: (92, 115, CLOAK),
    221: (93, 114, CLOAK),
    222: (94, 113, CLOAK),
    223: (95, 112, CLOAK),
    224: (96, 111, CLOAK),
}
for y, (x0, x1, cc) in body.items():
    out.rect(x0, y, x1 - x0 + 1, 1, cc)
# hood fold shading + cool rim on left, warm rim on right
for y in range(192, 220):
    x0 = body[y][0]
    x1 = body[y][1]
    out.set(x0, y, CLOAK2)
    out.set(x1, y, RIM if y < 216 else CLOAK)
    if y in (193, 200, 207, 214, 218):
        out.line(x0 + 2, y, x0 + 3, y, CLOAK3)
        out.line(x1 - 3, y - 0, x1 - 2, y, CLOAK3)
for yy in (192, 193, 198, 204, 210, 216):
    out.set(100 + (yy % 3), yy, CLOAK3)
    out.set(105 + (yy % 2), yy, CLOAK3)
# legs (striding)
for y, rng in ((225, (93, 97)), (226, (92, 96)), (227, (92, 96)),
              (228, (92, 96)), (229, (93, 97)), (230, (93, 98)),
              (231, (93, 97))):
    for x in range(rng[0], rng[1] + 1):
        out.set(x, y, CLOAK3)
for y, rng in ((226, (103, 107)), (227, (104, 108)), (228, (105, 109)),
              (229, (105, 109)), (230, (106, 110)), (231, (105, 109)),
              (232, (104, 108))):
    for x in range(rng[0], rng[1] + 1):
        out.set(x, y, CLOAK)
# gripping hand on staff
out.set(111, 201, CLOAK)
out.set(110, 202, CLOAK)
# warm light on the doorway stone near the orb
for px in ((116, 163), (117, 166), (115, 171), (116, 174), (118, 168), (113, 176)):
    out.set(*px, ORB3)
for px in ((118, 160), (119, 164), (118, 171), (115, 158), (114, 177), (117, 176)):
    out.set(*px, GLOW)

print(out.stats_text())
finish(out)
