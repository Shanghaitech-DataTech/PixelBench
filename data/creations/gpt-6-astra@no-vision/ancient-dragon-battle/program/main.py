import random, math
random.seed(21)
c = new_canvas(256,256,background='#211e35',name='ancient-dragon-battle')
# A compact, deliberately shared palette.
ink='#151a25'; deep='#252538'; violet='#393047'; cloud='#55364b'; smoke='#453b49'; smokehi='#62505a'
sky0='#49334f'; sky1='#714052'; sky2='#a55058'; sky3='#c66a5b'; sky4='#e58a61'; sky5='#f5ac70'; sun='#ffd591'
stone0='#30333f'; stone1='#45434c'; stone2='#5d5357'; stone3='#7a6563'; stone4='#a27c6b'; edge='#c39878'
red0='#542b38'; red1='#833b40'; red2='#ad5147'; red3='#d57954'
steel0='#34434d'; steel1='#627c82'; steel2='#a6b9ac'; pale='#e7d4a1'
fire0='#b14439'; fire1='#e36b36'; fire2='#ffa943'; fire3='#ffe19a'
# Sunset bands, broken by long cloud banks.
for y0,y1,col in [(0,32,sky0),(32,57,sky1),(57,83,sky2),(83,110,sky3),(110,139,sky4),(139,166,sky5)]: c.rect(0,y0,256,y1-y0,col)
c.circle(185,104,37,sun)
c.rect(148,111,74,2,sky5); c.rect(153,123,65,2,sky4)
def P(points,fill,outline=ink):
    c.poly(points,fill)
    if outline: c.poly(points,outline,fill=False)
