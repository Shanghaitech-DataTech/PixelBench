from pixelbench_api import *
import random

random.seed(7)
c = new_canvas(128, 128, background="#120d25", name="magic-forest-cottage")

# Compact nocturnal palette.
sky0="#120d25"; sky1="#1b1234"; sky2="#281746"; sky3="#382055"
moon0="#fff1bd"; moon1="#ead99c"; moon2="#c9bd92"
mist0="#756b8f"; mist1="#554d75"; mist2="#3c365d"
ink="#110d1b"; bark0="#211425"; bark1="#352033"; bark2="#4a2938"; bark3="#633442"
leaf0="#24142d"; leaf1="#351936"; leaf2="#4a203f"; leaf3="#61283f"; leaf4="#763440"
stone0="#29283a"; stone1="#3b3b4d"; stone2="#555467"; stone3="#706c79"; stone4="#8b8490"
wood0="#2a1a21"; wood1="#47272a"; wood2="#65382f"; wood3="#875044"
moss0="#263525"; moss1="#354a2d"; moss2="#4a6034"; moss3="#657444"
light0="#ffbd4c"; light1="#f58735"; light2="#ffd676"; light3="#fff0af"

# Layered purple sky.
c.rect(0,0,128,76,sky1)
c.rect(0,0,128,27,sky0)
c.dither(0,22,128,20,[sky0,sky1],"bayer4")
c.dither(0,42,128,25,[sky1,sky2],"bayer4")
c.rect(0,62,128,19,sky2)
c.dither(0,62,128,18,[sky2,sky3],"bayer4")

# Sparse stars and moon halo.
for x,y,col in [(12,13,moon2),(24,23,mist0),(45,10,moon1),(66,19,moon2),(95,8,moon1),(116,20,mist0),(79,34,mist0),(7,39,mist1),(36,35,mist0),(105,40,mist0),(58,5,mist1)]:
    c.set(x,y,col)
for x,y in [(18,30),(72,8),(110,29),(52,26)]:
    c.set(x,y,moon0); c.set(x+1,y,moon2)
# Moon behind right branches.
c.circle(91,28,18,mist1)
c.circle(91,27,15,moon1)
c.circle(91,27,13,moon0)
c.ellipse(85,22,4,2,moon1); c.ellipse(98,32,3,2,moon2); c.rect(79,30,4,2,moon2)

# Distant tree line.
for pts in [
 [(0,62),(7,43),(12,62)],[(9,63),(18,38),(23,63)],[(20,63),(28,48),(32,63)],
 [(103,64),(109,42),(114,64)],[(112,65),(121,36),(127,65)],[(93,64),(100,48),(105,64)]]:
    c.poly(pts,mist2)
c.rect(0,62,128,19,mist2)
# Distant trunks peeking through fog.
for x,w,h in [(5,3,29),(19,2,34),(31,3,24),(109,3,29),(122,3,35)]:
    c.rect(x,45,w,h,stone0)

# Horizontal drifting mist.
c.rect(0,69,128,7,mist1)
c.dither(0,66,128,5,[mist2,mist1],"checker")
c.rect(8,72,31,2,mist0); c.rect(2,74,51,2,mist1)
c.rect(81,68,43,2,mist0); c.rect(70,70,58,3,mist1)
c.rect(0,78,128,9,"#302d49")
c.dither(0,76,128,8,[mist1,"#302d49"],"bayer4")

# Cottage body: old stone walls.
c.poly([(42,64),(91,62),(102,76),(100,108),(39,108),(37,78)],ink)
c.rect(40,75,59,32,stone1)
c.rect(43,78,53,28,stone2)
# irregular stone courses
stones=[(44,79,10,5,stone3),(56,78,12,6,stone1),(70,79,11,5,stone3),(83,78,12,6,stone1),
(42,86,7,6,stone1),(51,86,12,5,stone3),(65,86,9,6,stone1),(76,86,14,5,stone3),(92,86,5,6,stone1),
(43,94,12,5,stone3),(57,93,8,6,stone1),(67,94,13,5,stone3),(82,93,9,6,stone1),(93,94,5,6,stone3),
(42,101,8,5,stone1),(52,101,13,5,stone3),(67,101,10,5,stone1),(79,101,12,5,stone3),(93,101,5,5,stone1)]
for x,y,w,h,col in stones: c.rect(x,y,w,h,col)
# mortar and chipped shadow pixels
for x,y in [(49,84),(68,84),(81,83),(46,92),(63,91),(74,92),(90,91),(55,100),(78,100),(95,99),(48,105),(66,105),(89,105)]: c.set(x,y,stone4)

