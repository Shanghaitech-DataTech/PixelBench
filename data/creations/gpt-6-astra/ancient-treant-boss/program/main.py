import random, math
random.seed(12)
result = new_canvas(256,256,background='#111e22',name='Ancient treant')
c=result
# limited woodland palette
ink='#10171b'; deep='#192523'; bark0='#293028'; bark1='#414333'; bark2='#5b5840'; bark3='#78704c'; bark4='#a29261'
moss0='#263e2c'; moss1='#3e5934'; moss2='#617844'; moss3='#89924d'
# sky bands and distant mist
c.rect(0,0,256,140,'#203631'); c.rect(0,87,256,90,'#29433a');c.rect(0,138,256,65,'#345044')
# distant trees
for i in range(34):
 x=random.randrange(256); w=random.randrange(2,8); top=random.randrange(0,48)
 col=random.choice(['#203a34','#263f37','#2c473c'])
 c.poly([(x,top),(x+w,top),(x+w+3,194),(x-4,194)],col)
 for j in range(3):
  y=random.randrange(20,135); d=random.choice([-1,1])*random.randrange(10,31)
  c.line(x,y,x+d,y-random.randrange(15,35),col)
# graphic god rays from upper right, nestled behind silhouette
for pts,col in [([(183,0),(197,0),(89,207),(62,214)],'#405b44'), ([(206,0),(211,0),(132,202),(118,207)],'#4b6548'), ([(232,0),(243,0),(191,210),(165,211)],'#405b44'), ([(158,0),(163,0),(32,191),(19,197)],'#354f3d')]:c.poly(pts,col)
# ground layers
c.poly([(0,193),(34,183),(71,193),(105,184),(164,190),(201,180),(255,191),(255,255),(0,255)],'#263b31')
c.ellipse(135,222,100,28,'#354533');c.ellipse(132,225,77,19,'#1c2c27')
# framing trunks
for x,w in [(-4,20),(237,22),(20,9),(222,8)]:
 c.poly([(x,0),(x+w,0),(x+w-5,75),(x+w,151),(x+w+7,207),(x-5,217),(x+2,128)],'#172a28')
 c.line(max(0,x+5),1,max(0,x+6),175,'#294039')
