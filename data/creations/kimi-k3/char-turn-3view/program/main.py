from pixelbench_api import *

COL = dict(a='#050100', b='#160701', c='#290e02', d='#421603', e='#5f1f04', f='#792806',
           g='#fdd5b7', h='#eaa377', i='#281820', j='#9e3e37', k='#50d4ec', l='#f2f8f9',
           m='#5187b3', n='#293d4b', o='#d28560', p='#545665', q='#a8b2c1', r='#ffffff',
           s='#e0f4f9', t='#767b90', u='#fbece6', v='#0b2139', w='#492544')

def put(cv, x, y, ch):
    if ch != '.':
        cv.set(x, y, COL[ch])

def seg(*pairs):
    s = ''.join(ch * n for ch, n in pairs)
    assert len(s) <= 66, ('seg too long', len(s))
    return s.ljust(66, '.')

def draw_rows(cv, y0, lines):
    for dy, line in enumerate(lines):
        assert len(line) == 66, ('row', y0 + dy, len(line))
        for dx, ch in enumerate(line):
            put(cv, dx, y0 + dy, ch)

TEX = "ccdccdcdcccdccdc"
def hair_row(cv, y, x0, x1, off=0, edges=True):
    if edges:
        cv.set(x0, y, COL['a']); cv.set(x1, y, COL['a'])
    for x in range(x0 + (1 if edges else 0), x1):
        cv.set(x, y, COL[TEX[(x + off) % 16]])

NEAR = ['kkiiiiikk', 'lliiimmll', 'ggnnnnnll']
FAR  = ['kkiikk', 'llimll', 'ggnnll']
def eye(cv, x, y, stamp):
    rows = [stamp[0], stamp[0], stamp[1], stamp[1], stamp[1], stamp[2], stamp[2]]
    for dy, r in enumerate(rows):
        for dx, ch in enumerate(r):
            put(cv, x + dx, y + dy, ch)

inp = input_canvas

# ================= FRAME 1: 3/4 view, turned to HER left (faces viewer's right) =================
f1 = inp.copy(name='f1')
f1.clear(0, 24, 66, 39)  # clear rows 24-62, keep hair top rows 0-23 and body rows 63+

# face skin (shifted right; nose side toward viewer's right)
f1.poly([(30,24),(50,24),(53,27),(53,42),(51,47),(47,50),(40,51),(34,48),(31,42),(30,34)], COL['g'])

# back-of-head mass + temple (hair texture rows)
mass = {24:(24,31),25:(24,31),26:(24,31),27:(24,31),28:(24,31),29:(24,31),30:(24,31),31:(24,31),
        32:(10,30),33:(10,30),34:(10,30),35:(10,30),36:(10,30),37:(10,30),38:(10,30),39:(10,30),
        40:(12,29),41:(12,29),42:(12,29),43:(12,28),44:(14,26),45:(15,24),46:(16,22)}
for yy, (x0, x1) in mass.items():
    hair_row(f1, yy, x0, x1, off=yy)
# restore the input's detailed left hair over the top of the mass
inp.select(0, 24, 24, 8).copy_to(0, 24, f1, mode='over')
# mass shading / highlights
f1.rect(13, 40, 14, 2, COL['d']); f1.rect(15, 42, 9, 2, COL['b'])
f1.rect(24, 25, 4, 2, COL['e']); f1.rect(25, 25, 2, 1, COL['f'])
f1.rect(12, 33, 3, 6, COL['d'])

# face shading + outline
f1.line(31, 28, 31, 40, COL['h'])
f1.line(36, 49, 46, 49, COL['h'])
f1.line(54, 30, 54, 43, COL['i'])
f1.set(55, 44, COL['i']); f1.set(55, 45, COL['i']); f1.set(54, 46, COL['i'])  # nose tip
f1.set(53, 47, COL['i']); f1.set(52, 48, COL['i']); f1.set(51, 49, COL['i'])  # jaw curve
f1.set(48, 50, COL['i']); f1.set(49, 50, COL['i']); f1.set(50, 50, COL['i'])  # chin bottom
f1.set(51, 45, COL['h']); f1.set(52, 45, COL['h']); f1.set(52, 46, COL['h'])  # nose shading
f1.rect(35, 46, 3, 2, COL['o'])  # near cheek blush

# brows, eyelids, eyes (near eye bigger, far eye compressed)
f1.rect(34, 34, 5, 2, COL['c']); f1.rect(46, 34, 4, 2, COL['c'])
f1.rect(33, 36, 9, 2, COL['h']); f1.rect(46, 36, 6, 2, COL['h'])
eye(f1, 33, 38, NEAR)
eye(f1, 46, 38, FAR)

