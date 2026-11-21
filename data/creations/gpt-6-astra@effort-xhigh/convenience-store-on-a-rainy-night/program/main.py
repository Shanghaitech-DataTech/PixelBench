# 64 x 64 convenience store, night rain.
result = new_canvas(64, 64, background='#111a2c', name='Rainy corner store')
c = result
P = {
 'sky':'#111a2c','far':'#17243a','far2':'#202e46','night':'#0c1527',
 'rain':'#334d68','rainhi':'#627e95','wall':'#314453','wallhi':'#47616c',
 'side':'#243444','edge':'#142738','tealdark':'#204d58','teal':'#36828a',
 'mint':'#7cc5b8','mintlight':'#b8e4ce','cream':'#fff0bc','light':'#ffdb87',
 'gold':'#e9ac5f','amber':'#bb7446','brown':'#77513f','interior':'#b98355',
 'shelf':'#6f6152','red':'#bf6461','redlight':'#e59c7a','blue':'#527b8e',
 'glass':'#719e9e','ground':'#1b2c43','puddle':'#253f55','wet':'#355b6b',
 'warmwet':'#756b59','warmhi':'#b39465','yellow':'#f5c559','coatshade':'#cc8c3e',
 'coatlight':'#ffe58a','rubber':'#142336','metal':'#8babb0','bike':'#c77367'
}
def R(x,y,w,h,k): c.rect(x,y,w,h,P.get(k,k))
def L(x,y,X,Y,k): c.line(x,y,X,Y,P.get(k,k))
def S(x,y,k): c.set(x,y,P.get(k,k))
def Q(points,k): c.poly(points,P.get(k,k))
# Quiet city silhouettes behind the shop.
R(0,5,11,31,'far'); R(0,3,5,3,'far')
R(52,7,12,34,'far'); R(57,2,7,8,'far2'); R(60,0,4,5,'far2')
R(2,9,2,3,'wall'); R(7,9,2,3,'far2'); R(2,17,2,4,'far2')
R(57,9,2,3,'wall'); R(61,9,2,3,'far'); R(61,17,2,4,'wall')
L(0,8,25,11,'night'); L(25,11,49,9,'night'); L(49,9,63,6,'night')
# Background rain: separated, short diagonal strokes.
for x,y,h in [(3,0,3),(15,3,4),(24,0,3),(35,4,3),(44,0,4),(51,3,2),(11,10,3),(29,7,3),(41,9,3),(62,25,4),(2,29,4),(59,30,3),(1,37,2)]:
 L(x,y,x-1,y+h,'rain')
# Pavement and curb plane.
R(0,41,64,23,'ground')
Q([(0,45),(43,42),(63,44),(63,48),(0,51)],'puddle')
L(0,49,63,46,'wet')
# Reflected light arranged in horizontal broken bands.
c.ellipse(23,56,19,5,P['puddle'])
c.ellipse(44,53,12,4,P['puddle'])
R(12,49,17,2,'warmwet'); R(14,52,18,1,'warmhi'); R(12,54,16,2,'warmwet')
R(16,54,9,1,'gold'); R(20,57,12,1,'warmwet'); R(15,59,10,1,'wet')
R(34,48,12,2,'warmwet'); R(36,50,10,1,'warmhi'); R(33,53,10,1,'warmwet')
R(38,55,9,1,'warmhi'); R(41,58,7,1,'warmwet')
R(3,55,8,1,'teal'); R(6,56,7,1,'wet'); R(8,59,6,1,'wet')
R(28,60,11,1,'wet'); R(31,61,6,1,'teal'); R(48,51,8,1,'wet')
R(53,56,8,1,'wet'); R(50,60,7,1,'puddle'); R(0,61,5,1,'puddle')
# Store shell: shaded narrow right-hand return and illuminated front.
Q([(53,16),(60,20),(60,43),(54,46),(53,22)],'night')
Q([(54,22),(59,24),(59,42),(54,44)],'side')
L(58,25,58,41,'wall')
R(6,23,49,23,'edge'); R(8,24,45,20,'wall')
R(8,25,2,18,'wallhi'); R(52,25,2,19,'wallhi')
R(7,43,47,3,'side'); R(7,43,47,1,'wallhi')
# Overhanging roof and fascia.
Q([(5,16),(11,13),(51,13),(59,18),(54,21),(5,20)],'edge')
Q([(6,16),(12,14),(51,14),(55,16)],'wallhi')
R(5,17,50,7,'tealdark'); R(5,17,50,1,'mint')
R(7,18,46,4,'teal')
Q([(55,17),(59,19),(59,24),(55,23)],'tealdark')
R(5,23,50,2,'edge'); R(7,23,46,1,'gold')
# Generic opening-hours sign, no brand.
R(13,17,21,6,'cream')
glyphs={'2':['111','001','111','100','111'],'4':['101','101','111','001','001'],'H':['101','101','111','101','101']}
for i,ch in enumerate('24H'):
 for yy,row in enumerate(glyphs[ch]):
  for xx,v in enumerate(row):
   if v=='1': S(17+i*5+xx,18+yy,'tealdark')
