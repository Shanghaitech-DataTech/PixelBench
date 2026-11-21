# Magic forest cottage, 128x128 pixel art
result = new_canvas(128, 128, background="#171127", name="magic-forest-cottage")

# Palette
sky0 = "#171127"
sky1 = "#211535"
sky2 = "#2d1b45"
sky3 = "#422553"
moon0 = "#f3dfad"
moon1 = "#dcc992"
moon2 = "#baa875"
cloud = "#6a5376"
cloud_dark = "#4c3b61"
mist = "#665b79"
mist_hi = "#82778c"
black = "#130f1d"
trunk0 = "#21151f"
trunk1 = "#382128"
trunk2 = "#55302f"
leaf0 = "#251326"
leaf1 = "#3a1934"
leaf2 = "#53223e"
leaf3 = "#6b2b3c"
stone0 = "#292735"
stone1 = "#3b3946"
stone2 = "#55505a"
stone3 = "#716a70"
wood0 = "#2b1b20"
wood1 = "#4b2b27"
wood2 = "#704035"
moss0 = "#25372f"
moss1 = "#355044"
moss2 = "#4e6650"
moss3 = "#718064"
glow0 = "#9a462e"
glow1 = "#e27a36"
glow2 = "#ffb84d"
glow3 = "#ffe08a"

# Sky bands and subtle block-dither
result.rect(0, 18, 128, 34, sky1)
result.rect(0, 44, 128, 26, sky2)
result.rect(0, 62, 128, 22, sky3)
for x, y in [(8,12),(18,23),(35,8),(48,18),(70,10),(83,27),(101,16),(115,33),(26,40),(91,45),(6,57),(58,38)]:
    result.set(x,y,"#756184")
for x, y in [(13,13),(39,25),(74,31),(111,11),(121,45),(54,7)]:
    result.set(x,y,"#c1a9bd")

# Full moon and crater pixels
result.circle(35, 29, 18, moon1)
result.circle(32, 26, 14, moon0)
result.poly([(22,20),(27,17),(30,19),(28,23),(23,23)], moon1)
result.rect(38,17,5,3,moon2)
result.rect(43,28,7,4,moon2)
result.rect(24,34,5,4,moon2)
result.rect(34,39,7,3,moon2)
result.set(20,29,moon2)
result.set(39,24,moon1)

# Clouds crossing moon, then distant haze
result.rect(0,39,22,3,cloud_dark)
result.rect(7,37,28,4,cloud)
result.rect(18,39,35,4,cloud)
result.rect(41,41,31,3,cloud_dark)
result.rect(80,32,28,3,cloud_dark)
result.rect(89,30,17,3,cloud)
result.rect(103,34,25,4,cloud_dark)
result.poly([(0,68),(18,65),(33,67),(49,63),(72,66),(92,62),(110,65),(128,61),(128,78),(0,78)], mist)
result.poly([(0,72),(20,70),(38,73),(58,69),(77,71),(96,68),(112,70),(128,67),(128,78),(0,78)], mist_hi)

# Distant pine silhouettes
for x,h in [(4,28),(13,22),(76,25),(87,31),(116,30),(124,25)]:
    base=78
    result.rect(x,base-h,2,h,black)
    result.poly([(x+1,base-h-7),(x-6,base-h+10),(x-2,base-h+9),(x-9,base-h+19),(x-3,base-h+17),(x-10,base-h+27),(x+9,base-h+27),(x+4,base-h+17),(x+10,base-h+19),(x+4,base-h+9),(x+7,base-h+10)], black)

# Cottage body, timber and irregular stone foundation
result.poly([(40,71),(98,68),(105,75),(104,105),(42,105)], stone1)
result.rect(43,75,59,27,stone2)
# stone blocks
for x,y,w,h in [(44,77,11,6),(57,76,13,7),(72,76,12,6),(86,74,14,7),(47,85,15,7),(64,85,9,6),(75,84,14,8),(91,83,10,7),(44,94,10,7),(56,93,14,8),(72,94,11,7),(85,93,16,8),(48,103,13,3),(65,102,18,4),(87,102,14,4)]:
    result.rect(x,y,w,h,stone1)
