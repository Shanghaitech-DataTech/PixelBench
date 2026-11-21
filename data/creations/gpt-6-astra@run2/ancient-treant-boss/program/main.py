import random, math
random.seed(21)
c=new_canvas(256,256,'#111e23',name='ancient_treant')
# A restrained nocturnal woodland palette.
bg0='#101b22'; bg1='#17292b'; bg2='#203734'; bg3='#29443b'; bg4='#345143'
ink='#10191c'; deep='#202824'; bark0='#30352b'; bark1='#464531'; bark2='#5e593b'; bark3='#787045'; bark4='#958454'; edge='#b4a16a'
moss0='#233c2c'; moss1='#365536'; moss2='#537342'; moss3='#7f9450'; moss4='#a0b563'
# Mist strata and distant uneven forest floor
c.rect(0,74,256,113,bg1)
c.rect(0,118,256,75,bg2)
c.poly([(0,179),(40,165),(78,175),(113,158),(171,170),(213,157),(255,173),(255,222),(0,222)],bg3)
# Far trunks: stepped roots, lit edges, high boughs
for x,w,y in [(7,10,0),(29,7,7),(49,11,0),(77,6,0),(94,8,0),(169,8,0),(190,11,0),(218,9,0),(244,14,0)]:
    col=bg1 if x%2 else bg0
    c.poly([(x,0),(x+w,0),(x+w-2,139),(x+w+8,184),(x-7,184),(x+1,141)],col)
    c.line(x+w-2,12,x+w-4,144,bg3)
    c.poly([(x+3,79),(x-15,54),(x-22,22),(x-17,24),(x-10,50),(x+5,66)],col)
    c.poly([(x+w-2,46),(x+21,26),(x+27,0),(x+23,0),(x+16,23),(x+2,36)],col)
