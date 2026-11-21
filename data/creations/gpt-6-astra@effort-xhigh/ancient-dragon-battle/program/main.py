import random, math
random.seed(24)
result = new_canvas(256,256, name='Ancient dragon — the last rampart')
c = result
# A closed, hand-picked palette: dusk violets, blue slate, verdigris and furnace gold.
P = {
'ink':'#171826','black':'#10131e','deep':'#242337','plum':'#382b43','cloud':'#4c354e','cloudlit':'#815060',
'sky0':'#59435e','sky1':'#765069','sky2':'#9b5b6d','sky3':'#bd6a70','sky4':'#d98172','sky5':'#e69a78','sky6':'#edb17e',
'sun':'#ffd599','sunhot':'#ffe6ad','haze':'#c48b80',
'mtnfar':'#826b7c','mtnedge':'#ad7d86','mtn':'#5d5b72','mtnlight':'#817084','mtnnear':'#42465e',
'smokedark':'#353442','smoke':'#4b414d','smokemid':'#61505a','smokelit':'#86616a','smokehot':'#ac6d65',
'land':'#55505b','landlit':'#736061','earth':'#3b3847','earthlit':'#5a4b51','rock':'#343642','rocklit':'#5c5153',
'stone0':'#303343','stone1':'#444959','stone2':'#5d6070','stone3':'#7b7983','stonelit':'#ad9490','stonehot':'#c28c6c',
'roof':'#42343f','rooflit':'#715052',
'wood0':'#332831','wood1':'#594039','wood2':'#805342','wood3':'#ad7450','rope':'#c29666',
'red0':'#612e39','red1':'#963b3e','red2':'#c35443','red3':'#e17e51',
'fire0':'#a43e3d','fire1':'#df5837','fire2':'#f7873b','fire3':'#ffb74e','fire4':'#ffe18b','fire5':'#fff1ba',
'dragon0':'#172e35','dragon1':'#24454a','dragon2':'#3b5d5d','dragon3':'#668078','dragon4':'#a3a892',
'wing0':'#382c36','wing1':'#663d43','wing2':'#925249','wing3':'#c07856','wing4':'#e3a06a',
'armor0':'#303e50','armor1':'#617387','armor2':'#a6b0b4','armor3':'#e0cfb4','gold':'#d3a16a'
}
def col(k): return P.get(k,k)
def rect(x,y,w,h,k): c.rect(x,y,w,h,col(k))
def line(x,y,X,Y,k): c.line(x,y,X,Y,col(k))
def poly(pts,k,edge=None):
    c.poly(pts,col(k))
    if edge: c.poly(pts,col(edge),fill=False)
def path(d,k,edge=None):
    c.path(d,col(k))
    if edge: c.path(d,col(edge),fill=False)
def ellipse(x,y,rx,ry,k): c.ellipse(x,y,rx,ry,col(k))
def pix(x,y,k):
    if 0<=x<256 and 0<=y<256: c.set(x,y,col(k))
def speckle(bounds,base,shades,count,cluster=False):
    ids=[c.color(col(k)) for k in base]
    x0,y0,x1,y1=bounds
    for _ in range(count):
        x=random.randint(x0,x1); y=random.randint(y0,y1)
        if c.get(x,y) in ids:
            k=random.choice(shades); pix(x,y,k)
            if cluster and x+1<256 and c.get(x+1,y) in ids: pix(x+1,y,k)
# Strata of sunset, with a little ordered pixel dithering at colour boundaries.
bands=[(0,24,'sky0'),(24,43,'sky1'),(43,65,'sky2'),(65,87,'sky3'),(87,111,'sky4'),(111,139,'sky5'),(139,183,'sky6'),(183,256,'land')]
for y0,y1,k in bands: rect(0,y0,256,y1-y0,k)
for i in range(len(bands)-2):
    y=bands[i][1]
    for yy in range(y-2,y+2):
        for xx in range(256):
            if (xx+2*yy)%4 < yy-y+2: pix(xx,yy,bands[i+1][2])
