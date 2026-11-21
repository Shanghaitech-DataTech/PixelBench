import math, random
random.seed(24)
W=H=256
# A limited, hand-picked palette, with warm wood against cool forest shadows.
P={
'ink':'#101918','deep':'#102423','bg0':'#132c2c','bg1':'#1b3835','bg2':'#25463e','bg3':'#32564a','fog':'#426857','foghi':'#587c60',
'ray':'#668567','rayhi':'#789570','sky':'#8ca17b','earth':'#24382f','soil':'#303e30','soilhi':'#3e4b34',
'b0':'#211e1b','b1':'#302920','b2':'#433627','b3':'#57432e','b4':'#705437','b5':'#8a6943','b6':'#a58050','b7':'#b99b64',
'rot':'#333b29','m0':'#203d2c','m1':'#345535','m2':'#4e703b','m3':'#71904a','m4':'#9eae5e',
'g0':'#244827','g1':'#3f7c32','g2':'#66b545','g3':'#abeb66','g4':'#e1ffa3',
'stone0':'#263d38','stone1':'#3b5045','stone2':'#57654f','grass':'#537145','grasshi':'#84915b'
}
c=new_canvas(256,256,P['bg0'],name='Ancient treant — Warden of the hollow')
def poly(points,col,can=c): can.poly(points,P.get(col,col))
def line(a,b,col,can=c): can.line(*a,*b,P.get(col,col))
# The vaulted forest has a luminous opening behind the crown.
poly([(43,0),(218,0),(250,148),(223,215),(28,211),(2,130)],'bg1')
poly([(82,0),(190,0),(213,85),(240,155),(207,207),(52,204),(36,124)],'bg2')
poly([(104,0),(164,0),(183,53),(207,126),(206,191),(76,192),(68,105)],'bg3')
poly([(120,0),(155,0),(164,64),(184,111),(190,190),(86,190),(96,93)],'fog')
# Distant slender trunks and their angular branches.
for x,y,w,col in [(21,24,5,'bg2'),(44,7,7,'bg3'),(65,29,4,'fog'),(88,2,5,'bg2'),(111,18,3,'bg3'),(173,7,5,'bg3'),(190,22,5,'bg2'),(218,10,6,'bg3'),(236,27,5,'bg2')]:
    poly([(x,y),(x+w,y),(x+w-2,159),(x+w+5,200),(x-5,200),(x+1,133)],col)
    line((x+2,y+61),(x-17,y+36),col); line((x+2,y+42),(x+18,y+18),col)
# Shafts of filtered sunlight, discretised into nested, hard-edged bands.
poly([(51,0),(62,0),(155,192),(126,205)],'fog')
poly([(55,0),(60,0),(147,190),(133,193)],'foghi')
poly([(78,0),(85,0),(194,199),(174,205)],'foghi')
poly([(80,0),(83,0),(184,190),(176,192)],'ray')
poly([(178,0),(184,0),(117,205),(86,210)],'foghi')
poly([(179,0),(183,0),(108,202),(98,202)],'ray')
poly([(204,0),(209,0),(171,200),(150,204)],'fog')
# Great foreground trees frame the clearing.
poly([(0,0),(31,0),(27,28),(31,62),(24,105),(28,159),(37,204),(19,221),(0,219)],'deep')
poly([(5,0),(15,0),(13,50),(19,84),(14,155),(22,195),(16,201),(8,155)],'bg1')
poly([(17,0),(23,0),(21,56),(17,95),(20,147),(14,134)],'bg2')
poly([(230,0),(255,0),(255,219),(235,213),(223,203),(234,173),(230,125),(236,71),(228,40)],'deep')
poly([(243,0),(248,0),(244,76),(247,142),(240,189),(236,194),(239,121),(236,67)],'bg1')
poly([(18,51),(41,33),(55,2),(62,0),(44,38),(25,66)],'deep')
poly([(235,63),(210,39),(192,4),(201,9),(219,32),(239,41)],'deep')
# Chunky high foliage shapes.
for x,y,rx,ry in [(3,6,38,17),(39,1,27,12),(71,2,21,10),(238,6,34,16),(218,3,27,14),(17,57,16,11),(251,72,18,13)]:
    c.ellipse(x,y,rx,ry,P['deep'])
