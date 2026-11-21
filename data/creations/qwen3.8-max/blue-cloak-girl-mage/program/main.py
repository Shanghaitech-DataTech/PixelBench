from pixelbench_api import *

# ---------------------------------------------------------------- palette
OUT    = '#141021'   # outline / darkest
HAIR_L = '#ece6fd'
HAIR_M = '#c8bcef'
HAIR_D = '#9a8bce'
HAIR_X = '#6b5b9e'
HAIR_R = '#f3d3a4'   # warm rim light from the staff

SKIN   = '#f9d8b7'
SKIN_D = '#e5b191'
SKIN_X = '#c78e6f'
BLUSH  = '#f2b3a0'
MOUTH  = '#c65f5c'

EYE_W  = '#ffffff'
EYE_A  = '#ffc846'
EYE_B  = '#e09a22'
EYE_C  = '#8a5413'
PUP    = '#2b1a2c'

CLOAK  = '#2e3d74'
CLOAK_L= '#46599f'
CLOAK_D= '#1e2950'
CLOAK_R= '#7d6f8f'   # warm rim on cloak right edge

GOLD   = '#f2b94c'
GOLD_D = '#b3792a'
ROBE   = '#93a7dc'
ROBE_D = '#657ab6'

BOOT   = '#f6f8fc'
BOOT_D = '#c5cde1'
BOOT_X = '#98a2bc'

WOOD   = '#9c6439'
WOOD_D = '#63401f'
WOOD_L = '#c88e52'

ORB_C  = '#fff8d2'
ORB_M  = '#ffd257'
ORB_O  = '#f79a1c'
ORB_R  = '#d1600f'
GLOW1  = '#ffbe3d66'
GLOW2  = '#ffbe3d33'
GLOW3  = '#ffbe3d1a'
SHAD   = '#0b091840'
SHAD2  = '#0b091866'

# ---------------------------------------------------------------- helpers
def rows(cv, x0, y0, data, cmap):
    for j, line in enumerate(data):
        for i, ch in enumerate(line):
            if ch == '.':
                continue
            cv.set(x0 + i, y0 + j, cmap[ch])

# ---------------------------------------------------------------- layers
ground = new_canvas(64, 64, name="ground")
glowl  = new_canvas(64, 64, name="glowlayer")
art    = new_canvas(64, 64, name="art")

CX = 27          # character centre
SX = 46          # staff shaft x

# ---------------------------------------------------------------- ground
ground.ellipse(28, 59, 15, 2, SHAD)
ground.ellipse(28, 59, 9, 1, SHAD2)

# ---------------------------------------------------------------- glow
glowl.circle(SX, 10, 10, GLOW3)
glowl.circle(SX, 10, 7, GLOW2)
glowl.circle(SX, 10, 5, GLOW1)

# ================================================================ ART
# ---- back hair (behind everything)
art.poly([(17, 12), (15, 26), (18, 35), (23, 33), (27, 35), (31, 33), (36, 35),
          (39, 26), (37, 12), (27, 4)], HAIR_X)
art.ellipse(CX, 14, 10, 10, HAIR_X)

# ---- boots (under the cloak hem)
art.rect(22, 45, 5, 12, BOOT)          # left leg  x22..26
art.rect(28, 45, 5, 12, BOOT)          # right leg x28..32
art.rect(21, 55, 6, 4, BOOT)           # left foot
art.rect(28, 55, 6, 4, BOOT)           # right foot
art.rect(21, 58, 6, 1, BOOT_X)         # soles
art.rect(28, 58, 6, 1, BOOT_X)
art.rect(25, 47, 2, 9, BOOT_D)         # inner shading
art.rect(28, 47, 2, 9, BOOT_D)
art.rect(21, 56, 1, 2, BOOT_D)
art.rect(33, 56, 1, 2, BOOT_D)
art.rect(22, 49, 5, 1, BOOT_D)         # top band
art.rect(28, 49, 5, 1, BOOT_D)
art.rect(22, 50, 5, 1, GOLD_D)
art.rect(28, 50, 5, 1, GOLD_D)

# ---- cloak body
art.path("M 20 26 C 15 31 13 38 12 46 L 16 43 L 21 47 L 27 44 L 33 47 L 38 43 "
         "L 42 46 C 41 38 39 31 34 26 Z", CLOAK)