R(39,19,10,1,'mint'); R(39,21,10,1,'mint')
# Window recess and warm interior.
R(10,25,22,17,'night'); R(11,26,20,14,'light')
R(11,26,20,2,'cream'); R(11,28,20,2,'gold')
R(11,30,20,10,'interior')
# Shelves, bottles and packaged groceries.
R(12,30,18,1,'cream')
for x,h,col in [(12,3,'red'),(16,2,'tealdark'),(20,3,'mint'),(25,2,'redlight'),(28,3,'cream')]:
 R(x,32-h,2,h,col)
R(11,33,20,1,'shelf'); R(11,32,20,1,'gold')
for x,h,col in [(12,3,'cream'),(16,2,'red'),(20,3,'teal'),(24,2,'cream'),(28,3,'gold')]:
 R(x,37-h,2,h,col)
R(11,37,20,1,'shelf'); R(11,38,20,2,'gold')
# Blue reflections on the glass, mullion, sill.
L(12,28,12,31,'cream'); L(13,28,15,28,'cream')
L(28,27,30,29,'cream'); L(28,38,30,40,'light')
R(21,26,1,15,'brown'); R(22,26,1,15,'wallhi')
R(10,40,22,2,'edge'); R(10,40,22,1,'mint')
# Entry, lit from behind, with a slightly open glass door.
R(33,25,13,20,'night'); R(34,26,11,17,'light')
R(34,26,11,2,'cream'); R(34,28,3,15,'gold')
R(35,30,2,8,'interior'); R(34,42,11,2,'cream')
Q([(39,27),(44,26),(44,43),(39,42)],'glass')
Q([(40,28),(43,27),(43,41),(40,40)],'light')
L(40,29,42,31,'cream'); L(43,27,43,41,'gold')
R(43,34,1,4,'brown'); S(43,34,'cream')
R(33,44,13,2,'wallhi'); R(34,44,11,1,'light')
# Narrow second window.
R(47,25,5,16,'edge'); R(48,26,3,13,'light')
R(48,26,3,2,'cream'); R(48,31,3,1,'brown'); R(49,29,2,2,'red')
R(48,36,3,1,'brown'); R(48,34,2,2,'teal'); R(47,40,5,1,'mint')
# Little exterior utility panel on the side wall.
R(56,29,2,7,'edge'); S(56,30,'blue'); S(56,33,'blue')
# Parked bicycle, dark outline with restrained bright spokes.
for x in [10,25]:
 c.circle(x,49,5,P['night'],fill=False)
 c.circle(x,49,4,P['metal'],fill=False)
 c.circle(x,49,3,P['ground'],fill=False)
 L(x-2,47,x+2,51,'rain'); L(x-2,51,x+2,47,'rain')
 S(x,49,'mintlight')
