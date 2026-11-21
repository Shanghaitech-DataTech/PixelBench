from pixelbench_api import new_canvas, view, finish

# 32x32 bamboo steamer sprite on transparency.
result = new_canvas(32, 32, background=None, name="bamboo-steamer")

outline = "#4b2b20"
deep = "#693a22"
shadow = "#8f5428"
bamboo_dark = "#b86f32"
bamboo = "#d99545"
bamboo_light = "#f0b95f"
highlight = "#ffd77f"
inside = "#5b3021"
dumpling_shadow = "#d8c99f"
dumpling = "#f3e6bd"
dumpling_hi = "#fff4d2"
steam = "#e9e4d6"

# Small rising wisps.
result.set(11, 1, steam).set(10, 2, steam).set(10, 3, steam).set(11, 4, steam)
result.set(20, 0, steam).set(19, 1, steam).set(19, 2, steam).set(20, 3, steam)
result.set(23, 5, steam).set(24, 4, steam).set(24, 3, steam)

# Raised lid, tilted upward on the left.
result.poly([(5,8),(8,6),(12,5),(20,5),(24,7),(27,10),(27,12),(25,14),(20,15),(13,14),(8,12),(5,10)], outline)
result.poly([(7,8),(10,6),(19,6),(23,7),(26,10),(25,12),(20,13),(13,13),(8,11),(6,9)], bamboo)
result.poly([(9,7),(13,6),(19,7),(23,8),(25,10),(23,10),(19,9),(13,9),(9,10),(7,9)], bamboo_light)
result.line(9,10,20,12,bamboo_dark)
result.line(10,11,19,13,shadow)
result.set(23,11,highlight).set(24,10,highlight)
# Lid knob.
result.rect(13,3,7,2,outline)
result.rect(14,2,5,1,outline)
result.rect(14,3,5,2,bamboo_dark)
result.rect(15,2,3,1,bamboo_light)

# Basket outer silhouette and dark interior.
result.poly([(4,17),(6,15),(11,14),(21,14),(27,16),(29,19),(28,27),(26,29),(7,29),(4,26)], outline)
result.poly([(6,18),(8,16),(13,15),(21,15),(26,17),(27,19),(25,21),(8,21),(6,19)], inside)
# Back rim catches light behind the food.
result.line(7,17,10,15,bamboo_light)
result.line(22,15,26,17,bamboo_light)
result.set(6,18,bamboo).set(27,18,bamboo_dark)

# Left dumpling: rounded body, pinched crown and folds.
result.poly([(7,19),(8,16),(10,15),(10,14),(12,15),(13,16),(14,19),(13,21),(9,21)], outline)
result.poly([(8,19),(9,16),(10,16),(10,15),(11,16),(12,16),(13,19),(12,20),(9,20)], dumpling)
result.set(9,17,dumpling_hi).set(9,18,dumpling_hi)
result.line(11,16,11,19,dumpling_shadow)

# Center dumpling, slightly taller and broad.
result.poly([(12,19),(13,16),(15,15),(15,13),(17,14),(18,13),(19,15),(21,17),(21,20),(19,22),(14,22)], outline)
result.poly([(13,19),(14,16),(16,16),(16,14),(17,15),(18,14),(18,16),(20,17),(20,20),(18,21),(14,21)], dumpling)
result.set(14,17,dumpling_hi).set(14,18,dumpling_hi).set(15,16,dumpling_hi)
result.line(17,15,17,19,dumpling_shadow)
result.set(19,17,dumpling_shadow).set(19,18,dumpling_shadow)

# Right dumpling with a separate peaked profile.
result.poly([(19,20),(20,17),(22,16),(23,14),(24,16),(26,17),(27,20),(26,22),(21,22)], outline)
result.poly([(20,20),(21,18),(23,17),(23,15),(24,17),(25,18),(26,20),(25,21),(21,21)], dumpling)
result.set(21,18,dumpling_hi).set(22,17,dumpling_hi)
result.line(24,17,24,20,dumpling_shadow)

# Thick front rim overlaps the dumpling bases.
result.poly([(4,20),(7,21),(12,22),(22,22),(27,20),(29,21),(28,24),(25,25),(8,25),(4,23)], outline)
result.poly([(6,21),(10,23),(23,23),(27,21),(27,23),(24,24),(9,24),(6,23)], bamboo_light)
result.line(10,22,22,22,highlight)
result.set(7,22,bamboo).set(25,23,bamboo)

# Curved bamboo body with vertical slats.
result.poly([(5,24),(8,25),(25,25),(28,23),(27,27),(25,28),(8,28),(5,26)], bamboo)
result.line(5,24,8,25,bamboo_light)
result.line(8,28,25,28,shadow)
result.rect(8,25,2,3,bamboo_dark)
result.rect(14,25,2,3,bamboo_light)
result.rect(20,25,2,3,bamboo_dark)
result.set(26,25,bamboo_dark).set(26,26,bamboo_dark)
# Base line and tiny feet.
result.rect(7,28,19,2,outline)
result.rect(8,28,17,1,bamboo_dark)
result.rect(8,30,4,1,deep)
result.rect(22,30,4,1,deep)

view(result, scale=16, margin=0)
finish(result)