# background canopy clusters
for i in range(140):
 x=random.randrange(256); y=random.randrange(0,52)
 if y<25 or x<48 or x>220:
  r=random.randrange(3,13);c.ellipse(x,y,r,max(2,r//2),random.choice(['#162c29','#1d352d','#263e30']))
# ground flecks
for i in range(480):
 x=random.randrange(256);y=random.randrange(190,256)
 c.rect(x,y,random.randrange(1,4),1,random.choice(['#314638','#43523b','#566044','#1c302a']))
# tree geometry on independent layer for procedural bark mask
wood=new_canvas(256,256,name='gnarled wood')
def poly(p,col=bark1):
 wood.poly(p,col);wood.poly(p,ink,fill=False)
def limb(points,widths):
 # polygon tapered bending trunk
 left=[];right=[]
 for (x,y),w in zip(points,widths):left.append((x-w,y));right.append((x+w,y))
 poly(left+right[::-1])
# antler canopy dead branches
limb([(115,93),(100,67),(89,49),(67,38),(52,18)],[12,10,7,5,1])
limb([(100,68),(109,46),(106,26),(113,9)],[8,6,4,0])
limb([(91,51),(78,26),(79,13)],[5,3,0])
limb([(74,40),(53,40),(38,28)],[4,3,0])
limb([(140,88),(154,62),(169,49),(185,24),(202,16)],[13,10,7,4,0])
limb([(158,62),(154,38),(142,23),(145,9)],[7,5,3,0])
limb([(176,41),(199,39),(215,26)],[5,3,0])
limb([(186,26),(182,10)],[3,0])
# widespread arms and upturned claw hands
poly([(111,108),(89,100),(73,110),(60,132),(42,130),(31,113),(20,112),(18,128),(32,153),(51,158),(71,153),(91,132),(109,136)])
poly([(146,107),(166,99),(180,108),(196,128),(211,116),(222,96),(231,102),(230,124),(214,147),(195,152),(178,142),(163,130),(144,135)])
# left talons spreading
limb([(29,132),(17,114),(13,93),(17,78)],[7,5,3,0])
limb([(31,125),(28,105),(33,86),(42,80)],[6,4,2,0])
limb([(41,136),(41,114),(48,99),(55,96)],[6,4,2,0])
limb([(20,126),(8,120),(5,105)],[4,2,0])
# right talons
limb([(217,124),(238,113),(246,96),(242,82)],[6,4,2,0])
limb([(226,111),(226,87),(218,76)],[5,3,0])
limb([(209,125),(207,105),(210,91)],[5,3,0])
limb([(231,122),(247,119),(253,106)],[4,2,0])
# legs and radiating roots
poly([(107,162),(130,179),(117,206),(99,221),(82,226),(59,226),(37,236),(49,222),(80,215),(90,198)])
poly([(132,174),(153,160),(165,196),(178,210),(198,216),(215,232),(190,226),(173,225),(149,213),(138,198)])
poly([(112,194),(124,193),(121,220),(108,236),(88,245),(70,244),(95,234),(103,217)])
poly([(142,193),(155,201),(156,221),(167,236),(183,242),(163,242),(146,230),(137,212)])
poly([(91,208),(85,218),(67,216),(52,208),(34,212),(48,203),(64,204),(76,209)])
poly([(170,208),(181,201),(196,202),(207,193),(202,207),(184,213)])
# torso bulk asymmetry
poly([(111,69),(125,59),(137,68),(151,66),(151,85),(161,104),(158,125),(164,148),(155,175),(142,195),(123,201),(104,187),(94,163),(99,141),(93,117),(103,97)])
# angular bark planes, all hand-composed
for p,col in [([(112,72),(121,65),(118,105),(106,133),(110,164),(123,185),(119,194),(103,181),(98,160),(103,138),(99,118)],bark2), ([(133,74),(145,72),(139,100),(145,125),(138,158),(144,178),(132,192),(122,178),(130,154),(128,125)],bark2), ([(146,89),(156,107),(150,139),(157,151),(148,174),(145,152),(143,138),(148,116)],bark0), ([(110,127),(117,136),(117,157),(124,176),(115,168),(110,151)],bark3), ([(123,71),(128,68),(125,93),(119,111),(117,108)],bark3)]:wood.poly(p,col)
# wood grain following long flowing paths; mask ensures texture inside silhouette
base=wood.copy(name='bark mask')
transparent_index=base.get(0,255)
for i in range(240):
 x=random.randrange(6,251);y=random.randrange(15,243)
 if base.get(x,y) in [base.color(ink),transparent_index]:continue
 col=random.choice([bark0,bark2,bark3,bark1])
 length=random.randrange(3,15)
 for j in range(length):
  xx=x+int(math.sin(j*.25+x)*2);yy=y+j
  if yy<255 and 0<=xx<256 and base.get(xx,yy) not in [transparent_index,base.color(ink)]:wood.set(xx,yy,col)
# sculpted ridge lines
for pts in [[(53,22),(66,42),(89,54),(99,76)],[(110,30),(113,46),(108,62)],[(188,27),(173,51),(154,69),(148,88)],[(153,42),(161,58)],[(26,119),(37,144),(51,147),(65,140),(79,117),(92,109)],[(166,109),(183,128),(196,140),(210,133),(226,115)],[(98,173),(99,195),(88,216),(62,222)],[(109,205),(109,222),(96,236)],[(151,177),(157,199),(178,220),(198,222)],[(144,208),(150,227),(166,237)]]:
 for a,b in zip(pts,pts[1:]):wood.line(*a,*b,bark3)
# dark split fissures
for d in ['M 115 76 L 111 95 L 102 110 L 106 122','M 133 76 L 130 92 L 135 102','M 151 134 L 146 147 L 148 159 L 141 174','M 104 150 L 103 165 L 112 180','M 128 158 L 122 170 L 128 184 L 126 193','M 80 121 L 70 144 L 57 150','M 166 116 L 178 135 L 190 143','M 95 207 L 91 217 L 75 222']:
 wood.path(d,ink,fill=False)
# fine broken grain carved into the wood, with lit edges
for i in range(850):
 x=random.randrange(8,249);y=random.randrange(20,241)
 if base.get(x,y) in [transparent_index,base.color(ink)]:continue
 if 45<x<94 and 112<y<158: dx,dy=1,-1
 elif 163<x<209 and 109<y<153: dx,dy=1,1
 elif y>210: dx,dy=1,0
 else: dx,dy=0,1
 n=random.randrange(2,8)
 col=random.choice([bark0,bark0,bark2,bark3])
 for j in range(n):
  xx=x+j*dx+(1 if j>4 and dx==0 else 0);yy=y+j*dy
  if 1<=xx<254 and 1<=yy<254 and all(base.get(xx+k,yy) not in [transparent_index,base.color(ink)] for k in [-1,0,1]):
   wood.set(xx,yy,col)
   if col==bark0 and j<n-1 and i%3==0:wood.set(xx-1,yy,bark3)
c.blit(wood,0,0)
# bark knots with rim glints
for x,y,rx,ry in [(102,139,4,8),(144,144,4,10),(157,114,3,6),(92,206,3,6),(62,143,5,3),(122,85,3,6)]:
 c.ellipse(x,y,rx+1,ry+1,bark3);c.ellipse(x,y,rx,ry,bark0);c.ellipse(x+1,y, max(1,rx-2),max(1,ry-3),ink);c.set(x-1,y-ry,bark4)
# malevolent recessed face
c.poly([(105,104),(111,99),(121,106),(125,113),(115,116),(107,112)],ink)
c.poly([(133,108),(145,99),(153,100),(149,111),(138,115),(131,114)],ink)
c.poly([(108,105),(113,104),(121,110),(115,112),(110,110)],'#3e713c')
c.poly([(135,110),(145,104),(149,103),(146,110),(137,112)],'#3e713c')
c.line(111,106,119,110,'#98d65e');c.line(112,107,117,109,'#d4f68b')
c.line(137,109,147,105,'#a3e56c');c.line(139,109,145,106,'#e4ffac')
# heavy brows
c.path('M 103 99 L 111 96 L 123 105 M 132 105 L 145 95 L 153 96',bark3,fill=False)
c.poly([(125,109),(120,125),(126,128),(132,125)],bark0)
c.line(126,112,128,122,bark3)
# jagged hollow maw
c.poly([(111,128),(119,132),(124,130),(130,133),(139,127),(146,121),(141,139),(131,148),(121,145),(115,138)],ink)
c.poly([(116,131),(121,134),(121,138)],bark3);c.poly([(134,134),(139,130),(136,138)],bark3)
c.line(123,144,132,146,bark2);c.line(135,146,142,140,bark2)
# moss patches over shoulder tops, joints and roots
for cx,cy,rx,ry in [(92,105,13,5),(163,101,13,5),(112,67,6,4),(146,68,7,4),(72,121,5,5),(46,135,8,3),(193,133,6,4),(103,174,6,4),(152,181,5,5),(80,216,10,3),(173,220,8,3),(152,55,6,3)]:
 for i in range(30):
  x=cx+random.randint(-rx,rx);y=cy+random.randint(-ry,ry)
  if ((x-cx)/rx)**2+((y-cy)/ry)**2<1:
   c.rect(x,y,random.randrange(2,5),random.randrange(1,3),random.choice([moss0,moss1,moss2]))
 for i in range(7):
  x=cx+random.randint(-rx+1,rx-1);y=cy+random.randint(-ry,0);c.rect(x,y,2,1,moss3)
# hanging vines with alternating leaves
for x,y,length,sway in [(73,110,43,5),(88,107,28,-4),(164,105,48,6),(177,114,30,4),(53,139,31,-3),(194,141,28,4),(95,58,27,-3),(157,48,33,3)]:
 points=[]
 for j in range(length):
  xx=x+round(math.sin(j/length*math.pi)*sway); yy=y+j;points.append((xx,yy));c.set(xx,yy,moss0);c.set(xx+1,yy,moss2 if j%5 else moss1)
 for j in range(5,length-2,7):
  xx,yy=points[j];side=1 if j%2 else -1
  c.poly([(xx,yy),(xx+side*4,yy-2),(xx+side*3,yy+2),(xx,yy+3)],moss1);c.set(xx+side*2,yy,moss2)
# ground stones and foreground roots/grasses
for x,y,s in [(20,225,6),(224,215,7),(57,244,7),(204,244,5),(130,239,4),(30,201,4)]:
 c.poly([(x-s,y),(x-2,y-s//2),(x+s-2,y-s//2),(x+s,y+2),(x,y+3)],'#1a2a28');c.line(x-s+1,y-1,x-2,y-s//2,'#5a6650');c.line(x-1,y-s//2,x+s-3,y-s//2,'#6f7654')
for i in range(100):
 x=random.randrange(256);y=random.randrange(202,256)
 if 50<x<211 and y<240:continue
 col=random.choice([moss0,moss1,'#50603c'])
 c.line(x,y,max(0,min(255,x+random.randint(-4,4))),y-random.randint(2,8),col)
# small luminous woodland motes
for x,y in [(57,90),(188,79),(76,174),(179,182),(39,170),(219,157),(124,39),(200,57)]:
 c.set(x,y,'#a2b86b');c.set(x,y+1,'#617e4a')
# foreground silhouette leaves
for x,y in [(4,240),(243,241),(15,250),(230,253)]:
 c.line(x,y,x+4,y-23,ink)
 for j in range(3):
  yy=y-j*6;c.poly([(x+2,yy),(max(0,x-8),yy-7),(max(0,x-3),yy-9),(x+3,yy-2)],'#152b25');c.poly([(x+3,yy-3),(min(255,x+13),yy-11),(min(255,x+13),yy-6)],'#1b3328')
assert c.stats()['colors_used'] <= 120
save('ancient-treant-boss',result)
view(c)
finish(result)
