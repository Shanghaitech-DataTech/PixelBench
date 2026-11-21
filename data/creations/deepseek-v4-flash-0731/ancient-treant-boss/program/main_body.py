from pixelbench_api import new_canvas, finish
import random

W = 256
c = new_canvas(W, W, background="#0a1510", name="treant")

BG="#0a1510"; CANOPY="#07100a"; GLOW="#1c3322"
RAY_A="#6f8f4f"; RAY_B="#a8c878"; RAY_C="#d8e4ae"
GROUND="#161a12"; GROUND2="#1e2418"; POOL="#2a3a20"
OUT="#050504"; BARK_D="#2c1d10"; BARK_M="#4d3019"; BARK_L="#6f4a26"; BARK_H="#94663a"
MOSS_D="#2e4f1e"; MOSS_M="#4d7a2e"; MOSS_L="#70a048"
EYE_OUT="#357f26"; EYE_GLOW="#52d838"; EYE_CORE="#c6fca0"
VINE="#24401a"; LEAF="#3f6b28"; ROCK="#1c1a14"

def mx(pts):
    return [(W - x, y) for x, y in pts]

# ---------------- background: forest, clearing, god rays ----------------
c.poly([(0,0),(255,0),(255,42),(212,66),(150,52),(90,72),(40,58),(0,40)], CANOPY)
# distant tree silhouettes on both sides
c.poly([(0,0),(30,0),(26,80),(30,160),(24,240),(34,255),(0,255)], "#060d08")
c.poly([(255,0),(W-30,0),(W-26,80),(W-30,160),(W-24,240),(W-34,255),(255,255)], "#060d08")
c.poly([(30,0),(56,0),(50,200),(60,255),(18,255),(22,120)], "#081208")
c.poly([(W-30,0),(W-56,0),(W-50,200),(W-60,255),(W-18,255),(W-22,120)], "#081208")
# clearing ambient glow behind the creature
c.ellipse(128,150,104,86, GLOW)
# forest floor
c.rect(0,166, W, W-166, GROUND)
c.ellipse(128,208,84,20, POOL)
c.ellipse(70,220,40,14, GROUND2)
c.ellipse(186,224,44,16, GROUND2)
c.ellipse(30,214,10,5, "#121610")
c.ellipse(214,216,9,5, "#121610")
c.ellipse(110,238,12,6, "#121610")
c.ellipse(150,242,11,5, "#121610")
# god rays pouring down
for pts, col in [ ([(136,0),(166,0),(190,255),(118,255)], RAY_C),
                ([(86,0),(110,0),(124,255),(64,255)], RAY_B),
                ([(178,0),(206,0),(222,255),(154,255)], RAY_A),
                ([(38,0),(64,0),(78,255),(24,255)], RAY_A),
                ([(214,0),(238,0),(250,255),(196,255)], RAY_B) ]:
    c.poly(pts, col)
# bushes at the base of the picture
c.ellipse(25,208,23,15, "#0d1a10")
c.ellipse(231,206,23,15, "#0d1a10")

# ---------------- roots rising from the ground (behind trunk) ----------------
back_roots = [
    [(104,186),(70,198),(38,206),(24,212),(30,204),(64,194),(96,188)],
    [(124,190),(112,204),(100,218),(94,226),(104,214),(118,202),(128,194)],
    mx([(104,190),(88,206),(76,218),(70,226),(80,214),(94,202),(102,194)]),
    mx([(124,186),(152,198),(184,206),(198,212),(192,204),(160,194),(130,188)]),
]
for pts in back_roots:
    c.poly(pts, BARK_D)
    c.poly(pts, OUT, fill=False)

# shadow under the trunk
c.ellipse(128,196,62,12, "#0c0e0a")

# ---------------- trunk ----------------
trunk_d = ("M 128 44 Q 64 50 72 84 Q 88 104 92 132 Q 96 160 98 192 "
          "L 158 192 Q 160 160 164 132 Q 168 104 184 84 Q 192 50 128 44 Z")
c.path(trunk_d, BARK_M, fill=True)
c.dither(96,58,64,116, [BARK_D, BARK_M], "bayer4")
c.path(trunk_d, OUT, fill=False)

for d in ["M 118 58 Q 112 96 114 136 Q 116 166 118 190",
          "M 138 58 Q 144 96 142 136 Q 140 166 138 190",
          "M 102 78 Q 96 114 100 152 Q 102 170 100 188",
          "M 154 78 Q 160 114 156 152 Q 154 170 156 188",
          "M 90 90 Q 87 116 91 142 Q 93 158 92 182",
          "M 166 90 Q 169 116 165 142 Q 163 158 164 182",
          "M 120 58 Q 124 98 122 138 Q 124 166 124 190",
          "M 134 58 Q 130 96 132 136 Q 130 166 132 190"]:
    c.path(d, BARK_D, fill=False)
