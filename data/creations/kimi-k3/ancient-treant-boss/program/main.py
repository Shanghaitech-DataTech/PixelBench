import math, random
random.seed(11)

W = H = 256
bg   = new_canvas(W, H, name='bg')
rays = new_canvas(W, H, name='rays')
tr   = new_canvas(W, H, name='treant')
gl   = new_canvas(W, H, name='glow')
fg   = new_canvas(W, H, name='fg')

# ---------------- palette ----------------
sky1 = bg.color('#081009'); sky2 = bg.color('#0b1a10')
sky3 = bg.color('#102417'); sky4 = bg.color('#16301f')
g1 = bg.color('#1b2a15'); g2 = bg.color('#141d0e'); g3 = bg.color('#0e1208')
sp1 = bg.color('#0f180a'); sp2 = bg.color('#090d05')
treec = bg.color('#0a120c'); canopy2 = bg.color('#0e2013')
shad = bg.color('#0b0f07')

# ---------------- sky bands ----------------
bg.rect(0, 0, 256, 56, sky1)
bg.rect(0, 56, 256, 56, sky2)
bg.rect(0, 112, 256, 60, sky3)
bg.rect(0, 172, 256, 46, sky4)
bg.dither(0, 52, 256, 8, [sky1, sky2])
bg.dither(0, 108, 256, 8, [sky2, sky3])
bg.dither(0, 168, 256, 8, [sky3, sky4])

# ---------------- distant forest ----------------
for (x, w, top) in [(14, 12, 60), (42, 7, 92), (224, 10, 68), (244, 12, 36), (198, 6, 118), (70, 5, 130)]:
    bg.rect(x, top, w, 218 - top, treec)
for (cx, cy, r) in [(18, 38, 26), (50, 64, 16), (236, 26, 30), (206, 82, 14), (250, 62, 20), (4, 88, 18), (72, 104, 12)]:
    bg.circle(cx, cy, r, canopy2)

# ---------------- ground ----------------
bg.rect(0, 218, 256, 15, g1)
bg.rect(0, 233, 256, 12, g2)
bg.rect(0, 245, 256, 11, g3)
bg.dither(0, 216, 256, 4, [sky4, g1])
bg.dither(0, 231, 256, 4, [g1, g2])
bg.dither(0, 243, 256, 4, [g2, g3])
tops = []
x = 0
while x <= 256:
    tops.append((min(x, 255), 214 + random.randrange(6)))
    x += 6
bg.poly(tops + [(255, 222), (0, 222)], g2)
for i in range(150):
    x = random.randrange(256); y = random.randrange(220, 256)
    bg.set(x, y, sp1 if random.random() < 0.55 else sp2)
bg.ellipse(128, 233, 76, 11, shad)

# ---------------- god rays (alpha layer) ----------------
rays.poly([(140, 0), (162, 0), (108, 256), (84, 256)], rays.color('#dcffb016'))
rays.poly([(178, 0), (196, 0), (158, 256), (138, 256)], rays.color('#dcffb024'))
rays.poly([(216, 0), (238, 0), (226, 256), (206, 256)], rays.color('#dcffb010'))
rays.circle(128, 96, 78, rays.color('#dcffb00a'))
rays.circle(128, 96, 56, rays.color('#dcffb010'))
rays.circle(128, 96, 36, rays.color('#dcffb018'))
rays.circle(212, 12, 26, rays.color('#dcffb010'))
rays.ellipse(128, 240, 64, 12, rays.color('#dcffb016'))

# ---------------- treant silhouette ----------------
key = tr.color('#140e08', name='outline')
mid = tr.color('#453017')
dark = tr.color('#2a1c0f')
light = tr.color('#5f4526')
hi = tr.color('#7d5d33')
crk = tr.color('#1c1209')
sock = tr.color('#0c0703')
rim = tr.color('#a07f4a')
transp = tr.color((0, 0, 0, 0))

