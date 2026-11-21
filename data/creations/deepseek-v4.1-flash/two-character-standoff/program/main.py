import math

W = H = 128

REV = {}
def hx(s):
    s = s.lstrip('#')
    return (int(s[0:2],16), int(s[2:4],16), int(s[4:6],16), 255)
def hue(h, ch):
    REV[hx(h)] = ch
    return h

# ---------------- palette ----------------
S0 = hue('#05070e',' ')
S1 = hue('#090d18','.')
S2 = hue('#0e1424',':')
S3 = hue('#141d31','-')
S4 = hue('#1b2742','=')
S5 = hue('#263555','+')
HZ1 = hue('#31405f','+')
HZ2 = hue('#3b4b6d','+')
AR1 = hue('#1e2233','w')
AR2 = hue('#26202e','e')
AG1 = hue('#1b2432','q')
AG2 = hue('#1c2a2c','p')
STAR = hue('#8ea3c4','*')
MOON = hue('#3f4d6b','m')
MOON2 = hue('#55658a','M')

GN0 = hue('#141020','g')
GN1 = hue('#1a1628','G')
GN2 = hue('#221c30','h')
GN3 = hue('#2b2438','H')
GN4 = hue('#0f0c19','j')
STONE = hue('#3a3450','o')

R_DK = hue('#3d0f13','r')
R_DR = hue('#61181c','R')
R_MD = hue('#8f2a28','#')
R_LT = hue('#c04337','@')
R_HI = hue('#e8805f','%')

S_DK = hue('#39414f','s')
S_MD = hue('#68738a','S')
S_LT = hue('#a3b0c4','$')
S_HI = hue('#dbe6f2','&')

CP0 = hue('#2a0b10','c')
CP1 = hue('#41121a','C')

G_DK = hue('#12301e','v')
G_MD = hue('#1e4a2b','V')
G_LT = hue('#2f6b3b','g')
G_HI = hue('#4a9451','W')
G_GL = hue('#7cc26a','w')

L_DK = hue('#33210f','l')
L_MD = hue('#553a22','L')
L_LT = hue('#7d5730','N')

K_DK = hue('#a26a4c','k')
K_MD = hue('#dc9f78','K')
K_LT = hue('#f6d3b0','n')

GOLD = hue('#d9a94b','y')
EYE_G = hue('#a9ff8a','!')
EYE_R = hue('#ff6a45','i')
DARK = hue('#08060c','x')

# ---------------- helpers ----------------
def taper(cv, ax, ay, bx, by, hwA, hwB, col):
    dx = bx - ax; dy = by - ay
    L = math.hypot(dx, dy) or 1.0
    px = -dy / L; py = dx / L
    pts = [(round(ax + px*hwA), round(ay + py*hwA)),
           (round(bx + px*hwB), round(by + py*hwB)),
           (round(bx - px*hwB), round(by - py*hwB)),
           (round(ax - px*hwA), round(ay - py*hwA))]
    cv.poly(pts, col)

def show(cv, x0=0, y0=0, x1=127, y1=127, step=1):
    pal = {p['index']: p['rgba'] for p in cv.palette()}
    out = []
    for y in range(y0, y1+1, step):
        row = []
        for x in range(x0, x1+1, step):
            rgba = tuple(pal[cv.get(x, y)])
            row.append('_' if rgba[3] == 0 else REV.get(rgba, '?'))
        out.append(''.join(row))
    print('\n'.join(out))

# ---------------- background ----------------
base = new_canvas(W, H, name='bg')

ys = [0, 16, 32, 48, 64, 80, 93]
cols = [S0, S1, S2, S3, S4, S5]
for i, cl in enumerate(cols):
    base.rect(0, ys[i], W, ys[i+1]-ys[i], cl)
for i in range(1, 6):
    base.dither(0, ys[i]-1, W, 3, [cols[i-1], cols[i]], pattern='bayer4')

# horizon glow
base.ellipse(64, 96, 64, 22, S5)
base.ellipse(64, 95, 48, 13, HZ1)
base.ellipse(64, 95, 30, 8, HZ2)

# subtle auras behind each fighter
base.circle(33, 74, 29, AR1)
base.circle(33, 74, 20, AR2)
base.circle(95, 74, 29, AG1)
base.circle(95, 74, 20, AG2)