# The sun is deliberately offset behind the outstretched right wing.
ellipse(187,75,34,34,'sun')
ellipse(187,75,29,29,'sunhot')
rect(151,91,73,2,'sky4'); rect(161,103,53,2,'sky4')
# Long, broken clouds frame the wing tips.
poly([(0,14),(19,14),(25,17),(52,18),(57,21),(81,22),(91,26),(80,29),(48,29),(42,27),(20,26),(14,24),(0,24)],'cloud')
line(3,25,24,26,'cloudlit'); line(41,28,72,29,'cloudlit')
poly([(134,7),(158,7),(165,10),(196,10),(207,13),(240,14),(255,17),(255,24),(227,24),(219,21),(188,21),(182,18),(154,17),(143,13)],'cloud')
line(179,20,214,21,'cloudlit'); line(231,25,255,26,'sky2')
poly([(0,60),(18,60),(24,63),(42,63),(48,66),(40,69),(11,69),(0,67)],'cloudlit')
poly([(217,48),(235,46),(255,48),(255,56),(238,54),(222,54),(210,52)],'sky2')
line(223,56,249,56,'sky5')
poly([(0,100),(17,97),(26,100),(51,99),(64,103),(53,107),(21,106),(8,108),(0,106)],'sky3')
line(2,109,27,109,'sky6'); line(31,107,44,107,'sky5')
# Distant peaks, with angular illuminated faces and drifting foothill haze.
poly([(0,150),(0,138),(16,128),(24,130),(45,109),(57,125),(68,119),(93,143),(119,130),(137,138),(155,119),(168,128),(187,113),(203,134),(216,122),(233,135),(247,118),(255,125),(255,182),(0,182)],'mtnfar')
for pts in [[(22,132),(45,109),(56,124),(47,120),(43,117),(37,129)],[(144,134),(155,119),(167,128),(156,125)],[(175,129),(187,113),(202,134),(186,122)],[(234,134),(247,118),(254,125),(247,123)]]: poly(pts,'mtnedge')
poly([(0,167),(0,154),(18,147),(33,153),(54,136),(66,145),(80,139),(99,158),(122,146),(142,158),(161,143),(178,157),(194,141),(212,154),(230,139),(255,151),(255,190),(0,190)],'mtn')
poly([(0,170),(24,157),(37,161),(54,136),(49,155),(58,161),(68,155),(78,165),(91,163),(110,177)],'mtnlight')
poly([(201,170),(230,139),(223,158),(237,156),(255,164),(255,179)],'mtnlight')
rect(0,175,256,2,'haze')
poly([(0,182),(27,169),(53,176),(73,164),(97,178),(125,170),(153,177),(171,167),(197,172),(216,164),(234,171),(255,170),(255,203),(0,203)],'mtnnear')
# Tiny far battlements embedded in the haze.
for x,y in [(5,162),(10,164),(238,155),(243,153),(248,155)]:
    rect(x,y,4,13,'mtn'); rect(x-1,y-1,2,3,'mtn'); rect(x+3,y-1,2,3,'mtn')
# Land and the pale road climbing towards the keep.
poly([(0,204),(40,188),(78,190),(113,184),(169,187),(219,185),(255,198),(255,255),(0,255)],'land','earth')
poly([(111,207),(151,207),(164,225),(196,255),(100,255),(124,225)],'landlit')
poly([(123,210),(149,210),(148,225),(165,255),(124,255),(133,230)],'earthlit')
for _ in range(150):
    x=random.randrange(256); y=random.randrange(191,256)
    if c.get(x,y) in [c.color(col('land')),c.color(col('landlit'))]:
        line(x,y,min(255,x+random.randrange(2,7)),y,random.choice(['earthlit','earth','landlit']))
# Smoke rises in clustered, wind-bent volumes behind the architecture and dragon.
def smoke_column(x,y,lean,height,scale):
    for i in range(height):
        yy=y-i*4; xx=x+int(lean*i)+int(2*math.sin(i))
        rr=int(scale+i*.25)
        ellipse(xx,yy,rr+2,rr,'smokedark')
        ellipse(xx-2,yy-2,rr,rr-1,'smoke')
        if i%2==0: ellipse(xx-3,yy-3,max(2,rr-3),max(2,rr-4),'smokemid')
        if i<4: ellipse(xx+3,yy+2,rr-2,rr-1,'smokelit')
