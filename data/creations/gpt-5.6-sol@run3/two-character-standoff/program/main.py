# Two-character anime standoff, 128x128 pixel art
c = new_canvas(128, 128, background="#161326", name="two_character_standoff")

# Palette
sky0 = "#211b35"; sky1 = "#392244"; sky2 = "#713040"; sky3 = "#c45443"; sun = "#f3a85b"
far = "#2a2033"; far2 = "#1d1928"; ground = "#171520"; ground2 = "#27202a"
ink = "#120f19"; outline = "#20141c"; skin = "#eab18d"; skin_hi = "#ffd2a6"; skin_sh = "#a75d57"
red0 = "#4b1725"; red1 = "#7d2430"; red2 = "#bd3b3e"; red3 = "#ed5a47"; red_hi = "#ff8a5b"
steel0 = "#4a4a5d"; steel1 = "#77788b"; steel2 = "#b9b8bd"; steel3 = "#eee2d0"; gold = "#e6a044"
green0 = "#15362f"; green1 = "#1f5740"; green2 = "#348052"; green3 = "#65ad62"; green_hi = "#a2d477"
brown = "#4a2928"; leather = "#754139"; cyan = "#85d8cf"; white = "#fff1d5"

# Pixel-banded sunset sky
c.rect(0, 0, 128, 18, sky0)
c.rect(0, 18, 128, 17, sky1)
c.rect(0, 35, 128, 16, sky2)
c.rect(0, 51, 128, 18, sky3)
c.rect(0, 69, 128, 18, "#8f3c3f")
# Blocky sunset glow centered in the gap
c.rect(54, 42, 20, 5, sun)
c.rect(50, 47, 28, 12, sun)
c.rect(47, 52, 34, 10, sun)
c.rect(51, 62, 26, 5, "#dc7049")
# Sparse clouds / speed-like atmosphere
for x,y,w in [(6,27,20),(0,31,13),(91,25,28),(102,31,26),(17,43,18),(94,45,24)]:
    c.rect(x,y,w,3,"#4b2941")
for x,y,w in [(3,57,22),(84,58,17),(102,54,25)]:
    c.rect(x,y,w,2,"#9d4145")
# Tiny drifting embers
for x,y in [(42,39),(83,35),(46,68),(79,72),(36,55),(88,49),(62,30),(69,75)]:
    c.set(x,y,"#ffc06b"); c.set(x+1,y,"#d85b43")

# Distant ruined battlements
c.poly([(0,69),(0,61),(5,61),(5,65),(9,65),(9,58),(14,58),(14,66),(21,66),(21,62),(27,62),(27,73)], far)
c.poly([(101,70),(101,64),(106,64),(106,57),(112,57),(112,64),(118,64),(118,60),(123,60),(123,55),(128,55),(128,76)], far)
c.rect(0,73,128,18,far)
# horizon chips
c.rect(30,70,19,3,far2); c.rect(80,69,18,4,far2); c.rect(55,75,21,2,far2)

# Ground and central reflection/gap
c.rect(0,88,128,40,ground)
c.poly([(46,88),(82,88),(75,128),(52,128)], "#211a24")
c.rect(57,91,14,2,"#7e3a3e"); c.rect(59,98,10,2,"#5f3037"); c.rect(61,109,7,2,"#3d262f")
# Ground texture
for x,y,w,col in [(0,105,25,ground2),(8,116,31,"#211c26"),(87,104,41,ground2),(94,116,28,"#211c26"),(29,98,18,"#30232a"),(75,95,15,"#30232a")]:
    c.rect(x,y,w,2,col)
for x,y in [(6,94),(22,110),(37,121),(84,115),(110,98),(121,123),(73,124),(49,103)]:
    c.rect(x,y,3,2,"#3a2930")

# KNIGHT: windblown scarf/cape behind
c.poly([(35,55),(20,58),(9,66),(25,66),(11,74),(31,72),(42,65)], ink)
c.poly([(34,57),(21,60),(13,65),(30,64),(17,71),(34,68),(43,62)], red1)
c.rect(13,64,13,2,red3); c.rect(21,69,11,2,red2)

