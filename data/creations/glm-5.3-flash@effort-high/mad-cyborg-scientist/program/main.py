# Mad Cyborg Scientist - 64x64 RPG character portrait
c = new_canvas(64, 64, background="#120e1c", name="mad-cyborg-scientist")

# ---------------- palette ----------------
BG    = c.color("#120e1c", "bg")
BG2   = c.color("#1e1730", "bg2")
BG3   = c.color("#2c2340", "bg3")
BG4   = c.color("#0d0a16", "bg4")
SKIN  = c.color("#e8b48c", "skin")
SKINL = c.color("#f6d2a8", "skin-light")
SKIN2 = c.color("#c08a5e", "skin-mid")
SKIN3 = c.color("#8a5a3a", "skin-dark")
MET   = c.color("#b6c0ca", "metal-light")
MET2  = c.color("#7e8894", "metal-mid")
MET3  = c.color("#4e5662", "metal-dark")
MET4  = c.color("#2b313b", "metal-black")
GLOW  = c.color("#5cff6e", "glow")
GLOW2 = c.color("#ccffb4", "glow-hot")
GLOWD = c.color("#2f6a38", "glow-dim")
HAIR  = c.color("#eceae6", "hair")
HAIR2 = c.color("#a9a5a8", "hair-shade")
COAT  = c.color("#d2ccbc", "coat")
COATL = c.color("#eee8d8", "coat-light")
COAT2 = c.color("#a49c8c", "coat-mid")
COAT3 = c.color("#6e6759", "coat-dark")
STAIN = c.color("#8a7148", "stain")
APRN  = c.color("#5e3f26", "apron")
APRN2 = c.color("#3e2a18", "apron-dark")
BELT  = c.color("#33241a", "belt")
BCKL  = c.color("#c9a83f", "buckle")
CABL  = c.color("#23232c", "cable")
RED   = c.color("#c23a44", "cable-red")
TEETH = c.color("#eae6da", "teeth")
MOUTH = c.color("#3a181a", "mouth")
TOOL  = c.color("#9aa0aa", "tool")
OUTL  = c.color("#0a0812", "outline")

# ---------------- background: strong light contrast ----------------
c.rect(0, 0, 64, 64, BG)
c.poly([(0, 0), (30, 0), (16, 64), (0, 64)], BG2)          # light beam from upper-left
c.poly([(0, 0), (14, 0), (6, 64), (0, 64)], BG3)           # brighter core of the beam
c.poly([(63, 6), (63, 64), (34, 64), (48, 26)], BG4)       # dark vignette, right side
c.circle(32, 22, 15, BG2)                                  # faint halo behind head
# dust motes
for (mx, my) in [(8, 18), (11, 30), (6, 44), (52, 12), (57, 26), (50, 20)]:
    c.set(mx, my, BG3)

# ---------------- electrode cables (behind head) ----------------
c.line(27, 4, 21, 0, CABL)
c.line(33, 3, 33, 0, CABL)
c.line(39, 4, 45, 0, CABL)
c.line(28, 4, 24, 0, RED)

# ---------------- skull: left human / right metal ----------------
skull = [(24, 11), (28, 9), (36, 9), (40, 12), (42, 17), (41, 25), (38, 29), (26, 29), (23, 25), (22, 17)]
c.poly(skull, SKIN)
c.poly([(32, 9), (36, 9), (40, 12), (42, 17), (41, 25), (38, 29), (32, 29)], MET2)

# metal plating details
c.line(32, 10, 32, 28, MET)          # lit centre seam edge
c.line(33, 10, 33, 15, MET3)         # panel seams
c.line(33, 22, 33, 28, MET3)
c.line(34, 12, 40, 13, MET3)
c.rect(40, 13, 2, 2, MET3); c.set(40, 13, MET)      # temple bolt
for (rx, ry) in [(36, 11), (39, 11), (34, 27), (38, 27)]:
    c.set(rx, ry, MET)               # rivets
# human side shading
c.line(30, 12, 30, 23, SKIN2)
c.line(31, 12, 31, 23, SKIN2)
c.line(24, 14, 28, 14, SKINL)        # forehead highlight (light from left)

