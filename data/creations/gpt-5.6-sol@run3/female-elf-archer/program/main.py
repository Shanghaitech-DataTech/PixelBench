# 64x64 female elf archer portrait sprite
from pixelbench_api import *

result = new_canvas(64, 64, background=None, name="female-elf-archer")

# Compact fantasy palette
outline = "#17251f"
deep = "#23372a"
hair_dark = "#1f5034"
hair_mid = "#2f7542"
hair_light = "#58a653"
hair_glint = "#86c96a"
skin_dark = "#9b5d45"
skin = "#d78b64"
skin_light = "#f0b283"
blush = "#c96e65"
eye = "#223028"
white = "#f3e7c8"
cloth_dark = "#315d3b"
cloth = "#57955a"
cloth_light = "#83bd70"
cream = "#d6d18f"
leather_dark = "#5a3826"
leather = "#8a5832"
leather_light = "#bd8245"
metal = "#a7b8a0"
metal_light = "#d5dfbd"

# Rear bow: dark contour and warm inner stave, angled behind the right shoulder.
result.path("M45 9 Q58 19 56 39 Q55 48 48 56", outline, fill=False)
result.path("M46 10 Q56 20 54 39 Q53 48 47 55", leather_light, fill=False)
result.line(46, 10, 47, 55, cream)
result.set(45, 9, metal_light).set(46, 9, metal_light)
result.set(47, 55, metal_light).set(48, 55, metal_light)
# Wrapped grip at the bow's midpoint.
result.rect(52, 31, 4, 8, outline)
result.rect(53, 32, 2, 6, leather)
result.set(53,33,leather_light).set(54,36,leather_light)

# Quiver and arrow shafts behind the left shoulder.
result.line(16, 8, 22, 35, outline)
result.line(18, 7, 24, 34, cream)
result.line(21, 8, 25, 34, cream)
# Arrowheads and fletching
result.poly([(15,7),(18,8),(17,11)], metal_light)
result.poly([(17,6),(20,7),(19,10)], metal)
result.poly([(20,7),(23,8),(21,11)], metal_light)
result.poly([(19,13),(23,12),(21,16)], hair_light)
result.poly([(21,13),(25,12),(23,16)], hair_mid)
result.poly([(23,13),(27,12),(25,16)], hair_light)
result.poly([(16,27),(23,25),(29,45),(19,48),(14,34)], outline)
result.poly([(18,28),(23,27),(27,43),(20,46),(16,34)], leather_dark)
result.line(18, 33, 25, 31, leather_light)

# Back leg and boot.
result.poly([(30,43),(39,43),(40,55),(38,61),(31,61),(33,54)], outline)
result.poly([(32,44),(37,44),(38,54),(36,58),(33,58),(35,52)], cloth_dark)
result.poly([(31,56),(38,55),(40,61),(30,61)], leather_dark)
result.rect(30,60,11,2,outline)
result.rect(33,57,5,2,leather)

# Forward leg, wrapped stocking, and boot.
result.poly([(23,42),(33,43),(30,55),(28,62),(19,62),(22,57),(21,50)], outline)
result.poly([(24,44),(30,44),(28,53),(26,58),(22,58),(24,52)], cloth)
result.line(23,48,29,50,cream)
result.line(22,52,28,54,cream)
result.poly([(20,57),(28,57),(29,62),(18,62)], leather_dark)
result.rect(18,61,12,2,outline)
result.rect(22,58,6,2,leather)

# Long rear hair mass flowing to the waist.
result.poly([(20,15),(27,10),(36,11),(43,17),(43,29),(46,36),(42,47),(37,43),(34,50),(29,44),(24,49),(18,41),(20,31),(16,25)], outline)
result.poly([(21,16),(28,11),(35,12),(41,17),(40,28),(44,36),(40,44),(36,39),(33,47),(29,41),(24,46),(20,40),(22,31),(18,25)], hair_dark)
result.poly([(22,17),(29,13),(33,13),(27,22),(25,34),(27,41),(23,43),(21,38),(24,29)], hair_mid)
result.poly([(36,15),(40,19),(38,29),(42,36),(39,40),(35,34),(37,25)], hair_mid)
result.poly([(25,17),(29,14),(28,25),(26,31)], hair_light)
result.poly([(39,20),(40,27),(38,31),(37,25)], hair_light)

