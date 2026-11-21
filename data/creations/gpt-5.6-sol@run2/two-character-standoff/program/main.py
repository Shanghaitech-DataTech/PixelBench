# 128x128 anime-style rival standoff
# Astra Pixel Art API objects are preloaded.

W, H = 128, 128
c = new_canvas(W, H, background="#130f1d", name="two_rivals_standoff")

# Compact hand-picked palette.
sky0 = "#130f1d"
sky1 = "#241426"
sky2 = "#3b1827"
sky3 = "#672333"
sky4 = "#a13b3b"
sunset = "#e87845"
glow = "#f2ad66"
cloud_dark = "#291522"
cloud_mid = "#4a1d2a"
ruin_far = "#211a27"
ruin_near = "#17151c"
ground = "#121319"
ground_hi = "#292027"
outline = "#0b0c12"
ink = "#111018"
metal_dark = "#391a24"
red_dark = "#641f2b"
red = "#a62b35"
red_hi = "#e34a42"
red_light = "#ff7960"
steel = "#9aa1a6"
steel_hi = "#d9d9cf"
steel_shadow = "#5c6069"
skin = "#e7ae8d"
skin_hi = "#ffd0a4"
hair = "#321927"
green_black = "#13231e"
green_dark = "#1e3d2d"
green = "#2f6b43"
green_mid = "#4c9857"
green_hi = "#83c566"
leather = "#57362a"
leather_hi = "#8f5c3b"
gold = "#d49b42"
eye = "#efff8e"

# Sky bands, stepped for intentional pixel-art depth.
c.rect(0, 0, 128, 22, sky0)
c.rect(0, 22, 128, 17, sky1)
c.rect(0, 39, 128, 18, sky2)
c.rect(0, 57, 128, 18, sky3)
c.rect(0, 75, 128, 17, sky4)
c.rect(0, 86, 128, 9, sunset)
# Keep the central air open; the horizontal sunset band supplies the backlight.
# Pixel clouds.
c.poly([(0,32),(14,32),(14,29),(28,29),(28,33),(40,33),(40,38),(20,38),(20,40),(0,40)], cloud_dark)
c.poly([(84,24),(99,24),(99,27),(116,27),(116,31),(128,31),(128,37),(105,37),(105,34),(84,34)], cloud_dark)
c.poly([(4,53),(18,53),(18,49),(30,49),(30,52),(43,52),(43,57),(4,57)], cloud_mid)
c.poly([(91,47),(104,47),(104,43),(119,43),(119,46),(128,46),(128,52),(91,52)], cloud_mid)
c.rect(55,27,18,2,"#4c2030")
c.rect(60,24,9,2,"#4c2030")

# Distant ruined skyline.
c.poly([(0,77),(8,77),(8,62),(12,62),(12,68),(17,68),(17,79),(23,79),(23,58),(27,58),(27,55),(31,55),(31,72),(38,72),(38,82),(46,82),(46,68),(50,68),(50,84),(57,84),(57,76),(62,76),(62,92),(0,92)], ruin_far)
c.poly([(74,91),(74,77),(81,77),(81,69),(86,69),(86,74),(91,74),(91,61),(95,61),(95,56),(100,56),(100,70),(106,70),(106,76),(111,76),(111,64),(117,64),(117,59),(121,59),(121,79),(128,79),(128,93)], ruin_far)
# Towers, broken crenellations near sides.
c.poly([(0,70),(4,70),(4,64),(8,64),(8,69),(12,69),(12,64),(16,64),(16,73),(20,73),(20,96),(0,96)], ruin_near)
c.poly([(108,76),(108,68),(112,68),(112,62),(116,62),(116,68),(120,68),(120,61),(124,61),(124,69),(128,69),(128,97),(107,97)], ruin_near)
# Horizon and ground.
c.poly([(0,91),(15,89),(27,93),(40,90),(53,94),(64,91),(75,94),(89,90),(105,93),(128,89),(128,128),(0,128)], ground)
c.rect(0,96,128,2,"#1c171d")
c.poly([(0,112),(20,110),(38,113),(58,109),(80,113),(101,108),(128,111),(128,128),(0,128)], "#0d1015")
# Ground shards / rim light.
c.line(48,102,62,101,ground_hi); c.line(69,102,82,101,ground_hi)
c.line(4,118,19,115,ground_hi); c.line(95,117,119,114,ground_hi)
c.poly([(60,105),(64,96),(68,105)], "#36252b")
c.set(64,98,sunset)

