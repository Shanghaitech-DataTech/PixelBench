from pixelbench_api import new_canvas, view, finish

# 32x32 bamboo steamer sprite on transparency.
c = new_canvas(32, 32, background=None, name="bamboo-steamer")

outline = "#4a2a1b"
deep = "#6b3b20"
shadow = "#8b542b"
bamboo_dark = "#a96834"
bamboo = "#d28a45"
bamboo_light = "#efb963"
highlight = "#ffd584"
inside = "#5a3222"
food_shadow = "#d8cfb7"
food = "#f4eed9"
food_hi = "#fff9e9"
steam = "#d7e5df"
steam_hi = "#f2faf5"

# Small rising curls of steam.
c.set(12, 2, steam)
c.set(11, 3, steam)
c.set(11, 4, steam)
c.set(12, 5, steam_hi)
c.set(13, 5, steam)
c.set(14, 4, steam)
c.set(14, 3, steam)
c.set(20, 1, steam)
c.set(19, 2, steam_hi)
c.set(19, 3, steam)
c.set(20, 4, steam)
c.set(21, 4, steam)
c.set(22, 3, steam)

# Lid propped open behind the basket: a slanted, shallow bamboo dome.
c.poly([(5,12),(6,9),(9,7),(18,6),(24,8),(27,11),(26,14),(22,15),(10,15),(6,14)], outline)
c.poly([(7,12),(8,9),(11,8),(18,7),(23,9),(25,11),(24,13),(20,14),(10,14),(7,13)], bamboo)
c.poly([(9,10),(12,8),(19,8),(23,10),(24,11),(22,11),(20,10),(12,10),(9,12)], bamboo_light)
c.line(8, 12, 23, 12, bamboo_dark)
c.line(10, 13, 21, 13, shadow)
c.set(8, 11, highlight)
c.set(9, 10, highlight)
c.set(22, 9, bamboo_dark)
# Lid handle.
c.rect(14, 5, 6, 2, outline)
c.rect(15, 4, 4, 2, outline)
c.rect(16, 4, 2, 2, bamboo_light)
c.rect(15, 6, 4, 1, bamboo_dark)

# Back rim and dark interior of the open steamer.
c.poly([(3,16),(5,14),(9,13),(23,13),(28,15),(29,18),(27,20),(5,20),(2,18)], outline)
c.poly([(5,16),(8,14),(23,14),(27,16),(27,18),(24,19),(7,19),(4,18)], inside)
c.line(7, 15, 24, 15, shadow)

# Three dumplings, each with a distinct pleated crown.
# Left dumpling.
c.poly([(5,19),(6,17),(7,16),(8,17),(9,15),(10,17),(11,16),(12,18),(12,21),(10,22),(7,22),(5,21)], outline)
c.poly([(6,19),(7,17),(8,18),(9,16),(10,18),(11,17),(11,20),(10,21),(7,21),(6,20)], food)
c.set(7,18,food_hi); c.set(8,19,food_hi); c.set(10,19,food_shadow)
# Center dumpling, slightly taller.
c.poly([(11,19),(12,16),(13,15),(14,16),(15,14),(16,16),(17,15),(18,17),(19,18),(19,21),(17,22),(13,22),(11,21)], outline)
c.poly([(12,19),(13,17),(14,17),(15,15),(16,17),(17,16),(18,18),(18,20),(17,21),(13,21),(12,20)], food)
c.set(13,18,food_hi); c.set(14,17,food_hi); c.set(17,19,food_shadow)
# Right dumpling.
c.poly([(19,19),(20,17),(21,16),(22,17),(23,15),(24,17),(25,17),(27,19),(27,21),(25,22),(21,22),(19,21)], outline)
c.poly([(20,19),(21,17),(22,18),(23,16),(24,18),(25,18),(26,19),(26,20),(25,21),(21,21),(20,20)], food)
c.set(21,18,food_hi); c.set(22,19,food_hi); c.set(25,19,food_shadow)

# Front rim overlaps the dumpling bases.
c.poly([(2,19),(4,18),(6,20),(26,20),(29,18),(30,20),(29,23),(27,24),(5,24),(3,23)], outline)
c.poly([(4,20),(6,21),(26,21),(28,20),(28,22),(26,23),(6,23),(4,22)], bamboo_light)
c.line(6, 22, 26, 22, bamboo)
c.set(5,20,highlight); c.set(27,21,bamboo_dark)

# Cylindrical woven basket body.
c.poly([(3,23),(5,22),(27,22),(29,23),(28,28),(26,30),(6,30),(4,28)], outline)
c.poly([(5,23),(7,24),(25,24),(27,23),(27,28),(25,29),(7,29),(5,28)], bamboo)
c.rect(6,24,20,2,bamboo_light)
c.rect(6,27,20,2,bamboo_dark)
c.line(7,26,25,26,highlight)
# Vertical slats and basket shading.
c.rect(7,24,2,5,bamboo_dark)
c.rect(9,24,1,5,bamboo_light)
c.rect(12,24,1,5,shadow)
c.rect(15,24,2,5,bamboo_dark)
c.rect(18,24,1,5,bamboo_light)
c.rect(21,24,1,5,shadow)
c.rect(24,24,2,5,bamboo_dark)
c.set(6,24,highlight); c.set(10,25,highlight); c.set(19,25,highlight)
# Strong lower binding band.
c.rect(5,28,22,2,outline)
c.rect(7,28,18,1,bamboo_light)
c.set(5,27,bamboo_dark); c.set(26,27,shadow)

view(c, scale=16, margin=0)
finish(c)