# moon & stars
base.circle(60, 17, 7, MOON)
base.circle(59, 16, 5, MOON2)
for (sx, sy) in [(14,14),(24,26),(44,8),(80,10),(94,22),(110,14),(118,34),(20,40),(8,30),(72,34),(104,44),(36,20)]:
    base.set(sx, sy, STAR)

# ground
base.rect(0, 93, W, 4, GN0)
base.rect(0, 97, W, 8, GN1)
base.rect(0, 105, W, 10, GN2)
base.rect(0, 115, W, 13, GN3)
base.dither(0, 95, W, 2, [GN0, GN1], pattern='checker')
base.dither(0, 104, W, 2, [GN1, GN2], pattern='checker')
base.dither(0, 114, W, 2, [GN2, GN3], pattern='checker')
base.line(0, 93, 127, 93, HZ2)

# ground stones
for (sx, sy, rx, ry) in [(12,124,4,1),(50,122,3,1),(78,125,5,2),(112,123,4,1),(28,109,3,1),(100,108,3,1)]:
    base.ellipse(sx, sy, rx, ry, STONE)
    base.ellipse(sx, sy-1, rx-1, ry-1, GN3)

# shadows
base.ellipse(35, 117, 22, 4, GN4)
base.ellipse(93, 117, 22, 4, GN4)

# ================= KNIGHT (left, facing right) =================
k = new_canvas(W, H, name='knight')

# ---- plume (behind helmet) ----
for i in range(12):
    t = i / 11.0
    x = (1-t)**2*34 + 2*(1-t)*t*22 + t*t*8
    y = (1-t)**2*30 + 2*(1-t)*t*12 + t*t*29
    rr = int(round(4 - 2.2*t))
    k.circle(int(round(x)), int(round(y)), rr, R_DR)
for i in range(10):
    t = i / 9.0
    x = (1-t)**2*35 + 2*(1-t)*t*24 + t*t*11
    y = (1-t)**2*29 + 2*(1-t)*t*13 + t*t*28
    rr = int(round(2.4 - 1.3*t))
    if rr < 0: rr = 0
    k.circle(int(round(x)), int(round(y)), rr, R_MD)
for i in range(7):
    t = i / 6.0
    x = (1-t)**2*33 + 2*(1-t)*t*23 + t*t*13
    y = (1-t)**2*27 + 2*(1-t)*t*12 + t*t*26
    k.set(int(round(x)), int(round(y)), R_LT)

# ---- cape tail (behind, flaring below the shield) ----
k.poly([(26,82),(17,89),(10,101),(13,108),(21,105),(22,92)], CP0)
k.poly([(24,86),(18,95),(14,104),(17,107),(20,101),(20,93)], CP1)
k.line(12,98,13,106, R_DR)

# ---- far leg ----
k.poly([(25,84),(35,84),(35,104),(34,112),(23,112),(22,100)], S_DK)
k.poly([(20,108),(35,108),(34,116),(19,116)], S_DK)
k.rect(20,108,15,2, S_MD)

# ---- near leg ----
k.poly([(40,84),(50,84),(51,98),(47,104),(40,102)], R_DR)
k.circle(45,101,4, S_MD)
k.circle(45,101,2, S_LT)
k.poly([(41,100),(50,100),(51,109),(44,111),(41,106)], R_MD)
k.line(42,101,42,108, R_LT)
k.poly([(42,108),(54,108),(59,112),(59,116),(41,116),(41,111)], S_MD)
k.rect(42,108,13,2, S_LT)
k.rect(55,111,4,2, S_HI)
k.line(41,115,58,115, S_DK)

# ---- torso ----
k.poly([(26,56),(48,54),(52,66),(50,78),(46,84),(31,86),(25,77),(24,64)], R_MD)
k.poly([(45,55),(52,66),(50,78),(46,84),(42,85),(46,74),(45,62)], R_DR)
k.line(30,58,28,76, R_LT)
k.line(33,60,31,78, R_MD)
k.line(30,68,48,66, R_DR)
k.line(31,74,49,72, R_DR)
k.line(31,67,48,65, R_LT)
k.line(32,73,49,71, R_LT)
k.line(50,68,50,78, R_HI)
# belt
k.rect(29,82,18,5, L_DK)
k.rect(36,82,4,5, GOLD)
k.rect(36,82,4,1, hue('#f0c96a','y'))
# tassets
k.poly([(29,87),(36,87),(36,98),(30,98)], R_DR)
k.poly([(41,87),(47,87),(48,97),(42,98)], R_MD)
k.line(42,88,42,96, R_LT)

