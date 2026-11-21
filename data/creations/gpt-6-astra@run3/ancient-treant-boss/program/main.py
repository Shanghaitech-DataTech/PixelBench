import random, math
random.seed(31)
result = new_canvas(256,256,background='#111e23',name='Ancient treant')
c=result
# restrained forest and bark palette
ink='#11151a'; deep='#182326'; fog='#344d49'; far='#243b3a'; mid='#20332f'
bark0='#292922'; bark1='#3d392b'; bark2='#514632'; bark3='#68583a'; bark4='#827047'; bark5='#a28b56'
moss0='#263c28'; moss1='#405a2d'; moss2='#60783b'; moss3='#8b9b4b'
# atmospheric forest bands
c.rect(0,35,256,151,'#293f3d'); c.rect(0,99,256,98,'#354b43')
# distant trunks
for x in range(-8,270,15):
    w=random.randint(3,8); top=random.randint(0,38)
    c.poly([(x,top),(x+w,top),(x+w-2,155),(x+w+7,189),(x-7,189),(x+1,139)],far)
    c.line(x+2,80,x-10,57,far); c.line(x+3,49,x+16,29,far)
# god rays, hard-edged soft color bands
for pts,col in [([(183,0),(194,0),(83,203),(45,213)],'#3b5146'), ([(187,0),(191,0),(66,213),(50,216)],'#465d4b'), ([(225,0),(231,0),(149,199),(123,206)],'#425949'), ([(229,0),(232,0),(140,207),(129,207)],'#50644e'), ([(84,0),(88,0),(12,166),(0,183)],'#3b5146')]: c.poly(pts,col)
# forest floor
c.poly([(0,190),(28,180),(50,184),(83,179),(110,186),(155,178),(190,183),(223,174),(255,183),(255,255),(0,255)],'#25382e')
c.ellipse(132,223,103,28,'#344533'); c.ellipse(131,231,86,20,'#40503a')
# background foliage clusters, purposeful pixel patches
for i in range(280):
    x=random.randrange(256); y=random.choice([random.randrange(0,60),random.randrange(174,216)])
    if 52<x<205 and y>174: continue
    col=random.choice([mid,moss0,'#2e4433','#3b5137'])
    c.rect(x,y,random.randint(2,8),random.randint(1,4),col)
# framing trees
for flip in (False,True):
    def P(points): return [(255-x if flip else x,y) for x,y in points]
    c.poly(P([(0,0),(20,0),(19,39),(26,78),(20,116),(25,162),(41,204),(19,198),(5,220),(0,219)]),'#122523')
    c.poly(P([(7,0),(13,0),(12,64),(18,97),(13,139),(21,182),(12,172),(9,107)]),'#20332b')
    c.poly(P([(14,68),(42,47),(61,8),(57,40),(44,59),(21,89)]),'#152a25')
    c.poly(P([(15,31),(35,22),(61,25),(37,30),(17,44)]),'#152a25')
# floor texture
for i in range(380):
    x=random.randrange(256); y=random.randrange(196,256)
    col=random.choice(['#1e3029','#2a3c2e','#526044','#5d6947','#394a34'])
    c.line(x,y,min(255,x+random.randint(1,5)),y,col)
# shadow under creature
c.ellipse(131,232,76,13,'#1a2925'); c.ellipse(133,231,58,8,'#15221f')
# outlined wood helper
wood_shapes=[]
def wood(pts,col=bark2):
    c.poly(pts,col); c.poly(pts,ink,fill=False); wood_shapes.append(pts)
def branch(points,width,col=bark2):
    # connected discs with crisp dark boundary
    for a,b in zip(points,points[1:]):
        steps=max(abs(b[0]-a[0]),abs(b[1]-a[1]))
        for i in range(steps+1):
            t=i/max(1,steps); x=round(a[0]+(b[0]-a[0])*t);y=round(a[1]+(b[1]-a[1])*t)
            r=max(1,round(width*(1-(points.index(a)+t)/(len(points)*1.15))))
            c.circle(x,y,r+1,ink)
    for k,(a,b) in enumerate(zip(points,points[1:])):
        steps=max(abs(b[0]-a[0]),abs(b[1]-a[1]))
        for i in range(steps+1):
            t=i/max(1,steps); x=round(a[0]+(b[0]-a[0])*t); y=round(a[1]+(b[1]-a[1])*t)
            r=max(1,round(width*(1-(k+t)/(len(points)*1.15))))
            c.circle(x,y,r,col)