# Knight legs, heavy greaves
c.poly([(27,94),(41,94),(40,108),(37,121),(25,121),(27,108)], ink)
c.poly([(29,95),(38,95),(37,108),(34,117),(27,117),(29,106)], steel0)
c.rect(27,116,12,5,ink); c.rect(23,120,16,5,ink); c.rect(27,117,9,3,steel1)
c.poly([(43,94),(54,96),(56,109),(61,119),(51,124),(45,111)], ink)
c.poly([(45,96),(52,98),(53,109),(58,118),(52,120),(48,109)], steel0)
c.poly([(52,118),(61,118),(65,123),(62,126),(50,125),(48,122)], ink)
c.rect(52,119,7,3,steel1)

# Knight torso silhouette and red plate
c.poly([(24,57),(32,49),(45,50),(53,60),(52,79),(58,94),(50,101),(29,99),(21,90),(24,73),(18,68)], ink)
c.poly([(29,55),(38,51),(47,56),(50,63),(48,80),(53,93),(47,97),(31,95),(25,88),(27,72),(22,67)], red0)
# chest armor plates
c.poly([(31,56),(43,54),(49,61),(47,72),(31,70),(26,64)], red2)
c.poly([(30,57),(41,55),(45,59),(33,61)], red3)
c.rect(30,70,18,4,outline)
c.poly([(29,74),(47,75),(49,88),(42,94),(30,90)], red1)
c.rect(32,76,13,3,red2); c.rect(31,88,16,3,red3)
c.rect(35,55,3,15,red_hi)
# belt
c.rect(26,91,25,5,ink); c.rect(31,92,18,3,leather); c.rect(39,91,5,5,gold); c.rect(40,92,3,3,"#ffe08a")

# Knight shoulder pauldrons and left arm
c.poly([(20,58),(27,53),(35,57),(33,67),(23,70),(17,66)], ink)
c.poly([(21,59),(27,55),(32,58),(30,65),(23,67),(19,64)], red2)
c.rect(22,58,8,2,red_hi)
c.poly([(20,66),(27,69),(24,82),(17,91),(11,87),(16,77)], ink)
c.poly([(21,69),(24,71),(21,80),(16,87),(13,85),(18,76)], red1)
c.rect(13,84,7,6,steel1); c.rect(12,86,7,3,steel2)

# Knight head profile, hair, face
c.poly([(27,47),(28,35),(34,27),(45,28),(52,35),(51,48),(45,55),(33,53)], ink)
# swept anime hair / helmet plume
c.poly([(29,39),(23,32),(30,33),(27,25),(36,30),(39,21),(43,29),(53,25),(49,34),(55,35),(48,40)], red0)
c.poly([(31,35),(34,28),(39,33),(42,25),(45,34),(51,31),(47,39)], red3)
c.rect(33,31,3,6,red_hi)
# face looking right
c.poly([(32,38),(45,35),(50,39),(48,48),(43,53),(34,50)], skin_sh)
c.poly([(34,38),(44,36),(48,39),(46,45),(42,49),(35,48)], skin)
c.rect(36,39,9,2,skin_hi)
# eye + brow + nose profile
c.rect(40,40,7,2,outline); c.rect(43,41,3,2,white); c.set(45,41,"#d63b36")
c.rect(46,43,4,2,skin); c.set(49,44,skin_hi); c.rect(43,47,5,2,outline)
# neck
c.rect(34,50,10,7,ink); c.rect(36,50,8,5,skin_sh)

# Knight sword held toward gap, stops before center
c.poly([(17,89),(20,86),(59,67),(62,68),(22,92)], ink)
c.poly([(21,87),(58,69),(59,71),(23,90)], steel2)
c.line(24,87,57,71,steel3)
c.poly([(17,85),(26,91),(24,95),(15,89)], gold)
c.rect(14,89,5,8,brown)

# ROGUE cloak tails behind, clearly green silhouette
c.poly([(99,58),(113,62),(126,73),(115,73),(127,84),(108,78),(118,92),(99,84)], ink)
c.poly([(100,60),(112,64),(121,71),(110,70),(123,81),(106,75),(114,86),(98,80)], green0)
c.rect(109,68,9,2,green2); c.rect(108,77,10,2,green1)

# Rogue legs and soft boots
c.poly([(83,91),(96,94),(94,108),(87,122),(74,124),(75,119),(83,106)], ink)
c.poly([(85,94),(93,95),(91,106),(85,118),(78,120),(85,104)], green0)
c.poly([(75,119),(88,117),(91,122),(87,126),(72,126),(70,123)], ink)
c.rect(77,119,10,3,leather)
c.poly([(99,92),(109,91),(110,108),(116,120),(111,125),(102,122),(102,108)], ink)
c.poly([(101,94),(106,94),(107,108),(113,119),(109,121),(105,108)], brown)
c.poly([(109,118),(117,119),(121,124),(117,127),(105,125),(104,122)], ink)
c.rect(109,120,8,3,leather)