# ---- pauldrons ----
k.ellipse(28,64,9,8, R_DK)
k.ellipse(27,61,8,5, R_MD)
k.line(21,60,24,58, R_LT)
# near pauldron
k.poly([(40,55),(50,56),(55,63),(52,72),(43,73),(37,65)], R_MD)
k.poly([(43,57),(50,58),(53,63),(50,70),(45,71),(40,65)], R_LT)
k.line(41,66,53,67, R_DR)
k.line(42,70,52,71, R_DR)
k.line(53,61,55,65, R_HI)

# ---- sword arm ----
taper(k, 46, 61, 55, 58, 4.5, 3, R_DR)
taper(k, 55, 58, 56, 48, 2.5, 2.5, S_MD)
k.line(54, 57, 54, 49, S_LT)
# ---- sword ----
taper(k, 57, 44, 71, 27, 2, 0.8, S_LT)    # blade
k.line(58, 43, 71, 27, S_HI)
k.line(56, 43, 70, 27, S_DK)
k.set(71, 26, S_HI); k.set(70, 27, S_HI)
k.line(51, 43, 58, 49, GOLD)               # crossguard
# hand
k.circle(55, 45, 2, S_LT)
k.set(56, 44, S_HI)
k.set(54, 46, S_MD)

# ---- shield ----
k.circle(22, 78, 11, S_DK)
k.circle(22, 78, 10, S_MD)
k.circle(22, 78, 8, R_DR)
k.circle(22, 78, 6, R_MD)
k.circle(22, 78, 4, S_MD)
k.circle(22, 78, 2, S_HI)
k.line(29, 71, 31, 76, S_LT)
k.line(16, 70, 21, 68, S_LT)

# ---- head ----
k.rect(31, 46, 11, 9, S_DK)
k.poly([(26,30),(41,30),(45,34),(46,42),(43,48),(39,51),(29,51),(24,46),(23,38),(24,33)], S_MD)
k.line(24, 34, 24, 45, S_DK)
k.line(26, 31, 30, 31, S_DK)
# dome highlight (front-lit)
k.ellipse(34, 34, 6, 4, S_LT)
k.ellipse(36, 33, 3, 2, S_HI)
# faceplate (front, lit)
k.poly([(39,31),(45,34),(46,42),(42,50),(37,50),(40,42)], S_LT)
k.poly([(43,34),(45,35),(46,42),(42,50),(40,50),(43,43)], S_MD)
k.line(46, 36, 46, 43, S_HI)
# visor
k.rect(33, 41, 13, 3, DARK)
k.rect(33, 40, 13, 1, S_LT)
k.rect(35, 44, 9, 1, S_DK)
# breathers / rivets
k.set(40, 48, S_DK); k.set(42, 48, S_DK); k.set(41, 49, S_DK)

# ================= ROGUE (right, facing left) =================
r = new_canvas(W, H, name='rogue')

# ---- cloak ----
r.poly([(90,50),(102,52),(110,64),(116,82),(115,100),(108,112),(98,112),(93,100),(90,84),(87,66)], G_DK)
r.poly([(98,54),(106,66),(110,84),(108,100),(102,108),(100,92),(99,76),(96,62)], G_MD)
r.line(108, 68, 112, 88, G_LT)
r.line(112, 74, 114, 94, G_DK)
r.line(102, 96, 106, 106, G_LT)

# ---- back leg ----
r.poly([(96,82),(105,84),(108,96),(106,108),(98,110),(94,98)], G_DK)
r.poly([(97,84),(103,86),(105,96),(103,106),(99,107),(96,96)], G_MD)
r.poly([(94,106),(106,106),(110,110),(110,116),(94,116)], L_DK)
r.rect(94,106,12,2, L_MD)
r.rect(104,110,6,2, L_LT)

# ---- front leg (crouched) ----
r.poly([(84,82),(93,84),(93,96),(87,103),(79,101),(78,92)], G_DK)
r.poly([(85,84),(91,86),(91,96),(86,101),(81,99),(80,92)], G_MD)
r.line(80,88,79,97, G_LT)
r.rect(78, 97, 9, 12, G_DK)
r.rect(79, 98, 3, 9, G_MD)
r.poly([(72,107),(86,107),(89,111),(89,116),(72,116)], L_DK)
r.rect(72,107,14,2, L_MD)
r.rect(72,109,4,2, L_LT)

