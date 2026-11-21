result = new_canvas(32,32,name='scooter_rider')
c=result
ink='#202c40'
steel='#6b8296'
light='#bfd6de'
teal='#26b8b4'
bright='#81e5d3'
skin='#efb486'
shade='#c88068'
# wheels and chassis
c.circle(8,27,3,ink)
c.circle(26,27,3,ink)
c.circle(8,27,1,steel)
c.circle(26,27,1,steel)
c.set(8,26,light); c.set(26,26,light)
c.line(8,25,24,25,ink)
c.line(9,26,22,26,ink)
c.line(9,24,22,24,teal)
c.line(10,24,20,24,bright)
# angled steering column and fork
c.line(26,26,23,13,ink)
c.line(25,24,23,15,steel)
c.line(22,13,26,13,ink)
c.set(25,12,ink)
# far leg, bent forwards
c.poly([(14,16),(17,16),(18,19),(16,22),(17,23),(16,24),(13,23),(13,21),(15,19)],ink)
c.line(16,18,16,20,'#49617b')
# torso silhouette
c.poly([(12,9),(15,9),(17,11),(17,16),(15,18),(11,17),(10,14)],ink)
c.poly([(12,10),(15,10),(16,12),(15,16),(12,16),(11,14)],teal)
c.line(12,11,11,13,bright)
# rear leg planted
c.poly([(11,16),(15,17),(14,20),(13,22),(15,23),(15,24),(10,24),(9,22),(11,19)],ink)
c.line(12,18,11,21,'#516783')
c.line(11,23,14,23,light)
# neck and face looking right
c.rect(13,7,3,3,ink)
c.rect(14,8,2,2,shade)
c.poly([(13,3),(17,3),(18,5),(18,6),(19,7),(17,8),(14,8),(12,6)],ink)
c.rect(14,4,3,4,skin)
c.set(18,6,skin)
c.set(16,5,ink)
c.set(14,7,shade)
# helmet cap with visor
c.poly([(10,4),(11,2),(13,1),(16,1),(18,3),(18,4),(12,4),(12,6),(10,6)],ink)
c.poly([(11,4),(12,2),(16,2),(17,3),(13,3),(12,5),(11,5)],teal)
c.line(13,2,15,2,bright)
c.line(13,5,14,8,ink)
# forward arm, bent to handlebar
c.poly([(15,10),(17,10),(20,13),(23,12),(24,13),(23,15),(19,15),(15,12)],ink)
c.line(16,11,19,14,teal)
c.line(20,14,22,13,skin)
c.set(23,13,skin)
c.set(16,10,bright)
view(result)
finish(result)
