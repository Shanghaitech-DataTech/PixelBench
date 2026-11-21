from pixelbench_api import *

# 64x64 transparent boss sprite: a hovering void eye.
result = new_canvas(64, 64, background=None, name="void-eye")

# Tight, ominous palette.
OUT = "#120a20"
OUT2 = "#21112f"
SHADOW = "#170c2f66"
SHADOW_CORE = "#2410448c"
FLESH_DARK = "#49304f"
FLESH = "#73556f"
SCLERA_SHADE = "#9b879e"
SCLERA = "#d1c6d2"
SCLERA_HI = "#eee8ed"
VEIN = "#77415f"
IRIS_RIM = "#25103f"
IRIS_DARK = "#3c1764"
IRIS = "#652b91"
IRIS_LIGHT = "#944bc2"
GLOW = "#d490f2"
PUPIL = "#09040f"
SPEC = "#f4d9ff"

# Soft hovering shadow, kept detached from the creature.
result.ellipse(32, 57, 18, 3, SHADOW)
result.ellipse(32, 57, 12, 2, SHADOW_CORE)
result.rect(22, 56, 21, 2, "#1d0d3855")

# Short curling tentacles, outlined first for a readable silhouette.
result.poly([(13,36),(8,40),(6,45),(7,50),(11,52),(15,50),(15,47),(12,48),(10,46),(11,42),(16,39)], OUT)
result.poly([(14,39),(10,42),(9,46),(10,49),(13,49),(13,47),(12,46),(13,42),(17,40)], FLESH_DARK)

result.poly([(21,43),(18,48),(18,53),(21,56),(25,55),(26,52),(24,51),(23,53),(21,51),(23,45)], OUT)
result.poly([(22,44),(20,48),(20,52),(22,54),(24,53),(22,51),(24,46)], FLESH)

result.poly([(29,45),(28,51),(30,56),(34,57),(37,54),(36,50),(34,49),(34,53),(32,54),(31,51),(33,46)], OUT)
result.poly([(31,46),(30,51),(32,55),(34,55),(35,53),(33,54),(32,51),(34,47)], FLESH_DARK)

result.poly([(40,44),(41,50),(39,53),(41,56),(45,56),(47,53),(46,50),(44,51),(45,47),(44,43)], OUT)
result.poly([(42,44),(43,49),(41,52),(42,54),(44,54),(45,52),(43,52),(44,48)], FLESH)

result.poly([(49,39),(53,41),(57,45),(57,49),(54,52),(50,51),(49,48),(52,49),(54,47),(53,44),(48,42)], OUT)
result.poly([(48,41),(52,43),(55,46),(55,48),(53,50),(51,49),(53,47),(52,45),(47,43)], FLESH_DARK)

# Main eye-body: angular outer carapace and thick lid rim.
result.poly([(7,27),(10,20),(16,15),(24,11),(34,10),(44,13),(52,18),(57,25),(57,33),(53,40),(46,45),(37,48),(27,48),(18,45),(11,40),(7,34)], OUT)
result.poly([(9,27),(12,21),(18,17),(25,13),(34,12),(43,15),(50,19),(55,26),(55,33),(51,38),(45,43),(36,46),(27,46),(19,43),(13,39),(9,33)], FLESH_DARK)

# Upper and lower lid masses.
result.poly([(11,27),(15,21),(23,16),(32,14),(42,16),(50,21),(54,27),(49,25),(42,22),(33,20),(24,21),(17,24)], FLESH)
result.poly([(10,31),(16,37),(24,41),(33,43),(42,41),(50,37),(55,31),(52,38),(45,43),(36,46),(27,45),(18,42),(12,37)], "#5d405f")
result.line(15,23,20,19,"#8b6c82")
result.line(44,18,50,23,"#8b6c82")
result.line(14,38,20,42,"#35233f")
result.line(45,42,51,37,"#35233f")

# Exposed sclera, intentionally faceted for pixel-art crispness.
result.poly([(11,29),(16,24),(24,21),(33,20),(42,22),(50,25),(54,30),(50,35),(42,40),(33,42),(24,40),(16,36)], SCLERA_SHADE)
result.poly([(14,29),(19,25),(26,23),(34,22),(42,24),(49,27),(52,30),(48,34),(41,38),(33,40),(25,38),(18,35)], SCLERA)
result.poly([(17,28),(22,25),(28,24),(27,27),(20,30),(17,32),(14,31)], SCLERA_HI)
result.poly([(40,25),(46,27),(50,30),(47,31),(43,29)], "#b6a7b8")
result.poly([(19,35),(25,38),(33,39),(29,37),(23,34)], "#b7a8b9")

# Veins curling inward from the corners.
result.line(13,30,19,30, VEIN)
result.line(18,30,22,27, VEIN)
result.set(17,31, "#9b526f")
result.line(16,35,22,34, VEIN)
result.line(20,34,23,36, VEIN)
result.line(51,30,46,30, VEIN)
result.line(47,30,44,27, VEIN)
result.line(49,34,44,34, VEIN)
result.line(45,34,42,37, VEIN)

# Deep purple iris: dark rim, jewel-like inner planes, and void pupil.
result.ellipse(33, 31, 11, 11, IRIS_RIM)
result.ellipse(33, 31, 9, 9, IRIS_DARK)
result.poly([(33,22),(38,24),(42,29),(40,35),(36,40),(30,40),(25,35),(24,29),(28,24)], IRIS)
result.poly([(29,24),(33,22),(33,28),(27,31),(25,29)], IRIS_LIGHT)
result.poly([(38,25),(41,29),(39,32),(35,28),(35,23)], "#7b37a8")
result.poly([(25,33),(29,30),(32,34),(31,40),(27,37)], "#4d1d78")
result.poly([(35,34),(40,32),(39,36),(35,40),(33,37)], "#55207e")

# Radial iris cuts.
for x0,y0,x1,y1 in [(33,23,33,27),(27,26,30,29),(25,31,29,31),(27,37,30,34),(33,39,33,35),(39,36,36,34),(41,30,37,30),(38,25,35,28)]:
    result.line(x0,y0,x1,y1,"#b05ad0")

# Faintly glowing pupil: glow ring, near-black core, tiny spectral glint.
result.ellipse(33, 31, 5, 6, GLOW)
result.ellipse(33, 31, 4, 5, "#6f378c")
result.ellipse(33, 31, 3, 5, PUPIL)
result.rect(31, 26, 2, 2, SPEC)
result.set(33, 27, "#c679e6")
result.set(35, 34, "#5d2878")

# Carapace chips and rim highlights make the scale legible at 1x.
result.rect(23,14,3,1,"#9a748d")
result.rect(39,16,3,1,"#8a657f")
result.rect(12,26,1,3,"#a27b92")
result.rect(51,27,1,3,"#3a2445")
result.set(18,18,"#a77d97")
result.set(47,20,"#b0889f")
result.set(17,40,"#87647b")
result.set(47,40,"#2b1938")

view(result, scale=8, margin=0)
finish(result)