# mouth
f1.set(42, 47, COL['j']); f1.set(43, 47, COL['j'])
f1.set(41, 47, COL['h']); f1.set(44, 47, COL['h'])

# right sideburn lock beside the cheek (far-side hair)
f1.rect(55, 24, 3, 17, COL['c'])
f1.line(58, 24, 58, 40, COL['a'])
f1.line(57, 26, 57, 39, COL['d'])
f1.set(56, 26, COL['e']); f1.set(56, 27, COL['e'])
f1.set(56, 41, COL['c']); f1.set(57, 41, COL['a']); f1.set(56, 42, COL['a'])

# front hair band copied from the input (asymmetric original), wisps trimmed to the cheeks
inp.select(30, 24, 23, 8).copy_to(30, 24, f1, mode='over')
f1.set(45, 25, COL['a']); f1.set(46, 25, COL['d']); f1.set(47, 25, COL['d']); f1.set(48, 25, COL['a'])
f1.rect(45, 26, 4, 2, COL['c'])
f1.set(46, 28, COL['d']); f1.set(47, 28, COL['d']); f1.set(48, 28, COL['d'])
f1.set(31, 26, COL['d']); f1.set(32, 26, COL['d']); f1.set(31, 27, COL['d'])

# collar left (copied from input), then mirrored to the right
inp.select(12, 50, 9, 2).copy_to(12, 50, f1, mode='over')
inp.select(9, 52, 17, 2).copy_to(9, 52, f1, mode='over')
inp.select(7, 54, 19, 4).copy_to(7, 54, f1, mode='over')
f1.select(7, 52, 19, 6).flip('h').copy_to(40, 52, f1)
f1.select(12, 50, 9, 2).flip('h').copy_to(45, 50, f1)
# jaw underside skin left of chin shadow
f1.rect(26, 52, 10, 2, COL['o'])
# chin shadow (shifted right with the turned jaw)
f1.rect(36, 52, 14, 2, COL['j'])

# bodice left from input, mirrored to right
inp.select(5, 58, 23, 5).copy_to(5, 58, f1, mode='replace')
f1.select(5, 58, 23, 5).flip('h').copy_to(38, 58, f1)
# bodice centre
f1.rect(28, 58, 10, 5, COL['s'])
f1.line(30, 58, 30, 62, COL['t']); f1.line(34, 58, 34, 62, COL['t'])
# neck + chest
f1.rect(38, 54, 8, 7, COL['o'])
f1.line(38, 54, 38, 60, COL['h']); f1.line(45, 54, 45, 60, COL['h'])
f1.rect(38, 61, 8, 2, COL['s']); f1.rect(40, 61, 4, 2, COL['g'])

# rebuild right side rows 63-74 (was front ponytail) by mirroring the left side
f1.select(0, 63, 27, 12).flip('h').copy_to(39, 63, f1)

# ================= FRAME 2: 3/4 view, turned to HER right (faces viewer's left) =================
f2 = inp.copy(name='f2')
# mirrored head/shoulders of f1 (before the peek tuft is added)
f1.select(0, 0, 66, 63).flip('h').copy_to(0, 0, f2)
# her side ponytail is on the NEAR side now: rebuild it big on viewer's right
inp.select(44, 24, 22, 8).copy_to(44, 24, f2, mode='over')   # ponytail top rows 24-31
f2.rect(46, 32, 13, 12, COL['c'])                             # ponytail mid rows 32-43
f2.rect(46, 32, 3, 12, COL['d']); f2.rect(56, 32, 3, 12, COL['d'])
f2.rect(50, 33, 4, 3, COL['e']); f2.rect(51, 34, 2, 2, COL['f'])
f2.line(58, 32, 58, 43, COL['a'])
inp.select(49, 44, 17, 19).copy_to(49, 44, f2, mode='over')   # ponytail front rows 44-62
# rows 63-118 keep the input pixels (ponytail bottom, hands, skirt)

# small peek of the ponytail behind the far shoulder for frame 1 (after f2 copy!)
f1.poly([(59, 44), (63, 46), (64, 52), (62, 60), (59, 62), (58, 56), (58, 48)], COL['c'])
f1.poly([(59, 44), (63, 46), (64, 52), (62, 60), (59, 62), (58, 56), (58, 48)], COL['a'], fill=False)
f1.line(60, 50, 60, 58, COL['d']); f1.line(61, 47, 61, 53, COL['e'])
f1.set(60, 60, COL['b']); f1.set(61, 61, COL['b'])