# ---- torso ----
r.poly([(84,54),(100,54),(102,66),(100,80),(96,86),(86,86),(82,76),(82,64)], G_MD)
r.poly([(96,56),(102,66),(100,80),(96,86),(92,86),(95,76),(95,64)], G_DK)
r.line(84,58,83,74, G_LT)
r.line(85,60,84,72, G_HI)
# belt
r.rect(83,81,17,5, L_DK)
r.rect(90,81,3,5, GOLD)
# mantle over shoulders
r.poly([(81,57),(105,55),(108,64),(97,70),(83,68)], G_LT)
r.line(83,59,103,57, G_HI)
r.line(84,66,102,67, G_MD)

# ---- hood ----
r.poly([(85,62),(81,50),(84,41),(92,35),(97,33),(104,39),(107,50),(104,62),(97,65),(89,64)], G_MD)
r.poly([(97,34),(104,39),(107,50),(104,62),(98,64),(102,50),(101,41)], G_DK)
# front rim (lit, thin)
r.poly([(86,62),(81,50),(84,41),(89,38),(89,44),(84,50),(88,62)], G_LT)
r.line(86,45,84,51, G_HI)
r.line(84,51,87,59, G_HI)
# peak fold
r.poly([(92,35),(97,33),(101,40),(96,41)], G_LT)
r.line(94,37,99,38, G_HI)
# interior shadow around face
r.poly([(94,42),(100,42),(102,51),(99,59),(95,61),(96,51)], G_DK)
# face cavity
r.ellipse(88, 50, 4, 6, DARK)
r.poly([(85,45),(88,44),(92,46),(92,53),(88,57),(85,53)], DARK)
# jaw & chin
r.ellipse(88, 54, 3, 3, K_MD)
r.ellipse(87, 55, 2, 2, K_LT)
r.line(85, 56, 89, 57, K_DK)
r.set(88, 51, K_MD)
# eye
r.set(84, 48, EYE_G); r.set(85, 48, EYE_G); r.set(85, 47, hue('#d8ffc0','+'))
r.set(83, 49, G_HI)

# ---- dagger arm ----
taper(r, 88, 64, 83, 73, 4, 3, G_MD)
taper(r, 83, 73, 79, 84, 3, 2.5, G_LT)
r.line(85, 65, 81, 73, G_HI)
r.circle(78, 85, 3, K_MD)
r.circle(78, 84, 2, K_LT)
# dagger
taper(r, 78, 86, 70, 92, 2, 1, S_LT)
r.line(79, 85, 71, 91, S_HI)
taper(r, 76, 84, 82, 89, 1.5, 1.5, GOLD)

# ---- far arm ----
r.poly([(100,62),(105,70),(104,80),(100,80),(100,70)], G_DK)
r.circle(101, 80, 3, G_DK)

# ---------------- composite ----------------
OUTK = hue('#181018','x')
OUTR = hue('#0b1a12','x')
kc = k.copy(name='k_halo')
kc.outline(OUTK)
rc = r.copy(name='r_halo')
rc.outline(OUTR)
base.blit(kc, 0, 0)
base.blit(k, 0, 0)
base.blit(rc, 0, 0)
base.blit(r, 0, 0)

# dust motes in the gap
for (dx, dy) in [(62,104),(66,96),(59,88),(68,110),(63,74),(71,101),(60,62)]:
    base.set(dx, dy, hue('#4a5c82','*'))

def sil(cv, x0=0, y0=0, x1=127, y1=127, step=2):
    pal = {p['index']: p['rgba'] for p in cv.palette()}
    out = []
    for y in range(y0, y1+1, step):
        row = []
        for x in range(x0, x1+1, step):
            rgba = tuple(pal[cv.get(x, y)])
            row.append('.' if rgba[3] == 0 else '#')
        out.append(''.join(row))
    print('\n'.join(out))

# gap tension: faint vertical shimmer between the two fighters
GL1 = hue('#2c3a58','=')
GL2 = hue('#38486b','=')
for gy in range(30, 118, 3):
    if gy % 6 == 0:
        base.set(63, gy, GL1)
    else:
        base.set(64, gy, GL2)
base.line(63, 34, 64, 40, GL2)

show(base, 0, 0, 127, 127, 2)
print(base.stats_text())
print('palette entries:', len(base.palette()))
save('standoff', base)
finish(base)
