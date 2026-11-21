result = new_canvas(64,64, '#101a30', name='rainy_corner')
c=result
# restrained night palette
ink='#11182b'; navy='#1b2942'; blue='#293d58'; wet='#344d66'; rain='#66879b'
# night skyline
c.rect(0,8,12,36,navy); c.rect(3,4,8,5,navy)
c.rect(53,4,11,40,'#17243b'); c.rect(58,0,6,6,'#17243b')
for x,y in [(2,14),(8,23),(57,10),(61,22)]: c.rect(x,y,2,3,'#34445a')
c.rect(0,43,64,21,'#20354e')
c.poly([(0,55),(23,45),(62,44),(64,64),(0,64)],'#293e57')
# building shadow, side wall and front
c.rect(7,16,49,31,ink)
c.rect(9,18,45,27,'#485262')
c.rect(10,21,43,22,'#777979')
c.rect(10,42,45,4,'#343b4c')
c.rect(53,20,3,24,'#303b50')
# roof fascia and unbranded light sign
c.rect(7,12,49,8,'#10182b')
c.rect(9,13,45,5,'#487e88')
c.rect(10,13,43,1,'#78b8b2')
c.rect(19,14,23,3,'#f3d993')
# abstract sign stripes only
c.rect(12,15,4,1,'#a3d4c3'); c.rect(46,15,5,1,'#a3d4c3')
c.rect(6,19,51,3,'#1b3548'); c.rect(7,19,49,1,'#74a5a3')
c.rect(8,22,47,1,'#172638')
# bright glass windows
c.rect(11,23,26,18,'#e3a764')
c.rect(12,24,24,15,'#ffd58c')
c.rect(12,24,24,2,'#fff0b8')
c.rect(12,27,24,1,'#e9be79')
# shelves and tiny stock
for y in [30,35]:
    c.rect(13,y,22,1,'#9d7055')
    c.rect(13,y+1,22,1,'#f3bd73')
for x,col,h in [(14,'#bb7159',3),(18,'#788a70',2),(22,'#ae7056',3),(26,'#70918a',2),(31,'#bc7758',3)]:
    c.rect(x,30-h,2,h,col); c.set(x,30-h,'#fff0b8')
for x,col in [(14,'#738d84'),(19,'#c38558'),(24,'#9d685d'),(29,'#788c72'),(33,'#ae7056')]:
    c.rect(x,33,2,2,col)
c.rect(12,37,24,3,'#c18b61')
# window framing and highlights
c.rect(23,23,2,18,'#3d5559'); c.rect(11,40,26,2,'#263e4c')
c.line(13,24,13,36,'#ffe9ac'); c.line(26,25,26,32,'#fff0b8')
c.line(28,37,33,32,'#f5d59a')
# door opening
c.rect(38,22,14,22,'#172b3b')
c.rect(40,24,10,18,'#f4bd78'); c.rect(40,24,10,2,'#ffedb1')
c.rect(41,27,8,12,'#cc925d')
c.rect(42,28,6,1,'#e9b672')
# open glass door swung outward right
c.poly([(49,24),(54,27),(54,43),(49,41)],'#35515a')
c.poly([(50,26),(53,28),(53,39),(50,38)],'#83aaa0')
c.line(51,28,51,36,'#c6d3ab'); c.set(52,36,'#ffe1a0')
c.rect(38,43,16,2,'#929083'); c.rect(37,45,19,2,'#172b40')
c.line(39,45,52,45,'#baac80')
# reflected light on wet pavement, broken horizontal clusters
c.poly([(13,46),(35,46),(42,60),(6,60)],'#394d5c')
for x,y,w,col in [(15,47,18,'#b5a072'),(11,49,12,'#758879'),(25,49,10,'#b2a078'),(9,51,8,'#647e7c'),(20,52,14,'#a18f70'),(12,54,13,'#c1a174'),(27,55,10,'#6b7e79'),(5,58,16,'#758a85'),(18,59,12,'#b69b74'),(40,48,10,'#bd9867'),(41,50,13,'#7a8274'),(43,53,7,'#a29572'),(45,56,10,'#617c7d')]: c.rect(x,y,w,1,col)
c.line(0,61,18,61,'#46637a'); c.line(29,62,46,62,'#48677c')
c.line(51,59,63,59,'#55758a'); c.line(54,60,60,60,'#38566e')
# umbrella stand beside entrance
c.rect(33,40,5,6,'#172b3b'); c.rect(34,41,3,4,'#5e757b')
c.line(33,41,37,41,'#9db2ad'); c.line(34,43,36,43,'#243c4c')
# folded umbrellas and curved handles
c.line(34,33,34,40,'#e09d77'); c.set(35,32,'#e5b48b'); c.set(36,33,'#e5b48b')
c.poly([(33,36),(35,35),(35,40)],'#b86e67')
c.line(37,34,36,40,'#a8bdac'); c.set(38,33,'#a8bdac')
c.line(36,37,36,40,'#577a8a')
# person stepping into doorway: shadow, boots, coat
c.ellipse(44,47,4,1,'#192c40')
c.rect(42,43,2,4,'#192c3c'); c.rect(45,42,2,3,'#192c3c'); c.rect(45,44,3,1,'#142536')
c.poly([(42,33),(46,33),(48,42),(46,44),(40,43),(40,39)],'#b87a38')
c.poly([(42,33),(45,33),(46,42),(41,42),(41,37)],'#efbe59')
c.line(42,35,41,40,'#ffe18b'); c.line(46,35,48,37,'#efbe59'); c.line(48,37,50,35,'#e3aa51'); c.set(50,35,'#f0c397')
# hood facing right
c.poly([(42,29),(45,29),(47,31),(47,34),(42,35),(40,33),(41,30)],'#d8a044')
c.rect(42,30,3,3,'#f5cd68'); c.rect(45,31,2,3,'#775f45'); c.set(47,32,'#edb77e'); c.set(44,30,'#ffe28e')
# parked bicycle left foreground
c.line(1,55,26,55,'#162a3e')
for x in [6,23]:
    c.circle(x,51,5,ink); c.circle(x,51,4,'#849ba1',fill=False)
    c.line(x-3,48,x+3,54,'#425e73'); c.line(x-3,54,x+3,48,'#425e73'); c.set(x,51,'#b3c1b6')
