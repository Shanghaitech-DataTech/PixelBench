import math
from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, background=None)

def C(name):
    return c.color(name)

pal = {
 'bg':'#07080f','bg1':'#0d1022','bg2':'#151a36','bg3':'#1d2650',
 'skin_hi':'#ffd9ac','skin':'#eab389','skin_sh':'#c08454','skin_dk':'#7e4a2c','skin_ln':'#331c10',
 'metal_hi':'#e8ecf2','metal':'#a8aeb8','metal_sh':'#535a64','metal_dk':'#2b2f38','metal_ln':'#12141a',
 'glow':'#5cfcff','glow2':'#00c8dd','white':'#ffffff','pupil':'#0a0a12',
 'h_hi':'#f6f6f0','h':'#d0d0c8','h_sh':'#8a8a84','h_dk':'#4e4e4a',
 'coat':'#e2dcc4','coat_sh':'#a39a7e','coat_dk':'#665f4a','grimy':'#7c744e',
 'apron':'#8a4a26','apron_sh':'#5c2f14','apron_dk':'#2e1806',
 'belt':'#241610','tool':'#98a0aa','tool_dk':'#383e48',
 'cable':'#1a1a22','cable_hi':'#3c3c46','wire_r':'#d62838','wire_y':'#e8b428',
 'led_r':'#ff3040','led_g':'#38ff70','led_y':'#ffd830',
}
for n, s in pal.items():
    c.color(s, name=n)

# ---------------- background ----------------
c.rect(0, 0, 64, 64, C('bg'))
c.circle(32, 30, 26, C('bg1'))
c.circle(34, 26, 20, C('bg2'))
c.circle(40, 20, 12, C('bg3'))

# ---------------- torso / coat ----------------
c.poly([(8,64),(10,55),(18,49),(46,49),(54,55),(56,64)], C('coat'))
c.poly([(8,64),(10,55),(17,49),(22,49),(22,64),(11,64)], C('coat_sh'))
c.poly([(42,49),(46,49),(54,55),(56,64),(42,64)], C('coat_dk'))
c.rect(31, 49, 10, 15, C('coat_sh'))
# lapels
c.line(20, 50, 26, 45, C('coat_dk'))
c.line(38, 45, 44, 50, C('coat_dk'))
# neck
c.rect(26, 42, 13, 9, C('skin_sh'))
c.rect(32, 42, 7, 9, C('metal_sh'))
c.rect(25, 43, 15, 3, C('skin_dk'))
# apron
c.poly([(25,49),(39,49),(40,63),(24,63)], C('apron'))
c.poly([(33,49),(39,49),(40,63),(35,63)], C('apron_sh'))
c.line(26, 49, 25, 62, C('apron_dk'))
c.rect(28, 51, 5, 4, C('apron_sh'))
# belt
c.rect(21, 58, 20, 3, C('belt'))
c.rect(28, 58, 7, 3, C('tool_dk'))
c.rect(30, 59, 3, 1, C('tool'))
# pocket + pen on coat left
c.rect(12, 54, 7, 5, C('coat_sh'))
c.line(14, 54, 14, 52, C('wire_y'))
c.set(27, 53, C('tool_dk')); c.set(31, 53, C('tool_dk')); c.set(35, 53, C('tool_dk'))
for gx, gy in [(13,55),(16,58),(13,61),(20,60),(44,60),(46,62)]:
    c.set(gx, gy, C('grimy'))
# eye light spilling onto shoulder
c.set(43, 50, C('glow2')); c.set(42, 51, C('glow2'))

# ---------------- head ----------------
c.ellipse(32, 29, 17, 19, C('skin'))

def half(side, rx=17, ry=19, cy=29):
    pts = [(32, cy - ry)]
    for y in range(cy - ry + 1, cy + ry):
        dx = int(round(rx * math.sqrt(max(0.0, 1 - ((y - cy) / ry) ** 2))))
        pts.append((32 + (dx if side == 'r' else -dx), y))
    pts.append((32, cy + ry))
    return pts

c.poly(half('r'), C('metal'))
c.line(32, 11, 32, 45, C('metal_ln'))
# plate seam + rivets on robot half
c.line(40, 13, 40, 33, C('metal_dk'))
for rx, ry in [(40,13),(40,33),(36,17),(44,20),(36,30)]:
    c.set(rx, ry, C('metal_ln'))
for vy in (34, 36, 38):
    c.line(42, vy, 45, vy, C('metal_ln'))

# ---------------- hair ----------------
c.ellipse(32, 13, 17, 7, C('h'))
c.circle(20, 12, 5, C('h_hi'))
c.circle(30, 9, 5, C('h_hi'))
c.circle(24, 11, 4, C('h'))
c.circle(36, 10, 5, C('h_sh'))
c.circle(41, 13, 4, C('h_dk'))
for (a, b, aa, bb, co) in [
    (19,12,15,6,'h_hi'), (22,9,21,3,'h_hi'), (27,8,26,2,'h'),
    (31,7,31,1,'h_sh'), (36,8,38,3,'h_dk'), (42,10,45,5,'h_dk'),
    (45,13,48,7,'h_sh'), (17,15,14,9,'h'), (46,16,49,11,'h_dk'),
]:
    c.line(a, b, aa, bb, C(co))
