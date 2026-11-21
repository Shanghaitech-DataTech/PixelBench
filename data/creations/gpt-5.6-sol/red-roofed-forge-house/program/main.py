from pixelbench_api import *

result = new_canvas(128,128,name='red_roofed_forge')
c=result
# restrained hand-picked palette
ink='#292632'; dark='#39313a'; stone='#726b70'; mortar='#514c58'; lightstone='#aaa197'; edge='#c6b6a0'
wood='#78503d'; woodlight='#b47c4c'; wooddark='#493333'; gold='#e6b574'
red='#b54139'; redlight='#dd6750'; reddark='#783337'; roofshadow='#542e37'
# floating diamond paving footprint
c.poly([(6,90),(62,62),(122,92),(66,121)],ink)
c.poly([(6,88),(62,60),(122,90),(66,119)],'#635e64')
c.poly([(6,88),(66,118),(66,122),(6,92)],'#413f49')
c.poly([(66,118),(122,90),(122,94),(66,122)],'#4d4851')
# stones follow two isometric directions
for a,b in [((15,88),(69,115)),((28,81),(83,108)),((42,74),(97,101)),((56,67),(111,94)),((17,95),(73,67)),((30,101),(87,73)),((44,108),(101,80)),((58,115),(115,87))]:
 c.line(*a,*b,'#777078')
# tiny cracks and moss
for x,y in [(16,90),(33,105),(106,95),(70,113),(99,84)]:
 c.line(x,y,x+3,y+1,'#494852')
 c.set(x+2,y+2,'#858078')
c.line(14,93,19,95,'#657260');c.line(104,99,110,96,'#657260')
# house walls, continuous vertical edges
c.poly([(23,56),(66,77),(106,57),(106,90),(66,110),(23,88)],ink)
c.poly([(25,56),(66,76),(66,107),(25,87)],'#90857c')
c.poly([(66,76),(104,57),(104,89),(66,108)],'#686471')
# masonry foundation
c.poly([(25,78),(66,98),(66,108),(25,88)],'#6c6567')
c.poly([(66,98),(104,79),(104,89),(66,108)],'#514f5c')
for x,y in [(26,82),(38,88),(51,94)]:
 c.line(x,y,x+11,y+5,'#aaa093');c.line(x+9,y+4,x+9,y+8,mortar)
for x,y in [(68,102),(80,96),(92,90)]:
 c.line(x,y,x+10,y-5,'#827c80');c.line(x+7,y-3,x+7,y+1,'#393c49')
# upper plaster highlights and timber framing
c.line(27,59,63,77,'#baaa95');c.line(69,78,101,62,'#89808a')
c.poly([(25,58),(29,60),(29,80),(25,78)],wooddark)
c.poly([(62,76),(66,78),(66,99),(62,97)],wooddark)
c.poly([(66,78),(70,76),(70,96),(66,98)],'#3e3038')
c.poly([(100,63),(104,61),(104,81),(100,83)],wooddark)
c.line(30,77,60,92,wood);c.line(30,78,60,93,wooddark)
c.line(72,94,98,81,wooddark)
# gable front under roof: vertical face on right
c.poly([(66,73),(85,38),(105,54),(105,60),(66,79)],wooddark)
c.poly([(72,71),(85,46),(99,57)],'#aa8b68')
c.line(85,46,85,66,wooddark)
c.line(77,61,95,52,wooddark)
# furnace arched black opening left wall
c.poly([(35,83),(35,69),(38,65),(44,65),(51,69),(54,74),(54,93)],ink)
c.poly([(37,83),(37,71),(40,68),(44,68),(49,71),(51,75),(51,89)],'#562d32')
# stone arch blocks
c.poly([(32,79),(36,81),(36,71),(32,69)],stone)
c.poly([(33,68),(37,70),(40,66),(36,63)],lightstone)
c.poly([(37,62),(41,65),(45,66),(45,62),(41,60)],edge)
c.poly([(46,64),(50,66),(54,71),(50,72)],'#a89b8d')
c.poly([(51,73),(56,75),(56,92),(52,90)],stone)
c.line(33,70,36,72,'#4c4751');c.line(51,80,55,82,'#4c4751')
# visible fiery hearth
c.poly([(38,82),(39,76),(41,78),(43,71),(45,78),(47,76),(49,84),(50,88)],'#ed6638')
c.poly([(39,83),(42,79),(44,76),(45,82),(47,80),(48,87)],'#ffae4e')
c.poly([(41,84),(43,80),(44,83),(46,84),(46,87)],'#ffe39b')
c.line(37,85,50,91,'#b64232');c.line(38,85,50,91,'#ffd079')
c.poly([(32,86),(50,95),(58,91),(40,82)],'#5b4b4c')
c.line(33,86,50,94,'#e19557');c.line(50,94,57,91,'#a16245')
# sturdy red roof: ridge direction clean 2:1 isometry
c.poly([(15,53),(37,18),(87,43),(111,57),(66,80)],ink)
c.poly([(16,51),(38,17),(87,41),(65,76)],roofshadow)
c.poly([(18,50),(39,19),(84,41),(64,73)],red)
# broad rows across tiled roof slope
for i in range(6):
 y=22+i*5; x=37-i*3
 c.line(x,y,x+44,y+22,reddark)
 c.line(x,y-1,x+44,y+21,redlight)
 # staggered individual tile seams
 for j in range(6):
  xx=x+3+j*7+(3 if i%2 else 0); yy=y+int((xx-x)/2)
  if xx <= x+43:
   c.line(xx,yy,xx-3,yy+4,reddark)