TRUNK = [
    (104, 42), (99, 48), (96, 56), (94, 66), (92, 76), (88, 84),
    (82, 90), (78, 96), (77, 102), (82, 108), (88, 114), (92, 122),
    (94, 132), (93, 144), (95, 156), (96, 168), (95, 180), (92, 190),
    (88, 198), (82, 206), (74, 214), (66, 222), (58, 230), (50, 238), (46, 244),
    (56, 246), (64, 240), (70, 246), (76, 238), (84, 246), (90, 236), (96, 246),
    (102, 238), (108, 248), (114, 238), (120, 248), (126, 238), (132, 248),
    (138, 238), (144, 248), (150, 238), (156, 246), (162, 236), (168, 244),
    (176, 234), (184, 242), (192, 234), (200, 240), (206, 232), (202, 224),
    (196, 216), (190, 208), (184, 200), (180, 192), (176, 184), (174, 174),
    (172, 162), (171, 150), (172, 138), (174, 128), (177, 118), (181, 110),
    (185, 102), (186, 96), (180, 90), (172, 84), (168, 76), (164, 66),
    (161, 56), (156, 48), (148, 42), (138, 38), (126, 36), (116, 38),
]
tr.poly(TRUNK, key)

ARM_L = [(84, 100), (74, 110), (60, 124), (46, 138), (36, 148), (32, 156),
         (40, 161), (50, 151), (62, 139), (76, 125), (88, 114), (94, 106)]
tr.poly(ARM_L, key)
ARM_R = [(180, 100), (190, 90), (200, 74), (210, 54), (215, 40), (223, 36),
         (225, 47), (217, 63), (206, 83), (194, 99), (184, 108)]
tr.poly(ARM_R, key)

CLAWS = [
    # left hand (low, spread)
    [(40, 150), (20, 144), (36, 158)],
    [(36, 156), (14, 158), (36, 164)],
    [(38, 162), (20, 174), (44, 166)],
    [(44, 164), (36, 180), (50, 168)],
    # right hand (raised)
    [(216, 38), (204, 10), (224, 34)],
    [(222, 36), (226, 6), (230, 36)],
    [(226, 40), (246, 16), (234, 44)],
    [(230, 46), (250, 38), (236, 52)],
    [(232, 52), (246, 60), (230, 58)],
    # crown antlers
    [(106, 42), (98, 10), (112, 36)],
    [(100, 24), (84, 14), (104, 30)],
    [(126, 38), (122, 6), (134, 34)],
    [(124, 18), (112, 8), (128, 22)],
    [(148, 42), (158, 12), (154, 40)],
    [(154, 26), (170, 16), (156, 32)],
    # shoulder / elbow spikes
    [(80, 96), (62, 74), (88, 90)],
    [(78, 102), (58, 94), (84, 96)],
    [(184, 94), (204, 68), (190, 96)],
    [(186, 102), (208, 90), (190, 102)],
    [(200, 74), (212, 66), (202, 82)],
    # small crown stubs
    [(114, 38), (117, 26), (121, 37)],
    [(136, 37), (141, 26), (144, 38)],
    # trunk nubs
    [(94, 128), (80, 122), (96, 138)],
    [(172, 148), (186, 142), (174, 158)],
    [(93, 168), (80, 164), (94, 178)],
    # ground-gripping roots
    [(52, 242), (30, 254), (62, 250)],
    [(204, 236), (230, 250), (198, 244)],
]
for c in CLAWS:
    tr.poly(c, key)

# ---------------- erosion -> 2px dark outline ----------------
def grid_of(c):
    return [[c.get(x, y) for x in range(256)] for y in range(256)]

def isv(g, x, y, v):
    return 0 <= x < 256 and 0 <= y < 256 and g[y][x] == v

