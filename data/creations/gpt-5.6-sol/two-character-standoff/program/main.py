from pixelbench_api import new_canvas, view, finish

# Two rivals at dusk, rendered with a deliberately small, reusable palette.
c = new_canvas(128, 128, background="#111426", name="two-character-standoff")

# Palette
sky0 = "#111426"; sky1 = "#191a31"; sky2 = "#25203a"; sky3 = "#36253e"
haze = "#593044"; ember = "#b64b45"; moon = "#f0b56b"; moon_hi = "#ffd98a"
ink = "#090b15"; outline = "#15101b"; ground = "#171622"; ground2 = "#24202b"
red0 = "#3a1823"; red1 = "#67202b"; red2 = "#9c2d32"; red3 = "#d64a3c"; red4 = "#f06a4d"; red_hi = "#ff9a68"
steel0 = "#41455a"; steel1 = "#74798d"; steel2 = "#b7b9c3"; steel3 = "#ece1d5"
skin0 = "#7e3c35"; skin1 = "#c87556"; skin2 = "#f0ae75"; hair = "#241421"
green0 = "#142b29"; green1 = "#1e4938"; green2 = "#2d7047"; green3 = "#4e9a57"; green4 = "#82c46a"; mint = "#b8dc86"
brown = "#513326"; gold0 = "#7d4b27"; gold1 = "#d28a3e"; gold2 = "#ffd06a"

# Banded night sky and horizon haze.
c.rect(0, 22, 128, 23, sky1)
c.rect(0, 45, 128, 20, sky2)
c.rect(0, 65, 128, 19, sky3)
c.rect(0, 84, 128, 20, haze)
c.dither(0, 34, 128, 16, [sky1, sky2], pattern="bayer4")
c.dither(0, 61, 128, 15, [sky2, sky3], pattern="checker")
c.dither(0, 79, 128, 13, [sky3, haze], pattern="bayer4")

# Sunset disc in the open central gap, partially veiled by cloud strips.
c.circle(64, 51, 12, moon)
c.rect(54, 48, 21, 3, moon_hi)
c.rect(53, 53, 23, 3, ember)
c.rect(55, 57, 19, 2, haze)
c.rect(7, 38, 24, 2, sky3); c.rect(17, 36, 22, 2, sky3)
c.rect(87, 41, 29, 2, sky3); c.rect(97, 39, 18, 2, sky3)
# Sparse stars / sparks.
for x, y in [(8,15),(17,25),(48,18),(70,13),(93,20),(116,12),(103,30),(58,28)]:
    c.set(x,y,moon_hi)
c.set(16,24,moon); c.set(94,19,moon)

# Distant broken skyline, kept low contrast.
c.poly([(0,81),(0,71),(7,71),(7,76),(13,76),(13,67),(19,67),(19,78),(25,78),(25,72),(31,72),(31,88)], sky1)
c.poly([(96,86),(96,73),(101,73),(101,67),(106,67),(106,76),(112,76),(112,62),(117,62),(117,75),(123,75),(123,69),(127,69),(127,88)], sky1)

# Ground and reflected sunset path.
c.rect(0, 101, 128, 27, ground)
c.dither(0, 101, 128, 9, [ground, ground2], pattern="checker")
c.poly([(55,101),(73,101),(84,127),(43,127)], "#382229")
c.dither(47, 105, 34, 23, ["#382229", "#4b282e"], pattern="bayer4")
c.rect(0,112,37,2,ink); c.rect(86,113,42,2,ink)
c.rect(9,121,29,2,outline); c.rect(91,123,27,2,outline)

# KNIGHT: wind-torn cape behind the armor.
c.poly([(19,55),(13,67),(11,88),(5,104),(17,101),(20,112),(29,103),(34,78),(31,58)], outline)
c.poly([(20,58),(16,69),(16,87),(10,100),(20,96),(22,105),(28,98),(31,76),(29,60)], red0)
c.poly([(18,62),(17,81),(14,94),(20,91),(23,100),(25,79),(28,65)], red1)
c.rect(15,78,3,13,red3)