smoke_column(101,158,-1.8,17,6)
smoke_column(180,165,1.7,19,7)
smoke_column(145,149,1.6,9,4)
# Further haze wisps between turrets.
path('M 82 156 Q 72 149 80 140 Q 88 133 81 126 Q 91 132 88 143 Q 83 150 92 156 Z','smokelit')
# Castle stands on a sharply edged bluff.
poly([(60,200),(84,191),(106,199),(134,190),(167,196),(197,192),(214,206),(203,218),(187,224),(164,225),(148,217),(126,220),(103,229),(80,218),(56,219),(44,211)],'rock','ink')
for pts in [[(62,202),(86,197),(74,211),(58,215)],[(86,202),(105,204),(98,222),(87,215)],[(155,201),(178,199),(168,213),(171,219),(155,215)],[(183,201),(201,198),(208,208),(188,218),(195,208)]]: poly(pts,'rocklit')
for x,y,X,Y in [(57,207,69,205),(86,213,97,219),(173,216,179,209),(194,211,202,205),(112,213,104,222)]: line(x,y,X,Y,'earth')
# Castle masonry helpers.
def masonry(x,y,w,h,base='stone1',bw=8,bh=5):
    rect(x,y,w,h,base)
    for yy in range(y+2,y+h-1,bh):
        line(x,yy,x+w-1,yy,'stone0')
        offset=0 if ((yy-y)//bh)%2 else bw//2
        for xx in range(x+offset,x+w,bw):
            line(xx,yy,xx, min(y+h-1,yy+bh-1),'stone0')
            if xx+2<x+w and random.random()<.6: line(xx+1,yy+1,min(x+w-1,xx+bw-2),yy+1,'stone2')
    line(x,y,x,y+h-1,'ink'); line(x+w-1,y,x+w-1,y+h-1,'ink')
def slit(x,y,hot=False):
    path(f'M {x} {y+7} L {x} {y+2} L {x+2} {y} L {x+3} {y+2} L {x+3} {y+7} Z','ink')
    line(x+3,y+2,x+3,y+7,'stone3')
    if hot: line(x+1,y+3,x+1,y+6,'fire2'); pix(x+2,y+5,'fire4')
def merlons(x,y,w,base='stone2'):
    rect(x,y+4,w,4,base); line(x,y+7,x+w-1,y+7,'ink')
    for xx in range(x,x+w-2,7):
        rect(xx,y,4,5,base); line(xx,y,xx+3,y,'stonelit'); line(xx,y,xx,y+4,'ink'); line(xx+4,y+1,xx+4,y+4,'ink')
# Rear towers and keep.
masonry(91,150,24,42,'stone1')
poly([(88,149),(102,128),(117,149)],'roof','ink')
poly([(102,129),(116,148),(106,146)],'rooflit')
line(94,145,107,145,'stonehot')
slit(98,156,True); slit(105,172)
masonry(126,143,34,53,'stone2',9,6)
rect(150,143,10,53,'stone1')
for yy in range(149,195,6): line(150,yy,159,yy,'stone0')
poly([(122,143),(142,119),(163,143)],'roof','ink')
poly([(142,120),(161,142),(147,141)],'rooflit')
for yy in [133,138]: line(134-(yy-133),yy,151+(yy-133),yy,'red0')
line(142,114,142,125,'ink')
poly([(143,114),(158,116),(153,120),(143,119)],'red1','ink'); line(144,115,150,116,'red3')
rect(123,143,40,3,'stone0'); line(124,143,161,143,'stonelit')
slit(133,151,True); slit(144,151,True); slit(133,169); slit(144,169,True)
# Stepped wings of the castle.
masonry(62,168,65,31,'stone1')
merlons(62,163,65)
masonry(157,170,42,31,'stone1'); merlons(157,165,42)
# Corner towers.
for tx,ty,tw in [(57,153,23),(180,154,23)]:
    masonry(tx,ty+7,tw,48,'stone2',7,6)
    rect(tx+tw-7,ty+7,6,48,'stone1')
    for yy in range(ty+11,ty+54,6): line(tx+tw-7,yy,tx+tw-2,yy,'stone0')
    rect(tx-2,ty+4,tw+4,5,'stone0'); line(tx-2,ty+4,tx+tw+1,ty+4,'stone3')
    merlons(tx-2,ty-1,tw+4)
    slit(tx+7,ty+15,tx>100); slit(tx+7,ty+34)
    line(tx+1,ty+10,tx+1,ty+52,'stone3')
# Front curtain wall, with the visible top walkway.
poly([(73,182),(181,182),(193,188),(65,188)],'stone3','ink')
masonry(67,190,121,22,'stone1',9,5)
rect(69,190,117,3,'stone0')
line(68,211,187,211,'stone0')
# Gatehouse and arched portcullis.
masonry(118,185,37,29,'stone2',8,5)
path('M 126 213 L 126 200 Q 126 191 136 191 Q 146 191 146 200 L 146 213 Z','ink')
path('M 130 212 L 130 201 Q 130 195 136 195 Q 142 195 142 201 L 142 212 Z','wood0')
for xx in range(130,143,3): line(xx,200,xx,212,'wood2')
for yy in [202,207]: line(128,yy,144,yy,'wood1')
path('M 125 212 L 125 200 Q 125 190 136 190 Q 147 190 147 200 L 147 212','stonelit',None)
# Restore hollow arch after the open path was rendered as a filled shape.
path('M 126 212 L 126 200 Q 126 192 136 192 Q 146 192 146 200 L 146 212','ink',None)
for xx in range(129,145,3): line(xx,200,xx,212,'wood1')
line(129,204,144,204,'wood2')
for xx,yy in [(125,197),(127,193),(131,190),(137,189),(142,191),(146,195)]: rect(xx,yy,2,2,'stone0')
merlons(117,180,39,'stone2'); merlons(66,184,51,'stone2'); merlons(156,184,34,'stone2')
# Buttresses break the flat curtain into strongly outlined facets.
for xx in [77,96,165,181]:
    poly([(xx,192),(xx+4,192),(xx+5,212),(xx+7,216),(xx-2,216),(xx,209)],'stone2','stone0')
    line(xx,193,xx,212,'stone3')
# Uneven stones, mortar losses and old cracks interrupt the masonry grid.
speckle((58,148,201,212),['stone1','stone2'],['stone0','stone2','stone3'],130,True)
for pts in [[(73,175),(70,179),(72,182)],[(108,194),(106,199),(109,202),(107,206)],[(171,174),(174,178),(171,182)],[(148,164),(146,167),(148,170)],[(190,188),(193,193),(191,197)]]:
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]): line(x0,y0,x1,y1,'stone0')
# Firelight is painted only onto exposed stone, preserving cold recessed mortar.
stone_warm={
    c.color(col('stone1')):'#785247',
    c.color(col('stone2')):'#a4755a',
    c.color(col('stone3')):'#d69b6c',
    c.color(col('stonelit')):'#edb87b'
}
stone_dim={
    c.color(col('stone1')):'#59464a',
    c.color(col('stone2')):'#7e6260',
    c.color(col('stone3')):'#aa8270',
    c.color(col('stonelit')):'#cba184'
}
for yy in range(145,204):
    for xx in range(58,204):
        idx=c.get(xx,yy)
        if idx not in stone_warm: continue
        d=min(math.hypot((xx-fx)*1.1,(yy-fy)*.8) for fx,fy in [(100,151),(183,160),(88,181),(156,159)])
        if d<10: pix(xx,yy,stone_warm[idx])
        elif d<19 and (d<16 or (xx+yy)%3): pix(xx,yy,stone_dim[idx])
