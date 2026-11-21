import random, math
rng = random.Random(41)
result = new_canvas(128,128,background='#3c354f',name='Embertide')
c = result
P = {
'sky0':'#3c354f','sky1':'#51405a','sky2':'#6e4863','sky3':'#925768','sky4':'#b96b71','sky5':'#d98277','sky6':'#e99a7d','sky7':'#f1ad83',
'cloud0':'#51445f','cloud1':'#70516a','cloud2':'#926277','cloud3':'#bd7e87','cloudrim':'#edaa94',
'sunedge':'#ed8c55','sun0':'#f5934b','sun1':'#ffad55','sun2':'#ffc16a','sun3':'#ffd080',
'distant':'#74647e','distantlight':'#a18496','seadark':'#474b6c','sea':'#5b5b7b','seamid':'#77708c','sealit':'#a08a9c','foam':'#c6a8ae',
'reflect0':'#b9848e','reflect1':'#dc9b90','reflect2':'#f4b181','reflect3':'#ffca89',
'ink':'#20283f','deep':'#2a304a','rock0':'#3a3b55','rock1':'#505066','rock2':'#6b5e72','rock3':'#997779','rock4':'#c69783','grass':'#525967','grasslit':'#a19a87',
'wallshade':'#38465f','wall':'#566076','walllit':'#85808a','walledge':'#c6a18d','roof':'#31374e','rooflit':'#656179','roofedge':'#a78583',
'flag':'#cc7379','flaglit':'#f6b08b','window':'#f8c78b','gold':'#e8b879','goldlight':'#ffe4ae','goldshadow':'#b67d67'
}
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(x,y,xx,yy,col): c.line(x,y,xx,yy,P.get(col,col))
def poly(points,col): c.poly(points,P.get(col,col))
# Stepped atmospheric colour, intentionally broad and clean.
for y,h,k in [(0,21,'sky0'),(21,12,'sky1'),(33,10,'sky2'),(43,9,'sky3'),(52,9,'sky4'),(61,8,'sky5'),(69,6,'sky6'),(75,6,'sky7')]: rect(0,y,128,h,k)
# Wisps at the upper corners frame the title.
poly([(0,6),(12,6),(12,8),(21,8),(21,11),(16,11),(16,13),(0,13)],'cloud0')
rect(0,13,12,1,'cloud1')
poly([(114,3),(127,3),(127,11),(108,11),(108,9),(101,9),(101,7),(114,7)],'cloud0')
rect(115,12,13,1,'cloud1')
# Large low sun: bright, hard-edged horizontal colour strata.
c.circle(36,55,24,P['sunedge'])
c.circle(36,55,23,P['sun0'])
for y in range(36,79):
    for x in range(12,61):
        if (x-36)**2+(y-55)**2 <= 23**2:
            k='sun0' if y<44 else 'sun1' if y<55 else 'sun2' if y<65 else 'sun3'
            c.set(x,y,P[k])
