result = new_canvas(32, 32, name='forest_slime')
c = result
# Restrained woodland palette; warm accents contrast against jade jelly.
ink='#182e2b'
dark='#24493b'
shade='#356345'
mid='#518548'
light='#80a956'
moss='#b0c66a'
# Tiny woody antlers behind the crown.
c.poly([(9,12),(8,9),(6,7),(6,3),(8,3),(8,6),(10,7),(10,3),(12,2),(12,8),(13,11)],ink)
c.line(7,4,7,7,'#9b7650')
c.line(7,7,10,9,'#9b7650')
c.line(11,4,11,10,'#9b7650')
c.set(11,3,'#dfbd7f')
c.set(7,4,'#dfbd7f')
c.poly([(19,11),(20,7),(20,3),(22,3),(22,6),(24,4),(25,5),(23,8),(22,11)],ink)
c.line(21,4,21,10,'#9b7650')
c.line(21,8,24,5,'#9b7650')
c.set(21,4,'#dfbd7f')
# A little fly agaric growing on the rear right shoulder.
c.rect(24,9,3,7,ink)
c.rect(25,10,1,5,'#efd5a0')
c.poly([(21,9),(22,6),(24,5),(27,5),(29,7),(30,10),(28,11),(22,11)],ink)
c.poly([(22,9),(23,7),(25,6),(27,6),(29,9)],'#b83c45')
c.line(23,10,28,10,'#743641')
c.line(24,6,26,6,'#ef6d59')
c.rect(24,7,2,1,'#fff0c6')
c.set(28,8,'#fff0c6')
c.set(22,9,'#f5bd99')
# Rounded front-facing jelly silhouette with soft lobes at its base.
c.poly([(12,10),(18,10),(18,11),(22,11),(22,12),(25,12),(25,14),(27,14),(27,17),(28,17),(28,21),(29,23),(29,26),(27,28),(23,28),(21,27),(19,29),(13,29),(11,28),(7,29),(3,27),(2,24),(3,21),(4,17),(6,14),(8,13),(8,12),(12,12)],ink)
c.poly([(12,11),(18,11),(18,12),(22,12),(22,13),(24,13),(24,15),(26,15),(26,18),(27,18),(27,23),(28,24),(28,26),(26,27),(22,27),(21,26),(18,28),(13,28),(11,27),(7,28),(4,26),(3,24),(4,21),(5,18),(7,15),(9,14),(9,13),(12,13)],shade)
c.poly([(12,12),(18,12),(18,13),(22,13),(24,15),(24,20),(22,24),(18,26),(10,26),(6,24),(5,21),(6,17),(9,15),(12,14)],mid)
c.poly([(11,14),(17,13),(21,14),(22,16),(18,16),(15,15),(11,17),(8,20),(6,21),(7,17)],light)
# Moss cap, with irregular drips and small leaf tufts.
c.poly([(9,12),(11,11),(12,9),(14,10),(16,9),(18,10),(20,11),(22,12),(23,14),(21,16),(19,14),(17,15),(16,13),(14,14),(12,16),(10,14),(8,15)],dark)
c.poly([(10,12),(12,12),(13,10),(14,11),(16,10),(18,11),(18,12),(21,12),(22,14),(20,14),(19,13),(17,14),(16,12),(14,13),(12,14)],light)
c.set(13,11,moss)
c.line(15,11,16,11,moss)
c.set(20,13,moss)
# Luminous, wide-set eyes: deep sockets, green halo, bright warm centres.
for x in (9,20):
    c.rect(x-1,18,5,5,dark)
    c.rect(x,17,3,7,dark)
    c.rect(x,18,3,5,'#8dbf65')
    c.rect(x,18,2,4,'#e9f69b')
    c.rect(x,18,2,2,'#fffbd3')
    c.set(x+2,22,'#b4df76')
# Cheerful little curved mouth and blush.
c.line(14,23,14,24,ink)
c.line(15,25,17,25,ink)
c.line(18,23,18,24,ink)
c.line(15,24,17,24,'#95b862')
c.line(7,23,8,23,'#8bb180')
c.line(24,23,25,23,'#8bb180')
# Translucent edge glints and sparse moss flecks.
c.line(5,22,5,24,'#a4c776')
c.set(6,25,light)
c.line(14,27,17,27,'#6c9750')
c.set(25,25,mid)
c.set(8,16,moss)
c.set(7,18,light)
c.set(24,16,light)
c.set(26,20,mid)
c.set(10,26,light)
view(result)
finish(result)
