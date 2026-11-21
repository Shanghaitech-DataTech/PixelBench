from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

def S(x, y, col):
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, col)

def R(x, y, w, h, col):
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            S(xx, yy, col)

def L(x0, y0, x1, y1, col):
    c.line(x0, y0, x1, y1, col)

# ---------------- palette ----------------
BG   = '#0d0d13'
BGl  = '#1a1a26'
sk   = '#e6b98c'
skL  = '#ffd9a8'
skS  = '#bf8a60'
skD  = '#77502e'
metal= '#9aa0a8'
metalL='#d4dae2'
metalS='#5a606a'
metalD='#2e343c'
hair = '#e8e8e4'
hairS= '#aca8a2'
glowA= '#2fd4b0'
glow = '#5affd8'
core= '#eafffb'
gloww='#9affea'
teeth='#f4f0de'
lip = '#8a4030'
mouth='#24100c'
coat = '#d4d4d0'
coatS= '#a2a29e'
dirt = '#8a7a50'
apron= '#7a4a28'
apronD='#542f16'
apronL='#96592f'
belt = '#33221a'
beltD= '#1d120c'
buckl= '#c8c8c8'
plug = '#c8cad0'
pr   = '#e04040'
pg   = '#40e060'
pb   = '#4070e8'
py   = '#e8c040'
wire = '#d0d0d0'
wireR= '#d03030'
wireY= '#e0b830'
wireB= '#4050c8'
pup  = '#1c1414'
scar = '#1a1c22'
led  = '#40e060'

# ---------------- backdrop ----------------
R(0, 0, 64, 64, BG)
R(6, 1, 52, 62, BGl)

# ---------------- neck ----------------
for y in range(32, 39):
    for x in range(24, 40):
        S(x, y, metal if x >= 32 else skS)
R(32, 32, 8, 7, metalS)
S(31, 33, skS); S(31, 34, skS); S(31, 35, skS); S(31, 36, skD)
L(40, 33, 44, 36, wire); L(41, 35, 42, 39, wireB); L(39, 33, 42, 39, wire)

# ---------------- head ---------
for y in range(8, 33):
    for x in range(16, 48):
        if x <= 31:
            S(x, y, skS)
        else:
            S(x, y, metalS)
for y in range(8, 33):
    for x in range(16, 30):
        S(x, y, sk)
for y in range(16, 30):
    for x in range(16, 21):
        S(x, y, skL)
for y in range(12, 30):
    for x in range(27, 31):
        S(x, y, skS)
S(30, 16, skD); S(30, 20, skD); S(30, 25, skD); S(29, 27, skD)
R(32, 10, 15, 4, metal)
for y in range(12, 31):
    for x in range(43, 47):
        S(x, y, metal)
R(41, 22, 6, 8, metal)
S(44, 24, metalL); S(45, 26, metalD)
for y in range(8, 32):
    S(31, y, scar)
for (x, y) in [(33, 30), (37, 31), (41, 30)]:
    S(x, y, plug); S(x, y - 1, wire)

# ---------------- human eye (left) ---------
R(20, 17, 6, 5, teeth)
for y in range(18, 21):
    for x in range(22, 25):
        S(x, y, pup)
S(23, 19, skD); S(24, 18, pup)
L(20, 17, 26, 17, skD)
L(20, 16, 25, 16, hair)
L(20, 22, 26, 22, skS); L(26, 22, 27, 24, skD)

# ---------------- nose (human side) ---------
L(21, 20, 19, 25, skS); L(24, 20, 25, 26, skS)
S(24, 26, skD); S(25, 25, skS); S(25, 27, skD)

# ---------------- glowing cybernetic eye (robot) ---------
R(36, 15, 9, 7, metalD)
R(37, 16, 7, 5, glowA)
R(38, 17, 5, 4, glow)
S(39, 17, gloww); S(39, 18, core); S(40, 17, core); S(40, 18, glow)
S(38, 18, glow); S(39, 19, glow); S(40, 19, gloww)
R(36, 14, 9, 2, metal)
S(35, 16, metalD)
S(35, 21, glowA); S(34, 22, glowA)
L(43, 22, 42, 28, wire); L(44, 20, 46, 28, wire); L(45, 25, 46, 30, wire)

# ---------------- hair (messy white, spiky top, bangs above eyes) ---------
# bulk cap: smooth arc silhouette, non-self-crossing
c.poly([(13,18),(13,12),(16,7),(20,4),(26,3),(33,3),(40,4),(44,7),(47,11),(47,18),
        (45,20),(41,17),(37,19),(33,16),(29,18),(25,15),(21,17),(17,15),(15,18),(13,18)], hair)
# crisp jagged spikes on top
c.poly([(15,6),(18,1),(20,7)], hair)
c.poly([(24,5),(27,0),(30,6)], hair)
c.poly([(34,4),(37,0),(39,6)], hair)
c.poly([(43,8),(45,3),(47,9)], hair)
# side wild locks hanging down
c.poly([(12,14),(11,18),(14,20),(15,16)], hair)
c.poly([(45,16),(47,20),(48,17),(46,13)], hair)
# a few stray strands on forehead
L(19, 12, 19, 15, hair)
L(28, 12, 29, 16, hair)
L(36, 13, 35, 17, hair)
L(30, 14, 31, 18, hair)
# hair shade at fringe roots
for y in range(15, 18):
    S(20, y, hairS); S(24, y, hairS); S(33, y, hairS); S(37, y, hairS)
