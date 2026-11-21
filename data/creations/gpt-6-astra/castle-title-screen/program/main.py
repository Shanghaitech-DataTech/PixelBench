import random
random.seed(19)
c = new_canvas(128,128,background='#211e35',name='Emberfall')
# Dusk: discrete horizontal colour fields
sky=[(0,16,'#383047'),(16,13,'#573b53'),(29,12,'#805065'),(41,12,'#ad6570'),(53,13,'#d68178'),(66,16,'#eca078')]
for y,h,col in sky:c.rect(0,y,128,h,col)
# Long stratified cloud banks
c.poly([(0,24),(8,24),(8,22),(25,22),(25,24),(39,24),(39,26),(57,26),(57,29),(44,29),(44,31),(18,31),(18,29),(0,29)],'#65445a')
c.rect(0,29,25,2,'#94566b');c.rect(12,31,40,1,'#b26a76')
c.poly([(70,23),(81,23),(81,20),(102,20),(102,22),(116,22),(116,25),(127,25),(127,32),(109,32),(109,30),(87,30),(87,28),(70,28)],'#4c354d')
c.line(89,31,118,31,'#8b5065');c.line(105,33,127,33,'#bb6b76')
# The low sun, golden rim and orange face
c.circle(36,55,22,'#f7b276');c.circle(36,56,20,'#f9bd79')
c.rect(17,61,39,1,'#f7ae6e')
c.rect(20,66,32,2,'#f3a068')
c.rect(24,71,25,2,'#ec9166')
# Clouds crossing the sun: warm fringes beneath mauve bodies
c.poly([(0,43),(11,43),(11,41),(20,41),(20,43),(30,43),(30,45),(45,45),(45,48),(26,48),(26,50),(9,50),(9,48),(0,48)],'#b96b74')
c.rect(2,48,20,1,'#e58c7a');c.rect(29,48,15,1,'#ed977b')
c.poly([(53,54),(64,54),(64,52),(77,52),(77,54),(96,54),(96,57),(83,57),(83,59),(61,59),(61,57),(53,57)],'#b36a75')
c.line(61,59,81,59,'#f0a084')
c.rect(0,62,12,2,'#d2827c');c.rect(0,65,7,1,'#f6ad86')
c.rect(1,73,20,1,'#f3b493');c.rect(53,70,15,1,'#efad8d')
# Far coast and ocean
c.poly([(0,78),(8,75),(14,75),(22,77),(28,77),(34,79),(47,79),(55,76),(63,77),(70,75),(80,78),(92,76),(106,78),(127,76),(127,87),(0,87)],'#886479')
c.rect(0,81,128,38,'#665b75')
c.rect(0,81,128,2,'#b8838e')
c.rect(0,86,128,8,'#7f6880');c.rect(0,94,128,8,'#615b76');c.rect(0,102,128,10,'#4a4c66');c.rect(0,112,128,8,'#383d56')
# Shattered sunset path on water
for y in range(83,113,2):
    half=int(5+(y-82)*.48)
    x=36-half+random.randint(-4,4)
    col= '#e9a08b' if y<91 else ('#bb8591' if y<101 else '#8e7288')
    c.rect(x,y,half*2+random.randint(-3,3),1,col)
    if y%4==1:c.rect(x+5,y+1,half,1,'#aa7c8e')
for i in range(84):
    y=random.randrange(84,119);x=random.randrange(0,125)
    if 19<x<56:continue
    col= '#a17b8b' if y<95 else '#706880'
    c.rect(x,y,min(random.randrange(2,8),128-x),1,col)
