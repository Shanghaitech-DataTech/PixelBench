# Two-frame paladin heavy attack animation.
W, H = 72, 72
f1 = new_canvas(W, H, background=None, name="paladin_ready")
f2 = new_canvas(W, H, background=None, name="paladin_heavy_attack")
OX, OY = 14, 5
f1.blit(input_canvas, OX, OY)
f2.blit(input_canvas, OX, OY)

# Palette aliases from the source sprite.
ink = "#101010"
near_black = "#2c2623"
dark = "#332d32"
steel_dark = "#5a565a"
steel_mid = "#858086"
steel = "#a9a5ab"
steel_light = "#dccaca"
white = "#ffffff"
warm_white = "#ffffd5"
gold_dark = "#804018"
gold = "#c67b02"
gold_hi = "#ffcc43"
gold_pale = "#ffe38c"
wood_dark = "#422110"
wood = "#734a29"
magenta_dark = "#55002a"
magenta = "#9e005d"
magenta_hi = "#ef5ba1"

# Remove the old raised polearm: head above the helmet, diagonal haft, and old hand.
f2.poly([(31,5),(41,5),(45,11),(42,18),(35,17),(29,12)], None)
f2.poly([(40,12),(47,12),(59,25),(57,31),(51,29),(42,20)], None)
f2.poly([(53,23),(66,23),(66,31),(58,31)], None)
# Clean stray pixels around the former weapon without disturbing the plume/body.
f2.rect(58,27,8,5,None)
f2.rect(55,20,5,4,None)

# White motion trail, placed behind the new weapon and arm.
f2.path("M 58 12 C 66 19 70 29 69 39 C 68 47 64 54 59 59 L 56 54 C 61 47 63 40 62 33 C 62 25 59 20 54 16 Z", white)
f2.path("M 55 16 C 61 22 64 29 64 37 C 64 43 62 48 59 52 L 57 48 C 59 42 59 35 58 29 C 58 23 56 20 52 18 Z", warm_white)
# Broken speed streaks make the trail read as motion rather than a static shape.
f2.poly([(65,16),(69,19),(70,24),(68,23)], white)
f2.poly([(68,43),(67,49),(63,55),(64,50)], white)
f2.rect(61,18,2,2,steel_light)
f2.rect(64,27,2,4,steel_light)
f2.rect(62,45,2,3,steel_light)

# The old weapon head occupied this area; erase its remaining isolated pixels.
f2.clear(31, 5, 15, 12)

# Pull the striking shoulder forward and extend the gauntleted arm down-right.
f2.poly([(38,25),(44,24),(49,28),(49,34),(45,37),(40,34)], ink)
f2.poly([(40,26),(44,26),(47,29),(46,33),(43,34),(40,32)], steel_dark)
f2.rect(42,27,4,3,steel_mid)
f2.rect(44,29,3,2,steel_light)
f2.poly([(45,32),(50,34),(53,40),(50,43),(46,38)], ink)
f2.poly([(47,33),(50,35),(52,39),(49,40),(47,37)], steel_mid)
f2.set(48,34,steel_light).set(50,38,steel_light)
# Gripping hand at the haft.
f2.poly([(49,39),(54,40),(55,44),(52,47),(48,44)], ink)
f2.rect(50,40,3,5,gold_dark)
f2.rect(51,40,3,3,gold_hi)
f2.set(52,41,gold_pale)