# high jagged crown branches
wood([(100,92),(89,67),(72,55),(63,30),(65,14),(72,34),(84,45),(82,23),(88,9),(90,34),(97,46),(111,52),(116,75)],bark1)
wood([(132,73),(139,45),(154,33),(160,9),(165,7),(165,32),(158,48),(166,43),(185,25),(192,10),(194,30),(183,44),(168,54),(156,78)],bark2)
wood([(108,69),(111,38),(104,22),(105,12),(116,28),(121,43),(129,31),(128,14),(133,21),(135,36),(124,57),(125,79)],bark2)
wood([(152,85),(175,63),(194,59),(204,46),(211,45),(205,64),(185,73),(178,88),(158,106)],bark1)
# thin twig forks
for pts in [[(76,44),(53,41),(43,30)],[(90,37),(101,24),(99,16)],[(178,46),(174,28),(179,20)],[(192,61),(217,63),(229,54)],[(68,32),(54,23),(52,15)]]: branch(pts,2,bark2)
# claw arms, spread out
wood([(105,100),(84,95),(67,105),(55,128),(41,137),(30,145),(29,163),(42,178),(56,171),(52,154),(69,145),(83,125),(104,131)],bark2)
wood([(153,102),(174,98),(188,112),(196,132),(212,140),(223,157),(218,173),(202,180),(194,170),(200,157),(180,149),(166,132),(151,131)],bark2)
# fingers with hooked twig claws
for pts,w in [([(39,150),(23,153),(18,169),(24,180)],4), ([(40,160),(33,178),(40,190),(47,187)],4), ([(48,164),(49,181),(59,188),(61,181)],3), ([(48,148),(57,153),(61,163)],3), ([(210,151),(228,150),(238,161),(236,174)],4), ([(214,162),(228,173),(226,189),(218,192)],4), ([(204,167),(211,185),(206,197),(201,196)],3), ([(201,154),(188,163),(188,174)],3)]: branch(pts,w,bark2)
# legs and lifted spreading roots
wood([(100,157),(125,171),(118,198),(105,218),(105,230),(83,239),(52,238),(36,244),(42,235),(66,225),(82,221),(87,200)],bark2)
wood([(130,170),(155,160),(164,188),(163,208),(177,222),(197,228),(220,231),(229,242),(212,237),(191,240),(162,230),(145,215),(138,197)],bark2)
wood([(111,195),(125,188),(130,212),(124,228),(132,241),(151,248),(126,246),(112,237),(109,222)],bark1)
wood([(90,214),(87,231),(71,244),(56,248),(63,240),(74,228)],bark1)
wood([(159,211),(161,227),(178,243),(196,248),(177,247),(153,236),(145,223)],bark1)
# central massive twisted trunk silhouette
wood([(96,81),(108,70),(128,73),(143,65),(156,79),(161,104),(156,128),(163,149),(155,171),(143,186),(128,194),(111,184),(93,174),(88,155),(94,130),(89,107)],bark2)
# trunk planes and knots
c.poly([(100,85),(110,80),(116,98),(109,124),(113,141),(106,164),(117,182),(101,174),(94,155),(102,133),(97,110)],bark3)
c.poly([(142,77),(152,84),(151,109),(143,130),(150,152),(143,172),(129,186),(135,161),(131,144),(139,117)],bark1)
c.poly([(119,79),(130,80),(127,103),(132,125),(126,148),(133,163),(124,180),(117,166),(121,143),(116,124),(121,101)],bark3)
c.poly([(153,112),(157,132),(153,150),(156,161),(147,174),(148,151),(143,134)],bark0)
# bark flowing fissures, roots and arms
for pts in [ [(102,83),(106,102),(101,118),(107,136),(102,155),(110,170)],[(115,82),(112,98),(115,108)],[(132,78),(130,95),(135,112)],[(149,83),(146,98),(148,109)],[(122,133),(118,151),(124,165),(120,174)],[(139,139),(136,151),(142,165),(137,179)],[(96,159),(102,173),(107,177)],[(88,107),(76,111),(67,129),(50,144),(43,162)],[(78,115),(70,137),(59,146)],[(169,109),(180,120),(184,139),(206,150),(213,166)],[(172,122),(179,145),(197,154)],[(102,180),(98,200),(93,214),(74,230),(57,232)],[(111,188),(106,209),(97,223)],[(146,185),(152,200),(151,214),(170,230),(192,234)],[(158,190),(157,206),(165,219)],[(119,210),(116,227),(127,239)],[(96,64),(104,67),(107,78)],[(146,68),(149,51),(159,39)],[(85,51),(91,58),(97,80)]]:
    for (x,y),(xx,yy) in zip(pts,pts[1:]):
        c.line(x,y,xx,yy,bark0); c.line(x-2,y,xx-2,yy,bark4)
