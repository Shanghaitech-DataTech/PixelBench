import random
random.seed(8)
result = new_canvas(128,128,background='#65cafa',name='summer-seaside')
c=result
# clear luminous sky
c.rect(0,0,128,17,'#65cafa')
c.rect(0,17,128,18,'#7bd4fc')
c.rect(0,35,128,14,'#91dffc')
# sun, with discrete warm corona
c.circle(105,17,10,'#a4e5ee')
c.circle(105,17,8,'#ffe48a')
c.circle(105,17,6,'#fff5bb')
c.rect(102,12,4,2,'#fffbdc')
# soft stepped clouds
def cloud(x,y):
    c.rect(x,y+6,26,5,'#c8e8f6')
    c.rect(x+3,y+3,20,6,'#effbff')
    c.rect(x+8,y,9,8,'#effbff')
    c.rect(x+6,y+2,14,7,'#ffffff')
    c.rect(x-2,y+7,31,2,'#effbff')
cloud(13,11)
cloud(63,27)
c.rect(0,38,16,3,'#d8f4fc'); c.rect(3,36,8,3,'#edfaff')
# ocean horizontal bands
c.rect(0,48,128,13,'#2475b5')
c.line(0,48,127,48,'#408ac5')
c.rect(0,61,128,10,'#238fc1')
c.rect(0,71,128,10,'#20a9ca')
c.rect(0,81,128,15,'#36c0ce')
# diagonal shoreline and sand
shore=[(0,80),(16,83),(32,88),(48,91),(63,92),(78,90),(95,86),(111,82),(127,80),(127,128),(0,128)]
c.poly(shore,'#f5d58d')
c.poly([(0,85),(17,88),(31,93),(47,97),(65,98),(81,95),(98,91),(114,87),(127,86),(127,96),(112,97),(95,101),(73,106),(49,106),(27,101),(11,97),(0,97)],'#f9dfa0')
# wet sand edge
c.poly([(0,80),(16,83),(32,88),(48,91),(63,92),(78,90),(95,86),(111,82),(127,80),(127,84),(111,86),(95,90),(78,94),(63,96),(48,95),(32,92),(16,87),(0,84)],'#d9c687')
# surf, pale turquoise shallow wash
c.poly([(0,76),(17,79),(32,83),(49,87),(65,88),(79,86),(97,82),(113,78),(127,76),(127,81),(112,84),(96,88),(79,92),(64,94),(48,93),(31,90),(15,85),(0,82)],'#8ae1d9')
# stepped foamy shoreline
for dy,col in [(0,'#eaffee'),(1,'#ffffff')]:
    pts=[(0,80+dy),(12,82+dy),(21,85+dy),(32,88+dy),(48,91+dy),(63,92+dy),(78,90+dy),(96,86+dy),(113,82+dy),(127,80+dy)]
    for a,b in zip(pts,pts[1:]):c.line(*a,*b,col)
# rolling wave crest
pts=[(0,70),(14,72),(28,76),(44,78),(62,78),(79,76),(96,72),(111,70),(127,69)]
for a,b in zip(pts,pts[1:]):c.line(*a,*b,'#b9f5ef')
for x,y,w in [(0,71,6),(18,74,7),(30,77,9),(47,79,12),(66,78,7),(86,74,9),(103,71,10),(120,70,8)]:c.rect(x,y,w,1,'#f6fff4')
# ocean flecks, controlled horizontal glints
for i in range(76):
    x=random.randrange(128); y=random.randrange(51,83)
    # keep glints within sea above incoming surf
    edge=75+int(10*(1-abs(x-55)/75))
    if y<edge:
        color= '#4b9dcb' if y<61 else ('#5ac6d9' if y<71 else '#76ddd9')
        c.rect(x,y,min(random.choice([2,3,4,6]),128-x),1,color)
for x,y in [(5,79),(22,85),(29,86),(45,90),(57,90),(73,89),(90,86),(103,82),(119,80)]:
    c.rect(x,y,3,1,'#ffffff')