# ---------------- eyes ----------------
# left human eye, angry brow
c.line(24, 16, 29, 18, SKIN3)
c.line(24, 17, 29, 19, SKIN3)
c.rect(25, 19, 4, 2, TEETH)
c.set(27, 19, OUTL); c.set(27, 20, OUTL)
c.line(25, 21, 28, 21, SKIN2)
# right glowing cybernetic eye
c.line(34, 16, 40, 16, MET3)                   # metal brow ridge
c.rect(34, 17, 6, 5, MET4)                     # socket recess
c.rect(35, 18, 4, 3, GLOW)                     # lens
c.set(36, 18, GLOW2); c.set(37, 18, GLOW2); c.set(36, 19, GLOW2)
c.set(40, 18, GLOWD); c.set(40, 20, GLOWD); c.set(33, 19, GLOWD)   # glow spill

# ---------------- nose ----------------
c.line(31, 20, 30, 23, SKIN2)
c.set(29, 24, SKIN3); c.set(31, 24, SKIN3); c.set(32, 24, MET3)

# ---------------- maniacal grin ----------------
c.poly([(23, 25), (40, 24), (41, 25), (38, 28), (26, 28)], MOUTH)
c.line(24, 25, 39, 25, TEETH)
for x in (26, 29, 32, 35, 38):
    c.set(x, 25, MOUTH)
for x in (25, 28, 31, 34, 37):
    c.set(x, 26, TEETH)
c.set(27, 27, TEETH); c.set(31, 27, TEETH); c.set(35, 27, TEETH)
c.set(22, 24, SKIN3); c.set(41, 23, MET3)      # grin creases
c.line(27, 29, 31, 29, SKIN3); c.line(32, 29, 36, 29, MET3)   # under-lip shadow

# ---------------- messy white hair ----------------
hair = [(21, 15), (19, 10), (23, 11), (24, 5), (27, 10), (29, 4), (32, 9),
        (34, 3), (37, 8), (39, 4), (42, 9), (44, 7), (43, 13), (41, 15)]
c.poly(hair, HAIR)
c.line(24, 7, 26, 12, HAIR2)
c.line(31, 6, 33, 11, HAIR2)
c.line(38, 7, 40, 12, HAIR2)
c.line(21, 12, 23, 15, HAIR2)
c.line(42, 10, 43, 13, HAIR2)
c.set(22, 16, HAIR2); c.set(22, 17, HAIR2)     # sideburn

# ---------------- brain electrode plugs ----------------
for (px, py) in [(26, 5), (32, 4), (38, 5)]:
    c.rect(px, py, 3, 2, MET4)
    c.set(px + 1, py, MET)

# ---------------- neck ----------------
c.rect(28, 30, 8, 4, SKIN)
c.rect(32, 30, 4, 4, MET2)
c.line(28, 30, 31, 30, SKIN3)
c.line(32, 30, 35, 30, MET3)
c.line(35, 31, 35, 33, MET3)

# ---------------- lab coat body ----------------
c.poly([(10, 64), (10, 46), (13, 38), (20, 33), (28, 31), (36, 31),
        (44, 33), (51, 38), (54, 46), (54, 64)], COAT)
c.poly([(46, 35), (51, 38), (54, 46), (54, 64), (46, 64)], COAT2)   # shaded right side
c.line(14, 39, 11, 45, COATL)                    # lit left edge
c.line(51, 38, 54, 46, COAT3)
# dirt and grime
c.rect(18, 42, 3, 2, STAIN)
c.rect(21, 57, 3, 2, STAIN)
c.rect(45, 44, 2, 2, STAIN)
c.set(16, 48, STAIN); c.set(43, 60, STAIN)

# ---------------- leather apron ----------------
c.poly([(26, 37), (38, 37), (40, 41), (40, 63), (24, 63), (24, 41)], APRN)
c.line(24, 41, 24, 62, APRN2)
c.line(40, 41, 40, 62, APRN2)
c.line(25, 62, 39, 62, APRN2)
c.line(26, 37, 38, 37, APRN2)
c.line(30, 38, 30, 44, APRN2); c.line(34, 38, 34, 44, APRN2)
c.set(32, 41, BCKL)
c.set(31, 47, APRN2); c.rect(33, 55, 2, 2, APRN2); c.set(28, 52, APRN2)