for d in ["M 126 58 Q 128 100 126 140 Q 128 170 128 190",
          "M 108 80 Q 106 120 108 150",
          "M 148 80 Q 150 120 148 150"]:
    c.path(d, BARK_L, fill=False)

# dense bark speckle detail (only where bark already is)
random.seed(7)
bm = c.color(BARK_M)
bl = c.color(BARK_L)
for _ in range(240):
    x = random.randint(80, 176)
    y = random.randint(50, 190)
    if c.get(x, y) == bm:
        c.set(x, y, BARK_D if random.random() < 0.5 else bl)

# ---------------- crown of branches on top ----------------
crowns = [
    ([(114,48),(117,22),(123,10),(128,20),(133,10),(139,22),(142,48)], [(128,2),(128,12),(124,16),(120,20),(132,20),(136,16)]),
    ([(96,62),(78,42),(68,36),(74,48),(58,32),(50,38),(64,54),(86,68)], [(50,38),(44,30),(58,40),(68,44)]),
    (mx([(96,62),(78,42),(68,36),(74,48),(58,32),(50,38),(64,54),(86,68)]), mx([(50,38),(44,30),(58,40),(68,44)])),
    ([(76,72),(62,60),(54,62),(64,74),(82,82)], [(54,62),(48,56),(60,54)]),
    (mx([(76,72),(62,60),(54,62),(64,74),(82,82)]), mx([(54,62),(48,56),(60,54)])),
]
for body, twigs in crowns:
    c.poly(body, BARK_M)
    c.poly(body, OUT, fill=False)
    for a, b in zip(twigs[0::2], twigs[1::2]):
        c.line(a[0], a[1], b[0], b[1], OUT)

# ---------------- arms / branch arms with claw-like twigs ----------------
left_arm = [(82,78),(40,100),(18,124),(14,142),(22,150),(30,138),(44,118),(66,102),(84,92)]
c.poly(left_arm, BARK_M)
c.poly(left_arm, OUT, fill=False)
c.poly(mx(left_arm), BARK_M)
c.poly(mx(left_arm), OUT, fill=False)
# arm bark lines + highlights
for a, b in [((76,86),(38,104)), ((70,96),(30,120)), ((58,100),(24,132)),
            ((80,82),(44,102)), ((64,92),(34,116))]:
    c.line(a[0], a[1], b[0], b[1], BARK_D)
for a, b in [((176,86),(218,104)), ((186,96),(226,120)), ((198,100),(232,132)),
            ((176,82),(212,102)), ((192,92),(222,116))]:
    c.line(a[0], a[1], b[0], b[1], BARK_D)
# claws
for a, b in [((16,128),(6,142)), ((18,137),(8,152)), ((22,147),(14,160)),
            ((12,130),(2,146)), ((28,140),(20,156)),
            ((240,128),(250,142)), ((238,137),(248,152)), ((234,147),(242,160)),
            ((244,130),(254,146)), ((228,140),(236,156))]:
    c.line(a[0], a[1], b[0], b[1], OUT)

# moss pads on shoulders and chest
for (x, y, rx, ry, col) in [(86,86,18,9,MOSS_D),(78,96,12,7,MOSS_M),(84,80,8,5,MOSS_M),
                           (170,86,18,9,MOSS_D),(178,96,12,7,MOSS_M),(164,98,12,7,MOSS_M),
                           (112,148,14,9,MOSS_D),(144,148,14,9,MOSS_D),(128,140,10,8,MOSS_M),
                           (96,124,9,14,MOSS_D),(160,124,9,14,MOSS_D)]:
    c.ellipse(x, y, rx, ry, col)
mm = c.color(MOSS_M)
for _ in range(130):
    x = random.randint(76, 180)
    y = random.randint(74, 156)
    if c.get(x, y) == mm:
        c.set(x, y, MOSS_L)

# knots
for (x, y, rx, ry) in [(122,150,4,5),(134,152,4,5)]:
    c.ellipse(x, y, rx, ry, BARK_D)

# ---------------- face (glowing green eyes in the trunk) ----------------
for cx in (106, 150):
    c.poly([(cx-14,100),(cx+14,92),(cx+15,99),(cx-13,104)], OUT)   # heavy brows
    c.ellipse(cx, 112, 11, 13, "#0a0806")                          # dark sockets
    c.ellipse(cx, 114, 9, 12, EYE_OUT)
    c.ellipse(cx, 116, 6, 9, EYE_GLOW)
    c.ellipse(cx, 118, 3, 5, EYE_CORE)
    c.line(cx, 109, cx, 127, "#060604")