# fine bark scars only inside wood palette
woodcols={c.color(k) for k in [bark1,bark2,bark3,bark4]}
for i in range(550):
    x=random.randrange(24,233); y=random.randrange(19,239)
    if c.get(x,y) in woodcols:
        col=random.choice([bark0,bark1,bark3,bark4])
        length=random.randint(1,5)
        for j in range(length):
            if y+j<256 and c.get(x,y+j) in woodcols:c.set(x,y+j,col)
# broken lit ridges trace the torsion of the ancient limbs
for pts in [[(68,25),(70,37),(80,49),(89,54)],[(86,24),(86,36),(94,48),(102,52)],[(113,31),(117,43),(115,59),(112,67)],[(132,26),(131,36),(123,48)],[(160,16),(161,31),(151,45),(146,61)],[(188,28),(178,41),(163,52)],[(201,53),(195,63),(180,68),(169,80)],[(83,103),(73,109),(62,128),(50,138)],[(36,145),(33,153),(37,162)],[(24,158),(22,168),(26,175)],[(37,174),(38,182),(42,186)],[(51,173),(54,180),(58,183)],[(172,106),(181,115),(190,135),(202,142)],[(218,154),(228,155),(233,162)],[(220,173),(223,179),(222,186)],[(205,176),(208,185),(204,191)],[(97,184),(93,203),(89,214),(76,223),(62,228)],[(142,187),(149,202),(148,215),(158,225)],[(164,223),(178,231),(193,234)],[(117,211),(113,224),(118,235),(126,240)]]:
    for k,(a,b) in enumerate(zip(pts,pts[1:])):
        c.line(a[0],a[1],b[0],b[1],bark3 if k%3==1 else bark4)
# short transverse splits and light catching splinters
for x,y in [(81,52),(95,62),(113,58),(148,55),(175,63),(79,117),(60,138),(176,117),(192,143),(106,91),(116,155),(133,160),(96,197),(153,214),(89,226)]:
    c.line(x-2,y,x+2,y+2,bark0)
    c.line(x+2,y+2,x+1,y+5,bark0)
    c.set(x-2,y-1,bark5)
# small dry twig spurs interrupt the heavy branch edges
for pts in [[(74,95),(67,91),(65,84)],[(183,105),(192,98),(193,91)],[(30,163),(26,158),(26,151)],[(226,177),(233,180),(237,178)]]:
    for a,b in zip(pts,pts[1:]):
        c.line(a[0],a[1],b[0],b[1],ink)
        c.line(a[0],a[1]-1,b[0],b[1]-1,bark2)
# concentric wood knots
for x,y,rx,ry in [(102,144,4,8),(148,153,3,6),(64,138,3,5),(177,126,3,6),(99,203,3,6),(153,49,2,4)]:
    c.ellipse(x,y,rx,ry,bark0);c.ellipse(x-1,y,rx-1,ry-2,bark4);c.ellipse(x,y+1,max(1,rx-2),max(1,ry-3),bark1);c.line(x,y-1,x,y+2,ink)
