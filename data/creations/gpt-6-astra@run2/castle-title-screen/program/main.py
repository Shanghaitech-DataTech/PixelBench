import random
random.seed(18)
result = new_canvas(128,128,background='#302b4e',name='Ember Tide')
c=result
# restrained sunset palette
sky0='#302b4e'; sky1='#493650'; sky2='#65405b'; sky3='#8b4e63'; sky4='#b96369'; sky5='#d77c70'; sky6='#ee9b79'
ink='#171f32'; deep='#242b40'; rock='#343449'; stone='#4d4356'; shade='#39384e'; warm='#79606b'; lit='#ad7e78'; gold='#f6c889'; cream='#ffe3a1'; orange='#f6ad69'
# Broad horizontal atmosphere
for y,h,col in [(24,12,sky1),(36,10,sky2),(46,10,sky3),(56,10,sky4),(66,10,sky5),(76,7,sky6)]: c.rect(0,y,128,h,col)
# sunset disc with a stepped silhouette
c.circle(35,57,20,'#ef975f')
c.circle(35,56,18,'#ffbb70')
c.rect(19,62,33,4,'#f8aa64')
c.rect(23,69,25,4,'#f39a60')
# Long banks of sculpted clouds
def cloud(points,col): c.poly(points,col)
cloud([(0,29),(9,29),(9,27),(22,27),(22,28),(28,28),(28,30),(43,30),(43,32),(54,32),(54,34),(37,34),(37,35),(16,35),(16,34),(0,34)],'#784b63')
c.line(0,34,26,34,'#a96470');c.line(30,34,44,34,'#a96470')
cloud([(64,26),(76,26),(76,24),(88,24),(88,25),(94,25),(94,27),(108,27),(108,28),(127,28),(127,34),(110,34),(110,32),(89,32),(89,30),(64,30)],'#65405b')
c.line(86,32,107,32,'#95586b');c.line(113,34,127,34,'#95586b')
cloud([(0,44),(8,44),(8,42),(18,42),(18,43),(23,43),(23,45),(29,45),(29,47),(13,47),(13,48),(0,48)],'#9c596c')
c.line(0,48,11,48,'#d77c70')
cloud([(42,47),(50,47),(50,45),(60,45),(60,46),(64,46),(64,48),(73,48),(73,50),(55,50),(55,49),(42,49)],'#a55d6c')
c.line(49,50,64,50,'#d77c70')
cloud([(0,62),(8,62),(8,60),(17,60),(17,62),(27,62),(27,64),(15,64),(15,65),(0,65)],'#c17174')
c.line(4,65,18,65,'#efa280')
cloud([(41,67),(54,67),(54,65),(66,65),(66,67),(76,67),(76,70),(56,70),(56,69),(41,69)],'#cf7c79')
c.line(48,70,69,70,'#f4b38a')
# Distant coastline across the horizon
c.poly([(65,78),(70,76),(75,76),(81,72),(87,73),(93,70),(102,71),(107,68),(113,69),(118,65),(127,67),(127,83),(65,83)],'#986c7c')
# Sea bands
c.rect(0,81,128,47,'#655a76')
c.rect(0,86,128,10,'#50516c')
c.rect(0,96,128,16,'#3a435e')
c.rect(0,112,128,16,deep)
c.line(0,81,72,81,'#e9a88b')
# horizontal sea ripples and sunset reflection
for y in range(83,111,2):
    center=34+(y%5)-2
    radius=7+(y-81)//3
    for j in range(3):
        x=center-radius+random.randrange(max(1,radius*2))
        length=random.randrange(2,8)
        c.line(x,y,min(x+length,64),y,random.choice(['#d38a87','#e9a88b','#ae7c87']))