S(20, 18, hair); S(33, 18, hair)
# hair framing the human side temple edge
L(13, 18, 14, 22, hair)
S(13, 21, hair); S(13, 22, hair)
# robot side has metal brow instead of hair covering
L(44, 17, 46, 15, hair)

# electrode plugs
plugs = [(19, pr), (24, pb), (35, pg), (40, pr), (44, pb)]
for (px, cap) in plugs:
    for yy in range(0, 9):
        S(px, yy, plug)
        S(px - 1, yy, wire)
    R(px - 1, 0, 2, 2, cap)
    S(px, 2, cap); S(px - 1, 2, cap)
R(28, 1, 2, 9, plug)
R(28, 0, 2, 2, pr)
L(24, 8, 27, 9, wire); L(19, 8, 17, 12, wire); L(40, 8, 44, 12, wire)

# ---------------- maniacal grin ---------
c.poly([(18,25),(19,27),(44,27),(45,25),(33,25),(32,27),(26,25)], mouth)
R(21, 26, 22, 4, mouth)
R(19, 27, 26, 4, mouth)
for (tx, ty) in [(19,26),(20,25),(21,26),(23,25),(24,26),(26,25),(28,26),
                (29,25),(31,26),(33,25),(34,26),(36,26),(37,25),(39,26),
                (41,25),(42,26),(44,25),(45,26)]:
    S(tx, ty, teeth)
for (tx, ty) in [(30,30),(33,31),(36,30)]:
    S(tx, ty, teeth)
L(18, 25, 16, 23, lip); L(45, 25, 47, 23, lip)
L(16, 23, 15, 22, skD); L(47, 23, 48, 22, scar)
L(25, 28, 26, 22, skD); L(38, 28, 37, 22, scar)
R(21, 24, 22, 2, lip)
S(18, 26, lip)

# ---------------- torso ---------
R(8, 38, 48, 22, coat)
c.poly([(4,42),(10,38),(26,38),(30,41),(30,60),(26,60),(6,60),(4,56)], coat)
for y in range(38, 60):
    for x in range(5, 31):
        S(x, y, coat)
R(9, 46, 8, 6, coatS)
S(12, 50, dirt); S(18, 49, dirt); S(23, 52, dirt)
R(10, 40, 4, 3, coatS)
R(32, 42, 10, 16, coatS)
R(24, 34, 12, 6, coat)
L(26, 34, 24, 40, coatS); L(34, 34, 36, 40, coatS)
c.poly([(10,42),(22,36),(34,42),(34,58),(12,58)], apron)
R(12, 42, 22, 16, apronL)
R(13, 44, 20, 14, apronD)
R(17, 46, 10, 8, apron)
L(15, 42, 15, 58, apronD)
L(31, 42, 31, 58, apronD)
S(17, 46, apron); S(26, 46, apron)
R(18, 48, 2, 6, metal)
S(19, 47, wireR)
R(22, 47, 2, 7, metal); S(22, 46, pr)

R(8, 54, 34, 5, belt)
R(6, 55, 2, 12, belt)
L(8, 62, 8, 60, belt)
R(16, 54, 10, 5, buckl)
S(19, 56, beltD); S(20, 56, beltD); S(21, 56, beltD)
R(8, 55, 4, 6, metal); R(8, 52, 3, 3, wireR)
L(10, 52, 12, 51, metal)
R(12, 55, 3, 5, metal); S(12, 54, wireB)
S(12, 60, py); S(11, 61, py)

# ---------------- robotic right arm ---------
c.poly([(38,40),(46,36),(60,36),(62,52),(52,56),(40,52)], metal)
c.poly([(40,50),(50,46),(62,50),(60,63),(50,63),(42,60)], metalS)
R(46, 37, 8, 6, metalL)
R(50, 44, 8, 6, metal)
for y in range(46, 60):
    for x in range(44, 50):
        S(x, y, metal)
for (bx, by) in [(40,39),(58,39),(58,44),(56,52)]:
    S(bx, by, metalD); S(bx, by, plug)
L(40, 45, 52, 43, metalD)
L(50, 51, 58, 50, metalD)
for y in range(50, 52):
    for x in range(44, 60):
        S(x, y, metal)
L(47, 50, 47, 52, metalD); S(47, 51, metalD)
L(56, 46, 57, 52, metalD)
for (bx, by) in [(52,47),(53,47),(54,47)]:
    S(bx, by, led)
L(40, 38, 44, 44, wire); L(43, 38, 41, 44, wireY)
L(45, 44, 50, 47, wireB)
R(44, 30, 3, 3, metalS)
S(45, 29, metal); L(46, 28, 55, 27, metal)

# ---------------- prosthetic hand ---------
R(50, 54, 11, 6, metal)
R(50, 54, 11, 4, metalD)
L(50, 58, 60, 58, metalD)
R(49, 56, 13, 6, metalS)
R(50, 59, 12, 4, metal)
R(52, 60, 4, 3, metal)
R(56, 61, 4, 2, metal)
R(49, 62, 5, 2, metal)
S(53, 63, metal); S(48, 63, metal)
S(50, 63, wire); S(54, 63, wireY); S(57, 63, wireR); S(59, 62, wireB)
L(53, 60, 50, 63, wire); L(55, 60, 53, 63, wireY)
L(58, 60, 60, 62, wireR)
S(52, 62, py); S(51, 62, py)

# ---------------- lighting ---------
L(8, 38, 26, 38, coat)
L(30, 40, 30, 58, coatS)
S(6, 57, coatS)

stats = c.stats()
print(c.stats_text())

finish(c)