# Knight rear plume, helmet and anime face opening.
c.poly([(25,35),(19,28),(22,20),(27,25),(30,17),(34,28),(31,38)], outline)
c.poly([(26,34),(22,28),(24,23),(28,28),(30,22),(31,35)], red3)
c.poly([(24,30),(22,40),(25,49),(34,54),(43,48),(45,36),(39,28)], outline)
c.poly([(27,31),(25,39),(27,47),(34,51),(40,47),(42,37),(38,31)], red2)
# Helmet crown and cheek guards.
c.poly([(25,32),(29,25),(39,26),(44,32),(42,38),(26,38)], red3)
c.poly([(29,27),(38,28),(41,31),(31,31)], red4)
c.rect(25,37,18,4,red1)
c.poly([(26,39),(29,49),(33,51),(31,41)], red3)
c.poly([(42,38),(41,48),(37,51),(38,41)], red1)
# Face slit.
c.poly([(31,36),(41,35),(39,42),(32,43)], skin1)
c.rect(33,36,7,2,skin2)
c.rect(36,39,4,2,hair); c.set(39,39,red_hi)
c.rect(32,43,7,2,skin0)

# Knight torso and massive near pauldron.
c.poly([(27,50),(20,58),(19,76),(24,94),(43,96),(52,81),(50,61),(42,50)], outline)
c.poly([(30,51),(23,58),(23,74),(27,91),(41,92),(48,79),(47,61),(40,52)], red1)
c.poly([(31,54),(40,53),(45,60),(43,78),(39,88),(29,86),(26,72),(27,59)], red2)
c.poly([(31,56),(39,55),(42,61),(40,78),(36,84),(30,82),(28,69)], red3)
c.poly([(20,52),(14,56),(11,65),(16,72),(27,70),(31,60),(28,53)], outline)
c.poly([(20,55),(15,58),(14,64),(18,68),(25,67),(28,60),(26,55)], red3)
c.rect(16,58,9,3,red4); c.rect(18,61,8,2,red_hi)
# Chest plate graphic and belts.
c.poly([(34,56),(40,59),(39,73),(34,80),(29,72),(29,60)], red4)
c.poly([(34,60),(38,62),(36,72),(33,75),(31,70),(31,62)], red2)
c.rect(23,77,24,4,outline); c.rect(25,78,20,2,gold0); c.rect(34,77,5,4,gold1)

# Knight sword arm, gauntlet, and blade aiming into the gap.
c.poly([(43,57),(50,55),(57,60),(57,67),(49,70),(44,65)], outline)
c.poly([(45,58),(49,58),(54,61),(54,65),(49,67),(45,64)], red3)
c.rect(51,61,8,7,outline); c.rect(52,62,6,5,steel1)
c.poly([(56,62),(61,60),(64,62),(60,65)], gold1)
c.poly([(58,60),(72,47),(75,47),(62,64)], steel3)
c.poly([(61,60),(72,49),(73,49),(62,62)], steel1)
c.set(71,50,steel3); c.set(70,51,steel3)

# Knight legs and boots.
c.poly([(26,88),(35,89),(36,106),(31,119),(20,119),(21,113),(27,107)], outline)
c.poly([(28,91),(33,92),(33,105),(28,113),(23,114),(29,105)], red2)
c.rect(20,114,14,6,outline); c.rect(21,114,11,3,red1)
c.poly([(36,89),(45,88),(51,106),(49,119),(38,119),(37,113),(42,106)], outline)
c.poly([(39,92),(43,92),(48,106),(46,114),(40,114),(44,106)], red1)
c.rect(38,114,13,6,outline); c.rect(40,114,9,3,red2)
# Armor glints.
c.rect(27,65,2,9,red_hi); c.rect(30,52,8,2,red4); c.set(23,84,red4); c.set(44,83,red4)

# ROGUE: long cloak and wind-swept scarf, silhouette first.
c.poly([(96,47),(106,45),(111,50),(117,48),(114,54),(123,57),(113,61),(119,67),(106,65),(99,59)], outline)
c.poly([(100,49),(106,48),(110,52),(115,51),(111,55),(118,58),(109,59),(114,63),(105,62),(100,57)], green2)
c.poly([(112,51),(116,50),(113,54)], green4)

