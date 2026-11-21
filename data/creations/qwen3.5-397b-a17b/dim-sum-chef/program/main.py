from pixelbench_api import *

# Create 32x32 canvas for dim sum chef
c = new_canvas(32, 32, name="dim_sum_chef")

# Define color palette - keeping within 86 colors
# Skin tones
skin = c.color("#f0c8a8", "skin")
skin_shadow = c.color("#d0a078", "skin_shadow")

# Hair
hair = c.color("#3a2010", "hair")
hair_highlight = c.color("#5a3520", "hair_highlight")

# Chef hat (white with shadows)
hat_white = c.color("#ffffff", "hat_white")
hat_shadow = c.color("#e8e8e8", "hat_shadow")
hat_dark_shadow = c.color("#c8c8c8", "hat_dark_shadow")

# Face features
eyes = c.color("#2a1a10", "eyes")
mouth = c.color("#c06050", "mouth")
cheeks = c.color("#f8b8a8", "cheeks")

# Clothing - traditional chef outfit (slightly off-white)
shirt = c.color("#f8f8f8", "shirt")
shirt_shadow = c.color("#d0d0d0", "shirt_shadow")
shirt_dark = c.color("#b0b0b0", "shirt_dark")

# Apron (white with flour dusting - distinct from shirt)
apron = c.color("#ffffff", "apron")
apron_shadow = c.color("#c8c8c8", "apron_shadow")
apron_fold = c.color("#a8a8a8", "apron_fold")
flour = c.color("#ffffff", "flour")

# Bamboo steamer colors (warm brown tones)
bamboo_light = c.color("#e8c080", "bamboo_light")
bamboo_mid = c.color("#c89050", "bamboo_mid")
bamboo_dark = c.color("#986030", "bamboo_dark")
bamboo_shadow = c.color("#684020", "bamboo_shadow")

# Steamer buns (creamy white)
bun_white = c.color("#fff8f0", "bun_white")
bun_shadow = c.color("#f0e0c8", "bun_shadow")
bun_fold = c.color("#e0d0b0", "bun_fold")

# Hands (slightly different from face for separation)
hands = c.color("#e8c0a0", "hands")
hands_shadow = c.color("#c89068", "hands_shadow")
hands_dark = c.color("#a87048", "hands_dark")

# Steam
steam = c.color("#e0e0e0", "steam")

# Background - transparent (already transparent)

# === DRAW CHEF HAT (tall traditional puffy hat) ===
# Top puff of hat
c.rect(10, 2, 12, 3, hat_white)
c.rect(9, 4, 14, 2, hat_white)
c.rect(8, 5, 16, 2, hat_white)
# Main hat body (tall cylindrical shape)
c.rect(8, 7, 16, 6, hat_white)
# Hat pleats/folds
c.set(10, 7, hat_shadow)
c.set(10, 8, hat_shadow)
c.set(10, 9, hat_shadow)
c.set(10, 10, hat_shadow)
c.set(14, 7, hat_shadow)
c.set(14, 8, hat_shadow)
c.set(14, 9, hat_shadow)
c.set(14, 10, hat_shadow)
c.set(18, 7, hat_shadow)
c.set(18, 8, hat_shadow)
c.set(18, 9, hat_shadow)
c.set(18, 10, hat_shadow)
# Hat band at bottom
c.rect(8, 12, 16, 2, hat_shadow)
c.rect(8, 13, 16, 1, hat_dark_shadow)
# Top of hat shadow
c.set(9, 5, hat_shadow)
c.set(10, 4, hat_shadow)
c.set(21, 5, hat_shadow)
c.set(21, 6, hat_shadow)

# === DRAW HAIR ===
# Hair peeking from sides of face
c.rect(8, 10, 2, 5, hair)
c.rect(22, 10, 2, 5, hair)
# Hair highlights
c.set(8, 11, hair_highlight)
c.set(8, 12, hair_highlight)
c.set(23, 11, hair_highlight)
c.set(23, 12, hair_highlight)
# Sideburns
c.set(8, 14, hair)
c.set(8, 15, hair)
c.set(23, 14, hair)
c.set(23, 15, hair)