# Castle banners with torn tails.
for x,y in [(60,171),(151,156),(185,176)]:
    line(x,y-2,x,y+13,'ink')
    poly([(x,y),(x+6,y+1),(x+6,y+12),(x+4,y+10),(x+2,y+13),(x,y+12)],'red1','ink')
    line(x+2,y+2,x+2,y+9,'red3'); pix(x+3,y+4,'gold')
# Fire shapes have dark red outside, serrated tongues, and pale yellow cores.
def flame(x,y,w,h):
    pts=[(x-w//2,y),(x-w//2-2,y-h//3),(x-w//3,y-h//2),(x-w//3-1,y-3*h//4),(x-1,y-h//2),(x+1,y-h),(x+w//4,y-2*h//3),(x+w//4+3,y-h//2),(x+w//2,y-3*h//4),(x+w//2+2,y-h//3),(x+w//2,y)]
    poly(pts,'fire0')
    pts=[(x-w//2+1,y),(x-w//3,y-h//3),(x-w//4,y-2*h//3),(x,y-h//3),(x+2,y-h+4),(x+w//3,y-h//3),(x+w//2,y-h//2),(x+w//2-1,y)]
    poly(pts,'fire2')
    poly([(x-w//3+1,y),(x-w//4,y-h//4),(x,y-h//2),(x+1,y-h//3),(x+3,y-2*h//3),(x+w//3,y-h//4),(x+w//3,y)],'fire3')
    poly([(x-2,y),(x-2,y-h//4),(x+1,y-h//2),(x+2,y-h//4),(x+4,y)],'fire4')
    line(x,y-1,x+1,y-h//5,'fire5')
flame(100,151,17,30); flame(110,153,10,21)
flame(157,161,12,22); flame(180,163,17,33); flame(193,160,11,24)
flame(88,183,8,17)
for x,y in [(102,145),(182,153),(193,152),(155,156)]: line(x-4,y+8,x+5,y+8,'fire3')
# Sparks around the burning towers, kept as discrete pixel clusters.
for _ in range(78):
    xx=random.choice([100,181,191])+random.randint(-14,15); yy=random.randint(115,168)
    if random.random()<.8: pix(xx,yy,random.choice(['fire1','fire2','fire3']))
    if random.random()<.15: pix(xx,yy-1,'fire4')
# The ancient dragon: monumental silhouette and translucent copper wing membranes.
# Far wing, sweeping to the left.
poly([(135,91),(121,62),(105,36),(72,20),(65,22),(60,42),(36,57),(52,56),(68,65),(77,65),(91,80),(105,77),(118,93),(133,100)],'ink','ink')
poly([(130,88),(116,59),(103,39),(72,24),(65,44),(42,55),(56,55),(71,62),(78,61),(92,76),(106,73),(119,89)],'wing1')
poly([(72,27),(104,42),(117,67),(79,57),(67,45)],'wing2')
poly([(80,58),(117,68),(128,87),(106,72),(93,73)],'wing0')
poly([(65,46),(76,58),(70,60),(56,53),(45,54)],'wing3')
poly([(74,28),(103,43),(101,45),(81,36)],'wing3')
line(70,24,65,44,'wing4'); line(65,44,43,55,'wing3')
# Stretched hide has long folds, old scars and sparse scale-like speckling.
poly([(74,28),(99,42),(104,45),(91,40)],'wing3')
poly([(70,38),(98,46),(104,49),(89,46)],'wing1')
poly([(69,44),(92,49),(102,54),(84,50)],'wing3')
line(78,35,87,40,'wing4'); line(89,41,94,44,'wing3')
line(82,43,88,48,'wing0'); line(82,44,87,48,'wing3')
for xx,yy in [(81,40),(85,44),(88,47)]: line(xx,yy,xx-1,yy+2,'wing3')
for xx,yy in [(77,30),(82,34),(89,35),(94,39),(75,42),(77,45),(91,49),(98,53),(87,57),(103,57)]:
    line(xx,yy,xx+1,yy,'wing3')
# Wing fingers and knuckled leading edge.
for pts in [[(134,91),(115,60),(103,38),(70,21),(67,24),(100,41),(112,63),(128,93)],[(105,43),(91,48),(77,61),(77,65),(82,61),(94,51),(108,49)],[(116,63),(108,68),(104,76),(108,78),(112,70),(120,68)]]: poly(pts,'dragon0','ink')
line(72,22,102,38,'dragon3'); line(103,39,116,61,'dragon2'); line(117,65,129,86,'dragon2')
poly([(67,24),(64,17),(70,20),(74,26)],'dragon4','ink')
# Right wing stretches across the sun: long, asymmetrical scalloped fingers.
poly([(139,88),(155,63),(177,38),(219,24),(231,22),(218,34),(207,56),(230,62),(222,64),(211,73),(207,85),(192,82),(180,86),(172,104),(153,99)],'ink','ink')
poly([(145,87),(160,63),(179,41),(225,25),(210,44),(203,56),(221,62),(209,70),(205,81),(192,78),(178,83),(170,99),(155,94)],'wing1')
poly([(181,43),(222,27),(204,54),(175,66),(157,82)],'wing2')
poly([(183,46),(213,31),(200,53),(172,67)],'wing3')
poly([(174,69),(203,58),(218,62),(206,69),(204,78),(191,75)],'wing2')
poly([(169,73),(185,78),(177,82),(169,95),(153,92)],'wing0')
poly([(203,56),(212,61),(204,65),(176,70)],'wing3')
line(182,42,222,27,'wing4'); line(194,51,208,37,'wing4')
# Subtle membrane folds fan away from the wing wrist.
poly([(180,45),(213,30),(208,35),(188,44)],'wing4')
poly([(177,54),(199,45),(204,38),(199,49),(182,57)],'wing1')
line(185,52,190,49,'wing3'); line(180,56,186,53,'wing3')
line(188,57,191,54,'wing0'); line(188,58,191,55,'wing4')
poly([(178,68),(199,60),(204,61),(186,68)],'wing4')
for xx,yy in [(183,48),(188,46),(198,37),(202,34),(182,59),(177,63),(195,63),(200,63),(180,71),(189,70)]:
    line(xx,yy,xx+1,yy,'wing3')
for pts in [[(139,89),(156,60),(177,37),(224,22),(230,22),(180,41),(162,65),(146,94)],[(178,41),(172,60),(175,69),(207,82),(207,86),(171,73),(166,64)],[(174,67),(193,58),(205,54),(209,56),(192,62),(177,72)],[(169,74),(174,84),(172,101),(169,104),(169,86),(164,80)]]: poly(pts,'dragon0','ink')
line(143,86,159,62,'dragon3'); line(159,62,179,39,'dragon3'); line(180,38,221,24,'dragon4')
line(172,44,169,62,'dragon2'); line(172,71,200,81,'dragon2')
poly([(222,24),(233,19),(229,26),(220,30)],'dragon4','ink')
# Small holes and scarred tears through the old membranes.
poly([(194,46),(199,40),(196,49)],'sunhot','wing0')
line(107,58,109,62,'wing3'); line(110,57,112,61,'wing3')
line(190,66,197,68,'wing4'); pix(199,69,'wing4')
# Tail curls upward to counterbalance the head.
path('M 151 101 C 169 103 182 116 201 117 C 217 118 231 107 233 94 L 236 88 C 238 110 221 127 202 127 C 178 127 163 117 150 114 Z','dragon0','ink')
path('M 163 109 C 184 126 215 127 230 109 C 219 125 196 128 179 120 Z','dragon2')
path('M 173 115 Q 206 132 227 113','dragon3',None)
# Thin highlight path is explicitly stroked.
c.path('M 176 118 Q 205 132 226 115',col('dragon3'),fill=False)
poly([(232,97),(232,90),(236,82),(239,92),(236,89),(235,99)],'dragon1','ink')
# Rear legs and hooked talons.
path('M 147 101 Q 162 104 166 116 L 158 127 L 162 130 L 168 128 L 166 133 L 156 134 L 151 129 L 156 117 L 145 113 Z','dragon0','ink')
poly([(158,112),(161,116),(154,126),(154,130),(157,131),(152,131),(151,128)],'dragon2')
poly([(160,131),(164,129),(163,134)],'dragon4','ink')
poly([(166,130),(170,127),(168,133)],'dragon4','ink')
path('M 130 101 L 122 116 L 113 120 L 110 118 L 111 125 L 117 125 L 128 120 L 140 107 Z','dragon0','ink')
line(124,115,117,121,'dragon3'); line(113,122,112,125,'dragon4')
# Muscular body and coiled S-shaped neck.
path('M 101 90 C 109 85 119 92 124 89 C 131 78 141 79 150 86 C 156 91 160 99 158 107 C 150 116 139 115 131 107 C 123 103 115 109 107 105 C 100 102 96 97 96 94 Z','dragon1','ink')
path('M 103 94 Q 111 102 120 98 L 131 93 Q 142 91 152 99 L 153 105 Q 144 111 135 103 Q 126 99 118 105 Q 107 108 100 99 Z','dragon2')
path('M 101 97 Q 112 108 124 101 Q 130 98 135 102 L 145 111 Q 136 110 131 105 Q 121 104 117 107 Q 105 108 100 100 Z','dragon3')
path('M 124 89 Q 136 80 146 87 L 151 94 Q 140 88 131 94 Z','dragon0')
line(130,87,137,84,'dragon3'); line(139,84,145,87,'dragon3')
# Dorsal spikes and warm edges.
for pts in [[(111,92),(109,84),(117,90)],[(120,91),(120,81),(127,86)],[(127,85),(131,75),(135,82)],[(137,83),(142,75),(144,85)],[(148,87),(155,81),(154,94)],[(159,103),(165,97),(167,108)],[(172,111),(179,106),(180,116)],[(187,119),(192,113),(194,121)],[(203,121),(207,116),(209,121)],[(218,118),(219,112),(224,113)]]:
    poly(pts,'dragon3','ink')
    if len(pts)==3: line(pts[0][0],pts[0][1],pts[1][0],pts[1][1],'dragon4')
# Forward arm reaches out over the castle.
path('M 135 97 Q 140 97 139 104 L 131 115 L 121 116 L 117 120 L 115 119 L 118 113 L 127 111 L 130 101 Z','dragon1','ink')
line(134,101,131,109,'dragon3'); line(129,112,122,113,'dragon2')
for x,y in [(116,117),(120,117),(123,116)]: poly([(x,y),(x-2,y+4),(x+1,y+2)],'dragon4','ink')
# Angular horned head, glowing eye, open jaw and pale teeth.
poly([(103,87),(98,82),(89,82),(84,86),(76,87),(74,91),(79,95),(91,96),(97,101),(103,98),(106,92)],'dragon1','ink')
poly([(81,87),(90,84),(98,85),(101,89),(94,90),(88,88)],'dragon3')
poly([(76,90),(85,89),(91,92),(98,93),(94,96),(83,94),(77,93)],'dragon0')
poly([(79,95),(88,97),(95,96),(99,99),(93,102),(84,100)],'dragon2','ink')
line(79,97,89,99,'dragon4')
poly([(95,83),(99,74),(103,71),(101,80),(100,86)],'dragon4','ink')
poly([(88,84),(87,77),(82,73),(90,76),(93,83)],'dragon3','ink')
poly([(103,89),(111,84),(108,92),(105,96)],'dragon2','ink')
line(101,77,102,74,'sun'); line(85,75,89,78,'dragon4')
line(87,88,93,89,'ink'); pix(90,88,'fire3'); pix(91,88,'fire5'); pix(92,88,'fire2')
pix(78,89,'ink'); line(82,94,91,95,'black')
for x,y in [(82,94),(87,95),(92,95)]: line(x,y,x+1,y+2,'armor3')
poly([(98,101),(100,107),(103,99)],'dragon3','ink')
# Deliberate scale clusters, belly rings and facial scars.
for x,y in [(105,94),(110,97),(116,98),(121,96),(126,93),(135,90),(140,89),(146,93),(148,97),(142,97),(137,94),(136,108),(145,108),(155,103),(164,111),(183,120),(198,124),(216,119)]:
    line(x,y,x+2,y,'dragon3'); pix(x+1,y+1,'dragon0')
for x,y in [(104,100),(109,103),(114,104),(119,104),(124,102)]: line(x,y,x-1,y+2,'dragon0')
line(96,86,98,89,'dragon0'); pix(98,90,'dragon4')
# A jet of dragon fire hits the left keep. The taper and gaps keep the face readable.
path('M 79 98 Q 74 107 80 117 Q 86 126 94 140 L 105 146 L 96 126 Q 86 114 83 106 L 82 100 Z','fire0')
poly([(79,99),(78,107),(81,116),(87,124),(94,139),(103,145),(98,133),(94,124),(85,113),(82,102)],'fire2')
poly([(80,100),(80,109),(84,115),(88,118),(94,130),(98,135),(94,124),(86,113),(82,102)],'fire3')
poly([(81,103),(82,112),(87,116),(91,122),(88,114),(84,110)],'fire5')
for x,y in [(75,108),(77,119),(83,125),(88,133),(91,119),(95,127),(72,116)]: pix(x,y,'fire3')
# Knights on the ramparts: helmet glints, kite shields and upright spears.
def knight(x,y,scale=1,facing=1,flag=False):
    # y is the soles of the boots.
    s=scale
    line(x-s,y-3*s,x-s,y,'ink'); line(x+s,y-3*s,x+2*s,y,'ink')
    rect(x-s,y-7*s,3*s,4*s,'armor0'); line(x-s,y-7*s,x-s,y-4*s,'armor1')
    rect(x-s,y-10*s,3*s,3*s,'ink'); rect(x-s,y-10*s,2*s,s,'armor2')
    pix(x+s,y-9*s,'armor1'); line(x-s,y-8*s,x+s,y-8*s,'black')
    line(x+2*s,y-6*s,x+4*s,y-7*s,'armor1')
    line(x+4*s,y-3*s,x+4*s,y-17*s,'wood2')
    poly([(x+4*s,y-20*s),(x+3*s,y-16*s),(x+5*s,y-16*s)],'armor2','ink')
    poly([(x-3*s,y-6*s),(x,y-7*s),(x+s,y-3*s),(x-s,y-s),(x-3*s,y-3*s)],'red1','ink')
    line(x-2*s,y-5*s,x-1*s,y-2*s,'gold')
    if flag:
        poly([(x+4*s,y-16*s),(x+11*s,y-14*s),(x+8*s,y-11*s),(x+4*s,y-12*s)],'red1','ink')
        line(x+5*s,y-15*s,x+8*s,y-14*s,'red3')
for x,y in [(64,155),(75,155),(98,165),(114,165),(166,168),(190,156),(76,186),(96,186),(111,186),(163,186),(179,186),(131,182),(146,182)]: knight(x,y)
# Several archers have bows instead of another vertical spear.
for x,y in [(86,165),(174,169)]:
    rect(x,y-7,3,5,'armor0'); rect(x,y-10,3,3,'ink'); line(x,y-10,x+2,y-10,'armor2')
    line(x+2,y-6,x+5,y-6,'armor2')
    c.path(f'M {x+5} {y-11} Q {x+10} {y-6} {x+5} {y-2}',col('wood3'),fill=False)
    line(x+5,y-11,x+5,y-2,'rope')
# Wooden siege towers on both flanks, all beams silhouetted and brass-lit.
def siege_tower(x,y,w,h,right=False):
    # square tower receding to the right, y is ground level.
    top=y-h
    poly([(x,top+5),(x+w-5,top),(x+w,top+5),(x+w-1,y-6),(x+3,y-4)],'wood0','ink')
    poly([(x+3,top+6),(x+w-7,top+4),(x+w-6,y-8),(x+5,y-7)],'wood1')
    poly([(x+w-6,top+4),(x+w-1,top+7),(x+w-2,y-8),(x+w-6,y-7)],'wood0','ink')
    for yy in range(top+9,y-8,4): line(x+4,yy,x+w-7,yy-1,'wood2')
    for xx in [x+2,x+w-8]:
        line(xx,top+5,xx+2,y-6,'ink'); line(xx+1,top+5,xx+3,y-8,'wood3')
    for yy in range(top+12,y-7,15):
        rect(x,yy,w-4,3,'ink'); line(x+1,yy,x+w-5,yy,'wood2')
        line(x+4,yy+3,x+w-9,min(y-8,yy+13),'wood3'); line(x+4,min(y-8,yy+13),x+w-9,yy+3,'wood0')
        for xx in [x+2,x+w-8]: pix(xx,yy+1,'armor1')
    rect(x-2,top+2,w+2,4,'wood0'); line(x-2,top+2,x+w-1,top+2,'wood3')
    for xx in range(x-2,x+w,6):
        rect(xx,top-3,4,5,'wood1'); line(xx,top-3,xx+3,top-3,'wood3'); line(xx,top-3,xx,top+1,'ink')
    # dark arrow slits
    rect(x+7,top+8,3,5,'black'); rect(x+7,top+23,3,4,'black')
    for xx in [x+4,x+w-5]:
        ellipse(xx,y-3,4,5,'ink'); ellipse(xx,y-3,2,3,'wood2'); pix(xx,y-3,'armor1')
    line(x-1,y-9,x+w,y-9,'wood3')
    if right:
        poly([(x+1,top+3),(x-21,top+15),(x-20,top+19),(x+2,top+7)],'wood1','ink')
        line(x,top+3,x-21,top+15,'wood3'); line(x-20,top+15,x-1,top-4,'rope')
        for t in range(1,20,4): line(x-t,top+4+t//2,x-t+1,top+7+t//2,'wood0')
    else:
        line(x+w-2,top+4,x+w+12,top+14,'wood3'); line(x+w-3,top-2,x+w+12,top+14,'rope')
    knight(x+8,top+2)
    line(x+w-4,top-2,x+w-4,top-19,'ink')
    poly([(x+w-4,top-19),(x+w+7,top-17),(x+w+3,top-14),(x+w+7,top-12),(x+w-4,top-13)],'red0','ink')
    line(x+w-3,top-18,x+w+3,top-17,'red2')
siege_tower(17,232,26,49)
siege_tower(222,224,24,58,True)
# Ladders reach the battered left wall.
for off in [0,4]: line(47+off,218,60+off,175,'wood3')
for t in range(1,12):
    yy=218-t*3; xx=47+int(t*.92); line(xx,yy,xx+4,yy,'wood1')
knight(53,198)
# Stones, fallen equipment and advancing troop blocks.
for _ in range(65):
    x=random.randint(0,255); y=random.randint(216,254)
    if c.get(x,y) in [c.color(col('land')),c.color(col('earthlit')),c.color(col('landlit'))]:
        line(x,y,min(255,x+2),y,'rock'); pix(x,y-1,'rocklit')
# Distant formations in orderly ranks on either side of the road.
def infantry(x,y,kind=0):
    line(x,y-2,x-1,y,'ink'); line(x+1,y-2,x+2,y,'ink')
    rect(x-1,y-6,3,5,'deep'); rect(x-1,y-8,3,2,'ink')
    pix(x,y-8,'armor1'); pix(x-1,y-5,'armor1')
    poly([(x+1,y-5),(x+4,y-5),(x+4,y-2),(x+2,y)],'red0' if kind else 'armor0','ink')
    pix(x+2,y-4,'wood3' if kind else 'armor1')
    line(x-3,y-1,x-1,y-14,'ink'); pix(x-1,y-15,'armor2')
for row in range(3):
    yy=216+row*9
    for xx in range(4,16,7): infantry(xx+row%2*3,yy,1)
    for xx in range(63,117,8): infantry(xx+(row%2)*3,yy,1)
    for xx in range(168,214,8): infantry(xx+(row%2)*3,yy,0)
# Midground pennants mark the two formations.
for x,y in [(72,224),(199,222)]:
    line(x,y,x,y-30,'ink')
    poly([(x,y-29),(x+11,y-27),(x+8,y-23),(x+12,y-20),(x,y-21)],'red1','ink')
    line(x+2,y-27,x+2,y-23,'red3'); line(x+2,y-23,x+7,y-23,'gold')
# Foreground ridge and larger, readable soldiers.
poly([(0,244),(12,239),(24,244),(35,237),(47,242),(60,239),(72,246),(86,241),(100,245),(113,247),(126,251),(154,250),(167,244),(182,246),(198,239),(216,243),(235,237),(255,240),(255,255),(0,255)],'black')
for x,y in [(16,250),(37,246),(59,254),(84,253),(180,253),(207,249),(236,249)]: knight(x,y,scale=1,flag=(x==37))
# Two foreground champions are larger than the ranked army.
knight(49,255,scale=2,flag=False)
knight(224,255,scale=2,flag=True)
# A broken wagon wheel and discarded blade along the central approach.
ellipse(108,242,5,4,'ink'); ellipse(108,242,3,2,'earthlit')
line(104,241,112,244,'wood0'); line(106,246,110,239,'wood0')
line(150,240,157,234,'armor1'); line(149,237,153,241,'ink'); line(148,242,150,240,'wood2')
# Arrows traverse the negative space in groups, with distinct fletchings and heads.
def arrow(x,y,dx,dy):
    line(x,y,x+dx,y+dy,'ink')
    ex=x+dx; ey=y+dy
    if dx>0:
        line(ex-2,ey,ex,ey,'armor3'); pix(ex-1,ey-1,'armor1')
        line(x,y,x-2,y-2,'ink'); line(x+2,y,x,y-2,'ink')
    else:
        pix(ex,ey,'armor2'); pix(ex+1,ey-1,'armor1')
        line(x,y,x+2,y+2,'ink'); line(x-2,y,x,y+2,'ink')
for a in [(17,119,10,-5),(30,135,12,-7),(42,114,8,-4),(18,147,10,-6),(220,133,-10,-5),(239,120,-11,-6),(244,146,-12,-4),(207,141,-8,-4),(36,90,9,-2),(153,39,-9,-3)]: arrow(*a)
# Last hot embers close to the viewer, with a handful of warm streaks.
for x,y in [(10,206),(46,175),(119,144),(164,132),(212,181),(215,214),(151,228),(116,230),(31,161),(14,224),(203,200),(91,234),(234,189),(5,237)]:
    pix(x,y,'fire2');
    if x%3==0: pix(x,y-1,'fire4')
for x,y in [(51,157),(212,153),(11,185),(115,133)]: line(x,y,x+1,y-2,'fire2')
# Pixel debris gives the foreground a tactile final edge.
for x,y in [(6,252),(29,254),(68,251),(96,254),(173,253),(193,252),(246,251)]:
    line(x,y,x+3,y,'earthlit'); pix(x+1,y-1,'rock')
assert result.stats()['size'] == (256,256) or result.stats()['size'] == [256,256]
assert result.stats()['colors_used'] <= 140
print(result.stats_text())
view(result, scale=3, margin=0)
save('ancient-dragon-battle', result)
finish(result)