# stone highlights
for x,y,w in [(45,77,8),(58,76,8),(74,76,7),(88,74,8),(48,85,10),(66,85,5),(77,84,8),(93,83,6),(46,94,6),(58,93,8),(74,94,6),(88,93,9)]:
    result.rect(x,y,w,1,stone3)

# Timber frame
result.rect(42,72,3,33,wood0)
result.rect(100,71,4,35,wood0)
result.rect(70,72,4,34,wood0)
result.rect(43,82,59,3,wood0)
result.rect(43,101,61,4,wood0)
result.line(45,74,70,82,wood1)
result.line(99,73,74,82,wood1)

# Steep roof dark outline and layered shingles
result.poly([(31,69),(46,43),(67,34),(93,45),(111,70),(104,76),(97,69),(43,71),(38,76)], black)
result.poly([(36,66),(49,46),(67,38),(91,48),(105,68),(96,67),(91,61),(48,65),(42,72)], moss0)
result.poly([(45,61),(51,48),(67,41),(88,50),(96,62),(79,58),(61,60)], moss1)
# Roof rows and shingles
result.line(43,63,99,65,moss2)
result.line(47,57,93,59,moss2)
result.line(52,51,87,54,moss2)
for x,y in [(49,62),(57,61),(67,61),(78,61),(88,62),(52,56),(61,57),(72,57),(83,58),(56,51),(67,53),(78,53),(62,46),(70,47)]:
    result.rect(x,y,5,2,moss3)
for x,y in [(39,67),(46,64),(54,66),(63,63),(74,65),(82,62),(93,66),(99,67),(50,53),(59,48),(85,55)]:
    result.rect(x,y,4,2,moss0)
# Uneven moss fringe
for x,h in [(40,4),(47,2),(54,5),(62,3),(73,5),(81,2),(90,4),(99,3)]:
    result.rect(x,66,3,h,moss2)

# Chimney with moonlit rim and smoke
result.rect(83,34,10,18,black)
result.rect(85,36,7,14,stone1)
result.rect(84,34,10,3,stone0)
result.rect(86,36,5,1,stone3)
result.poly([(88,33),(84,28),(89,24),(86,20),(92,16),(96,20),(93,25),(98,29),(94,34)], cloud_dark)

# Door
result.rect(78,84,17,20,wood0)
result.rect(81,87,11,17,wood1)
result.rect(82,88,8,2,wood2)
result.line(82,94,91,94,wood0)
result.set(89,97,glow2)
result.rect(76,102,21,3,stone0)

# Warm window with bloom pixels
result.rect(50,79,17,16,wood0)
result.rect(53,82,11,10,glow1)
result.rect(54,82,9,9,glow2)
result.rect(55,83,7,7,glow3)
result.rect(57,80,2,14,wood1)
result.rect(51,86,15,2,wood1)
result.set(49,84,glow0); result.set(67,84,glow0); result.set(50,94,glow0)

# Ground mass
result.poly([(0,89),(16,84),(34,88),(48,101),(75,105),(96,101),(112,91),(128,92),(128,128),(0,128)], black)
result.poly([(0,101),(25,96),(46,104),(67,109),(91,106),(111,99),(128,101),(128,128),(0,128)], trunk0)
# undergrowth patches
result.poly([(0,108),(13,101),(22,108),(31,102),(42,111),(55,105),(66,112),(79,108),(90,113),(104,104),(116,111),(128,106),(128,128),(0,128)], moss0)
result.rect(0,118,128,10,"#1d2927")

# Stone-slab path from door toward viewer
slabs = [((79,103),(96,103),(99,108),(76,109)),((71,109),(101,110),(108,117),(66,117)),((57,119),(111,118),(125,127),(45,127))]
for i,pts in enumerate(slabs):
    result.poly(list(pts), stone1 if i != 1 else stone2)
    result.line(pts[0][0],pts[0][1],pts[1][0],pts[1][1],stone3)
result.rect(84,106,7,2,stone0)
result.rect(75,113,11,2,stone0)
result.rect(93,121,17,2,stone0)
result.rect(54,125,16,2,stone3)

