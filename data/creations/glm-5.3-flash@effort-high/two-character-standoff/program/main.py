from pixelbench_api import *

W = H = 128

# ---------- background ----------
bg = new_canvas(W, H, background="#101024", name="bg")

# sky gradient bands (dark dramatic dusk)
sky = [
    (0,  "#0c0c1e"),
    (18, "#141433"),
    (36, "#1d1a3e"),
    (54, "#2a1f45"),
    (72, "#3a2547"),
]
for i, (y, col) in enumerate(sky):
    y2 = sky[i+1][0] if i+1 < len(sky) else 96
    bg.rect(0, y, W, y2-y, col)

# moon
bg.circle(96, 20, 9, "#e8e2d0")
bg.circle(93, 17, 8, "#101024")  # crescent cut

# distant mountains
bg.poly([(0, 96), (18, 70), (34, 88), (52, 62), (70, 90), (88, 66), (108, 92), (127, 74), (127, 96)], "#1a1530")
bg.poly([(0, 96), (30, 80), (60, 96), (90, 78), (127, 96)], "#221a38")

# ground
bg.rect(0, 96, W, 32, "#241c2c")
bg.rect(0, 96, W, 2, "#3a2e40")
for x in range(0, W, 7):
    bg.set(x, 99, "#2f2436")
    bg.set((x+3) % W, 103, "#2f2436")
    bg.set((x+5) % W, 108, "#2b2130")

# energy sparks in the gap (dramatic standoff)
for y in range(40, 96, 6):
    bg.set(64, y, "#7fd4ff")
    bg.set(63, y+2, "#4a9fd8")
    bg.set(65, y+3, "#4a9fd8")

# ---------- knight (left, red armor) ----------
kn = new_canvas(W, H, name="knight")
RED   = "#c03028"
DRED  = "#7a1a16"
LRED  = "#e86050"
STEEL = "#b8bcc8"
DSTL  = "#6a7080"
GOLD  = "#e0b040"
DKIN  = "#e8b890"

# cape behind
kn.poly([(26, 44), (18, 60), (16, 82), (24, 92), (30, 78), (32, 56)], DRED)
# legs
kn.rect(30, 84, 6, 14, DRED)   # back leg
kn.rect(38, 84, 6, 14, RED)    # front leg
kn.rect(28, 96, 9, 4, DSTL)    # back boot
kn.rect(38, 96, 9, 4, STEEL)   # front boot
# torso
kn.rect(28, 60, 18, 26, RED)
kn.rect(28, 60, 18, 4, LRED)   # shoulder highlight
kn.rect(34, 66, 6, 14, GOLD)   # breastplate emblem
kn.rect(28, 82, 18, 3, DRED)   # belt
kn.set(36, 83, GOLD)
# pauldrons
kn.rect(24, 58, 8, 8, LRED)
kn.rect(42, 58, 8, 8, LRED)
kn.rect(24, 64, 8, 2, DRED)
kn.rect(42, 64, 8, 2, DRED)
# head + helmet
kn.rect(32, 46, 10, 12, STEEL)
kn.rect(32, 46, 10, 3, DSTL)   # helm top
kn.rect(33, 52, 8, 3, "#0c0c14")  # visor slit
kn.set(35, 53, "#ff4030")      # glowing eye
kn.rect(31, 44, 12, 3, GOLD)   # crest base
kn.rect(36, 38, 2, 7, GOLD)    # crest plume
kn.set(35, 39, LRED)
# sword arm raised (right side of knight, toward centre)
kn.rect(46, 62, 5, 5, RED)     # upper arm
kn.rect(50, 58, 5, 5, RED)     # forearm
kn.rect(53, 54, 4, 5, DSTL)    # gauntlet
# sword pointing up-forward
kn.line(56, 52, 62, 30, STEEL)
kn.line(57, 52, 63, 30, STEEL)
kn.line(56, 52, 62, 30, "#e8ecf4")
kn.rect(52, 52, 8, 2, GOLD)    # crossguard
kn.rect(54, 54, 2, 4, GOLD)    # grip
# shield arm (left, back)
kn.rect(16, 62, 8, 16, DRED)
kn.rect(15, 60, 10, 4, GOLD)
kn.set(20, 70, GOLD)

# ---------- rogue (right, green cloak) ----------
rg = new_canvas(W, H, name="rogue")
GRN   = "#2e7d46"
DGRN  = "#1a4a2c"
LGRN  = "#4fae6a"
LEATH = "#5a4030"
DLEA  = "#3a2a1e"
SILV  = "#c8ccd8"
DKIN  = "#e8b890"
HAIR  = "#e8e0c8"

# cloak flowing behind (right)
rg.poly([(100, 44), (112, 58), (116, 84), (106, 94), (102, 74), (98, 54)], DGRN)
rg.poly([(100, 46), (108, 58), (110, 80), (104, 88), (100, 70)], GRN)
# legs
rg.rect(88, 82, 6, 14, DLEA)   # back leg
rg.rect(80, 82, 6, 14, LEATH)  # front leg
rg.rect(78, 94, 9, 4, "#2a2018")  # front boot
rg.rect(88, 94, 8, 4, "#2a2018")
# torso
rg.rect(78, 58, 16, 26, GRN)
rg.rect(78, 58, 16, 3, LGRN)
rg.rect(84, 62, 5, 18, DGRN)   # cloak fold front
rg.rect(78, 80, 16, 4, LEATH)  # belt
rg.set(85, 81, SILV)
# shoulders
rg.rect(76, 56, 8, 6, LGRN)
rg.rect(90, 56, 8, 6, LGRN)
# head: hood down-ish, face visible, hair
rg.rect(82, 44, 10, 12, DKIN)  # face
rg.rect(80, 42, 14, 5, GRN)    # hood top
rg.rect(79, 44, 3, 10, GRN)    # hood side
rg.rect(94, 44, 2, 10, GRN)
rg.rect(82, 42, 10, 4, HAIR)   # hair fringe
rg.set(84, 49, "#101018")      # eyes
rg.set(89, 49, "#101018")
rg.rect(85, 53, 4, 1, "#b87860")  # mouth
# dagger arm forward (toward centre, left side)
rg.rect(74, 62, 5, 4, GRN)
rg.rect(70, 60, 5, 4, DKIN)    # forearm
rg.rect(66, 58, 4, 5, LEATH)   # glove
# dagger
rg.line(64, 58, 56, 50, SILV)
rg.line(64, 59, 57, 51, "#eef0f8")
rg.rect(64, 56, 2, 5, DLEA)    # grip
rg.rect(63, 55, 4, 2, GOLD)    # guard
# back arm holding second dagger low
rg.rect(94, 62, 5, 4, GRN)
rg.rect(97, 66, 4, 5, DKIN)
rg.line(99, 72, 103, 80, SILV)
rg.rect(98, 70, 3, 3, DLEA)

result = flatten([bg, kn, rg], name="result")
print(result.stats_text())
finish(result)