for _ in range(78):
    x=random.randrange(256); y=random.randrange(34)
    if (x<83 or x>193) and c.get(x,y)==c.color(P['deep']):
        c.rect(x,y,random.randint(2,6),random.randint(1,3),P[random.choice(['bg0','bg1'])])
# Layered leaf masses break up the canopy while leaving the rays open.
random.seed(29)
for side in [0,1]:
    for _ in range(62):
        x=random.randint(2,53) if side==0 else random.randint(209,253)
        y=random.randint(7,88)
        if (side==0 and x>35 and y>44) or (side==1 and x<228 and y>53): continue
        col=random.choice(['bg0','bg1','bg2'])
        c.poly([(x-3,y),(x,y-2),(x+5,y-2),(x+6,y+1),(x+2,y+3),(x-3,y+2)],P[col])
        if random.random()<.4: c.line(x,y-2,x+3,y-2,P['bg3'])
# Faint background shrubs and horizontal mist rims.
for x,y in [(42,177),(63,183),(198,179),(219,183)]:
    for dx,dy in [(-9,2),(-3,-3),(4,-1),(11,4)]:
        c.ellipse(x+dx,y+dy,7,3,P['bg3'])
        c.line(x+dx-4,y+dy-3,x+dx+2,y+dy-3,P['fog'])
# Low mist and uneven forest floor.
poly([(0,197),(28,188),(56,191),(85,183),(113,189),(144,182),(186,186),(218,191),(255,185),(255,255),(0,255)],'earth')
poly([(30,214),(68,196),(109,192),(149,193),(201,200),(235,224),(214,243),(59,245),(18,232)],'soil')
poly([(58,214),(94,202),(151,200),(193,211),(205,224),(169,237),(78,237),(47,226)],'soilhi')
c.ellipse(129,225,78,16,P['earth']); c.ellipse(129,224,61,11,P['b0'])
# Sparse, horizontal ground flecks establish scale without noisy fill.
for _ in range(250):
    x=random.randint(4,251); y=random.randint(190,253)
    col=random.choice(['bg1','earth','soil','soilhi','stone1','m1'])
    c.line(x,y,min(255,x+random.randint(1,5)),y,P[col])
# Soft, quantised light shafts cross the open air and land on the forest floor.
# Only three discrete illumination strengths are used, preserving a tight palette.
ray_blends={}
for y in range(8,224):
    for x in range(23,234):
        strength=0
        # Each beam widens towards the ground, with a dim outer rim.
        for origin,slope,spread in [(34,.19,5),(51,.19,2),(145,.37,8),(157,.37,3)]:
            middle=origin+slope*y
            half=1+spread*y/223
            dist=abs(x-middle)
            if dist<half:
                level=1 if dist>half*.7 or y>166 else (2 if y>80 else 3)
                strength=max(strength,level)
        if not strength: continue
        idx=c.get(x,y)
        if idx in [c.color(P['deep']),c.color(P['ink'])]: continue
        key=(idx,strength)
        if key not in ray_blends:
            entry=next(e for e in c.palette() if e['index']==idx)
            rgb=entry['rgba'][:3]; target=(161,178,124); amount=[0,.15,.24,.32][strength]
            ray_blends[key]=tuple(round(a+(b-a)*amount) for a,b in zip(rgb,target))
        c.set(x,y,ray_blends[key])
