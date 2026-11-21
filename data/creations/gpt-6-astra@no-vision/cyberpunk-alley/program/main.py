import random, math
rng=random.Random(21)
c=new_canvas(128,128,'#090d20',name='Neon rain')
# A limited, hue-shifted night palette.
P={
'void':'#070b16','ink':'#0b1020','deep':'#10172b','navy':'#14213a','slate':'#1a3047',
'blue':'#20445b','steel':'#2b5969','mist':'#36727d','teal':'#328f99','cyan':'#52d6d3','ice':'#a6f4e7',
'wall':'#191b30','brick':'#252137','mortar':'#121528','purple':'#32223f','plum':'#482745','wine':'#682c52',
'red':'#a83b68','pink':'#f0579c','hot':'#ff83b4','pale':'#ffd0d8',
'gold':'#fcb473','amber':'#c66f58','dimamber':'#744850','glass':'#183c50','reflect':'#23566b',
'ground':'#121c31','wet':'#1b2c44','violet':'#323452','muted':'#546078','white':'#d6f6ed'}
def rect(x,y,w,h,k): c.rect(x,y,w,h,P.get(k,k))
def line(x,y,xx,yy,k): c.line(x,y,xx,yy,P.get(k,k))
def poly(pts,k): c.poly(pts,P.get(k,k))
def dot(x,y,k): c.set(x,y,P.get(k,k))
# High, narrow opening and distant haze.
rect(43,0,43,80,'deep')
poly([(50,0),(75,0),(77,70),(47,76)],'navy')
rect(57,20,16,53,'slate')
rect(61,39,11,38,'blue')
rect(63,52,7,21,'steel')
rect(64,60,5,12,'mist')
# Far buildings, fire escapes and little lit windows.
poly([(39,10),(54,18),(54,77),(38,84)],'wall')
poly([(76,9),(91,1),(94,83),(75,75)],'deep')
for y in [23,35,47,58]:
    rect(48,y,3,5,'slate'); line(43,y+6,54,y+8,'ink')
for y in [19,31,43,55]:
    rect(78,y,4,5,'blue'); rect(79,y,1,3,'steel')