# === DRAW FACE ===
# Main face area
c.rect(10, 10, 12, 11, skin)
# Face shape refinement
c.set(9, 11, skin)
c.set(9, 12, skin)
c.set(9, 13, skin)
c.set(9, 14, skin)
c.set(9, 15, skin)
c.set(9, 16, skin)
c.set(9, 17, skin)
c.set(22, 11, skin)
c.set(22, 12, skin)
c.set(22, 13, skin)
c.set(22, 14, skin)
c.set(22, 15, skin)
c.set(22, 16, skin)
c.set(22, 17, skin)
# Chin
c.rect(11, 20, 10, 2, skin)
c.set(10, 18, skin)
c.set(10, 19, skin)
c.set(21, 18, skin)
c.set(21, 19, skin)
c.set(10, 20, skin)
c.set(21, 20, skin)
# Face shadow under chin
c.set(12, 20, skin_shadow)
c.set(13, 20, skin_shadow)
c.set(18, 20, skin_shadow)
c.set(19, 20, skin_shadow)

# === EYES ===
# Left eye
c.set(12, 14, eyes)
c.set(13, 14, eyes)
c.set(14, 14, eyes)
# Right eye
c.set(17, 14, eyes)
c.set(18, 14, eyes)
c.set(19, 14, eyes)
# Eye highlights
c.set(13, 13, hat_white)
c.set(18, 13, hat_white)

# === EYEBROWS ===
c.set(11, 12, hair)
c.set(12, 12, hair)
c.set(13, 12, hair)
c.set(14, 12, hair)
c.set(17, 12, hair)
c.set(18, 12, hair)
c.set(19, 12, hair)
c.set(20, 12, hair)

# === NOSE ===
c.set(15, 15, skin_shadow)
c.set(16, 15, skin_shadow)
c.set(15, 16, skin_shadow)

# === CHEEKS ===
c.set(10, 16, cheeks)
c.set(11, 16, cheeks)
c.set(10, 17, cheeks)
c.set(20, 16, cheeks)
c.set(21, 16, cheeks)
c.set(21, 17, cheeks)

# === MOUTH (smiling) ===
c.set(14, 18, mouth)
c.set(15, 18, mouth)
c.set(16, 18, mouth)
c.set(17, 18, mouth)
c.set(15, 19, mouth)
c.set(16, 19, mouth)

# === NECK ===
c.rect(13, 20, 6, 2, skin)
c.set(12, 21, skin)
c.set(19, 21, skin)
c.set(13, 21, skin_shadow)
c.set(18, 21, skin_shadow)

# === SHIRT (traditional chef jacket) ===
# Main shirt body visible under apron
c.rect(6, 22, 20, 10, shirt)
# Collar
c.rect(11, 21, 3, 2, shirt)
c.rect(18, 21, 3, 2, shirt)
# Shirt folds/shadows
c.set(7, 23, shirt_shadow)
c.set(7, 24, shirt_shadow)
c.set(7, 25, shirt_shadow)
c.set(24, 23, shirt_shadow)
c.set(24, 24, shirt_shadow)
c.set(24, 25, shirt_shadow)
c.set(14, 23, shirt_shadow)
c.set(14, 24, shirt_shadow)
c.set(17, 23, shirt_shadow)
c.set(17, 24, shirt_shadow)
# Buttons down center
c.set(15, 23, shirt_dark)
c.set(15, 25, shirt_dark)
c.set(15, 27, shirt_dark)
c.set(15, 29, shirt_dark)

# === APRON (flour-dusted, over shirt) ===
# Main apron body - covers center of shirt (pure white to stand out)
c.rect(10, 24, 12, 8, apron)
c.rect(9, 25, 2, 7, apron)
c.rect(21, 25, 2, 7, apron)
# Apron bib (upper part)
c.rect(11, 22, 10, 3, apron)
# Apron straps going up to neck
c.rect(12, 21, 2, 2, apron)
c.rect(18, 21, 2, 2, apron)
# Apron folds/shadows for dimension
c.set(10, 26, apron_shadow)
c.set(10, 27, apron_shadow)
c.set(10, 28, apron_shadow)
c.set(21, 26, apron_shadow)
c.set(21, 27, apron_shadow)
c.set(21, 28, apron_shadow)
c.set(14, 27, apron_fold)
c.set(14, 29, apron_fold)
c.set(17, 27, apron_fold)
c.set(17, 29, apron_fold)
# Flour dusting (scattered white speckles on apron - using flour color)
c.set(11, 25, flour)
c.set(13, 26, flour)
c.set(15, 25, flour)
c.set(17, 26, flour)
c.set(19, 25, flour)
c.set(11, 28, flour)
c.set(13, 29, flour)
c.set(16, 28, flour)
c.set(19, 29, flour)
c.set(12, 30, flour)
c.set(18, 30, flour)

