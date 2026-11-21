from pixelbench_api import *

# 48x48 polar researcher sprite on transparency.
result = new_canvas(48, 48, background=None, name="polar_researcher")

# Compact cold-weather palette.
outline = "#172332"
deep = "#233747"
navy = "#2f4a5c"
coat = "#42677a"
coat_hi = "#5f8797"
coat_light = "#82a4ad"
fur_dark = "#756b61"
fur = "#b9aa94"
fur_hi = "#ded4c3"
goggle_frame = "#203241"
goggle = "#a9e6ef"
goggle_hi = "#e1fbff"
strap = "#151f2a"
mitten = "#314b59"
case_dark = "#26333a"
case = "#68777a"
case_hi = "#9eaaab"
metal = "#c5d4d3"
boot = "#19242c"
boot_hi = "#35464d"
snow = "#d7f0f2"

# Wind-blown hood/fur silhouette, leaning left.
result.poly([(10,8),(14,5),(21,5),(26,8),(29,13),(28,19),(24,22),(15,21),(10,17),(8,12)], outline)
result.poly([(12,8),(16,6),(21,7),(25,9),(27,13),(26,18),(23,20),(15,19),(11,16),(10,12)], fur_dark)
# Fur trim clusters.
result.poly([(10,9),(14,6),(20,6),(24,8),(27,12),(26,16),(23,14),(22,10),(18,8),(14,9),(12,13),(11,17),(9,14)], fur)
result.set(13,7,fur_hi).rect(16,6,4,1,fur_hi).set(22,8,fur_hi).set(25,11,fur_hi)
result.set(10,12,fur_hi).set(11,16,fur_hi).set(24,15,fur_hi)

# Shadowed face opening and large reflective goggles.
result.poly([(13,10),(18,8),(23,10),(25,13),(22,17),(16,17),(12,14)], deep)
result.rect(12,10,12,6,goggle_frame)
result.poly([(13,11),(18,10),(18,15),(13,15)], goggle)
result.poly([(19,10),(23,11),(23,14),(19,15)], goggle)
result.rect(14,11,4,1,goggle_hi).rect(20,11,3,1,goggle_hi)
result.set(13,14,"#6faebb").set(19,14,"#6faebb")
result.rect(11,11,2,2,strap).rect(24,12,2,2,strap)
# Scarf and windward collar.
result.poly([(14,17),(24,16),(27,20),(24,24),(15,23),(11,20)], outline)
result.poly([(15,18),(23,17),(25,20),(23,22),(16,22),(12,20)], coat_hi)
result.line(15,21,23,20,coat_light)

# Main parka, strongly leaning forward.
result.poly([(15,21),(25,19),(32,24),(34,33),(29,37),(18,35),(12,29)], outline)
result.poly([(16,22),(24,20),(30,24),(32,32),(28,35),(19,33),(14,29)], coat)
# Back shadow and padded panel divisions.
result.poly([(25,21),(30,24),(32,32),(28,35),(26,29)], navy)
result.line(16,25,29,23,coat_hi)
result.line(17,29,31,28,deep)
result.line(19,33,30,32,deep)
result.rect(16,23,5,2,coat_hi)
result.set(15,26,coat_light).set(16,26,coat_hi).set(18,30,coat_hi)
# Wind-flapped coat hem.
result.poly([(18,33),(30,33),(29,38),(25,37),(23,39),(20,37),(17,38),(15,35)], outline)
result.poly([(19,34),(28,34),(27,36),(24,35),(23,37),(20,35),(18,36),(17,35)], coat)

# Forward arm reaching into wind (left).
result.poly([(16,22),(12,21),(7,25),(3,29),(5,32),(10,29),(15,27),(19,25)], outline)
result.poly([(15,23),(12,23),(8,26),(5,29),(6,30),(10,27),(15,26),(18,24)], coat_hi)
result.line(8,27,12,29,coat_light)
# Forward mitten.
result.poly([(5,28),(2,29),(1,32),(3,34),(6,33),(8,30)], outline)
result.poly([(5,29),(3,30),(3,32),(5,32),(7,30)], mitten)

# Rear arm down to sample case.
result.poly([(29,24),(34,25),(36,31),(36,35),(32,36),(30,31),(27,28)], outline)
result.poly([(29,25),(33,26),(34,31),(35,34),(33,34),(31,30),(28,27)], navy)
result.set(33,28,coat_hi).set(34,29,coat_hi)
# Rear mitten gripping handle.
result.poly([(34,33),(37,33),(39,35),(38,38),(34,37),(32,35)], outline)
result.rect(34,34,3,3,mitten)

# Sample case handle and case, carried low behind.
result.rect(36,35,8,2,case_dark)
result.rect(38,34,5,2,outline)
result.rect(39,35,3,1,metal)
result.poly([(36,37),(45,37),(47,40),(46,47),(34,47),(33,40)], outline)
result.poly([(36,38),(44,38),(45,40),(45,45),(35,45),(35,40)], case)
result.rect(36,39,9,1,case_hi)
result.rect(39,38,2,7,case_dark)
result.rect(40,40,1,2,metal)
result.rect(35,44,10,1,"#4b5b5e")
result.set(36,38,metal).set(44,39,metal).set(36,45,case_hi)

# Legs in a braced, offset stance.
result.poly([(19,35),(25,35),(25,41),(22,45),(15,45),(15,42)], outline)
result.poly([(20,36),(23,36),(23,40),(20,43),(17,43),(17,41)], deep)
result.line(18,38,23,38,navy)
result.poly([(26,35),(31,34),(34,40),(34,44),(27,44),(26,40)], outline)
result.poly([(27,36),(30,36),(32,40),(32,42),(29,42),(28,39)], navy)
result.set(29,37,coat_hi).set(31,40,deep)

# Heavy insulated boots with broad soles.
result.poly([(14,42),(21,42),(23,44),(22,47),(10,47),(9,45)], boot)
result.poly([(10,44),(18,44),(20,45),(19,46),(11,46)], boot_hi)
result.rect(9,46,13,2,outline)
result.poly([(29,41),(35,41),(39,44),(39,47),(27,47),(26,45)], boot)
result.poly([(30,43),(34,43),(37,45),(29,45)], boot_hi)
result.rect(27,46,12,2,outline)

# Wind-driven snow flecks emphasize direction without filling the background.
result.line(1,8,6,8,snow)
result.line(3,13,8,13,"#9dcdd3")
result.line(0,19,5,19,snow)
result.line(2,23,4,23,"#9dcdd3")
result.line(1,39,5,39,snow)
result.set(7,5,"#9dcdd3").set(4,16,snow).set(8,36,"#9dcdd3")

view(result, scale=10, margin=1, edges="all")
finish(result)
