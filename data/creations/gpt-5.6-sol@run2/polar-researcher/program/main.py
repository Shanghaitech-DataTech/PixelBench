# Polar researcher sprite, 48x48, transparent background.
result = new_canvas(48, 48, background=None, name="polar_researcher")

# Palette
outline = "#172536"
deep = "#21384a"
shadow = "#2d4d60"
coat = "#3f7183"
coat_hi = "#5e93a1"
ice = "#9fd6df"
glint = "#d9f6f4"
fur_dark = "#8a735c"
fur = "#c2aa84"
fur_hi = "#ead7ae"
strap = "#604d45"
case_dark = "#394955"
case_mid = "#687b84"
case_light = "#9aadb2"
accent = "#e08b45"
boot = "#24313b"

# Wind streaks / blown snow, sparse and disconnected.
result.line(2, 8, 7, 8, ice)
result.set(5, 7, glint)
result.line(0, 15, 5, 15, ice)
result.line(3, 16, 8, 16, ice)
result.line(37, 4, 42, 4, ice)
result.set(44, 5, glint)
result.line(38, 38, 44, 38, ice)
result.set(41, 37, glint)

# Scarf tails whipping left.
result.poly([(24,15),(18,15),(13,12),(7,12),(7,14),(13,15),(18,19),(24,19)], outline)
result.poly([(22,16),(17,16),(12,14),(9,14),(14,16),(18,18),(23,18)], accent)
result.poly([(23,18),(17,20),(10,19),(5,21),(12,22),(18,22),(25,20)], outline)
result.poly([(21,19),(17,21),(11,20),(8,21),(13,21),(18,21),(24,19)], "#b85f38")

# Backpack behind the torso.
result.poly([(19,18),(13,20),(11,27),(13,33),(19,34),(22,29),(22,20)], outline)
result.poly([(18,20),(14,21),(13,27),(14,31),(19,32),(20,28),(20,21)], shadow)
result.rect(13,24,2,5,coat_hi)
result.rect(14,31,5,2,deep)

# Rear arm holding sample case.
result.poly([(20,22),(17,23),(14,28),(11,30),(12,34),(16,33),(19,29),(23,27)], outline)
result.poly([(20,24),(18,24),(16,29),(13,31),(14,32),(16,31),(19,27),(22,26)], coat)
result.set(18,25,coat_hi)
# Mitten and case handle.
result.poly([(13,29),(10,29),(9,31),(10,34),(14,34),(16,32)], outline)
result.rect(11,30,3,3,fur_dark)
result.rect(7,31,5,2,outline)
result.rect(8,32,2,3,case_dark)
# Sample case, angled blocky silhouette.
result.poly([(3,33),(11,33),(14,35),(14,43),(12,45),(3,45),(1,43),(1,35)], outline)
result.poly([(4,35),(10,35),(12,36),(12,42),(10,43),(3,43),(3,36)], case_mid)
result.rect(4,36,7,2,case_light)
result.rect(5,39,2,2,accent)
result.rect(8,39,3,1,deep)
result.set(11,42,case_dark)
result.rect(5,32,4,2,case_dark)

# Legs: bent and planted, leaning into wind.
# Back leg.
result.poly([(22,31),(28,31),(28,35),(24,39),(21,44),(16,44),(15,42),(19,38)], outline)
result.poly([(23,33),(26,33),(25,35),(22,39),(20,42),(17,42),(21,36)], shadow)
# Back boot.
result.poly([(16,41),(21,41),(22,44),(20,46),(12,46),(11,44)], outline)
result.poly([(14,43),(20,43),(20,44),(13,44)], boot)
# Front leg thrust forward.
result.poly([(27,31),(33,31),(34,36),(37,40),(36,44),(31,44),(30,40),(27,37)], outline)
result.poly([(29,33),(32,33),(32,36),(35,40),(34,42),(32,42),(31,39),(29,36)], coat)
result.set(32,34,coat_hi)
# Front boot, toe points right.
result.poly([(32,41),(37,41),(39,43),(45,44),(46,46),(43,47),(34,46),(31,44)], outline)
result.poly([(35,43),(38,43),(40,45),(44,45),(43,46),(35,45)], boot)
result.rect(40,44,3,1,case_mid)

# Main parka, strongly slanted to the right.
result.poly([(22,17),(29,16),(35,20),(36,27),(34,34),(27,36),(20,32),(19,25)], outline)
result.poly([(24,19),(29,18),(33,21),(34,27),(32,32),(27,34),(22,31),(21,25)], coat)
# Shadow and lit windward edge.
result.poly([(21,25),(25,25),(27,34),(22,31)], shadow)
result.poly([(30,19),(33,22),(34,28),(32,31),(31,25)], coat_hi)
result.rect(27,19,2,14,deep)
result.rect(28,20,1,11,accent)
result.rect(23,28,3,2,coat_hi)
result.rect(25,33,7,2,deep)

# Forward arm bracing into wind.
result.poly([(31,20),(35,20),(38,24),(42,25),(43,29),(40,32),(37,29),(34,28),(31,25)], outline)
result.poly([(34,22),(36,23),(38,26),(41,26),(41,29),(39,29),(37,27),(35,27),(33,24)], coat)
result.set(36,23,coat_hi)
# Large mitten.
result.poly([(40,25),(44,24),(47,26),(47,30),(44,32),(40,30)], outline)
result.poly([(42,26),(44,26),(46,27),(45,30),(42,29)], fur_dark)
result.set(44,27,fur)

# Hood silhouette and fur ruff.
result.poly([(20,8),(23,4),(30,3),(36,6),(39,11),(38,17),(34,21),(27,20),(22,17),(19,13)], outline)
result.poly([(22,9),(24,6),(30,5),(34,7),(37,11),(36,16),(33,18),(27,18),(23,16),(21,12)], coat)
result.set(25,6,coat_hi)
result.line(23,7,21,12,coat_hi)
# Fur ring around face.
result.poly([(25,7),(31,6),(35,9),(36,13),(33,17),(27,17),(23,14),(23,10)], fur_dark)
result.poly([(26,8),(31,7),(34,10),(34,14),(32,16),(27,15),(24,13),(25,10)], fur)
# blocky fur tufts
result.set(24,9,fur_hi); result.set(26,7,fur_hi); result.set(32,8,fur_hi)
result.set(35,11,fur_hi); result.set(34,15,fur_hi); result.set(27,16,fur_hi)

# Face shadow / balaclava opening.
result.poly([(27,9),(32,9),(34,11),(33,14),(31,15),(27,14),(25,12)], deep)
result.set(32,14,fur_dark)
# Pale blue goggles with thick bridge and reflection.
result.poly([(25,10),(29,9),(34,10),(35,12),(33,14),(27,13),(24,12)], outline)
result.poly([(26,10),(29,10),(29,12),(26,12)], ice)
result.poly([(31,10),(34,11),(33,13),(30,12)], "#73b8c7")
result.set(27,10,glint)
result.set(32,10,glint)
result.set(34,12,ice)
result.set(30,11,outline)
# Goggle strap.
result.line(24,11,22,11,strap)
result.line(35,11,36,12,strap)

# Hood seam and snow highlights.
result.line(29,5,33,7,coat_hi)
result.set(36,9,ice)
result.set(22,14,ice)
result.set(34,18,ice)

# Small parka details and snow catchlights.
result.rect(29,25,2,1,case_light)
result.set(33,29,ice)
result.set(20,28,ice)
result.set(29,35,ice)
result.set(14,27,ice)

view(result, scale=10, margin=1, edges="all")
finish(result)