# diamond frame
for a,b in [((6,51),(11,44)),((11,44),(15,51)),((15,51),(6,51)),((11,44),(20,44)),((20,44),(15,51)),((20,44),(23,51))]: c.line(*a,*b,'#c38375')
c.line(19,41,23,51,'#9aa9a5'); c.line(19,41,22,40,'#b5c3b7'); c.set(23,40,ink)
c.line(11,43,11,41,'#aeb6a9'); c.rect(8,41,6,2,ink); c.line(9,41,12,41,'#657c87')
c.circle(15,51,1,'#bec0ab'); c.line(15,51,17,53,'#adb7ae'); c.line(16,53,18,53,ink)
c.line(18,52,18,55,'#142638')
# rain streaks, selectively in open areas
for x,y,n in [(2,1,3),(15,2,3),(29,0,3),(44,4,3),(55,1,3),(61,7,4),(6,7,2),(20,8,2),(37,5,3),(59,28,4),(3,30,3),(0,39,3),(60,39,3),(57,49,2),(32,57,2),(3,56,2),(38,51,2),(60,54,2)]:
    c.line(x,y,x-1 if x else x,y+n,rain)
# awning drips
for x,y in [(8,23),(29,22),(55,24)]: c.line(x,y,x,y+2,'#8aadae')
# small ripple pairs
for x,y in [(4,45),(57,46),(30,60),(53,55)]:
    c.line(x,y,x+3,y,'#6c8b9a'); c.set(x+1,y+1,'#415d74')
# Cool contour separates the warm raincoat from the illuminated doorway.
c.line(40,34,39,39,'#35515a')
c.line(39,39,39,43,'#35515a')
c.line(41,29,40,31,'#35515a')
c.line(41,28,45,28,'#35515a')
c.line(47,30,48,32,'#35515a')
# Consolidate closely related shades into a compact final palette.
from collections import Counter
counts=Counter(c.get(x,y) for y in range(64) for x in range(64))
pal={p['index']:p['rgba'] for p in c.palette()}
remap={i:i for i in counts}
while len(counts)>72:
    ids=list(counts)
    a,b=min(((a,b) for j,a in enumerate(ids) for b in ids[j+1:]), key=lambda ab: sum((pal[ab[0]][k]-pal[ab[1]][k])**2 for k in range(3))*(1+min(counts[ab[0]],counts[ab[1]])/80))
    if counts[a]>counts[b]: a,b=b,a
    for i in remap:
        if remap[i]==a: remap[i]=b
    counts[b]+=counts.pop(a)
for y in range(64):
    for x in range(64):
        i=c.get(x,y)
        if remap[i]!=i: c.set(x,y,remap[i])
view(c)
finish(result)
