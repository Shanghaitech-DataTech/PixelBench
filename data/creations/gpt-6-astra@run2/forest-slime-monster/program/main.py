result = new_canvas(32, 32, name='forest_slime')
c = result
ink='#172d29'
shade='#285043'
mid='#3e7750'
green='#68a357'
light='#a1c66c'
moss='#bbcf74'
# Antler silhouette and warm inner wood.
c.poly([(8,13),(7,9),(5,8),(4,5),(5,4),(7,7),(8,7),(8,3),(10,3),(10,8),(12,6),(13,7),(11,10),(11,13)],ink)
c.line(9,4,9,11,'#bb9c68')
c.line(6,6,8,9,'#bb9c68')
c.set(9,4,'#e4cb91')
c.line(10,9,12,7,'#bb9c68')
c.poly([(21,12),(21,9),(19,7),(20,6),(22,8),(23,4),(25,4),(25,8),(27,6),(28,7),(26,10),(24,11),(24,14)],ink)
c.line(24,5,23,12,'#bb9c68')
c.line(23,10,26,8,'#bb9c68')
c.line(21,8,22,9,'#bb9c68')
c.set(24,5,'#e4cb91')
# Mushroom sits behind the shoulder.
c.rect(24,11,3,6,ink)
c.rect(25,11,1,5,'#efcf9e')
c.poly([(21,10),(22,7),(24,6),(27,6),(29,8),(30,11),(28,13),(23,13),(21,12)],ink)
c.poly([(22,10),(23,8),(25,7),(27,7),(29,10),(29,11),(22,11)],'#b9414a')
c.line(23,12,28,12,'#76323f')
c.line(23,8,26,7,'#ec6b58')
c.rect(25,8,2,2,'#ffe2b3')
c.set(28,10,'#ffe2b3')
c.set(23,10,'#ffe2b3')
# Compact round slime with small basal lobes.
body=[(4,26),(3,23),(4,18),(6,14),(9,11),(13,10),(19,10),(23,12),(26,16),(28,22),(28,26),(26,28),(21,29),(17,28),(13,29),(8,29),(5,28)]
c.poly(body,ink)
c.poly([(5,25),(4,22),(5,18),(8,14),(11,12),(17,11),(22,13),(25,17),(27,23),(26,26),(23,27),(18,26),(13,28),(8,27)],shade)
c.poly([(5,22),(6,17),(9,14),(12,12),(18,12),(22,14),(24,18),(24,23),(21,25),(16,25),(12,27),(7,26)],mid)
c.poly([(6,20),(7,16),(11,13),(16,12),(20,13),(22,15),(22,19),(19,22),(11,23),(7,23)],green)
# Moss cap, broken hanging edges.
c.poly([(6,16),(8,13),(10,11),(14,10),(19,10),(22,12),(24,15),(22,16),(21,14),(19,14),(18,17),(16,16),(16,14),(13,14),(12,16),(10,15),(9,17),(8,16)],'#547d3e')
c.poly([(8,14),(10,12),(14,11),(19,11),(22,13),(20,13),(18,12),(16,14),(14,13),(12,14),(10,13)],light)
c.line(11,12,14,11,moss)
c.set(18,11,moss)
c.set(8,15,light)
c.set(18,15,green)
# Soft broad highlights and lower translucent rim.
c.line(6,18,6,20,light)
c.set(7,17,light)
c.line(8,26,11,26,green)
c.line(20,26,23,26,green)
c.set(25,24,green)
# Dark eye sockets and luminous yellow-green pupils.
for x in (9,19):
    c.rect(x,17,5,5,shade)
    c.rect(x+1,18,3,4,ink)
    c.rect(x+1,18,3,3,'#cde875')
    c.rect(x+1,18,2,2,'#fbffbc')
    c.set(x+2,21,'#8eba58')
# Friendly small mouth and cheeks.
c.set(15,22,ink)
c.set(17,22,ink)
c.set(16,23,ink)
c.line(7,22,8,22,'#8cba67')
c.line(23,22,24,22,'#8cba67')
# Tiny moss flecks and leaf sprout.
c.set(9,24,'#a1c66c')
c.set(11,24,green)
c.set(21,24,green)
c.line(15,10,14,8,shade)
c.poly([(14,9),(11,8),(11,6),(14,7),(15,9)],mid)
c.set(12,7,light)
c.poly([(15,9),(16,6),(19,6),(18,8)],green)
c.set(17,7,light)
view(result)
finish(result)
