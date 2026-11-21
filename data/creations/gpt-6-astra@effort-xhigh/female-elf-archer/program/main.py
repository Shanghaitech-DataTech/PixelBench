# 64x64 RPG sprite: woodland elf archer
result = new_canvas(64, 64, name='elf_archer')
c = result
P = {
'ink':'#192f30','deep':'#214239','hairdark':'#245542','hairshade':'#2e704c',
'hair':'#3d945b','hairlight':'#68b976','hairshine':'#a0d68b',
'clothdeep':'#42664b','clothshade':'#6b9860','cloth':'#a1ca7d','clothlight':'#cbe698','clothshine':'#e6f1b5',
'skinline':'#684c43','skindark':'#b77c60','skinshade':'#d69c75','skin':'#efbd8a','skinlight':'#ffdbab',
'leatherdark':'#473d33','leathershade':'#70503b','leather':'#956942','leatherlight':'#c39859',
'gold':'#dfbe72','goldlight':'#f9dfa0','eye':'#254b45','white':'#f5edce',
}
def poly(points, col): c.poly(points, P.get(col,col))
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(x1,y1,x2,y2,col): c.line(x1,y1,x2,y2,P.get(col,col))
def dot(x,y,col): c.set(x,y,P.get(col,col))

# A compact ground contact shadow.
c.ellipse(32,61,13,2,'#203c3d55')
c.ellipse(33,61,9,1,'#203c3d88')

# Bow carried behind the left shoulder: wood limbs and a taut fine string.
line(17,10,20,48,'leatherdark')
line(18,12,21,47,'gold')
poly([(17,9),(15,10),(12,14),(10,19),(9,25),(9,31),(11,38),(14,43),(19,48),(21,49),(21,46),(17,42),(14,36),(12,30),(12,24),(13,18),(16,13),(18,11)],'ink')
line(16,11,12,18,'leatherlight')
line(12,18,10,25,'leatherlight')
line(10,25,10,31,'gold')
line(10,31,13,39,'leatherlight')
line(13,39,19,46,'leatherlight')
line(19,46,20,47,'goldlight')
line(15,13,12,20,'goldlight')
line(11,23,11,29,'leather')
rect(10,27,3,6,'leathershade')
line(10,28,12,29,'gold')
line(10,31,12,32,'leatherlight')
dot(17,10,'goldlight')

# Three feathered arrows rise above a leather quiver.
for x,y in [(43,7),(47,6),(51,9)]:
    line(x,y+2,x-5,y+20,'ink')
    line(x,y+2,x-4,y+18,'leatherlight')
    poly([(x,y),(x-3,y+2),(x-3,y+7),(x-1,y+5),(x+1,y+2)],'ink')
    line(x-1,y+2,x-2,y+5,'clothlight')
    dot(x,y+1,'white')
    dot(x-3,y+4,'hairlight')
poly([(42,20),(49,22),(44,37),(40,39),(36,35)],'ink')
poly([(42,22),(47,23),(43,35),(40,37),(38,34)],'leathershade')
poly([(42,23),(44,23),(40,35),(39,34)],'leather')
line(46,25,42,36,'leatherdark')
poly([(41,19),(49,21),(49,24),(40,22)],'leatherdark')
line(42,20,48,22,'leatherlight')
line(40,22,47,24,'gold')

# Large back mass of long green hair, with separated flowing ends.
poly([(28,4),(35,4),(40,6),(43,10),(42,17),(38,23),(38,31),(35,38),(35,43),(31,47),(27,45),(24,47),(19,46),(21,42),(17,44),(14,43),(18,38),(19,32),(18,24),(19,16),(21,10),(24,6)],'ink')
poly([(25,8),(31,6),(37,7),(39,13),(35,23),(35,33),(32,40),(33,44),(29,43),(25,45),(22,44),(24,39),(19,42),(17,42),(21,35),(21,27),(20,23),(22,14)],'hairshade')
poly([(25,9),(30,7),(33,10),(28,20),(26,28),(26,36),(23,41),(20,42),(23,34),(22,27),(22,20)],'hair')
poly([(26,12),(28,11),(25,22),(24,30),(25,35),(23,39),(23,28),(23,21)],'hairlight')
poly([(30,22),(34,18),(33,30),(30,37),(30,43),(27,44),(28,36)],'hairdark')
line(21,27,22,32,'hairshine')
line(19,39,17,42,'hairlight')
dot(23,43,'hairshine')

