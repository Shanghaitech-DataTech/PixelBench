import random
random.seed(18)
result=new_canvas(128,128,background='#edb18c',name='mountain-village-sunrise')
c=result
# A restrained dawn palette, laid in crisp bands.
c.rect(0,0,128,17,'#d99589'); c.rect(0,17,128,17,'#ebb093'); c.rect(0,34,128,24,'#f6c59b')
c.rect(9,13,24,2,'#efb49a'); c.rect(17,11,18,2,'#efb49a'); c.rect(93,20,26,2,'#f8c9a2'); c.rect(101,18,19,2,'#f8c9a2')
c.circle(65,30,12,'#f9dba6'); c.circle(65,30,9,'#ffe9b2')
# Far serrated ranges.
c.poly([(0,48),(10,39),(19,43),(32,26),(44,39),(53,34),(67,47),(82,30),(92,37),(108,24),(122,40),(127,36),(127,71),(0,71)],'#a897a7')
c.poly([(20,41),(32,26),(44,39),(36,35),(32,32),(28,38)],'#e9c3ba')
c.poly([(94,37),(108,24),(122,40),(111,34),(108,30),(103,35)],'#e9c3ba')
c.poly([(64,48),(82,30),(92,37),(84,36),(80,40),(77,40)],'#d1adb1')
c.poly([(0,55),(15,46),(29,52),(46,39),(59,50),(70,45),(85,57),(104,42),(117,50),(127,45),(127,78),(0,78)],'#7c8196')
c.poly([(29,52),(46,39),(43,48),(49,47),(56,52),(61,57),(48,53)],'#9895a5')
c.poly([(85,57),(104,42),(101,49),(109,50),(118,56)],'#9592a2')
c.poly([(0,64),(19,58),(34,62),(50,56),(69,63),(88,58),(111,61),(127,56),(127,84),(0,84)],'#697d83')
# Valley mist.
c.rect(25,65,70,2,'#a1a49b');c.rect(36,68,55,2,'#b3afa0')
def pine(x,y,h,shadow,light,trunk='#555c53'):
    c.rect(x-1,y-h//2,2,h//2+2,trunk)
    for f in [0.0,.21,.42]:
        top=y-h+int(h*f); bot=top+int(h*.56); w=int(h*(.19+f*.12))
        c.poly([(x,top),(x-w,bot),(x+w,bot)],shadow)
        c.poly([(x,top),(x-w,bot),(x-1,bot-2)],light)
for x,y,h in [(2,77,18),(12,74,23),(23,76,17),(35,72,14),(91,75,19),(101,74,24),(114,76,20),(124,73,26)]:
    pine(x,y,h,'#506b70','#68817b')
# Meadow terraces.
c.poly([(0,81),(17,76),(39,78),(59,72),(83,76),(104,73),(127,80),(127,128),(0,128)],'#7f8c72')
c.poly([(0,92),(22,84),(45,87),(67,82),(91,87),(127,81),(127,128),(0,128)],'#9a9c76')
c.poly([(0,105),(22,101),(47,106),(80,98),(105,103),(127,97),(127,128),(0,128)],'#697d61')
# The walkway widens toward the viewer.
c.poly([(61,83),(70,83),(73,92),(65,102),(65,109),(87,127),(52,127),(49,115),(50,105),(61,94)],'#545e59')
c.poly([(62,84),(69,84),(70,93),(60,104),(59,111),(80,127),(56,127),(52,114),(54,105),(64,93)],'#b6aa8c')
# Stone shapes with sunlit top edges.
for pts in [[(63,86),(68,86),(69,89),(63,89)],[(62,92),(68,92),(66,95),(60,95)],[(58,98),(64,97),(63,100),(56,101)],[(55,104),(60,103),(60,107),(54,108)],[(54,111),(59,110),(61,114),(55,115)],[(57,118),(64,116),(68,120),(61,122)],[(65,123),(70,121),(77,126),(68,127)],[(55,123),(59,122),(63,126),(56,127)]]:
    c.poly(pts,'#d2c1a0');c.line(*pts[0],*pts[1],'#eed5aa')
# Shadows under the three cabins.
c.ellipse(29,89,21,4,'#69765f');c.ellipse(101,87,22,4,'#69765f');c.ellipse(65,89,24,5,'#737a61')
def house(x,y,w,h):
    # y is wall top, gable projects above it
    roof='#443f49'; log='#9a604a'; shade='#704b40'; hi='#c38a58'
    c.rect(x,y,w,h,shade)
    c.rect(x+2,y,w-7,h-2,log)
    c.poly([(x-3,y),(x+w//2,y-15),(x+w+3,y),(x+w+3,y+3),(x-3,y+3)],roof)
    c.poly([(x+w//2,y-12),(x+2,y),(x+w-3,y)],'#ad7551')
    c.poly([(x+w//2,y-16),(x-5,y+1),(x-4,y+4),(x+w//2,y-11),(x+w+4,y+3),(x+w+5,y)],roof)
    for gy in [y-7,y-3]:
        half=(gy-(y-12))*(w-5)//24
        c.line(x+w//2-half,gy,x+w//2+half,gy,'#915b46')
        c.line(x+w//2-half,gy-1,x+w//2+half,gy-1,'#c38a58')
    c.line(x-4,y,x+w//2,y-15,'#e0ad74'); c.line(x+w//2,y-15,x+w+4,y,'#b57758')
    for yy in range(y+5,y+h-1,4):
        c.line(x+1,yy,x+w-2,yy,'#583f39');c.line(x+2,yy-1,x+w-7,yy-1,hi)
    c.rect(x,y+2,2,h-2,'#d09a62');c.rect(x+w-3,y+2,2,h-2,'#593e39')
    # Door and glowing windows.
    dx=x+w//2-2
    c.rect(dx,y+h-12,6,12,'#3e3c3e');c.rect(dx+1,y+h-11,4,10,'#77503d');c.set(dx+4,y+h-6,'#e7bc78')
    for wx in [x+4,x+w-10]:
        c.rect(wx,y+5,6,7,'#403d40');c.rect(wx+1,y+6,4,4,'#f7c673');c.line(wx+2,y+6,wx+2,y+9,'#b7804d');c.line(wx-1,y+12,wx+6,y+12,'#d3a06a')
    c.rect(dx-1,y+h,8,2,'#c4af8b');c.line(x,y+h-1,x+w-1,y+h-1,'#4f4942')
    # A masonry chimney tucked into the roof.
    cx=x+w-8
    c.rect(cx,y-14,4,9,'#77686a');c.line(cx,y-14,cx,y-7,'#bb9b8b');c.rect(cx-1,y-15,6,2,'#574f56')
    c.set(cx+2,y-10,'#b59886')
    return cx+2,y-16
s1=house(12,70,28,18)
s2=house(88,69,27,17)
s3=house(46,63,35,24)
# Central attic, golden trim and welcoming doorstep.
c.rect(61,57,6,5,'#493e3d');c.rect(62,58,4,3,'#ffda87');c.set(63,59,'#b77a4b')
c.line(48,65,78,65,'#dca56a')
c.rect(60,89,11,2,'#d3bb94');c.rect(59,91,13,2,'#7c7b68')
# Smoke curls drift into the dawn, rendered as stepped pixel clusters.
for sx,sy in [s1,s2,s3]:
    c.poly([(sx-1,sy),(sx+2,sy),(sx+2,sy-4),(sx+5,sy-7),(sx+5,sy-11),(sx+2,sy-14),(sx+1,sy-13),(sx+3,sy-10),(sx+2,sy-7),(sx-1,sy-5)],'#c4b2ae')
    c.line(sx,sy-2,sx,sy-5,'#e7ccc0');c.line(sx+1,sy-6,sx+3,sy-8,'#e7ccc0');c.rect(sx+1,sy-16,3,2,'#d8b9b0')
# Split rail fence provides scale beside the main path.
for x,y in [(7,98),(18,95),(29,94),(40,96),(87,96),(99,94),(112,95),(123,98)]:
    c.rect(x,y-7,2,10,'#645343');c.set(x,y-7,'#d3af79')
for a,b in [((7,94),(40,92)),((7,97),(40,95)),((87,92),(123,94)),((87,95),(123,97))]:
    c.line(*a,*b,'#a78459')
# Foreground pines frame the central light.
pine(8,112,53,'#2e514e','#42685a','#514b3e')
pine(122,114,59,'#294b4b','#3b6155','#514b3e')
pine(23,119,33,'#355749','#4b7159','#514b3e')
# Clusters of meadow texture, ochre grass and small stones.
for i in range(150):
    x=random.randrange(128);y=random.randrange(91,128)
    if c.color_name(c.get(x,y)) in ['#697d61','#9a9c76','#7f8c72']:
        col=random.choice(['#b6ad76','#879268','#526e56'])
        c.line(x,y,min(x+random.choice([1,2,3]),127),y,col)
        if i%4==0:c.set(x,y-1,col)
for x,y in [(39,112),(92,116),(106,106),(14,122),(84,104),(44,98)]:
    c.poly([(x,y),(x+2,y-2),(x+5,y-1),(x+6,y+1),(x,y+1)],'#536861');c.line(x+2,y-2,x+4,y-2,'#a4aa8b')
# Tiny flowers catching the first sun.
for x,y in [(32,103),(43,118),(89,110),(100,122),(35,126),(76,102)]:
    c.set(x,y,'#e7bc76');c.set(x+1,y-1,'#f1d196');c.set(x,y+1,'#466952')
assert result.stats()['colors_used'] <= 86
view(result)
save('mountain-village-sunrise',result)
finish(result)