g = grid_of(tr)
for y in range(256):
    for x in range(256):
        if g[y][x] == key:
            if all(isv(g, x + dx, y + dy, key) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                tr.set(x, y, mid)
g = grid_of(tr)
for y in range(256):
    for x in range(256):
        if g[y][x] == mid:
            if any(isv(g, x + dx, y + dy, key) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                tr.set(x, y, key)

def interior(x, y):
    v = tr.get(x, y)
    return v != key and v != transp

# ---------------- form shading (light from top-right) ----------------
for y in range(256):
    run = None
    spans = []
    for x in range(256):
        if interior(x, y):
            if run is None:
                run = [x, x]
            else:
                run[1] = x
        else:
            if run:
                spans.append(tuple(run)); run = None
    if run:
        spans.append(tuple(run))
    for x0, x1 in spans:
        w = x1 - x0 + 1
        if w >= 16:
            for i in range(7):
                if x0 + i <= x1:
                    tr.set(x0 + i, y, dark)
            for i in range(7, 12):
                if x0 + i <= x1 and (i + y) % 2 == 0:
                    tr.set(x0 + i, y, dark)
            for i in range(5):
                tr.set(x1 - i, y, light)
            for i in range(2):
                tr.set(x1 - 5 - i, y, hi)
        elif w >= 9:
            tr.set(x0, y, dark); tr.set(x0 + 1, y, dark)
            tr.set(x1, y, light); tr.set(x1 - 1, y, light)

# cast shadows
tr.poly([(82, 116), (96, 110), (98, 132), (86, 134)], dark)
tr.poly([(162, 110), (178, 102), (172, 128), (160, 124)], dark)

# twig / claw cores (thin shapes were eaten by the outline pass)
CLAW_CORE = [
    ((38, 150), (24, 146)), ((34, 156), (18, 158)), ((36, 160), (24, 172)), ((42, 163), (38, 177)),
    ((217, 38), (207, 14)), ((222, 36), (224, 10)), ((226, 40), (244, 20)), ((230, 46), (248, 38)), ((232, 52), (244, 60)),
    ((106, 42), (100, 14)), ((126, 38), (123, 10)), ((148, 42), (156, 16)),
    ((80, 96), (66, 78)), ((78, 102), (62, 94)), ((182, 94), (198, 72)), ((184, 102), (202, 92)),
    ((92, 128), (82, 123)), ((172, 148), (183, 143)), ((92, 168), (82, 165)),
    ((52, 245), (33, 252)), ((203, 239), (227, 248)),
]
for (a, b) in CLAW_CORE:
    tr.line(a[0], a[1], b[0], b[1], mid)

# ---------------- bark cracks & knots ----------------
def crack(x, y0, y1, wave=3.0, amp=1):
    for y in range(y0, y1):
        xx = x + round(math.sin(y / wave) * amp)
        if interior(xx, y):
            tr.set(xx, y, crk)
        if interior(xx + 1, y) and random.random() < 0.5:
            tr.set(xx + 1, y, crk)

for (cx, a, b) in [(116, 108, 150), (140, 104, 136), (108, 160, 196), (150, 150, 190),
                   (128, 170, 205), (98, 120, 142), (160, 120, 150), (120, 210, 232),
                   (148, 208, 230), (104, 190, 212), (156, 186, 206), (60, 130, 148),
                   (196, 84, 100), (210, 56, 70)]:
    crack(cx, a, b, wave=random.uniform(2.5, 4.5), amp=random.choice((1, 1, 2)))

# bark grain: short vertical dashes with a lit right edge
for (bx, a, b) in [(104, 116, 196), (118, 120, 220), (134, 112, 224), (146, 116, 210),
                   (158, 120, 186), (98, 140, 176), (112, 204, 232), (152, 200, 230), (166, 140, 170)]:
    yy = a
    while yy < b:
        ln = random.randrange(3, 8)
        for y2 in range(yy, min(yy + ln, b)):
            if interior(bx, y2) and tr.get(bx, y2) == mid:
                tr.set(bx, y2, crk)
            if interior(bx + 1, y2) and tr.get(bx + 1, y2) == mid:
                tr.set(bx + 1, y2, light)
        yy += ln + random.randrange(2, 6)

tr.ellipse(142, 168, 4, 6, crk)
tr.ellipse(142, 168, 2, 3, sock)
tr.set(139, 163, light); tr.set(140, 162, light)
tr.ellipse(112, 148, 3, 4, crk)
tr.set(110, 145, light)

# root separation lines
for (x0, y0, x1, y1) in [(104, 224, 100, 240), (128, 226, 128, 244), (152, 224, 156, 240),
                          (82, 216, 72, 232), (174, 216, 184, 230)]:
    tr.line(x0, y0, x1, y1, key)

# ---------------- face (angry brow dipping toward centre) ----------------
tr.poly([(102, 64), (128, 71), (154, 64), (152, 72), (128, 77), (104, 72)], crk)
tr.poly([(106, 77), (122, 81), (121, 87), (109, 84)], sock)
tr.poly([(150, 77), (134, 81), (135, 87), (147, 84)], sock)
tr.poly([(118, 95), (124, 92), (128, 95), (132, 92), (138, 95), (135, 105), (128, 111), (121, 105)], sock)

# glowing heart-crack
tr.line(128, 122, 124, 132, key); tr.line(124, 132, 131, 141, key); tr.line(131, 141, 126, 152, key)
tr.line(129, 122, 125, 132, key); tr.line(125, 132, 132, 141, key); tr.line(132, 141, 127, 152, key)

# ---------------- rim light (top-right edges) ----------------
def istransp(xx, yy):
    if 0 <= xx < 256 and 0 <= yy < 256:
        return tr.get(xx, yy) == transp
    return True

to_rim = []
for y in range(256):
    for x in range(256):
        if tr.get(x, y) != key:
            continue
        up_right = istransp(x + 1, y) or istransp(x, y - 1) or istransp(x + 1, y - 1)
        body = any((not istransp(xx, yy)) and tr.get(xx, yy) != key
                   for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                                  (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)))
        if up_right and body:
            to_rim.append((x, y))
for x, y in to_rim:
    tr.set(x, y, rim)

# ---------------- moss ----------------
mo_d = tr.color('#2c4a18'); mo = tr.color('#4c7a26')
mo_l = tr.color('#71a83c'); mo_hi = tr.color('#96cc55')

def moss(cx, cy, r):
    for yy in range(cy - r, cy + r + 1):
        for xx in range(cx - r - 1, cx + r + 2):
            if (xx - cx) ** 2 + (yy - cy) ** 2 <= r * r + random.randrange(3):
                if 0 <= xx < 256 and 0 <= yy < 256 and tr.get(xx, yy) != transp:
                    tr.set(xx, yy, mo)
    for i in range(r * 3):
        xx = cx + random.randrange(-r, r + 1); yy = cy + random.randrange(-r, r + 1)
        if 0 <= xx < 256 and 0 <= yy < 256:
            v = tr.get(xx, yy)
            if v != transp and v != key:
                tr.set(xx, yy, mo_l if random.random() < 0.5 else mo_d)
    for i in range(max(2, r)):
        xx = cx + random.randrange(-r, r + 1); yy = cy + random.randrange(-r, r + 1)
        if 0 <= xx < 256 and 0 <= yy < 256 and tr.get(xx, yy) in (mo, mo_l):
            tr.set(xx, yy, mo_hi)

for (cx, cy, r) in [(103, 42, 5), (152, 44, 4), (80, 93, 6), (183, 93, 6),
                    (57, 127, 4), (207, 57, 4), (171, 191, 5), (74, 218, 5),
                    (186, 222, 5), (112, 34, 2), (146, 40, 3), (96, 176, 4), (162, 160, 4)]:
    moss(cx, cy, r)

# ---------------- hanging vines ----------------
vine = tr.color('#3a6420'); leaf = tr.color('#5d8f30')
def vinef(x, y, l, drift=1):
    cxx = x
    for i in range(l):
        yy = y + i
        cxx = x + round(math.sin(i / 3.0) * drift)
        if 0 <= cxx < 256 and 0 <= yy < 256:
            tr.set(cxx, yy, vine)
        if i % 5 == 2:
            if 0 <= cxx - 1 < 256:
                tr.set(cxx - 1, yy, leaf)
            if 0 <= cxx + 1 < 256:
                tr.set(cxx + 1, yy, leaf)
    if 0 <= cxx < 256 and y + l < 256:
        tr.set(cxx, y + l, leaf)

vinef(48, 148, 26); vinef(62, 134, 34); vinef(200, 86, 20); vinef(74, 112, 38)
vinef(92, 86, 20); vinef(170, 118, 26); vinef(58, 146, 18); vinef(188, 98, 24)

# ---------------- glow layer (eyes / mouth / heart) ----------------
e_mid = gl.color('#8cff5a'); e_hot = gl.color('#ecffd0'); core = gl.color('#9dff5e')
gl.poly([(110, 79), (120, 81), (119, 84), (111, 83)], e_mid)
gl.poly([(146, 79), (136, 81), (137, 84), (145, 83)], e_mid)
gl.set(114, 81, e_hot); gl.set(115, 81, e_hot)
gl.set(142, 81, e_hot); gl.set(141, 81, e_hot)
gl.circle(115, 81, 6, gl.color('#6cff4a2e'))
gl.circle(115, 81, 4, gl.color('#6cff4a4d'))
gl.circle(141, 81, 6, gl.color('#6cff4a2e'))
gl.circle(141, 81, 4, gl.color('#6cff4a4d'))
gl.ellipse(128, 88, 16, 3, gl.color('#6cff4a14'))
gl.set(125, 98, e_mid); gl.set(127, 99, e_mid); gl.set(129, 99, e_mid)
gl.set(131, 98, e_mid); gl.set(128, 102, e_mid)
gl.circle(128, 101, 5, gl.color('#59e83c22'))
gl.line(128, 124, 125, 132, core); gl.line(125, 132, 130, 140, core); gl.line(130, 140, 126, 150, core)
gl.circle(128, 138, 9, gl.color('#59e83c22'))
gl.circle(128, 138, 5, gl.color('#6cff4a33'))

# ---------------- foreground ----------------
fg.rect(0, 224, 256, 14, fg.color('#cfe8c010'))
gr1 = fg.color('#2e5620'); gr2 = fg.color('#22431a')

def tuft(x, y, h, col):
    for i in range(h):
        fg.set(x, y - i, col)
    fg.set(x - 1, y - 1, col); fg.set(x + 1, y - 2, col)

for x in range(6, 252, 9):
    if random.random() < 0.55:
        tuft(x + random.randrange(4), random.randrange(228, 252), random.randrange(3, 7),
             gr1 if random.random() < 0.5 else gr2)
for x in list(range(8, 40, 10)) + list(range(216, 250, 10)):
    if random.random() < 0.7:
        tuft(x + random.randrange(3), random.randrange(215, 221), random.randrange(3, 5),
             gr1 if random.random() < 0.5 else gr2)

# foreground roots breaking the surface
fg.poly([(70, 252), (84, 240), (94, 252)], key)
fg.poly([(76, 251), (84, 244), (90, 251)], mid)
fg.poly([(170, 252), (184, 242), (196, 252)], key)
fg.poly([(176, 251), (184, 246), (190, 251)], mid)

# corner hanging vines (framing)
cv = fg.color('#0d1a0c'); cvl = fg.color('#22431a')
def cvine(x, l, drift=2):
    for i in range(l):
        xx = x + round(math.sin(i / 4.0) * drift)
        fg.set(xx, i, cv)
        if i % 6 == 3:
            fg.set(xx + 1, i, cvl)
            fg.set(xx - 1, i, cv)
for x, l in [(8, 46), (22, 30), (36, 52), (232, 40), (246, 56), (218, 26)]:
    cvine(x, l)

# fireflies / spores
ff = fg.color('#e4ff9e')
for i in range(14):
    x = random.randrange(16, 240); y = random.randrange(36, 205)
    if 100 < x < 160 and 60 < y < 115:
        continue
    fg.set(x, y, ff)
    if random.random() < 0.4:
        fg.set(x + 1, y, fg.color('#9cc95e'))

# glowing mushrooms at the roots
st = fg.color('#c9b98a')
fg.rect(64, 238, 2, 4, st); fg.rect(62, 236, 6, 2, core); fg.set(63, 236, e_hot)
fg.rect(192, 242, 2, 3, st); fg.rect(190, 240, 5, 2, core)

# ---------------- compose ----------------
flat = flatten([bg, rays, tr, gl, fg], name='ancient-treant-boss')
print(flat.stats_text())
view(flat)
finish(flat)