# folds / shading
art.path("M 20 28 C 17 33 15 39 14 44 L 16 43 L 21 47 L 22 40 Z", CLOAK_D)
art.path("M 34 28 C 37 33 39 39 40 44 L 38 43 L 33 47 L 32 40 Z", CLOAK_D)
art.line(19, 33, 17, 44, CLOAK_D)
art.line(35, 33, 37, 44, CLOAK_D)
art.line(16, 32, 14, 42, CLOAK_L)
art.path("M 34 27 C 38 32 40 38 41 45 L 42 46 C 41 38 39 31 34 26 Z", CLOAK_R)

# ---- inner robe panel
art.poly([(23, 31), (31, 31), (32, 45), (22, 45)], ROBE)
art.poly([(28, 31), (31, 31), (32, 45), (28, 45)], ROBE_D)
art.line(27, 33, 27, 44, ROBE_D)

# ---- belt
art.rect(22, 38, 11, 3, GOLD_D)
art.rect(22, 39, 11, 1, GOLD)
art.rect(26, 38, 3, 3, GOLD)
art.set(27, 39, ORB_M)

# ---- collar / lapels
art.poly([(19, 25), (27, 33), (24, 34), (16, 28)], CLOAK_L)
art.poly([(35, 25), (27, 33), (30, 34), (38, 28)], CLOAK_L)
art.poly([(19, 25), (27, 33), (26, 33), (18, 26)], CLOAK_D)
art.circle(27, 31, 2, GOLD)
art.set(27, 30, ORB_M)
art.set(26, 31, GOLD_D)

# ---- sleeves + arms
art.poly([(20, 27), (16, 34), (14, 42), (19, 44), (22, 36), (23, 29)], CLOAK)
art.poly([(18, 33), (15, 41), (19, 44), (20, 38)], CLOAK_D)
art.ellipse(17, 45, 2, 2, SKIN)
art.set(16, 46, SKIN_D)

art.poly([(34, 27), (39, 30), (43, 34), (44, 39), (39, 40), (36, 35), (32, 31)], CLOAK)
art.poly([(39, 31), (43, 35), (44, 39), (41, 39)], CLOAK_D)

# ---- neck
art.rect(25, 22, 5, 5, SKIN_D)
art.rect(25, 22, 5, 2, SKIN_X)

# ---- face
art.path("M 20 14 Q 20 9 27 9 Q 34 9 34 14 L 34 18 Q 34 23 27 25 Q 20 23 20 18 Z",
         SKIN)
art.path("M 20 18 Q 20 23 27 25 Q 34 23 34 18 L 34 20 Q 33 24 27 25 Q 21 24 20 20 Z",
         SKIN_D)
art.rect(31, 12, 3, 8, SKIN_D)      # soft shade on the right of the face

fmap = {'K': OUT, 'W': EYE_W, 'I': EYE_A, 'B': EYE_B, 'D': EYE_C, 'P': PUP,
        'M': MOUTH, 'S': SKIN_D, 'R': BLUSH, 'N': SKIN_X}
rows(art, 20, 15, [
    ".KKKKK...KKKKK.",   # y15 lash line
    ".KWIII...IIIWK.",   # y16
    ".KIPPB...BPPIK.",   # y17
    ".KDDDD...DDDDK.",   # y18
    "..KKKK...KKKK..",   # y19 lower lash
    ".RR....N....RR.",   # y20 blush + nose
    "...............",   # y21
    "......MM.......",   # y22 mouth
    "......SSS......",   # y23 chin shade
], fmap)
art.set(25, 22, SKIN_X)             # mouth corners
art.set(28, 22, SKIN_X)

# ---- hair: crown + bangs
art.ellipse(CX, 8, 9, 5, HAIR_M)
art.path("M 18 9 Q 18 3 27 3 Q 36 3 36 9 L 36 12 Q 33 8 27 8 Q 21 8 18 12 Z", HAIR_D)
art.ellipse(24, 6, 4, 2, HAIR_L)
art.ellipse(31, 6, 2, 1, HAIR_L)
# fringe spikes
art.poly([(18, 10), (19, 15), (22, 11)], HAIR_M)
art.poly([(24, 11), (27, 16), (30, 11)], HAIR_M)
art.poly([(32, 11), (35, 15), (36, 10)], HAIR_M)
art.poly([(25, 11), (27, 15), (29, 11)], HAIR_D)
art.poly([(19, 10), (20, 14), (21, 11)], HAIR_D)
art.poly([(33, 11), (34, 14), (35, 10)], HAIR_D)