# bright roof edge and staggered tips
c.line(18,50,64,73,'#ee7b59')
c.line(18,51,64,74,reddark)
c.poly([(17,53),(64,77),(66,80),(16,55)],wooddark)
c.line(19,54,64,76,woodlight)
# far narrow roof slope, right gable silhouette
c.poly([(85,40),(108,55),(112,58),(105,60),(84,45),(65,77),(63,75)],reddark)
c.line(85,41,109,56,redlight)
c.line(85,44,65,77,'#e2674b')
c.line(89,47,69,79,roofshadow)
# ridge terracotta cap tiles
c.poly([(36,17),(39,15),(89,40),(86,44)],reddark)
c.line(39,16,88,40,'#ed8b65')
c.line(37,18,86,43,'#c85743')
for x,y in [(43,18),(51,22),(59,26),(67,30),(75,34),(83,38)]:
 c.line(x,y,x-2,y+3,'#873338')
# small square chimney, placed through back roof plane
c.poly([(67,30),(67,13),(77,8),(85,12),(85,29),(76,34)],ink)
c.poly([(69,15),(76,18),(76,32),(69,29)],'#958587')
c.poly([(76,18),(83,14),(83,28),(76,32)],'#635d6c')
c.line(69,21,75,24,'#514954');c.line(77,24,82,21,'#413e4c')
c.line(72,16,72,22,'#b6a398');c.line(79,17,79,22,'#92838a')
c.poly([(66,12),(77,6),(87,11),(76,17)],'#b3a599')
c.poly([(70,12),(77,9),(83,11),(76,14)],'#2a2933')
c.poly([(66,12),(76,17),(76,20),(66,15)],'#857981')
c.poly([(76,17),(87,11),(87,14),(76,20)],'#5a5362')
# wisps of warm smoke in discrete pixel clusters
c.poly([(76,5),(74,3),(75,1),(80,1),(82,3),(79,5)],'#a2a2ad')
c.set(73,2,'#777b8b');c.set(81,0,'#c0bac0')
# right facade window with golden panes
c.poly([(89,66),(97,62),(97,75),(89,79)],wooddark)
c.poly([(90,67),(96,64),(96,73),(90,76)],'#e9a453')
c.line(93,66,93,75,'#5f433e');c.line(90,71,96,68,'#5f433e')
c.line(89,79,98,75,woodlight)
# hanging wooden sign on iron bracket right
c.line(101,67,113,61,ink);c.line(101,68,112,62,'#81747b')
c.line(110,63,110,68,ink);c.line(118,62,118,66,ink)
c.poly([(106,71),(120,64),(120,76),(106,83)],ink)
c.poly([(107,72),(119,66),(119,75),(107,81)],woodlight)
c.line(108,76,118,71,'#865434');c.line(108,80,118,75,'#d9a060')
# little dark anvil symbol on the sign
c.poly([(109,72),(117,68),(116,72),(114,74),(114,76),(111,77),(112,74),(110,75)],'#3b3037')
# blacksmith anvil in foreground, steel silhouette
c.poly([(57,101),(66,96),(75,100),(66,105)],'#393641')
c.poly([(62,99),(66,97),(69,99),(69,105),(64,108),(61,106)],'#444650')
c.poly([(52,92),(63,89),(77,95),(72,99),(62,100),(56,97)],'#30333e')
c.poly([(52,91),(63,87),(78,94),(72,96),(62,97),(55,94)],'#9d9fa6')
c.line(56,92,63,89,'#d0c9bb');c.line(63,89,75,95,'#b5b6bc')
c.poly([(57,95),(62,97),(72,96),(72,99),(63,101),(57,98)],'#565969')
# barrel helper: hoops lie on horizontal isometric ellipses
def barrel(x,y):
 c.ellipse(x,y+12,8,4,ink)
 c.rect(x-8,y,17,12,ink)
 c.ellipse(x,y,8,4,ink)
 c.rect(x-7,y,15,11,wood)
 c.ellipse(x,y+10,7,4,wood)
 c.rect(x-5,y+1,3,11,woodlight)
 c.line(x,y+2,x,y+12,'#946541');c.line(x+4,y+1,x+4,y+11,wooddark)
 c.ellipse(x,y,7,3,'#c08c57')
 c.line(x-5,y-1,x+4,y+2,'#805137');c.line(x-2,y-2,x+5,y+1,'#805137')
 for dy in [3,9]:
  c.path(f'M {x-7} {y+dy-1} Q {x} {y+dy+5} {x+7} {y+dy-1}', '#3f424d',fill=False)
  c.set(x-5,y+dy+1,'#a0a0a1');c.set(x-4,y+dy+2,'#787f87')
 c.set(x+2,y-1,'#563e33')
# stacked supplies at left corner
barrel(19,83)
barrel(31,92)
barrel(22,73)
# scattered coals and useful hand tools
for x,y in [(41,98),(45,100),(39,96),(49,102)]:
 c.rect(x,y,2,2,'#3a333c')
c.set(44,100,'#d66a3e');c.set(39,96,'#a94a36')
c.line(77,104,87,99,woodlight);c.poly([(84,98),(87,96),(92,98),(89,101)],'#9599a3');c.line(85,98,89,100,'#c0bab1')
view(result)
finish(result)
