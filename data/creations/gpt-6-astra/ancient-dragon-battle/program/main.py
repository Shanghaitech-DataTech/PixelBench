import random, math
random.seed(12)
c=new_canvas(256,256,name='ancient_dragon_battle')
# Restrained sunset, stone, iron and fire palette.
ink='#151625'; deep='#242039'; plum='#38283e'; violet='#503448'; wine='#75404b'; red='#a24a45'; rust='#bf5b43'; orange='#e98248'; gold='#ffbb61'; light='#ffe5a0'
# Wide stepped bands in the dusk sky
for y in range(256):
    col=('#28243e' if y<16 else '#392b46' if y<34 else '#513348' if y<53 else '#79404d' if y<71 else '#a3504b' if y<88 else '#ca674e' if y<110 else '#e58b59' if y<139 else '#ae6652' if y<170 else '#594249')
    c.line(0,y,255,y,col)
c.circle(183,77,35,'#ed9c60'); c.circle(183,77,29,'#ffc878')
# Long torn clouds, with warm undersides
for pts,col in [([(0,20),(24,20),(34,24),(60,24),(67,28),(91,29),(75,34),(42,32),(22,30),(0,30)],plum), ([(163,8),(198,9),(211,13),(255,13),(255,23),(226,20),(215,17),(177,17)],plum), ([(0,64),(19,62),(27,65),(52,66),(61,69),(33,73),(0,70)],wine), ([(204,54),(226,50),(255,51),(255,58),(234,57),(215,60)],wine)]:c.poly(pts,col)
for x,y,w in [(2,75,29),(218,65,35),(3,42,42),(196,31,44),(112,113,32),(206,103,48)]:c.line(x,y,x+w,y,'#cc7658')
# Far serrated mountains
c.poly([(0,140),(0,115),(10,108),(17,111),(35,91),(48,109),(63,103),(75,122),(87,112),(99,121),(114,113),(134,136),(159,124),(175,110),(189,119),(211,96),(224,114),(237,107),(255,127),(255,166)],'#79505a')
c.poly([(0,153),(0,137),(27,114),(38,126),(50,119),(72,144),(95,132),(113,148),(139,134),(157,139),(183,126),(195,139),(218,118),(230,132),(255,121),(255,172)],'#513e50')
for pts in [[(14,114),(35,91),(43,105),(35,101),(31,106),(27,104)],[(201,108),(211,96),(221,111),(212,105),(210,107)]]:c.poly(pts,'#b37665')
# distant banners and siege scars
for x in [6,41,61,213,244]:
    c.line(x,143,x,130,plum);c.poly([(x,130),(x+8,132),(x+5,136),(x,135)],'#71434a')
# ground and broken plateau
c.poly([(0,179),(33,164),(55,168),(77,156),(104,166),(136,155),(173,163),(200,153),(223,165),(255,160),(255,256),(0,256)],'#403242')
c.poly([(0,216),(30,199),(64,205),(99,193),(143,202),(191,189),(227,196),(255,186),(255,256),(0,256)],'#292839')
for i in range(250):
    x=random.randrange(256);y=random.randrange(177,256)
    c.line(x,y,min(255,x+random.randint(1,5)),y,random.choice(['#4b3c46','#352d3d','#59434a']))
# Smoke columns behind castle and creature: clustered opaque curls
for bx,by,scale in [(98,150,1),(183,139,1.1),(201,164,.65),(65,169,.6)]:
    for j in range(13):
        xx=int(bx+math.sin(j*.69)*7-j*1.8); yy=int(by-j*5*scale);r=int(6+j*.42)
        c.circle(xx,yy,r,random.choice(['#3a303e','#42343f','#4d3843']))
        if j%2==0:c.circle(xx-3,yy-2,max(2,r-4),'#58404a')
# Castle platform
c.poly([(64,204),(82,185),(190,184),(211,203),(202,220),(57,220)],ink)
c.poly([(65,209),(83,195),(193,196),(204,208),(195,219),(60,219)],'#4e4350')
for x in range(65,201,13):c.line(x,215,x+5,209,'#76606a')
# walls helpers
def box(x,y,w,h,col,edge=ink):
    c.rect(x,y,w,h,edge);c.rect(x+1,y+1,w-2,h-2,col)