# Seaward rock stacks
c.poly([(3,96),(5,89),(8,86),(10,88),(11,94),(16,98)],'#43415c')
c.line(0,99,19,99,'#a48a9b')
c.poly([(52,101),(55,94),(57,94),(59,99),(64,102)],'#3c3c56')
c.line(51,103,65,103,'#8f7a90')
# Cliff silhouette, fractured broad slabs
c.poly([(67,76),(81,72),(103,73),(117,69),(127,70),(127,117),(105,114),(97,108),(88,107),(83,100),(77,98),(75,90),(69,87)],'#353449')
c.poly([(67,77),(82,75),(93,77),(86,83),(84,94),(79,90),(77,84),(70,85)],'#876271')
c.poly([(83,79),(99,78),(95,87),(97,92),(90,102),(84,97),(86,88)],'#604d64')
c.poly([(100,78),(116,74),(111,86),(114,93),(105,109),(96,105),(101,94),(96,88)],'#4c4158')
c.poly([(117,76),(127,73),(127,111),(119,106),(115,95),(118,86)],'#625065')
c.poly([(70,78),(78,78),(74,81),(73,86),(70,84)],'#b37b77')
c.line(80,81,78,87,'#ad7878');c.line(88,81,87,87,'#967080');c.line(87,91,86,96,'#967080')
c.line(102,83,100,89,'#7b5b70');c.line(121,82,118,90,'#8c6475')
c.line(110,96,106,103,'#706078');c.line(94,94,91,99,'#302e43')
c.poly([(66,75),(79,72),(91,73),(101,71),(114,69),(127,69),(127,74),(112,75),(101,78),(84,77),(77,79),(68,78)],'#494451')
c.line(67,75,81,73,'#c18a78');c.line(83,74,96,74,'#a88177');c.line(102,73,112,71,'#a88177')
# Castle courtyard and walls
D='#302e45'; S='#554457'; M='#7f5c66'; L='#bf8579'; H='#e3a386'
c.rect(77,60,36,14,D);c.rect(78,61,34,11,S)
c.rect(78,62,34,2,M);c.line(79,63,110,63,L)
for x in range(78,112,5):c.rect(x,58,3,5,S);c.line(x,58,x+2,58,L)
# Main keep behind front wall
c.rect(87,49,14,15,S);c.rect(87,49,3,15,M)
c.poly([(85,49),(94,40),(103,49)],D);c.line(85,49,94,40,L);c.line(87,49,101,49,M)
c.rect(93,53,3,6,D);c.rect(93,53,1,4,'#dc9478')
# Two tall, asymmetrical towers
for x,y,w in [(75,41,10),(104,36,11)]:
    c.rect(x,y,w,33 if x==75 else 37,D)
    c.rect(x+1,y+1,w-2,30 if x==75 else 34,S)
    c.rect(x+1,y+1,2,29 if x==75 else 33,M)
    c.line(x+1,y+3,x+1,y+29,L)
    c.rect(x-1,y-1,w+2,4,D)
    c.rect(x,y-1,w,2,M)
    c.line(x,y-1,x+w-1,y-1,L)
    for xx in [x-1,x+3,x+w-2]:
        c.rect(xx,y-4,3,4,S);c.line(xx,y-4,xx+2,y-4,L)
    for yy in [y+7,y+18]:
        c.rect(x+5,yy,2,5,D);c.set(x+5,yy+1,'#d78c74');c.set(x+5,yy+2,'#eeb180')
    for yy in range(y+6,y+31,6):
        c.line(x+2,yy,x+3,yy,M);c.set(x+7,yy+3,M)
    # Flags flying inland on fine poles
    px=x+4;top=y-16
    c.line(px,top,px,y-5,D);c.set(px,top,H)
    c.poly([(px+1,top+1),(px+7,top+2),(px+12,top+1),(px+10,top+5),(px+12,top+7),(px+6,top+7),(px+1,top+5)],'#9f5264')
    c.line(px+1,top+1,px+6,top+2,'#f0a080');c.line(px+1,top+2,px+1,top+4,'#d37b73')
# Gate arch and raised threshold
c.path('M 91 74 L 91 68 Q 94 62 97 68 L 97 74 Z',D)
c.line(91,68,91,73,M);c.rect(93,68,2,6,'#201f35');c.line(90,74,99,74,L)
c.poly([(92,76),(97,76),(102,79),(100,82),(94,81),(90,82),(87,81),(94,79)],'#9c7578')
# Small masonry glints
for x,y in [(86,66),(99,66),(86,70),(101,71),(89,58),(98,59)]:c.rect(x,y,2,1,M)
# Clifftop scrub silhouettes
for x,y in [(68,74),(119,68),(123,68),(115,71)]:
    c.line(x,y,x,y-4,'#373748');c.line(x,y-2,x-2,y-3,'#373748');c.line(x,y-1,x+2,y-3,'#373748')
# Birds to anchor the scale
for x,y in [(56,36),(62,39),(19,57)]:
    c.line(x-2,y,x,y+1,'#67485e');c.line(x,y+1,x+2,y,'#67485e')
# Dark foreground rocks frame the entire vista
c.poly([(0,107),(6,105),(12,109),(15,114),(25,112),(32,117),(43,119),(48,127),(0,127)],'#22263c')
c.poly([(0,107),(6,105),(12,109),(6,108),(3,111),(0,111)],'#55506a')
c.poly([(16,115),(25,112),(32,117),(25,116),(21,118)],'#45465f')
c.poly([(73,127),(82,118),(88,118),(94,111),(102,114),(110,108),(119,109),(127,105),(127,127)],'#22263c')
c.poly([(94,111),(102,114),(98,115),(93,114),(87,120),(83,120)],'#51475f')
c.poly([(110,108),(119,109),(127,105),(127,108),(120,112),(114,111),(106,115)],'#65536a')
c.poly([(112,116),(119,113),(125,114),(127,121),(122,119),(117,120)],'#303149')
# Foreground grass and crevices
for x,y in [(4,108),(10,111),(29,117),(99,114),(124,108)]:
    c.line(x,y,x-1,y-5,'#22263c');c.line(x,y,x+2,y-3,'#22263c')
c.line(12,118,17,123,'#171e32');c.line(102,121,107,118,'#171e32')
# Title lettering with a one-pixel shadow; restrained menu ornament
c.text(38,9,'EMBERFALL','#211e35')
c.text(37,8,'EMBERFALL','#f9d4a2')
c.line(20,11,31,11,'#b58178');c.set(18,11,'#f0b68d');c.set(33,11,'#f0b68d')
c.line(94,11,105,11,'#b58178');c.set(108,11,'#f0b68d')
c.line(49,19,76,19,'#a47779');c.set(62,18,'#edb68f');c.set(62,20,'#edb68f')
c.text(35,119,'PRESS START','#181d30');c.text(34,118,'PRESS START','#d2ac99')
# Consolidate near-identical accents into the final limited palette.
merges = {c.color(a):c.color(b) for a,b in [('#f7ae6e','#f3a068'),('#f6ad86','#f0a084'),('#efad8d','#f0a084'),('#181d30','#171e32')]}
for y in range(128):
    for x in range(128):
        old=c.get(x,y)
        if old in merges:c.set(x,y,merges[old])
view(c)
save('emberfall',c)
finish(c)
