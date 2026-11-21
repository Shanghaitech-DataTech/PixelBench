from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="dragon_hatchling")

# Palette
outline = "#17251f"
deep = "#243b2d"
dark = "#31533a"
mid = "#477449"
green = "#5f9255"
light = "#82ad65"
high = "#a1c679"
belly = "#d3c98d"
belly_shadow = "#aaa66f"
horn = "#d8d0a4"
horn_shadow = "#918d70"
mouth = "#522d35"
tongue = "#b85b65"
eye = "#f0c94f"
shine = "#fff3b0"

# Rear wing (right), half spread: thick, angular silhouette.
c.poly([(36,29),(41,13),(45,7),(48,19),(57,13),(54,27),(48,34)], outline)
c.poly([(39,28),(42,15),(44,11),(45,23),(54,18),(51,27),(47,31)], dark)
c.poly([(43,25),(44,15),(46,25),(52,21),(49,28),(46,30)], mid)
c.line(45,24,53,18,light)
c.line(45,25,44,11,deep)
# Wing edge claws
c.poly([(44,11),(45,5),(47,11)], horn_shadow)
c.poly([(54,18),(59,14),(55,22)], horn_shadow)

# Front wing (left), spread down and out.
c.poly([(28,27),(23,14),(17,8),(17,19),(8,14),(12,27),(20,36)], outline)
c.poly([(26,28),(22,16),(19,12),(20,24),(11,18),(15,27),(21,33)], mid)
c.poly([(22,26),(20,16),(23,22),(24,30)], green)
c.line(20,24,11,18,light)
c.line(20,24,19,12,deep)
# Wing claws
c.poly([(17,9),(15,5),(20,9)], horn_shadow)
c.poly([(11,18),(6,15),(10,22)], horn_shadow)

# Tail silhouette, curled to the right and upward.
c.poly([(36,43),(46,43),(53,39),(58,34),(60,37),(55,44),(48,49),(39,51)], outline)
c.poly([(38,45),(46,45),(53,41),(57,37),(57,40),(52,45),(47,48),(39,49)], mid)
c.line(43,46,53,42,light)
# Tail spikes
c.poly([(49,43),(50,37),(53,42)], outline)
c.poly([(50,41),(50,38),(52,42)], horn_shadow)
c.poly([(54,39),(55,33),(58,37)], outline)
c.poly([(55,37),(56,34),(57,38)], horn)
c.poly([(57,36),(61,31),(60,39)], outline)
c.poly([(58,36),(60,33),(59,38)], horn_shadow)

# Body and haunches.
c.ellipse(34,39,12,14,outline)
c.ellipse(35,39,9,12,dark)
c.poly([(27,34),(30,27),(39,28),(44,37),(42,48),(27,48),(23,41)], outline)
c.poly([(29,34),(31,29),(37,30),(41,37),(40,47),(28,46),(26,40)], mid)
# Back scales/highlights.
c.poly([(35,30),(39,32),(36,35),(32,33)], green)
c.poly([(38,35),(42,38),(38,39),(34,37)], green)
c.poly([(39,41),(42,44),(38,45),(35,42)], light)
c.set(30,36,light).set(31,35,light).set(29,40,green).set(33,45,green)

# Pale segmented belly, from throat into torso.
c.poly([(27,29),(32,28),(35,34),(35,44),(32,49),(27,45),(25,37)], belly_shadow)
c.poly([(28,30),(31,30),(33,34),(33,44),(31,47),(28,44),(27,37)], belly)
c.line(27,35,33,35,belly_shadow)
c.line(27,39,33,39,belly_shadow)
c.line(28,43,33,43,belly_shadow)
c.set(29,31,shine).set(28,36,high)

