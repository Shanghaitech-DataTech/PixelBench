import random, math
random.seed(18)
c=new_canvas(256,256,name='ancient_dragon_battle')
# restrained sunset palette
ink='#191724'; deep='#282334'; stone='#4c4651'; mid='#69616a'; light='#938077'; gold='#f6b761'
for y in range(256):
 col=('#382b49' if y<25 else '#57334c' if y<49 else '#85404f' if y<73 else '#b7514f' if y<99 else '#dc7157' if y<123 else '#eb9564' if y<151 else '#75545a' if y<188 else '#352d3b')
 c.line(0,y,255,y,col)
c.circle(190,94,31,'#f6b761'); c.circle(190,94,26,'#ffca79')
# long broken sunset clouds
for x,y,w in [(4,26,42),(25,31,54),(135,22,75),(171,32,65),(3,66,37),(205,54,49),(96,114,30),(157,133,78)]:
 c.rect(x,y,w,3,'#774052'); c.rect(x+8,y-2,max(3,w-16),2,'#774052')
# far mountain ranges
c.poly([(0,135),(19,115),(29,124),(48,96),(64,119),(76,107),(99,135),(116,122),(143,143),(166,126),(182,138),(208,116),(231,135),(250,113),(255,119),(255,179),(0,179)],'#7c525e')
c.poly([(0,149),(22,137),(39,145),(62,128),(93,157),(119,142),(141,152),(166,144),(189,161),(222,137),(255,150),(255,188),(0,188)],'#584451')
c.poly([(42,111),(48,96),(59,114),(49,108)],'#b07878')
# rising smoke behind keep
for cx,cy,r in [(147,142,16),(148,125,13),(139,113,14),(128,99,14),(118,88,12),(120,74,11),(177,151,16),(184,132,14),(179,116,11),(191,105,13),(204,95,10),(214,90,9)]:
 c.circle(cx,cy,r,'#44333f');c.circle(cx-3,cy-3,max(2,r-4),'#57404b')
