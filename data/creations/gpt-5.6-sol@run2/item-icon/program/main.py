# Ancient golden compass inventory icon, 32x32.
result = new_canvas(32, 32, background=None, name="ancient_golden_compass")

outline = "#17131d"
outline_hi = "#2b2030"
shadow = "#5b3915"
bronze = "#8f5c1c"
gold = "#c98a28"
light_gold = "#f2c858"
pale_gold = "#ffe68a"
face = "#332a2c"
face_light = "#4a3931"
cream = "#f8df91"
blue_dark = "#10375d"
blue = "#176b9d"
blue_bright = "#31b9d5"
blue_glint = "#9cf3ee"

# Four directional crown points behind the case.
result.poly([(15,0),(19,5),(16,9),(12,5)], outline)
result.poly([(15,2),(17,5),(15,7),(14,5)], gold)
result.set(15,2,pale_gold)
result.poly([(31,15),(26,19),(22,16),(26,12)], outline)
result.poly([(29,15),(26,17),(24,15),(26,14)], gold)
result.poly([(15,31),(12,26),(15,22),(19,26)], outline)
result.poly([(15,29),(14,26),(16,24),(17,26)], bronze)
result.poly([(0,15),(5,12),(9,15),(5,19)], outline)
result.poly([(2,15),(5,14),(7,16),(5,17)], bronze)

# Stepped round case silhouette and raised gold bezel.
result.poly([(9,2),(21,2),(21,3),(25,3),(25,5),(28,5),(28,9),(30,9),(30,21),(28,21),(28,25),(25,25),(25,28),(21,28),(21,30),(9,30),(9,29),(5,29),(5,27),(2,27),(2,23),(0,23),(0,9),(2,9),(2,6),(5,6),(5,3),(9,3)], outline)
result.poly([(10,3),(20,3),(20,4),(24,4),(24,6),(27,6),(27,10),(29,10),(29,20),(27,20),(27,24),(24,24),(24,27),(20,27),(20,29),(10,29),(10,28),(6,28),(6,26),(3,26),(3,22),(2,22),(2,10),(4,10),(4,7),(7,7),(7,4),(10,4)], shadow)
result.poly([(10,4),(20,4),(20,5),(24,5),(24,7),(26,7),(26,10),(28,10),(28,20),(26,20),(26,24),(23,24),(23,27),(19,27),(19,28),(10,28),(10,27),(7,27),(7,25),(5,25),(5,22),(3,22),(3,11),(5,11),(5,8),(8,8),(8,5),(10,5)], gold)

# Upper-left light and lower-right aged shading on the rim.
result.line(9,5,20,5,light_gold)
result.line(6,8,9,5,light_gold)
result.line(4,11,4,20,light_gold)
result.set(5,9,pale_gold)
result.set(7,7,pale_gold)
result.line(8,26,19,26,bronze)
result.line(25,10,25,21,bronze)
result.line(22,25,25,22,bronze)
result.set(26,10,light_gold)

# Reassert a round stepped bezel over the angular shoulders.
result.circle(15,15,12,outline)
result.circle(15,15,11,shadow)
result.circle(15,15,10,gold)
# Uneven highlight and patina keep the old metal from looking flat.
result.line(9,6,20,6,light_gold)
result.line(6,9,6,19,light_gold)
result.line(9,25,20,25,bronze)
result.line(24,10,24,21,bronze)
result.set(8,7,pale_gold)
result.set(7,8,pale_gold)

# Recessed compass face and inner dark lip.
result.circle(15,15,9,outline)
result.circle(15,15,8,face)
# Subtle aged face quadrants.
result.poly([(7,14),(9,10),(14,7),(14,12),(11,15)], face_light)
result.poly([(16,18),(20,15),(23,15),(21,21),(16,23)], "#292329")

# Cardinal tick marks around the dial.
result.poly([(14,6),(16,6),(15,10)], pale_gold)
result.poly([(24,14),(24,16),(20,15)], light_gold)
result.poly([(14,24),(16,24),(15,20)], bronze)
result.poly([(6,14),(6,16),(10,15)], light_gold)
# Minor ticks.
for x,y in [(9,9),(21,9),(9,21),(21,21)]:
    result.set(x,y,gold)
result.set(10,8,cream)
result.set(20,8,gold)
result.set(8,20,bronze)
result.set(22,20,bronze)

# Long ornate needle, with a pale north tip and dark south tip.
result.poly([(15,7),(18,14),(16,15),(15,13),(14,15),(12,14)], outline)
result.poly([(15,8),(17,14),(15,12),(13,14)], cream)
result.set(15,8,pale_gold)
result.poly([(14,15),(15,17),(16,15),(18,22),(15,20),(12,22)], outline)
result.poly([(15,17),(17,21),(15,19),(13,21)], bronze)
# Horizontal needle crosspiece.
result.poly([(8,15),(13,13),(15,15),(13,17)], outline)
result.poly([(22,15),(17,17),(15,15),(17,13)], outline)
result.poly([(10,15),(14,14),(14,16)], gold)
result.poly([(20,15),(16,16),(16,14)], light_gold)

# Compact diamond crystal hub, outlined for UI readability.
result.poly([(15,11),(19,15),(15,19),(11,15)], outline)
result.poly([(15,12),(18,15),(15,18),(12,15)], blue)
result.poly([(15,12),(18,15),(15,15),(12,15)], blue_bright)
result.poly([(15,15),(18,15),(15,18)], blue_dark)
result.set(14,13,blue_glint)
result.set(13,14,"#65dbe3")

# Small metal nicks and glints suggest an old, handled artifact.
result.set(8,6,pale_gold)
result.set(6,12,"#e8ae3e")
result.set(23,7,"#a66c20")
result.set(27,18,"#714616")
result.set(20,27,"#6f4518")
result.set(4,23,"#a96f20")

view(result, scale=16, margin=0)
finish(result)