# Banks of layered clouds, with stepped silhouettes and warm undersides.
poly([(0,27),(8,27),(8,25),(20,25),(20,27),(28,27),(28,29),(38,29),(38,32),(48,32),(48,34),(36,34),(36,35),(17,35),(17,34),(0,34)],'cloud0')
poly([(0,31),(16,31),(16,32),(30,32),(30,33),(41,33),(41,35),(24,35),(24,36),(6,36),(6,35),(0,35)],'cloud2')
rect(5,36,16,1,'cloud3');rect(27,35,11,1,'cloud3')
poly([(59,37),(66,37),(66,35),(79,35),(79,33),(94,33),(94,35),(103,35),(103,37),(119,37),(119,39),(127,39),(127,44),(102,44),(102,43),(85,43),(85,42),(64,42),(64,40),(52,40),(52,39),(59,39)],'cloud1')
poly([(58,40),(79,40),(79,41),(101,41),(101,42),(127,42),(127,45),(109,45),(109,44),(88,44),(88,43),(64,43),(64,42),(58,42)],'cloud3')
rect(70,43,13,1,'cloudrim');rect(112,45,16,1,'cloudrim')
# Long, thin cloud across the sun, asymmetrical gaps create depth.
poly([(0,47),(8,47),(8,46),(18,46),(18,47),(26,47),(26,49),(37,49),(37,51),(26,51),(26,52),(8,52),(8,51),(0,51)],'cloud2')
rect(0,51,17,1,'cloud3');rect(18,52,9,1,'cloudrim');rect(32,51,12,1,'cloud3')
poly([(0,61),(7,61),(7,59),(14,59),(14,60),(21,60),(21,62),(33,62),(33,64),(21,64),(21,65),(0,65)],'cloud3')
rect(0,65,13,1,'cloudrim');rect(28,64,10,1,'cloudrim')
poly([(66,58),(76,58),(76,56),(89,56),(89,57),(105,57),(105,59),(127,59),(127,64),(111,64),(111,63),(88,63),(88,62),(61,62),(61,60),(66,60)],'cloud3')
rect(52,67,17,1,'cloudrim');rect(62,69,23,1,'sky7');rect(1,71,14,1,'cloudrim')
# Far coast and ocean horizon.
poly([(0,75),(7,74),(11,71),(15,72),(20,75),(28,75),(35,77),(54,77),(54,81),(0,81)],'distant')
line(0,75,7,74,'distantlight');line(7,74,11,71,'distantlight')
rect(0,79,128,36,'sea')
rect(0,79,128,2,'sealit');rect(0,81,128,1,'seamid')
rect(0,90,128,7,'seadark');rect(0,97,128,5,'sea');rect(0,102,128,13,'seadark')
# Ocean colour planes and many horizontal, clustered glints.
for x,y,w,col in [(0,84,18,'seamid'),(5,86,17,'seamid'),(52,84,17,'seamid'),(0,88,13,'sealit'),(57,90,16,'seamid'),(9,94,13,'seamid'),(1,98,22,'seamid'),(50,97,26,'seamid'),(60,102,25,'sea'),(8,105,19,'sea'),(26,108,39,'sea'),(1,111,40,'sea'),(60,112,30,'sea')]: rect(x,y,w,1,col)
for y,x,w in [(80,28,22),(82,23,29),(84,29,18),(86,22,29),(88,26,24),(90,19,32),(92,22,24),(94,15,33),(96,21,25),(98,17,39),(101,24,25),(104,15,42),(107,23,24),(110,15,39)]:
    rect(x,y,w,1,'reflect0')
    inset=rng.randint(2,7)
    rect(x+inset,y,max(3,w-inset-rng.randint(3,9)),1,'reflect1' if y>92 else 'reflect2')
    if y<95: rect(x+inset+3,y, max(2,w//3),1,'reflect3')
    if y in (84,90,96,104): rect(x-4,y+1,8,1,'reflect0')
for i in range(44):
    x=rng.randrange(0,87); y=rng.randrange(83,114)
    if abs(x-35)<14 and y<100: continue
    rect(x,y,rng.choice([2,3,4,6]),1,rng.choice(['sea','seamid','sealit']) if y<98 else rng.choice(['sea','seamid']))
# Tiny distant rock and a pale sea edge at the foot of the headland.
poly([(1,85),(4,82),(7,83),(9,85)],'seadark');rect(0,85,12,1,'sealit')
poly([(81,90),(85,90),(91,99),(99,103),(109,109),(126,111),(127,117),(108,115),(94,108),(87,103),(82,97)],'seamid')
line(86,98,94,105,'foam');line(96,106,106,110,'sealit');rect(107,112,10,1,'foam')
# Sheer seaside cliff, broken into large faces and deep fissures.
poly([(65,80),(73,77),(88,77),(98,75),(115,77),(127,75),(127,115),(115,114),(103,110),(96,103),(86,99),(80,92),(71,90),(71,86),(65,85)],'deep')
poly([(67,80),(79,78),(87,80),(84,88),(88,97),(82,91),(74,89),(74,85),(68,84)],'rock3')
poly([(78,80),(93,78),(98,84),(96,95),(104,105),(98,102),(91,97),(87,89),(84,87)],'rock2')
poly([(92,80),(105,78),(108,90),(105,98),(114,112),(104,107),(101,100),(96,97),(99,90)],'rock1')
poly([(108,80),(122,79),(127,83),(127,112),(119,110),(115,100),(117,91)],'rock0')
poly([(69,81),(75,81),(76,85),(80,85),(80,88),(75,87),(73,84),(69,84)],'rock4')
poly([(81,81),(84,82),(82,88),(85,93),(81,89)],'rock4')
poly([(88,80),(93,80),(92,88),(96,94),(94,95),(89,88)],'rock3')
poly([(102,81),(105,81),(105,89),(102,93),(104,99),(101,96),(102,89)],'rock2')
poly([(112,83),(116,83),(113,91),(116,98),(112,97),(110,90)],'rock1')
line(88,91,92,96,'rock0');line(94,99,98,100,'rock3');line(105,102,109,108,'rock2')
line(122,87,119,96,'deep');line(119,96,123,104,'deep');line(113,103,116,110,'deep')
for x,y,w,col in [(69,82,4,'rock4'),(76,84,3,'rock2'),(82,86,2,'rock3'),(90,85,3,'rock4'),(94,91,2,'rock3'),(100,83,4,'rock2'),(106,85,2,'rock3'),(110,88,3,'rock2'),(118,82,5,'rock2'),(121,97,3,'rock1'),(109,105,3,'rock1'),(97,99,3,'rock1')]: rect(x,y,w,1,col)
# Broken seams catch the last light along the rock faces.
poly([(74,83),(76,83),(77,87),(79,89),(77,88)],'rock2')
poly([(87,82),(89,82),(88,86),(90,90),(92,93),(90,92),(86,87)],'rock1')
line(78,89,82,90,'rock0');line(83,94,87,96,'rock3')
line(89,98,93,100,'rock2');line(96,102,100,104,'rock0')
line(100,85,101,89,'rock3');line(106,93,107,97,'rock2')
rect(119,86,4,1,'rock1');rect(117,89,3,1,'rock2')
rect(124,101,3,1,'rock2');line(120,104,122,108,'rock1')
# Thin surf, broken where the water slips behind the crags.
rect(83,99,4,1,'sealit');rect(88,103,4,1,'foam')
rect(94,107,4,1,'sealit');rect(101,110,6,1,'foam')
# Turf and retaining wall; a little bridge joins the outer ledge.
poly([(63,80),(69,77),(75,77),(80,75),(95,75),(101,74),(110,76),(121,75),(127,73),(127,79),(116,81),(102,80),(90,80),(80,82),(72,81),(67,83)],'grass')
line(65,80,73,78,'grasslit');line(73,78,85,78,'rock4');line(111,77,122,77,'grasslit')
rect(75,73,42,5,'wallshade');rect(75,73,42,1,'walledge');rect(78,75,32,1,'wall')
# Central keep, behind the two towers. Crenellations read in silhouette.
rect(83,57,23,18,'ink')
rect(85,58,19,16,'wall');rect(99,58,5,16,'wallshade')
rect(84,55,4,4,'wall');rect(92,55,4,4,'wall');rect(100,55,4,4,'wallshade')
rect(84,55,4,1,'walledge');rect(92,55,4,1,'walledge');rect(100,55,4,1,'walllit')
rect(85,60,16,1,'walllit');rect(86,62,3,1,'walllit');rect(94,64,3,1,'walllit');rect(87,68,3,1,'wallshade')
# Dark arched main gate and warm recess.
rect(93,69,5,7,'ink');rect(94,67,3,3,'ink');rect(94,70,1,5,'rock3');rect(95,69,2,6,'deep')
rect(88,63,2,4,'ink');rect(89,64,1,2,'window')
rect(100,63,2,4,'ink')
# Two slate-roofed towers. Pixel outlines and left-facing sunset edges.
def tower(x,top,base,width):
    # top is the roof apex; shaft begins 11 px below it
    left=x-width//2; right=left+width-1; sy=top+11
    rect(left-1,sy-1,width+2,base-sy+2,'ink')
    rect(left,sy,width,base-sy,'wall')
    rect(left,sy,2,base-sy,'walllit')
    rect(right-2,sy,3,base-sy,'wallshade')
    line(left,sy+1,left,base-2,'walledge')
    rect(left-2,sy-2,width+4,3,'roof')
    rect(left-1,sy-1,width+2,1,'roofedge')
    poly([(left-3,sy-3),(x,top),(right+3,sy-3)],'ink')
    poly([(left-1,sy-4),(x,top+1),(x+2,sy-4)],'rooflit')
    poly([(x,top+2),(x+2,sy-4),(right+1,sy-4)],'roof')
    line(left-1,sy-4,x,top+1,'roofedge')
    rect(left,sy+6,width,1,'wallshade')
    rect(left,sy+6,3,1,'walllit')
    # Narrow lancet windows.
    for wy in [sy+2,sy+10]:
        if wy+4<base:
            rect(x-1,wy+1,3,4,'ink');rect(x,wy,1,1,'ink')
            rect(x,wy+1,1,3,'window')
    for xx,yy in [(left+3,sy+8),(left+2,sy+17),(left+5,sy+20),(right-3,sy+14)]:
        if yy<base-1: rect(xx,yy,2,1,'walllit')
    rect(left-1,base-2,width+2,2,'wallshade');rect(left-1,base-2,3,1,'walledge')
    # Banner on a fine gold pole, flowing toward the sea.
    line(x,top-9,x,top,'ink');line(x,top-9,x,top-1,'walledge')
    poly([(x+1,top-9),(x+5,top-10),(x+10,top-8),(x+8,top-5),(x+4,top-6),(x+1,top-5)],'ink')
    poly([(x+1,top-8),(x+5,top-9),(x+9,top-7),(x+7,top-5),(x+4,top-6),(x+1,top-6)],'flag')
    line(x+1,top-8,x+5,top-9,'flaglit')
    c.set(x,top-10,P['goldlight'])
tower(78,43,77,10)
tower(108,36,78,12)
# Outer steps and low defensive wall continuing to the right.
rect(116,68,12,9,'wallshade');rect(116,68,12,1,'walllit')
for x in [117,123]: rect(x,65,3,4,'wallshade');rect(x,65,3,1,'walledge')
rect(118,71,3,1,'wall');rect(123,74,4,1,'wall')
for x,y,w in [(65,80,8),(68,78,7),(70,76,6)]: rect(x,y,w,1,'walledge')
# A few windswept birds in open sky.
for x,y in [(49,42),(56,47),(9,40)]:
    line(x-2,y,x,y+1,'cloud0');line(x,y+1,x+2,y,'cloud0')
# Near rocks create a widescreen-like framing and foreground depth.
poly([(0,96),(4,99),(7,98),(12,102),(14,108),(20,112),(24,112),(29,116),(35,119),(45,120),(51,124),(70,124),(77,121),(91,120),(97,116),(104,116),(111,109),(117,108),(121,104),(127,104),(127,127),(0,127)],'ink')
poly([(0,96),(4,99),(7,98),(12,102),(14,108),(20,112),(18,114),(10,111),(6,106),(0,105)],'rock0')
poly([(0,96),(3,100),(6,100),(10,104),(8,104),(4,102),(0,101)],'rock2')
poly([(0,108),(5,109),(11,114),(13,121),(7,119),(4,114),(0,114)],'deep')
poly([(15,112),(20,112),(24,114),(27,117),(36,121),(29,120),(24,117),(18,116)],'rock0')
line(17,112,22,114,'rock1')
poly([(96,117),(103,116),(110,110),(117,109),(121,105),(127,105),(127,112),(120,113),(116,117),(108,117),(102,121),(94,122)],'rock0')
poly([(105,115),(111,110),(116,110),(120,107),(120,109),(116,113),(111,113)],'rock2')
line(121,105,126,105,'rock3');line(111,110,116,110,'rock3')
poly([(118,116),(123,113),(127,113),(127,123),(124,120),(122,118),(114,122)],'deep')
# Foreground grasses are sparse silhouettes, with a rim of evening light.
for x,y in [(4,100),(20,114),(115,110),(124,105)]:
    line(x,y,x-2,y-5,'ink');line(x,y,x+1,y-7,'ink');line(x,y-1,x+3,y-4,'ink')
# Hand-built, serif gold title; each pixel is intentional and un-antialiased.
glyphs={
'E':['1111111','0110001','0110000','0110000','0110010','0111110','0110010','0110000','0110000','0110001','1111111'],
'M':['111000111','011000110','011101110','011101110','011010110','011010110','011000110','011000110','011000110','011000110','111000111'],
'B':['1111110','0110011','0110011','0110011','0111110','0110011','0110011','0110011','0110011','0110011','1111110'],
'R':['1111110','0110011','0110011','0110011','0111110','0111100','0110110','0110011','0110011','0110011','1110011'],
'T':['1111111','1001001','0001000','0001000','0001000','0001000','0001000','0001000','0001000','0001000','0011100'],
'I':['11111','00100','00100','00100','00100','00100','00100','00100','00100','00100','11111'],
'D':['1111100','0110110','0110011','0110011','0110011','0110011','0110011','0110011','0110011','0110110','1111100']}
title='EMBER TIDE'
width=sum(len(glyphs[ch][0])+1 if ch!=' ' else 4 for ch in title)-1
px=(128-width)//2; pixels=[]
for ch in title:
    if ch==' ': px+=4;continue
    for yy,row in enumerate(glyphs[ch]):
        for xx,b in enumerate(row):
            if b=='1': pixels.append((px+xx,9+yy))
    px+=len(glyphs[ch][0])+1
for x,y in pixels:
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(1,2)]: c.set(x+dx,y+dy,P['deep'])
for x,y in pixels: c.set(x,y,P['goldlight' if y<13 else 'gold' if y<18 else 'goldshadow'])
# Fine ornamental rule under the title.
line(36,24,58,24,'goldshadow');line(69,24,91,24,'goldshadow')
line(48,23,58,23,'gold');line(69,23,79,23,'gold')
poly([(63,21),(66,24),(63,27),(60,24)],'goldshadow')
c.set(63,23,P['goldlight']);c.set(62,24,P['gold']);c.set(63,25,P['gold'])
# Small title-screen prompt in the dark foreground.
c.text(32,119,'PRESS START',P['goldshadow'],font='5x7')
c.text(31,118,'PRESS START',P['goldlight'],font='5x7')
# Menu marker.
poly([(23,119),(26,121),(23,123)],'gold')
w,h,rgba=result.to_rgba()
visible_colors={tuple(rgba[i:i+4]) for i in range(0,len(rgba),4) if rgba[i+3] > 0}
assert (w,h)==(128,128)
assert len(visible_colors)<=86
print(f'Final output: {w}x{h}, {len(visible_colors)} visible colours.')
view(result,scale=4,margin=0)
save('ember-tide',result)
finish(result)