# Rogue body and cloak mass
c.poly([(82,56),(91,50),(102,52),(109,62),(107,76),(113,91),(106,100),(84,99),(75,91),(78,75),(71,68)], ink)
c.poly([(86,55),(95,52),(103,56),(106,64),(103,76),(109,91),(103,96),(87,95),(79,89),(82,75),(75,68)], green0)
# flowing cloak main panels
c.poly([(93,57),(104,59),(103,75),(108,91),(100,95),(94,78)], green1)
c.poly([(86,58),(94,56),(93,91),(84,94),(80,86),(82,68)], green2)
c.poly([(87,59),(92,57),(89,88),(85,90),(83,84)], green3)
c.rect(84,62,3,18,green_hi)
c.poly([(95,58),(102,61),(99,67),(95,65)], green3)
# waist straps and pouches
c.rect(80,89,27,5,ink); c.rect(84,90,19,3,leather); c.rect(94,89,4,5,gold)
c.rect(101,92,7,7,brown); c.rect(102,93,5,4,leather)

# Rogue shoulder/cowl and forward arm
c.poly([(82,55),(91,51),(99,55),(97,66),(84,68),(76,63)], ink)
c.poly([(83,57),(91,53),(96,56),(94,63),(85,65),(79,62)], green2)
c.rect(84,57,9,2,green_hi)
c.poly([(81,65),(87,69),(81,80),(73,88),(68,84),(75,75)], ink)
c.poly([(82,68),(85,70),(79,78),(72,85),(70,83),(77,73)], green1)
# glove
c.poly([(68,81),(74,84),(72,90),(66,91),(63,87)], ink); c.rect(67,84,5,5,leather)

# Rogue hood and face profile looking left
c.poly([(82,51),(77,45),(77,36),(84,28),(96,27),(104,34),(103,47),(98,55),(88,57)], ink)
c.poly([(80,44),(80,36),(86,30),(96,30),(101,35),(100,46),(96,52),(87,53)], green0)
# angular hood highlights and long tail
c.poly([(81,37),(86,30),(96,30),(91,34),(84,42)], green2)
c.poly([(98,31),(103,35),(101,47),(97,51),(98,41)], green1)
c.poly([(101,47),(109,52),(102,55),(94,52)], green0)
c.rect(84,33,8,2,green3)
# face opening
c.poly([(82,40),(86,35),(96,35),(99,39),(97,47),(91,51),(84,48)], skin_sh)
c.poly([(83,40),(88,36),(96,37),(97,40),(94,46),(89,48),(84,46)], skin)
c.rect(84,39,10,2,skin_hi)
# eye looking left
c.rect(82,41,9,2,outline); c.rect(84,42,4,2,white); c.set(84,42,cyan)
c.set(81,43,skin_hi); c.rect(84,47,6,2,outline)
# mask/scarf
c.poly([(83,46),(91,48),(98,44),(97,51),(91,55),(84,52)], green0)
c.rect(88,49,7,2,green2)

# Rogue dagger toward gap but leaving central air
c.poly([(67,84),(64,82),(73,66),(76,65),(72,83)], ink)
c.poly([(66,81),(73,67),(74,68),(69,83)], steel2)
c.line(69,78,73,69,steel3)
c.poly([(64,80),(72,84),(70,88),(62,84)], gold)
c.rect(60,84,6,4,brown)
# Second reverse dagger at right hip
c.poly([(106,88),(110,87),(119,102),(117,105)], ink)
c.poly([(109,89),(117,102),(116,103),(108,91)], steel2)
c.rect(104,86,7,4,gold)

# Foreground dust and sparks emphasize central gap
for x,y in [(58,83),(63,78),(68,87),(60,94),(72,73),(54,90)]:
    c.set(x,y,"#ffbd68")
for x,y in [(61,85),(70,81),(56,87)]:
    c.rect(x,y,2,1,"#e45b42")
# Foot contact shadows
c.rect(19,124,44,3,"#0d0c12"); c.rect(70,125,51,3,"#0d0c12")

result = c
view(result, scale=4, margin=0)
finish(result)
