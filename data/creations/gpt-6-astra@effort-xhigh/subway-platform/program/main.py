# 64 x 64 subway platform, built as crisp, individually placed pixel clusters.
result = new_canvas(64, 64, background='#142739', name='subway_platform')
c = result
P = {
    'ink':'#102333', 'deep':'#1c3548', 'wall':'#294759', 'steel':'#496977',
    'mid':'#678a92', 'light':'#a9c2bf', 'ivory':'#e7e5cd', 'white':'#fff2cf',
    'glass':'#437784', 'glint':'#8dbfc1', 'teal':'#2c6775', 'darkglass':'#214654',
    'train':'#b7c9bd', 'trainshadow':'#789f9c', 'gold':'#edb758', 'amber':'#b57c43',
    'floor':'#3d5868', 'tile':'#486575', 'joint':'#293f51', 'shadow':'#243d4d',
    'skin':'#e8b38c', 'skinshade':'#b97869', 'orange':'#df794f', 'coatlight':'#f5b15d',
    'red':'#a94d50', 'lavender':'#868ca9', 'lavlight':'#b7b6cc', 'pants':'#283647'
}
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(x,y,x2,y2,col): c.line(x,y,x2,y2,P.get(col,col))
def poly(pts,col): c.poly(pts,P.get(col,col))
def px(x,y,col): c.set(x,y,P.get(col,col))

# Receding overhead structure, with long directional light strips.
rect(0,0,64,17,'wall')
poly([(0,0),(63,0),(63,4),(0,9)],'deep')
line(0,9,63,4,'steel')
rect(0,2,26,1,'light'); rect(0,3,20,1,'ivory')
rect(39,1,25,1,'mid'); rect(43,2,21,1,'ivory')
line(0,15,63,15,'steel')
rect(0,16,64,2,'ink')
rect(3,10,3,9,'steel'); rect(59,5,3,14,'steel')
line(3,10,3,18,'mid'); line(59,6,59,18,'mid')

# Suspended station signs: a line number and an unbranded direction board.
rect(9,2,1,4,'ink'); rect(29,2,1,3,'ink'); rect(52,2,1,3,'ink')
rect(3,5,12,10,'ink'); rect(4,5,10,9,'gold')
c.text(7,6,'2',P['ink'])
rect(19,5,38,10,'ink')
line(20,5,55,5,'mid')
c.text(22,7,'EAST',P['ivory'])
line(48,10,54,10,'gold'); line(51,7,54,10,'gold'); line(51,13,54,10,'gold')

# Tunnel and rail bed. The approaching cab remains visible beyond the doors.
rect(0,18,64,25,'ink')
rect(0,38,64,4,'deep')
line(0,40,63,40,'steel')
# Arrival streaks above the train roof.
line(0,18,19,18,'mid'); line(24,18,39,18,'steel')
poly([(0,20),(48,20),(53,21),(57,24),(60,29),(60,35),(57,39),(0,39)],'trainshadow')
poly([(0,20),(48,20),(53,21),(56,24),(0,24)],'train')
line(0,20,47,20,'ivory')
rect(0,24,46,7,'darkglass')
rect(0,25,45,2,'glass')
rect(11,24,2,8,'train'); rect(26,24,2,8,'train'); rect(41,24,3,8,'train')
line(1,28,9,28,'mid'); line(14,28,23,28,'mid'); line(29,28,38,28,'mid')
# Cab windshield, sloped nose, and headlamp.
poly([(47,23),(51,23),(56,27),(57,30),(47,30)],'darkglass')
line(48,24,51,24,'glass'); line(51,24,55,27,'glass')
poly([(57,28),(59,30),(59,35),(56,37),(55,34)],'train')
line(0,32,45,32,'ivory')
rect(0,33,56,2,'orange'); line(0,34,54,34,'red')
line(0,36,55,36,'train')
rect(57,32,3,2,'white'); px(56,33,'gold')
rect(56,37,3,1,'white'); px(59,36,'gold')
rect(0,38,56,2,'darkglass')
# Window light trails emphasize motion without blurring the pixel grid.
line(0,25,8,25,'glint'); line(15,26,24,26,'mid')
line(0,30,17,30,'teal'); line(20,30,34,30,'teal')
line(0,36,8,36,'ivory'); line(12,36,21,36,'light')
line(0,22,13,22,'ivory'); line(18,22,27,22,'ivory')
line(0,23,6,23,'trainshadow'); line(0,37,18,37,'mid')
# Cab divider makes the front of the train distinct from carriage windows.
line(45,22,45,31,'trainshadow')
line(46,23,46,31,'light'); line(48,31,56,31,'train')

# Half-height platform screen doors. Front rails, paired seams and glass reflections.
rect(0,25,64,2,'deep'); line(0,25,63,25,'light')
rect(0,41,64,2,'steel'); line(0,41,63,41,'light')
for x in (0,21,43,62):
    rect(x,26,2,15,'deep')
    line(x,27,x,40,'mid')
for x in (11,32,53):
    line(x,27,x,40,'steel')
    line(x+1,27,x+1,40,'light')
    rect(x-1,34,1,3,'ink'); rect(x+2,34,1,3,'ink')
# Glass sheen as clean diagonal clusters, not noisy texture.
for x in (4,25,46):
    line(x+4,28,x,32,'glint')
    line(x+5,29,x+2,32,'mid')
    line(x+3,37,x+1,39,'mid')
