result = new_canvas(128,128,name='red_roofed_forge')
c=result
P={'ink':'#292632','deep':'#38303a','stone':'#68646a','stoneLight':'#999087','mortar':'#49454e','cream':'#c8b79a','plaster':'#a68d73','shade':'#7d685c','wood':'#664536','woodHi':'#ac7950','woodDark':'#432f2b','redDark':'#702f38','red':'#ac3e3d','redMid':'#c54e42','redLight':'#ed7855','roofShade':'#8b3338','metal':'#646c77','metalLight':'#a3a7a4','ember':'#dc4c28','orange':'#ff923f','gold':'#ffd777','hot':'#fff1b0'}
def poly(pts,col): c.poly(pts,P.get(col,col))
def line(a,b,col): c.line(*a,*b,P.get(col,col))
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
# beveled stone foundation, small diamond tile
poly([(9,88),(62,61),(119,89),(119,94),(65,122),(9,94)],'ink')
poly([(10,88),(63,62),(118,89),(65,116)],'#696761')
poly([(10,89),(65,116),(65,121),(10,94)],'#47474b')
poly([(65,116),(118,89),(118,94),(65,121)],'#55565a')
line((13,90),(64,115),'#8e8878'); line((66,115),(116,90),'#939080')
# fitted paving stones
for pts in [[(13,86),(25,80),(37,86),(25,92)],[(19,96),(31,90),(43,96),(31,102)],[(34,104),(46,98),(58,104),(46,110)],[(50,112),(62,106),(74,112),(65,117)],[(77,108),(89,102),(101,108)],[(91,99),(104,92),(115,97)],[(105,86),(113,82),(119,86),(112,90)]]:
 poly(pts,'#7a786e'); c.poly(pts,'#55565a',fill=False)
