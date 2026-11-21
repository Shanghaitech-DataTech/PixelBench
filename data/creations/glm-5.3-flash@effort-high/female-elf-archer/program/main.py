from pixelbench_api import *

c = new_canvas(64, 64, name="elf_archer")

# ---------------- palette ----------------
SKIN   = c.color('#f2c9a2', 'skin')
SKINSH = c.color('#d9a87b', 'skin_shadow')
HAIR   = c.color('#3f9e4d', 'hair')
HAIRD  = c.color('#28703a', 'hair_dark')
HAIRL  = c.color('#7ccd7c', 'hair_light')
OUT    = c.color('#aad9a2', 'outfit')
OUTD   = c.color('#78b478', 'outfit_dark')
OUTL   = c.color('#cdeec6', 'outfit_light')
LEATH  = c.color('#7d5433', 'leather')
LEATHD = c.color('#583a22', 'leather_dark')
BOWC   = c.color('#a06e38', 'bow')
SHAFT  = c.color('#dcb878', 'shaft')
EYEC   = c.color('#1e2f1c', 'eye')
WHITE  = c.color('#f6faf2', 'white')
MOUTH  = c.color('#c2765a', 'mouth')
GOLD   = c.color('#e6c465', 'gold')

# ---------------- bow on her back (behind everything) ----------------
c.path('M 52 9 Q 60 32 15 55', BOWC, fill=False)
c.path('M 51 9 Q 59 32 15 54', BOWC, fill=False)
c.line(52, 9, 15, 55, WHITE)          # bowstring

# ---------------- quiver + arrows (behind body) ----------------
c.poly([(42, 26), (46, 25), (50, 42), (46, 43)], LEATH, fill=True)
c.line(46, 25, 50, 42, LEATHD)
c.line(42, 26, 46, 43, LEATHD)
# arrow shafts poking above the shoulder
c.line(45, 26, 47, 14, SHAFT)
c.line(47, 26, 49, 16, SHAFT)
c.line(43, 26, 44, 15, SHAFT)
# fletchings
for (fx, fy) in [(47, 14), (46, 13), (48, 13), (49, 16), (48, 15), (50, 15),
                 (44, 15), (43, 14), (45, 14)]:
    c.set(fx, fy, HAIRL)

# ---------------- long back hair ----------------
c.rect(25, 7, 14, 4, HAIR)
c.rect(23, 10, 18, 9, HAIR)
c.rect(22, 18, 20, 10, HAIR)
c.rect(22, 22, 5, 28, HAIR)     # left fall
c.rect(37, 22, 5, 30, HAIR)     # right fall
# shading + strands
c.line(40, 10, 41, 50, HAIRD)
c.line(23, 12, 23, 48, HAIRD)
c.line(28, 8, 27, 12, HAIRL)
c.set(30, 8, HAIRL); c.set(33, 8, HAIRL)
c.set(24, 30, HAIRL); c.set(24, 38, HAIRL)
c.set(40, 34, HAIRL); c.set(39, 44, HAIRL)

# ---------------- neck ----------------
c.rect(31, 23, 4, 4, SKIN)
c.line(31, 24, 34, 24, SKINSH)

# ---------------- torso / tunic ----------------
c.rect(25, 27, 17, 6, OUT)
c.rect(26, 33, 15, 5, OUT)
c.poly([(26, 38), (41, 38), (43, 50), (24, 50)], OUTD, fill=True)   # skirt
c.line(25, 27, 25, 32, OUTD)
c.line(41, 27, 41, 32, OUTD)
c.line(33, 28, 33, 37, OUTD)            # lacing
c.set(33, 29, OUTL); c.set(33, 31, OUTL); c.set(33, 33, OUTL)
c.rect(30, 26, 7, 1, OUTL)              # collar
c.line(26, 41, 40, 41, HAIRD)           # skirt top shadow
c.line(35, 42, 40, 49, OUTD)            # skirt fold

# ---------------- belt ----------------
c.rect(26, 38, 15, 2, LEATH)
c.line(26, 39, 40, 39, LEATHD)
c.set(33, 38, GOLD); c.set(33, 39, GOLD)

# ---------------- arms ----------------
c.rect(22, 28, 3, 11, OUT)              # viewer-left arm
c.line(22, 28, 22, 38, OUTD)
c.rect(22, 39, 3, 3, SKIN)              # hand
c.rect(41, 28, 3, 11, OUT)              # viewer-right arm
c.line(43, 28, 43, 38, OUTD)
c.rect(41, 39, 3, 3, SKIN)

# ---------------- legs + boots ----------------
c.rect(28, 50, 4, 6, SKIN)
c.rect(34, 50, 4, 6, SKIN)
c.rect(27, 55, 5, 6, LEATHD)
c.rect(34, 55, 5, 6, LEATHD)
c.line(27, 55, 31, 55, LEATH)
c.line(34, 55, 38, 55, LEATH)
c.set(32, 60, LEATHD); c.set(39, 60, LEATHD)   # toes

# ---------------- head ----------------
c.ellipse(33, 17, 6, 7, SKIN, fill=True)
c.line(38, 13, 39, 20, SKINSH)          # face shading (light from left)
c.set(38, 21, SKINSH); c.set(37, 22, SKINSH)

# pointed ears
c.poly([(28, 16), (23, 12), (27, 20)], SKIN, fill=True)
c.line(24, 13, 27, 18, SKINSH)
c.poly([(38, 16), (43, 12), (39, 20)], SKIN, fill=True)
c.line(42, 13, 39, 18, SKINSH)

# eyes (three-quarter, shifted right)
c.rect(31, 17, 2, 2, EYEC); c.set(31, 17, WHITE)
c.rect(36, 17, 2, 2, EYEC); c.set(36, 17, WHITE)
c.set(31, 15, HAIRD); c.set(32, 15, HAIRD)
c.set(36, 15, HAIRD); c.set(37, 15, HAIRD)
c.set(34, 19, SKINSH)                   # nose
c.set(33, 21, MOUTH); c.set(34, 21, MOUTH)

# ---------------- front hair / bangs ----------------
c.rect(27, 9, 13, 4, HAIR)
c.set(26, 10, HAIR); c.set(40, 10, HAIR)
c.set(26, 11, HAIR); c.set(40, 11, HAIR)
c.rect(26, 12, 3, 9, HAIR)              # left framing lock
c.rect(38, 12, 3, 9, HAIR)              # right framing lock
c.set(30, 13, HAIR); c.set(33, 13, HAIR); c.set(36, 13, HAIR)
c.set(31, 14, HAIR); c.set(34, 14, HAIR)
c.line(28, 9, 38, 9, HAIRL)             # highlight
c.set(27, 12, HAIRL); c.set(39, 14, HAIRL)
c.line(39, 12, 40, 19, HAIRD)           # right lock shade
c.line(26, 13, 26, 19, HAIRD)

# ---------------- final tidy-up: outline the whole figure ----------------
c.outline('#1d2b1d')

# ---------------- summary + save ----------------
print(c.stats_text())
save('elf_archer', c)

# declare the deliverable
finish(c)