# Far leg and boot, then the weight-bearing near leg.
poly([(34,43),(40,43),(40,49),(39,53),(41,57),(45,59),(45,61),(37,61),(35,58),(34,51)],'ink')
poly([(35,45),(39,45),(38,52),(36,53),(35,50)],'skinshade')
line(37,46,37,51,'skin')
poly([(35,52),(39,51),(40,56),(42,58),(44,59),(43,60),(37,60),(36,57)],'clothdeep')
poly([(37,53),(38,53),(38,56),(40,59),(38,59),(37,57)],'clothshade')
line(36,52,39,52,'leatherlight')
line(37,56,39,55,'leather')
line(38,60,44,60,'leatherdark')
poly([(27,43),(34,44),(34,49),(32,55),(32,58),(34,60),(33,62),(25,62),(24,60),(27,56),(26,50)],'ink')
poly([(28,45),(32,45),(32,49),(30,54),(28,54),(28,50)],'skin')
line(28,46,28,50,'skinlight')
line(32,46,31,51,'skinshade')
poly([(27,52),(32,53),(31,58),(33,60),(32,61),(26,61),(26,59),(28,56)],'clothdeep')
poly([(28,53),(30,54),(29,58),(27,60),(29,60),(31,58),(31,55)],'clothshade')
line(27,52,31,53,'gold')
line(28,55,31,55,'leather')
line(27,58,30,58,'leatherlight')
line(26,61,32,61,'leatherdark')
dot(27,59,'clothlight')

# Far arm, turned away, in a short mint sleeve and archery bracer.
poly([(38,26),(41,28),(43,33),(42,37),(40,41),(38,42),(36,39),(38,35),(36,30)],'ink')
poly([(39,28),(40,29),(42,33),(40,35),(37,32)],'clothshade')
line(40,30,41,33,'cloth')
poly([(39,34),(41,34),(40,38),(38,39),(37,38)],'skinshade')
poly([(39,36),(41,36),(40,40),(38,41),(37,39)],'leathershade')
line(39,36,41,36,'leatherlight')
poly([(37,40),(39,41),(39,43),(37,44),(36,42)],'skin')
dot(37,41,'skinlight')

# Neck and fitted light green tunic.
poly([(29,20),(36,20),(36,24),(39,26),(39,31),(37,36),(38,40),(41,46),(37,48),(33,46),(30,49),(24,46),(26,40),(26,35),(23,30),(24,26),(29,24)],'ink')
poly([(30,21),(35,21),(35,25),(33,28),(29,26)],'skinshade')
poly([(31,22),(34,22),(34,25),(32,26),(30,25)],'skin')
poly([(27,25),(29,25),(32,28),(35,25),(37,26),(38,30),(36,36),(37,40),(28,40),(28,34),(25,29)],'cloth')
poly([(26,27),(28,26),(31,29),(29,34),(30,38),(28,38),(27,33),(25,30)],'clothlight')
poly([(36,28),(38,28),(38,31),(36,35),(36,39),(33,39),(33,35)],'clothshade')
line(27,27,30,29,'clothshine')
line(30,29,32,30,'clothdeep')
line(32,30,35,27,'clothdeep')
dot(32,31,'goldlight')
# Leaf-shaped skirt panels.
poly([(28,39),(36,39),(39,45),(36,47),(33,44),(30,47),(25,45)],'clothshade')
poly([(28,40),(32,40),(31,45),(29,47),(26,45)],'clothlight')
poly([(33,40),(35,40),(37,44),(36,46),(33,43)],'cloth')
line(26,45,29,47,'gold')
line(29,47,31,45,'goldlight')
line(36,46,38,45,'gold')
line(32,41,32,44,'clothdeep')

# Diagonal quiver harness and waist belt.
poly([(36,25),(38,26),(29,38),(27,37)],'leatherdark')
line(36,26,28,37,'leather')
line(36,27,29,37,'leatherlight')
poly([(27,37),(32,38),(37,37),(38,39),(32,41),(27,39)],'leatherdark')
line(28,38,32,39,'leather')
line(33,39,37,38,'leatherlight')
rect(31,38,3,3,'gold')
dot(32,39,'leatherdark')
# Belt pouch on the near hip.
poly([(25,38),(28,38),(29,42),(27,44),(24,43),(24,40)],'ink')
rect(25,40,3,3,'leather')
line(25,40,27,40,'leatherlight')
dot(26,41,'goldlight')