# ---------------- tool belt ----------------
c.rect(10, 50, 44, 4, BELT)
c.rect(29, 50, 6, 4, BCKL)
c.rect(31, 51, 2, 2, OUTL)
c.rect(14, 52, 6, 7, APRN2); c.rect(14, 52, 6, 3, BELT)    # left pouch
c.rect(44, 52, 6, 7, APRN2); c.rect(44, 52, 6, 3, BELT)    # right pouch
c.rect(16, 45, 2, 2, TOOL); c.rect(16, 47, 2, 4, RED)      # screwdriver
c.rect(45, 46, 2, 2, TOOL); c.line(45, 48, 46, 51, TOOL)   # wrench

# ---------------- collar and lapels ----------------
c.poly([(24, 32), (28, 30), (36, 30), (40, 32), (37, 36), (27, 36)], COAT3)
c.poly([(25, 34), (30, 34), (27, 45), (23, 40)], COAT2)
c.line(30, 34, 27, 45, COAT3)
c.poly([(39, 34), (34, 34), (37, 45), (41, 40)], COAT3)

# ---------------- left arm: coat sleeve + hand with wrench ----------------
c.poly([(13, 38), (19, 39), (18, 52), (12, 51)], COAT2)
c.line(18, 40, 17, 51, COAT3)
c.line(12, 51, 18, 52, COAT3)
c.rect(11, 52, 6, 5, SKIN)
c.rect(8, 46, 3, 3, TOOL); c.set(9, 46, BG3)
c.line(10, 48, 12, 49, TOOL)
c.line(12, 49, 12, 57, TOOL)
c.set(11, 53, SKIN2); c.set(13, 53, SKIN2); c.set(11, 55, SKIN2); c.set(13, 55, SKIN2)

# ---------------- right arm: exposed metal robotic arm ----------------
c.circle(48, 37, 3, MET3)                        # pauldron
c.circle(48, 37, 2, MET2)
c.set(46, 35, MET); c.set(47, 35, MET)
c.rect(49, 40, 5, 8, MET2)                       # upper arm
c.line(49, 40, 49, 47, MET)
c.line(53, 40, 53, 47, MET3)
c.line(49, 43, 53, 43, MET3)
c.line(54, 41, 54, 46, CABL)
c.rect(49, 47, 5, 3, MET3); c.rect(50, 47, 3, 3, MET2); c.set(51, 48, MET)  # elbow
c.rect(51, 50, 5, 7, MET2)                       # forearm
c.line(51, 50, 51, 56, MET)
c.line(51, 52, 55, 52, MET3); c.line(51, 55, 55, 55, MET3)
c.rect(51, 57, 5, 2, MET4)                       # wrist
c.rect(51, 59, 5, 3, MET3)                       # prosthetic palm
c.rect(51, 61, 1, 2, MET2); c.rect(53, 61, 1, 3, MET2); c.rect(55, 61, 1, 2, MET2)
c.set(50, 60, MET2)
# cables into the prosthetic hand
c.line(50, 48, 45, 50, RED)
c.line(51, 50, 46, 52, CABL)
c.line(52, 58, 48, 60, CABL)
c.line(56, 60, 60, 63, RED)
c.line(51, 62, 49, 63, CABL)

# ---------------- silhouette outlines ----------------
c.line(24, 11, 22, 17, OUTL)
c.line(22, 17, 23, 25, OUTL)
c.line(23, 25, 26, 29, OUTL)
c.line(40, 12, 42, 17, OUTL)
c.line(42, 17, 41, 25, OUTL)
c.line(41, 25, 38, 29, OUTL)
c.line(13, 38, 10, 46, OUTL)
c.line(10, 46, 10, 63, OUTL)
c.line(51, 38, 54, 46, OUTL)
c.line(54, 46, 54, 63, OUTL)

print(c.stats_text())
print(c.matrix_text(region=(16, 0, 48, 32)))
print(c.matrix_text(region=(8, 30, 60, 64)))
print(c.matrix_text(region=(0, 40, 16, 64)))
finish(c)
