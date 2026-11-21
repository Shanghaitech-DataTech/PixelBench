# 48x48 RPG wooden magic staff on transparency.
result = new_canvas(48, 48, background=None, name="magic-staff")

# Compact palette.
outline = result.color("#24152d", "outline")
deep_wood = result.color("#4a241f", "deep_wood")
wood = result.color("#754025", "wood")
wood_mid = result.color("#9b5f31", "wood_mid")
wood_light = result.color("#c18447", "wood_light")
wood_glint = result.color("#e0a85c", "wood_glint")
purple_dark = result.color("#4a247e", "purple_dark")
purple = result.color("#7d3fc2", "purple")
violet = result.color("#a958ee", "violet")
lilac = result.color("#d68cff", "lilac")
spark = result.color("#f0c1ff", "spark")
glow = result.color("#a958ee80", "glow")

# Shaft outline, widening into a sturdy foot and branching into the head.
result.poly([(10,44),(11,39),(14,35),(15,30),(18,26),(19,21),(22,17),(27,18),
             (25,24),(22,28),(21,33),(18,37),(17,42),(15,46),(11,46)], outline)
# Main shaft body.
result.poly([(12,43),(13,39),(16,35),(17,30),(20,26),(21,21),(23,19),(25,19),
             (23,23),(20,28),(19,33),(16,37),(15,42),(14,44)], wood)
# Lit facing plane and lower carved facets.
result.poly([(15,41),(16,36),(19,32),(20,27),(22,23),(23,20),(25,19),(23,24),
             (21,29),(20,34),(17,38),(16,43),(14,44)], wood_mid)
result.line(17,35,19,30,wood_light)
result.line(20,27,22,23,wood_light)
result.set(16,38,wood_glint)
# Dark wood grain and carved grip marks.
result.line(12,40,15,39,deep_wood)
result.line(14,35,17,34,deep_wood)
result.line(17,29,20,29,deep_wood)
result.line(18,25,21,26,deep_wood)
result.set(13,42,wood_light)
result.set(15,37,wood_light)
result.set(18,32,wood_glint)
result.set(20,26,wood_glint)

# Large hooked head: dark silhouette first.
result.poly([(20,21),(20,16),(21,16),(20,11),(22,11),(22,8),(25,8),(25,6),
             (29,6),(29,4),(34,4),(34,5),(38,5),(38,7),(41,7),(41,10),
             (43,10),(43,15),(41,15),(41,18),(38,18),(38,21),(34,22),
             (31,20),(31,17),(35,17),(35,16),(38,16),(38,14),(40,14),
             (40,11),(38,11),(38,9),(34,9),(34,8),(30,8),(30,9),(27,9),
             (27,12),(25,12),(25,17),(24,17),(24,21)], outline)
# Warm wood inside the hook.
result.poly([(22,19),(22,15),(23,15),(22,12),(24,12),(24,9),(27,9),(27,7),
             (31,7),(31,6),(34,6),(34,7),(38,7),(38,9),(40,9),(40,12),
             (42,12),(41,15),(39,15),(39,18),(36,18),(36,20),(34,20),
             (33,19),(36,19),(36,17),(39,17),(39,15),(41,15),(41,11),
             (39,11),(39,9),(35,9),(35,8),(30,8),(30,10),(27,10),(27,13),
             (25,13),(25,18),(23,20)], wood)
# Head's highlighted upper ridge and inner shadow.
result.line(25,9,29,6,wood_mid)
result.line(29,6,34,6,wood_light)
result.line(35,7,38,8,wood_mid)
result.set(28,8,wood_glint)
result.set(32,6,wood_glint)
result.line(23,13,24,18,wood_mid)
result.line(26,11,26,16,deep_wood)
result.line(37,18,34,20,deep_wood)
result.set(39,10,wood_light)

# Suspended faceted amethyst in the curl.
result.set(33,10,glow)
result.set(32,11,glow)
result.set(38,12,glow)
result.set(37,16,glow)
result.poly([(34,10),(37,10),(39,13),(37,17),(34,18),(31,14)], purple_dark)
result.poly([(34,11),(36,11),(38,13),(36,16),(34,17),(32,14)], purple)
result.poly([(34,11),(36,12),(36,15),(34,17),(32,14)], violet)
result.poly([(34,11),(36,12),(34,14),(32,14)], lilac)
result.set(34,11,spark)
result.set(37,13,lilac)
result.set(35,16,purple_dark)

# Purple motes, sized and spaced to read as magical particles.
result.set(42,4,glow)
result.set(43,3,violet)
result.set(44,4,lilac)
result.set(43,5,purple)
result.set(17,10,glow)
result.set(18,9,lilac)
result.set(19,10,purple)
result.set(18,11,violet)
result.set(44,22,purple)
result.set(43,23,lilac)
result.set(44,24,violet)
result.set(7,27,purple_dark)
result.set(8,26,violet)
result.set(9,27,lilac)
result.set(8,28,purple)
# Tiny star specks.
result.set(13,17,lilac)
result.set(14,16,spark)
result.set(14,18,purple)
result.set(46,15,lilac)
result.set(29,1,violet)
result.set(5,34,purple)

view(result, scale=10, margin=1, edges="all")
save("magic-staff", result)
finish(result)