# Hind legs and feet.
c.poly([(27,43),(25,49),(20,52),(17,51),(19,47),(22,43)], outline)
c.poly([(24,44),(23,48),(20,50),(19,50),(21,46)], mid)
c.poly([(19,50),(15,53),(21,53),(23,50)], outline)
c.set(17,52,horn).set(20,52,horn)
c.poly([(38,44),(43,47),(46,52),(43,54),(38,50),(34,48)], outline)
c.poly([(38,46),(41,48),(43,51),(42,52),(38,49),(35,47)], dark)
c.poly([(42,51),(40,54),(47,54),(45,51)], outline)
c.set(43,53,horn).set(46,53,horn)

# Neck rising into head.
c.poly([(28,34),(23,29),(20,23),(24,17),(34,17),(39,23),(37,31),(33,36)], outline)
c.poly([(27,32),(24,28),(23,23),(26,19),(32,19),(36,23),(35,29),(32,34)], green)
c.poly([(31,19),(35,23),(33,28),(30,26)], light)
# Neck scale clusters.
c.poly([(24,27),(27,25),(29,28),(26,30)], mid)
c.poly([(29,29),(32,27),(34,30),(31,33)], dark)

# Head and muzzle, growling left.
c.poly([(23,17),(20,13),(22,9),(28,7),(35,10),(38,15),(36,21),(29,24),(22,22),(17,25),(10,23),(7,19),(10,16),(17,16)], outline)
c.poly([(23,18),(21,14),(23,11),(28,9),(33,11),(35,15),(34,19),(29,22),(23,20),(18,23),(11,21),(9,19),(11,18),(18,18)], green)
# Brow and face planes.
c.poly([(22,12),(29,10),(33,12),(29,14),(23,14)], light)
c.poly([(19,16),(25,14),(24,18),(18,19)], mid)
c.poly([(29,15),(35,15),(33,20),(28,21)], dark)
c.set(30,11,high).set(31,12,high).set(16,19,light)

# Small swept horns and cheek spike.
c.poly([(24,10),(22,5),(27,9)], outline)
c.poly([(24,8),(23,6),(26,9)], horn)
c.poly([(31,10),(34,5),(35,12)], outline)
c.poly([(32,9),(34,6),(34,11)], horn_shadow)
c.poly([(35,19),(41,20),(35,23)], outline)
c.poly([(36,20),(39,20),(35,22)], horn)

# Open mouth with lower jaw.
c.poly([(18,19),(14,18),(10,20),(14,22),(21,22),(25,19)], mouth)
c.set(11,20,tongue).set(12,20,tongue).set(13,21,tongue)
# Teeth and jaw rim.
c.poly([(15,19),(16,22),(18,19)], horn)
c.poly([(21,20),(20,23),(23,20)], horn)
c.line(11,22,20,24,outline)
c.line(20,24,24,21,outline)
c.set(13,22,belly).set(14,23,belly).set(18,23,belly)
# Nostril.
c.set(12,18,outline).set(13,18,deep)

# Eye under heavy brow.
c.rect(25,13,4,3,outline)
c.set(26,14,eye).set(27,14,shine).set(28,14,outline)
c.line(24,12,30,12,deep)

# Forelegs planted wide.
c.poly([(26,33),(22,35),(20,43),(22,48),(27,48),(28,43),(29,35)], outline)
c.poly([(25,35),(23,36),(22,43),(23,46),(26,46),(26,42),(27,35)], green)
c.poly([(22,46),(18,49),(27,50),(27,46)], outline)
c.set(20,48,horn).set(23,49,horn).set(26,49,horn)
c.poly([(35,34),(39,35),(41,43),(40,49),(34,49),(32,44),(33,36)], outline)
c.poly([(35,36),(38,37),(39,43),(38,47),(35,47),(34,43)], mid)
c.poly([(35,47),(32,50),(42,50),(40,47)], outline)
c.set(34,49,horn).set(37,49,horn).set(40,49,horn)

# Pixel-scale accents for texture and silhouette readability.
for x,y,col in [(22,31,light),(25,32,high),(39,33,light),(42,40,green),(24,39,dark),(37,38,deep),(31,50,deep),(29,52,deep)]:
    c.set(x,y,col)

finish(c)
view(c, scale=8, margin=1, edges="all")