# menacing brows and eye hollows
c.poly([(98,100),(109,99),(121,106),(118,115),(106,115),(99,109)],ink)
c.poly([(132,106),(143,98),(153,96),(151,108),(140,114),(132,114)],ink)
c.poly([(101,104),(110,104),(118,109),(115,112),(107,111)],'#315e30')
c.poly([(134,109),(142,103),(150,101),(147,108),(139,112)],'#315e30')
c.poly([(104,105),(110,106),(117,109),(114,111),(107,109)],'#8bd84b')
c.poly([(135,109),(143,105),(148,103),(145,109),(138,111)],'#8bd84b')
c.line(107,106,114,109,'#dcff91'); c.line(139,109,146,105,'#dcff91');c.set(111,108,'#f0ffca');c.set(143,107,'#f0ffca')
c.poly([(97,98),(103,94),(120,103),(123,108),(110,102)],bark4)
c.poly([(130,105),(143,94),(154,92),(151,99),(142,101)],bark3)
# nose and jagged mouth
c.poly([(124,105),(118,122),(124,125),(132,121)],bark1);c.line(124,108,122,120,bark4)
c.poly([(106,122),(114,127),(120,126),(126,130),(133,125),(144,120),(139,135),(130,142),(116,137)],ink)
c.poly([(109,124),(115,128),(114,132)],bark4);c.poly([(135,129),(141,124),(137,132)],bark3)
c.line(119,136,128,139,bark0); c.line(129,139,136,134,bark3)
# moss grows over shoulders and crown, clustered edges
for x,y,rx,ry in [(94,84,9,5),(103,76,8,4),(150,78,8,4),(78,104,9,4),(64,121,5,4),(169,102,10,5),(183,113,6,4),(99,169,7,3),(149,178,6,4),(85,220,8,3),(173,225,9,3),(85,48,5,3),(163,51,7,3)]:
    c.ellipse(x,y,rx,ry,moss0)
    for i in range(rx*3):
        xx=x+random.randint(-rx+1,rx-1); yy=y+random.randint(-ry,ry)
        if ((xx-x)/rx)**2+((yy-y)/max(1,ry))**2<1:
            c.rect(xx,yy,random.randint(1,3),2,random.choice([moss1,moss2,moss2,moss3]))
# hanging vines and little paired leaves
for x,y,end,bend in [(77,106,151,-5),(92,83,124,-6),(165,55,92,4),(177,106,153,8),(66,52,86,-3),(194,69,118,-4),(158,85,131,5),(58,129,159,-4)]:
    pts=[]
    for yy in range(y,end+1):
        xx=x+round(math.sin((yy-y)/(end-y)*math.pi)*bend)
        pts.append((xx,yy));c.set(xx+1,yy,moss0);c.set(xx,yy,moss2)
    for k in range(6,len(pts)-2,8):
        xx,yy=pts[k]; d=1 if k%16==6 else -1
        c.line(xx,yy,xx+d*3,yy-2,moss1); c.line(xx+d,yy-1,xx+d*3,yy-2,moss3)
# sparse crown foliage, keeps the ancient broken silhouette
for x,y in [(54,39),(79,42),(95,60),(113,37),(161,27),(179,45),(200,63),(145,68)]:
    for j in range(7):
        xx=x+random.randint(-8,8); yy=y+random.randint(-4,3)
        c.rect(xx,yy,random.randint(3,6),2,random.choice([moss0,moss1,moss2]))
# mushrooms on trunk flank
for x,y in [(94,151),(95,157),(159,143)]:
    c.line(x,y,x,y+4,bark5);c.line(x-3,y,x+3,y,'#ad925e');c.line(x-2,y-1,x+1,y-1,'#c5ab76');c.line(x-3,y+1,x+2,y+1,bark1)
# foreground grass and stones
for x,y in [(19,233),(33,219),(224,222),(238,243),(11,252),(204,251),(62,254),(181,252)]:
    for j in range(6):
        xx=x+random.randint(-6,6);h=random.randint(4,12)
        c.line(xx,y,xx+random.randint(-4,4),y-h,random.choice([ink,moss0,moss1,moss2]))
for x,y in [(25,246),(233,231),(65,212),(184,215),(153,250),(9,220)]:
    c.poly([(x-5,y),(x-3,y-4),(x+2,y-5),(x+6,y-1),(x+4,y+2),(x-4,y+2)],'#1a2b27');c.line(x-3,y-4,x+2,y-5,'#69735a');c.line(x-3,y-3,x+3,y-2,'#4c5c47')
# drifting green spores around the old guardian
for x,y in [(53,96),(201,91),(75,179),(185,193),(46,200),(220,124),(121,52),(34,122),(173,159),(70,77)]:
    c.set(x,y,'#8da65b');c.set(x,y+1,'#576e43')
assert tuple(result.stats()['size']) == (256,256)
assert result.stats()['colors_used'] <= 120
view(result)
save('ancient-treant-boss',result)
finish(result)
