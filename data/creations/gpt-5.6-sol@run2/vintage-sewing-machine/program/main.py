from pixelbench_api import *

# 48 px vintage mechanical sewing machine sprite.
c = new_canvas(48, 48, background=None, name="vintage-sewing-machine")

# Palette
outline = "#17272a"
deep = "#203b3b"
dark = "#294b49"
mid = "#3e6660"
light = "#6f8b78"
cream = "#e4d7ae"
cream_hi = "#fff0c8"
gold = "#c79a45"
gold_hi = "#f1c96b"
steel = "#9aaca8"
steel_hi = "#dbe1d5"
shadow = "#101b1f"
red_dark = "#8e2630"
red = "#c83a3f"
red_hi = "#f05b50"

# Rear feet and cast-iron base shadow.
c.rect(8, 40, 6, 3, shadow)
c.rect(36, 40, 6, 3, shadow)
c.set(7, 41, shadow); c.set(42, 41, shadow)

# Slightly angled base: dark outline, enamel inset, cream bed.
c.poly([(4,34),(38,33),(45,37),(43,42),(7,43),(3,40)], outline)
c.poly([(6,35),(37,34),(42,37),(40,40),(8,41),(5,39)], deep)
c.poly([(8,34),(34,33),(39,35),(36,38),(9,39),(6,37)], cream)
c.poly([(9,35),(34,34),(37,35),(35,37),(9,38),(7,37)], cream_hi)
c.line(10,39,39,39,gold)
c.set(7,40,gold); c.set(40,38,gold)

# Red fabric under the presser foot, draped over front edge.
c.poly([(19,34),(32,34),(37,36),(35,38),(19,39)], red_dark)
c.poly([(20,34),(31,34),(35,35),(33,37),(19,38)], red)
c.line(21,35,32,35,red_hi)
c.poly([(19,38),(33,37),(32,41),(20,42)], red_dark)
c.poly([(21,38),(31,37),(30,40),(21,41)], red)
c.line(22,39,29,39,red_hi)

# Upright pillar silhouette, with cast-metal curve into the arm.
c.poly([(33,9),(39,10),(41,13),(41,31),(38,35),(32,34),(33,30),(35,28),(35,17),(31,15)], outline)
c.poly([(34,10),(38,11),(39,13),(39,29),(37,32),(34,32),(36,28),(36,16),(33,14)], dark)
c.line(38,14,38,27,mid)
c.set(37,12,light); c.set(38,13,light)

# Main overhanging arm: classic rounded vintage body.
c.poly([(11,7),(32,7),(37,10),(36,16),(31,19),(18,18),(15,21),(14,28),(9,28),(8,24),(9,17),(6,14),(7,10)], outline)
c.poly([(11,8),(31,8),(35,10),(34,15),(30,17),(17,16),(14,19),(13,26),(10,26),(10,19),(8,14),(8,11)], dark)
c.poly([(12,9),(30,9),(33,11),(32,14),(29,15),(16,14),(13,17),(11,22),(10,18),(10,14),(9,12)], mid)
# Enamel highlight and gold pinstripe.
c.line(12,9,29,9,light)
c.set(31,10,light); c.set(32,11,light)
c.line(12,15,29,15,gold)
c.set(30,14,gold_hi); c.set(11,16,gold)

# Decorative badge on the arm.
c.poly([(19,10),(27,10),(29,12),(27,14),(19,14),(17,12)], gold)
c.poly([(20,11),(26,11),(27,12),(26,13),(20,13),(19,12)], deep)
c.line(21,12,25,12,gold_hi)
c.set(18,11,cream_hi); c.set(28,11,cream_hi)

# Front face / tension dial and thread guides.
c.rect(9,17,5,7,outline)
c.rect(10,18,3,5,cream)
c.set(11,19,cream_hi); c.set(12,22,gold)
c.circle(16,18,2,outline)
c.circle(16,18,1,gold)
c.set(16,17,gold_hi)
c.line(16,20,19,22,steel)
c.set(18,21,steel_hi)
# Top spool pin and thread spool.
c.rect(15,4,2,4,outline)
c.rect(14,4,4,2,gold)
c.rect(13,3,5,2,cream)
c.line(17,6,26,8,steel)
c.set(18,6,steel_hi); c.set(22,7,steel_hi)

# Needle head, bar and presser mechanism.
c.poly([(12,25),(19,25),(20,29),(18,32),(12,32),(10,29)], outline)
c.poly([(13,26),(18,26),(18,29),(17,31),(12,30),(12,28)], dark)
c.rect(16,27,3,2,gold)
c.rect(17,29,2,7,outline)
c.rect(17,29,1,6,steel_hi)
c.set(18,35,steel_hi); c.set(18,36,outline)
# Presser foot around needle.
c.rect(15,35,6,2,outline)
c.rect(16,35,4,1,steel_hi)
c.set(15,36,steel); c.set(20,36,steel)
# Small faceplate highlights and screw.
c.line(13,27,13,30,steel)
c.set(14,27,steel_hi); c.set(14,30,gold_hi)

# Large exposed handwheel on right: outlined ring with spokes.
c.circle(40,20,7,outline)
c.circle(40,20,5,cream)
c.circle(40,20,3,deep)
# Four spokes.
c.line(40,15,40,25,gold)
c.line(35,20,45,20,gold)
c.line(37,17,43,23,gold)
c.line(43,17,37,23,gold)
c.circle(40,20,1,outline)
c.set(40,20,steel_hi)
# Wheel rim highlights and crank handle.
c.set(38,14,cream_hi); c.set(39,14,cream_hi); c.set(44,18,cream_hi)
c.set(44,22,gold_hi); c.set(36,24,gold)
c.line(44,19,46,17,outline)
c.rect(45,15,2,3,outline)
c.set(45,15,gold_hi)

# Bed hardware and tiny reflected highlights.
c.rect(25,31,7,2,outline)
c.rect(26,31,5,1,steel)
c.set(27,31,steel_hi)
c.set(11,36,steel); c.set(12,36,steel_hi)
c.set(6,38,mid); c.set(39,37,light)

# A few crisp dark separations reinforce the silhouette.
c.set(8,12,outline); c.set(9,10,outline)
c.line(34,16,34,28,outline)
c.set(35,30,mid); c.set(36,31,light)

result = c
view(result, scale=10, margin=1, edges="all")
finish(result)