# Main diamond frame.
L(10,49,14,43,'bike'); L(14,43,19,49,'bike'); L(19,49,10,49,'bike')
L(14,43,22,43,'bike'); L(22,43,19,49,'bike'); L(22,43,25,49,'metal')
L(22,43,21,40,'metal'); L(21,40,24,40,'metal'); S(24,41,'night')
L(14,43,13,41,'metal'); L(11,41,15,41,'night'); L(12,40,15,40,'metal')
S(19,49,'cream'); L(19,49,20,51,'metal'); L(19,51,21,51,'night')
L(7,44,11,44,'metal'); L(7,45,7,47,'wallhi')
# Umbrellas in a small open wire rack to the right of the entrance.
# Crooked handles and folded fabric.
L(48,35,49,42,'metal'); L(47,35,47,34,'metal'); L(47,34,48,34,'metal')
Q([(47,36),(49,36),(50,42),(49,44)],'red')
L(48,36,49,41,'redlight')
L(52,34,52,42,'metal'); L(52,34,53,33,'metal'); S(54,34,'metal')
Q([(51,36),(53,36),(53,42),(52,44)],'blue'); L(51,36,52,41,'mint')
L(55,36,54,43,'metal'); S(56,35,'metal'); S(55,35,'metal')
Q([(54,38),(56,38),(54,44),(53,43)],'teal')
R(47,42,10,1,'night'); R(47,43,1,4,'metal'); R(56,43,1,4,'wallhi')
L(48,46,55,46,'metal'); L(50,43,50,46,'wallhi'); L(53,43,53,46,'wallhi')
# Person stepping into the store, viewed from behind.
# A shadowed silhouette separates the yellow coat from the warm interior.
Q([(35,36),(40,36),(42,38),(43,36),(44,36),(44,39),(42,41),(43,44),(42,45),(35,45),(34,43),(33,42),(34,39)],'edge')
# Boots staggered to show the raised foot.
R(36,44,3,4,'night'); R(39,43,3,3,'night')
R(36,47,4,1,'rubber'); R(40,45,3,1,'rubber'); S(40,44,'blue')
Q([(36,36),(40,36),(42,39),(41,41),(42,44),(35,44),(35,40)],'coatshade')
Q([(36,37),(39,36),(40,39),(40,43),(35,43)],'yellow')
L(35,38,34,41,'coatlight'); S(34,42,'amber')
L(41,38,43,37,'yellow'); S(43,36,'cream')
L(38,39,38,42,'coatlight'); L(36,43,40,43,'gold')
# Rounded rain hood and its seam.
Q([(36,31),(39,31),(41,33),(42,35),(41,37),(39,38),(35,38),(34,35),(35,33)],'brown')
Q([(36,32),(39,32),(41,34),(41,36),(39,38),(36,37),(35,35),(35,34)],'coatshade')
Q([(36,33),(38,32),(40,34),(40,36),(38,37),(36,36)],'yellow')
L(36,34,37,33,'coatlight'); L(37,33,38,33,'coatlight'); S(40,35,'brown')
# Hood folds and the dark sleeve seam read as a figure from behind.
L(36,37,39,38,'coatshade'); S(35,39,'coatshade'); L(40,40,40,42,'coatshade')
# Sparse glints sit over the merchandise on the shop glass.
L(13,27,15,29,'cream'); S(13,29,'light')
L(24,34,26,36,'light'); L(24,35,25,36,'gold')
# Water dropping from the eaves; a few foreground streaks.
L(5,25,5,28,'rainhi'); S(5,30,'blue')
L(59,25,59,27,'rainhi'); S(58,29,'rain')
for x,y,h in [(1,19,3),(4,34,3),(62,35,4),(30,44,3),(59,48,3),(3,48,2),(8,57,2),(48,58,3),(26,58,2),(61,59,3),(31,2,2),(46,6,3),(19,7,2)]:
 L(x,y,x-1,y+h,'rainhi' if y>42 else 'rain')
# Ripples and isolated droplets on the wet street.
L(1,53,4,53,'wet'); S(2,52,'rainhi')
L(53,53,58,53,'blue'); L(54,54,57,54,'puddle'); S(56,52,'rainhi')
L(33,58,36,58,'wet'); S(35,57,'metal')
L(10,62,16,62,'wet'); S(13,61,'blue')
L(59,44,62,44,'wet'); S(61,43,'rainhi')
# A few clean glints in the broken warm reflection.
R(18,51,3,1,'light'); R(24,54,4,1,'warmhi'); R(37,52,3,1,'gold')
view(result, scale=8, margin=0)
save('rainy_corner_store', result)
finish(result)
