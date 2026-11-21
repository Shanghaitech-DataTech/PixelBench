import random
random.seed(19)
result = new_canvas(128, 128, name='Sunrise in the high valley')
c = result
P = {
'sky0':'#797b9d','sky1':'#99869e','sky2':'#b591a4','sky3':'#d0a0a5','sky4':'#e6b1a4','sky5':'#f2c29e','sky6':'#f7d5a6','sun':'#ffe8b2','sunCore':'#fff0bd',
'cloudShade':'#ce9ba1','cloud':'#f4c6ae','cloudLight':'#ffddba',
'far':'#a496af','farLight':'#c7b1bb','farShade':'#8c87a4','snow':'#ecd2c7','snowShade':'#c3b4c9',
'mount':'#777c96','mountLight':'#9d95a7','mountShade':'#646e8b','ridge':'#586a7b','ridgeLight':'#7e8a91','ridgeShade':'#465c70',
'forestFar':'#647c7b','forestLight':'#82938a','forestShade':'#4f6c6c',
'grassBack':'#7e937d','grassLight':'#a4ad82','grass':'#657f64','grassShade':'#506c58','grassDark':'#3d594d','goldGrass':'#c1ba7c','grassTip':'#dfca87',
'pineDark':'#243f40','pine':'#31564b','pineMid':'#44715a','pineLight':'#668467','pineGold':'#98a274',
'ink':'#343645','woodDark':'#593f41','woodShade':'#805143','wood':'#a86c48','woodMid':'#c38a54','woodLight':'#dfaa69','woodEdge':'#f0c883',
'roofDark':'#633e43','roofShade':'#925345','roof':'#bd704f','roofLight':'#d9905c','roofTip':'#eeb37b',
'windowDark':'#633c37','window':'#f8bd67','windowLight':'#ffdfa0',
'stoneDark':'#57615d','stone':'#829088','stoneLight':'#abb1a0','stoneSun':'#c8bea1','pathDark':'#786f62','path':'#a3987d',
'smokeShade':'#bcb0ba','smoke':'#dac4c2','smokeLight':'#eed6c7','flower':'#e9b878','flowerShade':'#b88860'
}
for k,v in P.items(): c.color(v,k)
def poly(points, col): c.poly(points,col)
def line(a,b,col): c.line(*a,*b,col)
# A quiet, banded dawn sky.
for y,h,col in [(0,7,'sky0'),(7,8,'sky1'),(15,8,'sky2'),(23,8,'sky3'),(31,9,'sky4'),(40,10,'sky5'),(50,24,'sky6')]:
    c.rect(0,y,128,h,col)
