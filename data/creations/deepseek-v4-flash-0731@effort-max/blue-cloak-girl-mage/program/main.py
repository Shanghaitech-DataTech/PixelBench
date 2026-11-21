from pixelbench_api import *

c = new_canvas(64, 64)

# ---------------- palette ----------------
o  = c.color('#1a1d33', 'outline')
s  = c.color('#f6d3ae', 'skin')
S  = c.color('#eeb68c', 'skin_shade')
D  = c.color('#d99a6c', 'skin_dark')
B  = c.color('#f0a58a', 'blush')
h  = c.color('#eef1f8', 'hair')
H  = c.color('#ffffff', 'hair_light')
k  = c.color('#aeb6cc', 'hair_shade')
K  = c.color('#7f88a4', 'hair_dark')
e  = c.color('#ffffff', 'eye_white')
i  = c.color('#2fd4c0', 'iris')
I  = c.color('#18a08f', 'iris_dark')
p  = c.color('#10162c', 'pupil')
L  = c.color('#b8fff0', 'eye_light')
m  = c.color('#a04a3a', 'mouth')
cN = c.color('#28336e', 'cloak')
C  = c.color('#3d4a94', 'cloak_light')
d  = c.color('#1a2248', 'cloak_dark')
g  = c.color('#d8a83c', 'gold')
G  = c.color('#f2cf6a', 'gold_light')
g2 = c.color('#8a6420', 'gold_dark')
w  = c.color('#f4f4fa', 'boot')
W  = c.color('#c6c6d6', 'boot_shade')
b2 = c.color('#8f8fa4', 'boot_dark')
st = c.color('#7a4c2a', 'staff')
sd = c.color('#4e2f18', 'staff_dark')
sl = c.color('#96603a', 'staff_light')
oc = c.color('#ffd94a', 'orb_core')
ob = c.color('#ffc020', 'orb_bright')
om = c.color('#e08c14', 'orb_mid')
sh = c.color('#181e3e', 'shadow')
sh2 = c.color((24, 28, 60, 120), 'shadow2')
gl1 = c.color((255, 190, 40, 26), 'glow_soft')
gl2 = c.color((255, 180, 30, 60), 'glow')
gp  = c.color((255, 190, 60, 55), 'glow_pool')

# ---------------- ground shadow ----------------
c.ellipse(36, 60, 18, 2, sh)          # pool shadow under body
c.ellipse(55, 58, 3, 1, sh2)          # staff tip shadow
c.ellipse(52, 59, 6, 2, gp)           # warm glow pool under orb

# ---------------- staff + orb (behind body) ----------------
c.circle(50, 7, 6, gl1)                # soft outer aura
c.circle(50, 7, 4, gl2)                # tighter glow
c.line(49, 5, 56, 58, sd)              # staff shaft: dark edge
c.line(48, 4, 55, 57, st)              # staff shaft: main
c.line(50, 6, 57, 59, sl)              # staff shaft: lit edge
c.circle(50, 7, 3, om)                  # orb body
c.circle(50, 7, 2, ob)                  # orb bright
c.circle(50, 7, 1, oc)                  # orb core (48..52, 6..8)
c.set(49, 6, oc)
# sparkles
for (sx, sy, sc) in [(44, 3, oc), (55, 13, oc), (43, 10, ob), (53, 15, oc), (51, 1, oc)]:
    c.set(sx, sy, sc)

# ---------------- cloak robe ----------------
robe = [(25, 27), (39, 27), (44, 33), (46, 47), (44, 52), (20, 52), (18, 47), (20, 33)]
c.poly(robe, d)                          # base robe (dark blue cloak)
c.poly(robe, o, fill=False)              # silhouette outline
# left fold (shade)
c.poly([(26, 27), (32, 27), (31, 37), (28, 46), (25, 52), (21, 52), (20, 44), (22, 34)], d)
# right fold (caught light)
c.poly([(34, 27), (39, 27), (43, 33), (45, 46), (44, 52), (41, 52), (39, 44), (36, 36)], cN)
c.poly([(35, 27), (38, 27), (41, 35), (42, 46), (41, 52), (39, 52), (38, 46), (36, 36)], C)

# ---------------- hem trim ----------------
c.rect(21, 50, 22, 2, g)                # gold hem band
c.rect(22, 52, 20, 1, g2)               # hem underline

# ---------------- collar / hood ----------------
c.ellipse(31, 27, 9, 4, d)              # collar behind neck
c.ellipse(31, 27, 9, 4, o, fill=False)

# ---------------- arm + hand to staff ----------------
c.line(41, 29, 46, 33, d)                # arm from shoulder
c.set(46, 34, d); c.set(46, 35, d)
c.rect(47, 35, 6, 6, d)                  # gloved hand
c.rect(48, 36, 3, 2, C)                  # hand highlight
c.rect(47, 35, 6, 6, o, fill=False)
c.rect(46, 34, 5, 1, g)                  # gold cuff
c.rect(45, 33, 2, 1, g)

