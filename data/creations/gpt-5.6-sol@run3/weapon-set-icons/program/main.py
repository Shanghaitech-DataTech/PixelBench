# 64x64 pixel-art weapon icon set
result = new_canvas(64, 64, background=None, name="weapon-set-icons")

# Shared compact palette
outline = result.color("#171923", "outline")
deep = result.color("#292d3a", "deep")
steel_dark = result.color("#687282", "steel_dark")
steel = result.color("#aeb8c5", "steel")
steel_light = result.color("#e4edf2", "steel_light")
wood_dark = result.color("#5b3028", "wood_dark")
wood = result.color("#9b5637", "wood")
wood_light = result.color("#d38a4b", "wood_light")
gold_dark = result.color("#9a5b25", "gold_dark")
gold = result.color("#e6a83c", "gold")
gold_light = result.color("#ffd76a", "gold_light")
blue_dark = result.color("#244b70", "blue_dark")
blue = result.color("#3e79a6", "blue")
blue_light = result.color("#68b3d1", "blue_light")
red = result.color("#a9433d", "red")

# --- Sword, upper-left: raised diagonal blade ---
# Outer silhouette
result.poly([(4,25),(7,28),(13,22),(16,25),(18,23),(15,20),(26,9),(28,3),(22,5),(11,16),(8,13),(6,15),(9,18)], outline)
# Blade body
result.poly([(11,18),(23,6),(26,5),(25,8),(13,20)], steel)
result.poly([(12,18),(23,7),(24,7),(13,19)], steel_light)
result.line(14,19,25,8,steel_dark)
# Crossguard
result.poly([(7,13),(9,12),(18,21),(18,24),(16,25)], gold_dark)
result.poly([(8,14),(9,13),(17,21),(17,23)], gold)
result.set(9,14,gold_light)
# Grip and pommel
result.poly([(7,18),(10,21),(7,25),(5,23)], outline)
result.poly([(8,19),(9,21),(7,23),(6,22)], wood)
result.set(8,20,wood_light)
result.rect(3,24,4,4,outline)
result.rect(4,24,2,2,gold)
result.set(4,24,gold_light)
# Blade glint
result.set(23,6,steel_light); result.set(22,7,steel_light)

# --- Bow and arrow, upper-right ---
# Bow dark silhouette, stepped recurved arc
bow_outline = [(39,4),(42,4),(45,6),(48,9),(50,13),(51,17),(50,22),(47,27),(43,29),(40,29),(39,27),(42,26),(45,23),(47,19),(47,15),(46,11),(43,8),(40,7)]
result.poly(bow_outline, outline)
# Wood interior, deliberately stepped
bow_inner = [(41,5),(44,7),(47,10),(49,14),(49,19),(46,24),(43,27),(41,27),(44,24),(46,20),(46,14),(44,10),(41,7)]
result.poly(bow_inner, wood)
result.line(42,6,45,10,wood_light)
result.line(48,13,48,19,wood_light)
result.line(45,23,42,26,wood_light)
# String
result.line(40,6,40,27,steel_light)
result.set(41,16,steel_light)
# Arrow across bow
result.rect(35,15,21,3,outline)
result.rect(36,16,19,1,steel_light)
result.poly([(55,13),(61,16),(55,19)], outline)
result.poly([(55,15),(59,16),(55,17)], steel)
# Fletching
result.poly([(36,15),(32,12),(34,16),(32,20),(36,17)], outline)
result.poly([(35,15),(33,14),(34,16),(33,18),(35,17)], red)
# Binding
result.rect(47,14,3,5,outline)
result.rect(48,15,1,3,gold)

# --- Shield, lower-left ---
# Strong heraldic silhouette
result.poly([(15,34),(27,38),(27,48),(24,55),(16,61),(8,55),(5,48),(5,38)], outline)
# Gold rim
result.poly([(15,36),(25,39),(25,48),(22,54),(16,58),(10,54),(7,48),(7,39)], gold)
# Inner blue field
result.poly([(15,39),(22,41),(22,48),(20,52),(16,55),(12,52),(10,48),(10,41)], blue_dark)
result.poly([(15,40),(20,42),(20,49),(16,53),(13,51),(12,47),(12,42)], blue)
# Center boss and cross motif
result.rect(14,40,4,14,outline)
result.rect(15,41,2,12,gold)
result.rect(10,45,12,4,outline)
result.rect(11,46,10,2,gold)
result.rect(14,45,4,4,gold_light)
result.set(12,42,blue_light); result.set(13,42,blue_light)
# Rim shine and lower shadow
result.line(9,40,14,38,gold_light)
result.line(8,41,8,47,gold_light)
result.line(11,54,16,57,gold_dark)
result.line(17,57,22,53,gold_dark)
# Rivets
for x,y in [(9,40),(21,40),(9,49),(22,49)]:
    result.set(x,y,gold_light)

# --- Battle axe, lower-right: diagonal haft, broad steel head ---
# Handle outline from lower-left to upper-right
result.poly([(34,58),(37,61),(54,42),(51,39)], outline)
result.poly([(36,58),(37,59),(53,41),(52,40)], wood)
result.line(38,56,51,42,wood_light)
# Pommel
result.poly([(33,57),(38,60),(37,63),(32,61)], outline)
result.poly([(34,58),(37,60),(36,61),(33,60)], gold)
# Axe head outer silhouette
result.poly([(45,37),(51,33),(57,33),(62,36),(59,42),(55,47),(50,47),(46,44),(49,40)], outline)
# Steel blade
result.poly([(52,35),(57,35),(60,37),(57,41),(54,44),(51,45),(48,43),(51,40)], steel_dark)
result.poly([(54,35),(57,36),(58,37),(56,40),(53,43),(50,43),(53,40)], steel)
result.poly([(57,36),(59,37),(56,41),(53,43),(53,41)], steel_light)
# Rear spike
result.poly([(49,36),(43,35),(39,37),(45,39),(50,40)], outline)
result.poly([(48,37),(44,36),(41,37),(45,38),(49,39)], steel)
result.line(43,36,47,37,steel_light)
# Head collar and gold binding
result.poly([(48,39),(52,43),(49,47),(45,43)], outline)
result.poly([(49,40),(51,43),(49,45),(47,43)], gold_dark)
result.set(49,41,gold); result.set(48,42,gold_light)
# Handle wraps
result.line(42,50,45,53,outline)
result.line(44,48,47,51,outline)
result.set(44,51,gold); result.set(46,49,gold)

finish(result)
view(result, scale=8, margin=0)
