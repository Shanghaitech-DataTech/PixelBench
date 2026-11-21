C = new_canvas(64, 64, background=None, name="elf-archer")

# palette
SKIN   = C.color("#f2c9a0", "skin")
SKINSH = C.color("#d9a87c", "skin_shadow")
HAIR   = C.color("#4e9b4e", "hair_green")
HAIRD  = C.color("#356e35", "hair_dark")
HAIRL  = C.color("#7cc47c", "hair_light")
OUTFIT = C.color("#cfe8c0", "outfit_lightgreen")
OUTFITD= C.color("#a3c78f", "outfit_mid")
OUTFITDD=C.color("#7ba56a", "outfit_dark")
LEATHER= C.color("#8a5a33", "leather")
LEATHERD=C.color("#5f3d20", "leather_dark")
WOOD   = C.color("#a5713d", "bow_wood")
WOODD  = C.color("#7a4f28", "bow_wood_dark")
EYE    = C.color("#2f6b3f", "eye_green")
WHITE  = C.color("#ffffff", "white")
MOUTH  = C.color("#c47a6a", "mouth")
GOLD   = C.color("#e0c060", "gold")
FEATHER= C.color("#e8e0c8", "fletching")
BLADE  = C.color("#c8d8c0", "arrowhead")

# ---- hair back layer (long green hair behind body) ----
C.rect(16, 12, 32, 40, HAIR)          # main back mass
C.rect(14, 20, 4, 30, HAIR)           # left fall
C.rect(46, 20, 4, 30, HAIR)           # right fall
C.rect(15, 46, 3, 6, HAIRD)
C.rect(46, 46, 3, 6, HAIRD)
# darker inner shading on back hair
C.rect(18, 16, 4, 32, HAIRD)
C.rect(42, 16, 4, 32, HAIRD)
# light strands
for y in range(14, 48, 3):
    C.set(20, y, HAIRL)
    C.set(43, y+1, HAIRL)

# ---- head ----
C.ellipse(31, 16, 8, 9, SKIN)         # face
C.rect(27, 8, 9, 3, HAIR)             # fringe top
C.rect(25, 10, 4, 6, HAIR)            # left fringe
C.rect(35, 10, 4, 6, HAIR)            # right fringe
C.set(26, 11, HAIRL); C.set(37, 12, HAIRL)

# pointed ears (three-quarter: left ear prominent)
C.poly([(22,15),(18,9),(23,13)], SKIN, fill=True)
C.poly([(41,14),(45,9),(42,14)], SKIN, fill=True)
C.line(19,11,21,14, SKINSH)
C.line(43,11,42,13, SKINSH)

# face shading
C.line(37, 14, 38, 20, SKINSH)        # right side shadow
C.set(36, 21, SKINSH)

# eyes (looking slightly left, three-quarter)
C.rect(26, 16, 2, 2, WHITE)
C.set(26, 16, EYE); C.set(27, 17, EYE)
C.rect(33, 16, 2, 2, WHITE)
C.set(33, 16, EYE); C.set(34, 17, EYE)
C.line(25, 15, 28, 15, HAIRD)         # brows
C.line(32, 15, 35, 15, HAIRD)
C.set(29, 21, MOUTH); C.set(30, 21, MOUTH)
C.set(28, 20, SKINSH); C.set(31, 20, SKINSH)  # nose hint

# ---- neck & shoulders ----
C.rect(29, 24, 5, 4, SKIN)
C.line(29, 27, 33, 27, SKINSH)

# ---- outfit (light green tunic) ----
C.poly([(20,29),(43,29),(46,52),(18,52)], OUTFIT, fill=True)
C.rect(20, 29, 24, 4, OUTFITD)        # collar shade
C.line(31, 29, 31, 52, OUTFITD)       # centre seam
C.line(30, 29, 30, 52, OUTFITDD)
# belt
C.rect(20, 40, 24, 3, LEATHER)
C.rect(29, 40, 4, 3, GOLD)
# tunic shading right side
C.rect(41, 33, 4, 8, OUTFITD)
# skirt flare darker hem
C.rect(18, 50, 28, 2, OUTFITD)

# ---- arms ----
# left arm down along body
C.rect(18, 30, 4, 12, OUTFIT)
C.rect(18, 41, 4, 4, SKIN)
# right arm across holding bow low
C.rect(41, 30, 4, 8, OUTFIT)
C.rect(42, 37, 4, 4, SKIN)
C.set(43, 34, OUTFITD)

# ---- quiver on back (visible over right shoulder) ----
C.rect(44, 24, 5, 16, LEATHER)
C.rect(44, 24, 5, 2, LEATHERD)
C.rect(44, 27, 5, 1, LEATHERD)
# arrows sticking up
C.line(45, 24, 45, 17, WOOD)
C.line(47, 24, 47, 15, WOOD)
C.line(49, 24, 49, 17, WOOD)
C.set(45, 16, FEATHER); C.set(45, 15, FEATHER)
C.set(47, 14, FEATHER); C.set(47, 13, FEATHER)
C.set(49, 16, FEATHER); C.set(49, 15, FEATHER)
C.set(46, 17, FEATHER)
C.set(48, 15, FEATHER)

# ---- bow over left shoulder ----
# longbow curve from lower-left up over shoulder to right
C.path("M 14 52 C 8 40, 8 26, 15 16 C 20 10, 27 7, 34 8", WOOD, fill=False)
C.path("M 16 52 C 10 41, 10 27, 16 18", WOODD, fill=False)
# bowstring
C.line(14, 52, 34, 8, "#e8e8e0")
# grip wrap
C.rect(11, 33, 3, 6, LEATHERD)

# ---- front hair strands over shoulders ----
C.rect(22, 12, 4, 20, HAIR)
C.rect(36, 12, 4, 18, HAIR)
C.line(23, 14, 23, 30, HAIRL)
C.line(38, 14, 38, 28, HAIRL)
C.line(25, 30, 25, 34, HAIRD)
C.line(37, 28, 37, 32, HAIRD)

# small leaf clasp in hair
C.set(24, 9, GOLD); C.set(25, 9, GOLD); C.set(24, 8, GOLD)

print(C.stats_text())
finish(C)