# ---- front side locks (over the cloak)
art.poly([(17, 13), (15, 24), (17, 34), (21, 33), (20, 22), (20, 14)], HAIR_D)
art.poly([(37, 13), (39, 24), (37, 34), (33, 33), (34, 22), (34, 14)], HAIR_D)
art.poly([(17, 14), (16, 24), (18, 32), (19, 31), (18, 22), (18, 15)], HAIR_M)
art.poly([(37, 14), (38, 24), (36, 32), (35, 31), (36, 22), (36, 15)], HAIR_M)
art.poly([(19, 26), (18, 32), (20, 33), (20, 27)], HAIR_X)
art.poly([(35, 26), (36, 32), (34, 33), (34, 27)], HAIR_X)

# ---- warm rim light from the staff (right side)
art.line(36, 8, 37, 14, HAIR_R)
art.line(37, 15, 38, 22, HAIR_R)
art.set(34, 13, SKIN)

# ---- orb head (before outline so it gets a dark ring)
art.circle(SX, 10, 5, ORB_R)
art.circle(SX, 10, 4, ORB_O)
art.circle(SX, 9, 3, ORB_M)
art.circle(SX - 1, 8, 2, ORB_C)
art.set(SX - 2, 7, '#ffffff')
art.set(SX - 1, 7, '#ffffff')

# ---- outline the whole silhouette
art.outline(OUT)

# ================================================================ thin props
# drawn after outline() so the outline pass cannot eat them

# ---- hem gold trim, sitting just above the outlined edge
art.path("M 13 45 L 16 42 L 21 46 L 27 43 L 33 46 L 38 42 L 41 45",
         GOLD_D, fill=False)
art.path("M 13 44 L 16 41 L 21 45 L 27 42 L 33 45 L 38 41 L 41 44",
         GOLD, fill=False)

# ---- staff shaft with hand-built outline (starts under the orb ring)
art.rect(SX - 1, 16, 4, 44, OUT)
art.rect(SX, 17, 2, 42, WOOD)
art.rect(SX + 1, 17, 1, 42, WOOD_D)
art.rect(SX, 17, 1, 42, WOOD_L)
# gold fittings
art.rect(43, 16, 8, 5, OUT)
art.rect(44, 17, 6, 3, GOLD_D)
art.rect(44, 17, 6, 1, GOLD)
art.rect(44, 42, 6, 5, OUT)
art.rect(45, 43, 4, 3, GOLD_D)
art.rect(45, 43, 4, 1, GOLD)
# prongs holding the orb (claws over its lower sides)
art.poly([(41, 14), (43, 9), (44, 15)], GOLD_D)
art.poly([(51, 14), (49, 9), (48, 15)], GOLD_D)
art.set(42, 12, GOLD)
art.set(50, 12, GOLD)
art.set(43, 11, GOLD)
art.set(49, 11, GOLD)

# ---- gripping hand over the shaft
art.ellipse(44, 38, 4, 3, OUT)
art.ellipse(44, 38, 3, 2, SKIN)
art.rect(45, 36, 3, 2, SKIN_D)
art.set(46, 37, SKIN)
art.set(47, 38, SKIN_X)
art.set(43, 40, SKIN_D)

# ---------------------------------------------------------------- sparkles
sp = new_canvas(64, 64, name="sparkles")
def star(cv, x, y, col, big=False):
    cv.set(x, y, col)
    cv.set(x - 1, y, col); cv.set(x + 1, y, col)
    cv.set(x, y - 1, col); cv.set(x, y + 1, col)
    if big:
        cv.set(x - 2, y, col); cv.set(x + 2, y, col)
        cv.set(x, y - 2, col); cv.set(x, y + 2, col)
star(sp, 56, 17, ORB_M, True)
star(sp, 37, 4, ORB_M)
star(sp, 55, 5, ORB_C)
star(sp, 40, 18, GLOW1, True)
star(sp, 58, 26, GLOW2)

result = flatten([ground, glowl, art, sp], name="mage")

view(result)
print(result.stats_text())
finish(result)