# Well behind path on left
result.ellipse(27,91,17,6,stone0)
result.rect(11,91,33,17,stone0)
result.poly([(11,93),(44,93),(42,108),(14,108)], stone1)
result.ellipse(27,92,15,5,stone3)
result.ellipse(27,93,12,3,black)
result.rect(14,96,9,5,stone2); result.rect(25,97,8,5,stone2); result.rect(35,95,7,6,stone2)
result.rect(17,103,12,5,stone2); result.rect(31,103,10,5,stone2)
result.line(14,94,14,73,wood1); result.line(40,94,40,72,wood1)
result.rect(11,71,32,3,wood0)
result.rect(13,72,28,2,wood2)
result.line(19,82,35,82,wood2)
result.circle(27,82,5,wood0,fill=False)
result.circle(27,82,2,wood2)
result.line(32,78,37,74,wood2)
result.line(27,84,27,92,"#1c151d")

# Ancient twisted trees framing the scene
# Left trunk and branches
result.poly([(0,18),(8,20),(10,38),(7,55),(14,69),(12,91),(6,106),(0,108)], trunk0)
result.poly([(3,18),(8,25),(7,42),(4,55),(9,70),(7,89),(2,99),(0,98),(0,22)], trunk1)
result.poly([(7,48),(15,35),(25,30),(27,24),(22,25),(17,31),(10,34)], trunk1)
result.poly([(8,59),(20,51),(32,50),(38,45),(31,47),(20,47),(10,52)], trunk0)
result.line(5,37,1,23,trunk2)
# Right trunk
result.poly([(128,13),(119,17),(117,32),(121,45),(115,59),(117,75),(108,93),(107,109),(116,112),(124,94),(126,72),(123,56),(128,45)], trunk0)
result.poly([(126,20),(121,30),(124,45),(120,57),(121,73),(115,91),(115,104),(120,96),(126,75),(125,56),(128,46)], trunk2)
result.poly([(120,40),(109,31),(99,28),(94,22),(99,23),(105,27),(117,30)], trunk0)
result.poly([(119,56),(108,47),(96,45),(90,40),(96,42),(108,42),(122,49)], trunk1)

# Leaf masses, blocky clusters
for cx,cy,rx,ry,col in [
    (5,15,11,8,leaf0),(15,20,12,8,leaf1),(26,17,10,7,leaf2),(2,31,10,8,leaf2),(16,34,8,6,leaf3),
    (123,12,11,8,leaf0),(112,18,13,8,leaf1),(100,15,9,6,leaf2),(126,30,10,8,leaf2),(110,35,9,7,leaf3),
    (8,64,8,6,leaf1),(119,67,10,7,leaf1)]:
    result.ellipse(cx,cy,rx,ry,col)
# Pixel notches/highlights in foliage
for x,y,col in [(11,16,leaf3),(20,22,leaf3),(27,15,leaf3),(4,29,leaf3),(16,32,"#7a3443"),(109,17,leaf3),(101,14,leaf3),(119,29,leaf3),(110,34,"#7a3443"),(3,13,leaf2),(124,8,leaf2)]:
    result.rect(x,y,5,3,col)

# Foreground grasses, mushrooms, and tiny fireflies
for x,y,h in [(3,119,7),(8,122,5),(16,116,8),(22,121,6),(34,115,9),(39,122,6),(113,116,9),(120,120,7),(125,113,10),(102,118,7)]:
    result.line(x,y,x-2,y-h,moss2)
    result.line(x,y,x+3,y-h+2,moss1)
result.rect(26,115,2,4,moon2); result.rect(23,113,7,2,"#8c4c4c")
result.rect(117,109,2,4,moon2); result.rect(114,107,7,2,"#8c4c4c")
for x,y in [(18,61),(31,70),(107,60),(111,79),(5,80),(46,73)]:
    result.set(x,y,glow3)
    result.set(x+1,y,glow1)

# A few crisp foreground accents
result.rect(0,109,5,3,trunk2)
result.rect(121,98,7,4,trunk1)
result.set(104,106,moss3)
result.set(32,111,moss3)

view(result, scale=4, margin=0)
finish(result)