def masonry(x,y,w,h,base,lit):
    c.rect(x,y,w,h,base)
    for yy in range(y+2,y+h,6):
        c.line(x,yy,x+w-1,yy,'#39313e')
        for xx in range(x+(3 if (yy-y)//6%2 else 0),x+w,9):
            c.line(xx,yy,xx,min(yy+5,y+h-1),'#39313e')
            if random.random()<.7:c.line(xx+1,yy+1,min(xx+6,x+w-1),yy+1,lit)
def tower(x,y,w,h):
    box(x,y+7,w,h-7,'#63505a'); masonry(x+2,y+9,w-4,h-11,'#63505a','#856570')
    c.rect(x+w-7,y+9,5,h-11,'#433946');c.line(x+2,y+9,x+2,y+h-2,'#a17774')
    box(x-2,y+5,w+4,6,'#98706c');c.line(x-1,y+6,x+w,y+6,'#c6947e')
    for xx in range(x-2,x+w,7):box(xx,y,5,7,'#88636a');c.line(xx+1,y+1,xx+3,y+1,'#bd8a79')
    for yy in range(y+20,y+h-6,22):
        box(x+w//2-2,yy,5,11,ink);c.set(x+w//2+2,yy+9,'#df8751')
    box(x-2,y+h-6,w+4,7,'#544652')
# rear great keep
tower(113,132,39,66)
box(120,118,25,17,'#55404e')
masonry(121,120,23,13,'#63505a','#8a6267')
for xx in [125,136]:
    c.rect(xx,122,3,8,ink);c.set(xx+2,128,'#de9159')
c.poly([(117,119),(132,97),(148,119)],ink);c.poly([(120,117),(132,101),(144,117)],'#583947');c.line(132,102,142,117,'#a66757')
c.line(132,97,132,87,ink);c.poly([(133,88),(144,90),(141,94),(133,93)],'#b86b4f')
# side curtain walls
box(69,171,127,40,'#5c4b55');masonry(71,179,123,29,'#584854','#7c6067')
c.rect(72,177,120,3,ink);c.line(73,175,191,175,'#ae8275')
for x in range(71,195,9):box(x,167,6,9,'#84666a');c.line(x+1,168,x+4,168,'#bc8b7c')
# arrow slits
for x in [78,96,116,151,171,187]:
    c.rect(x,188,3,9,ink);c.line(x+3,188,x+3,197,'#967169')
# gateway with stepped gothic arch
c.poly([(119,212),(119,192),(123,184),(132,178),(141,184),(145,192),(145,212)],ink)
c.poly([(123,211),(123,193),(126,187),(132,183),(138,188),(141,194),(141,211)],'#282334')
for x in range(125,141,4):c.line(x,189 if x not in [125,137] else 193,x,208,'#68515a')
c.line(123,197,141,197,'#6d535a');c.line(123,204,141,204,'#6d535a')
c.poly([(122,213),(141,213),(157,232),(106,232)],'#6a4a48')
c.line(120,216,110,228,'#a17059')
tower(79,138,25,76);tower(166,128,29,83)
# shields and banners on stone
for x,y in [(86,172),(174,163)]:
    c.line(x-1,y-2,x+11,y-2,'#bd976d'); c.poly([(x,y),(x+9,y),(x+9,y+15),(x+5,y+20),(x,y+15)],ink);c.poly([(x+1,y+1),(x+8,y+1),(x+8,y+14),(x+5,y+18),(x+1,y+14)],'#8d3844');c.line(x+4,y+4,x+4,y+13,'#db9f64');c.line(x+2,y+7,x+6,y+7,'#db9f64')
# Castle fires, nested jagged tongues
def fire(x,y,w,h):
    c.poly([(x-w,y),(x-w+1,y-h//3),(x-w//2,y-h//2),(x-w//2-2,y-h),(x+1,y-h*2//3),(x+w//3,y-h-4),(x+w//2,y-h//3),(x+w,y-h//2),(x+w,y)],'#a6433c')
    c.poly([(x-w+2,y),(x-w//2,y-h//3),(x-w//2,y-h*3//4),(x+1,y-h//2),(x+w//3,y-h*4//5),(x+w-2,y)],'#ed7840')
    c.poly([(x-w//2,y),(x-1,y-h//2),(x+2,y-h//3),(x+3,y-h*2//3),(x+w//2,y)],'#ffc365')
    c.poly([(x-2,y),(x,y-h//3),(x+3,y)],'#fff0b2')
fire(93,140,11,27);fire(182,130,13,26);fire(152,172,7,22);fire(69,178,6,19)
# THE ANCIENT DRAGON: broad torn bat wings with articulated fingers.
def shape(points,fill,edge=ink):
    c.poly(points,fill);c.poly(points,edge,fill=False)
# far wing
shape([(134,69),(157,41),(185,12),(211,13),(238,28),(223,28),(208,40),(201,56),(187,53),(177,67),(163,65),(149,83)],'#673344')
shape([(141,65),(163,42),(185,17),(180,37),(172,49),(162,60)],'#a6504b')
shape([(184,18),(208,17),(230,26),(209,31),(184,48),(175,59)],'#87404a')
shape([(181,45),(208,34),(199,52),(186,49),(178,61),(165,62)],'#97474b')
for pts in [[(138,72),(165,42),(185,15),(208,16),(236,28)],[(185,16),(181,39),(164,64)],[(184,43),(209,33),(235,28)]]:
    for a,b in zip(pts,pts[1:]):c.line(*a,*b,'#d17b60')
# near wing great angular sail
shape([(133,73),(115,48),(82,17),(59,14),(23,29),(45,30),(56,44),(66,61),(79,58),(89,76),(102,74),(114,91),(135,87)],'#6c3444')
shape([(128,72),(111,51),(82,22),(91,45),(106,67),(119,83)],'#a04b4c')
shape([(80,21),(60,18),(31,27),(49,28),(61,40),(76,50),(93,58)],'#b05a53')
shape([(78,26),(76,49),(68,56),(80,53),(91,69),(101,69),(92,52)],'#8e4149')
# ribs and weathered wing scars
for pts in [[(131,80),(111,49),(81,18),(59,15),(24,29)],[(81,19),(77,48),(66,60)],[(80,21),(95,53),(89,75)],[(95,53),(111,70),(113,88)]]:
    for a,b in zip(pts,pts[1:]):c.line(*a,*b,ink)
for a,b in [((128,74),(110,49)),((109,47),(81,20)),((79,19),(60,16)),((59,17),(30,27)),((82,25),(96,53))]:c.line(*a,*b,'#e19a6b')
for x,y in [(56,28),(61,31),(65,33),(88,42),(95,51),(111,68),(190,28),(197,25)]:c.line(x,y,x+3,y+2,'#c0715a')
# curling tail behind body
c.path('M 138 82 C 124 109 88 118 63 105 L 52 89 L 65 96 C 84 106 108 99 120 80 Z',ink)
c.path('M 131 86 C 116 107 84 111 65 102 L 58 94 L 67 98 C 90 106 113 94 122 83 Z','#77514e')
c.path('M 126 90 C 109 108 83 108 66 101', '#b88564',fill=False)
# body, neck and crocodilian head
c.path('M 115 74 Q 119 62 131 62 Q 143 63 149 75 Q 156 89 165 81 L 175 69 L 184 67 L 192 72 L 203 74 L 208 80 L 203 85 L 190 85 L 185 80 Q 173 99 160 100 Q 140 99 133 87 L 124 96 L 113 90 Z',ink)
c.path('M 118 75 Q 122 65 132 65 Q 141 67 145 78 Q 155 94 166 85 L 177 73 L 185 71 L 191 76 L 202 77 L 204 81 L 191 81 L 184 76 Q 173 97 161 96 Q 145 95 135 82 L 122 92 L 117 87 Z','#67504e')
c.path('M 123 69 Q 135 65 143 79 Q 156 99 168 88 L 179 75 L 186 74', '#b07a5a',fill=False)
c.path('M 141 84 Q 151 99 164 94 Q 174 89 182 79 L 187 82 Q 171 103 157 98 Z','#a57558')
# horns, spines and ancient ridges
for pts in [[(177,71),(176,58),(184,69)],[(183,69),(190,58),(188,72)],[(125,66),(122,55),(131,64)],[(133,66),(135,58),(139,70)],[(142,73),(147,66),(148,79)],[(114,97),(112,103),(120,98)],[(102,103),(100,109),(108,105)]]:shape(pts,'#c39269')
c.line(178,61,180,69,light);c.line(188,61,185,69,light)
c.rect(187,74,5,3,ink);c.line(188,74,191,74,'#ffdc78');c.set(189,75,'#fff2c0');c.set(201,78,ink)
c.line(192,82,205,82,ink)
for x in [194,198,202]:c.line(x,82,x-1,84,'#efcd93')
# dangling limbs with hooked talons
for pts in [[(130,83),(139,93),(137,102),(145,108),(143,111),(132,106),(132,97),(124,91)],[(154,91),(156,99),(163,102),(164,107),(160,108),(150,102),(148,94)]]:shape(pts,'#73554e')
for a,b in [((135,105),(135,112)),((140,108),(140,114)),((144,108),(146,113)),((158,104),(158,110)),((162,105),(165,110))]:c.line(*a,*b,'#dfb681')
# scale clusters following body
for x,y in [(121,75),(126,71),(130,76),(125,82),(135,78),(137,83),(145,86),(150,91),(157,92),(165,90),(171,85),(176,79)]:
    c.line(x,y,x+2,y,'#ba8864');c.set(x+1,y+1,'#342c37')
# Armor-like plates catch sunset along the coiling throat.
for x,y in [(144,88),(148,92),(153,94),(158,95),(163,94),(168,92),(172,89),(176,85),(179,81)]:
    c.line(x,y,x+1,y+3,'#654749');c.set(x+2,y,'#d4a171')
for x,y in [(119,78),(121,84),(126,86),(130,80),(134,73),(139,79)]:
    c.line(x,y,x+2,y,'#96705b');c.set(x+2,y+1,'#3d323b')
# short gout of fire bends onto the eastern battlement
c.poly([(202,84),(209,90),(207,97),(214,111),(206,107),(203,118),(198,112),(191,123),(186,117),(193,105),(198,100),(199,92)],'#aa4941')
c.poly([(203,85),(206,92),(203,98),(209,108),(202,105),(199,115),(194,117),(197,106),(201,99)],'#ef8946')
c.poly([(203,87),(203,96),(200,104),(202,109),(197,113),(199,102)],'#ffe092')
# sparks in air
for i in range(80):
    x=random.randrange(55,216);y=random.randrange(103,182)
    if random.random()<.7 and not (110<x<171 and y>129):c.set(x,y,random.choice([orange,gold,'#b55b48']))
# rampart defenders
def knight(x,y,scale=1,shieldcol='#536574',facing=1):
    # y is ground; compact 12 pixel silhouette
    c.line(x-2,y,x-1,y-4,ink);c.line(x+2,y,x+1,y-4,ink)
    c.rect(x-2,y-9,5,6,ink);c.rect(x-1,y-8,3,4,'#68747e');c.set(x-1,y-8,'#bac0b2')
    c.rect(x-2,y-13,5,4,ink);c.rect(x-1,y-12,3,2,'#9ba7a5');c.line(x-2,y-10,x+2,y-10,ink);c.set(x+2,y-11,'#e9c598')
    shape([(x-4,y-8),(x,y-8),(x,y-3),(x-2,y-1),(x-4,y-3)],shieldcol)
    c.line(x-3,y-7,x-3,y-4,'#adad9a')
    c.line(x+3,y-5,x+4,y-19,'#b29075');c.line(x+4,y-19,x+4,y-22,'#d4cfb0');c.set(x+3,y-19,'#7c9094')
for x,y in [(76,168),(110,168),(155,168),(187,129),(172,129),(84,139),(99,139)]:knight(x,y)
# siege towers timber framework on either flank
def siege(x,y,w,h):
    # y base, sloped side silhouette
    shape([(x,y-3),(x+3,y-h),(x+w-5,y-h),(x+w,y-3)],'#3d2d34')
    for yy in range(y-h+7,y-4,6):c.line(x+4,yy,x+w-4,yy,'#705044')
    for xx in [x+3,x+w-6]:
        c.line(xx,y-h,xx-2 if xx==x+3 else xx+3,y-4,ink)
        c.line(xx+1,y-h+2,xx-1 if xx==x+3 else xx+4,y-4,'#b17d55')
    for yy in range(y-h+16,y-5,17):
        c.line(x+3,yy,x+w-4,yy,'#bf8859');c.line(x+4,yy-15,x+w-4,yy-1,'#231e2b');c.line(x+5,yy-15,x+w-4,yy-2,'#986746')
    box(x-2,y-h-3,w+2,10,'#664436')
    for xx in range(x-2,x+w,6):box(xx,y-h-7,4,7,'#8f6045')
    for xx in [x+3,x+w-3]:
        c.circle(xx,y-2,5,ink);c.circle(xx,y-2,3,'#77523e');c.set(xx,y-2,'#c39a63');c.line(xx-2,y-2,xx+2,y-2,ink)
    c.line(x+w-2,y-h+7,min(255,x+w+17),y-h+17,ink);c.line(x+w-2,y-h+8,min(255,x+w+17),y-h+18,'#aa7c54')
siege(17,208,25,54);siege(226,192,23,46)
# pennants atop siege engines
for x,y in [(29,147),(238,139)]:
    c.line(x,y,x,y-18,ink);shape([(x+1,y-18),(x+15,y-15),(x+10,y-11),(x+1,y-11)],'#a04a44');c.line(x+2,y-17,x+10,y-15,'#df9665')
# arrows tracing trajectories, with fletching
for x,y,dx,dy in [(45,91,10,7),(20,115,10,5),(67,120,11,-7),(220,96,-10,-7),(222,121,-12,-5),(147,120,7,-10),(49,142,9,-10),(213,144,-8,-12),(31,83,10,6)]:
    c.line(x,y,x+dx,y+dy,'#221e2d');c.set(x+dx,y+dy,'#e2bb8b');c.line(x,y,x-2,y-3,'#d5a985');c.set(x-2,y,'#d5a985')
# massed troops: readable repeating helmet-shield-spear silhouettes
for row in range(4):
    yy=205+row*11
    for col in range(8):
        xx=43+col*10+row*3
        if 103<xx<157 and row<2:continue
        knight(xx,yy,shieldcol=random.choice(['#455667','#526472','#66505b']))
for row in range(4):
    for col in range(7):
        xx=164+col*12-row*3;yy=207+row*12
        knight(xx,yy,shieldcol=random.choice(['#803f48','#6e3c49','#8f4b4b']))
# foreground black soil silhouette
c.poly([(0,242),(12,238),(27,243),(39,240),(53,247),(76,246),(98,250),(137,247),(161,251),(190,245),(211,248),(231,240),(255,244),(255,256),(0,256)],ink)
# large foreground champion and war standard
knight(32,246,shieldcol='#67777a')
c.line(20,251,25,210,ink);c.line(21,251,26,209,'#a38b72');c.poly([(26,209),(39,211),(48,208),(45,224),(36,226),(25,222)],ink);c.poly([(27,211),(39,213),(46,211),(43,221),(36,224),(27,220)],'#973f48');c.line(34,214,34,220,'#e3b774');c.line(31,217,38,217,'#e3b774')
# foreground spear silhouette at right edge
c.line(240,255,231,210,ink);c.poly([(228,211),(229,199),(234,209)],'#a3aaa5');c.line(230,204,231,210,light)
for x,y in [(7,230),(11,222),(62,235),(151,241),(219,225),(247,219),(207,235)]:
    c.line(x,y,x+3,y-2,'#d58d52');c.set(x+1,y-1,'#ffcf73')
assert c.stats()['size']==(256,256) or list(c.stats()['size'])==[256,256]
assert c.stats()['colors_used']<=140
view(c)
save('ancient-dragon-battle',c)
finish(c)