# KNIGHT: rear cape silhouette and wind-swept red cape.
c.poly([(27,55),(17,62),(13,78),(12,99),(7,109),(19,107),(28,99),(37,80),(39,64)], outline)
c.poly([(25,59),(17,66),(17,79),(12,91),(14,103),(8,108),(20,105),(24,98),(31,91),(34,70)], red_dark)
c.poly([(18,75),(12,83),(14,91),(9,99),(20,95),(25,82)], red)
c.poly([(16,97),(10,105),(22,101),(27,92),(23,100)], red_hi)
# Far leg.
c.poly([(25,88),(36,89),(35,105),(42,117),(38,121),(30,110),(26,103)], outline)
c.poly([(28,91),(34,92),(33,104),(39,116),(36,117),(29,106)], metal_dark)
c.poly([(36,116),(43,116),(46,120),(45,123),(35,123),(33,120)], outline)
c.poly([(37,117),(42,118),(44,121),(36,121)], red_dark)
# Body armor outer silhouette.
c.poly([(25,48),(39,47),(48,55),(50,72),(45,89),(28,91),(20,80),(20,61)], outline)
# Torso breastplate.
c.poly([(28,52),(39,51),(45,57),(46,72),(41,84),(29,85),(23,78),(24,61)], red)
c.poly([(28,53),(35,52),(34,82),(28,82),(24,76),(25,61)], red_hi)
c.poly([(35,52),(41,54),(45,61),(45,70),(40,78),(35,81)], red_dark)
# Breastplate facets and trim.
c.line(35,53,35,80,red_light)
c.line(27,62,43,61,metal_dark)
c.line(26,76,42,79,metal_dark)
c.poly([(30,64),(35,67),(40,64),(38,74),(35,78),(31,73)], "#7d2430")
c.set(35,69,gold); c.set(35,70,gold)
# Belt.
c.rect(24,82,22,5,outline); c.rect(27,83,17,3,leather)
c.rect(34,82,5,5,gold); c.rect(35,83,3,3,"#f2c75c")
# Front leg armored, wide stance.
c.poly([(22,84),(34,84),(33,103),(28,119),(22,120),(20,113),(23,101),(18,94)], outline)
c.poly([(24,87),(31,87),(30,102),(26,116),(23,116),(23,111),(26,100),(21,93)], red)
c.poly([(25,88),(29,88),(28,101),(24,108),(25,97),(22,93)], red_hi)
c.poly([(19,116),(29,116),(31,120),(29,123),(17,123),(16,120)], outline)
c.poly([(20,117),(27,117),(29,120),(19,120)], red_dark)
# Shoulder pauldron.
c.poly([(20,56),(22,49),(28,44),(38,45),(42,51),(41,58),(32,61),(23,59)], outline)
c.poly([(23,54),(25,49),(30,47),(37,48),(40,52),(39,56),(31,58),(24,57)], red)
c.poly([(24,52),(30,48),(31,57),(25,56)], red_light)
c.line(31,47,31,57,"#ff8a68")
# Helmet, anime angular profile facing right.
c.poly([(22,45),(22,34),(27,25),(38,23),(47,28),(50,38),(47,50),(38,54),(28,50)], outline)
c.poly([(26,44),(25,35),(29,28),(38,26),(44,29),(47,37),(44,47),(37,51),(29,48)], red)
c.poly([(27,35),(31,28),(36,27),(34,47),(29,46)], red_hi)
c.poly([(36,27),(43,30),(46,37),(43,42),(35,42)], red_dark)
# Face opening and skin sliver.
c.poly([(34,35),(47,35),(48,40),(43,45),(34,43)], outline)
c.poly([(36,37),(45,37),(46,40),(42,43),(36,42)], skin)
c.rect(40,38,5,2,hair)
c.set(44,39,"#ffd66b")
# Helmet brow, cheek, horn-like crest.
c.line(33,34,47,34,steel_shadow)
c.poly([(43,41),(49,39),(47,48),(42,51)], red_dark)
c.poly([(25,29),(20,21),(25,22),(31,27)], red_hi)
c.poly([(27,26),(24,17),(29,19),(34,26)], red)
c.poly([(30,25),(29,14),(34,18),(37,26)], red_dark)
# Sword arm thrust toward central gap.
c.poly([(42,58),(49,57),(57,66),(54,71),(47,66),(40,64)], outline)
c.poly([(43,60),(48,60),(54,66),(52,68),(47,64),(42,63)], red)
c.rect(52,65,8,5,outline); c.rect(53,66,6,3,gold)
# Sword angled upward but stopping near center.
c.poly([(56,62),(59,64),(74,45),(75,40),(71,43)], outline)
c.poly([(58,62),(59,62),(73,44),(73,42),(71,45)], steel_hi)
c.line(60,60,72,45,steel_shadow)
c.poly([(71,44),(74,39),(76,37),(75,43)], steel_hi)

