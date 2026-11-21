# Female elf archer, 64x64 pixel-art sprite
c = new_canvas(64, 64, background=None, name="female-elf-archer")

# Palette
outline = "#172c2b"
deep = "#244238"
hair_dark = "#286044"
hair = "#3f9855"
hair_light = "#76c85b"
skin_shadow = "#c77f62"
skin = "#e8aa7d"
skin_light = "#ffd0a0"
blush = "#d77f73"
white = "#f7f1d2"
eye = "#315d45"
outfit_dark = "#315f47"
outfit = "#63a85a"
outfit_light = "#a4d36a"
leather_dark = "#57382a"
leather = "#8a5a36"
leather_light = "#c28a4b"
metal = "#c7d5b0"
boot = "#40382e"

# Bow behind figure: curved segmented longbow and string
c.line(50, 8, 55, 13, outline).line(55, 13, 58, 22, outline).line(58, 22, 59, 32, outline)
c.line(59, 32, 57, 43, outline).line(57, 43, 52, 51, outline)
c.line(49, 8, 54, 14, leather_light).line(54, 14, 57, 23, leather)
c.line(57, 23, 58, 32, leather_light).line(58, 32, 56, 42, leather).line(56, 42, 51, 50, leather_light)
c.line(50, 9, 51, 49, metal)
# Quiver and arrows
c.poly([(43,18),(51,17),(54,39),(44,42),(41,23)], outline)
c.poly([(44,20),(50,19),(52,38),(45,40),(43,23)], leather)
c.line(44, 19, 41, 7, outline).line(48, 18, 48, 5, outline).line(51, 19, 54, 8, outline)
c.line(42, 8, 39, 11, metal).line(42, 8, 44, 11, metal)
c.line(48, 6, 45, 9, metal).line(48, 6, 51, 9, metal)
c.line(54, 9, 51, 12, metal).line(54, 9, 57, 11, metal)
# Back leg
c.poly([(35,43),(45,43),(46,54),(43,61),(36,61),(38,53)], outline)
c.poly([(38,45),(43,45),(44,53),(41,58),(38,58),(40,52)], outfit_dark)
c.rect(36,57,8,4,boot).rect(35,60,10,2,outline)
# Rear arm
c.poly([(38,27),(46,29),(48,39),(44,46),(40,43),(43,37)], outline)
c.poly([(39,29),(44,30),(46,38),(43,43),(41,41),(43,36)], skin_shadow)
c.rect(41,40,5,4,leather)
# Torso and tunic silhouette
c.poly([(23,27),(36,25),(43,31),(42,44),(46,50),(40,54),(25,53),(19,46),(20,34)], outline)
c.poly([(25,28),(35,27),(40,32),(39,43),(43,49),(39,51),(26,50),(22,45),(22,34)], outfit)
# Tunic shadows and hem
c.poly([(22,38),(28,37),(29,49),(25,49),(22,45)], outfit_dark)
c.poly([(29,28),(35,27),(39,32),(37,36),(30,34)], outfit_light)
c.line(25,49,39,51,outfit_light)
c.poly([(25,50),(31,50),(30,55),(24,55),(21,52)], outline)
c.poly([(27,50),(31,51),(29,54),(24,53)], outfit_dark)
# Belt
c.poly([(21,42),(40,42),(41,47),(22,46)], outline)
c.poly([(23,43),(39,43),(39,45),(23,45)], leather)
c.rect(29,42,6,5,leather_light).rect(31,43,2,3,outline)
# Front leg, angled stance
c.poly([(29,52),(37,51),(39,59),(47,60),(48,63),(36,63),(32,57),(29,62),(22,62),(23,59)], outline)
c.poly([(30,53),(35,53),(36,59),(42,60),(38,61),(34,59),(32,55),(29,60),(24,60)], outfit)
c.rect(38,59,9,3,boot)
# Neck
c.rect(27,23,9,8,outline).rect(29,23,6,7,skin_shadow).rect(30,23,5,5,skin)
# Far pointed ear
c.poly([(38,12),(51,15),(40,23),(36,21)], outline)
c.poly([(39,14),(48,16),(39,21)], skin)
c.line(41,16,44,17,skin_shadow)
# Face outline and base, three-quarter view
c.poly([(20,10),(30,6),(40,9),(44,16),(40,25),(34,29),(25,27),(19,21),(17,14)], outline)
c.poly([(22,10),(30,8),(38,10),(42,15),(39,23),(34,27),(26,25),(21,20),(19,14)], skin)
# Near pointed ear prominent
c.poly([(20,14),(8,13),(18,23),(23,21)], outline)
c.poly([(19,16),(11,15),(18,21),(22,20)], skin)
c.line(14,16,19,19,skin_shadow).set(17,18,skin_light)
# Face lighting and shadow planes
c.poly([(22,11),(31,9),(35,11),(29,14),(24,19),(21,18)], skin_light)
c.poly([(36,11),(41,15),(38,23),(34,26),(33,21)], skin_shadow)
c.set(22,20,blush).set(23,20,blush).set(36,21,blush)
# Eyes and brows, looking right
c.line(23,15,28,14,hair_dark).line(33,14,38,15,hair_dark)
c.rect(24,16,4,2,white).rect(34,16,4,2,white)
c.set(27,16,eye).set(37,16,eye).set(27,17,outline).set(37,17,outline)
# Nose and mouth
c.line(32,17,31,21,skin_shadow).set(32,21,skin_light)
c.line(29,23,34,23,outline).set(31,23,blush).set(32,23,blush)
# Hair mass, long and windswept
c.poly([(15,13),(17,7),(23,3),(33,2),(41,6),(45,12),(42,17),(40,12),(35,8),(29,8),(22,11),(20,17),(19,28),(15,39),(10,42),(13,31),(10,35),(11,23),(7,29),(10,17)], outline)
c.poly([(17,12),(19,8),(24,5),(32,4),(39,7),(43,11),(41,14),(36,9),(29,9),(23,12),(22,20),(20,29),(16,36),(13,38),(15,29),(13,32),(14,21),(11,26),(13,15)], hair)
# Long rear hair locks
c.poly([(34,7),(41,10),(43,19),(41,31),(46,38),(40,37),(36,29),(38,20)], outline)
c.poly([(36,9),(39,11),(41,19),(39,29),(43,35),(40,34),(38,28),(40,18)], hair_dark)
c.poly([(19,22),(25,24),(25,35),(21,42),(17,47),(12,45),(17,37)], outline)
c.poly([(20,24),(23,25),(23,34),(19,40),(16,44),(14,44),(19,35)], hair_dark)
# Hair highlights and bangs
c.poly([(20,9),(24,5),(31,4),(27,7),(23,11)], hair_light)
c.poly([(28,4),(35,5),(39,8),(34,7),(29,8)], hair_light)
c.poly([(19,9),(24,8),(29,9),(27,13),(23,15),(22,20),(19,18)], hair_dark)
c.poly([(25,8),(32,7),(36,9),(32,11),(30,16),(27,14)], hair)
c.line(16,18,16,31,hair_light).line(17,31,14,38,hair_light)
c.line(39,11,40,22,hair_light).line(40,23,38,29,hair_light)
# Front arm and glove, angled down toward bow grip
c.poly([(22,30),(27,31),(27,39),(35,45),(33,49),(26,45),(21,39),(18,34)], outline)
c.poly([(22,32),(25,33),(25,40),(32,45),(31,47),(27,43),(23,39),(20,34)], skin)
c.rect(30,44,5,5,outline).rect(31,44,3,4,leather)
# Shoulder trim and cloak pin
c.line(22,29,29,34,outfit_light)
c.circle(23,29,2,outline).circle(23,29,1,metal)
# Small loose hair pixels for liveliness
c.set(9,31,hair_light).set(11,40,hair).set(15,48,hair_dark).set(42,34,hair_light)

view(c, scale=8, margin=0)
finish(c)