# Steep roof silhouette and layered old shingles.
c.poly([(32,77),(55,46),(77,44),(106,75),(102,80),(30,81)],ink)
c.poly([(35,75),(56,48),(76,47),(102,75),(95,75),(74,55),(57,55),(42,76)],wood0)
c.poly([(40,70),(57,51),(74,50),(95,71),(91,73),(73,57),(58,57),(45,73)],moss0)
# roof shingle rows
c.line(43,68,92,68,wood1); c.line(47,63,87,63,wood2); c.line(51,58,82,58,wood1)
for x,y in [(48,66),(58,66),(69,66),(80,66),(88,66),(52,61),(63,61),(75,61),(83,61),(57,56),(68,56),(77,56)]:
    c.line(x,y,x+3,y+2,wood3)
# moss clumps along roof planes and eaves
c.poly([(36,73),(43,66),(48,67),(52,62),(59,63),(64,58),(71,59),(76,56),(84,61),(89,62),(95,70),(98,74),(91,72),(85,69),(78,70),(72,65),(64,67),(57,65),(50,71),(43,70)],moss1)
for x,y in [(42,69),(50,66),(58,63),(66,63),(75,62),(83,66),(91,70)]:
    c.rect(x,y,5,2,moss2); c.set(x+1,y-1,moss3)
c.rect(31,76,74,4,ink); c.rect(35,76,66,2,wood2)

# Crooked chimney.
c.poly([(75,51),(77,34),(87,35),(85,56)],ink)
c.poly([(78,50),(80,36),(85,37),(83,54)],stone1)
c.rect(79,36,7,3,stone3); c.set(82,41,stone4); c.rect(78,47,6,2,stone2)
# smoke wisps
c.rect(81,29,3,5,mist1); c.rect(83,25,3,5,mist1); c.rect(86,21,4,3,mist1); c.set(89,20,mist0)

# Timber framing.
c.rect(61,77,4,30,wood0); c.rect(40,81,58,3,wood0)
c.line(40,104,61,82,wood1); c.line(66,82,97,105,wood1)
c.rect(43,83,2,23,wood2); c.rect(94,82,3,24,wood1)

