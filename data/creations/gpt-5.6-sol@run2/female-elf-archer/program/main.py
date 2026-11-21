# Female elf archer, 64x64 pixel art
from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="female-elf-archer")

# Palette
outline = "#182b27"
deep = "#23463a"
hair_dark = "#1f563d"
hair_mid = "#2f7a4e"
hair = "#48a85f"
hair_light = "#72cf72"
skin_dark = "#b96853"
skin = "#e29a72"
skin_light = "#f3bd8d"
blush = "#d67a68"
cloth_dark = "#376647"
cloth = "#69a85d"
cloth_light = "#9bce73"
cloth_pale = "#c2df8b"
leather_dark = "#4b3026"
leather = "#805036"
leather_light = "#b07848"
metal = "#d8d08e"
metal_hi = "#f4e6a0"
boot = "#563b31"
boot_hi = "#75513c"
white = "#f5e6c6"
shadow = "#10231f66"

# Grounding shadow
c.ellipse(31, 60, 15, 2, shadow)

# Bow behind figure: recurved silhouette and highlights
c.line(48, 12, 51, 15, outline)
c.line(51, 15, 53, 22, outline)
c.line(53, 22, 53, 33, outline)
c.line(53, 33, 50, 43, outline)
c.line(50, 43, 46, 48, outline)
c.line(47, 12, 50, 16, leather_light)
c.line(50, 16, 52, 23, leather)
c.line(52, 23, 52, 33, leather)
c.line(52, 33, 49, 42, leather_light)
c.line(49, 42, 45, 47, leather)
# bow string
c.line(48, 12, 46, 47, "#d7c99c")
# grip
c.rect(50, 28, 4, 5, outline)
c.rect(51, 29, 2, 3, leather_light)

# Quiver and arrows behind right shoulder
# arrow shafts
for x, top in [(42,5),(45,7),(48,5)]:
    c.line(x, top+3, x-2, 28, metal)
# narrow arrowheads and compact fletching
c.set(42,4,metal_hi); c.set(41,5,metal); c.set(42,5,metal_hi)
c.set(48,4,metal_hi); c.set(47,5,metal); c.set(48,5,metal_hi)
c.set(45,6,metal_hi); c.set(44,7,metal); c.set(45,7,metal_hi)
c.line(40,10,42,11,hair_light); c.set(40,11,hair_mid)
c.line(44,11,46,12,hair_light); c.set(44,12,hair_mid)
c.line(47,9,49,10,hair_light); c.set(47,10,hair_mid)
# quiver case
c.poly([(39,19),(47,18),(46,38),(40,39),(37,22)], outline)
c.poly([(40,21),(46,20),(45,36),(41,37),(39,22)], leather)
c.line(40,23,45,22,leather_light)
c.line(41,34,45,33,leather_dark)

# Long rear hair mass
c.poly([(21,13),(27,8),(37,8),(43,13),(44,23),(41,29),(43,39),(39,46),(34,42),(29,47),(23,43),(20,35),(17,28),(18,19)], outline)
c.poly([(22,14),(28,9),(36,9),(41,13),(42,21),(39,28),(41,37),(38,43),(34,39),(30,45),(25,41),(23,34),(19,27),(20,18)], hair_dark)
c.poly([(23,14),(29,10),(35,10),(39,13),(37,18),(31,20),(29,28),(30,39),(26,41),(24,33),(21,26),(21,18)], hair_mid)
c.poly([(24,14),(29,11),(33,11),(28,18),(26,27),(27,35),(25,33),(22,25),(22,18)], hair)
c.line(25,15,22,25,hair_light)
c.line(27,19,25,32,hair)
c.line(36,13,40,22,hair)
c.line(38,26,39,37,hair_light)
c.set(29,40,hair_light); c.set(30,41,hair_light)

# Head / jaw in three-quarter view
c.poly([(27,11),(35,9),(41,13),(42,18),(48,20),(43,23),(40,28),(34,30),(28,26),(25,20)], outline)
c.poly([(28,12),(35,10),(40,13),(40,19),(45,20),(41,22),(39,26),(34,28),(29,25),(27,20)], skin)
# pointed ear, prominently right-facing
c.poly([(40,15),(52,16),(43,23),(39,22)], outline)
c.poly([(41,17),(49,17),(42,21),(40,21)], skin)
c.line(43,18,46,18,skin_light)
c.set(42,20,skin_dark)
# face light plane and cheek
c.poly([(31,12),(36,11),(39,14),(39,21),(36,26),(32,26),(29,23),(29,16)], skin_light)
c.set(39,22,blush); c.set(38,23,blush)
# nose
c.line(39,17,41,19,skin_dark); c.set(40,18,skin_light)
# eye and brow
c.line(35,15,39,15,hair_dark)
c.set(37,16,outline); c.set(38,16,outline); c.set(38,17,"#d8c56b")
c.set(39,16,white)
# mouth
c.line(37,23,40,23,skin_dark); c.set(39,22,skin_light)