# Torso silhouette and tunic.
result.poly([(24,30),(35,28),(43,34),(42,44),(37,49),(24,47),(19,42),(20,34)], outline)
result.poly([(25,31),(34,30),(40,34),(39,42),(36,46),(25,45),(21,41),(22,34)], cloth)
# Tunic shadow and hem
result.poly([(22,37),(28,39),(37,36),(40,38),(39,43),(35,46),(25,44),(21,40)], cloth_dark)
result.poly([(24,43),(36,45),(34,48),(25,46)], cloth_light)
result.line(25,45,35,47,cream)
# Belt, buckle, pouch
result.poly([(21,39),(39,40),(39,43),(22,42)], outline)
result.poly([(23,40),(37,41),(37,42),(23,41)], leather)
result.rect(29,39,5,5,outline)
result.rect(30,40,3,3,leather_light)
result.set(31,41,deep)
# Diagonal harness anchors the bow and quiver to the outfit.
result.line(39,31,27,44,outline)
result.line(38,32,28,43,leather_light)
result.set(36,34,cream).set(33,37,cream)
result.poly([(37,41),(43,42),(42,48),(37,47)], outline)
result.poly([(38,42),(41,43),(40,46),(38,46)], leather)

# Rear arm, bent toward the waist.
result.poly([(38,31),(44,33),(45,39),(40,43),(36,40),(41,37)], outline)
result.poly([(39,33),(42,34),(43,38),(40,41),(38,39),(42,36)], skin)
result.set(41,34,skin_light).set(42,35,skin_light)
# Bracer
result.poly([(39,39),(43,37),(45,40),(41,44),(38,42)], outline)
result.poly([(40,39),(43,39),(43,41),(41,42),(39,41)], leather)
result.set(42,40,leather_light)

# Neck.
result.poly([(28,25),(36,25),(37,32),(30,35),(26,31)], outline)
result.poly([(29,25),(35,25),(35,31),(30,33),(28,30)], skin_dark)
result.poly([(30,25),(35,25),(34,30),(30,31)], skin)

# Head, three-quarter view facing right.
result.poly([(23,14),(30,10),(38,12),(43,18),(42,25),(38,29),(30,29),(24,25),(21,20)], outline)
result.poly([(25,14),(31,11),(37,13),(41,18),(40,24),(37,27),(30,27),(25,24),(23,20)], skin)
# Face light plane and cheek shadow
result.poly([(31,13),(37,14),(40,18),(39,23),(36,26),(32,25),(34,21)], skin_light)
result.poly([(25,22),(31,26),(29,28),(24,24)], skin_dark)
result.set(38,24,blush).set(39,23,blush)
# Pointed ear to the left, with inner ear.
result.poly([(24,17),(14,15),(22,23),(26,22)], outline)
result.poly([(23,18),(16,16),(22,21),(25,21)], skin)
result.line(18,17,23,20,skin_dark)
result.set(17,16,skin_light)
# Nose, eye, brow, mouth
result.line(34,17,38,17,hair_dark)
result.rect(35,18,3,2,eye)
result.set(36,18,white)
result.set(37,19,deep)
result.poly([(39,19),(42,22),(38,22)], skin_dark)
result.set(40,21,skin_light)
result.line(36,24,39,24,blush)
result.set(39,25,skin_dark)

# Hair cap, side sweep, and long front lock.
result.poly([(21,18),(22,13),(28,9),(36,10),(42,15),(39,18),(35,15),(31,19),(27,18),(24,24)], outline)
result.poly([(23,17),(24,13),(29,10),(35,11),(40,15),(38,17),(34,14),(31,17),(27,16),(24,21)], hair_mid)
result.poly([(25,14),(30,11),(34,12),(30,14),(27,18),(24,19)], hair_light)
result.line(28,11,34,12,hair_glint)
result.poly([(24,20),(29,19),(29,30),(25,38),(21,35),(24,28)], outline)
result.poly([(25,20),(28,20),(27,29),(24,35),(22,34),(25,27)], hair_mid)
result.line(26,22,26,30,hair_light)

# Foreground arm crosses the torso, hand resting near belt.
result.poly([(22,32),(27,32),(30,38),(37,40),(36,45),(28,42),(24,39),(20,37)], outline)
result.poly([(23,33),(26,33),(29,38),(35,40),(35,43),(29,41),(25,38),(22,36)], skin)
result.poly([(21,32),(26,31),(28,35),(23,39),(19,37)], cloth_dark)
result.poly([(22,33),(25,33),(26,35),(23,37),(21,36)], cloth_light)
# Forearm guard and hand/fingers
result.poly([(28,38),(34,39),(33,43),(28,41)], leather_dark)
result.line(29,39,33,40,leather_light)
result.poly([(33,39),(39,41),(37,45),(33,43)], skin)
result.line(35,41,38,42,skin_light)
result.set(36,44,skin_dark)

# Shoulder leaf clasp and small outfit highlights.
result.circle(23,31,2,outline)
result.poly([(22,30),(25,31),(23,33),(21,31)], cream)
result.set(23,31,cloth_light)
result.line(34,32,38,35,cloth_light)
result.set(25,44,cloth_light).set(26,45,cloth_light)

# A few hard outline accents to keep the stance crisp.
result.set(18,62,outline).set(29,62,outline).set(30,61,outline).set(40,61,outline)
result.set(14,15,outline).set(15,15,outline)

view(result, scale=8, margin=0)
finish(result)