# Warm windows with heavy wood frames.
def window(x,y,w,h):
    c.rect(x-2,y-2,w+4,h+4,ink)
    c.rect(x,y,w,h,light1)
    c.rect(x+1,y+1,w-2,h-2,light0)
    c.rect(x+2,y+2,w-4,h-4,light2)
    c.set(x+2,y+1,light3)
    c.rect(x+w//2,y,2,h,wood0); c.rect(x,y+h//2,w,2,wood0)
window(47,87,11,12); window(75,85,14,13)
# light pools on wall and ground
c.dither(46,100,14,5,[light1,stone2],"checker")
c.dither(72,99,20,6,[light1,stone2],"checker")

# Rounded wooden door.
c.poly([(64,107),(64,90),(66,86),(72,84),(77,87),(79,91),(79,107)],ink)
c.poly([(67,106),(67,91),(69,88),(73,87),(76,90),(76,106)],wood1)
c.line(70,88,70,106,wood3); c.line(74,88,74,106,wood0)
c.set(74,97,light0); c.set(75,97,light2)

# Forest floor behind foreground.
c.rect(0,104,128,24,"#17151f")
c.dither(0,104,128,14,["#17151f",moss0],"bayer4")
# Reassert cottage lower edge and threshold.
c.rect(39,106,62,3,ink); c.rect(65,106,14,3,wood0); c.rect(65,109,16,2,stone3)

# Stone-slab path in perspective.
path=[[(65,110),(80,110),(84,114),(62,114)],[(60,116),(86,116),(93,121),(54,121)],[(48,123),(97,123),(108,127),(37,127)]]
for i,p in enumerate(path):
    c.poly(p,ink)
    inner=[(x+(1 if x<72 else -1),y) for x,y in p]
    c.poly(inner,[stone2,stone3,stone1][i])
for x,y in [(68,112),(78,112),(63,118),(74,118),(86,119),(52,125),(69,125),(91,125)]: c.set(x,y,stone4)

# Stone well at left foreground.
c.ellipse(23,102,17,7,ink)
c.rect(7,101,33,16,ink)
c.poly([(8,102),(39,102),(37,117),(10,117)],stone1)
# masonry blocks
for r in [(10,103,8,5,stone3),(19,103,9,5,stone2),(29,103,8,5,stone3),(9,109,11,6,stone2),(21,109,8,6,stone3),(30,109,7,6,stone2)]: c.rect(*r)
c.line(9,108,38,108,ink); c.ellipse(23,101,16,6,stone4); c.ellipse(23,101,12,4,ink); c.ellipse(23,102,9,2,"#0a0a12")
# Well posts and winch.
c.rect(8,79,4,24,wood0); c.rect(10,80,3,22,wood2)
c.rect(35,78,4,25,wood0); c.rect(35,80,2,21,wood2)
c.line(9,81,24,73,wood1); c.line(24,73,39,81,wood1); c.line(13,80,35,80,wood2)
c.rect(14,88,22,4,ink); c.rect(16,89,18,3,wood3); c.circle(15,90,3,wood1); c.circle(35,90,3,wood1)
c.line(24,92,24,101,stone4); c.set(24,97,moon1)
# crank
c.line(38,90,43,93,wood3); c.line(43,93,43,97,wood2)

# Ancient twisted trees framing the scene, in front of moon/sky.
# Left trunk and roots.
c.poly([(0,116),(0,19),(8,18),(11,38),(16,48),(14,66),(20,78),(16,95),(27,111),(22,119)],ink)
c.poly([(0,112),(2,23),(7,22),(8,42),(13,50),(11,66),(17,79),(13,94),(23,111),(17,113),(9,101),(7,122)],bark1)
c.poly([(3,104),(6,62),(10,52),(12,65),(9,82),(15,98),(12,108)],bark2)
c.line(5,29,2,66,bark3); c.line(11,52,16,43,bark2)
# left branches
c.poly([(4,36),(7,32),(28,24),(47,24),(47,28),(30,28),(14,38)],ink)
c.poly([(6,32),(20,17),(24,4),(28,3),(27,13),(16,31)],ink)
c.poly([(7,47),(21,39),(38,40),(37,44),(22,43),(11,52)],ink)
c.poly([(3,25),(0,9),(3,0),(8,0),(7,13),(11,28)],ink)
# Right massive tree.
c.poly([(109,128),(104,112),(110,94),(106,78),(112,62),(110,46),(116,34),(117,15),(125,7),(128,8),(128,128)],ink)
c.poly([(116,124),(109,112),(115,94),(111,79),(117,63),(115,48),(121,36),(121,19),(127,13),(128,18),(128,124)],bark1)
c.poly([(121,119),(115,107),(119,89),(115,77),(120,61),(119,47),(124,35),(126,20),(128,18),(128,118)],bark2)
c.line(122,39,116,75,bark3); c.line(126,59,121,89,bark0)
# right branches crossing moon
c.poly([(117,43),(104,35),(93,34),(94,30),(106,31),(119,36)],ink)
c.poly([(121,29),(105,20),(89,17),(88,13),(107,16),(125,23)],ink)
c.poly([(123,54),(104,52),(96,46),(98,43),(108,48),(126,48)],ink)
c.poly([(122,24),(114,9),(116,0),(122,0),(120,9),(127,21)],ink)

# Leaf clusters: dark crimson and plum, blocky and irregular.
def leaves(cx,cy,col):
    c.rect(cx-7,cy-3,14,7,col); c.rect(cx-4,cy-6,9,13,col)
    c.rect(cx-9,cy-1,3,4,col); c.rect(cx+6,cy,4,4,col)
    c.set(cx-5,cy-6,leaf4); c.set(cx+3,cy-4,leaf4)
for x,y,col in [(9,15,leaf1),(19,22,leaf2),(31,20,leaf3),(43,25,leaf1),(14,38,leaf3),(29,39,leaf2),(2,52,leaf2),
(116,14,leaf2),(106,18,leaf3),(95,15,leaf2),(120,34,leaf3),(104,40,leaf1),(122,53,leaf2),(111,55,leaf3)]:
    leaves(x,y,col)
# Smaller leaf sparks and dangling moss.
for x,y,col in [(25,11,leaf4),(37,16,leaf3),(50,23,leaf2),(18,31,leaf4),(101,10,leaf4),(112,27,leaf4),(99,37,leaf3),(117,60,leaf4)]:
    c.rect(x,y,3,2,col)
for x,y,h in [(31,27,7),(44,29,6),(16,43,8),(105,42,8),(114,57,9)]:
    c.line(x,y,x,y+h,moss1); c.set(x,y+h,moss2)

# Foreground roots, grasses, fungi, and final mist curls.
c.poly([(0,121),(18,113),(31,117),(20,120),(42,128),(0,128)],bark0)
c.poly([(128,116),(109,111),(96,118),(111,118),(92,128),(128,128)],bark0)
for x,y in [(4,111),(30,119),(45,114),(101,112),(115,109),(88,116)]:
    c.line(x,y,x-2,y-5,moss2); c.line(x,y,x+2,y-7,moss1)
# mushrooms near path
c.rect(43,119,1,4,moon2); c.ellipse(43,119,3,1,leaf4)
c.rect(99,116,1,4,moon2); c.ellipse(99,116,2,1,light1)
# foreground mist ribbons
c.rect(0,116,34,2,mist2); c.rect(27,120,20,2,mist1)
c.rect(91,111,37,2,mist1); c.rect(104,115,24,2,mist2)
# firefly pinpricks near cottage
for x,y in [(33,85),(31,91),(105,82),(108,88),(53,73)]:
    c.set(x,y,light0)

view(c, scale=4, margin=0)
finish(c)
