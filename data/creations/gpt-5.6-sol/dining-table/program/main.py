# 64x64 top-down family dining table sprite
result = new_canvas(64, 64, background=None, name="family_dining_table")

# Palette
outline = "#211512"
deep = "#3a2118"
shadow = "#55301f"
wood_dark = "#754326"
wood = "#a86432"
wood_light = "#ca8242"
honey = "#e0a052"
highlight = "#f0bd6a"
cloth_dark = "#8b3c32"
cloth = "#c75a46"
cream_shadow = "#d7c49e"
cream = "#f2e2b9"
cream_hi = "#fff2cf"
bowl_dark = "#6b2920"
bowl = "#b7462f"
leaf = "#3f713b"
leaf_hi = "#69a64d"
red = "#db3d32"
red_hi = "#f06a3f"
yellow = "#f3b62e"
yellow_hi = "#ffd85a"
purple = "#76425e"

# Ground contact shadows (subtle, pixel-stepped)
result.rect(23, 4, 18, 10, deep)
result.rect(23, 50, 18, 10, deep)
result.rect(4, 23, 10, 18, deep)
result.rect(50, 23, 10, 18, deep)
result.rect(13, 13, 40, 40, deep)

# Top chair: back, slats, seat and short join
result.poly([(22,2),(41,2),(43,4),(43,8),(41,10),(22,10),(20,8),(20,4)], outline)
result.rect(23, 4, 17, 4, wood_dark)
result.rect(25, 4, 2, 4, wood_light)
result.rect(30, 4, 3, 4, wood_light)
result.rect(36, 4, 2, 4, wood_light)
result.rect(24, 9, 15, 5, outline)
result.rect(26, 9, 11, 4, wood)
result.rect(28, 10, 7, 2, wood_light)

# Bottom chair
result.poly([(22,54),(41,54),(43,56),(43,60),(41,62),(22,62),(20,60),(20,56)], outline)
result.rect(23, 56, 17, 4, wood_dark)
result.rect(25, 56, 2, 4, wood_light)
result.rect(30, 56, 3, 4, wood_light)
result.rect(36, 56, 2, 4, wood_light)
result.rect(24, 50, 15, 5, outline)
result.rect(26, 51, 11, 4, wood)
result.rect(28, 52, 7, 2, wood_light)

# Left chair
result.poly([(2,22),(8,20),(10,22),(10,41),(8,43),(4,43),(2,41)], outline)
result.rect(4, 23, 4, 17, wood_dark)
result.rect(4, 25, 4, 2, wood_light)
result.rect(4, 30, 4, 3, wood_light)
result.rect(4, 36, 4, 2, wood_light)
result.rect(9, 24, 5, 15, outline)
result.rect(9, 26, 4, 11, wood)
result.rect(10, 28, 2, 7, wood_light)

# Right chair
result.poly([(54,22),(56,20),(60,20),(62,22),(62,41),(60,43),(56,43),(54,41)], outline)
result.rect(56, 23, 4, 17, wood_dark)
result.rect(56, 25, 4, 2, wood_light)
result.rect(56, 30, 4, 3, wood_light)
result.rect(56, 36, 4, 2, wood_light)
result.rect(50, 24, 5, 15, outline)
result.rect(51, 26, 4, 11, wood)
result.rect(52, 28, 2, 7, wood_light)

# Main table silhouette and heavy rim
result.poly([(14,11),(49,11),(52,14),(52,49),(49,52),(14,52),(11,49),(11,14)], outline)
result.poly([(15,13),(48,13),(50,15),(50,48),(48,50),(15,50),(13,48),(13,15)], wood_dark)
result.rect(15, 15, 33, 33, wood)

# Table planks and warm worn highlights
result.rect(16, 16, 31, 2, wood_light)
result.rect(16, 46, 31, 2, shadow)
result.rect(16, 19, 1, 26, honey)
result.rect(30, 18, 1, 28, wood_dark)
result.rect(42, 18, 1, 28, wood_dark)
result.rect(31, 19, 1, 26, wood_light)
result.rect(43, 19, 1, 26, wood_light)
result.rect(19, 22, 8, 1, wood_light)
result.rect(34, 42, 6, 1, honey)
result.rect(18, 44, 7, 1, shadow)
result.set(46, 20, highlight)
result.set(18, 19, highlight)
result.set(46, 44, wood_dark)

# Four red placemats, each oriented toward its chair
result.rect(23, 16, 17, 7, cloth_dark)
result.rect(24, 16, 15, 6, cloth)
result.rect(23, 41, 17, 7, cloth_dark)
result.rect(24, 42, 15, 6, cloth)
result.rect(15, 24, 7, 16, cloth_dark)
result.rect(15, 25, 6, 14, cloth)
result.rect(42, 24, 7, 16, cloth_dark)
result.rect(43, 25, 6, 14, cloth)

# Plates with chunky ceramic rims
result.ellipse(31, 19, 5, 2, cream_shadow)
result.ellipse(31, 19, 4, 2, cream)
result.rect(29, 18, 5, 2, cream_hi)
result.ellipse(31, 44, 5, 2, cream_shadow)
result.ellipse(31, 44, 4, 2, cream)
result.rect(29, 43, 5, 2, cream_hi)
result.ellipse(18, 32, 2, 5, cream_shadow)
result.ellipse(18, 32, 2, 4, cream)
result.rect(17, 30, 2, 5, cream_hi)
result.ellipse(46, 32, 2, 5, cream_shadow)
result.ellipse(46, 32, 2, 4, cream)
result.rect(45, 30, 2, 5, cream_hi)

# Cutlery marks
result.rect(25, 17, 1, 4, cream_hi)
result.rect(37, 17, 1, 4, cream_hi)
result.rect(25, 43, 1, 4, cream_hi)
result.rect(37, 43, 1, 4, cream_hi)
result.rect(16, 26, 4, 1, cream_hi)
result.rect(16, 37, 4, 1, cream_hi)
result.rect(44, 26, 4, 1, cream_hi)
result.rect(44, 37, 4, 1, cream_hi)

# Central fruit bowl: dark outline, red ceramic body
result.ellipse(32, 32, 9, 7, bowl_dark)
result.ellipse(32, 31, 8, 6, bowl)
result.ellipse(32, 29, 7, 4, cream)
result.ellipse(32, 30, 6, 4, honey)

# Fruit pile and leaves
result.poly([(31,27),(33,24),(35,27),(34,29)], leaf)
result.set(32, 25, leaf_hi)
result.circle(28, 29, 2, red)
result.set(27, 28, red_hi)
result.circle(32, 28, 2, yellow)
result.set(31, 27, yellow_hi)
result.circle(36, 29, 2, red)
result.set(35, 28, red_hi)
result.circle(30, 32, 2, purple)
result.set(29, 31, red_hi)
result.circle(34, 32, 2, yellow)
result.set(33, 31, yellow_hi)

# Bowl lip and front shine, restoring the vessel's readable edge
result.line(26, 34, 38, 34, bowl_dark)
result.rect(27, 35, 11, 2, bowl)
result.rect(29, 37, 7, 1, bowl_dark)
result.rect(28, 35, 3, 1, red_hi)
result.set(38, 33, highlight)

# Corner pegs and bright rim nicks
for x, y in [(15,15),(48,15),(15,48),(48,48)]:
    result.set(x, y, honey)
result.set(14, 16, wood_light)
result.set(49, 47, shadow)

view(result, scale=8, margin=0)
finish(result)