# ================= FRAME 3: rear view =================
f3 = inp.copy(name='f3')
f3.clear(0, 24, 66, 39)  # rows 24-62
# remove the front ponytail connector hair (upper right rows 17-23), mirror the left side there
f3.select(6, 17, 20, 7).flip('h').copy_to(40, 17, f3)

# back-of-head hair mass
for yy in range(24, 32):
    hair_row(f3, yy, 5, 60, off=yy)
for yy in range(32, 40):
    hair_row(f3, yy, 6, 59, off=yy)
for yy in range(40, 46):
    hair_row(f3, yy, 8, 57, off=yy)
# highlights and shading on the mass
f3.rect(14, 26, 7, 3, COL['e']); f3.rect(16, 27, 3, 2, COL['f'])
f3.rect(40, 25, 6, 3, COL['e']); f3.rect(42, 26, 2, 2, COL['f'])
f3.rect(9, 39, 48, 2, COL['d']); f3.rect(11, 42, 44, 2, COL['d'])

# back collar / bodice (symmetric, same dress language)
R50 = seg(('.', 12), ('p', 9), ('.', 24), ('p', 9), ('.', 12))
R52 = seg(('.', 9), ('p', 3), ('q', 17), ('p', 2), ('q', 4), ('p', 2), ('q', 17), ('p', 3), ('.', 9))
R54 = seg(('.', 7), ('p', 2), ('q', 3), ('r', 4), ('s', 3), ('q', 2), ('s', 3), ('p', 2), ('q', 14),
          ('p', 2), ('s', 3), ('q', 2), ('s', 3), ('r', 4), ('q', 3), ('p', 2), ('.', 7))
R56 = seg(('.', 5), ('p', 2), ('t', 2), ('r', 3), ('s', 2), ('r', 2), ('s', 3), ('q', 3), ('s', 3),
          ('q', 2), ('t', 15), ('q', 2), ('s', 3), ('q', 3), ('s', 3), ('r', 2), ('s', 2), ('t', 2),
          ('p', 2), ('.', 5))
R58 = seg(('.', 5), ('p', 2), ('q', 2), ('s', 3), ('q', 2), ('s', 5), ('q', 2), ('s', 5), ('q', 2),
          ('t', 10), ('q', 2), ('s', 5), ('q', 2), ('s', 5), ('q', 2), ('s', 3), ('q', 2), ('p', 2), ('.', 5))
R61 = seg(('.', 7), ('p', 2), ('q', 3), ('s', 4), ('t', 3), ('q', 2), ('s', 6), ('t', 10), ('s', 6),
          ('q', 2), ('s', 4), ('t', 3), ('q', 3), ('p', 2), ('.', 7))
draw_rows(f3, 50, [R50, R50, R52, R52, R54, R54, R56, R56, R58, R58, R58, R61, R61])

# hair bottom locks over the shoulders (drawn after the collar)
locks = {46: [(8, 57)], 47: [(10, 22), (26, 38), (44, 55)], 48: [(10, 20), (28, 36), (46, 53)],
         49: [(12, 18), (29, 35), (47, 51)], 50: [(13, 17), (30, 34), (48, 50)], 51: [(30, 34)]}
for yy, segs in locks.items():
    for (x0, x1) in segs:
        hair_row(f3, yy, x0, x1, off=yy)

# rebuild right rows 63-74 (remove front ponytail bottom) mirroring the left
f3.select(0, 63, 27, 12).flip('h').copy_to(39, 63, f3)

# back ponytail hanging down her left (viewer's left), over everything
bands = [(8, 13, 12, 25), (14, 21, 10, 27), (22, 35, 11, 28), (36, 50, 12, 26),
         (51, 62, 14, 24), (63, 70, 15, 22), (71, 72, 17, 20)]
for y0, y1, x0, x1 in bands:
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            f3.set(x, y, COL['c'])
        f3.set(x0, y, COL['a']); f3.set(x1, y, COL['a'])
        f3.set(x0 + 1, y, COL['d']); f3.set(x1 - 1, y, COL['d'])
for y in range(14, 51):
    f3.set(16, y, COL['e']); f3.set(17, y, COL['e'])
for y in range(18, 24):
    f3.set(18, y, COL['f'])
for y in range(52, 63):
    f3.set(16, y, COL['d']); f3.set(17, y, COL['d'])
f3.set(18, 71, COL['b']); f3.set(19, 71, COL['b']); f3.set(18, 72, COL['b'])

view(f1)
view(f2)
view(f3)
finish([f1, f2, f3])
