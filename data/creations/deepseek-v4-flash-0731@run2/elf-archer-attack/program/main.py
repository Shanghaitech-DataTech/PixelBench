from pixelbench_api import *

W, H = 44, 47

HAIR   = input_canvas.color('#c30074', 'hair')
HAIRL  = input_canvas.color('#ef5ba1', 'hair_light')
HAIRD  = input_canvas.color('#55002a', 'hair_dark')
SKIN   = input_canvas.color('#c5956a', 'skin')
SKIN2  = input_canvas.color('#df9859', 'skin_dark')
TUN    = input_canvas.color('#252a23', 'tunic')
TUND   = input_canvas.color('#313b31', 'tunic_dark')
WOOD   = input_canvas.color('#74341c', 'wood')
WOODL  = input_canvas.color('#bc6c0c', 'wood_light')
CLOAK  = input_canvas.color('#5d422f', 'cloak')
CLOAKL = input_canvas.color('#d1b6a2', 'cloak_light')
BOOT   = input_canvas.color('#8e7058', 'boot')
GOLD   = input_canvas.color('#ffe75a', 'gold')
OUT    = input_canvas.color('#121311', 'outline')
LEAF   = input_canvas.color('#529439', 'leaf')
LEAFD  = input_canvas.color('#304915', 'leaf_dark')
LEAFZ  = input_canvas.color('#9cde5a', 'leaf_light')
SH     = input_canvas.color('#17003599', 'shadow')

f1 = new_canvas(W, H)
f1.blit(input_canvas, 0, 0)

f2 = new_canvas(W, H)

def hseg(y, x0, x1, col):
    for x in range(x0, x1 + 1):
        f2.set(x, y, col)

# -- leaves --
leaves = [
 (0,35,42,LEAF),(0,36,39,LEAFZ),
 (1,33,42,LEAF),(1,35,41,LEAFZ),(1,42,42,LEAFD),
 (2,32,42,LEAF),(2,34,40,LEAFZ),(2,36,36,LEAFD),
 (3,31,42,LEAF),(3,33,41,LEAFZ),(3,38,38,LEAFD),
 (4,30,42,LEAF),(4,32,40,LEAFZ),(4,36,36,LEAFD),
 (5,31,42,LEAF),(5,33,39,LEAFZ),
 (6,32,42,LEAF),(6,34,40,LEAFZ),
 (7,33,42,LEAF),(7,35,41,LEAFZ),(7,37,37,LEAFD),
 (8,34,42,LEAF),(8,36,40,LEAFZ),
 (9,35,42,LEAF),(9,37,39,LEAFZ),
 (10,36,42,LEAF),(10,38,41,LEAFZ),
 (11,37,42,LEAF),(11,39,41,LEAFZ),
]
for (y, x0, x1, col) in leaves:
    hseg(y, x0, x1, col)

# -- hair --
hair = [
 (3,15,24),(4,13,25),(5,11,26),(6,10,26),(7,9,27),(8,8,27),(9,7,27),(10,6,27),
 (11,5,27),(12,4,27),(13,4,27),(14,3,27),(15,3,26),(16,2,26),(17,2,25),(18,2,24),
 (19,2,23),(20,2,22),(21,1,21),(22,1,20),(23,1,19),(24,1,18),(25,0,17),(26,0,16),
]
for (y, x0, x1) in hair:
    hseg(y, x0, x1, HAIR)
for (y, x0) in [(4,13),(5,11),(6,10),(12,4),(14,3),(16,2),(18,2),(20,2),(22,1),(24,1)]:
    f2.set(x0, y, HAIRL)
for (y, x0) in [(13,4),(15,3),(17,2),(19,2),(21,1),(23,1),(25,0)]:
    f2.set(x0, y, HAIRD)

# -- face --
face = [
 (12,19,24),(13,18,27),(14,18,27),(15,18,27),(16,18,27),(17,18,26),(18,18,26),
 (19,18,25),(20,18,25),(21,19,25),(22,19,24),(23,20,24),(24,21,24),
]
for (y, x0, x1) in face:
    hseg(y, x0, x1, SKIN)
f2.set(22, 15, OUT); f2.set(23, 15, OUT); f2.set(24, 15, OUT)
f2.set(25, 16, SKIN2); f2.set(26, 16, SKIN2); f2.set(26, 17, SKIN2)
f2.set(24, 19, OUT)
f2.set(27, 13, HAIR); f2.set(27, 14, HAIR)
f2.set(17, 17, SKIN2); f2.set(16, 18, SKIN2)