# Foreground hair cap and side locks
c.poly([(23,14),(27,9),(35,7),(41,10),(43,14),(39,14),(36,12),(33,17),(29,19),(27,26),(23,25),(24,18),(20,18)], outline)
c.poly([(24,14),(28,10),(35,8),(40,10),(41,13),(37,13),(35,11),(32,16),(28,18),(26,24),(24,23),(26,16),(22,17)], hair)
c.poly([(26,13),(30,10),(35,9),(31,14),(28,17),(26,22),(26,16),(23,16)], hair_light)
c.line(35,10,40,12,hair_mid)
c.line(34,12,31,18,hair_dark)
# temple braid / beads
c.set(29,19,hair_light); c.set(28,21,hair); c.set(28,23,hair_light); c.set(29,25,hair)
c.set(29,27,metal_hi)

# Neck
c.poly([(30,26),(39,25),(39,33),(31,33)], outline)
c.rect(32,26,6,7,skin)
c.rect(34,26,4,5,skin_light)

# Back shoulder / capelet
c.poly([(28,29),(39,28),(46,33),(45,40),(25,39),(22,34)], outline)
c.poly([(28,30),(38,29),(44,33),(43,37),(26,37),(24,34)], cloth_dark)
c.line(27,31,42,35,cloth_light)

# Torso tunic, fitted three-quarter silhouette
c.poly([(27,31),(38,29),(44,34),(42,45),(38,49),(27,47),(23,41),(24,34)], outline)
c.poly([(28,32),(37,30),(42,34),(40,44),(37,47),(28,45),(25,40),(26,34)], cloth)
c.poly([(29,32),(35,31),(37,45),(30,44),(27,39),(27,34)], cloth_light)
c.poly([(30,33),(34,32),(34,42),(30,42),(28,38)], cloth_pale)
# neckline and collar
c.poly([(29,30),(34,35),(38,30),(40,31),(35,37),(32,37),(27,32)], outline, fill=False)
c.line(30,31,34,35,skin_light)
c.line(34,35,38,30,skin)
# small leaf brooch
c.poly([(34,35),(36,36),(34,39),(32,36)], metal)
c.set(34,36,metal_hi)

# Rear arm (right side), bent toward belt
c.poly([(42,33),(47,35),(47,42),(42,47),(39,44),(43,40),(42,37)], outline)
c.poly([(43,34),(45,36),(45,40),(41,44),(40,43),(43,39)], skin)
c.set(43,35,skin_light); c.set(42,43,skin_light)
# bracer
c.poly([(41,41),(45,39),(47,42),(43,46),(40,44)], outline)
c.poly([(42,41),(45,40),(46,42),(43,44),(41,43)], leather)
c.line(43,41,45,42,leather_light)

# Front arm hanging left
c.poly([(25,34),(21,35),(19,45),(21,53),(26,51),(24,45),(28,39)], outline)
c.poly([(24,35),(22,36),(21,45),(23,50),(24,49),(23,44),(26,38)], skin)
c.line(23,36,22,43,skin_light)
# glove / hand
c.poly([(21,48),(25,47),(27,53),(24,56),(21,53)], outline)
c.poly([(22,49),(24,49),(25,52),(24,54),(22,52)], leather)
c.set(23,49,leather_light)

# Belt
c.poly([(26,43),(40,44),(41,49),(27,48)], outline)
c.poly([(27,44),(39,45),(39,47),(28,46)], leather)
c.rect(32,44,5,5,metal)
c.rect(33,45,3,3,leather_dark)
c.set(32,44,metal_hi)

# Split tunic skirt
c.poly([(27,47),(39,47),(43,55),(35,57),(31,53),(27,57),(23,54)], outline)
c.poly([(28,48),(38,48),(41,54),(35,55),(31,51),(27,55),(25,53)], cloth_dark)
c.poly([(29,48),(34,49),(31,52),(28,54),(26,53)], cloth_light)
c.poly([(35,49),(38,49),(40,53),(35,54)], cloth)
c.line(31,49,31,52,cloth_pale)

# Legs, staggered standing pose
c.poly([(27,53),(33,53),(33,61),(25,61),(24,58)], outline)
c.poly([(28,53),(32,53),(31,59),(26,59),(26,57)], boot)
c.line(28,54,27,58,boot_hi)
c.poly([(35,54),(41,53),(44,60),(37,62),(34,60)], outline)
c.poly([(36,55),(40,54),(42,59),(38,60),(36,59)], boot)
c.line(38,55,40,59,boot_hi)
# boot tops and soles
c.line(26,55,32,55,leather_light)
c.line(36,56,41,55,leather_light)
c.rect(24,59,9,2,outline)
c.rect(37,59,7,2,outline)
c.line(26,59,31,59,boot_hi)
c.line(38,59,41,59,boot_hi)

# Crisp selective outline accents and stray highlights
c.set(20,18,hair_light); c.set(19,24,hair_mid)
c.set(42,12,hair_light); c.set(43,13,hair_mid)
c.set(48,16,skin_light)
c.set(30,29,skin_light)
c.set(25,40,cloth_pale)
c.set(40,48,cloth_light)

view(c, scale=8, margin=0)
finish(c)
