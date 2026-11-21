# Summer seaside scene, 128x128 pixel art.
result = new_canvas(128, 128, background="#77d7f2", name="summer-seaside")

# Palette
sky = "#77d7f2"
sky_light = "#9ee8f7"
white = "#fff9df"
cloud_shadow = "#d9eef0"
sun = "#ffe35a"
sun_hi = "#fff39a"
horizon = "#1769a8"
deep = "#197bb9"
mid = "#18a8c2"
teal = "#29c7c2"
sea_light = "#74e0d1"
foam = "#f7fff1"
foam_shadow = "#ccefe2"
sand = "#f6c968"
sand_light = "#ffdc83"
sand_dark = "#d99d45"
red = "#e4433f"
red_dark = "#b82f35"
navy = "#174c70"
towel_blue = "#2f85bd"
towel_light = "#f7f1d0"
flip = "#ef5b45"
flip_dark = "#a93836"

# Sky subtle horizontal light near horizon.
result.rect(0, 39, 128, 9, sky_light)
result.rect(0, 46, 128, 3, "#b9eff4")

# Sun with crisp pixel halo and bright core.
result.rect(102, 8, 9, 2, sun_hi)
result.rect(98, 12, 17, 2, sun)
result.rect(95, 15, 23, 10, sun)
result.rect(98, 25, 17, 3, sun)
result.rect(102, 28, 9, 2, sun_hi)
result.rect(99, 17, 15, 7, "#ffe968")

# Soft blocky clouds.
result.rect(7, 16, 31, 6, white)
result.rect(11, 12, 9, 5, white)
result.rect(19, 9, 12, 10, white)
result.rect(29, 13, 12, 8, white)
result.rect(10, 22, 28, 2, cloud_shadow)
result.rect(51, 27, 30, 5, white)
result.rect(56, 23, 10, 6, white)
result.rect(64, 20, 9, 10, white)
result.rect(73, 24, 12, 7, white)
result.rect(55, 32, 26, 2, cloud_shadow)

# Two flying gulls.
result.line(48, 14, 52, 12, navy)
result.line(52, 12, 56, 15, navy)
result.set(52, 13, navy)
result.line(78, 10, 81, 8, navy)
result.line(81, 8, 85, 10, navy)

# Sea bands: deep horizon to turquoise shore.
result.rect(0, 49, 128, 8, horizon)
result.rect(0, 57, 128, 9, deep)
result.rect(0, 66, 128, 9, mid)
result.rect(0, 75, 128, 10, teal)
result.rect(0, 83, 128, 10, sea_light)

# Distant sea glints and broken wave lines.
for x, y, w, col in [
    (4,53,15,"#4ca9d2"),(27,51,8,"#4ca9d2"),(72,54,14,"#55b7d8"),(96,52,20,"#55b7d8"),
    (14,61,18,"#50c6d4"),(42,64,10,"#6bd3dc"),(66,60,19,"#55bfd3"),(102,63,13,"#6bd3dc"),
    (1,70,12,"#73d8d5"),(24,72,20,"#67d9d5"),(56,69,12,"#7ee0dc"),(85,73,27,"#64d5d2")]:
    result.rect(x, y, w, 2, col)

# Small sailboat far out.
result.line(91, 39, 91, 55, navy)
result.poly([(90,40),(90,52),(81,52)], white)
result.poly([(93,43),(93,52),(100,52)], "#ffe8b5")
result.rect(82, 53, 18, 2, red_dark)
result.rect(85, 55, 12, 1, navy)

# Rolling white surf with stepped scallops.
result.poly([(0,82),(10,80),(18,82),(27,79),(39,82),(49,80),(60,83),(72,79),(84,81),(96,78),(108,81),(118,79),(127,80),(127,92),(0,92)], foam)
result.rect(0, 88, 128, 5, foam)
result.rect(7, 92, 17, 2, foam_shadow)
result.rect(30, 90, 14, 3, foam_shadow)
result.rect(54, 93, 22, 2, foam_shadow)
result.rect(88, 89, 18, 3, foam_shadow)
result.rect(112, 92, 13, 2, foam_shadow)
result.rect(2, 85, 9, 2, white)
result.rect(43, 84, 12, 2, white)
result.rect(78, 83, 9, 2, white)
result.rect(106, 84, 16, 2, white)

# Golden sand foreground.
result.rect(0, 95, 128, 33, sand)
result.poly([(0,95),(19,94),(31,97),(49,94),(63,96),(82,93),(98,96),(113,94),(127,95),(127,100),(0,100)], sand_light)
# Wet sand accents and scattered grains.
result.rect(4,99,18,2,"#edba59")
result.rect(31,101,12,2,sand_light)
result.rect(72,98,21,2,"#edba59")
result.rect(107,102,14,2,sand_light)
for x, y in [(8,112),(14,122),(25,104),(45,116),(55,108),(64,124),(76,113),(91,105),(104,119),(119,110),(35,126),(113,125)]:
    result.rect(x,y,2,1,sand_dark)
for x, y in [(3,118),(20,115),(31,110),(51,124),(67,105),(82,121),(97,114),(122,119)]:
    result.set(x,y,sand_light)

# Umbrella pole and cast shadow.
result.poly([(15,116),(48,113),(52,116),(19,120)], "#d49c4a")
result.rect(33,62,3,51, white)
result.rect(35,62,2,51, "#c9b99a")
result.rect(31,111,9,3, navy)

# Red-and-white striped umbrella canopy, outlined for readability.
result.poly([(7,61),(12,53),(19,47),(29,43),(39,44),(49,49),(57,58),(58,62),(7,62)], navy)
result.poly([(9,59),(14,52),(21,48),(29,45),(38,46),(47,50),(55,59)], white)
result.poly([(9,59),(20,48),(26,46),(24,59)], red)
result.poly([(24,59),(30,45),(37,46),(40,59)], white)
result.poly([(40,59),(39,46),(47,50),(55,59)], red)
# Canopy lower scallops.
result.rect(9,59,15,4, red_dark)
result.rect(24,59,16,4, white)
result.rect(40,59,16,4, red_dark)
result.rect(12,62,9,2, red_dark)
result.rect(28,62,8,2, white)
result.rect(45,62,8,2, red_dark)
result.rect(33,45,3,17, red_dark)

# Striped towel in perspective on the sand.
result.poly([(69,102),(104,101),(116,122),(76,124)], navy)
result.poly([(71,101),(103,101),(113,120),(77,122)], towel_light)
result.poly([(76,102),(83,102),(88,121),(80,121)], towel_blue)
result.poly([(90,102),(98,102),(107,120),(98,121)], towel_blue)
# Towel fringe.
for x in [78,84,91,98,105,111]:
    result.line(x,121,x,124,navy)

# Flip-flops beside towel, each with a dark sole and bright straps.
result.poly([(53,107),(58,105),(63,108),(63,117),(59,121),(54,119),(52,113)], flip_dark)
result.poly([(54,107),(58,106),(62,109),(61,116),(58,119),(54,117),(53,112)], flip)
result.line(55,110,58,113,white)
result.line(61,109,58,113,white)
result.poly([(61,101),(66,100),(70,104),(69,113),(65,116),(61,113),(59,106)], flip_dark)
result.poly([(62,102),(66,101),(69,104),(68,111),(65,114),(62,112),(60,106)], "#ff7354")
result.line(62,105,65,108,white)
result.line(68,104,65,108,white)

# A few foreground shell-like highlights.
result.rect(44,103,4,2, white)
result.set(46,102,white)
result.rect(119,116,5,2, white)
result.set(121,115,white)

view(result, scale=4, margin=0)
finish(result)