# ROGUE: trailing cloak silhouette.
c.poly([(100,51),(111,58),(116,72),(113,89),(121,106),(111,105),(104,96),(96,83),(91,62)], outline)
c.poly([(101,54),(108,59),(112,71),(109,87),(116,101),(109,100),(101,91),(95,79),(94,61)], green_dark)
c.poly([(107,64),(113,73),(109,86),(116,99),(109,96),(104,82)], green)
c.poly([(111,85),(121,103),(113,102),(106,95)], green_mid)
# Back leg.
c.poly([(96,87),(108,89),(108,105),(115,118),(111,122),(103,112),(99,103)], outline)
c.poly([(99,91),(105,92),(105,105),(111,117),(108,118),(102,108)], green_black)
c.poly([(107,117),(118,117),(120,121),(117,123),(106,123),(104,120)], outline)
c.poly([(109,118),(116,118),(118,121),(107,121)], leather)
# Main torso, slim silhouette.
c.poly([(88,50),(101,49),(108,58),(108,77),(103,91),(87,91),(79,80),(80,62)], outline)
c.poly([(90,53),(99,52),(105,59),(105,75),(101,87),(89,88),(82,79),(83,63)], green)
c.poly([(96,53),(101,56),(104,61),(104,76),(100,84),(96,84)], green_dark)
c.poly([(84,61),(91,55),(92,85),(88,85),(83,78)], green_mid)
# Cloak folds.
c.line(89,58,87,84,green_hi)
c.line(96,55,98,84,"#244e35")
c.line(101,62,102,78,green_hi)
# Belt and pouches.
c.rect(81,84,25,5,outline); c.rect(84,85,19,3,leather)
c.rect(87,84,5,5,gold)
c.rect(99,87,7,6,outline); c.rect(100,88,5,4,leather_hi)
# Front leg crouched forward.
c.poly([(84,86),(96,86),(94,103),(85,116),(79,117),(76,113),(84,101),(79,94)], outline)
c.poly([(86,89),(93,89),(91,101),(84,113),(79,114),(84,102),(82,94)], green_dark)
c.poly([(86,91),(90,90),(88,101),(82,109),(85,99)], green_mid)
c.poly([(75,113),(85,113),(87,118),(84,121),(73,121),(71,118)], outline)
c.poly([(76,115),(83,115),(85,118),(74,119)], leather)
# Hood and head, pointed anime profile facing left.
c.poly([(82,49),(77,42),(79,31),(86,23),(98,23),(106,31),(106,43),(101,53),(90,57)], outline)
c.poly([(82,46),(80,40),(82,32),(88,26),(97,26),(103,32),(103,42),(98,50),(90,53)], green_dark)
c.poly([(83,37),(87,28),(93,26),(91,51),(86,49),(82,43)], green)
c.poly([(94,26),(100,29),(103,34),(102,43),(97,49),(93,50)], green_black)
# Hood tail.
c.poly([(101,28),(111,30),(106,34),(115,39),(104,39)], outline)
c.poly([(102,30),(108,31),(104,34),(111,37),(103,36)], green_mid)
# Shadowed face and visible eye.
c.poly([(82,38),(96,36),(99,41),(96,47),(87,48),(82,44)], outline)
c.poly([(84,39),(94,38),(96,41),(94,45),(87,46),(83,43)], skin)
c.poly([(84,39),(95,38),(91,41),(84,42)], hair)
c.rect(84,41,5,2,hair)
c.set(84,41,eye); c.set(85,41,"#caff62")
# Scarf/mask.
c.poly([(84,44),(96,42),(97,47),(91,51),(84,48)], green_black)
c.line(85,45,95,43,green_hi)
# Shoulder clasp.
c.circle(82,57,6,outline)
c.circle(82,57,4,green_mid)
c.circle(82,57,2,gold)
c.set(81,56,"#ffe075")
# Forward arm and reverse-grip dagger kept out of body gap.
c.poly([(83,60),(77,62),(72,74),(76,78),(82,71),(88,66)], outline)
c.poly([(82,62),(78,64),(74,73),(76,75),(80,69),(86,65)], green_mid)
c.poly([(72,72),(78,75),(77,80),(72,78)], outline)
c.rect(72,74,5,3,leather_hi)
# Dagger points down into center gap.
c.poly([(72,78),(75,79),(67,96),(65,100),(66,94)], outline)
c.poly([(72,79),(73,80),(67,95),(67,97),(66,96)], steel_hi)
c.line(69,89,72,81,steel_shadow)
# Rear arm raised with small knife.
c.poly([(103,58),(110,55),(115,48),(119,51),(114,61),(106,67)], outline)
c.poly([(104,59),(109,57),(114,50),(117,52),(112,59),(106,64)], green)
c.rect(114,47,6,5,outline); c.rect(115,48,4,3,leather_hi)
c.poly([(117,48),(119,49),(124,38),(124,34),(121,37)], outline)
c.poly([(119,47),(120,47),(123,38),(123,36),(122,39)], steel_hi)

# Foreground sparks/dust emphasize the empty air between rivals.
for x,y,col in [(61,56,sunset),(67,61,gold),(63,72,"#f3c269"),(69,82,sunset),(58,88,"#b94b3e"),(72,91,"#d87b47"),(64,115,"#62402f")]:
    c.set(x,y,col)
c.set(62,57,gold); c.set(68,62,"#f6ce70")

# Sparse character rim pixels for readability against the sky.
c.line(19,62,19,77,"#d43a3d")
c.line(109,62,112,72,green_hi)
c.set(25,47,red_light); c.set(40,49,red_light)
c.set(82,48,green_hi); c.set(84,30,green_hi)

view(c, scale=4, margin=0)
finish(c)