# === HANDS (clearly separated, holding steamer) ===
# Left hand - fingers visible gripping steamer side
c.rect(4, 24, 5, 5, hands)
c.set(4, 25, hands)
c.set(4, 26, hands)
c.set(3, 25, hands)
c.set(3, 26, hands)
# Left thumb
c.set(8, 25, hands)
c.set(8, 26, hands)
# Left hand shadow/fingers detail
c.set(5, 27, hands_shadow)
c.set(6, 27, hands_shadow)
c.set(7, 27, hands_shadow)
c.set(5, 28, hands_dark)
c.set(6, 28, hands_dark)

# Right hand - fingers visible gripping steamer side
c.rect(23, 24, 5, 5, hands)
c.set(27, 25, hands)
c.set(27, 26, hands)
c.set(28, 25, hands)
c.set(28, 26, hands)
# Right thumb
c.set(23, 25, hands)
c.set(23, 26, hands)
# Right hand shadow/fingers detail
c.set(26, 27, hands_shadow)
c.set(25, 27, hands_shadow)
c.set(24, 27, hands_shadow)
c.set(26, 28, hands_dark)
c.set(25, 28, hands_dark)

# === BAMBOO STEAMER (centered, held by hands) ===
# Bottom base of steamer
c.rect(10, 28, 12, 3, bamboo_shadow)
c.rect(9, 29, 14, 2, bamboo_dark)
# Steamer body sides
c.rect(8, 25, 2, 4, bamboo_mid)
c.rect(22, 25, 2, 4, bamboo_mid)
# Top rim of steamer
c.rect(7, 24, 18, 2, bamboo_light)
c.rect(6, 25, 2, 1, bamboo_light)
c.rect(24, 25, 2, 1, bamboo_light)
# Bamboo weave texture
c.set(8, 26, bamboo_dark)
c.set(8, 27, bamboo_dark)
c.set(23, 26, bamboo_dark)
c.set(23, 27, bamboo_dark)
c.set(9, 25, bamboo_mid)
c.set(9, 26, bamboo_mid)
c.set(22, 25, bamboo_mid)
c.set(22, 26, bamboo_mid)
# Handle on top of steamer
c.rect(12, 22, 8, 2, bamboo_dark)
c.rect(13, 21, 6, 1, bamboo_shadow)
# Handle attachment points
c.set(12, 23, bamboo_shadow)
c.set(19, 23, bamboo_shadow)

# === STEAMER BUNS (visible inside steamer) ===
# Buns showing inside - round puffy shapes
c.set(10, 24, bun_white)
c.set(11, 24, bun_white)
c.set(12, 24, bun_white)
c.set(13, 24, bun_white)
c.set(14, 24, bun_white)
c.set(15, 24, bun_white)
c.set(16, 24, bun_white)
c.set(17, 24, bun_white)
c.set(18, 24, bun_white)
c.set(19, 24, bun_white)
c.set(20, 24, bun_white)
c.set(21, 24, bun_white)
# Bun tops (rounded appearance with shadow)
c.set(11, 23, bun_shadow)
c.set(13, 23, bun_shadow)
c.set(15, 23, bun_shadow)
c.set(17, 23, bun_shadow)
c.set(19, 23, bun_shadow)
c.set(21, 23, bun_shadow)
# More bun detail between shadows
c.set(12, 23, bun_white)
c.set(14, 23, bun_white)
c.set(16, 23, bun_white)
c.set(18, 23, bun_white)
c.set(20, 23, bun_white)
# Bun fold lines
c.set(12, 24, bun_fold)
c.set(15, 24, bun_fold)
c.set(18, 24, bun_fold)
# Second row of buns (partial, behind first)
c.set(13, 23, bun_white)
c.set(16, 23, bun_white)
c.set(19, 23, bun_white)

# === STEAM (rising from steamer, subtle) ===
c.set(13, 20, steam)
c.set(14, 19, steam)
c.set(15, 20, steam)
c.set(16, 19, steam)
c.set(17, 20, steam)
c.set(14, 18, steam)
c.set(16, 18, steam)
c.set(15, 17, steam)

print(c.stats_text())
print(c.matrix_text())

finish(c)