# building foundation
poly([(24,72),(67,94),(110,72),(110,81),(67,103),(24,81)],'ink')
poly([(25,73),(67,95),(67,101),(25,80)],'#625c5b')
poly([(68,95),(109,74),(109,80),(68,101)],'#858078')
for x in [31,44,57]: line((x,77+(x-25)//2),(x,81+(x-25)//2),'mortar')
for x in [78,92,104]: line((x,90-(x-68)//2),(x,96-(x-68)//2),'mortar')
# plaster walls
poly([(25,42),(68,64),(68,95),(25,73)],'plaster')
poly([(68,64),(90,37),(110,42),(110,74),(68,96)],'cream')
poly([(27,48),(65,67),(65,89),(27,70)],'#b59a7d')
poly([(70,66),(107,47),(107,72),(70,91)],'#cfbc99')
# side structural timbers
poly([(25,43),(29,45),(29,75),(25,73)],'woodDark')
poly([(64,61),(69,63),(69,96),(64,94)],'woodDark')
line((65,65),(65,92),'woodHi')
poly([(27,68),(65,87),(65,92),(27,73)],'wood')
line((29,69),(63,86),'woodHi')
poly([(27,49),(63,67),(63,70),(27,52)],'wood')
poly([(28,71),(31,73),(61,68),(58,66)],'wood')
# right corner beam and gable beams
poly([(106,45),(110,43),(110,75),(106,77)],'woodDark')
line((107,48),(107,73),'woodHi')
line((70,64),(107,45),'woodDark'); line((70,65),(107,46),'wood')
poly([(88,42),(91,41),(91,53),(88,55)],'wood')
# small gable vent
poly([(94,44),(101,44),(101,48),(94,52)],'woodDark')
line((96,46),(96,49),'metal');line((99,45),(99,48),'metal')
# roof dark overhang
poly([(20,43),(47,13),(92,35),(115,40),(115,45),(68,69),(20,46)],'ink')
poly([(47,15),(70,19),(114,41),(91,38)],'roofShade')
line((50,16),(91,36),'redLight')
# broad tiled roof plane
poly([(21,42),(48,15),(91,37),(68,65)],'redDark')
# courses and staggered tile seams on parallelogram
# left-to-right ridge axis and down-slope vector
A=(48,16); U=(42,21); V=(-26,27)
def rp(t,s): return (round(A[0]+U[0]*t+V[0]*s),round(A[1]+U[1]*t+V[1]*s))
for row in range(6):
 s0=row/6; s1=(row+1)/6
 poly([rp(0,s0),rp(1,s0),rp(1,s1),rp(0,s1)], ['redMid','red','redMid','red','redMid','red'][row])
 line(rp(0,s1),rp(1,s1),'redDark')
 line(rp(0,s0+0.025),rp(1,s0+0.025),'redLight' if row%2==0 else '#da6150')
 for j in range(7):
  t=(j+(0.5 if row%2 else 0))/6
  if 0<t<1: line(rp(t,s0+0.03),rp(t,s1),'roofShade')
# outer roof edge and individual endcaps
line((21,43),(67,66),'redDark');line((22,42),(67,64),'#ef855d')
line((68,65),(92,37),'redDark');line((69,64),(92,38),'redLight')
line((47,15),(90,36),'#f18a62')
for i in range(7):
 x=48+i*6;y=16+i*3
 line((x,y),(x+1,y+2),'redDark')
# furnace masonry on right wall: skewed arch opening
poly([(76,91),(76,68),(79,61),(84,57),(96,51),(102,53),(105,59),(105,77)],'mortar')
poly([(78,89),(78,68),(81,62),(85,59),(96,54),(100,55),(103,60),(103,77)],'#8d8277')
# arch block highlights
line((79,66),(83,62),'stoneLight');line((84,60),(89,57),'#beb09a');line((91,56),(96,54),'#beb09a')
line((99,55),(101,59),'#b3a490')
line((80,62),(83,65),'mortar');line((86,58),(87,62),'mortar');line((94,54),(94,58),'mortar')
# black inner vault
poly([(82,85),(82,69),(84,65),(88,62),(96,58),(99,61),(99,78)],'deep')
poly([(84,82),(84,72),(88,67),(96,63),(97,66),(97,78)],'#612e2b')
# warm furnace cheeks
line((81,72),(81,85),'#b86339');line((100,64),(100,78),'#c19063')
for y in [73,79,85]: line((77,y),(81,y-2),'mortar')
for y in [63,69,75]: line((100,y),(104,y-2),'mortar')
# licking flames
poly([(83,81),(85,73),(87,76),(89,67),(91,70),(94,63),(95,71),(97,69),(98,78),(91,83)],'ember')
poly([(85,80),(87,75),(89,77),(91,70),(93,73),(95,68),(95,77),(97,77),(90,82)],'orange')
poly([(88,80),(90,75),(91,78),(93,73),(94,78),(92,81)],'hot')
# charcoal grate and hearth lip
line((83,82),(98,75),'woodDark')
for x,y in [(85,81),(89,79),(93,77),(97,75)]: line((x,y),(x,y+3),'ink')
poly([(76,89),(103,75),(108,78),(81,92)],'#a2947c')
poly([(81,92),(108,78),(108,81),(81,95)],'#625c59')
line((80,90),(103,78),'#e3ae6b')
# exposed plaster gable beneath the roof edge
poly([(72,62),(92,40),(109,44)],'cream')
line((72,62),(92,40),'woodDark')
line((73,62),(92,42),'woodHi')
line((92,40),(109,44),'woodDark')
line((72,63),(108,45),'woodDark')
line((90,44),(90,53),'wood')
poly([(94,44),(100,45),(100,47),(94,50)],'woodDark')
line((96,45),(96,48),'metal')
line((99,46),(99,47),'metal')
# chimney rises through roof, chunky stone flue
poly([(59,28),(59,9),(69,4),(78,9),(78,27),(68,32)],'ink')
poly([(60,10),(68,14),(68,30),(60,26)],'#797175')
poly([(68,14),(77,10),(77,26),(68,31)],'#a49a8b')
for y in [17,23]:
 line((60,y),(68,y+4),'mortar');line((69,y+4),(76,y),'#6d6866')
line((64,12),(64,19),'mortar');line((72,18),(72,24),'#6d6866')
poly([(57,8),(68,3),(80,8),(69,14)],'#b9aca0')
poly([(57,8),(69,14),(69,17),(57,11)],'#655e62')
poly([(69,14),(80,8),(80,11),(69,17)],'#89827d')
poly([(62,8),(68,5),(75,8),(69,11)],'deep')
line((62,8),(68,5),'ink')
# hanging sign bracket on side wall
line((33,51),(33,58),'ink');line((33,52),(48,59),'ink')
line((34,52),(48,58),'metal')
line((39,56),(39,61),'woodDark');line((48,60),(48,65),'woodDark')
poly([(35,58),(54,67),(54,78),(35,69)],'woodDark')
poly([(36,60),(53,68),(53,76),(36,68)],'woodHi')
line((37,65),(52,72),'wood');line((37,61),(52,68),'#d2a36a')
# simple hammer icon on sign
poly([(40,62),(46,65),(46,68),(40,65)],'#e6c995')
line((44,66),(44,71),'#e6c995')
c.set(37,62,'#ead4a4');c.set(52,73,'#ead4a4')
# barrel helper with shaped silhouette, staves, hoops and oval lid
def barrel(x,y):
 poly([(x-6,y-6),(x-4,y-9),(x+3,y-9),(x+6,y-6),(x+7,y+5),(x+4,y+8),(x-3,y+8),(x-7,y+5)],'woodDark')
 poly([(x-5,y-5),(x-3,y-7),(x+3,y-7),(x+5,y-5),(x+6,y+4),(x+3,y+6),(x-3,y+6),(x-6,y+4)],'woodHi')
 poly([(x+2,y-6),(x+5,y-5),(x+6,y+4),(x+3,y+6),(x+2,y+6)],'wood')
 for dx in [-3,0,3]: line((x+dx,y-5),(x+dx,y+5),'wood')
 for dy in [-3,4]:
  poly([(x-6,y+dy-2),(x,y+dy),(x+6,y+dy-2),(x+6,y+dy),(x,y+dy+2),(x-6,y+dy)],'metal')
  line((x-5,y+dy-1),(x,y+dy+1),'metalLight')
 c.ellipse(x,y-6,5,3,P['woodDark']);c.ellipse(x,y-7,4,2,'#bc8b57')
 line((x-2,y-8),(x+2,y-6),'wood');c.set(x+3,y+4,'#c4b9a4')
# stacked supply barrels
barrel(25,88);barrel(39,95);barrel(30,77)
# smith's anvil on a wooden block in forecourt
poly([(59,102),(67,98),(74,102),(74,109),(67,113),(59,109)],'woodDark')
poly([(60,103),(67,106),(67,111),(60,108)],'wood')
poly([(67,106),(73,103),(73,108),(67,111)],'woodHi')
line((70,106),(70,109),'wood')
poly([(56,94),(68,89),(78,94),(73,98),(68,100),(70,103),(73,104),(67,108),(60,104),(64,101),(63,98),(58,97)],'ink')
poly([(56,94),(68,90),(77,94),(68,98),(61,97)],'metalLight')
poly([(61,97),(68,100),(74,97),(72,100),(68,102),(68,105),(63,103),(65,101),(64,98)],'metal')
line((58,94),(67,91),'#d4d3bc');line((64,104),(67,106),'#a5a9a6')
# scattered coal and hot cinders near hearth
for x,y in [(88,96),(92,92),(94,96),(99,88),(85,99)]:
 rect(x,y,2,2,'deep')
c.set(92,92,P['ember']);c.set(99,88,P['orange'])
assert c.stats()['size'] == (128,128) or c.stats()['size'] == [128,128]
assert c.stats()['colors_used'] <= 86
view(c)
save('red_roofed_forge',c)
finish(result)