for x,y,l,col in [(1,86,10,'#8c7188'),(49,84,15,'#af8190'),(2,92,12,'#767089'),(53,91,15,'#82758b'),(3,101,10,'#61617e'),(42,104,14,'#68647e'),(63,99,14,'#68647e'),(19,114,15,'#4f546e'),(6,107,16,'#50516c'),(58,109,18,'#50516c')]: c.line(x,y,x+l,y,col)
# Cliff mass, angular rock strata
cliff=[(70,85),(79,80),(93,81),(104,76),(127,75),(127,128),(75,128),(79,119),(84,115),(80,107),(83,102),(75,98),(76,93),(69,91)]
c.poly(cliff,rock)
c.poly([(75,88),(83,85),(92,85),(88,93),(89,99),(84,102),(82,98),(82,93),(74,91)],warm)
c.poly([(93,84),(104,80),(112,81),(107,89),(103,94),(104,99),(97,108),(94,120),(86,126),(88,113),(91,106),(90,97)],stone)
c.poly([(112,81),(127,78),(127,111),(119,115),(120,102),(113,98),(116,90)],shade)
c.poly([(77,93),(82,95),(81,100),(86,104),(83,112),(78,116),(80,106),(75,100)],shade)
c.poly([(104,95),(110,91),(107,103),(101,109),(99,120),(94,124),(96,111)],deep)
c.poly([(120,84),(124,81),(122,96),(118,100),(120,92)],stone)
c.line(84,88,81,91,lit);c.line(94,89,92,94,warm);c.line(99,104,95,109,warm)
c.line(115,103,112,110,rock)
# Grass rim and retaining walls
c.poly([(68,86),(76,82),(88,82),(95,79),(105,77),(127,76),(127,81),(111,82),(103,81),(93,85),(78,86),(72,89)],'#55545c')
c.line(73,85,89,83,'#9b8276');c.line(96,81,105,79,'#9b8276')
# castle silhouette: two unequal fortified towers
c.rect(81,55,36,25,shade)
c.rect(83,59,29,19,stone)
# central roof behind walls
c.poly([(89,61),(99,49),(109,61)],deep)
c.line(90,60,99,50,warm)
c.rect(93,61,15,13,stone)
c.rect(94,61,2,13,warm)
# tower helper, machicolations and crenels
def tower(x,top,w,bottom):
    c.rect(x,top+7,w,bottom-top-7,shade)
    c.rect(x+1,top+8,w-5,bottom-top-8,stone)
    c.rect(x+1,top+8,2,bottom-top-8,warm)
    c.rect(x-1,top+3,w+2,5,shade)
    c.rect(x-1,top+3,w-2,3,lit)
    for xx in range(x-1,x+w+1,4):
        c.rect(xx,top,2,4,warm)
        c.set(xx,top,lit)
    c.line(x-1,top+7,x+w,top+7,deep)
    for xx in range(x+1,x+w-1,3): c.set(xx,top+6,deep)
    for yy in range(top+12,bottom-2,6):
        c.line(x+2,yy,x+4,yy,warm)
        c.line(x+w-4,yy+3,x+w-2,yy+3,deep)
    for yy in [top+11,top+23]:
        if yy+3<bottom:
            c.rect(x+w//2,yy,2,4,deep)
            c.set(x+w//2,yy+1,'#e5ad78')
tower(78,48,12,81)
tower(108,39,13,79)
# banner poles and wind-tossed swallowtails
for x,y in [(83,36),(114,27)]:
    c.line(x,y,x,y+12,deep)
    c.set(x,y,gold)
    c.poly([(x+1,y+1),(x+6,y+2),(x+12,y+1),(x+10,y+4),(x+12,y+6),(x+6,y+7),(x+1,y+5)],'#a24e63')
    c.line(x+1,y+1,x+6,y+2,'#eea477')
    c.line(x+1,y+2,x+1,y+5,'#eea477')
# front curtain crenels
c.rect(89,70,19,10,stone)
c.line(90,70,107,70,lit)
for x in range(90,108,4): c.rect(x,67,2,3,warm); c.set(x,67,lit)
c.line(89,72,107,72,deep)
# arched doorway
c.rect(97,75,5,6,deep);c.rect(98,74,3,1,deep)
c.line(97,76,97,80,warm)
c.set(101,79,'#d9996d')
# path snaking down the headland
c.poly([(99,81),(103,81),(99,84),(90,86),(87,89),(80,90),(81,88),(90,84),(96,84)],'#a18a7b')
c.line(88,86,94,84,'#c69d82')
# tiny birds, deliberate paired pixels
for x,y in [(59,57),(65,60),(13,73)]:
    c.line(x-2,y-1,x,y,sky2);c.line(x,y,x+2,y-1,sky2)
# water around foot of cliff
for x,y,w in [(71,104,7),(69,111,9),(65,116,12),(55,121,17)]:
    c.line(x,y,x+w,y,'#77758b');c.line(x+2,y+1,x+w-2,y+1,'#4f546e')
# dramatic dark foreground rock framing
c.poly([(0,96),(5,98),(9,105),(14,107),(16,112),(23,112),(29,118),(40,121),(47,127),(0,127)],ink)
c.poly([(0,98),(5,101),(7,108),(14,112),(5,111),(0,107)],rock)
c.line(1,98,5,101,'#585064')
c.poly([(14,114),(21,114),(27,120),(19,119)],deep)
c.poly([(103,128),(108,118),(114,116),(115,110),(120,107),(122,101),(127,99),(127,128)],ink)
c.poly([(115,111),(121,109),(124,103),(127,102),(127,108),(122,114)],deep)
# little foreground grasses
for x,y in [(4,101),(13,112),(117,111),(123,105)]:
    c.line(x,y,x-2,y-5,ink);c.line(x,y,x+1,y-6,ink)
# title typography and fine ornamental rules
c.text(30,11,'EMBER TIDE',ink,spacing=2)
c.text(30,10,'EMBER TIDE',gold,spacing=2)
c.line(32,21,56,21,'#916b72'); c.line(71,21,95,21,'#916b72')
c.poly([(63,19),(65,21),(63,23),(61,21)],gold)
c.set(28,21,gold);c.set(99,21,gold)
# restrained menu prompt on dark footer
c.rect(37,116,55,10,ink)
c.text(40,118,'NEW GAME','#d0ad91',spacing=1)
c.set(34,120,gold);c.set(35,121,gold);c.set(34,122,gold)
view(c)
finish(result)