# Long, broken cloud shelves, kept away from the sun.
poly([(0,19),(11,19),(11,17),(24,17),(24,18),(35,18),(35,20),(45,20),(45,22),(16,22),(16,23),(0,23)],'cloudShade')
c.rect(3,20,27,1,'cloud');c.rect(9,18,13,1,'cloud')
poly([(84,13),(95,13),(95,11),(106,11),(106,12),(115,12),(115,14),(127,14),(127,17),(107,17),(107,16),(84,16)],'cloudShade')
c.rect(92,15,24,1,'cloud');c.rect(110,17,18,1,'cloudLight')
c.rect(1,35,16,2,'cloud');c.rect(6,34,18,1,'cloud');c.rect(0,37,10,1,'cloudLight')
c.rect(100,31,15,1,'cloudLight');c.rect(110,29,18,2,'cloud')
# The rising disk is partly swallowed by the distant peaks.
c.circle(62,34,13,'sun');c.circle(62,34,10,'sunCore')
c.rect(44,47,37,1,'sky6')
# Far snowy range.
poly([(0,52),(8,47),(14,49),(30,28),(38,37),(43,35),(55,49),(68,44),(83,27),(91,39),(96,35),(112,49),(121,44),(127,47),(127,77),(0,77)],'far')
poly([(0,52),(8,47),(13,50),(30,28),(25,43),(19,47),(17,52),(8,55)],'farLight')
poly([(30,28),(38,37),(43,35),(55,49),(58,60),(39,50),(35,40)],'farShade')
poly([(20,40),(30,28),(38,37),(34,36),(32,39),(29,35),(25,40),(25,37)],'snow')
poly([(30,29),(32,39),(29,35),(27,37)],'snowShade')
poly([(65,48),(83,27),(78,42),(73,43),(70,48),(68,52)],'farLight')
poly([(83,27),(91,39),(96,35),(113,50),(108,59),(89,47),(85,39)],'farShade')
poly([(75,37),(83,27),(91,39),(86,36),(84,38),(82,34),(79,39),(78,36)],'snow')
poly([(84,29),(86,37),(84,38),(82,34)],'snowShade')
# Second layer, indigo crags; open saddle beneath the sun.
poly([(0,51),(10,45),(22,58),(34,48),(42,55),(50,60),(60,59),(68,64),(80,51),(91,48),(102,58),(112,50),(127,56),(127,85),(0,85)],'mount')
poly([(0,51),(10,45),(7,54),(17,61),(21,66),(0,65)],'mountLight')
poly([(10,45),(22,58),(29,55),(34,48),(31,61),(42,67),(39,77),(10,71)],'mountShade')
poly([(68,64),(80,51),(91,48),(87,54),(82,55),(78,62),(75,62),(72,67)],'mountLight')
poly([(91,48),(102,58),(112,50),(108,60),(121,69),(119,78),(85,76)],'mountShade')
# Rounder, closer foothills hide the mountain bases.
poly([(0,67),(10,62),(20,64),(29,62),(40,67),(51,69),(65,70),(76,67),(88,61),(99,60),(113,65),(127,61),(127,90),(0,90)],'ridge')
poly([(0,68),(12,64),(28,64),(40,69),(49,72),(32,71),(18,68),(6,70)],'ridgeLight')
poly([(72,70),(89,64),(99,62),(112,67),(127,64),(127,86),(70,84)],'ridgeShade')
# Small clustered conifers define the depth between village and mountains.
def distant_tree(x,y,h,col):
    c.line(x,y,x,y+h,col)
    poly([(x,y),(x-2,y+5),(x-1,y+5),(x-3,y+h-1),(x+3,y+h-1),(x+1,y+5),(x+2,y+5)],col)
for x in range(0,128,4):
    y = 65 + int(3*__import__('math').sin(x*.07)) + random.choice([-1,0,1])
    distant_tree(x,y,random.randrange(6,11),'forestFar')
# The sloping village meadow.
poly([(0,82),(15,79),(29,81),(43,79),(59,78),(72,77),(88,73),(105,74),(116,77),(127,76),(127,127),(0,127)],'grassBack')
poly([(0,92),(17,88),(29,90),(46,86),(64,88),(80,83),(95,83),(109,80),(127,83),(127,127),(0,127)],'grass')
poly([(0,111),(13,108),(23,110),(34,106),(46,111),(68,106),(90,103),(113,100),(127,102),(127,127),(0,127)],'grassShade')
poly([(0,122),(21,116),(34,118),(48,124),(68,121),(83,117),(102,112),(127,113),(127,127),(0,127)],'grassDark')
# Thin light on the meadow terraces.
for pts,col in [([(1,86),(17,83),(28,85),(39,83)],'grassLight'), ([(87,79),(103,77),(116,80)],'grassLight'), ([(20,111),(32,109),(45,113)],'goldGrass'), ([(89,103),(108,101),(118,104)],'grassLight')]:
    for a,b in zip(pts,pts[1:]): line(a,b,col)
# Ground texture comes in deliberate horizontal clusters.
ids = {c.color(n) for n in ['grassBack','grass','grassShade','grassDark']}
for i in range(240):
    x=random.randrange(2,126); y=random.randrange(81,128)
    base=c.get(x,y)
    if base in ids:
        col = random.choice(['grassLight','goldGrass']) if base == c.color('grassBack') else random.choice(['grass','grassShade','grassLight'])
        w=random.choice([1,2,2,3,4])
        for xx in range(x,min(x+w,127)):
            if c.get(xx,y)==base:c.set(xx,y,col)
