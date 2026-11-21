result = new_canvas(32,32,name='skeleton_grunt')
c=result
ink='#252633'
joint='#41404a'
shade='#77796e'
bone='#c4c1a0'
light='#eee5ba'
white='#fff2cc'
wooddark='#49302b'
wood='#875133'
woodlight='#b47743'
metal='#78868b'
shine='#c7d9cf'
# crouched legs with dark sockets
c.poly([(12,21),(16,21),(15,25),(13,27),(13,29),(8,29),(8,27),(11,26)],ink)
c.line(13,22,13,25,bone)
c.set(12,25,shade)
c.rect(10,26,3,2,joint)
c.line(11,28,9,28,bone)
c.poly([(18,21),(21,21),(22,25),(21,27),(23,28),(24,30),(18,30),(18,28),(19,26),(18,24)],ink)
c.line(19,23,20,25,bone)
c.set(20,26,joint)
c.line(20,27,20,28,shade)
c.line(20,29,22,29,bone)
# bent sword arm, behind torso
c.poly([(13,12),(10,12),(8,15),(8,19),(6,20),(7,23),(10,22),(11,18),(12,16),(14,15)],ink)
c.line(11,13,9,16,bone)
c.line(9,17,9,19,shade)
c.set(9,16,light)
c.rect(7,20,3,2,bone)
# raised short sword, pointing outward
c.poly([(2,9),(5,11),(8,18),(6,20),(4,16)],ink)
c.poly([(3,11),(4,12),(7,18),(6,18)],metal)
c.line(3,11,6,17,shine)
c.line(4,19,9,17,ink)
c.line(5,19,8,18,'#bda269')
c.line(7,20,8,23,wooddark)
c.set(8,23,'#bda269')
c.set(7,20,light)
# hunched upper back and spine
c.poly([(13,10),(17,9),(21,11),(23,15),(21,20),(20,23),(14,23),(12,20),(12,16)],ink)
c.line(17,12,18,20,shade)
c.set(17,13,bone)
c.set(18,16,bone)
c.set(18,19,bone)
# shoulder blades
c.line(13,12,15,11,light)
c.line(19,11,21,13,bone)
c.set(21,14,shade)
# ribs around black hollow chest
c.line(13,14,15,15,bone)
c.line(15,15,17,15,light)
c.line(19,14,20,13,bone)
c.line(13,17,16,18,bone)
c.set(17,17,shade)
c.line(19,17,20,16,bone)
c.line(14,19,16,20,bone)
# pelvic girdle
c.line(14,21,15,22,light)
c.line(15,22,19,22,bone)
c.line(19,22,20,20,shade)
c.set(17,21,shade)
c.set(17,22,ink)
# shield arm
c.line(22,14,24,17,ink)
c.line(21,14,23,17,bone)
# skull, pitched forward and down
c.poly([(11,2),(16,2),(19,4),(19,8),(17,11),(12,12),(9,10),(8,7),(9,4)],ink)
c.poly([(11,3),(16,3),(18,5),(18,8),(16,10),(11,10),(9,8),(9,5)],bone)
c.poly([(11,3),(15,3),(17,4),(17,5),(10,5)],light)
c.line(10,6,10,7,light)
c.line(18,6,17,9,shade)
# heavy eye sockets and nose
c.rect(10,6,3,3,ink)
c.rect(15,6,2,3,ink)
c.set(12,6,joint)
c.set(16,6,joint)
c.set(14,9,ink)
c.set(13,8,shade)
# broken jaw and teeth
c.line(11,10,11,11,bone)
c.line(13,10,13,11,light)
c.line(15,10,15,11,bone)
c.set(16,10,shade)
c.line(12,12,16,12,ink)
# small round wooden shield with reinforced rim
c.poly([(24,15),(28,16),(30,19),(30,23),(28,26),(24,27),(21,25),(20,22),(21,18)],ink)
c.poly([(24,16),(27,17),(29,19),(29,23),(27,25),(24,26),(22,24),(21,21),(22,18)],metal)
c.poly([(24,17),(27,18),(28,20),(28,23),(26,25),(24,25),(22,23),(22,20)],wooddark)
c.poly([(24,18),(26,18),(27,20),(27,23),(26,24),(24,24),(23,22),(23,20)],wood)
c.line(24,18,24,24,woodlight)
c.line(26,19,26,24,wooddark)
c.set(27,21,woodlight)
c.line(22,19,23,17,shine)
c.set(28,19,shine)
c.set(23,24,shade)
c.rect(24,20,3,3,ink)
c.rect(24,20,2,2,metal)
c.set(24,20,shine)
c.set(25,24,woodlight)
view(result)
finish(result)