# Hood, face, and trailing pointed tip.
c.poly([(91,31),(101,25),(111,29),(117,39),(112,53),(99,57),(88,50),(83,40)], outline)
c.poly([(92,34),(101,28),(108,31),(113,39),(109,49),(100,53),(91,49),(87,41)], green1)
c.poly([(94,33),(103,29),(109,34),(111,40),(103,38),(94,41),(88,40)], green3)
c.poly([(89,38),(83,32),(86,43)], outline); c.poly([(89,37),(85,34),(87,42)], green2)
# Face in deep hood.
c.poly([(94,39),(108,38),(106,47),(99,51),(93,47)], skin0)
c.poly([(96,40),(106,40),(105,45),(99,47),(95,45)], skin1)
c.rect(96,40,11,2,hair); c.rect(96,42,4,2,hair); c.rect(103,41,3,2,mint)
c.set(104,41,steel3); c.rect(99,47,6,2,outline)

# Rogue crouched torso and layered cloak.
c.poly([(91,50),(80,58),(77,75),(85,87),(104,86),(115,72),(111,55),(105,50)], outline)
c.poly([(93,52),(84,59),(81,73),(87,82),(102,82),(111,70),(108,55),(103,52)], green1)
c.poly([(96,52),(86,61),(84,72),(90,79),(102,78),(108,68),(106,55)], green2)
c.poly([(101,53),(106,56),(105,67),(98,77),(91,77),(87,71),(88,62),(94,56)], green3)
# Cloak folds and clasp.
c.circle(95,56,3,gold1); c.set(95,55,gold2)
c.poly([(88,60),(82,73),(87,81),(92,77),(91,64)], green4)
c.poly([(105,58),(109,68),(102,79),(98,77),(103,64)], green1)
c.line(95,59,95,76,mint)

# Rogue forward arm and dagger into the center, leaving body gap.
c.poly([(88,58),(79,59),(70,66),(72,72),(82,69),(94,65)], outline)
c.poly([(88,61),(81,62),(74,67),(75,69),(82,66),(92,63)], green2)
c.rect(70,65,7,7,outline); c.rect(72,66,5,5,brown)
c.poly([(71,67),(65,68),(62,71),(69,70)], gold1)
c.poly([(66,68),(56,66),(54,68),(65,71)], steel3)
c.poly([(64,69),(56,67),(58,69)], steel1)
# Back hand and reverse blade.
c.poly([(107,67),(115,70),(118,77),(113,80),(105,73)], outline)
c.poly([(108,69),(113,72),(115,76),(112,77),(107,72)], green3)
c.rect(112,75,7,5,brown)
c.poly([(118,76),(123,72),(125,73),(120,79)], steel2)

# Rogue legs: wide, low stance.
c.poly([(88,79),(99,80),(97,95),(87,108),(76,108),(76,102),(84,94)], outline)
c.poly([(89,82),(96,83),(93,92),(85,104),(79,104),(87,92)], green0)
c.rect(74,104,15,7,outline); c.rect(77,104,11,3,brown)
c.poly([(100,79),(109,77),(114,91),(121,102),(119,109),(107,108),(106,103),(109,98),(102,92)], outline)
c.poly([(102,82),(107,81),(111,91),(117,102),(116,105),(110,104),(112,99),(106,92)], green1)
c.rect(107,104,14,7,outline); c.rect(110,104,9,3,brown)
# Green highlights.
c.rect(86,68,2,6,mint); c.rect(99,31,7,2,green4); c.set(106,52,mint); c.set(91,80,green4)

# Contact shadows and a few airborne embers emphasize the central pause.
c.rect(13,119,42,4,ink); c.rect(72,109,50,4,ink)
for x,y,col in [(61,78,red4),(67,83,gold2),(59,91,ember),(71,95,moon),(64,99,gold1),(53,87,red3),(75,58,mint)]:
    c.set(x,y,col)
c.rect(63,76,2,2,gold2); c.set(64,75,moon_hi)

view(c, scale=4, margin=0)
finish(c)