# Heavy weapon now points down-right. Dark outline first, then wood and metal.
f2.line(50,39,62,58,ink)
f2.line(51,39,63,58,ink)
f2.line(52,39,64,58,ink)
f2.line(52,40,63,57,wood)
f2.line(53,41,64,57,gold_dark)
f2.set(55,44,gold_pale).set(59,50,gold_pale)
# Hammer/axe head at the end of the downswing.
f2.poly([(58,55),(64,52),(69,56),(69,63),(65,67),(59,64),(55,60)], ink)
f2.poly([(59,56),(64,54),(67,57),(67,62),(64,65),(59,62),(57,59)], steel_dark)
f2.poly([(61,55),(65,55),(67,58),(65,61),(60,60),(58,58)], steel_mid)
f2.poly([(62,55),(65,56),(66,58),(63,58),(60,57)], steel_light)
f2.rect(65,59,3,3,near_black)
f2.set(61,56,white).set(59,58,steel_light)
# Tiny impact chips at the lowest point.
f2.rect(67,66,3,2,white)
f2.rect(63,68,2,2,warm_white)
f2.set(70,64,white)

# Change the footing. Clear both original feet/ground shadow, retaining the upper legs.
f2.poly([(19,49),(50,49),(53,66),(47,71),(20,71),(15,65)], None)
# Back leg (screen-left) stays bent and braced.
f2.poly([(27,47),(35,47),(36,54),(32,60),(25,60),(22,57),(23,52)], ink)
f2.poly([(27,48),(33,49),(33,53),(30,57),(25,57),(24,54)], steel_dark)
f2.rect(27,49,5,3,steel_mid)
f2.rect(24,57,10,4,ink)
f2.rect(26,57,8,2,steel)
f2.rect(27,59,8,2,gold)
f2.rect(30,59,5,2,gold_hi)
# Character's left leg (screen-right) steps forward and bears the weight.
f2.poly([(38,46),(46,46),(49,53),(52,59),(59,63),(59,68),(51,70),(43,66),(40,57),(36,52)], ink)
f2.poly([(39,48),(44,48),(47,53),(49,59),(45,62),(42,57),(41,53),(37,51)], steel_dark)
f2.poly([(42,48),(45,50),(47,55),(48,59),(45,60),(43,55)], steel_mid)
f2.rect(43,49,3,3,steel_light)
f2.poly([(47,59),(53,61),(58,64),(57,67),(51,68),(45,64)], steel_dark)
f2.poly([(50,61),(55,63),(57,65),(53,66),(48,64)], steel_mid)
f2.rect(52,63,4,2,steel_light)
# Gold knee and ankle accents tie the new legs into the original armor.
f2.poly([(39,48),(46,48),(48,52),(45,55),(40,54),(38,51)], ink)
f2.rect(40,49,6,4,gold)
f2.rect(42,49,4,2,gold_hi)
f2.rect(45,62,4,3,gold_dark)
f2.set(46,62,gold_hi).set(47,62,gold_pale)

# Restore layered waist armor and the split tabard over the new leg pose.
f2.rect(29,47,16,3,ink)
f2.rect(31,47,12,2,gold_dark)
f2.rect(34,47,7,2,gold_hi)
f2.poly([(32,49),(38,49),(38,58),(35,62),(31,59)], ink)
f2.poly([(33,50),(37,50),(37,57),(35,59),(33,57)], magenta_dark)
f2.rect(34,50,3,4,magenta)
f2.set(35,50,magenta_hi)
# Plate divisions and highlights keep the limbs consistent with the source sprite.
f2.line(25,53,32,53,near_black)
f2.line(24,56,30,56,near_black)
f2.set(27,50,steel_light).set(25,54,steel).set(29,57,white)
f2.line(43,55,48,57,near_black)
f2.line(46,60,53,63,near_black)
f2.set(44,53,steel_light).set(47,58,steel).set(52,64,white)
f2.rect(24,61,11,2,ink)
f2.rect(26,61,8,2,gold_dark)
f2.rect(28,61,6,2,gold_hi)
# Reassert boot silhouettes after the plate detailing.
f2.rect(21,58,4,3,ink)
f2.rect(57,64,3,4,ink)

# A few dust pixels emphasize the planted forward step.
f2.rect(56,69,5,2,"#17003599")
f2.rect(49,70,4,1,"#17003599")

view(f1, scale=7, margin=1, edges="all")
view(f2, scale=7, margin=1, edges="all")
finish([f1, f2])
