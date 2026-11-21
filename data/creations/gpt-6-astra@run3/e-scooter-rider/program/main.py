result = new_canvas(32, 32, name='e-scooter-rider')
c = result
ink = '#20283e'
metal = '#61758a'
light = '#c4e1e5'
teal = '#26b4af'
# wheels and scooter chassis
c.circle(7,27,3,ink)
c.circle(26,27,3,ink)
c.circle(7,27,1,metal)
c.circle(26,27,1,metal)
c.set(7,26,light).set(26,26,light)
c.line(7,24,22,24,ink)
c.line(7,25,23,25,ink)
c.line(9,24,21,24,teal)
c.line(22,24,25,21,ink)
# angled steering column and fork
c.line(26,26,23,13,ink)
c.line(25,24,23,15,metal)
c.set(26,24,teal)
c.rect(21,12,6,2,ink)
c.rect(25,12,2,1,light)
# back leg, bent slightly to the rear
c.poly([(12,16),(16,17),(13,20),(12,23),(9,23),(10,19)],ink)
c.line(12,18,11,21,'#4c5876')
c.rect(9,22,6,2,ink)
c.rect(10,22,3,1,light)
# forward leg with a readable bent knee
c.poly([(14,16),(17,16),(19,19),(17,22),(17,23),(14,23),(14,21),(16,19),(13,19)],ink)
c.line(16,17,17,19,'#657495')
c.line(17,19,15,22,'#657495')
c.rect(15,22,5,2,ink)
c.rect(16,22,3,1,light)
# jacket, leaning forward
c.poly([(13,9),(16,9),(18,12),(17,17),(12,18),(10,15),(11,11)],ink)
c.poly([(13,10),(15,10),(17,12),(15,16),(12,16),(11,14)],'#e57542')
c.line(12,11,11,14,'#ffb65d')
c.line(12,16,15,16,'#b94739')
# bent arm reaching right to the grip
c.line(15,11,19,14,ink)
c.line(16,11,20,13,ink)
c.line(19,14,23,13,ink)
c.line(16,12,19,13,'#ffb65d')
c.line(20,13,22,12,'#f4b88b')
c.set(23,12,'#f4b88b')
# neck and face profile
c.rect(14,7,3,3,ink)
c.rect(15,8,2,2,'#d58b70')
c.poly([(13,4),(17,4),(18,6),(19,7),(18,8),(16,9),(13,7)],ink)
c.poly([(14,5),(17,5),(17,6),(18,7),(17,8),(15,8),(14,7)],'#f4b88b')
c.set(17,6,ink)
c.set(14,6,'#ffd6a0')
# rounded helmet shell, extended visor and strap
c.poly([(12,2),(16,2),(18,4),(18,5),(12,6),(10,5),(10,4)],ink)
c.poly([(12,3),(16,3),(17,4),(12,5),(11,4)],teal)
c.line(12,3,15,3,'#8ce5ce')
c.line(15,5,19,5,ink)
c.line(13,6,15,8,ink)
c.set(14,7,'#61758a')
view(result, scale=12)
finish(result)