# ---------------- boots ----------------
def boots(x0):
    c.rect(x0, 53, 6, 5, w)
    c.rect(x0, 53, 2, 4, W)
    c.rect(x0, 53, 6, 5, o, fill=False)
    c.rect(x0 + 1, 58, 4, 1, b2)
    c.rect(x0, 59, 6, 1, o)
boots(24)
boots(34)

# ---------------- brooch ----------------
c.set(32, 28, g); c.set(31, 29, g); c.set(33, 29, g); c.set(32, 30, g); c.set(32, 29, oc)

# ---------------- head (pixel rows) ----------------
R = {
 2:  '.' * 10 + 'h' + '..' + 'h' + '.' * 10,
 3:  '.' * 8 + 'H' + 'h' * 6 + 'H' + '.' * 8,
 4:  '.' * 7 + 'h' * 12 + '.' * 5,
 5:  '.' * 6 + 'h' * 14 + '.' * 4,
 6:  '.' * 5 + 'H' * 2 + 'h' * 14 + '.' * 3,
 7:  '.' * 4 + 'h' * 18 + '.' * 2,
 8:  '.' * 4 + 'k' * 2 + 'h' * 16 + 'k' * 2,
 9:  '..' + 'h' * 2 + 'o' + 's' * 14 + 'h' * 5,
 10: '..' + 'h' * 2 + 'o' + 's' * 14 + 'h' * 5,
 11: '..' + 'h' * 2 + 'o' + 'k' * 3 + 's' * 8 + 'k' * 3 + 'h' * 5,
 12: '..' + 'h' * 2 + 'o' + 'k' + 's' * 12 + 'k' + 'h' * 5,
 13: '..' + 'h' * 2 + 'o' + 's' * 14 + 'h' * 5,
 14: '..' + 'h' * 2 + 'o' + 's' * 14 + 'h' * 5,
 15: '..' + 'h' * 2 + 'o' + 's' * 14 + 'h' * 5,
 16: '..' + 'h' * 2 + 'o' + 's' * 14 + 'h' * 5,
 17: '..' + 'h' * 2 + 'o' + 's' * 14 + 'h' * 5,
 18: '..' + 'h' * 3 + 'o' + 's' * 12 + 'h' * 6,
 19: '..' + 'h' * 3 + 'o' + 's' * 10 + 'h' * 6,
 20: '..' + 'h' * 3 + 'o' + 's' * 8 + 'h' * 7,
 21: '..' + 'h' * 4 + 'o' + 's' * 6 + 'h' * 7,
 22: '..' + 'h' * 4 + 'o' + 's' * 4 + 'h' * 7,
 23: '..' + 'h' * 4 + 'o' + 's' * 4 + 'h' * 7,
 24: '.' * 11 + 'o' + 'D' * 2 + 'o' + '.' * 10,
}
CH = {'h': h, 'H': H, 'k': k, 's': s, 'S': S, 'D': D, 'o': o}
for y, row in R.items():
    for xoff, chv in enumerate(row):
        if chv != '.':
            c.set(20 + xoff, y, CH[chv])

# ---------------- face details ----------------
# brows
for xoff in range(26, 31):
    c.set(xoff, 12, k)
    c.set(37 - (xoff - 26), 12, k)
# eyes
LE = {13: [(26, K), (27, e), (28, L), (29, e), (30, e)],
      14: [(26, p), (27, p), (28, i), (29, i), (30, e)],
      15: [(26, p), (27, i), (28, i), (29, I), (30, e)]}
RE = {13: [(33, e), (34, e), (35, L), (36, e), (37, e)],
      14: [(33, e), (34, i), (35, i), (36, p), (37, p)],
      15: [(33, e), (34, I), (35, i), (36, p), (37, p)]}
for y, cells in LE.items():
    for xx, cc in cells:
        c.set(xx, y, cc)
for y, cells in RE.items():
    for xx, cc in cells:
        c.set(xx, y, cc)
# face extras
for (xx, yy, cc) in [(26, 17, B), (27, 17, B), (36, 17, B), (37, 17, B),
                    (31, 16, S), (31, 18, m), (32, 18, m), (31, 19, D)]:
    c.set(xx, yy, cc)

# shoulder-length hair spilling over the hood
for xx in range(25, 32):
    c.set(xx, 25, h)
for xx in range(33, 40):
    c.set(xx, 25, h)
c.set(38, 26, h); c.set(39, 26, h)
c.set(40, 27, h)

print(c.stats_text())
print(c.matrix_text((19, 1, 44, 24)))
print(c.matrix_text((40, 30, 56, 44)))

finish(c)