# Conifers behind the cottages.
def pine(x,y,h,scheme='normal'):
    # Deliberately stepped branch tiers, a tapered trunk, warm upper-left tips.
    cols = ('forestShade','forestFar','forestLight') if scheme=='far' else ('pineDark','pine','pineMid')
    dark,mid,light=cols
    c.rect(x-1,y+h//2,2,h-h//2+3,'woodDark' if scheme!='far' else 'forestShade')
    for j in range(4):
        top=y+int(h*j*.16)
        bot=y+int(h*(.35+j*.19))
        half=max(2,int(h*(.12+j*.045)))
        poly([(x,top),(x-half+2,bot-3),(x-half,bot),(x-2,bot-1),(x+1,bot+1),(x+half,bot),(x+half-2,bot-3)],dark)
        poly([(x,top),(x-1,top+4),(x-half+2,bot-2),(x-1,bot-3),(x+1,bot-1),(x+half-2,bot-1)],mid)
        line((x-1,top+4),(x-half+2,bot-2),light)
        if h>25:
            c.line(x-half+1,bot-1,x-half+3,bot-1,light)
            c.line(x+2,bot-3,x+half-2,bot-2,dark)
    c.set(x,y,light)
for x,y,h in [(4,65,23),(17,63,20),(37,64,23),(95,56,23),(115,58,24),(124,66,21)]: pine(x,y,h,'far')
# Sunlit clearing and little routes that meet at the central steps.
poly([(98,92),(103,94),(92,100),(83,104),(70,109),(65,106),(80,101),(89,98)],'pathDark')
poly([(100,93),(101,94),(89,100),(81,103),(69,107),(67,106),(81,102),(91,98)],'path')
poly([(24,102),(28,102),(36,106),(49,108),(62,107),(70,109),(67,114),(51,113),(36,111),(26,106)],'pathDark')
poly([(26,103),(29,105),(38,108),(52,110),(65,109),(67,112),(50,111),(36,110)],'path')
poly([(60,98),(66,98),(68,103),(78,106),(84,110),(85,115),(80,120),(76,127),(46,127),(55,119),(67,113),(67,110),(60,106),(58,102)],'pathDark')
poly([(61,99),(65,99),(65,103),(74,107),(81,111),(81,115),(75,121),(69,127),(49,127),(59,119),(71,113),(70,109),(61,105)],'path')
# Smaller path stones run towards the houses.
for x,y,w in [(97,95,3),(91,98,3),(86,100,3),(79,103,4),(27,104,3),(33,107,3),(40,109,4),(48,110,3),(55,110,4),(62,105,3),(65,107,4),(70,108,3),(73,110,4)]:
    c.line(x,y,x+w,y,'stoneLight');c.set(x+w,y+1,'stoneDark')
# Individually shaped foreground cobbles.
for x,y,w,h in [(73,112,6,3),(67,114,5,3),(75,116,5,3),(61,118,6,3),(68,120,6,3),(55,122,6,3),(61,125,7,3),(72,124,3,3),(51,126,6,2),(61,112,3,2)]:
    poly([(x+1,y),(x+w-1,y),(x+w,y+1),(x+w-1,y+h),(x,y+h),(x-1,y+1)],'stoneDark')
    poly([(x+1,y),(x+w-1,y),(x+w-1,y+1),(x+w-2,y+h-1),(x,y+h-1),(x,y+1)],'stoneLight')
    c.line(x+1,y,x+w-2,y,'stoneSun')
# Cottage casting shadows into the lawn.
poly([(42,99),(76,96),(91,101),(78,106),(47,106),(38,103)],'grassShade')
poly([(10,102),(36,99),(46,103),(36,108),(12,108)],'grassShade')
poly([(91,94),(114,92),(120,97),(104,100),(89,98)],'grassShade')
# Three timber cottages: side and front planes share a coherent light direction.
def cottage(cx,apex,half,base,depth,hero=False):
    # Front gable sits at cx; rear ridge is offset up and to the right.
    eave=apex+half+2
    left=cx-half;right=cx+half
    shift=depth
    # Foundation and solid body.
    poly([(left+2,eave-1),(cx,apex+4),(right-1,eave-1),(right-1,base),(left+2,base)],'woodDark')
    poly([(right-1,eave-1),(right+shift-2,eave-4),(right+shift-2,base-4),(right-1,base)],'woodShade')
    poly([(left+3,eave),(cx,apex+5),(right-2,eave),(right-2,base-3),(left+3,base-3)],'woodMid' if hero else 'wood')
    poly([(left+3,eave),(cx,apex+5),(cx+2,apex+8),(left+5,eave),(left+5,base-3),(left+3,base-3)],'woodLight')
    for y in range(eave+2,base-3,4):
        c.line(left+3,y,right-2,y,'woodShade')
        c.line(left+4,y+1,right-3,y+1,'woodLight' if hero else 'woodMid')
        c.line(right,y,right+shift-3,y-3,'woodDark')
        if shift>6:c.line(right,y+1,right+shift-3,y-2,'wood')
    # Gable boards taper upwards.
    for y in range(apex+9,eave,3):
        hw=max(1,y-apex-5)
        c.line(cx-hw,y,cx+hw,y,'woodShade')
        c.line(cx-hw+1,y+1,cx+hw-1,y+1,'woodLight' if hero else 'woodMid')
    # Roof in silhouette, then the illuminated receding slope.
    poly([(left-2,eave+2),(cx-1,apex),(cx+shift,apex-3),(right+shift+2,eave-2),(right+1,eave+3),(cx,apex+5),(left+1,eave+3)],'roofDark')
    poly([(cx,apex+1),(cx+shift,apex-2),(right+shift,eave-3),(right+1,eave),(cx+1,apex+3)],'roof')
    poly([(cx+shift,apex-2),(right+shift,eave-3),(right+1,eave),(right-1,eave-3),(cx+shift-2,apex-1)],'roofShade')
    # Shingle courses with staggered gaps.
    for k in range(4,half+2,3):
        c.line(cx+k-1,apex+k,cx+shift+k-2,apex+k-3,'roofLight')
        for xx in range(cx+k+2,cx+shift+k-2,4):c.set(xx,apex+k-1-(xx-(cx+k))//max(1,shift//3),'roofDark')
    c.line(cx,apex,cx+shift,apex-3,'roofTip')
    c.line(left-2,eave+1,cx,apex,'woodDark')
    c.line(left-1,eave,cx,apex+1,'roofTip')
    c.line(cx,apex+2,right+1,eave+1,'roofLight')
    c.line(right+1,eave+1,right+shift+1,eave-2,'woodDark')
    c.line(right+1,eave,right+shift,eave-3,'roofLight')
    # Timber frame: wall corners, lintel and gable king post.
    c.rect(left+2,eave+1,2,base-eave-2,'woodDark')
    c.rect(right-3,eave+1,2,base-eave-2,'woodDark')
    c.line(left+4,eave+1,right-2,eave+1,'woodDark')
    c.line(left+4,eave+2,right-4,eave+2,'woodEdge' if hero else 'woodMid')
    c.line(cx,apex+5,cx,apex+10,'woodDark')
    # Stone foundation blocks.
    c.rect(left+2,base-2,2*half-2,3,'stoneDark')
    for xx in range(left+3,right-1,5):
        c.rect(xx,base-2,min(4,right-xx-1),2,'stone')
        c.set(xx,base-2,'stoneLight')
    c.line(right,base-1,right+shift-2,base-4,'stoneDark')
    # The front door.
    dw=7 if hero else 5
    dx=cx-2;dy=base-(14 if hero else 11)
    c.rect(dx-1,dy-1,dw+2,base-dy,'woodDark')
    c.rect(dx,dy,dw,base-dy-2,'woodShade')
    for xx in range(dx+1,dx+dw,2):c.line(xx,dy+1,xx,base-3,'wood')
    c.line(dx,dy,dx+dw-1,dy,'woodLight')
    c.set(dx+dw-2,dy+6,'windowLight')
    if hero:
        c.rect(dx+2,dy+2,3,3,'window');c.set(dx+2,dy+2,'windowLight')
    # Golden window with inset shadow and mullions.
    wx=left+6;wy=base-(13 if hero else 11)
    ww=6 if hero else 5;wh=6 if hero else 5
    c.rect(wx-1,wy-1,ww+2,wh+2,'woodDark')
    c.rect(wx,wy,ww,wh,'window')
    c.rect(wx,wy,max(2,ww//2),wh-1,'windowLight')
    c.line(wx+ww//2,wy,wx+ww//2,wy+wh-1,'woodShade')
    c.line(wx,wy+wh//2,wx+ww-1,wy+wh//2,'woodShade')
    c.line(wx-1,wy+wh+1,wx+ww,wy+wh+1,'woodLight')
    if hero:
        # Attic window and the side window.
        c.rect(cx-3,apex+11,7,7,'woodDark');c.rect(cx-2,apex+12,5,4,'window')
        c.line(cx-2,apex+12,cx+2,apex+12,'windowLight');c.line(cx,apex+12,cx,apex+15,'woodShade')
        sx=right+2;sy=eave+5
        poly([(sx-1,sy),(sx+5,sy-2),(sx+5,sy+6),(sx-1,sy+8)],'woodDark')
        poly([(sx,sy+1),(sx+4,sy),(sx+4,sy+5),(sx,sy+6)],'window')
        c.line(sx+2,sy+1,sx+2,sy+5,'woodShade');c.line(sx,sy+3,sx+4,sy+2,'woodShade')
    # Thick cap and warm edge on each chimney.
    chx=cx+shift+1;chy=apex-2
    c.rect(chx,chy,4,11 if hero else 8,'woodDark')
    c.rect(chx,chy,3,10 if hero else 7,'stone')
    c.line(chx,chy,chx,chy+7,'stoneSun')
    c.line(chx+1,chy+3,chx+2,chy+3,'stoneDark');c.set(chx+1,chy+6,'stoneDark')
    c.rect(chx-1,chy-1,6,2,'stoneDark');c.rect(chx-1,chy-1,5,1,'stoneLight')
    return chx+1,chy-2
# Back right, then left, then central focal cottage.
chimR=cottage(99,68,10,95,6,False)
chimL=cottage(23,75,13,105,7,False)
chimC=cottage(59,61,16,101,13,True)
# Central entry: broad lit doorstep joins the stone path.
c.rect(56,99,12,3,'stoneDark');c.rect(56,99,11,1,'stoneSun')
c.rect(55,102,14,2,'stone');c.rect(55,102,13,1,'stoneLight')
# Porch lantern and firewood, small human-scale details.
c.line(70,83,73,83,'woodDark');c.line(72,83,72,85,'woodDark')
c.rect(70,85,4,5,'woodDark');c.rect(71,86,2,3,'window');c.set(71,86,'windowLight')
for x,y in [(79,98),(83,97),(87,96),(81,96),(85,95)]:
    c.rect(x-1,y-1,4,3,'woodDark');c.rect(x,y-1,2,2,'woodMid');c.set(x,y,'woodLight')
# Pale, broken smoke ribbons drift left through the still morning.
poly([(chimC[0]-1,chimC[1]+1),(chimC[0]+2,chimC[1]+1),(chimC[0]+3,53),(71,50),(69,48),(70,45),(67,43),(65,44),(65,47),(68,51),(71,53)],'smokeShade')
poly([(chimC[0],chimC[1]),(chimC[0]+1,chimC[1]),(74,53),(71,51),(70,49),(69,49),(68,46),(69,44),(66,43),(66,47),(68,50),(72,54)],'smoke')
c.line(66,43,65,41,'smokeLight');c.line(65,40,67,39,'smoke');c.set(68,38,'smokeShade')
poly([(chimL[0]-1,chimL[1]+1),(chimL[0]+1,chimL[1]+1),(33,68),(30,65),(29,63),(30,60),(28,59),(27,62),(28,65),(31,68)],'smoke')
c.line(28,59,26,57,'smokeShade');c.set(27,55,'smokeShade');c.set(29,62,'smokeLight')
poly([(chimR[0],chimR[1]+1),(chimR[0]+1,chimR[1]+1),(108,60),(105,57),(104,54),(102,54),(103,58),(106,60)],'smokeShade')
c.line(104,55,104,57,'smoke');c.line(107,60,107,63,'smoke')
# Fence along the right terrace, receding towards the cottage.
for x,y,h in [(91,103,7),(99,100,6),(107,99,6),(114,98,5)]:
    c.rect(x,y-h,2,h+1,'woodDark');c.line(x,y-h,x,y-1,'woodMid');c.set(x,y-h,'woodEdge')
for off in [-5,-2]:
    c.line(91,103+off,99,100+off,'wood');c.line(99,100+off,107,99+off,'wood');c.line(107,99+off,114,98+off,'wood')
    c.line(91,102+off,99,99+off,'woodLight');c.line(99,99+off,114,97+off,'woodMid')
# Foreground framing pines, richly tiered and asymmetric.
pine(5,60,53)
pine(121,51,66)
pine(125,83,39)
# A few warmer branch catches on the sunrise-facing left pine.
for x,y,w in [(4,67,2),(1,78,3),(0,89,4),(2,98,3),(116,76,3),(110,94,4),(107,107,4)]:c.line(x,y,x+w,y,'pineLight')
# Rocks and low plants anchor the foreground.
def rock(x,y,w,h):
    poly([(x,y),(x+2,y-h),(x+w-2,y-h-1),(x+w,y-1),(x+w-1,y+1),(x+1,y+1)],'stoneDark')
    poly([(x+1,y-1),(x+2,y-h),(x+w-3,y-h-1),(x+w-1,y-2),(x+w-3,y-1)],'stone')
    c.line(x+2,y-h,x+w-3,y-h-1,'stoneLight')
rock(34,119,9,4);rock(89,124,12,5);rock(13,113,7,3);rock(111,116,5,3)
for x,y in [(22,120),(29,125),(37,111),(46,115),(87,114),(98,109),(102,124),(17,117),(42,126),(88,121),(109,119)]:
    c.line(x,y,x-2,y-3,'pineMid');c.line(x,y,x+2,y-2,'grassLight');c.line(x,y,x,y-4,'grass')
for x,y in [(23,113),(27,115),(31,113),(42,108),(46,111),(88,108),(94,112),(98,114),(21,122),(24,125),(104,120)]:
    c.line(x,y,x,y+2,'grassDark');c.set(x,y,'flower');
    if x%2:c.set(x+1,y,'flowerShade')
# A few clear grass edges along the cobbles.
for x,y in [(54,117),(48,123),(45,126),(82,120),(87,115),(82,107),(57,107)]:
    c.line(x,y,x-1,y-2,'grassDark');c.set(x+1,y-1,'goldGrass')
# Small finishing touches: irregular cobbles and grass lapping their edges.
for x,y,w in [(61,104,3),(65,106,3),(68,109,4),(78,114,2),(65,117,3),(57,121,3),(53,125,3)]:
    c.line(x,y,x+w-1,y,'stoneSun')
    c.line(x,y+1,x+w-1,y+1,'stone')
c.set(72,114,'pathDark');c.set(76,118,'pathDark');c.set(63,121,'pathDark')
c.line(56,123,58,123,'stoneDark');c.line(64,126,66,126,'stoneDark')
# Chipped golden roof edges and the sun-facing timber corner.
c.line(44,79,52,71,'roofTip')
c.line(45,82,45,95,'woodLight')
c.set(45,85,'woodEdge');c.set(45,93,'woodEdge')
# Wood-grain dashes kept outside the door and windows.
for x,y,w in [(49,83,3),(63,85,4),(62,97,3),(16,93,2),(31,97,2),(104,88,2),(51,97,2)]:
    c.line(x,y,x+w-1,y,'woodShade')
# Moss and a tiny cluster of flowers beside the welcome step.
c.line(42,101,47,101,'grass');c.set(43,100,'goldGrass')
for x,y in [(47,100),(49,102),(51,100)]:
    c.set(x,y,'flower');c.set(x,y+1,'grassDark')
# Forked pine tips break the silhouette into natural boughs.
for x,y,d in [(1,78,1),(3,89,1),(1,99,1),(6,106,1),(118,74,-1),(114,87,-1),(110,99,-1),(113,110,-1)]:
    c.line(x,y,x+3*d,y-2,'pineMid')
    c.line(x+1*d,y,x+3*d,y,'pineLight')
# Two tiny distant birds in the open sky.
c.line(34,14,36,15,'farShade');c.line(36,15,38,14,'farShade')
c.set(42,18,'farShade');c.set(44,18,'farShade');c.set(43,19,'farShade')
assert c.stats()['size'] == (128,128) or c.stats()['size'] == [128,128]
assert c.stats()['colors_used'] <= 86
print(c.stats_text())
view(result,scale=4,margin=0)
save('mountain-village-sunrise',result)
finish(result)