def cloudbank(x,y,w,col):
    c.poly([(x,y+4),(x+8,y+4),(x+13,y),(x+w//3,y),(x+w//3+6,y-3),(x+w//2,y-3),(x+w//2+8,y+1),(x+w-9,y+1),(x+w,y+5),(x+w-8,y+7),(x+3,y+7)],col)
for a in [(-13,17,84,violet),(93,12,73,violet),(198,30,69,cloud),(-20,52,87,cloud),(10,77,75,sky1),(191,67,73,sky2),(104,42,42,sky1),(15,112,57,sky3)]: cloudbank(*a)
for x,y,w in [(1,45,26),(24,46,34),(171,19,38),(217,49,31),(87,55,18),(2,99,21)]: c.line(x,y,x+w,y,sky3)
# Craggy distant mountain layers.
P([(0,129),(13,119),(26,123),(45,93),(55,108),(63,104),(80,132),(96,120),(112,136),(137,111),(147,120),(160,105),(177,121),(194,115),(211,91),(221,108),(233,101),(255,125),(255,179),(0,179)],'#895e66',None)
for pts in [[(28,122),(45,93),(55,108),(48,104),(45,111),(41,110)],[(194,115),(211,91),(221,108),(212,102),(208,108)],[(143,120),(160,105),(177,121),(162,113),(158,117)]]: P(pts,'#bd8074',None)
P([(0,150),(20,136),(34,144),(55,126),(70,143),(88,137),(110,153),(131,136),(151,150),(179,135),(197,147),(221,128),(239,138),(255,131),(255,191),(0,191)],'#5c4e5d',None)
P([(0,170),(30,157),(56,163),(93,153),(120,163),(150,157),(183,169),(216,152),(255,163),(255,217),(0,217)],'#42414e',None)
# Smoke columns travel left in the wind, behind the architecture.
def smokeplume(x,y,scale):
    for i in range(12):
        xx=x-int(i*1.8*scale)+random.randint(-3,3); yy=y-int(i*5*scale)
        rr=int((5+i*.65)*scale)
        c.circle(xx,yy,rr,cloud if i>7 else smoke)
        if i<9: c.circle(xx-2,yy-2,max(2,rr-3),smokehi)
    for i in range(4): c.rect(x-int((i+8)*1.8*scale)-14,y-int((i+8)*5*scale),13,2,cloud)
smokeplume(96,150,.88); smokeplume(182,136,1.12); smokeplume(218,183,.7)
# Fire is made from angular tongues, avoiding smooth vector edges.
def flame(x,y,h,w):
    P([(x-w,y),(x-w-2,y-h//3),(x-w//2,y-h//2),(x-w//2-1,y-h),(x+2,y-h*2//3),(x+w//2,y-h*4//5),(x+w//2,y-h//3),(x+w+2,y-h//2),(x+w,y)],fire0,None)
    P([(x-w+2,y),(x-w//2,y-h//3),(x-1,y-h*4//5),(x+2,y-h//2),(x+w//2,y-h//3),(x+w-1,y)],fire1,None)
    P([(x-w//2,y),(x-1,y-h//2),(x+2,y-h//3),(x+w//2,y)],fire2,None)
    P([(x-2,y),(x,y-h//4),(x+3,y)],fire3,None)
# Distant buildings and ruined roofs.
for x,y,w,h in [(36,168,20,34),(204,167,22,38),(89,156,22,43),(140,150,25,46)]:
    c.rect(x,y,w,h,stone0); P([(x-3,y),(x+w//2,y-15),(x+w+3,y)],red0)
    c.rect(x+5,y+8,3,8,fire2)
for x,y,h,w in [(86,158,37,7),(102,158,26,6),(151,152,30,6),(185,138,42,10),(204,178,28,6)]: flame(x,y,h,w)
# Castle masonry, with staggered joints and sparse chips.
def masonry(x,y,w,h,base,lit=False):
    c.rect(x,y,w,h,base)
    for yy in range(y+5,y+h,6):
        c.line(x,yy,x+w-1,yy,stone0)
        for xx in range(x-5+((yy-y)//6%2)*6,x+w,12):
            if x<xx<x+w: c.line(xx,yy-5,xx,yy-1,stone0)
        if lit:
            for xx in range(x+2,x+w-3,13): c.line(xx,yy-4,xx+5,yy-4,stone3)
    for _ in range(w*h//100):
        xx=random.randrange(x+1,x+w-1); yy=random.randrange(y+1,y+h-1)
        c.line(xx,yy,min(xx+random.randint(1,3),x+w-1),yy,stone3 if lit else stone2)
    c.rect(x,y,w,h,ink,fill=False)
def merlons(x,y,w,col):
    c.rect(x,y+6,w,5,col); c.line(x,y+10,x+w-1,y+10,ink)
    for xx in range(x,x+w-3,9):
        c.rect(xx,y,6,8,ink); c.rect(xx+1,y+1,4,6,col); c.line(xx+1,y+1,xx+4,y+1,edge)
def window(x,y,w=5,h=12,glow=False):
    P([(x,y+h),(x,y+3),(x+w//2,y),(x+w,y+3),(x+w,y+h)],ink)
    c.line(x+w+1,y+4,x+w+1,y+h,stone3)
    if glow:
        c.rect(x+1,y+4,w-1,h-4,fire1); c.line(x+w//2,y+3,x+w//2,y+h-1,fire3)
        c.line(x,y+h//2+1,x+w,y+h//2+1,stone0)
# Tall back keep.
masonry(104,132,52,68,stone2,True)
P([(101,133),(101,126),(114,126),(114,121),(128,121),(128,125),(142,125),(145,129),(159,129),(159,135)],stone3)
merlons(103,123,54,stone3)
for x in [112,127,143]: window(x,143,5,15,x==143)
c.line(108,163,152,163,edge); c.line(106,166,154,166,ink)
# Towers framing the keep.
def tower(x,y,w,h,hot=False):
    masonry(x,y,w,h,stone2,True)
    c.rect(x+1,y+1,5,h-2,stone1); c.rect(x+w-6,y+2,5,h-3,stone3)
    c.line(x+w-2,y+4,x+w-2,y+h-1,stone4)
    for yy in range(y+18,y+h-6,22):
        c.rect(x-2,yy,w+4,3,ink); c.line(x-1,yy,x+w,yy,stone3)
    c.rect(x-3,y-2,w+6,8,ink); c.rect(x-2,y-2,w+4,5,stone3)
    for xx in range(x,x+w,7): c.rect(xx,y+5,3,4,stone0)
    merlons(x-3,y-10,w+6,stone3)
    window(x+w//2-3,y+13,6,14,hot)
    window(x+w//2-2,y+42,4,11,False)
tower(63,125,28,85,True)
tower(170,119,29,92,True)
# Red pennants and finials on the stone towers.
for x,y,d in [(69,98,1),(180,90,-1),(125,106,1)]:
    c.line(x,y,x,y+26,ink); c.set(x,y-1,pale)
    P([(x+1,y+1),(x+15*d,y+4),(x+11*d,y+8),(x+18*d,y+12),(x+1,y+10)],red1)
    c.line(x+2*d,y+3,x+10*d,y+5,red3)
# Long curtain wall and open gateway.
masonry(49,179,161,43,stone1)
c.rect(50,184,159,3,stone2); c.line(51,184,208,184,stone4)
for x in [52,82,103,152,178,201]:
    P([(x,187),(x+5,187),(x+8,220),(x-2,220)],stone0)
    c.line(x+1,188,x+2,218,stone3)
P([(116,221),(116,199),(119,192),(126,188),(133,188),(140,192),(143,200),(143,221)],stone3)
P([(120,222),(120,201),(123,195),(130,192),(137,196),(139,202),(139,222)],ink)
c.line(123,199,123,216,red0); c.line(136,199,136,218,red0)
for xx in range(123,139,4): c.line(xx,198,xx,207,stone2)
c.line(122,202,137,202,stone2); c.line(122,206,137,206,stone2)
c.rect(46,175,167,7,ink); c.rect(47,175,165,4,stone3)
merlons(47,169,166,stone2)
# A fracture and fallen masonry.
c.line(96,185,92,192,ink); c.line(92,192,97,198,ink); c.line(97,198,93,207,ink)
for xx,yy in [(60,220),(69,226),(101,223),(188,222),(202,225)]: P([(xx,yy),(xx+2,yy-3),(xx+7,yy-2),(xx+8,yy+2),(xx,yy+2)],stone2)
# Rampart defenders: helmets, tunics, kite shields, spears.
def knight(x,y,side=1):
    c.line(x+side*5,y-13,x+side*5,y+7,'#9b7d63')
    P([(x+side*5,y-17),(x+side*5-2,y-12),(x+side*5+1,y-12)],steel2)
    c.rect(x-2,y+2,5,7,ink); c.rect(x-2,y+2,4,5,steel0)
    c.line(x-1,y+8,x-2,y+11,ink); c.line(x+2,y+8,x+2,y+11,ink)
    c.rect(x-3,y-4,6,6,ink); c.rect(x-2,y-4,4,4,steel1)
    c.line(x-2,y-4,x+1,y-4,steel2); c.line(x-1,y-1,x+2,y-1,ink)
    c.set(x+2,y-2,steel2); c.line(x+2,y+3,x+side*5,y+2,steel1)
    P([(x-4,y+3),(x,y+2),(x+1,y+7),(x-2,y+10),(x-5,y+7)],red0)
    c.line(x-3,y+4,x-2,y+8,pale); c.line(x-4,y+5,x-1,y+5,pale)
for x,y,s in [(58,162,1),(76,161,1),(100,162,-1),(118,161,1),(148,162,1),(165,161,-1),(192,162,1),(72,112,-1),(184,106,1),(135,117,1)]: knight(x,y,s)
# Flames in front of stonework, concentrated on the breached right tower.
for args in [(193,126,25,5),(176,128,24,5),(91,181,21,5),(159,177,29,5),(206,205,27,7)]: flame(*args)
c.line(172,133,170,145,fire1); c.line(197,139,197,161,fire1)
# Ground plane, approach road and a dark foreground lip.
P([(0,213),(25,207),(51,216),(77,213),(107,221),(133,217),(167,216),(200,218),(230,205),(255,215),(255,255),(0,255)],'#35343c',None)
P([(118,221),(140,221),(171,255),(87,255)],'#64514c',None)
for i in range(170):
    x=random.randrange(256); y=random.randrange(218,256)
    col=random.choice([stone0,stone1,'#514349'])
    c.line(x,y,min(255,x+random.randrange(1,5)),y,col)
# Siege towers: tall, angular timber frames with diagonal braces.
def siege(x,y,w,h):
    wood0='#332b31'; wood1='#60443d'; wood2='#94664c'
    # Back wheels first.
    for xx in [x+4,x+w-4]:
        c.circle(xx,y+h,6,ink); c.circle(xx,y+h,4,wood1); c.circle(xx,y+h,1,ink)
        c.line(xx-3,y+h,xx+3,y+h,wood2); c.line(xx,y+h-3,xx,y+h+3,wood2)
    P([(x-2,y+h-2),(x+4,y),(x+w-6,y),(x+w+3,y+h-2)],wood0)
    for yy in range(y+8,y+h-6,7): c.line(x+2,yy,x+w-1,yy,wood1)
    for xx in [x+4,x+w-6]:
        c.line(xx,y,xx-4 if xx<x+w//2 else xx+6,y+h-2,ink)
        c.line(xx+1,y,xx-3 if xx<x+w//2 else xx+7,y+h-2,wood2)
    for yy in [y+14,y+34,y+54]:
        if yy<y+h-3:
            c.rect(x,yy,w,4,ink); c.line(x,yy,x+w-1,yy,wood2)
            c.line(x+3,yy+4,x+w-5,min(yy+20,y+h-3),wood2)
            c.line(x+w-5,yy+4,x+3,min(yy+20,y+h-3),wood1)
    c.rect(x-4,y-4,w+7,14,ink); c.rect(x-3,y-3,w+5,11,wood1)
    for xx in range(x-2,x+w+2,5):
        c.line(xx,y-3,xx,y+7,wood0); c.set(xx+1,y-2,wood2)
    c.rect(x-5,y-7,w+9,4,ink); c.line(x-4,y-7,x+w+3,y-7,wood2)
    for xx in range(x-3,x+w+1,8): c.rect(xx,y-11,5,5,wood0); c.line(xx,y-11,xx+4,y-11,wood2)
    c.rect(x+w//2-2,y,4,5,ink)
    for yy in [y+20,y+40]:
        if yy<y+h-8: c.rect(x+w//2-2,yy,4,7,ink)
    # Hanging siege banner.
    P([(x+4,y+12),(x+12,y+12),(x+12,y+30),(x+8,y+27),(x+4,y+30)],red0)
    c.line(x+8,y+15,x+8,y+23,red3)
siege(12,161,26,64); siege(225,166,23,57)
# Raised assault gangway.
P([(35,169),(58,174),(58,179),(35,174)],'#60443d')
for xx in range(39,58,5): c.line(xx,170,xx,176,ink)
c.line(36,165,59,171,ink)
# Distant disciplined ranks; helmets pick up the setting sun.
def soldier(x,y,large=False):
    if not large:
        c.line(x+4,y-9,x+4,y+6,'#9b7d63'); c.line(x+4,y-11,x+3,y-8,steel2)
        c.rect(x-2,y-2,5,4,ink); c.line(x-1,y-2,x+1,y-2,steel1); c.set(x+2,y-1,steel2)
        c.rect(x-2,y+2,4,5,steel0); c.line(x-1,y+6,x-2,y+9,ink); c.line(x+1,y+6,x+2,y+9,ink)
        P([(x-4,y+2),(x,y+2),(x,y+7),(x-2,y+9),(x-4,y+7)],'#4c5054'); c.line(x-3,y+3,x-3,y+6,steel1)
    else:
        c.line(x+7,y-18,x+5,y+10,ink); c.line(x+8,y-18,x+6,y+10,'#9b7d63')
        P([(x+8,y-23),(x+5,y-17),(x+9,y-17)],steel2)
        c.rect(x-3,y-5,7,6,ink); c.rect(x-2,y-5,5,4,steel0); c.line(x-2,y-5,x+1,y-5,steel2); c.rect(x+1,y-3,3,2,ink)
        c.rect(x-3,y+1,7,8,ink); c.rect(x-2,y+1,4,6,steel0); c.line(x+3,y+3,x+6,y+2,steel1)
        c.line(x-1,y+8,x-2,y+13,ink); c.line(x+2,y+8,x+3,y+13,ink)
        P([(x-6,y+2),(x,y+1),(x+1,y+8),(x-3,y+12),(x-7,y+8)],ink)
        P([(x-5,y+3),(x-1,y+2),(x,y+8),(x-3,y+10),(x-6,y+7)],red0,None)
        c.line(x-3,y+3,x-3,y+8,red3); c.line(x-5,y+5,x-1,y+5,red3)
for y,xs in [(218,range(49,107,10)),(226,range(44,104,11)),(233,range(39,102,12)),(218,range(159,211,10)),(227,range(166,218,11)),(235,range(174,224,12))]:
    for x in xs: soldier(x,y)
for x,y in [(18,240),(36,246),(60,244),(83,250),(182,248),(207,246),(234,241)]: soldier(x,y,True)
# Standards amongst the armies.
for x,y,flip in [(47,209,1),(215,207,-1)]:
    c.line(x,y-14,x,y+33,ink); c.set(x,y-15,pale)
    P([(x+flip,y-12),(x+flip*13,y-10),(x+flip*12,y+8),(x+flip*6,y+4),(x+flip,y+6)],red0)
    c.line(x+flip*3,y-9,x+flip*3,y+3,red2)
    c.line(x+flip*5,y-3,x+flip*10,y-3,pale); c.line(x+flip*7,y-6,x+flip*7,y+1,pale)
# The ancient dragon. Long curling tail beneath the huge wings.
body0='#23343b'; body1='#365151'; body2='#557165'; body3='#8e9572'
d='M 139 80 C 124 85 121 99 103 106 C 85 116 64 113 64 103 C 64 96 72 94 77 97 C 68 97 69 104 74 105 C 89 109 107 94 117 84 L 129 73 Z'
c.path(d,body1); c.path(d,ink,False)
c.path('M 69 106 C 84 115 109 96 120 89',body2,False)
# Far wing, its rim a series of deliberate stepped points.
P([(137,72),(153,43),(180,22),(218,15),(207,31),(212,45),(222,59),(206,55),(195,61),(190,75),(180,67),(165,68),(154,82)],red0)
P([(143,69),(158,44),(180,27),(212,18),(197,41),(181,49),(165,62)],red1,None)
P([(154,74),(180,52),(198,43),(208,51),(196,53),(187,68),(177,62),(165,64)],red2,None)
for a,b in [((140,74),(180,26)),((140,74),(211,19)),((140,74),(199,42)),((140,74),(188,70))]: c.line(*a,*b,ink)
c.line(155,47,180,26,red3); c.line(180,26,212,17,red3)
# Near wing rises above the whole composition, with five ragged scallops.
P([(127,79),(112,48),(99,29),(70,12),(74,30),(63,49),(43,65),(27,73),(47,73),(57,81),(61,93),(73,85),(83,89),(88,102),(100,91),(110,93),(119,86),(131,87)],red0)
P([(122,78),(108,49),(98,34),(74,17),(80,35),(72,52),(56,67),(46,70),(60,72),(67,84),(77,77),(89,86),(97,78),(109,85)],red1,None)
P([(79,36),(98,35),(111,54),(121,77),(98,61),(73,55)],red2,None)
P([(75,55),(97,62),(121,79),(88,74),(68,68),(51,69)],'#994b45',None)
P([(97,65),(120,81),(100,86),(91,80),(79,78)],red2,None)
# Strong arm and fingers inside the wing.
P([(128,84),(118,72),(105,48),(96,33),(72,14),(73,20),(92,38),(100,56),(115,82),(124,90)],body0)
c.line(75,19,95,36,body3); c.line(95,36,106,56,body2); c.line(107,58,120,80,body2)
for pts in [[(96,35),(85,53),(62,68),(31,72)],[(103,53),(91,66),(68,78),(62,90)],[(113,72),(97,76),(88,98)],[(121,80),(105,85),(100,90)]]:
    for a,b in zip(pts,pts[1:]): c.line(*a,*b,ink)
    for a,b in zip(pts[:2],pts[1:2]): c.line(a[0]+1,a[1],b[0]+1,b[1],red3)
# Rips and weathering on old membranes.
for pts in [[(48,72),(53,67),(51,73)],[(74,86),(77,81),(80,88)],[(99,89),(101,84),(104,89)],[(207,52),(203,46),(209,50)]]: P(pts,ink,None)
for x,y in [(83,43),(86,46),(92,54),(72,61),(106,69),(170,43),(185,37),(185,58)]: c.line(x,y,x+2,y+1,red3)
# Powerful trunk and arched neck.
P([(116,81),(124,72),(138,72),(151,78),(163,77),(168,66),(178,59),(187,60),(191,67),(183,74),(180,85),(170,94),(154,99),(140,94),(130,90),(122,92)],body0)
P([(121,79),(136,76),(153,83),(166,83),(173,69),(180,64),(185,64),(178,75),(177,85),(166,91),(151,91),(137,85),(126,84)],body1,None)
P([(141,87),(153,91),(167,91),(177,83),(174,90),(167,95),(153,96)],body3,None)
c.line(154,96,163,96,pale)
for x,y in [(144,89),(150,91),(157,92),(164,91),(170,88)]: c.line(x,y,x+1,y+4,body0)
# Hind legs and talons curl back under its body.
P([(138,89),(139,99),(130,104),(124,102),(125,110),(120,113),(117,109),(119,100),(128,94),(127,88)],body0)
c.line(132,96,124,103,body2); c.line(121,103,121,109,body2)
P([(156,94),(157,102),(151,108),(143,108),(139,114),(137,110),(139,105),(147,102),(148,95)],body0)
c.line(151,99,150,103,body2); c.line(143,106,140,110,body2)
for x,y in [(117,110),(121,112),(125,109),(137,111),(141,112),(145,108)]: c.line(x,y,x-2,y+3,pale)
# Outstretched forearm.
P([(170,86),(180,88),(186,81),(190,81),(188,87),(181,93),(172,91)],body1)
for x,y in [(187,82),(189,83),(187,86)]: c.line(x,y,x+4,y-2,pale)
# Horned crocodilian head, sharp silhouette and glowing eye.
P([(175,62),(176,57),(184,55),(190,59),(195,61),(204,62),(206,67),(201,70),(190,70),(187,74),(178,70)],body0)
P([(180,59),(185,58),(192,63),(202,64),(202,66),(190,66),(184,64),(179,65)],body2,None)
c.line(188,69,201,68,ink); c.line(189,70,200,70,red1)
c.set(201,64,ink); c.line(185,62,189,62,ink); c.line(186,63,189,63,fire2); c.set(188,63,fire3)
P([(179,59),(174,53),(172,44),(178,50),(184,56)],pale)
P([(185,57),(186,50),(194,45),(191,52),(190,59)],body3)
c.line(187,54,193,47,pale)
for x,y in [(191,69),(195,69),(199,68)]: c.line(x,y,x,y+2,pale)
# Dorsal spikes, old scars and little clusters of armour scales.
for x,y,s in [(120,75,5),(128,72,6),(136,73,5),(145,76,5),(157,77,4),(164,74,5),(167,68,5),(171,63,5)]:
    P([(x-2,y),(x-3,y-s),(x+3,y+1)],body3)
for x,y in [(124,80),(131,80),(136,82),(143,84),(150,85),(156,87),(163,86),(171,79),(176,72)]:
    c.line(x,y,x+2,y,body2); c.set(x+1,y+1,body0)
c.line(134,79,137,84,pale); c.line(137,80,140,85,body2)
# Dragonfire pours diagonally onto the right battlement.
P([(204,68),(213,75),(215,81),(223,90),(220,92),(227,103),(223,102),(230,116),(226,124),(217,129),(205,126),(201,117),(205,110),(205,101),(209,106),(208,93),(211,97),(207,81)],fire0,None)
P([(204,69),(211,78),(212,87),(218,96),(217,104),(223,113),(220,123),(212,124),(207,117),(211,109),(210,97),(209,85)],fire1,None)
P([(204,69),(209,78),(210,89),(215,100),(214,110),(219,117),(216,123),(211,119),(213,111),(211,101),(208,91)],fire2,None)
c.path('M 205 70 L 208 80 L 209 92 L 213 105 L 212 112 L 215 118',fire3,False)
flame(215,133,19,10)
# Arrows crossing open sky and castle approaches, with fletching.
def arrow(x,y,dx,dy):
    c.line(x,y,x+dx,y+dy,ink)
    c.set(x+dx,y+dy,pale)
    c.line(x+1,y-1,x+3,y,steel2); c.line(x,y+2,x+2,y+2,ink)
for a in [(19,112,11,-7),(34,136,9,-9),(50,105,11,-5),(109,116,8,-9),(232,144,-8,-10),(219,154,-8,-7),(25,91,9,-4),(145,111,8,-9),(8,145,11,-6)]: arrow(*a)
# Flying cinders are clustered near the burning stone and trail in the wind.
for i in range(100):
    x=random.randrange(68,233); y=random.randrange(80,215)
    if (x>159 or 80<x<105) and random.random()<.7:
        existing=c.get(x,y)
        if existing in [c.color(k) for k in [smoke,smokehi,cloud,sky2,sky3,sky4,stone0,stone1]]:
            c.set(x,y,fire1 if i%3 else fire2)
            if i%7==0: c.set(x,y+1,fire0)
# Foreground spear tips and debris anchor the cropped battlefield.
for x,y in [(6,249),(106,251),(156,253),(248,249)]:
    c.line(x,y,x+4,y-27,ink); P([(x+4,y-32),(x+1,y-25),(x+5,y-25)],steel1)
for x,y in [(8,232),(113,238),(148,230),(229,251)]:
    c.line(x,y,x+8,y+3,ink); c.line(x+2,y,x+7,y+1,stone2)
print(c.stats_text())
print(c.matrix_text(region=(174,54,206,75)))
save('ancient-dragon-battle',c)
finish(c)