# distant sailboat and reflection
c.line(91,48,91,64,'#f8f1d1')
c.poly([(89,49),(89,60),(79,60)],'#ffffff')
c.poly([(93,52),(99,60),(93,60)],'#e1f3f5')
c.poly([(78,62),(101,62),(97,65),(83,65)],'#fff8de')
c.line(83,65,97,65,'#164f86')
c.rect(85,68,10,1,'#69c7de')
c.rect(88,70,5,1,'#69c7de')
# two gulls, two pairs of angled wings
for x,y in [(49,22),(65,13)]:
    c.line(x-5,y-2,x-2,y-1,'#35758f');c.line(x-2,y-1,x,y+1,'#35758f')
    c.line(x,y+1,x+2,y-1,'#35758f');c.line(x+2,y-1,x+5,y-2,'#35758f')
    c.set(x-3,y-2,'#ffffff');c.set(x+3,y-2,'#ffffff')
# sparse sand texture
for i in range(95):
    x=random.randrange(128);y=random.randrange(95,128)
    c.rect(x,y,min(random.choice([1,2]),128-x),1,random.choice(['#e9c77f','#ffe8ae','#ffe8ae']))
# umbrella long cast shadow
c.poly([(32,98),(38,98),(71,112),(66,117),(48,115),(24,105)],'#dbb875')
c.poly([(34,99),(39,99),(67,113),(56,112)],'#cfa86d')
# towel shadow and towel perspective
c.poly([(77,98),(100,102),(91,123),(65,117)],'#d2ae71')
c.poly([(77,96),(100,100),(89,121),(64,115)],'#fffae5')
c.poly([(75,100),(98,104),(95,109),(72,104)],'#31a6b9')
c.poly([(70,109),(93,113),(90,118),(67,113)],'#31a6b9')
c.line(77,97,99,101,'#ffffff')
c.line(65,115,89,120,'#e8e7cc')
for x,y in [(65,116),(69,117),(73,118),(77,119),(81,120),(85,121),(89,122)]:c.line(x,y,x-1,y+1,'#fff8df')
# umbrella pole
c.line(34,72,34,100,'#a46c48');c.line(35,72,35,99,'#fff1ba')
c.rect(33,100,4,1,'#b58a56')
# bold striped canopy domed silhouette
c.poly([(7,77),(11,70),(18,63),(27,59),(34,57),(42,59),(52,64),(59,71),(63,77)],'#bd3c4d')
c.poly([(8,75),(12,69),(19,63),(28,59),(34,58),(25,65),(20,74),(19,78),(14,76)],'#f65459')
c.poly([(34,58),(25,65),(19,77),(27,75),(34,78),(34,63)],'#fff9df')
c.poly([(34,58),(35,77),(43,75),(49,78),(45,67),(41,62)],'#f65459')
c.poly([(35,58),(42,60),(51,65),(58,72),(62,77),(55,75),(49,78),(45,67),(40,61)],'#fff9df')
# scalloped valance and ribs
c.poly([(7,76),(13,75),(19,77),(19,80),(14,79),(10,79)],'#d7424f')
c.poly([(19,77),(26,75),(34,77),(34,80),(28,79),(24,79)],'#e9e5ce')
c.poly([(34,77),(42,75),(49,77),(47,80),(41,79),(35,80)],'#d7424f')
c.poly([(49,77),(55,75),(63,77),(60,80),(55,79),(50,80)],'#e9e5ce')
c.line(34,59,25,65,'#ff8080');c.line(25,65,20,74,'#ff8080')
c.line(35,60,41,64,'#fffef0')
c.rect(33,55,3,3,'#c13f4f');c.set(34,55,'#ffe4ba')
# flipflops on the right, clear separation from towel
for x,y in [(106,107),(116,110)]:
    c.ellipse(x+1,y+3,4,7,'#d5ae70')
    c.ellipse(x,y,3,6,'#1c6684')
    c.ellipse(x,y-1,3,5,'#258eac')
    c.line(x-2,y-2,x,y+1,'#ffc360');c.line(x,y+1,x+2,y-3,'#ffc360')
    c.set(x,y+2,'#ffdf88')
# small shell and beach stones
c.poly([(12,113),(14,110),(17,110),(19,113),(18,115),(14,115)],'#fff4d7')
c.line(15,111,15,114,'#e5b593');c.line(17,111,16,114,'#e5b593')
c.rect(45,121,3,1,'#d4ae6f');c.set(46,120,'#fff0c4')
assert result.stats()['size'] == (128,128) or result.stats()['size'] == [128,128]
assert result.stats()['colors_used'] <= 86
view(result)
save('summer-seaside',result)
finish(result)