# Near arm hangs forward, with cuff, bracer and a small articulated hand.
poly([(25,26),(28,28),(28,31),(26,34),(26,38),(25,42),(26,45),(24,47),(21,45),(21,41),(22,36),(21,31),(22,28)],'ink')
poly([(24,27),(26,28),(27,31),(25,34),(22,32),(22,30)],'cloth')
poly([(24,28),(25,28),(25,31),(23,32),(22,31)],'clothlight')
line(23,33,25,34,'gold')
poly([(23,34),(25,35),(25,38),(23,40),(22,39)],'skin')
line(23,35,23,38,'skinlight')
poly([(22,38),(25,39),(24,43),(22,42)],'leather')
line(22,38,25,39,'leatherdark')
line(22,39,24,40,'leatherlight')
line(22,41,24,42,'leatherdark')
poly([(22,43),(24,43),(25,45),(24,46),(22,45)],'skin')
dot(22,43,'skinlight')
dot(24,45,'skinshade')

# Face angled right: broad near cheek and a small far plane.
poly([(29,10),(36,9),(40,11),(41,15),(41,17),(43,18),(42,20),(40,20),(39,23),(35,25),(31,24),(28,21),(27,16)],'skinline')
poly([(30,11),(36,10),(39,12),(40,16),(40,18),(42,18),(41,19),(39,20),(38,23),(35,24),(31,22),(29,20),(28,16)],'skin')
poly([(30,12),(35,11),(38,12),(39,15),(38,18),(39,20),(36,22),(33,22),(30,19)],'skinlight')
poly([(29,16),(31,19),(32,22),(35,24),(31,22),(29,20)],'skinshade')
line(39,20,40,19,'skinshade')
# Exposed long pointed ear, angled back from the near temple.
poly([(29,15),(26,14),(21,12),(22,16),(25,19),(28,19),(30,17)],'skinline')
poly([(28,16),(24,15),(22,13),(23,16),(26,18),(28,18)],'skin')
line(24,15,27,17,'skindark')
line(23,14,27,15,'skinlight')
dot(28,19,'gold')
dot(28,20,'goldlight')
# Eyes and restrained expression.
line(33,15,36,15,'hairdark')
dot(37,16,'skindark')
line(33,17,36,17,'eye')
line(33,16,35,16,'white')
dot(35,16,'eye')
dot(34,16,'white')
dot(36,16,'eye')
line(39,15,40,15,'hairdark')
dot(39,17,'eye')
dot(40,16,'white')
dot(37,19,'skinshade')
line(36,21,38,21,'skindark')
dot(36,22,'skinlight')

# Crown, swept fringe and locks in front of the shoulder.
poly([(22,12),(23,8),(27,5),(33,4),(38,5),(41,8),(42,12),(41,15),(39,14),(38,10),(35,10),(33,13),(29,16),(28,14),(26,13),(24,14)],'hairdark')
poly([(23,11),(25,8),(29,6),(34,5),(38,6),(40,9),(40,12),(38,10),(34,9),(31,13),(28,14),(27,12),(24,13)],'hair')
poly([(24,10),(27,7),(32,6),(35,6),(33,8),(29,9),(27,11)],'hairlight')
line(27,7,31,6,'hairshine')
line(25,9,26,8,'hairshine')
poly([(32,10),(35,8),(38,8),(36,9),(33,12),(29,14)],'hairlight')
line(37,6,39,8,'hairlight')
dot(40,10,'hairlight')
# A tapered lock under the ear frames the body.
poly([(27,20),(29,21),(30,25),(29,29),(27,32),(28,28),(27,25),(25,23)],'hairdark')
poly([(27,21),(28,23),(29,26),(28,29),(28,25),(26,23)],'hairlight')
dot(27,22,'hairshine')
# Gold leaf hair clasp.
poly([(23,10),(25,9),(27,10),(25,12),(23,12)],'leatherdark')
line(24,10,26,10,'goldlight')
dot(24,11,'gold')

assert result.stats()['size'] == (64, 64) or result.stats()['size'] == [64, 64]
assert result.stats()['colors_used'] <= 86
print(result.stats_text())
view(result, scale=8, margin=0)
save('female-elf-archer', result)
finish(result)