# Distant canopy clusters
for i in range(110):
    x=random.randrange(256); y=random.randrange(4,53)
    r=random.randrange(3,16)
    c.ellipse(x,y,r,max(2,r//2),random.choice([bg0,bg1,bg2]))
# Hard-edged, pale shafts of light entering the clearing.
c.poly([(47,0),(56,0),(159,199),(125,205)],'#3a5040')
c.poly([(53,0),(57,0),(151,196),(135,199)],'#4b6048')
c.poly([(167,0),(175,0),(236,193),(214,192)],'#354e40')
c.poly([(173,0),(176,0),(229,182),(220,184)],'#496047')
c.poly([(106,0),(109,0),(175,168),(163,170)],'#304a3c')
# Mossy ground and clearing terraces
c.poly([(0,192),(37,182),(74,186),(106,176),(146,185),(189,179),(224,187),(255,181),(255,255),(0,255)],'#283b31')
c.ellipse(130,217,105,27,'#354734')
c.ellipse(129,220,80,17,'#465239')
c.ellipse(130,224,58,11,'#1b2926')
for i in range(490):
    x=random.randrange(256); y=random.randrange(180,256)
    col=random.choice(['#1b2c29','#23372d','#3d5035','#53603e'])
    c.line(x,y,min(255,x+random.randrange(1,5)),y,col)
# Background grasses
for i in range(95):
    x=random.randrange(256); y=random.randrange(174,222)
    if 68<x<184: continue
    c.line(x,y,x+random.randrange(-3,4),y-random.randrange(2,7),random.choice([bg1,moss1,moss2]))
# Tapered angular limbs, each with a dark contour.
def ribbon(points,widths,col):
    left=[];right=[]
    for i,((x,y),w) in enumerate(zip(points,widths)):
        a=points[max(0,i-1)];b=points[min(len(points)-1,i+1)]
        dx=b[0]-a[0];dy=b[1]-a[1];d=math.hypot(dx,dy) or 1
        nx=-dy/d*w/2;ny=dx/d*w/2
        left.append((round(x+nx),round(y+ny)));right.append((round(x-nx),round(y-ny)))
    c.poly(left+right[::-1],col)
def branch(points,widths,base=bark1):
    ribbon(points,[w+4 if w>1 else w+1 for w in widths],ink)
    ribbon(points,widths,base)
    # upper exposed sapwood ridge
    shifted=[(x-1,y-1) for x,y in points]
    ribbon(shifted,[max(1,w*.28) for w in widths],bark2)
# Crown deadwood, a broken crown of antler-like limbs
for pts,ws in [([(119,91),(106,59),(95,43),(77,35),(69,21)],[22,15,10,6,0]), ([(102,58),(110,39),(108,21),(115,10)],[10,8,5,0]), ([(98,46),(89,29),(91,13)],[7,5,0]), ([(140,83),(151,51),(167,35),(177,13)],[24,15,9,0]), ([(153,51),(150,26),(141,14)],[10,6,0]), ([(164,37),(188,32),(202,19)],[8,5,0]), ([(149,65),(179,55),(197,43),(212,44)],[12,9,4,0]), ([(117,68),(128,45),(126,29),(134,20)],[13,9,6,0])]:
    branch(pts,ws)
# The massive roots and widely planted legs
for pts,ws in [([(113,165),(102,193),(91,218),(62,229),(38,233)],[32,28,21,10,0]), ([(102,200),(77,209),(62,215),(55,226)],[17,12,6,0]), ([(96,214),(98,229),(84,239),(65,240)],[19,13,6,0]), ([(143,167),(151,192),(163,215),(188,226),(218,229)],[33,29,23,12,0]), ([(151,197),(175,203),(191,216),(211,218)],[15,11,6,0]), ([(163,214),(148,229),(157,239),(180,243)],[20,13,7,0]), ([(119,182),(123,209),(115,225),(119,236)],[16,12,7,0])]:
    branch(pts,ws)
# Arms reach out around the viewer, elbows thick and twisted.
for pts,ws in [([(111,127),(88,121),(73,143),(55,139),(40,115)],[29,25,23,21,17]), ([(151,127),(174,142),(190,128),(205,101)],[29,27,24,17]), ([(79,139),(67,113),(60,95)],[10,7,0]), ([(178,140),(190,151),(206,153)],[12,7,0])]:
    branch(pts,ws)
# Left hand, five long hooked twig claws.
for pts,ws in [([(41,117),(29,107),(21,93),(23,80),(29,74)],[16,10,7,4,0]), ([(35,111),(38,94),(34,78),(39,66),(46,63)],[12,9,6,3,0]), ([(42,109),(49,95),(49,82),(56,74)],[11,8,4,0]), ([(30,112),(18,112),(12,102),(13,93)],[10,7,4,0]), ([(43,122),(54,115),(56,104),(53,99)],[10,7,4,0])]:
    branch(pts,ws)
# Right hand, lifted and open.
for pts,ws in [([(204,102),(202,84),(207,68),(204,56),(198,52)],[17,11,7,4,0]), ([(208,94),(218,79),(221,63),(216,53)],[13,10,6,0]), ([(212,101),(228,90),(236,75),(232,64)],[12,9,5,0]), ([(212,109),(232,106),(242,95),(242,85)],[11,8,4,0]), ([(200,105),(190,94),(190,83),(184,77)],[11,8,4,0])]:
    branch(pts,ws)
# Core trunk silhouette; broken, irregular edges and a heavy barrel chest.
body=[(109,61),(121,64),(128,52),(137,60),(148,56),(151,79),(158,97),(157,114),(169,133),(160,155),(162,175),(150,193),(134,202),(115,195),(99,183),(97,164),(91,146),(99,127),(100,105),(104,83)]
c.poly(body,ink)
c.poly([(111,65),(121,71),(129,58),(136,67),(145,61),(146,84),(153,99),(151,117),(163,134),(154,157),(157,174),(146,188),(133,196),(117,189),(105,179),(104,161),(97,146),(104,128),(106,105),(109,84)],bark1)
# Broad structural planes of bark, following a spiral in the old trunk
c.poly([(111,68),(117,75),(113,99),(117,126),(110,146),(117,171),(112,185),(105,177),(104,157),(99,146),(108,118),(107,98)],bark3)
c.poly([(129,60),(136,70),(131,89),(132,121),(124,146),(132,169),(129,194),(118,188),(122,167),(115,147),(124,124),(123,98)],bark2)
c.poly([(145,65),(146,88),(153,102),(150,120),(161,136),(152,156),(157,174),(145,187),(137,193),(143,168),(136,148),(143,126),(139,106)],bark0)
c.poly([(137,72),(141,93),(138,121),(132,141),(139,161),(138,183),(133,193),(131,163),(125,144),(133,119)],bark3)
# Bark fissures drawn only into wood. This keeps all texture inside the silhouette.
wood={c.color(v) for v in [bark0,bark1,bark2,bark3,bark4]}
def woodpixel(x,y,col):
    if 0<=x<256 and 0<=y<256 and c.get(x,y) in wood: c.set(x,y,col)
for i in range(490):
    x=random.randrange(15,242);y=random.randrange(22,238)
    if c.get(x,y) not in wood:continue
    length=random.randrange(3,14)
    dx=random.choice([-1,0,0,1]); col=random.choice([deep,bark0,bark2,bark3])
    for j in range(length):
        xx=x+(j//4)*dx
        woodpixel(xx,y+j,col)
        if col==deep:woodpixel(xx-1,y+j,bark3)
# Long spiraling splits in the torso
for pts in [[(119,73),(116,89),(120,108),(118,122)],[(132,72),(128,90),(130,107)],[(109,130),(105,148),(112,165),(109,178)],[(143,124),(136,143),(144,165),(141,182)],[(124,156),(127,173),(121,189)],[(151,137),(147,152),(153,171)]]:
    ribbon(pts,[3]*len(pts),deep)
    for a,b in zip(pts,pts[1:]): c.line(a[0]-2,a[1],b[0]-2,b[1],bark3)
# Knots and tiny concentric wounds in the wood
for x,y,rx,ry in [(112,155,4,7),(146,176,3,6),(91,133,4,5),(178,133,4,5),(151,192,3,6),(103,201,3,5)]:
    c.ellipse(x,y,rx+1,ry+1,bark2);c.ellipse(x,y,rx,ry,deep);c.ellipse(x,y,rx-1,ry-2,bark0);c.line(x,y-2,x,y+2,ink)
# Overhanging angular brows, cavernous sockets, and an ancient angry face
c.poly([(106,91),(115,90),(125,97),(127,104),(117,107),(108,102)],deep)
c.poly([(131,99),(137,92),(150,87),(150,99),(142,105),(132,106)],deep)
# Green glow is restricted to sharp rings, with a brilliant core.
c.poly([(108,95),(116,95),(123,100),(122,104),(114,103),(109,100)],'#375d32')
c.poly([(133,100),(140,95),(148,92),(147,100),(140,103),(133,104)],'#375d32')
c.poly([(110,96),(116,97),(122,101),(116,101),(111,99)],'#85c34e')
c.poly([(134,101),(141,97),(147,94),(145,100),(139,102)],'#85c34e')
c.line(112,97,119,100,'#ccf980');c.line(136,100,145,96,'#ccf980')
c.line(114,97,117,98,'#efffb6');c.line(141,98,145,96,'#efffb6')
# Brow shelves and split nose
ribbon([(105,91),(115,92),(125,98)],[5,5,2],bark3)
ribbon([(131,97),(140,91),(151,88)],[2,5,5],bark2)
c.poly([(127,98),(130,105),(135,112),(130,115),(123,113)],bark0)
c.line(127,102,126,111,bark4)
# Jagged hollow mouth, broken wood teeth
c.poly([(113,115),(121,118),(127,117),(132,119),(143,111),(141,122),(135,128),(123,131),(114,126)],ink)
c.poly([(114,116),(119,119),(119,123),(116,122)],bark3)
c.poly([(123,119),(127,120),(125,124)],bark2)
c.poly([(135,118),(140,114),(138,122)],bark3)
c.poly([(118,127),(121,123),(123,129)],bark2)
c.poly([(129,128),(133,123),(135,126)],bark2)
c.line(118,132,128,135,bark3)
# Moss in irregular clustered cushions, lit on the upper edge.
def moss(x,y,rx,ry):
    c.ellipse(x,y,rx,ry,moss0)
    for j in range(max(4,rx*2)):
        xx=x+random.randint(-rx+1,rx-1); yy=y+random.randint(-ry, max(0,ry-1))
        if ((xx-x)/rx)**2+((yy-y)/max(1,ry))**2>1:continue
        col=moss2 if yy<y else moss1
        c.rect(xx,yy,random.randint(2,4),2,col)
        if random.random()<.4:c.line(xx,yy-1,xx+1,yy-1,moss3)
for p in [(99,45,10,4),(113,62,8,4),(155,51,9,4),(177,54,9,3),(91,119,13,5),(72,139,9,4),(53,130,6,3),(159,125,11,4),(185,122,7,4),(150,162,6,8),(106,174,5,7),(91,218,9,4),(164,216,10,4),(132,67,6,3)]:moss(*p)
# Hanging vines with leaves and occasional broken tips
for pts in [[(93,119),(89,135),(91,151),(87,166),(89,175)],[(78,140),(79,158),(73,176),(75,183)],[(158,123),(166,139),(161,159),(165,177)],[(181,54),(177,72),(180,82)],[(106,45),(103,62),(99,75)],[(196,117),(200,135),(196,146)],[(59,133),(57,150),(61,158)]]:
    for a,b in zip(pts,pts[1:]):
        c.line(a[0],a[1],b[0],b[1],ink);c.line(a[0]+1,a[1],b[0]+1,b[1],moss2)
    for x,y in pts[1:-1]:
        c.poly([(x,y),(x-5,y-4),(x-5,y),(x-1,y+3)],moss1)
        c.line(x-4,y-2,x,y+1,moss3)
        c.poly([(x+1,y+6),(x+5,y+1),(x+6,y+4),(x+3,y+7)],moss2)
# Shelf fungi emphasizing the immense age of the trunk
for x,y,w in [(151,143,6),(154,149,4),(104,183,5),(95,208,4)]:
    c.ellipse(x,y,w,2,ink);c.line(x-w,y-1,x+w-1,y-1,'#a78959');c.line(x-w+1,y,x+w,y,'#6e5940');c.line(x-2,y+1,x+2,y+1,'#c1aa75')
# A few luminous spores catch the shafts of light.
for x,y in [(62,59),(71,86),(166,88),(188,172),(46,171),(214,155),(120,29),(26,150),(231,124),(68,196),(179,193)]:
    c.set(x,y,'#b1c581');c.set(x,y+1,moss2)
# Foreground dark banks and fern silhouettes frame the clearing.
c.poly([(0,226),(20,230),(33,242),(58,246),(73,255),(0,255)],bg0)
c.poly([(192,255),(211,244),(232,239),(243,228),(255,224),(255,255)],bg0)
def fern(x,y,flip=1,s=1):
    c.line(x,y,x+int(5*s)*flip,y-int(29*s),moss1)
    for j in range(6):
        yy=y-int((5+j*4)*s);xx=x+int(j*.7*s)*flip
        w=int((10-j)*s)
        c.line(xx,yy,xx-w,yy-int(5*s),moss1)
        c.line(xx,yy,xx+w,yy-int(7*s),moss1)
        c.line(xx-w,yy-int(5*s),xx-3,yy-1,moss2 if j>2 else moss1)
        c.line(xx+w,yy-int(7*s),xx+3,yy-1,moss2 if j>3 else moss1)
fern(23,249,1,1);fern(236,251,-1,1.2);fern(9,238,-1,.7)
# Small ground stones and sparse warm leaf litter.
for x,y in [(46,222),(204,239),(71,246),(227,218),(34,204)]:
    c.poly([(x-4,y),(x-2,y-3),(x+3,y-2),(x+5,y+1),(x+1,y+3)],ink)
    c.line(x-2,y-3,x+2,y-2,'#6b7155')
for x,y in [(52,239),(182,235),(197,222),(76,227),(139,244),(36,217),(216,206)]:
    c.line(x,y,x+3,y-1,'#8c8250')
result=c
view(result)
finish(result)
