# Polar researcher sprite, 48x48, transparent background.
result = new_canvas(48, 48, background=None, name="polar_researcher")

# Tight arctic palette.
outline = result.color("#17283b", "outline")
deep = result.color("#263e55", "deep_navy")
shadow = result.color("#36556b", "coat_shadow")
coat = result.color("#56788c", "coat")
coat_hi = result.color("#7798a8", "coat_highlight")
fur_dark = result.color("#8ea6ac", "fur_shadow")
fur = result.color("#c5d5d5", "fur")
snow = result.color("#e9f1ed", "snow_highlight")
goggle_dark = result.color("#28475d", "goggle_frame")
goggle = result.color("#9fd9e8", "goggle_reflection")
goggle_hi = result.color("#d5f5f6", "goggle_glint")
strap = result.color("#b5c6c5", "strap")
case_dark = result.color("#293b46", "case_outline")
case_mid = result.color("#48616a", "case")
case_hi = result.color("#6f8990", "case_highlight")
boot = result.color("#1e303c", "boot")
warning = result.color("#d89c42", "case_mark")

# Rear scarf tails, pulled hard to the right by wind.
result.poly([(28,11),(39,9),(37,12),(44,13),(35,15),(28,14)], outline)
result.poly([(29,12),(38,11),(35,13),(41,13),(34,14),(29,13)], coat_hi)
result.poly([(29,15),(40,17),(36,19),(44,21),(32,19),(27,17)], outline)
result.poly([(29,16),(38,18),(34,19),(40,20),(31,18)], coat)

# Back arm carrying the sample case.
result.poly([(27,24),(34,25),(37,31),(34,34),(30,31),(28,28)], outline)
result.poly([(29,25),(33,27),(35,31),(33,32),(30,30)], shadow)
# Case handle behind mitten.
result.rect(34,29,7,2,case_dark)
result.rect(36,28,4,2,case_dark)
result.rect(37,29,2,2,case_hi)

# Sample case, solid and readable.
result.poly([(33,31),(44,31),(45,42),(34,43),(32,40)], case_dark)
result.rect(34,33,9,8,case_mid)
result.rect(35,34,8,1,case_hi)
result.rect(35,35,1,5,case_hi)
result.rect(38,32,3,2,outline)
result.rect(36,37,5,3,deep)
result.rect(37,37,3,1,warning)
result.rect(38,36,1,3,warning)
result.set(42,40,case_dark)
# Mitten curled around handle.
result.rect(31,29,5,4,outline)
result.rect(31,29,3,3,coat_hi)
result.set(34,30,fur)

# Main forward-leaning parka torso.
result.poly([(18,17),(27,16),(32,20),(32,31),(28,38),(15,37),(12,32),(13,24)], outline)
result.poly([(19,18),(26,18),(30,21),(29,31),(26,35),(17,35),(14,31),(15,24)], coat)
# Windward shadow and blocky folds.
result.poly([(15,24),(19,22),(19,34),(16,34),(14,30)], shadow)
result.rect(20,19,6,2,coat_hi)
result.rect(26,22,3,8,coat_hi)
result.rect(18,33,9,2,deep)
result.rect(22,27,2,6,shadow)
result.rect(24,28,4,2,coat_hi)
# Parka hem and drawcord.
result.rect(15,35,13,3,outline)
result.rect(17,35,9,1,coat_hi)
result.set(16,38,strap)
result.set(27,38,strap)

# Front arm braced into wind, angled down-left.
result.poly([(17,20),(13,21),(10,27),(6,31),(8,35),(12,33),(14,29),(20,24)], outline)
result.poly([(16,22),(14,22),(12,27),(8,31),(9,33),(11,31),(13,27),(18,24)], coat_hi)
result.rect(6,31,5,4,outline)
result.rect(7,31,3,3,deep)
result.set(6,32,fur_dark)

# Hood, projecting forward and low.
result.poly([(12,7),(18,3),(25,4),(30,9),(30,16),(26,20),(18,20),(11,16),(8,12)], outline)
result.poly([(13,8),(18,5),(24,6),(28,10),(28,15),(25,18),(18,18),(12,15),(10,12)], fur_dark)
# Thick fur rim.
result.poly([(12,9),(17,5),(24,6),(28,10),(27,16),(23,19),(17,17),(11,14)], fur)
result.poly([(14,10),(18,7),(23,7),(26,10),(25,15),(22,17),(17,16),(13,13)], deep)
# Face opening shadow.
result.poly([(14,11),(18,8),(24,9),(26,12),(24,16),(18,16),(14,14)], shadow)

# Goggles: pale blue reflective band, clearly framed.
result.poly([(13,10),(18,8),(25,9),(27,11),(25,14),(18,14),(13,13)], goggle_dark)
result.poly([(15,10),(19,9),(24,10),(25,11),(24,13),(18,13),(15,12)], goggle)
result.rect(19,9,2,4,goggle_hi)
result.set(22,10,goggle_hi)
result.rect(11,11,3,1,strap)
# Lower face wrap and fur pixels.
result.poly([(16,14),(24,14),(23,17),(18,17),(15,16)], deep)
result.rect(18,14,5,1,coat_hi)
result.set(11,9,snow)
result.set(12,7,snow)
result.set(15,6,snow)
result.set(27,8,fur_dark)
result.set(29,12,fur)

# Legs separated in a planted, wind-braced stance.
# Forward leg reaches left.
result.poly([(16,37),(22,37),(20,41),(15,43),(10,43),(9,41),(13,39)], outline)
result.poly([(17,38),(20,38),(18,40),(14,42),(11,42),(14,40)], shadow)
# Rear leg leans right.
result.poly([(23,37),(28,37),(31,43),(29,46),(25,45),(24,41)], outline)
result.poly([(24,38),(27,38),(29,43),(28,44),(26,43)], coat)
# Heavy boots with broad soles.
result.poly([(9,41),(15,41),(17,43),(15,46),(7,46),(5,44),(6,42)], boot)
result.rect(6,45,10,2,outline)
result.rect(8,42,6,1,deep)
result.poly([(27,42),(31,42),(35,44),(34,47),(27,47),(25,45)], boot)
result.rect(27,46,8,1,outline)
result.rect(29,43,3,1,deep)

# A few sharp snow specks caught on the windward edges.
result.set(8,29,snow)
result.set(13,21,snow)
result.set(15,19,snow)
result.set(10,15,snow)

view(result, scale=10, margin=1, edges="all")
finish(result)
