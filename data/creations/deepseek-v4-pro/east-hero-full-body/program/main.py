from pixelbench_api import *

W, H = 256, 256

# ----------------------------------------------------------------------------
# Canvases (layers)
# ----------------------------------------------------------------------------
bg   = new_canvas(W, H, name="bg")
mist = new_canvas(W, H, name="mist")
ch   = new_canvas(W, H, name="char")
fg   = new_canvas(W, H, name="fg")


def col(hexval, name):
    return bg.color(hexval, name)


# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------
SKY = ['#8fb6cf', '#9cc0d6', '#adccdd', '#c0d7e2', '#d0e0e6', '#dde8ea']
sky_idx = [col(s, 'sky%d' % i) for i, s in enumerate(SKY)]

far_mt   = col('#8fa7b4', 'far_mt')
mid_mt   = col('#5f7684', 'mid_mt')
ground   = col('#41505a', 'ground')
ground2  = col('#33434c', 'ground2')

mist1 = mist.color((255, 255, 255, 58), 'mist1')
mist2 = mist.color((255, 255, 255, 42), 'mist2')
mist3 = mist.color((255, 255, 255, 28), 'mist3')
fgmist = fg.color((255, 255, 255, 20), 'fgmist')

outline  = col('#1b1820', 'outline')
hair     = col('#16151a', 'hair')
hair_hi  = col('#2b2833', 'hair_hi')
skin     = col('#d8ae8c', 'skin')
skin_sh  = col('#b98f6e', 'skin_sh')
robe     = col('#2e3542', 'robe')
robe_sh  = col('#222832', 'robe_sh')
robe_hi  = col('#4a5466', 'robe_hi')
sash     = col('#9d3b32', 'sash')
sash_sh  = col('#772a24', 'sash_sh')
sash_hi  = col('#c2574a', 'sash_hi')
hat      = col('#c7a15a', 'hat')
hat_sh   = col('#a07c3e', 'hat_sh')
hat_dk   = col('#6f552a', 'hat_dk')
hat_hi   = col('#e0bc78', 'hat_hi')
blade    = col('#d9dfe6', 'blade')
blade_sh = col('#a8b3bf', 'blade_sh')
blade_hi = col('#f2f6fa', 'blade_hi')
gold     = col('#c9a23e', 'gold')
gold_sh  = col('#9a7728', 'gold_sh')
hilt     = col('#4a3626', 'hilt')


def inset(pts, f):
    n = len(pts)
    cx = sum(p[0] for p in pts) / n
    cy = sum(p[1] for p in pts) / n
    return [(round(cx + (x - cx) * f), round(cy + (y - cy) * f)) for x, y in pts]


# ----------------------------------------------------------------------------
# Background: sky bands, layered misty mountains, ground
# ----------------------------------------------------------------------------
for i, s in enumerate(sky_idx):
    y0 = i * 28
    y1 = min((i + 1) * 28, 170)
    bg.rect(0, y0, W, y1 - y0, s)

# pale moon and distant birds
bg.circle(58, 58, 14, col('#e8eef1', 'moon'), fill=True)
bg.line(192, 62, 198, 58, outline)
bg.line(198, 58, 204, 62, outline)
bg.line(208, 56, 214, 52, outline)
bg.line(214, 52, 220, 56, outline)

bg.poly([(0, 168), (24, 124), (46, 142), (70, 114), (96, 146), (122, 118),
         (148, 150), (172, 122), (198, 148), (224, 116), (244, 140), (255, 128),
         (255, 168)], far_mt, fill=True)
bg.poly([(0, 180), (20, 140), (52, 158), (84, 134), (116, 164), (150, 142),
         (186, 162), (214, 138), (240, 156), (255, 148), (255, 182)],
        mid_mt, fill=True)
bg.rect(0, 178, W, 20, ground)
bg.rect(0, 198, W, H - 198, ground2)

# horizon glow
bg.rect(0, 170, W, 8, col('#cddde2', 'haze'))

# ----------------------------------------------------------------------------
# Mist layers (separate canvas so flatten blends them)
# ----------------------------------------------------------------------------
mist.rect(0, 118, W, 12, mist3)
mist.rect(0, 146, W, 22, mist1)
mist.rect(0, 172, W, 24, mist2)
mist.rect(0, 196, W, 14, mist3)