# grim maw / crack below the eyes
c.poly([(106,138),(114,144),(122,140),(130,146),(138,140),(146,144),(152,138),
       (146,152),(136,148),(128,154),(120,148),(112,152),(104,146)], "#060604")
c.path("M 108 142 Q 128 136 148 142 Q 140 150 128 146 Q 116 150 108 142 Z", BARK_D, fill=True)
c.line(114,138, 142,142, "#060604")

# ---------------- hanging vines ----------------
for a, b in [((38,120),(34,156)), ((46,112),(42,162)), ((24,140),(20,166)),
            ((60,102),(56,134)), ((128,20),(126,40)),
            ((218,120),(222,156)), ((210,112),(214,162)), ((232,140),(236,166)),
            ((196,102),(200,134))]:
    c.line(a[0], a[1], b[0], b[1], VINE)

# ---------------- roots rising up in front of the trunk ----------------
front_roots = [
    [(100,190),(84,166),(72,146),(64,140),(70,134),(80,150),(92,168),(104,186)],
    mx([(100,190),(84,166),(72,146),(64,140),(70,134),(80,150),(92,168),(104,186)]),
    [(116,194),(110,178),(104,168),(110,164),(118,176),(124,192)],
]
for pts in front_roots:
    c.poly(pts, BARK_D)
    c.poly(pts, OUT, fill=False)

# ---------------- grass, rocks, leaves, glints ----------------
tufts = [(30,182,4),(50,178,4),(70,184,4),(90,178,5),(110,186,4),(130,180,5),
        (150,186,4),(170,178,5),(190,182,4),(210,178,4),(230,184,4),
        (58,196,4),(148,198,4),(196,196,4),(84,206,4),(172,208,4)]
for x, y, w in tufts:
    c.poly([(x, y+4), (x+w, y), (x+2*w, y+4)], MOSS_D)
for x, y, rx, ry in [(40,212,7,5),(200,222,8,6),(140,236,9,6),(88,230,6,4),(172,234,6,4)]:
    c.ellipse(x, y, rx, ry, ROCK)
for (x, y, col) in [(150,66,LEAF),(162,60,LEAF),(176,74,LEAF),(60,148,LEAF),(200,128,LEAF),
                   (210,142,LEAF),(88,186,LEAF),(120,212,LEAF),(150,208,LEAF),(182,198,LEAF),
                   (70,112,LEAF),(190,108,LEAF),(104,178,LEAF),(64,176,LEAF),(128,70,LEAF),
                   (94,52,LEAF),(166,50,LEAF),(38,164,LEAF),(218,160,LEAF),(168,120,LEAF)]:
    c.set(x, y, col)
for (x, y, col) in [(120,92,RAY_C),(142,62,RAY_C),(160,124,RAY_C),(100,152,RAY_C),
                   (182,88,RAY_C),(76,122,RAY_C),(204,180,RAY_C),(110,56,RAY_C)]:
    c.set(x, y, col)
# foreground grass to seat the creature
for (x, y, w, col) in [(120,196,6,MOSS_D),(132,194,6,MOSS_M),(96,200,6,MOSS_D),
                       (144,200,6,MOSS_D),(108,206,5,MOSS_M),(140,204,5,MOSS_M)]:
    c.poly([(x, y+3), (x+w, y), (x+2*w, y+3)], col)

# ---- extra detail: rim light on the left, moss drips, sparkles, root tendrils ----
for a, b in [((85,64),(78,88)), ((83,118),(77,148)), ((81,158),(79,182)),
            ((66,96),(30,116)), ((212,112),(244,128))]:
    c.line(a[0], a[1], b[0], b[1], BARK_H)
for a, b in [((78,92),(80,108)), ((170,92),(166,106)), ((128,156),(128,170))]:
    c.line(a[0], a[1], b[0], b[1], MOSS_D)
for (x, y) in [(128,6),(118,12),(140,14),(108,20),(150,24),(96,30),(158,32),
              (132,44),(122,58),(70,70),(186,66),(112,88),(150,120),(128,180),
              (60,140),(200,150),(84,58),(176,54)]:
    c.set(x, y, "#e8f0c0")
for a, b in [((64,196),(52,212)), ((190,198),(204,214)), ((112,202),(104,214)),
            ((150,204),(158,216)), ((136,208),(132,220))]:
    c.line(a[0], a[1], b[0], b[1], BARK_H)

print(c.stats_text())
finish(c)
