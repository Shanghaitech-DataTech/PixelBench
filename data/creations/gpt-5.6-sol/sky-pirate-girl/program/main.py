# 64x64 anime-style sky pirate portrait
c = new_canvas(64, 64, background=None, name="sky-pirate-girl")

# Compact palette
outline = c.color("#171827", "outline")
deep = c.color("#25223b", "deep")
navy = c.color("#263b59", "navy")
navy_hi = c.color("#3d5a73", "navy_hi")
navy_light = c.color("#57758a", "navy_light")
cream = c.color("#f5ddbd", "cream")
skin = c.color("#e8ad83", "skin")
skin_shadow = c.color("#bd765f", "skin_shadow")
blush = c.color("#d98278", "blush")
hair_dark = c.color("#5a302f", "hair_dark")
hair = c.color("#9b5542", "hair")
hair_hi = c.color("#d28257", "hair_hi")
red_dark = c.color("#741f32", "red_dark")
red = c.color("#c33a3f", "red")
red_hi = c.color("#ee6250", "red_hi")
gold_dark = c.color("#8c5529", "gold_dark")
gold = c.color("#d69a3e", "gold")
gold_hi = c.color("#f2cb63", "gold_hi")

# Back hair: wind-swept mass and flying locks
c.poly([(12,13),(18,8),(28,6),(38,8),(45,14),(48,23),(45,34),(39,41),(25,43),(15,35),(10,25)], outline)
c.poly([(10,17),(4,15),(9,20),(2,22),(11,24)], outline)
c.poly([(13,25),(5,29),(12,30),(4,35),(16,33)], outline)
c.poly([(15,33),(8,40),(18,37)], outline)
c.poly([(15,14),(8,13),(13,18),(5,19),(14,22)], hair_dark)
c.poly([(14,26),(7,29),(15,30),(8,34),(19,32)], hair)
c.poly([(17,11),(26,8),(36,10),(43,16),(45,25),(40,34),(34,39),(22,39),(15,33),(12,24)], hair_dark)
c.poly([(18,12),(27,9),(36,11),(42,17),(43,24),(38,20),(34,14),(25,13),(18,18)], hair)
c.poly([(13,34),(7,40),(18,37),(24,34)], hair_dark)
c.poly([(13,18),(7,16),(13,21)], hair_hi)
c.poly([(12,29),(7,30),(14,32)], hair_hi)

# Neck and ear behind face
c.poly([(29,34),(39,34),(41,45),(29,47),(25,42)], outline)
c.poly([(30,33),(38,34),(38,43),(30,44),(27,40)], skin_shadow)
c.poly([(39,23),(45,23),(46,30),(43,34),(39,32)], outline)
c.poly([(40,24),(44,25),(44,30),(42,32),(40,30)], skin)
c.set(42,28,skin_shadow); c.set(43,27,skin_shadow)

# Face, three-quarter view
c.poly([(20,15),(28,12),(37,14),(41,19),(42,28),(38,35),(33,39),(26,37),(20,32),(17,24)], outline)
c.poly([(21,16),(28,13),(36,15),(40,19),(40,28),(37,34),(32,37),(26,35),(21,31),(19,24)], skin)
# face shadow and cheek plane
c.poly([(19,24),(22,27),(24,35),(29,37),(25,35),(20,31)], skin_shadow)
c.poly([(35,31),(39,28),(37,34),(32,37),(29,36)], skin_shadow)
c.rect(34,30,4,2,blush)
c.set(33,30,blush)
# nose
c.line(32,23,31,28,skin_shadow); c.line(31,28,34,29,skin_shadow)
c.set(33,27,cream)
# eyes and brows
c.line(22,21,28,20,hair_dark); c.line(34,20,39,21,hair_dark)
c.poly([(22,23),(25,21),(29,23),(26,26),(23,25)], outline)
c.poly([(23,23),(25,22),(27,23),(26,24),(24,24)], cream)
c.set(26,23,navy_light); c.set(26,24,outline)
c.poly([(34,23),(36,21),(40,23),(38,25),(35,25)], outline)
c.poly([(35,23),(37,22),(39,23),(38,24),(36,24)], cream)
c.set(37,23,navy_light); c.set(38,23,outline)
# confident smile
c.line(30,32,34,33,red_dark); c.line(34,33,37,31,red_dark)
c.set(34,32,cream); c.set(35,32,cream)