rect(2,35,19,1,'teal'); rect(23,35,20,1,'teal'); rect(45,35,17,1,'teal')
for x in (5,17,26,38,47,59):
    rect(x,35,2,1,'gold')
# Door status lamps.
for x in (1,22,44,63): px(x,24,'gold')

# Platform edge and staggered tiled paving. The perspective opens toward the viewer.
rect(0,43,64,21,'floor')
line(0,43,63,43,'ivory')
rect(0,44,64,3,'gold')
line(0,47,63,47,'joint')
for x in range(1,64,3): px(x,45,'amber')
rect(0,54,64,1,'tile'); rect(0,63,64,1,'tile')
line(0,53,63,53,'joint'); line(0,62,63,62,'joint')
for a,b in ((7,0),(25,22),(43,45),(59,63)):
    line(a,48,b,63,'joint')
line(0,59,8,59,'tile'); line(24,58,28,58,'tile'); line(59,59,63,59,'tile')
# Grounded cast shadows, slightly elongated along the platform.
poly([(3,55),(16,55),(23,58),(10,59),(2,57)],'shadow')
poly([(28,57),(36,56),(44,60),(33,61),(27,59)],'shadow')
poly([(45,57),(56,56),(62,59),(52,60),(44,59)],'shadow')

# Bench: wooden slats on dark metal supports, behind the seated passenger.
rect(2,44,19,1,'ink')
rect(3,45,17,3,'amber')
line(3,45,19,45,'gold'); line(3,47,19,47,'orange')
rect(4,48,1,7,'ink'); rect(18,48,1,7,'ink')
rect(2,50,19,2,'ink'); line(3,50,20,50,'gold')
rect(2,48,2,3,'steel'); rect(20,48,1,4,'steel')
px(4,55,'mid'); px(18,55,'mid')

# Passenger 1: seated, leaning toward a phone, knees bent to the right.
rect(8,37,4,1,'ink'); rect(7,38,6,3,'ink')
rect(9,39,4,3,'skin'); rect(9,39,2,1,'skinshade'); px(13,40,'skin')
rect(9,42,2,1,'skinshade')
poly([(8,42),(11,43),(13,47),(12,50),(7,50),(7,45)],'ink')
poly([(8,43),(10,43),(12,47),(11,49),(8,49)],'lavender')
line(8,44,8,47,'lavlight')
line(11,45,13,47,'lavender'); line(13,47,15,45,'skin')
rect(15,43,2,3,'ink'); px(15,43,'glint')
rect(9,50,7,3,'pants'); rect(14,51,3,5,'pants')
rect(10,52,3,4,'pants'); line(10,52,10,55,'steel')
rect(10,56,4,2,'ink'); rect(14,56,5,2,'ink'); line(15,57,18,57,'light')

# Passenger 2: upright waiting silhouette, a warm coat and a small tote.
rect(31,33,4,1,'ink'); rect(30,34,6,4,'ink')
rect(31,35,4,4,'skin'); rect(31,35,3,1,'skinshade'); px(35,36,'skin')
rect(32,39,2,1,'skinshade')
poly([(30,39),(34,39),(36,42),(37,49),(35,51),(29,51),(28,47),(29,42)],'ink')
poly([(30,40),(34,40),(35,43),(35,49),(29,49),(29,44)],'orange')
line(30,41,30,46,'coatlight'); rect(31,40,3,2,'coatlight')
line(34,43,35,47,'amber'); px(35,48,'skin')
line(29,43,28,47,'orange'); px(28,48,'skin')
rect(30,50,2,7,'pants'); rect(34,50,2,7,'pants')
line(30,51,30,55,'steel')
rect(29,57,4,2,'ink'); rect(34,57,4,2,'ink'); px(37,58,'light')
# The tote sits outside the body so the arm pose reads clearly.
line(26,48,26,50,'ivory'); line(28,48,28,50,'ivory')
rect(25,50,5,4,'ink'); rect(26,50,3,3,'train'); px(26,51,'ivory')

# Passenger 3: walking right, with a backpack and widely separated legs.
rect(50,37,4,1,'ink'); rect(49,38,6,3,'ink')
rect(51,39,4,3,'skin'); px(55,40,'skin'); rect(51,42,2,1,'skinshade')
poly([(49,42),(53,42),(55,45),(53,51),(48,51),(47,46)],'ink')
poly([(50,43),(53,43),(54,46),(52,50),(49,49),(48,46)],'ivory')
line(50,43,49,46,'light')
# Brick-red backpack on the trailing shoulder.
rect(46,44,3,6,'ink'); rect(46,45,3,4,'red'); px(46,45,'orange')
line(49,43,50,47,'red')
# Forward bent arm.
line(53,45,55,48,'train'); line(55,48,57,46,'skin'); px(57,45,'skin')
poly([(49,50),(51,51),(49,54),(47,57),(45,57),(47,53)],'pants')
poly([(51,50),(53,50),(54,54),(57,56),(56,58),(52,55),(50,53)],'pants')
line(52,52,53,54,'steel')
rect(44,57,4,2,'ink'); line(44,58,47,58,'light')
rect(56,57,4,2,'ink'); line(57,58,59,58,'light')

assert tuple(result.stats()['size']) == (64, 64)
assert result.stats()['colors_used'] <= 86
print(result.stats_text())
view(result, scale=8, margin=0)
save('subway_platform', result)
finish(result)
