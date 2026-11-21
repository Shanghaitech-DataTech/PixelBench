result = new_canvas(32,32)
c=result
o='#27252d'; dark='#48414a'; bone='#c9c4a4'; light='#f0e7c4'; shade='#928f7b'; wood='#94603d'; wh='#c18a4c'; ws='#613e30'; metal='#9caeb5'; shine='#d9e6df'
# legs and bent stance
c.poly([(12,20),(16,21),(15,25),(13,26),(12,29),(8,29),(9,27),(11,26)],o)
c.poly([(17,20),(20,20),(21,24),(20,26),(23,28),(23,30),(18,30),(17,28),(18,25),(16,24)],o)
c.line(13,22,12,25,bone); c.set(13,22,light); c.set(12,26,dark)
c.line(11,27,10,28,bone); c.line(9,29,12,29,shade)
c.line(18,22,19,24,bone); c.set(19,25,dark); c.line(19,27,20,28,bone); c.line(19,29,22,29,bone)
# torso and neck
c.poly([(12,10),(17,9),(21,12),(20,17),(18,20),(19,22),(13,23),(11,21),(12,18),(10,15)],o)
c.line(15,10,17,19,shade)
c.line(13,11,18,11,bone)
for y in [13,16]:
 c.line(12,y,15,y+1,bone); c.line(16,y+1,19,y,bone); c.set(12,y,light)
c.line(16,12,17,18,bone)
c.line(12,19,14,20,bone); c.line(14,20,18,19,bone)
c.line(13,21,17,21,shade); c.set(15,21,o)
# sword arm to left
c.poly([(10,11),(12,12),(11,16),(9,18),(6,17),(5,15),(7,13)],o)
c.line(10,12,9,15,bone); c.set(10,12,light); c.set(9,16,dark)
c.line(8,16,6,15,bone)
# short sword upward, leftward
c.poly([(2,4),(5,6),(7,13),(5,14),(3,9)],o)
c.poly([(3,6),(4,7),(6,12),(5,12)],metal)
c.line(3,6,5,11,shine)
c.line(4,14,8,12,o); c.line(4,13,7,12,'#b09b63')
c.line(6,14,7,17,ws); c.set(6,15,light); c.set(7,16,bone); c.set(7,18,o)
# shield arm
c.line(20,12,23,15,o); c.line(20,13,22,15,bone)
# skull, leaning forward
c.poly([(11,2),(16,2),(19,4),(19,8),(17,10),(17,12),(11,12),(10,10),(8,9),(8,5)],o)
c.poly([(11,3),(16,3),(18,5),(18,8),(16,10),(16,11),(11,11),(11,9),(9,8),(9,5)],bone)
c.line(11,3,16,3,light); c.line(10,4,10,6,light); c.line(11,4,16,4,light)
c.line(18,6,18,8,shade); c.set(17,9,shade)
c.rect(10,6,3,3,o); c.rect(15,6,3,2,o); c.set(15,8,dark)
c.set(13,9,o); c.set(14,9,o)
c.line(11,10,16,10,shade)
c.set(12,10,light); c.set(14,10,light); c.set(16,10,light)
# small wooden shield with metal rim
c.poly([(23,13),(27,14),(29,17),(28,23),(24,26),(20,23),(19,17),(20,14)],o)
c.poly([(23,14),(26,15),(28,17),(27,22),(24,24),(21,22),(20,17),(21,15)],shade)
c.poly([(23,15),(26,16),(27,18),(26,22),(24,23),(22,21),(21,17)],wood)
c.line(23,15,23,22,wh); c.line(25,16,25,22,ws); c.line(21,17,22,20,wh)
c.line(21,15,23,14,metal); c.line(27,18,26,22,dark)
c.rect(23,18,3,3,o); c.rect(23,18,2,2,metal); c.set(23,18,shine)
c.set(22,16,shine); c.set(24,23,metal)
view(result)
finish(result)