# -- neck + torso --
hseg(24, 22, 25, SKIN)
torso = [
 (25,20,26),(26,19,27),(27,19,27),(28,19,27),(29,19,26),(30,19,26),
 (31,18,25),(32,18,24),(33,18,23),(34,19,22),(35,19,21),(36,19,21),(37,20,20),
]
for (y, x0, x1) in torso:
    hseg(y, x0, x1, TUN)
for (y, x0) in [(26,19),(27,19),(28,19),(29,19),(30,19),(31,18),(32,18),(33,18)]:
    f2.set(x0, y, TUND)
hseg(33, 18, 23, GOLD); hseg(34, 19, 22, GOLD)

# -- draw arm -- (to cheek, elbow back)
f2.line(23, 26, 13, 31, TUND)
f2.line(13, 31, 25, 21, TUND)
f2.line(14, 32, 26, 22, TUND)
# shoulder
f2.set(22, 24, TUND); f2.set(23, 25, TUND)
# hand at cheek (drawing the string)
hseg(19, 24, 25, SKIN); hseg(20, 24, 25, SKIN); f2.set(25, 20, SKIN)
f2.set(24, 21, SKIN)

# -- bow arm -- (forward to grip)
f2.line(25, 26, 31, 24, TUND)
f2.line(25, 27, 32, 25, TUND)
f2.line(25, 28, 32, 26, TUND)
hseg(23, 30, 31, SKIN); hseg(24, 31, 32, SKIN)

# -- cloak --
cloak = [
 (34,13,18),(35,12,18),(36,11,18),(37,10,17),(38,9,16),(39,8,15),(40,7,14),
 (41,6,13),(42,5,12),(43,4,11),(44,3,10),(45,2,9),(46,2,8),
]
for (y, x0, x1) in cloak:
    hseg(y, x0, x1, CLOAK)
for (y, x0) in [(34,13),(35,12),(36,11),(37,10),(38,9),(39,8),(40,7),(41,6),(42,5),(43,4),
               (44,3),(45,2),(46,2)]:
    f2.set(x0, y, CLOAKL)

# -- legs --
f2.line(20, 34, 24, 41, TUND)
f2.line(21, 34, 25, 41, TUND)
f2.line(24, 41, 26, 44, TUND)
f2.line(18, 34, 12, 40, TUND)
f2.line(19, 34, 13, 40, TUND)
f2.line(12, 40, 9, 44, TUND)
f2.set(25, 43, BOOT); f2.set(26, 44, BOOT); f2.set(26, 45, BOOT); f2.set(27, 44, BOOT)
f2.set(28, 44, BOOT); f2.set(27, 45, BOOT)
f2.set(9, 44, BOOT); f2.set(9, 45, BOOT); f2.set(10, 43, BOOT); f2.set(8, 44, BOOT)
f2.set(8, 45, BOOT); f2.set(7, 44, BOOT)

# -- bow --
# grip (thick block around x30-31, y22-28)
for (y, x0, x1) in [(22,30,31),(23,30,31),(24,30,31),(25,30,32),(26,30,32),(27,30,32)]:
    hseg(y, x0, x1, WOOD)
# upper limb (deep curve, bulging forward/right)
f2.path("M 31 22 Q 39 13 42 5", WOOD, fill=False)
f2.path("M 32 23 Q 40 14 43 6", WOOD, fill=False)
f2.path("M 33 24 Q 41 15 43 7", WOOD, fill=False)
f2.set(42, 5, WOODL)
# lower limb
f2.path("M 31 28 Q 41 37 42 45", WOOD, fill=False)
f2.path("M 32 29 Q 42 38 43 46", WOOD, fill=False)
f2.path("M 33 28 Q 42 36 43 44", WOOD, fill=False)
f2.set(42, 45, WOODL)
# string: from upper tip (42,5) to draw hand (25,20) and to lower tip (42,45)
f2.line(42, 5, 25, 20, OUT)
f2.line(42, 45, 25, 20, OUT)
f2.set(25, 20, OUT)

# -- shadow --
for (y, x0, x1) in [(44,4,29),(45,5,28),(46,7,26)]:
    hseg(y, x0, x1, SH)

print(f2.matrix_text())

# ---------- submit ----------
finish([f1, f2])