for (a, b, aa, bb, co) in [
    (21,12,22,17,'h_sh'), (25,11,26,16,'h'), (29,10,30,15,'h_sh'), (33,10,34,14,'h_dk'),
]:
    c.line(a, b, aa, bb, C(co))
# messy side-swept fringe (right temple overhang)
for (x, y, co) in [(48,13,'h'),(49,14,'h_sh'),(48,15,'h_sh'),(47,16,'h_dk'),(48,17,'h_dk'),
                  (49,18,'h_dk'),(46,19,'h_dk'),(45,20,'h_sh')]:
    c.set(x, y, C(co))

# ---------------- electrode plugs ----------------
for px in (26, 32, 38):
    c.rect(px, 3, 3, 6, C('metal_ln'))
    c.rect(px, 4, 3, 4, C('metal_dk'))
c.set(27, 3, C('led_g')); c.set(33, 3, C('led_r')); c.set(39, 3, C('led_y'))
for (a, b, aa, bb, co) in [
    (29,6,37,4,'cable'), (35,6,43,5,'cable_hi'), (41,6,48,9,'cable'),
    (44,5,50,13,'cable_hi'), (49,9,55,18,'cable'), (51,13,57,26,'cable_hi'),
    (47,22,53,30,'cable'),
]:
    c.line(a, b, aa, bb, C(co))

# ---------------- face ----------------
# human eye (left)
c.ellipse(24, 27, 3, 2, C('white'))
c.circle(24, 27, 1, C('skin_ln'))
c.set(24, 26, C('white'))
c.line(23, 30, 26, 30, C('skin_sh'))
c.line(21, 22, 27, 23, C('h_sh'))
# robotic eye (right)
c.rect(34, 22, 8, 9, C('metal_ln'))
c.rect(35, 23, 6, 7, C('metal_dk'))
c.circle(38, 25, 3, C('glow'))
c.circle(38, 25, 2, C('glow2'))
c.circle(38, 25, 1, C('white'))
c.set(42, 24, C('glow')); c.set(43, 26, C('glow')); c.set(41, 29, C('glow'))
c.set(41, 22, C('metal_hi'))
c.line(35, 22, 41, 23, C('metal_ln'))
# nose (human side)
c.line(29, 29, 30, 35, C('skin_sh'))
c.set(30, 35, C('skin_dk'))
c.set(31, 31, C('skin_sh'))
c.set(30, 33, C('skin_sh'))
# glow spill from cyber eye across the nose bridge
c.set(28, 29, C('glow2')); c.set(28, 30, C('glow'))
c.set(29, 28, C('glow2'))
# cheek shading / rim
c.set(20, 31, C('skin_hi')); c.set(20, 32, C('skin_hi')); c.set(19, 30, C('skin_hi'))
for (x, y, co) in [(16,26,'skin_hi'),(16,30,'skin_hi'),(16,34,'skin_hi'),(16,38,'skin_hi'),
                  (46,30,'metal_ln'),(46,36,'metal_ln'),(46,42,'metal_ln'),(45,44,'metal_ln')]:
    c.set(x, y, C(co))
c.line(42, 40, 45, 44, C('metal_ln'))
# maniacal grin
c.rect(23, 38, 18, 5, C('skin_dk'))
for x in [24,26,28,30,33,35]:
    c.set(x, 38, C('white'))
for x in [25,27,29,32,34,37]:
    c.set(x, 41, C('white'))
c.set(39, 38, C('metal_hi')); c.set(39, 41, C('metal_hi'))
c.set(22, 38, C('skin_ln')); c.set(41, 39, C('skin_ln'))
c.line(24, 44, 40, 44, C('skin_sh'))
c.set(32, 43, C('skin_dk'))

# ---------------- robotic arm (right) ----------------
c.circle(51, 52, 5, C('metal_sh'))
c.circle(51, 52, 4, C('metal'))
c.line(48, 49, 54, 49, C('metal_hi'))
c.rect(48, 53, 9, 6, C('metal'))
c.rect(48, 53, 9, 4, C('metal'))
c.line(48, 53, 56, 53, C('metal_hi'))
c.line(48, 56, 56, 56, C('metal_dk'))
c.rect(49, 57, 8, 1, C('metal_sh'))
c.rect(48, 58, 9, 1, C('metal_dk'))
# palm
c.rect(45, 59, 9, 5, C('metal'))
c.line(46, 59, 53, 59, C('metal_hi'))
c.line(46, 62, 53, 62, C('metal_dk'))
# thumb
c.rect(43, 59, 2, 3, C('metal_sh'))
c.set(43, 58, C('metal_dk'))
# two claw fingers reaching right
c.rect(53, 59, 4, 2, C('metal_hi'))
c.rect(56, 59, 2, 2, C('metal_sh'))
c.rect(53, 62, 4, 2, C('metal_hi'))
c.rect(56, 62, 2, 2, C('metal_sh'))
# wrist cables
c.line(49, 62, 44, 61, C('cable'))
c.line(44, 61, 40, 63, C('cable'))
c.line(48, 63, 42, 63, C('wire_r'))

print(c.stats_text())
finish(c)
