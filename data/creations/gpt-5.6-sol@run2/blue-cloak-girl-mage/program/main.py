# 64x64 front-facing anime mage sprite
from pixelbench_api import *

result = new_canvas(64, 64, background=None, name="blue-cloak-girl-mage")

# Compact named palette
outline = result.color("#11172d", "outline")
deep = result.color("#17254b", "deep_blue")
navy = result.color("#203766", "navy")
blue = result.color("#31558c", "cloak_blue")
lightblue = result.color("#4f79ad", "cloak_light")
shadow = result.color("#293d70", "cloak_shadow")
white = result.color("#f3f0e5", "boot_white")
white_sh = result.color("#b9c7d4", "boot_shadow")
skin = result.color("#f1b99d", "skin")
skin_sh = result.color("#c77f72", "skin_shadow")
hair = result.color("#d9e1ea", "silver_hair")
hair_sh = result.color("#879ab5", "hair_shadow")
eye = result.color("#6dd3cf", "eyes")
gold = result.color("#cc7724", "amber_dark")
amber = result.color("#f3a62f", "amber")
glow = result.color("#ffd76a", "amber_glow")
hot = result.color("#fff1aa", "glow_core")
leather = result.color("#6e4938", "staff_wood")

# Staff behind the figure: slightly angled for a relaxed stance.
result.line(55, 56, 50, 14, outline)
result.line(54, 56, 49, 15, leather)
result.set(53, 49, gold).set(53, 50, gold)
# Pixel-art amber crystal and restrained halo.
result.set(49, 7, glow).set(48, 8, glow).set(50, 8, glow).set(46, 10, glow).set(52, 10, glow)
result.poly([(49,6),(53,10),(51,15),(47,15),(45,10)], outline)
result.poly([(49,7),(52,10),(50,14),(47,14),(46,10)], amber)
result.poly([(49,8),(51,10),(49,13),(47,10)], glow)
result.set(49,9,hot).set(48,10,hot)
result.rect(48,15,3,2,gold)

# Back hair and hood silhouette.
result.poly([(24,10),(28,7),(35,7),(40,11),(41,20),(38,26),(24,26),(21,20),(22,13)], outline)
result.poly([(25,10),(29,8),(35,8),(39,12),(39,21),(36,25),(25,24),(23,20),(23,13)], hair_sh)
result.rect(24,16,3,9,hair)
result.rect(36,16,3,9,hair)
result.set(23,18,hair).set(39,18,hair)

# Cloak outer mass, broad shoulders and flared hem.
result.poly([(22,21),(17,24),(14,34),(16,43),(12,52),(19,56),(28,54),(34,55),(43,57),(48,52),(44,43),(47,34),(43,24),(38,21)], outline)
result.poly([(22,23),(18,25),(16,34),(18,42),(14,51),(20,54),(28,52),(34,53),(42,55),(46,51),(42,42),(45,34),(42,25),(37,23)], navy)
# Cape planes and folds.
result.poly([(18,27),(23,24),(27,28),(25,50),(20,53),(15,51),(19,42),(17,34)], blue)
result.poly([(39,24),(43,27),(44,34),(41,42),(45,51),(42,54),(35,52),(34,28)], shadow)
result.poly([(24,26),(31,29),(29,52),(25,51)], lightblue)
result.poly([(31,29),(36,26),(35,52),(30,53)], deep)
result.line(19,42,17,50,lightblue)
result.line(41,42,44,50,blue)

# Face in front of hair.
result.poly([(27,10),(35,10),(38,13),(37,19),(34,23),(29,23),(25,19),(25,13)], outline)
result.poly([(27,11),(35,11),(37,14),(36,19),(33,22),(29,22),(26,19),(26,13)], skin)
result.rect(27,19,9,2,skin_sh)
result.rect(28,20,7,2,skin)
# Fringe with readable asymmetry.
result.poly([(25,12),(27,9),(35,9),(38,12),(37,15),(35,13),(34,16),(32,12),(29,15),(26,15)], hair)
result.poly([(25,12),(28,9),(31,9),(28,14),(26,15)], hair_sh)
# Anime eyes, brows, tiny mouth.
result.rect(27,16,3,1,outline).rect(33,16,3,1,outline)
result.set(28,17,eye).set(34,17,eye)
result.set(31,20,skin_sh)
result.rect(30,21,3,1,outline)
result.set(31,21,skin)

# High cloak collar and gold clasp.
result.poly([(21,22),(25,20),(30,25),(31,29),(24,27)], outline)
result.poly([(42,22),(37,20),(32,25),(31,29),(39,27)], outline)
result.poly([(22,23),(25,22),(29,26),(25,26)], blue)
result.poly([(41,23),(37,22),(33,26),(38,26)], blue)
result.rect(29,25,5,4,outline)
result.rect(30,26,3,2,amber)
result.set(31,26,glow)

# Relaxed arms: left hangs, right hand lightly grips staff.
result.poly([(18,26),(14,35),(15,43),(19,43),(21,34),(24,28)], outline)
result.poly([(19,27),(16,35),(17,41),(19,41),(20,34),(23,28)], blue)
result.rect(16,41,4,3,outline)
result.rect(17,41,3,2,skin)
result.poly([(40,27),(44,31),(48,36),(51,34),(53,37),(49,41),(45,39),(41,35)], outline)
result.poly([(40,28),(43,32),(47,37),(49,35),(51,37),(49,39),(46,38),(42,35)], blue)
result.rect(49,34,4,5,skin)
result.set(49,34,outline).set(52,38,outline)

# Tunic opening beneath cloak.
result.poly([(27,29),(35,29),(36,43),(33,48),(28,48),(26,43)], outline)
result.poly([(28,30),(34,30),(34,42),(32,46),(29,46),(28,42)], white)
result.rect(28,30,6,3,navy)
result.rect(28,39,6,2,gold)
result.set(31,39,amber)

# Legs, one subtly offset to keep the pose relaxed.
result.poly([(25,46),(31,46),(31,55),(29,60),(22,60),(21,57),(24,53)], outline)
result.poly([(32,46),(37,47),(39,54),(43,57),(42,60),(34,60),(32,55)], outline)
result.poly([(26,47),(30,47),(29,54),(27,58),(23,58),(23,57),(26,52)], white_sh)
result.poly([(33,47),(36,48),(37,54),(41,57),(41,58),(35,58),(34,54)], white_sh)
# White boot faces and dark soles.
result.poly([(24,52),(29,53),(28,58),(22,58),(23,55)], white)
result.poly([(35,53),(38,54),(42,57),(41,58),(35,58)], white)
result.rect(21,58,9,2,outline)
result.rect(34,58,9,2,outline)
result.rect(23,57,5,1,white)
result.rect(36,57,5,1,white)

# Selective highlights and pixel cleanup accents.
result.set(19,29,lightblue).set(18,30,lightblue).set(41,28,lightblue)
result.line(20,53,25,51,lightblue)
result.set(43,52,lightblue)
result.set(13,51,outline).set(47,51,outline)

view(result, scale=8, margin=1, edges="all")
finish(result)