# Fallen monoliths / stones in the clearing.
for x,y,s in [(32,211,10),(218,211,9),(72,238,7),(188,237,9),(8,231,6),(241,238,7),(54,194,5)]:
    poly([(x-s,y),(x-s+2,y-s//2),(x+2,y-s//2-2),(x+s,y-2),(x+s+1,y+3),(x-4,y+4)],'ink')
    poly([(x-s+1,y),(x-s+3,y-s//2),(x+2,y-s//2-1),(x+s-1,y-2),(x+3,y+1)],'stone1')
    line((x-s+4,y-s//2),(x+1,y-s//2-1),'stone2')
# All wood is drawn on an independent sprite layer.
t=new_canvas(256,256,name='Gnarled wood')
def tp(points,col): poly(points,col,t)
def tl(a,b,col): line(a,b,col,t)
def tube(points,widths,colour,outline=True):
    # Angular tapered limbs with varying widths and mitered joints.
    left=[]; right=[]
    for i,(x,y) in enumerate(points):
        a=points[max(0,i-1)]; b=points[min(len(points)-1,i+1)]
        dx=b[0]-a[0]; dy=b[1]-a[1]; d=max(1,math.hypot(dx,dy))
        nx=-dy/d; ny=dx/d
        r=widths[i]/2
        left.append((round(x+nx*r),round(y+ny*r)))
        right.append((round(x-nx*r),round(y-ny*r)))
    shape=left+right[::-1]
    if outline:
        # Wide outer shape is built recursively, so no antialiased edges appear.
        tube(points,[w+4 if w>2 else w+2 for w in widths],'ink',False)
    tp(shape,colour)
    return shape
# Rear root tangles, partly submerged in the clearing.
for pts,ws in [([(115,188),(84,207),(76,222),(47,229),(33,226)],[18,13,10,6,1]), ([(144,190),(171,206),(181,222),(207,227),(221,221)],[19,14,8,5,1]), ([(105,195),(79,194),(63,203),(45,201),(39,196)],[11,8,6,3,1]), ([(157,191),(181,193),(198,205),(216,203)],[14,10,5,1])]:
    tube(pts,ws,'b2')
    tube([(x,y-2) for x,y in pts],[max(1,w*.22) for w in ws],'b4',False)
# Crown: long broken antler-like boughs.
crown=[
 ([(115,78),(100,51),(82,38),(74,19),(60,12)],[24,19,13,7,1]),
 ([(90,43),(60,40),(48,26),(48,13)],[13,9,6,1]),
 ([(76,24),(87,16),(91,4)],[6,4,1]),
 ([(61,39),(41,44),(31,35)],[7,4,1]),
 ([(125,69),(126,43),(116,26),(119,10)],[23,15,8,2]),
 ([(121,40),(105,34),(102,19)],[9,5,1]),
 ([(143,77),(154,49),(176,34),(181,16),(193,8)],[24,18,11,6,1]),
 ([(159,46),(155,26),(161,12)],[12,6,1]),
 ([(176,35),(202,32),(213,21),(214,11)],[11,8,4,1]),
 ([(198,32),(211,44),(226,40)],[6,4,1])]
for pts,ws in crown:
    tube(pts,ws,'b3')
    tube([(x-2,y-1) for x,y in pts],[max(1,w*.28) for w in ws],'b5',False)
# A broken branch shows pale splintered heartwood.
tp([(113,24),(115,14),(120,9),(123,12),(122,23)],'b6')
tl((117,17),(119,12),'b7')
# Large spreading arms, composed of elbows and crooked branch forearms.
leftpts=[(104,108),(81,102),(67,119),(55,141),(40,152)]
rightpts=[(155,111),(178,103),(191,115),(198,134),(213,142)]
tube(leftpts,[31,30,24,21,21],'b3')
tube(rightpts,[34,29,24,22,21],'b3')
# Horn branches off the upper arm silhouette.
for pts,ws in [([(82,105),(73,82),(57,73),(47,59)],[13,9,6,1]), ([(61,76),(43,79),(34,69)],[7,4,1]), ([(180,106),(188,83),(202,72),(206,58)],[12,9,6,1]), ([(194,80),(218,77),(227,65)],[7,4,1])]:
    tube(pts,ws,'b3'); tube([(x-1,y-1) for x,y in pts],[max(1,w*.25) for w in ws],'b5',False)
# Four separated twig claws on each massive hand.
claws=[
 ([(41,146),(28,142),(22,150),(25,164)],[12,9,5,1]),
 ([(37,153),(28,161),(29,176),(36,183)],[11,8,5,1]),
 ([(43,157),(40,174),(47,185),(54,186)],[10,7,4,1]),
 ([(48,151),(54,158),(53,168),(57,174)],[9,7,4,1]),
 ([(211,136),(222,126),(232,129),(237,141)],[11,8,4,1]),
 ([(217,141),(233,145),(237,157),(231,169)],[12,8,5,1]),
 ([(213,148),(221,160),(217,174),(209,180)],[11,8,5,1]),
 ([(206,147),(204,162),(197,169),(198,175)],[10,7,4,1])]
for pts,ws in claws:
    tube(pts,ws,'b3'); tube([(x-1,y-1) for x,y in pts],[max(1,w*.25) for w in ws],'b5',False)
# Main trunk: a broad, uneven humanoid chest, narrowing into two heavy root legs.
body=[(108,53),(122,48),(138,53),(150,62),(155,80),(158,93),(174,107),(170,128),(161,145),(165,169),(160,190),(166,207),(183,227),(178,234),(153,231),(140,219),(132,198),(125,184),(118,201),(110,220),(96,233),(74,235),(69,230),(88,214),(94,194),(92,172),(98,151),(87,131),(89,114),(99,95),(100,75)]
tp(body,'ink')
bodyinner=[(109,56),(122,51),(136,56),(147,64),(152,80),(155,95),(170,108),(167,126),(158,144),(162,170),(157,191),(163,208),(178,228),(176,231),(155,228),(143,217),(135,196),(125,179),(115,200),(107,218),(94,230),(74,231),(91,216),(98,194),(96,171),(102,150),(91,130),(93,115),(102,97),(103,76)]
tp(bodyinner,'b3')
# Flowing faceted planes give the trunk volume.
tp([(109,57),(120,53),(121,72),(111,96),(112,121),(105,147),(110,167),(106,193),(97,217),(80,229),(93,213),(100,190),(99,168),(104,149),(96,128),(102,103)],'b5')
tp([(121,54),(134,56),(140,68),(137,90),(143,110),(132,133),(132,156),(143,179),(144,202),(154,222),(143,215),(132,191),(119,170),(121,144),(127,118),(123,97),(126,75)],'b4')
tp([(145,64),(151,80),(151,98),(167,111),(162,128),(151,146),(156,164),(151,189),(157,209),(173,226),(160,224),(148,207),(145,185),(137,163),(138,144),(147,121),(143,101)],'b2')
tp([(108,124),(117,133),(114,151),(119,175),(111,199),(104,216),(91,226),(101,207),(106,185),(102,164)],'b2')
tp([(128,130),(134,143),(130,155),(137,179),(127,169),(121,157)],'b1')
tp([(156,98),(165,105),(171,111),(164,118),(154,121),(148,117)],'b4')
# Facets on the arms and hands.
for pts,col in [([(96,101),(83,93),(75,98),(68,111),(61,125),(59,140),(45,147),(40,145),(48,137),(56,118),(66,100),(81,89)],'b5'), ([(86,108),(76,111),(71,124),(65,144),(49,157),(43,157),(57,142),(65,119),(75,105)],'b1'), ([(158,104),(177,91),(185,100),(195,115),(204,133),(218,139),(216,146),(199,139),(189,121),(180,108),(170,108)],'b5'), ([(174,114),(183,114),(186,128),(194,141),(207,151),(213,152),(203,155),(187,144),(178,126)],'b1'), ([(71,110),(78,104),(83,105),(74,118),(68,132),(65,132)],'b6'), ([(182,103),(190,112),(195,125),(191,122),(185,115)],'b6')]: tp(pts,col)
# Roots in front turn the feet into a many-fingered pedestal.
frontroots=[ ([(107,191),(104,217),(87,230),(58,239),(45,237)],[17,15,11,5,1]), ([(113,205),(113,225),(103,239),(88,246),(82,244)],[12,11,7,4,1]), ([(145,194),(151,214),(169,226),(194,235),(212,233)],[18,15,11,6,1]), ([(148,211),(143,227),(150,240),(169,246),(181,243)],[12,10,7,5,1]), ([(96,219),(82,218),(70,225),(67,237)],[10,7,4,1]), ([(162,221),(179,217),(193,221),(198,228)],[11,7,4,1]) ]
for pts,ws in frontroots:
    tube(pts,ws,'b3')
    tube([(x-1,y-2) for x,y in pts],[max(1,w*.29) for w in ws],'b5',False)
# Save the structural colour mask before engraving weathered grain.
wood_indices={t.color(P[k]) for k in ['b1','b2','b3','b4','b5','b6','b7']}
wood={(x,y) for y in range(256) for x in range(256) if t.get(x,y) in wood_indices}
def clipped_line(a,b,col):
    x0,y0=a; x1,y1=b; n=max(abs(x1-x0),abs(y1-y0),1)
    for i in range(n+1):
        x=round(x0+(x1-x0)*i/n); y=round(y0+(y1-y0)*i/n)
        if (x,y) in wood: t.set(x,y,P[col])
# Long, broken bark strips follow the growth of each limb.
def grain(pts,widths):
    for i in range(len(pts)-1):
        a=pts[i]; b=pts[i+1]; dx=b[0]-a[0]; dy=b[1]-a[1]; d=max(1,math.hypot(dx,dy)); nx=-dy/d; ny=dx/d
        for offset in [-.31,-.08,.18,.35]:
            start=random.uniform(.0,.2); end=random.uniform(.65,1.)
            p=(round(a[0]+dx*start+nx*widths[i]*offset),round(a[1]+dy*start+ny*widths[i]*offset))
            q=(round(a[0]+dx*end+nx*widths[i+1]*offset),round(a[1]+dy*end+ny*widths[i+1]*offset))
            clipped_line(p,q,'b1')
            clipped_line((p[0]-1,p[1]-1),(q[0]-1,q[1]-1),random.choice(['b4','b5','b6']))
for pts,ws in crown+claws+frontroots+[(leftpts,[31,30,24,21,21]),(rightpts,[34,29,24,22,21])]: grain(pts,ws)
# Segmented vertical fissures and raised bark scales across the main bole.
for _ in range(108):
    x=random.randint(96,161); y=random.randint(53,219)
    if (x,y) not in wood: continue
    dx=random.choice([-3,-2,-1,1,2,3]); length=random.randint(4,13)
    col=random.choice(['b1','b2','b4','b5'])
    clipped_line((x,y),(x+dx,y+length//2),col)
    clipped_line((x+dx,y+length//2),(x+dx-1,y+length),col)
    if random.random()<.7:
        clipped_line((x-1,y+1),(x+dx-1,y+length//2),random.choice(['b5','b6']))
# Broad strips of exposed heartwood and chipped raised bark plates.
for pts,col in [
 ([(107,71),(110,65),(109,77),(106,83),(105,92),(103,96)],'b6'),
 ([(133,59),(137,63),(139,72),(137,79),(136,70)],'b6'),
 ([(109,135),(113,140),(111,151),(114,160),(113,166),(109,154)],'b5'),
 ([(133,133),(136,128),(139,126),(135,137),(134,148),(132,153)],'b5'),
 ([(139,151),(142,145),(143,156),(148,166),(148,174),(145,169)],'b4'),
 ([(100,175),(103,171),(103,185),(100,199),(96,210),(97,197)],'b6'),
 ([(114,181),(117,180),(113,195),(110,202),(111,193)],'b6'),
 ([(148,205),(151,209),(154,217),(160,223),(163,227),(155,222)],'b6'),
 ([(100,216),(98,221),(88,230),(76,233),(85,229),(94,222)],'b6'),
 ([(121,60),(122,65),(119,75),(120,79),(117,83),(116,79)],'b2')]: tp(pts,col)
for a,b in [((107,74),(108,68)),((135,64),(137,71)),((100,182),(99,191)),((109,139),(111,144)),((134,133),(137,127)),((152,215),(155,220)),((94,226),(88,230))]: tl(a,b,'b7')
# Large looping knots: hand-placed to preserve readable anatomy.
for x,y,rx,ry in [(105,143,5,10),(148,158,5,12),(78,111,5,7),(187,119,4,7),(113,68,4,7),(105,207,3,6)]:
    t.ellipse(x,y,rx,ry,P['b1']); t.ellipse(x-1,y-1,rx-1,ry-1,P['b5']); t.ellipse(x,y,rx-2,ry-2,P['b2'])
    tl((x,y-ry+4),(x-1,y+ry-3),'b0'); t.set(x-2,y-ry+1,P['b6'])
# Major black clefts in the lower trunk.
tp([(124,132),(120,143),(121,157),(116,170),(123,163),(128,168),(125,154),(129,144)],'b0')
tl((122,140),(119,151),'b6'); tl((117,166),(116,172),'b5')
tp([(152,176),(148,184),(151,196),(153,207),(155,201),(152,190),(156,184)],'b0')
# Face carved into the living trunk: deep, angular brows and wicked bright eyes.
tp([(104,84),(113,81),(124,87),(127,97),(116,98),(105,93),(101,88)],'b0')
tp([(134,86),(147,79),(154,82),(153,94),(143,98),(131,96)],'b0')
# Subdued green reflected light surrounds the sockets.
tp([(105,88),(114,85),(122,89),(124,95),(116,95),(107,92)],'g0')
tp([(135,89),(145,84),(151,85),(149,92),(140,95),(133,94)],'g0')
tp([(106,88),(113,88),(121,91),(121,94),(114,93),(108,91)],'g2')
tp([(135,91),(144,87),(150,86),(148,91),(141,93),(135,94)],'g2')
tl((108,88),(118,91),'g3'); tl((110,89),(118,92),'g4')
tl((137,91),(148,87),'g3'); tl((139,91),(147,88),'g4')
tp([(102,82),(111,78),(123,84),(128,89),(126,91),(114,85),(105,85)],'b5')
tl((105,81),(112,80),'b7'); tl((113,81),(122,85),'b6')
tp([(132,87),(142,79),(151,77),(153,81),(143,83),(133,90)],'b5')
tl((139,82),(146,79),'b6')
# Crooked central ridge and its shadow.
tp([(128,82),(131,90),(129,99),(134,106),(126,110),(120,104),(124,99)],'b2')
tl((128,86),(126,99),'b6'); tl((126,99),(123,103),'b5'); tl((123,104),(128,106),'b6')
# The maw is a jagged cavity, with splinter-like teeth.
tp([(108,105),(116,109),(124,110),(130,112),(140,106),(149,102),(147,115),(140,124),(127,128),(116,122),(110,115)],'b0')
tp([(115,114),(125,117),(139,113),(141,118),(132,124),(122,123)],'deep')
tp([(111,108),(117,111),(119,117),(115,115)],'b6')
tp([(123,112),(128,113),(126,119)],'b5')
tp([(139,108),(144,106),(141,115),(137,117)],'b6')
tp([(117,122),(119,117),(123,124)],'b4')
tp([(132,125),(135,119),(137,121)],'b5')
tl((112,118),(118,125),'b5'); tl((119,127),(129,130),'b5'); tl((134,128),(143,123),'b4')
# Moss cushions accumulate on upward-facing shoulders, crown and bark ledges.
def moss(x,y,rx,ry,seed):
    rng=random.Random(seed)
    # stepped, interlocking leaf clusters, with a dark fringe
    for j in range(10):
        xx=x+rng.randint(-rx,rx); yy=y+rng.randint(-ry,ry)
        ww=rng.randint(3,7); hh=rng.randint(2,4)
        t.rect(xx,yy,ww,hh,P['m0'])
    for j in range(18):
        xx=x+rng.randint(-rx+1,rx); yy=y+rng.randint(-ry,ry)
        t.rect(xx,yy,rng.randint(2,5),rng.randint(1,3),P[rng.choice(['m1','m1','m2','m2','m3'])])
    for j in range(5):
        xx=x+rng.randint(-rx+1,rx); yy=y+rng.randint(-ry,0)
        t.line(xx,yy,xx+2,yy,P['m4'])
for args in [(81,96,11,4,2),(171,99,12,4,6),(91,45,8,3,7),(153,44,9,3,8),(62,36,8,3,9),(194,31,9,3,10),(112,59,6,2,12),(107,132,4,3,14),(153,171,5,3,15),(94,215,7,3,16),(162,218,7,3,18),(55,139,5,2,19)]: moss(*args)
# Hanging vines, angular curves, small paired leaves.
def vine(points,seed):
    rng=random.Random(seed)
    for a,b in zip(points,points[1:]):
        tl((a[0]+1,a[1]),(b[0]+1,b[1]),'ink'); tl(a,b,'m2')
    for i in range(1,len(points)-1):
        x,y=points[i]; side=rng.choice([-1,1])
        tp([(x,y),(x+side*4,y-3),(x+side*3,y+1),(x,y+2)],'m3')
        t.set(x,y,P['m4'])
for pts,seed in [([(65,38),(64,50),(68,62),(66,78),(70,89)],1), ([(89,46),(87,60),(89,73),(85,85)],2), ([(162,45),(165,59),(162,73),(165,85)],3), ([(197,33),(200,46),(197,59),(199,71)],4), ([(76,98),(78,114),(73,128),(74,146),(80,158)],5), ([(86,100),(86,118),(90,132),(86,145)],6), ([(177,102),(173,117),(177,131),(176,148),(183,155)],7), ([(185,105),(183,118),(189,133),(187,142)],8), ([(153,172),(151,186),(156,198)],9)]: vine(pts,seed)
# Tufted hanging moss catches warmer light along the shoulders.
random.seed(117)
for x,y in [(77,99),(85,98),(167,101),(173,100),(158,44),(91,46),(60,38)]:
    for dx in range(-5,7,2):
        length=random.randint(4,12)
        tl((x+dx,y),(x+dx-1,y+length),'m0')
        tl((x+dx-1,y),(x+dx-2,y+length-2),'m1')
        if dx%3==0: tl((x+dx-1,y),(x+dx-2,y+length//2),'m3')
# A long creeper winds across the trunk, suggesting centuries of growth.
for a,b in zip([(102,120),(113,130),(129,134),(145,131),(155,138),(151,149)],[(113,130),(129,134),(145,131),(155,138),(151,149),(153,155)]):
    tl((a[0],a[1]+1),(b[0],b[1]+1),'b1'); tl(a,b,'m1')
for x,y,flip in [(112,129,1),(124,133,-1),(139,132,1),(154,139,1),(151,148,-1)]:
    tp([(x,y),(x+4*flip,y-5),(x+5*flip,y-3),(x+3*flip,y),(x,y+1)],'m2')
    tl((x,y-1),(x+3*flip,y-3),'m3')
# Reflections of the eyes catch ridges directly beneath the cavities.
tl((110,95),(116,97),'m2'); tl((141,98),(146,96),'m2')
t.set(118,97,P['m3']); t.set(139,99,P['m3'])
# Small shelf fungi make the ancient tree feel enormous.
for x,y in [(98,156),(155,133),(144,64)]:
    t.rect(x-3,y,7,2,P['b0']); t.rect(x-2,y-2,5,2,P['b6']); t.line(x-2,y-2,x+1,y-2,P['b7']); t.set(x+1,y+2,P['b2'])
# Selective gold rim light picks out broken upper-left bark edges.
rim_rng=random.Random(44)
wood_light={t.color(P[k]) for k in ['b2','b3','b4','b5','b6']}
ink_index=t.color(P['ink'])
for y in range(16,231):
    for x in range(25,233):
        idx=t.get(x,y)
        if idx not in wood_light: continue
        if (t.get(x-2,y-2)==ink_index or t.get(x-2,y-1)==ink_index) and rim_rng.random()<.5:
            t.set(x,y,P['b6'] if y>135 else P['b7'])
# Composite and tuck the lowest roots into foreground vegetation.
result=flatten([c,t],name='Ancient Treant Boss')
# Grass is concentrated near the edges and around the toes.
random.seed(91)
for _ in range(102):
    x=random.randint(3,252); y=random.randint(205,254)
    if 89<x<174 and y<239: continue
    if random.random()<.3 and 50<x<213: continue
    col=random.choice(['m0','m1','m2','grass'])
    h=random.randint(3,8)
    result.line(x,y,x-2,y-h,P[col]); result.line(x,y,x+2,y-h+2,P[col])
    if random.random()<.5: result.set(x-2,y-h,P['grasshi'])
# Ferns frame the roots; paired leaflets get smaller towards each tip.
def fern(x,y,lean,height):
    tip=(x+lean,y-height)
    result.line(x+1,y,tip[0]+1,tip[1],P['deep'])
    result.line(x,y,*tip,P['m2'])
    for j in range(1,6):
        u=j/7; xx=round(x+lean*u); yy=round(y-height*u)
        span=round(7*(1-u)+2)
        result.line(xx,yy,xx-span,yy-4,P['m1'])
        result.line(xx,yy-1,xx-span+1,yy-5,P['m2'])
        result.line(xx,yy,xx+span,yy-3,P['m2'])
        result.line(xx+2,yy-2,xx+span,yy-4,P['m3'])
for x,y in [(25,237),(232,229),(49,252),(206,251)]:
    fern(x,y,-9,18); fern(x,y,4,23); fern(x,y,13,13)
# Pale mushrooms and tiny gold flowers give a sense of scale.
for x,y in [(45,218),(48,216),(212,224),(216,225),(68,247)]:
    result.rect(x,y,1,4,P['b6']); result.rect(x-2,y-1,5,2,P['b3'])
    result.line(x-1,y-2,x+1,y-2,P['b7'])
# A few airborne spores catch the light.
for x,y in [(41,94),(50,113),(70,170),(202,97),(213,188),(91,28),(166,18),(34,181),(230,111),(117,18),(207,60),(68,67),(178,181),(84,184),(201,204)]:
    result.set(x,y,P['m4'])
    if (x+y)%3==0: result.set(x,y-1,P['ray'])
# Dark near-ground framing leaves.
for pts in [[(0,253),(0,234),(8,240),(13,229),(15,247),(26,238),(22,253)],[(229,255),(236,245),(237,231),(243,241),(251,224),(250,245),(255,239),(255,255)]]:
    poly(pts,'deep',result)
view(result)
print(result.stats_text())
assert result.stats()['size']==(256,256) or result.stats()['size']==[256,256]
assert result.stats()['colors_used']<=120
save('ancient-treant-boss',result)
finish(result)
