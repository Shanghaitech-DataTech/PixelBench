# Dim sum chef, 32x32 front-facing character sprite
result = new_canvas(32, 32, background=None, name="dim-sum-chef")

# Palette
outline = "#2b1d24"
hair = "#3b2526"
hair_hi = "#5a3430"
skin_dark = "#b9694e"
skin = "#e79a70"
skin_hi = "#ffc094"
white_sh = "#b9c3c3"
white = "#eef0df"
white_hi = "#fff9df"
red_dark = "#8c3031"
red = "#c84b3f"
red_hi = "#ef6850"
bamboo_dark = "#765025"
bamboo = "#b47b35"
bamboo_hi = "#dcad58"
bun_sh = "#d9d7bd"
bun = "#fff1ce"
flour = "#ffffff"

# Chef toque: outlined, symmetric stepped silhouette
result.rect(10, 2, 12, 1, outline)
result.rect(7, 4, 18, 7, outline)
result.rect(9, 3, 4, 1, outline)
result.rect(14, 2, 4, 1, outline)
result.rect(19, 3, 4, 1, outline)
result.set(6, 6, outline); result.set(25, 6, outline)
result.rect(8, 4, 16, 6, white)
result.rect(10, 3, 3, 1, white_hi)
result.rect(14, 3, 4, 1, white_hi)
result.rect(19, 4, 4, 1, white_hi)
result.rect(7, 6, 2, 3, white)
result.rect(23, 6, 2, 3, white)
result.rect(9, 8, 14, 2, white_sh)
result.rect(10, 8, 12, 1, white)

# Head and ears
result.rect(8, 10, 16, 8, outline)
result.rect(7, 12, 2, 5, outline); result.rect(23, 12, 2, 5, outline)
result.rect(8, 11, 16, 6, skin)
result.rect(7, 13, 2, 3, skin_dark); result.rect(23, 13, 2, 3, skin_dark)
result.set(8, 12, skin_hi); result.set(9, 11, skin_hi)
# Hair under hat and side locks
result.rect(9, 10, 14, 2, hair)
result.rect(8, 11, 2, 3, hair)
result.rect(22, 11, 2, 3, hair)
result.set(10, 11, hair_hi); result.set(21, 11, hair_hi)
# Face
result.rect(11, 13, 2, 1, outline); result.rect(19, 13, 2, 1, outline)
result.set(12, 13, "#4b2d2b"); result.set(19, 13, "#4b2d2b")
result.set(15, 14, skin_dark); result.set(16, 14, skin_hi)
result.rect(14, 16, 4, 1, outline)
result.rect(15, 16, 2, 1, "#f4b0a0")

# Torso / jacket silhouette
result.rect(6, 18, 20, 11, outline)
result.rect(4, 20, 3, 7, outline); result.rect(25, 20, 3, 7, outline)
result.rect(7, 18, 18, 10, white)
result.rect(5, 21, 2, 5, red); result.rect(25, 21, 2, 5, red)
result.set(5, 21, red_hi); result.set(26, 21, red_hi)
# Collar / neckerchief
result.poly([(10,18),(15,18),(14,22)], red_dark)
result.poly([(17,18),(22,18),(18,22)], red_dark)
result.rect(14, 18, 4, 2, red)
result.set(15, 20, red_hi); result.set(16, 20, red_hi)

# Apron, clearly separated by shadowed edge
apron = "#d5ddda"
result.poly([(9,20),(23,20),(25,31),(7,31)], outline)
result.poly([(10,21),(22,21),(24,31),(8,31)], white_sh)
result.poly([(11,21),(21,21),(22,31),(9,31)], apron)
# Flour dust on the exposed bib and lower apron
for x,y in [(11,21),(13,22),(18,21),(20,22),(12,29),(17,29)]:
    result.set(x,y,flour)
result.set(15,21,white_hi); result.set(19,22,white_hi)

# Forearms and hands behind steamer, separated from clothing
result.rect(4, 23, 5, 4, outline); result.rect(23, 23, 5, 4, outline)
result.rect(5, 23, 4, 3, skin_dark); result.rect(23, 23, 4, 3, skin_dark)
result.rect(6, 23, 3, 2, skin); result.rect(23, 23, 3, 2, skin)
result.set(7,23,skin_hi); result.set(24,23,skin_hi)

# Bamboo steamer in foreground
result.rect(7, 22, 18, 8, outline)
result.rect(8, 22, 16, 2, bamboo_hi)
result.set(8,22,bamboo); result.set(23,22,bamboo)
# Three buns with dark separation
result.rect(9, 20, 4, 3, outline); result.rect(14, 19, 4, 4, outline); result.rect(19, 20, 4, 3, outline)
result.rect(10, 20, 2, 2, bun); result.rect(15, 19, 2, 3, bun); result.rect(20, 20, 2, 2, bun)
result.set(11,20,bun_sh); result.set(16,19,bun_sh); result.set(21,20,bun_sh)
result.set(10,20,white_hi); result.set(15,19,white_hi); result.set(20,20,white_hi)
# Steamer basket bands and weave
result.rect(8, 24, 16, 5, bamboo)
result.rect(8, 24, 16, 1, bamboo_hi)
result.rect(8, 28, 16, 2, bamboo_dark)
result.rect(9, 28, 14, 1, bamboo_hi)
for x in (10,14,18,22):
    result.rect(x,25,1,3,bamboo_dark)
for x in (11,15,19):
    result.set(x,26,bamboo_hi)
result.set(8,29,outline); result.set(23,29,outline)

# Feet below apron
result.rect(8, 31, 6, 1, outline); result.rect(18, 31, 6, 1, outline)

view(result, scale=16, margin=1, edges="all")
finish(result)
