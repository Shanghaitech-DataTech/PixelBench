# 16x16 female lab researcher chibi sprite
result = new_canvas(16, 16, background=None, name="female-lab-researcher-chibi")

# Palette
outline = "#17151d"
hair = "#24212a"
hair_hi = "#423b48"
skin = "#e8a876"
skin_hi = "#ffc08b"
skin_sh = "#bd7658"
eye = "#6b3d24"
white = "#f5f3e9"
coat_sh = "#b9cbd0"
coat_deep = "#718b96"
shirt = "#6fb5ad"
cyan = "#62dbe0"
glass_hi = "#d5ffff"
shoe = "#342b38"

# Hair mass and head outline
result.rect(5, 0, 6, 1, outline)
result.rect(4, 1, 8, 2, outline)
result.rect(3, 3, 10, 4, outline)
result.rect(4, 7, 8, 2, outline)
result.rect(4, 1, 7, 2, hair)
result.rect(3, 3, 2, 4, hair)
result.rect(11, 3, 2, 4, hair)
result.set(5, 1, hair_hi)
result.set(6, 1, hair_hi)
result.set(4, 2, hair_hi)
result.set(4, 3, hair_hi)

# Face
result.rect(5, 3, 6, 4, skin)
result.rect(6, 7, 4, 1, skin_sh)
result.set(5, 4, skin_hi)
result.set(10, 4, skin_hi)
# Hair fringe
result.set(5, 3, hair)
result.set(6, 3, hair)
result.set(7, 3, hair)
result.set(8, 3, hair)
result.set(9, 3, hair)
result.set(10, 3, hair)
result.set(5, 4, hair)
result.set(8, 4, hair)
result.set(10, 4, hair)
# Eyes, brows, tiny smile
result.set(6, 4, outline)
result.set(9, 4, outline)
result.set(6, 5, eye)
result.set(9, 5, eye)
result.set(7, 6, skin_sh)
result.set(8, 6, skin_sh)
result.set(5, 6, skin_hi)

# Feet behind coat
result.rect(5, 13, 2, 2, outline)
result.rect(9, 13, 2, 2, outline)
result.set(5, 14, shoe)
result.set(6, 14, shoe)
result.set(9, 14, shoe)
result.set(10, 14, shoe)

# Body / lab coat silhouette
result.rect(5, 8, 6, 1, outline)
result.rect(4, 9, 8, 5, outline)
result.set(3, 10, outline)
result.set(3, 11, outline)
result.set(12, 10, outline)
result.set(12, 11, outline)
# White coat and sleeves
result.set(5, 8, white)
result.set(6, 8, white)
result.set(9, 8, white)
result.set(10, 8, white)
result.rect(5, 9, 6, 4, white)
result.set(4, 9, white)
result.set(4, 10, white)
result.set(3, 11, white)
result.set(11, 9, coat_sh)
result.set(11, 10, white)
result.set(12, 11, white)
# Shirt visible at open collar
result.set(7, 8, skin_sh)
result.set(8, 8, skin_sh)
result.set(7, 9, shirt)
result.set(8, 9, shirt)
# Coat lapels, seam, shadows, pockets
result.set(6, 9, coat_sh)
result.set(9, 9, coat_sh)
result.set(7, 10, coat_sh)
result.set(8, 10, coat_sh)
result.set(8, 11, coat_deep)
result.set(8, 12, coat_deep)
result.set(5, 12, coat_sh)
result.set(10, 12, coat_sh)
result.set(6, 13, coat_deep)
result.set(9, 13, coat_deep)
# Hands
result.set(3, 12, skin)
result.set(12, 12, skin)
# Test tube held at right
result.set(13, 10, outline)
result.set(14, 10, outline)
result.set(13, 11, glass_hi)
result.set(13, 12, cyan)
result.set(14, 11, cyan)
result.set(14, 12, outline)
result.set(13, 13, outline)

view(result, scale=32, margin=1, edges="all")
finish(result)