# Front fringe over forehead
c.poly([(16,17),(19,11),(28,8),(37,10),(40,14),(35,13),(32,19),(29,14),(25,20),(23,14),(19,23)], outline)
c.poly([(18,17),(20,12),(28,9),(35,11),(38,13),(34,12),(31,17),(29,12),(25,18),(23,12),(20,21)], hair)
c.poly([(21,13),(27,10),(30,11),(24,14)], hair_hi)
c.poly([(32,11),(36,12),(33,14)], hair_hi)

# Goggles perched on head: strap, lenses, bridge
c.line(17,13,39,10,outline); c.line(17,14,39,11,gold_dark)
c.poly([(18,9),(25,7),(29,9),(28,14),(24,17),(19,15),(17,12)], outline)
c.poly([(19,10),(24,8),(27,10),(26,13),(23,15),(20,14),(19,12)], gold)
c.poly([(21,10),(24,9),(26,10),(25,13),(22,14),(20,12)], navy_light)
c.set(21,10,cream); c.set(22,10,cream)
c.poly([(29,8),(36,7),(40,10),(39,14),(34,16),(30,14),(28,11)], outline)
c.poly([(30,9),(35,8),(38,10),(38,13),(34,15),(31,13),(30,11)], gold)
c.poly([(32,9),(35,9),(37,10),(37,12),(34,14),(32,13)], navy_light)
c.set(32,9,cream); c.set(33,9,cream)
c.rect(27,10,3,2,gold_dark)

# Wind-whipped right-side hair tails
c.poly([(39,13),(47,10),(44,15),(54,13),(46,19),(57,20),(44,23)], outline)
c.poly([(40,14),(47,12),(44,16),(52,15),(45,19),(54,20),(43,21)], hair)
c.poly([(44,15),(48,14),(45,17)], hair_hi)
c.poly([(41,31),(50,28),(46,33),(55,33),(46,37),(52,41),(39,37)], outline)
c.poly([(42,32),(48,30),(45,34),(52,34),(44,36),(49,39),(40,36)], hair_dark)
c.poly([(44,33),(48,32),(45,35)], hair_hi)

# Torso silhouette / short coat
c.poly([(25,41),(15,44),(10,51),(8,63),(55,63),(53,50),(45,44),(39,41)], outline)
c.poly([(24,43),(16,46),(13,52),(12,63),(51,63),(50,51),(44,46),(39,43),(33,49)], navy)
# shoulders and coat highlights
c.poly([(16,46),(10,51),(8,63),(14,63),(16,53),(23,47)], deep)
c.poly([(44,46),(50,51),(52,63),(46,63),(45,52),(39,45)], navy_hi)
c.line(15,51,20,48,navy_light); c.line(47,50,50,57,navy_light)
# lapels
c.poly([(24,42),(32,49),(26,57),(19,46)], outline)
c.poly([(24,44),(30,49),(26,54),(21,46)], navy_hi)
c.poly([(39,42),(32,49),(38,57),(45,46)], outline)
c.poly([(39,44),(34,49),(38,54),(43,46)], navy_light)
# cream shirt gap
c.poly([(30,48),(33,49),(36,55),(34,63),(27,63),(27,55)], cream)
c.line(30,51,32,62,skin_shadow)

# Red scarf around neck and streaming tail
c.poly([(23,39),(29,42),(39,40),(44,44),(39,50),(28,49),(21,45)], outline)
c.poly([(24,40),(30,43),(38,42),(42,44),(38,48),(28,47),(23,44)], red)
c.poly([(27,41),(32,44),(39,43),(37,45),(29,45)], red_hi)
c.poly([(41,43),(50,40),(47,45),(58,44),(50,49),(58,52),(42,49)], outline)
c.poly([(42,44),(49,42),(47,46),(55,45),(49,48),(55,50),(41,48)], red)
c.poly([(47,44),(51,43),(49,46)], red_hi)

# Coat seams, brass buttons, sleeve detail
c.line(20,51,18,63,navy_hi); c.line(43,52,46,63,deep)
for x,y in [(24,55),(23,60),(40,56),(41,61)]:
    c.circle(x,y,1,gold_dark); c.set(x,y,gold_hi)
c.rect(11,56,5,2,gold_dark); c.rect(12,56,3,1,gold)
c.rect(48,57,4,2,gold_dark); c.rect(48,57,3,1,gold)
# final crisp facial/hair pixels
c.set(18,26,hair_hi); c.set(19,29,hair_hi); c.set(39,18,hair_hi)
c.set(21,28,skin); c.set(25,34,cream)

view(c, scale=8, margin=0)
finish(c)