# ----------------------------------------------------------------------------
# Character
# ----------------------------------------------------------------------------

# --- flowing hair behind head/body ------------------------------
hair_pts = [(96, 88), (152, 88), (166, 128), (182, 178), (188, 220),
            (176, 240), (158, 226), (150, 198), (138, 176), (110, 176),
            (98, 198), (86, 228), (68, 242), (58, 220), (68, 178), (82, 128)]
ch.poly(hair_pts, hair, fill=True)
ch.line(150, 120, 160, 190, hair_hi)
ch.line(98, 120, 86, 190, hair_hi)
ch.line(138, 120, 132, 180, hair_hi)
ch.line(110, 120, 116, 180, hair_hi)
ch.line(140, 200, 148, 232, hair_hi)
ch.line(104, 200, 94, 232, hair_hi)

# --- face (lower half visible under tilted hat) ------------------
ch.ellipse(124, 108, 18, 22, outline, fill=True)
ch.ellipse(124, 108, 15, 19, skin, fill=True)
ch.line(112, 112, 110, 120, skin_sh)      # nose shadow
ch.line(114, 124, 126, 124, outline)      # mouth
ch.line(116, 128, 122, 128, skin_sh)      # underlip shade
ch.line(136, 110, 138, 122, skin_sh)      # jaw shade (far side)

# --- main robe body ---------------------------------------------
robe_pts = [(116, 134), (90, 142), (80, 152), (74, 184), (66, 216), (56, 250),
            (192, 250), (182, 212), (172, 178), (164, 152), (152, 140), (130, 134)]
ch.poly(robe_pts, outline, fill=True)
ch.poly(inset(robe_pts, 0.94), robe, fill=True)

# --- sleeves ----------------------------------------------------
ls_pts = [(78, 152), (94, 150), (100, 168), (98, 206), (88, 228), (76, 220),
          (70, 190), (68, 164)]
ch.poly(ls_pts, outline, fill=True)
ch.poly(inset(ls_pts, 0.90), robe, fill=True)

rs_pts = [(144, 140), (162, 142), (176, 150), (180, 166), (172, 182),
          (160, 178), (148, 162), (142, 150)]
ch.poly(rs_pts, outline, fill=True)
ch.poly(inset(rs_pts, 0.90), robe, fill=True)

# --- collar / inner robe ----------------------------------------
ch.poly([(116, 134), (130, 134), (123, 152)], robe_sh, fill=True)
ch.line(116, 134, 123, 152, outline)
ch.line(130, 134, 123, 152, outline)
ch.line(119, 138, 123, 148, robe_hi)

# --- sash and knot ----------------------------------------------
sash_pts = [(78, 196), (168, 190), (166, 208), (80, 214)]
ch.poly(sash_pts, outline, fill=True)
ch.poly(inset(sash_pts, 0.90), sash, fill=True)
ch.line(88, 200, 160, 196, sash_hi)
ch.line(86, 206, 160, 202, sash_sh)

knot_pts = [(84, 206), (102, 202), (110, 226), (98, 234), (88, 228)]
ch.poly(knot_pts, outline, fill=True)
ch.poly(inset(knot_pts, 0.88), sash, fill=True)

tail_pts = [(94, 224), (112, 220), (106, 248), (98, 250), (90, 244)]
ch.poly(tail_pts, outline, fill=True)
ch.poly(inset(tail_pts, 0.90), sash_sh, fill=True)

# --- fabric folds / flowing details ------------------------------
for a, b in [((120, 214), (110, 250)), ((140, 214), (150, 250)),
             ((96, 206), (82, 250)), ((160, 206), (180, 250)),
             ((128, 214), (128, 246))]:
    ch.line(a[0], a[1], b[0], b[1], robe_sh)
for a, b in [((130, 210), (126, 244)), ((150, 208), (162, 244)),
             ((84, 200), (74, 240)), ((170, 204), (188, 242)),
             ((100, 208), (92, 246)), ((158, 208), (166, 246))]:
    ch.line(a[0], a[1], b[0], b[1], robe_hi)

# --- loose front hair strands over robe --------------------------
ch.line(112, 120, 104, 152, hair)
ch.line(136, 118, 142, 150, hair)

