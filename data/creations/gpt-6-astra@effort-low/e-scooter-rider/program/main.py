result = new_canvas(32,32)
c=result
o='#202b40'; metal='#668b9b'; hi='#b5d9db'; tire='#182438'; skin='#efb17e'; shade='#cb805f'; blue='#268fa4'; light='#5ac6c6'; pants='#394b70'
# wheels
for x in (7,25):
 c.circle(x,27,3,tire); c.circle(x,27,1,metal); c.set(x,26,hi)
# deck and upright right-facing scooter
c.line(7,25,21,25,o); c.line(8,26,22,26,o); c.line(9,25,21,25,hi)
c.line(21,25,24,23,o)
c.line(25,25,23,13,o); c.line(24,24,22,13,metal); c.set(24,23,hi)
c.rect(20,12,7,2,o); c.rect(24,12,3,1,hi)
# legs: bent knees, two feet on the deck
c.poly([(12,15),(17,16),(17,19),(14,22),(14,24),(10,24),(11,21),(13,18)],o)
c.line(15,18,12,22,pants); c.line(12,22,12,23,pants)
c.rect(10,23,5,2,o); c.rect(11,23,3,1,hi)
c.poly([(12,15),(16,15),(19,20),(19,23),(22,24),(16,24),(16,21),(13,19)],o)
c.poly([(13,17),(16,17),(18,20),(17,23),(17,21)],pants)
c.rect(17,23,5,2,o); c.rect(18,23,3,1,hi)
# torso leaning forward
c.poly([(12,9),(16,9),(18,12),(16,17),(11,17),(10,14)],o)
c.poly([(12,10),(15,10),(17,12),(15,16),(11,16),(11,13)],blue)
c.line(12,11,11,14,light)
# neck
c.rect(15,8,2,3,o); c.rect(15,8,1,2,shade)
# forward bent arm reaching handle
c.line(16,11,19,14,o); c.line(19,14,23,13,o)
c.line(16,12,19,15,o); c.line(19,15,24,14,o)
c.line(16,12,19,14,light); c.line(20,14,23,13,skin)
c.set(24,13,skin)
# head face profile and helmet
c.poly([(12,3),(17,3),(18,5),(18,6),(19,7),(18,8),(17,9),(14,9),(12,7)],o)
c.rect(14,5,4,3,skin); c.set(18,7,skin); c.set(17,6,o); c.set(14,8,shade); c.set(16,8,skin)
c.line(13,6,15,8,o)
c.poly([(11,5),(11,3),(13,1),(17,1),(19,3),(19,5)],o)
c.poly([(12,4),(12,3),(14,2),(17,2),(18,3),(18,4)],'#ed7253')
c.line(14,2,16,2,'#ffc084'); c.rect(11,5,9,1,o); c.set(12,4,'#ffc084')
view(result)
finish(result)