# castle silhouette and masonry
c.poly([(50,181),(50,158),(66,158),(66,137),(77,137),(77,125),(91,125),(91,137),(102,137),(102,117),(115,104),(128,117),(128,141),(150,141),(150,125),(165,125),(165,145),(181,145),(181,158),(202,158),(202,200),(43,200)],ink)
def tower(x,y,w,h):
 c.rect(x,y,w,h,ink);c.rect(x+2,y+3,w-4,h-3,stone);c.rect(x+3,y+3,4,h-3,mid);c.rect(x+w-6,y+3,4,h-3,'#39333f')
 for yy in range(y+8,y+h,7):
  c.line(x+2,yy,x+w-3,yy,'#37313f')
  for xx in range(x+5+(3 if yy%2 else 0),x+w-3,8):c.line(xx,yy-5,xx,yy, '#39333f')
 for xx in range(x,x+w,7):c.rect(xx,y-5,5,8,ink);c.rect(xx+1,y-4,3,5,mid)
 c.line(x+1,y+2,x+w-2,y+2,light)
 for yy in range(y+12,y+h-5,20):
  c.rect(x+w//2-2,yy,4,9,ink);c.set(x+w//2,yy+2,'#b65c43')
tower(102,117,28,71);tower(67,142,29,56);tower(150,141,27,60)
c.poly([(99,116),(115,94),(133,116)],ink);c.poly([(103,114),(115,99),(127,114)],'#654552');c.line(115,96,115,84,ink)
c.poly([(116,84),(135,87),(125,92),(116,91)],'#b94b49')
# fire tongues, dark red perimeter and luminous cores
def fire(x,y,h,w=8):
 c.poly([(x-w,y),(x-w-2,y-h//3),(x-w//2,y-h//2),(x-2,y-h),(x+2,y-h//2),(x+w//2,y-h*3//4),(x+w,y-h//3),(x+w,y)],'#a6433d')
 c.poly([(x-w+2,y),(x-w//2,y-h//3),(x,y-h+4),(x+2,y-h//3),(x+w-1,y-h//2),(x+w-2,y)],'#ef783c')
 c.poly([(x-3,y),(x-3,y-6),(x+1,y-h//2),(x+4,y)],'#ffd17a')
for v in [(140,166,34,10),(134,153,24,7),(159,144,28,7),(178,171,32,10),(85,147,22,6),(110,127,21,5)]:fire(*v)
# battlement foreground wall
c.rect(31,180,190,38,ink);c.rect(33,184,186,32,stone)
for y in range(188,218,7):
 c.line(33,y,219,y,'#36313e')
 for x in range(35+(5 if y%2 else 0),219,12):c.line(x,y-5,x,y,'#36313e');c.line(x+1,y-5,x+6,y-5,'#5b535c')
for x in range(32,222,11):
 c.rect(x,174,7,10,ink);c.rect(x+1,175,5,7,mid);c.line(x+1,175,x+5,175,light)
c.rect(32,184,189,3,'#817079');c.line(32,187,220,187,ink)
# gate arch
c.path('M 110 217 L 110 202 Q 124 182 138 202 L 138 217 Z',ink)
c.path('M 114 217 L 114 203 Q 124 189 134 203 L 134 217 Z','#3b2830')
for x in range(115,135,4):c.line(x,201,x,216,'#77504b')
c.line(114,208,134,208,ink)
tower(26,170,22,51);tower(205,166,24,57)
# burning right tower
fire(216,169,30,8)
# dragon: huge angular wings and sinuous tail, rim-lit in sunset
c.path('M 109 76 C 85 85 75 98 54 96 C 39 94 39 83 48 79 C 39 88 51 91 60 87 L 90 68 Z',ink)
c.path('M 104 74 C 83 82 72 94 53 92', '#74504c',False)
# left wing high sweep
c.poly([(115,65),(96,45),(72,26),(38,13),(46,27),(51,44),(48,60),(61,51),(72,54),(77,66),(88,60),(97,70),(105,78)],ink)
c.poly([(107,64),(93,47),(72,30),(43,17),(55,33),(58,47),(62,46),(74,50),(80,60),(87,55)],'#713e48')
c.poly([(48,21),(72,32),(97,57),(62,40)],'#a85a52')
c.line(42,16,72,29,'#b66a59');c.line(72,29,110,67,'#d38a65')
c.line(72,30,76,54,ink);c.line(73,33,56,46,ink);c.line(88,46,88,58,ink)
# right wing rising and extended
c.poly([(113,64),(130,38),(156,17),(184,9),(174,23),(168,41),(170,56),(158,48),(146,52),(137,64),(127,64),(121,77)],ink)
c.poly([(120,63),(134,40),(157,21),(179,12),(168,29),(164,48),(157,43),(144,48),(133,59)],'#824650')
c.poly([(134,41),(157,22),(174,16),(154,34),(124,62)],'#b26658')
c.line(119,65,133,39,'#cc8766');c.line(133,39,158,19,'#cc8766');c.line(158,19,181,11,'#cc8766')
c.line(155,24,158,44,ink);c.line(154,26,140,52,ink)
# body and neck
c.path('M 89 71 Q 101 57 119 61 L 133 66 Q 142 68 145 57 L 148 49 L 158 47 L 165 51 L 172 53 L 171 59 L 159 61 Q 157 80 142 84 L 120 81 L 109 86 L 96 82 Z',ink)
c.path('M 94 72 Q 104 62 119 65 L 135 71 Q 149 73 150 55 L 157 51 L 164 55 L 158 58 Q 154 77 142 79 L 119 76 L 106 80 Z','#4d4547')
c.path('M 109 65 L 120 66 L 136 73 Q 151 76 154 59 L 158 59 Q 156 81 141 82 L 121 79 Z','#9b755d')
for x,y in [(100,68),(109,66),(118,67),(128,70),(138,74)]:c.line(x,y,x+3,y,'#8e7864')
for x,y in [(121,77),(128,79),(135,80),(143,79),(149,75)]:c.line(x,y,x+1,y+3,'#4d4547')
# horns and back spikes
c.poly([(148,51),(144,40),(152,47),(156,48),(161,40),(160,51)],ink)
c.line(146,42,150,48,'#c8a47a')
for x,y in [(91,69),(99,64),(108,61),(118,62),(132,66)]:c.poly([(x,y+2),(x-3,y-6),(x+5,y)],ink)
c.set(162,53,'#ffd87c');c.set(163,53,'#fff0a6');c.line(164,58,170,57,'#ad795c')
# claws
for pts in [[(115,77),(116,88),(126,94),(130,93),(123,86),(125,78)],[(98,76),(91,86),(98,91),(105,89),(99,86),(106,80)]]:c.poly(pts,ink)
for x,y in [(127,92),(101,89)]:
 c.line(x,y,x+4,y+3,'#d7ad7a');c.line(x-3,y+1,x,y+4,'#d7ad7a')
# exhaled fire diagonal toward castle
c.poly([(171,57),(179,61),(184,70),(192,77),(194,88),(204,100),(200,110),(192,102),(185,98),(182,86),(178,78),(176,68)],'#a8443e')
c.poly([(171,57),(180,65),(182,73),(189,80),(190,90),(199,102),(193,98),(185,94),(182,83),(178,77)],'#ef783c')
c.poly([(172,58),(180,70),(181,78),(187,86),(190,95),(184,89),(179,80)],'#ffcf74')
# foreground rolling battlefield
c.poly([(0,220),(29,217),(57,227),(99,220),(142,223),(178,218),(208,224),(238,215),(255,219),(255,255),(0,255)],'#302b36')
c.poly([(0,242),(37,235),(80,245),(126,231),(165,241),(207,233),(255,239),(255,255),(0,255)],'#242330')
# siege towers at sides
for x,y in [(4,174),(233,169)]:
 c.poly([(x,y+54),(x+4,y),(x+17,y),(x+23,y+54)],ink)
 c.rect(x+3,y+1,17,16,'#62454a');c.rect(x+2,y-3,19,5,ink)
 for xx in [x+4,x+17]:c.line(xx,y+13,xx-2 if xx==x+4 else xx+3,y+52,'#95705c')
 for yy in [y+20,y+35,y+48]:
  c.line(x+2,yy,x+21,yy,'#936752');c.line(x+4,yy-13,x+19,yy,'#63474a');c.line(x+19,yy-13,x+4,yy,'#63474a')
 c.rect(x+6,y+3,10,7,ink)
 for xx in [x+3,x+19]:c.circle(xx,y+54,4,ink);c.set(xx,y+54,'#806351')
# tiny defenders and ranked soldiers
def knight(x,y,side=False):
 c.line(x+5,y-13,x+5,y+7,'#ad8d72');c.poly([(x+3,y-12),(x+5,y-17),(x+7,y-12)],'#b4a39b')
 c.rect(x-2,y-5,5,5,ink);c.rect(x-1,y-5,3,3,'#8f9192');c.set(x-1,y-5,'#d2c4ac');c.line(x-1,y-1,x+2,y-1,ink)
 c.rect(x-2,y,5,7,'#58606c');c.line(x-2,y+1,x+4,y+2,'#8b8585');c.line(x-1,y+7,x-2,y+10,ink);c.line(x+2,y+7,x+3,y+10,ink)
 c.poly([(x-5,y+1),(x,y),(x,y+7),(x-3,y+9),(x-5,y+6)],ink)
 c.poly([(x-4,y+2),(x-1,y+1),(x-1,y+6),(x-3,y+7),(x-4,y+5)],'#a75550' if side else '#596c7b');c.line(x-3,y+2,x-3,y+6,'#c0a77e')
for x,y in [(53,171),(65,171),(98,171),(146,171),(190,171),(202,171),(32,164)]:knight(x,y)
for y,start in [(226,55),(237,72),(250,46)]:
 for x in range(start,206,14):knight(x,y,True)
# flags amid formations
for x,y in [(49,222),(204,230)]:
 c.line(x,y-27,x,y+9,'#a58668');c.poly([(x+1,y-26),(x+16,y-24),(x+12,y-18),(x+17,y-13),(x+1,y-16)],ink);c.poly([(x+2,y-25),(x+13,y-23),(x+10,y-18),(x+2,y-18)],'#ab4c49')
# arrows crossing sunset
for x,y,dx,dy in [(22,101,15,-9),(44,116,13,-11),(65,104,10,-13),(203,120,-11,-13),(224,104,-12,-9),(33,137,12,-8),(227,140,-10,-11),(73,126,8,-12)]:
 c.line(x,y,x+dx,y+dy,ink);c.line(x,y,x-3,y, '#d2b18b');c.line(x+dx,y+dy,x+dx- (3 if dx>0 else -3),y+dy+1,ink)
# embers and ground debris
for i in range(125):
 x=random.randrange(60,232);y=random.randrange(95,219)
 if random.random()<.55 and x>120:c.set(x,y,random.choice(['#f6b761','#ef783c','#b85644']))
for i in range(100):
 x=random.randrange(256);y=random.randrange(225,256)
 if random.random()<.6:c.line(x,y,min(255,x+2),y,random.choice(['#4a3a40','#65504a','#191724']))
view(c)
finish(c)