# --- sword (straight jian), tip on ground ------------------------
# blade
ch.rect(170, 172, 8, 76, outline)
ch.rect(172, 176, 4, 70, blade)
ch.poly([(170, 244), (178, 244), (174, 252)], outline, fill=True)
ch.poly([(172, 246), (176, 246), (174, 250)], blade, fill=True)
ch.line(173, 178, 173, 244, blade_hi)
ch.line(176, 178, 176, 242, blade_sh)

# guard
ch.rect(162, 168, 22, 7, outline)
ch.rect(164, 170, 18, 3, gold)
ch.line(164, 170, 181, 170, gold_sh)

# hilt
ch.rect(170, 150, 8, 20, outline)
ch.rect(172, 154, 4, 16, hilt)
ch.line(173, 156, 173, 168, gold)

# pommel
ch.ellipse(174, 148, 7, 5, outline, fill=True)
ch.ellipse(174, 148, 5, 3, gold, fill=True)

# --- hand resting on pommel -------------------------------------
ch.ellipse(174, 150, 9, 9, outline, fill=True)
ch.ellipse(174, 150, 6, 7, skin, fill=True)
ch.line(171, 147, 171, 155, skin_sh)
ch.line(175, 147, 175, 155, skin_sh)
ch.line(177, 149, 177, 155, skin_sh)

# --- hat (douli) tilted down ------------------------------------
# brim: wide ellipse, darker underside
ch.ellipse(124, 92, 60, 16, outline, fill=True)
ch.ellipse(124, 92, 56, 12, hat, fill=True)
ch.ellipse(124, 95, 50, 8, hat_sh, fill=True)
ch.line(72, 92, 176, 92, hat_dk)
# cone: asymmetric apex for a tilted look
cone_pts = [(74, 96), (174, 96), (130, 38)]
ch.poly(cone_pts, outline, fill=True)
ch.poly(inset(cone_pts, 0.92), hat, fill=True)
# woven bamboo lines on the cone
ch.line(99, 70, 154, 70, hat_dk)
ch.line(89, 80, 162, 80, hat_dk)
ch.line(82, 88, 168, 88, hat_dk)
ch.line(130, 40, 126, 90, hat_sh)
ch.line(123, 46, 121, 90, hat_hi)
# soft shadow cast by the brim over the visible upper face
ch.rect(108, 108, 34, 3, skin_sh)

# --- foreground mist (very subtle, in front of robe bottom) ------
fg.rect(0, 204, W, 14, fgmist)

# ----------------------------------------------------------------------------
# Composite and inspect
# ----------------------------------------------------------------------------
result = flatten([bg, mist, ch, fg], name="result")


def coarse(c, step=8):
    rows = []
    for y in range(0, H, step):
        line = ''
        for x in range(0, W, step):
            i = c.get(x, y)
            name = c.color_name(i)
            if name.startswith('sky'):
                chh = '.'
            elif name in ('far_mt', 'mid_mt', 'ground', 'ground2', 'haze'):
                chh = ':'
            elif name == 'hair':
                chh = 'H'
            elif name == 'hair_hi':
                chh = 'h'
            elif name == 'skin':
                chh = 'S'
            elif name == 'skin_sh':
                chh = 's'
            elif name == 'robe':
                chh = 'R'
            elif name in ('robe_sh', 'robe_hi'):
                chh = 'r'
            elif name in ('sash', 'sash_sh', 'sash_hi'):
                chh = 'A'
            elif name in ('hat', 'hat_sh', 'hat_dk', 'hat_hi'):
                chh = 'T'
            elif name in ('blade', 'blade_sh', 'blade_hi'):
                chh = '|'
            elif name in ('gold', 'gold_sh'):
                chh = 'G'
            elif name == 'hilt':
                chh = 'I'
            elif name == 'outline':
                chh = '#'
            elif name.startswith('#'):
                chh = '.'
            else:
                chh = '?'
            line += chh
        rows.append(line)
    return '\n'.join(rows)


print(result.stats_text())
print('--- COARSE OVERVIEW (8px steps) ---')
print(coarse(result))
print('--- FACE ---')
print(result.matrix_text(region=(104, 100, 150, 132), indices=False))
print('--- SWORD / HAND ---')
print(result.matrix_text(region=(150, 140, 192, 182), indices=False))

finish(result)
