import random, math
random.seed(27)
result = new_canvas(256,256,background='#201d32',name='ancient-dragon-battle')
c=result
# Compact, shared cinematic palette
ink='#171b28'; deep='#252336'; plum='#3e2d43'; wine='#633849'; rust='#9b4945'; red='#ca6046'; orange='#eb864b'; gold='#ffb95f'; light='#ffdc8b'; cream='#fff1b1'
stone0='#252d3c'; stone1='#364454'; stone2='#4d5b66'; stone3='#738080'; stone4='#a6a18b'
# Sunset, in discrete pixel bands
bands=[(0,25,'#33273e'),(25,49,'#513046'),(49,72,'#773d4c'),(72,96,'#a74d4b'),(96,116,'#d26b4f'),(116,144,'#e98d59'),(144,175,'#d58a5a'),(175,256,'#514450')]
for y0,y1,col in bands:c.rect(0,y0,256,y1-y0,col)
# Irregular edges between the broad bands
for y,col in [(25,'#33273e'),(49,'#513046'),(72,'#773d4c'),(96,'#a74d4b'),(116,'#d26b4f')]:
 for i in range(12):
  x=random.randrange(256);c.rect(x,y,random.randrange(4,25),random.randrange(1,3),col)
# Setting sun
c.circle(176,77,37,gold); c.circle(176,77,33,'#ffc973')
c.rect(143,91,68,2,'#ffb95f'); c.rect(147,100,58,2,'#eb864b');c.rect(156,107,42,2,'#eb864b')
# Streaked clouds and torn, lit edges
def cloud(x,y,w,h,col,lit=None):
 c.poly([(x,y+h//2),(x+7,y+h//2),(x+12,y+1),(x+w//3,y+1),(x+w//3+4,y),(x+w*2//3,y+2),(x+w-9,y+h//2),(x+w,y+h//2+2),(x+w-6,y+h),(x+3,y+h)],col)
 if lit:c.line(x+7,y+h,x+w-8,y+h,lit)
cloud(-8,9,79,10,plum,wine);cloud(169,7,93,12,plum,wine)
cloud(6,47,64,7,wine,rust); cloud(210,61,54,9,wine,red)
cloud(1,92,42,7,rust,orange); cloud(202,105,61,6,rust,orange)
cloud(81,117,61,4,red,gold)
for x,y,w in [(3,35,24),(18,38,13),(225,29,27),(237,33,11),(97,9,25),(104,12,16),(9,108,32),(217,96,25)]:c.rect(x,y,w,1,rust)
# Far mountains
c.poly([(0,150),(0,124),(14,113),(21,118),(38,101),(51,118),(59,113),(81,139),(101,118),(112,132),(129,122),(145,145),(175,129),(183,132),(204,111),(216,123),(224,118),(247,137),(255,126),(255,173)],'#88535b')
c.poly([(9,129),(38,101),(51,118),(44,115),(38,110),(33,118),(27,119)],'#b97363')
c.poly([(185,135),(204,111),(216,123),(208,120),(203,118),(200,127)],'#b97363')
c.poly([(0,156),(16,137),(32,149),(56,123),(66,136),(74,133),(97,158),(118,137),(135,147),(149,136),(175,154),(196,138),(220,148),(238,132),(255,143),(255,188),(0,188)],'#614855')
c.poly([(37,155),(56,123),(65,136),(57,132),(54,141)],'#8a5e61')
# Hazy distant ruined spires
for x,y,w in [(6,151,6),(42,145,4),(225,149,5),(244,145,7)]:
 c.rect(x,y,w,24,'#514450');c.poly([(x-1,y),(x+w//2,y-8),(x+w,y)],'#514450')
# Smoke billows behind the dragon and castle
smoke=['#503b49','#67434c','#81504f','#a45c51']
def plume(x,y,h,width):
 for i in range(h//7):
  yy=y-i*7; xx=int(x+math.sin(i*.65)*5-i*.22)
  r=int(width+i*.35)
  c.circle(xx,yy,r,smoke[0]);c.circle(xx+3,yy-2,max(2,r-2),smoke[1])
  if i<5:c.circle(xx+5,yy+2,max(2,r-4),smoke[2])
plume(198,146,70,9);plume(107,167,66,7);plume(231,176,48,7)
# Rolling field and the castle's crag
c.poly([(0,194),(31,183),(64,186),(92,177),(148,180),(192,173),(225,185),(255,182),(255,255),(0,255)],'#45404a')
c.poly([(39,223),(52,191),(68,180),(195,179),(222,194),(239,223),(255,244),(255,255),(0,255)],'#30323c')
c.poly([(49,224),(68,189),(104,191),(86,209),(84,232),(66,226)],'#50505a')
c.poly([(187,193),(210,199),(224,225),(203,217),(196,235),(177,246)],'#4c4650')
c.poly([(65,201),(78,196),(70,218),(61,220)],'#73706b')
c.poly([(93,207),(105,197),(102,224),(92,239),(85,237)],'#42444e')
c.poly([(198,205),(207,213),(209,224),(199,219)],'#716365')
# Sooty castle masonry, individually staggered

def masonry(x,y,w,h,base=stone1):
 c.rect(x,y,w,h,ink);c.rect(x+2,y+1,w-4,h-2,base)
 for yy in range(y+3,y+h-2,6):
  c.line(x+2,yy,x+w-3,yy,stone0)
  for xx in range(x+3+((yy//6)%2)*5,x+w-3,10):
   c.line(xx,yy,xx,yy+5,stone0)
   if random.random()<.7:c.line(xx+1,yy+1,min(xx+6,x+w-3),yy+1,stone2)
 c.line(x+w-3,y+1,x+w-3,y+h-2,stone3)

def merlons(x,y,w,base=stone2):
 c.rect(x,y+6,w,5,ink);c.rect(x+1,y+7,w-2,2,base)
 for xx in range(x,x+w-3,9):
  c.rect(xx,y,6,8,ink);c.rect(xx+1,y+1,4,6,base);c.line(xx+1,y+1,xx+4,y+1,stone4)

def window(x,y,fire=False):
 c.rect(x,y+2,5,12,ink);c.rect(x+1,y,3,14,ink)
 c.line(x+5,y+3,x+5,y+13,stone3)
 if fire:
  c.rect(x+1,y+4,3,9,red);c.rect(x+2,y+6,2,7,gold);c.set(x+2,y+5,light)
 else:c.rect(x+1,y+3,1,8,stone0)

def tower(x,y,w,h):
 masonry(x,y+8,w,h-8)
 c.rect(x-2,y+8,w+4,4,ink);c.rect(x-1,y+8,w+2,2,stone3)
 for yy in range(y+24,y+h-4,23):
  c.rect(x,yy,w,3,stone0);c.line(x+1,yy,x+w-2,yy,stone2)
 merlons(x-3,y,w+6)
 for wx in [x+6,x+w-11]:
  window(wx,y+17,random.random()<.45)
 if h>55:window(x+w//2-2,y+43,True)
# Rear keep, damaged and lit from within
masonry(116,139,64,61)
merlons(116,132,64)
tower(120,122,23,72)
tower(162,117,25,79)
# High slate roof and pennant
c.poly([(118,122),(131,98),(146,122)],ink);c.poly([(121,120),(131,102),(141,120)],stone1)
c.line(131,103,141,120,stone3);c.line(131,98,131,88,ink)
c.poly([(132,89),(146,91),(139,94),(132,94)],'#9b4945');c.line(133,90,142,91,gold)
# Castle courtyard fire silhouettes
for x,y in [(146,149),(155,151),(173,146),(119,164)]:window(x,y,True)
# Main curtain wall
masonry(63,171,158,37)
merlons(62,163,161)
c.rect(64,181,155,3,stone0);c.line(65,180,219,180,stone3)
# front buttresses
for x in [78,100,177,200]:
 c.poly([(x,181),(x+5,181),(x+5,199),(x+8,211),(x-2,211),(x,199)],ink)
 c.poly([(x+1,183),(x+3,183),(x+3,200),(x+5,209),(x,209)],stone2)
# Towers on either end
tower(57,144,29,70);tower(207,136,29,78)
# Gatehouse and its dark arch
tower(123,155,43,60)
c.path('M132 213 L132 191 Q144 174 156 191 L156 213 Z',ink)
c.path('M135 212 L135 193 Q144 180 153 193 L153 212 Z','#493c3e')
for xx in range(136,154,4):c.line(xx,190 if xx in (140,144,148) else 194,xx,211,ink)
for yy in [195,201,207]:c.line(134,yy,154,yy,ink)
c.path('M130 210 L130 191 Q144 171 158 191 L158 210',stone4,False)
c.line(129,213,159,213,stone0)
# Path through the foreground
c.poly([(134,212),(154,212),(193,255),(108,255)],'#605252')
c.poly([(137,213),(146,213),(157,237),(148,255),(119,255)],'#78615a')
for i in range(65):
 yy=random.randrange(215,255);xx=random.randrange(max(109,134-(yy-212)//2),min(191,155+(yy-212)))
 c.line(xx,yy,xx+random.randrange(1,4),yy,random.choice(['#8a7161','#4b454a','#9a7a63']))
# Splintered banners on tower facades
for x,y in [(65,176),(216,168),(126,181)]:
 c.line(x-2,y,x+9,y,ink);c.poly([(x,y+1),(x+7,y+1),(x+7,y+15),(x+4,y+12),(x+1,y+17)],'#713b46')
 c.line(x+1,y+2,x+1,y+12,'#ad584c');c.rect(x+3,y+4,2,7,gold);c.rect(x+1,y+6,6,2,gold)
# Fire tongues at rooflines

def flame(x,y,h,w=7):
 c.poly([(x-w,y),(x-w+1,y-h//3),(x-3,y-h//2),(x-4,y-h),(x+1,y-h*2//3),(x+3,y-h-4),(x+4,y-h//2),(x+w,y-3),(x+w-2,y+2)],'#a74638')
 c.poly([(x-w+2,y),(x-2,y-h//2),(x-2,y-h+4),(x+2,y-h//2),(x+4,y-h*2//3),(x+w-2,y),(x,y+2)],orange)
 c.poly([(x-3,y),(x,y-h//2),(x+1,y-h//3),(x+3,y),(x,y+2)],light)
 c.line(x,y-2,x,y-7,cream)
for xx,yy,hh,ww in [(101,170,23,7),(111,170,32,7),(151,139,22,6),(157,138,18,5),(191,152,30,9),(200,146,39,8),(209,144,23,6),(227,137,15,6)]:flame(xx,yy,hh,ww)
# Collapse and glowing rubble
for i in range(48):
 x=random.randrange(89,119);y=random.randrange(180,208)
 c.rect(x,y,random.choice([1,2,3]),2,random.choice([stone0,stone2,rust,orange]))
# Tiny defenders, shields and bright helmets

def knight(x,y,side=1,shield='#935044'):
 # y at boots; 12px tall
 c.line(x-1,y-4,x-2,y,ink);c.line(x+2,y-4,x+3,y,ink)
 c.rect(x-2,y-8,5,5,ink);c.rect(x-1,y-8,3,5,stone3)
 c.rect(x-2,y-12,5,4,ink);c.rect(x-1,y-12,3,2,'#b8b6a0');c.set(x+1,y-10,ink)
 c.set(x-1,y-13,stone3)
 sx=x-4 if side==1 else x+3
 c.poly([(sx-1,y-8),(sx+3,y-8),(sx+3,y-3),(sx+1,y-1),(sx-1,y-3)],ink)
 c.poly([(sx,y-7),(sx+2,y-7),(sx+2,y-3),(sx+1,y-2),(sx,y-3)],shield)
 c.line(sx+1,y-6,sx+1,y-3,light)
 px=x+5*side
 c.line(px,y-3,px,y-19,'#92715b');c.poly([(px-1,y-18),(px,y-23),(px+1,y-18)],stone4)
 c.line(x+2*side,y-7,px,y-8,stone3)
for x,y in [(63,150),(78,150),(93,169),(115,169),(137,161),(159,161),(181,170),(212,141),(229,141)]:knight(x,y)
# Siege towers, with wood beams and wheels

def siege(x,y,w,h):
 # top floor y, total h
 c.poly([(x,y+h),(x+5,y),(x+w-6,y),(x+w,y+h)],ink)
 c.poly([(x+4,y+h-3),(x+8,y+3),(x+w-9,y+3),(x+w-4,y+h-3)],'#57423f')
 for yy in range(y+9,y+h-4,7):c.line(x+6,yy,x+w-6,yy,'#87604c')
 for yy in [y+17,y+36,y+54]:
  if yy<y+h-6:
   c.rect(x+2,yy,w-4,4,ink);c.line(x+3,yy,x+w-4,yy,'#a37752')
   c.line(x+7,yy+4,x+w-8,min(yy+18,y+h-4),ink);c.line(x+8,yy+4,x+w-7,min(yy+18,y+h-4),'#ac7d54')
 for xx in [x+4,x+w-6]:c.line(xx,y+1,xx-2 if xx<x+w//2 else xx+2,y+h-2,'#a17855')
 c.rect(x-2,y-3,w+4,5,ink);c.line(x-1,y-3,x+w,y-3,'#b28c61')
 for xx in range(x-2,x+w,7):c.rect(xx,y-8,4,7,ink);c.rect(xx+1,y-7,2,4,'#87604c')
 for xx in [x+5,x+w-5]:
  c.circle(xx,y+h,5,ink);c.circle(xx,y+h,3,'#79604d');c.set(xx,y+h,ink);c.line(xx-2,y+h-2,xx+2,y+h+2,ink)
 # slit
 c.rect(x+w//2-3,y+3,6,7,ink)
 c.line(x+w-2,y+9,x+w+15,y+20,ink);c.line(x+w-2,y+8,x+w+15,y+19,'#b28c61')
siege(12,160,30,66)
siege(237,175,18,40)
knight(24,157,1,'#ac7048')
c.line(18,152,18,131,ink);c.poly([(19,132),(34,135),(30,139),(35,142),(19,140)],'#773c45');c.line(20,133,29,135,'#d47b50')
# Dragon - long curling tail behind wings
c.path('M134 82 C111 90 105 111 78 117 C59 121 46 110 53 99 C56 94 64 93 69 95 C58 96 56 102 62 106 C78 118 101 88 116 79 Z',ink)
c.path('M128 84 C107 95 103 110 78 113 C64 117 52 108 55 102 C55 113 73 112 85 106 C99 98 108 83 121 82 Z','#6e6953')
c.path('M122 85 C102 94 99 110 76 113 C67 114 61 111 59 108', '#c49761',False)
# Left wing: thick angular leading spar and torn scalloped trailing membrane
left=[(131,83),(117,52),(96,30),(44,16),(54,32),(59,48),(70,44),(80,49),(83,62),(91,59),(100,67),(103,81),(115,77),(125,91)]
c.poly(left,ink)
c.poly([(126,81),(113,53),(95,34),(50,21),(60,41),(69,39),(82,46),(88,55),(95,54),(105,65),(108,74),(116,71)],'#81433e')
c.poly([(52,22),(96,34),(110,52),(80,39)],'#b65d47')
c.poly([(80,41),(114,55),(125,80),(106,62)],'#9b4945')
c.poly([(61,33),(66,40),(78,43),(74,37)],'#cc7950')
# ribs and deep seams
for pts in [[(46,18),(96,31),(115,51),(131,83)],[(97,32),(81,42),(84,60)],[(114,52),(98,55),(104,79)],[(96,32),(62,32),(59,46)]]:
 for a,b in zip(pts,pts[1:]):c.line(*a,*b,ink)
for a,b in [((49,19),(95,32)),((96,33),(114,52)),((115,52),(128,81)),((97,34),(84,46)),((84,46),(85,56)),((113,54),(104,63))]:c.line(*a,*b,'#d4a16a')
c.poly([(94,31),(91,23),(97,26),(101,33)],ink);c.line(94,25,97,30,light)
# Right wing, vaulted against the sun
right=[(140,86),(145,59),(161,35),(213,17),(207,29),(204,45),(196,43),(187,49),(184,63),(175,60),(164,68),(160,83),(148,94)]
c.poly(right,ink)
c.poly([(145,81),(150,59),(164,39),(207,22),(199,39),(191,40),(181,48),(179,57),(173,55),(160,64),(156,79),(148,87)],'#9b4945')
c.poly([(165,39),(205,23),(187,38),(151,62)],'#ce744e')
c.poly([(152,64),(181,49),(176,57),(161,63),(155,80)],'#b65d47')
for pts in [[(141,86),(148,58),(162,36),(212,18)],[(162,36),(194,34),(204,44)],[(162,36),(178,46),(184,62)],[(148,58),(163,65),(160,82)]]:
 for a,b in zip(pts,pts[1:]):c.line(*a,*b,ink)
for a,b in [((144,80),(151,58)),((151,57),(164,37)),((164,37),(208,21)),((166,38),(192,35)),((164,39),(178,47))]:c.line(*a,*b,'#e0ae73')
c.poly([(160,36),(164,28),(166,34)],ink);c.set(164,31,light)
# Dragon trunk and S-curved neck
c.path('M110 80 Q120 71 135 77 L148 81 Q158 82 163 68 Q166 60 175 64 L186 75 L180 87 Q170 84 169 89 Q161 101 143 100 Q123 99 110 90 Z',ink)
c.path('M115 81 Q128 77 139 83 Q155 89 164 74 L168 67 L174 67 L179 77 Q170 76 166 87 Q158 97 142 95 Q125 93 115 88 Z','#61654e')
c.path('M120 80 Q131 79 141 85 Q154 91 164 78 L169 68 L173 68 L171 75 Q164 93 148 94 Q134 92 120 86 Z','#8c8860')
c.path('M121 89 Q150 104 166 87 L173 80 L179 81 L175 87 Q169 86 166 92 Q156 103 137 97 Z','#b18c5d')
# Segmented belly scales
for x,y in [(129,93),(135,95),(141,96),(147,97),(153,96),(159,94),(164,91),(169,86)]:c.line(x,y-2,x+2,y+1,'#665646')
# Back spikes silhouette and ivory tips
for x,y in [(112,80),(120,77),(128,77),(137,80),(146,82),(155,79),(161,73),(166,66)]:
 c.poly([(x-2,y+1),(x-1,y-6),(x+4,y+2)],ink);c.line(x-1,y-4,x+1,y,stone4)
# Rear haunch, bent legs and talons
c.path('M129 91 Q139 89 140 99 L134 107 L139 111 L136 116 L125 109 L129 101 L121 98 Z',ink)
c.path('M129 94 L135 96 L136 100 L130 107 L136 112 L132 112 L127 108 L132 99 L125 97 Z','#85835b')
c.poly([(136,111),(141,111),(143,117),(140,115),(138,115),(138,119),(135,117),(133,115)],ink)
c.line(140,113,142,116,light);c.line(137,114,137,117,light)
c.path('M148 94 L156 96 L153 104 L159 109 L155 113 L146 105 Z',ink)
c.path('M149 96 L153 98 L150 104 L156 110 L153 109 L148 104 Z','#a09161')
c.line(157,110,161,115,ink);c.line(155,112,157,116,light)
# Extended forelimb
c.path('M162 85 L167 89 L163 96 L173 96 L177 102 L171 103 L168 100 L159 100 L158 96 Z',ink)
c.path('M163 88 L164 91 L161 97 L171 98 L173 100 L161 99 L160 96 Z','#92936a')
c.line(173,98,176,101,light);c.line(170,100,172,103,light)
# Horned skull, hooked muzzle and open jaws
c.poly([(170,68),(175,64),(184,65),(190,70),(195,73),(194,78),(183,80),(177,77),(170,80),(166,75)],ink)
c.poly([(171,69),(178,67),(184,68),(186,72),(193,74),(192,76),(182,76),(176,74),(171,77)],'#949068')
c.poly([(173,69),(179,68),(184,70),(181,72),(174,72)],'#c4ad77')
c.poly([(174,65),(172,54),(176,57),(179,65)],ink);c.line(174,57,177,64,light)
c.poly([(181,66),(184,56),(186,57),(184,68)],ink);c.line(185,58,183,65,light)
# jaw opening, teeth and nostril
c.poly([(180,78),(190,79),(194,83),(190,85),(178,81),(173,77)],ink)
c.line(179,80,190,83,'#9f996b');c.line(182,76,191,77,ink)
c.set(188,77,cream);c.set(184,77,cream);c.set(186,81,cream);c.set(192,74,ink)
c.line(179,71,184,71,ink);c.line(180,72,183,72,gold);c.set(182,72,cream);c.set(183,72,red)
# Carefully clustered scale glints
for x,y in [(118,83),(124,84),(129,82),(132,86),(139,88),(146,90),(152,88),(158,85),(164,79),(170,72),(174,69),(126,88),(136,90)]:
 c.line(x,y,x+2,y,'#c0af78');c.set(x+2,y+1,'#454f43')
# Dragon's fire breath, curling down onto the tallest wall
c.path('M192 78 Q202 79 205 94 Q209 109 221 116 L213 120 Q204 113 202 105 Q199 91 191 83 Z','#ae4a37')
c.path('M193 79 Q201 81 203 93 Q209 113 219 116 L214 117 Q204 110 201 99 Q199 87 192 82 Z',orange)
c.path('M194 80 Q199 83 202 94 Q206 109 215 114 Q207 104 203 87 Z',light)
c.path('M194 80 Q200 86 200 90 L196 83 Z',cream)
for x,y in [(205,91),(209,103),(218,110),(211,117),(198,88)]:c.set(x,y,gold)
# Airborne arrows with distinct steel heads and feathered tails
def arrow(x,y,dx,dy):
 c.line(x,y,x+dx,y+dy,ink);c.line(x+1,y,x+dx,y+dy,'#c2aa83')
 c.line(x-1,y-2,x+2,y,ink);c.line(x-2,y+1,x+1,y+2,stone4)
 ex=x+dx;ey=y+dy;c.poly([(ex,ey),(ex-4 if dx>0 else ex+4,ey),(ex,ey-3 if dy<0 else ey+3)],stone4)
for a in [(27,117,12,-12),(88,131,10,-15),(175,125,-9,-13),(230,91,-12,-11),(39,76,13,-7),(6,139,9,-12),(92,54,9,11),(235,116,-12,-7)]:arrow(*a)
# Ember spray, hottest near fires
for i in range(110):
 x=random.randrange(82,241);y=random.randrange(104,204)
 if random.random()<.5 and y<137:continue
 if random.random()<.6 and (x<117 or x>184):
  c.rect(x,y,1,random.choice([1,1,2]),random.choice([orange,gold,light,rust]))
# Rows of attacking infantry, ordered in perspective
for row in range(3):
 y=219+row*12
 for col in range(5):
  x=63+col*11-row*4
  knight(x,y,1,'#965140')
for row in range(3):
 y=222+row*12
 for col in range(4):
  x=195+col*12+row*2
  knight(x,y,-1,'#a16e45')
# Standards above the soldiers
for x,y in [(57,211),(192,212)]:
 c.line(x,y+24,x,y-20,ink);c.line(x+1,y+24,x+1,y-20,'#ae8c63')
 c.poly([(x+1,y-18),(x+16,y-16),(x+12,y-10),(x+17,y-7),(x+1,y-8)],ink)
 c.poly([(x+2,y-17),(x+13,y-15),(x+10,y-10),(x+13,y-9),(x+2,y-10)],'#873d40')
 c.rect(x+5,y-15,2,5,gold);c.rect(x+3,y-13,6,1,gold)
 c.poly([(x-1,y-20),(x,y-25),(x+2,y-20)],stone4)
# Foreground grass, stones and broken shafts
for i in range(82):
 x=random.randrange(256);y=random.randrange(233,256)
 if 116<x<182:continue
 col=random.choice([ink,deep,'#57504e'])
 c.line(x,y,x+random.randrange(2,5),y,col)
 if random.random()<.3:c.line(x+1,y,x,y-3,col)
c.poly([(0,245),(11,240),(22,244),(31,241),(44,250),(57,249),(65,255),(0,255)],ink)
c.poly([(218,255),(234,247),(242,247),(248,238),(255,241),(255,255)],ink)
c.line(17,243,34,233,'#a58b68');c.poly([(34,233),(34,230),(38,229),(36,234)],stone3)
c.ellipse(35,247,7,3,ink);c.ellipse(35,246,5,2,'#6f5548');c.set(35,246,stone4)
# Near camera knight silhouette anchors the lower left
c.poly([(8,255),(9,245),(6,242),(6,232),(10,228),(16,229),(20,234),(20,243),(23,255)],ink)
c.rect(10,225,7,7,ink);c.rect(11,225,5,3,stone3);c.line(11,225,15,225,stone4)
c.poly([(9,234),(16,234),(18,245),(12,250),(7,245)],'#633849');c.line(10,235,10,244,'#bb7b54')
c.line(22,255,22,218,ink);c.line(23,255,23,220,'#a58b68');c.poly([(21,219),(22,212),(25,219)],stone4)
view(c)
save('ancient-dragon-battle',c)
finish(result)