rect(56,53,4,16,'ink'); rect(57,54,2,12,'red')
line(56,53,60,53,'pink')
rect(69,45,5,3,'teal'); rect(70,45,3,1,'cyan')
rect(63,67,6,10,'ink'); line(64,67,69,67,'teal')
# Near architecture: perspective walls frame a narrow lane.
poly([(0,0),(35,0),(46,28),(46,84),(0,110)],'wall')
poly([(0,0),(17,0),(19,91),(0,104)],'brick')
poly([(34,0),(43,16),(45,85),(37,89)],'purple')
line(35,1,40,82,'wine')
poly([(93,0),(127,0),(127,108),(86,82),(86,21)],'deep')
poly([(113,0),(127,0),(127,110),(111,99)],'wall')
line(91,2,87,80,'blue'); line(94,4,91,82,'slate')
# Left brickwork broken by shadow.
for y in range(15,99,7):
    line(0,y,17,y-2,'mortar')
    for x in range((y//7%2)*7,18,13):
        line(x,y-5,x,y-1,'mortar')
for x,y in [(2,22),(7,55),(1,71),(25,49),(26,52),(32,72)]:
    line(x,y,x+4,y,'purple')
# Upper windows, mullions, air-conditioning unit.
rect(4,4,18,19,'ink'); rect(6,6,14,15,'purple')
rect(8,7,4,12,'dimamber'); rect(14,7,4,12,'wine')
line(5,21,23,21,'muted'); line(12,6,12,20,'ink'); line(6,14,19,14,'ink')
rect(25,8,9,16,'ink'); rect(27,10,5,12,'slate')
line(29,10,29,21,'deep'); line(26,24,35,25,'wine')
rect(0,26,16,9,'deep'); line(0,26,16,26,'muted')
for y in [28,30,32]: line(2,y,12,y,'slate')
rect(13,28,3,5,'ink')
# Pipes and utility conduits.
line(23,0,23,30,'ink'); line(24,0,24,29,'muted')
line(24,29,30,32,'muted'); line(30,32,30,62,'wine')
line(3,48,3,99,'ink'); line(4,49,4,97,'dimamber')
for y in [56,76,94]: line(2,y,5,y,'slate')
line(121,0,121,95,'ink'); line(122,0,122,96,'blue')
for y in [14,36,59,79]: line(120,y,124,y,'steel')
# Recessed right shop and rolling shutter.
poly([(96,49),(127,53),(127,98),(95,81)],'ink')
poly([(99,57),(126,61),(126,96),(98,80)],'slate')
for y in range(60,91,3):
    line(100,y,126,y+9,'deep')
line(97,55,97,81,'steel')
poly([(94,49),(127,53),(127,59),(93,54)],'blue')
line(94,49,127,53,'teal'); line(94,54,127,59,'ink')
# Tiny distant awning and alley lamps.
poly([(42,58),(54,60),(55,64),(42,63)],'wine')
line(42,58,54,60,'red')
rect(47,65,5,12,'ink'); rect(48,67,3,6,'dimamber')
line(53,26,59,26,'ink'); rect(57,26,3,2,'gold'); dot(58,28,'amber')
# Neon housings and crisp luminous tubes.
rect(2,35,36,14,'ink'); rect(3,36,34,12,'wine'); rect(4,37,32,10,'red')
rect(5,38,30,8,'purple')
c.text(6,39,'RAMEN',P['hot'],spacing=1)
line(4,37,35,37,'pink'); line(4,47,35,47,'pink'); line(3,38,3,46,'hot')
rect(36,39,3,6,'deep'); dot(37,40,'amber')
# Vertical blue sign, offset away from building.
line(100,16,109,16,'ink'); line(100,48,111,48,'ink')
rect(106,13,16,39,'ink'); rect(107,14,14,37,'blue')
rect(108,15,12,35,'teal'); rect(109,16,10,33,'deep')
line(108,16,108,49,'cyan'); line(120,16,120,49,'cyan')
line(109,15,119,15,'ice'); line(109,50,119,50,'cyan')
c.text(110,18,'夜',P['ice'],font='8px')
c.text(110,29,'市',P['cyan'],font='8px')
c.text(110,40,'場',P['cyan'],font='8px')
# Projecting warm sign in middle distance.
rect(79,37,10,17,'ink'); rect(80,38,8,15,'dimamber')
rect(81,39,6,13,'amber')
for y in [41,45,49]: line(82,y,85,y,'gold')
line(82,42,82,43,'gold'); line(85,46,85,47,'gold')
# Street surface, narrowing towards light at the vanishing point.
poly([(46,77),(63,71),(76,71),(91,79),(127,103),(127,127),(0,127),(0,103)],'ground')
poly([(63,73),(70,73),(86,128),(37,128)],'wet')
poly([(76,76),(87,80),(127,108),(127,116)],'navy')
line(0,108,48,79,'slate'); line(0,110,48,80,'ink')
line(89,81,127,106,'steel'); line(91,84,127,109,'ink')
line(60,78,19,127,'navy'); line(74,76,116,127,'navy')
# Irregular horizontal reflections: broken ribbons of neon on asphalt.
for x,y,w,k in [
(62,76,8,'steel'),(61,79,12,'teal'),(59,81,9,'blue'),(67,83,7,'mist'),
(39,85,13,'wine'),(33,89,17,'red'),(29,92,17,'wine'),(23,96,25,'wine'),
(19,101,29,'red'),(10,107,31,'wine'),(4,115,39,'wine'),(0,122,43,'purple'),
(81,82,9,'blue'),(86,86,12,'steel'),(89,90,13,'teal'),(91,95,20,'blue'),
(94,99,19,'teal'),(96,104,28,'blue'),(100,110,27,'steel'),(103,115,24,'teal'),
(108,120,20,'reflect'),(117,125,11,'steel'),(43,109,20,'violet'),(50,119,29,'slate')]:
    rect(x,y,w,1,k)
for pts,k in [([(8,112),(20,108),(46,108),(40,112),(25,114),(3,114)],'wine'),
              ([(0,119),(15,116),(43,116),(38,120),(19,121),(0,121)],'red'),
              ([(88,99),(106,99),(118,102),(100,103),(91,102)],'reflect'),
              ([(92,112),(112,112),(127,118),(127,121),(112,117),(94,115)],'blue'),
              ([(39,124),(51,121),(78,122),(91,127),(32,127)],'slate')]: poly(pts,k)
# Sharp reflection highlights with gaps.
for x,y,w,k in [(34,87,7,'pink'),(37,91,11,'red'),(23,98,13,'pink'),(29,98,5,'hot'),
(17,104,16,'pink'),(37,103,7,'red'),(12,110,13,'red'),(20,112,20,'pink'),
(4,118,13,'pink'),(26,117,7,'hot'),(10,120,15,'red'),(7,124,22,'wine'),
(87,88,5,'cyan'),(94,94,10,'cyan'),(96,101,12,'teal'),(105,102,7,'cyan'),
(104,107,10,'cyan'),(112,111,10,'ice'),(109,114,12,'teal'),(118,118,9,'cyan'),
(54,96,7,'blue'),(52,105,8,'steel'),(46,114,10,'blue'),(50,125,12,'mist')]: rect(x,y,w,1,k)
# Pavement seams and debris along edges.
for x,y,xx,yy in [(1,117,9,114),(6,127,14,122),(35,126,39,123),(112,122,118,125),(91,91,96,94)]: line(x,y,xx,yy,'ink')
rect(3,106,15,2,'ink')
for x in range(4,18,3): dot(x,106,'muted')
poly([(35,93),(39,92),(42,94),(38,96)],'muted'); line(37,93,40,94,'slate')
# Left vending machine, large enough for individual product rows.
poly([(12,64),(32,64),(36,68),(36,98),(31,101),(12,100)],'ink')
rect(13,65,19,34,'wine'); rect(14,66,17,32,'red')
rect(15,69,12,19,'ink'); rect(16,70,10,16,'glass')
rect(16,70,10,2,'cyan')
for y in [74,80]:
    for x,k in [(17,'pink'),(21,'gold'),(24,'ice')]:
        rect(x,y,2,4,k); dot(x,y-1,'steel')
    line(16,y+4,26,y+4,'steel')
rect(28,71,2,8,'plum'); dot(28,73,'ice'); dot(28,77,'cyan')
rect(28,83,2,2,'gold'); rect(17,91,10,5,'ink'); line(18,91,25,91,'dimamber')
line(14,66,30,66,'hot'); line(14,67,14,97,'pink'); line(31,68,31,98,'dimamber')
poly([(32,66),(35,69),(35,97),(32,99)],'purple')
rect(15,99,3,3,'ink'); rect(29,99,3,3,'ink')
# A second smaller vending machine beneath the right awning.
poly([(99,65),(113,68),(113,95),(99,89)],'ink')
poly([(100,66),(112,69),(112,93),(100,88)],'blue')
poly([(102,69),(110,71),(110,84),(102,81)],'ink')
for x in [103,106,109]:
    for y in [73,78]: rect(x,y,2,3,'teal'); dot(x,y,'cyan')
line(100,66,112,69,'ice'); line(100,67,100,87,'cyan')
rect(103,85,6,3,'ink'); dot(111,83,'gold')
# A few rubbish bags at the far wall, readable masses.
poly([(39,77),(43,75),(46,79),(46,86),(37,89),(36,84)],'ink')
line(39,79,40,84,'slate'); line(39,77,43,76,'muted')
poly([(116,94),(120,91),(125,93),(127,100),(127,105),(115,100)],'ink')
line(119,94,123,93,'slate')
# Heavy power cables sag across the opening. Double pixels at supports.
for d in ['M 0 9 Q 39 36 91 11 Q 111 5 127 9',
          'M 0 13 Q 43 43 103 17 L 127 14',
          'M 23 0 Q 45 25 79 23 Q 102 21 127 30',
          'M 35 31 Q 64 44 104 32']:
    c.path(d,P['void'],fill=False)
c.path('M 0 8 Q 39 35 91 10',P['slate'],fill=False)
c.path('M 36 30 Q 64 43 104 31',P['blue'],fill=False)
for x,y in [(38,26),(80,25),(98,15)]: rect(x,y,2,3,'ink'); dot(x,y,'muted')
# Fine rain, bright only where it catches a sign. Kept out of the silhouette.
for i in range(96):
    x=rng.randrange(1,127); y=rng.randrange(0,123)
    if 55<x<91 and y>76: continue
    if 11<x<37 and 63<y<102: continue
    length=rng.choice([1,2,2,3])
    k='slate'
    if x>92: k=rng.choice(['blue','steel','slate'])
    elif x<38 and 31<y<63: k=rng.choice(['wine','red','dimamber'])
    line(x,y,x-1,y+length,k)
# Rings and tiny splashes on the lit water.
for x,y,k in [(49,94,'steel'),(18,115,'red'),(94,109,'teal'),(56,117,'steel'),(34,123,'wine'),(110,98,'cyan'),(8,103,'red')]:
    line(x-2,y,x+2,y,k); dot(x-3,y-1,k); dot(x+3,y-1,k)
# Person and the contact reflection, central foreground.
poly([(69,119),(80,119),(84,125),(78,126),(65,126),(67,123)],'ink')
line(67,124,73,124,'purple'); line(77,125,81,125,'blue')
# Boots and separated legs.
poly([(69,107),(74,108),(73,119),(69,121),(66,120),(68,117)],'void')
poly([(75,107),(79,106),(79,117),(82,119),(81,121),(76,120),(74,115)],'void')
line(78,112,78,117,'blue'); line(67,120,71,120,'wine'); line(78,120,81,120,'teal')
# Coat, collar and bent arm holding the umbrella.
poly([(69,94),(75,93),(79,97),(79,105),(82,112),(67,113),(68,103),(65,100)],'void')
poly([(74,95),(77,97),(77,108),(80,111),(74,111)],'deep')
line(69,97,68,106,'wine'); line(67,107,67,111,'red')
line(77,96,79,99,'teal'); line(79,105,80,110,'steel')
line(71,101,72,109,'navy'); line(69,113,79,113,'ink')
# Head in profile, rim lit by both signs.
rect(70,88,7,7,'void'); rect(71,87,5,2,'void')
line(70,89,70,92,'wine'); rect(75,90,2,4,'slate'); dot(77,92,'steel')
line(72,95,75,95,'muted')
# Umbrella handle and arm, against the dark coat.
line(77,84,77,102,'steel'); line(78,85,78,99,'ink')
c.path('M 77 99 V 102 Q 75 105 74 102',P['muted'],fill=False)
poly([(78,98),(76,99),(73,99),(71,97),(70,98),(73,102),(77,101)],'ink')
line(74,99,77,98,'dimamber'); dot(77,99,'gold')
# Transparent dome: preserve architecture through broad dark glass panels.
# Sparse tinted planes, interrupted ribs and transmitted rain sell clear vinyl.
canopy=new_canvas(128,128,name='Clear vinyl')
canopy.poly([(57,86),(61,81),(68,78),(77,77),(85,80),(91,85),(93,88),(86,87),(80,89),(73,87),(65,89)],'#35778864')
canopy.poly([(59,85),(64,81),(71,79),(75,79),(69,83),(67,86)],'#6193a05c')
canopy.poly([(78,79),(84,81),(89,85),(88,86),(82,85)],'#4b94a878')
c=flatten([c,canopy],name='Cyberpunk alley')
# Visible city lights and rain transmitted through the plastic.
line(61,84,65,84,'wine'); line(60,85,64,85,'red')
line(87,84,89,85,'teal'); line(70,81,69,83,'blue')
line(82,82,81,84,'steel'); dot(65,83,'steel')
# Pixel arch, scalloped edge, metal ribs.
c.path('M 56 87 L 59 83 L 64 80 L 70 78 L 77 77 L 83 79 L 88 82 L 92 86 L 93 88',P['cyan'],fill=False)
line(63,80,69,78,'ice'); line(70,77,76,76,'ice')
c.path('M 56 87 Q 61 85 65 89 Q 69 86 73 88 Q 77 86 81 89 Q 87 85 93 88',P['steel'],fill=False)
c.path('M 77 78 Q 69 80 65 88 M 77 78 Q 77 82 81 88 M 77 78 Q 86 81 92 87',P['mist'],fill=False)
line(76,75,76,77,'white'); dot(56,87,'ice'); dot(93,88,'ice')
# A few trailing drops off the rim.
line(58,90,57,92,'steel'); dot(90,91,'cyan'); dot(64,92,'mist')
# Foreground rain streaks, a restrained final layer.
for x,y,k in [(7,8,'steel'),(45,4,'blue'),(60,11,'steel'),(99,5,'blue'),(104,58,'teal'),(7,85,'red'),(42,100,'steel'),(90,114,'blue'),(121,73,'steel'),(53,52,'mist'),(33,57,'red')]: line(x,y,x-1,y+4,k)
result=c
print(c.stats_text())
print(c.matrix_text(region=(54,75,94,96)))
save('cyberpunk-alley',result)
finish(result)
