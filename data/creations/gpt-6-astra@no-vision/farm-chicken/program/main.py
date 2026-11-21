c = new_canvas(32, 32, name='farm_chicken')
# Muted warm barnyard palette.
ink='#775541'
shade='#b99568'
mid='#d5b887'
cream='#ead6a4'
light='#f7e8bf'
rededge='#934e43'
red='#bc6551'
redlight='#d88765'
foot='#be8247'
gold='#e2ac58'
# Little planted legs, with open space between the toes.
c.rect(12,23,2,5,ink)
c.rect(20,23,2,5,ink)
c.line(11,28,15,28,ink)
c.line(19,28,23,28,ink)
c.line(12,25,12,27,foot)
c.line(20,25,20,27,foot)
c.line(12,28,14,28,gold)
c.line(20,28,22,28,gold)
c.set(11,27,foot)
c.set(19,27,foot)
# Raised tail feathers and the full pear-shaped silhouette.
c.poly([(8,13),(5,10),(3,10),(4,14),(2,13),(2,16),(4,19),(4,21),(7,24),(12,26),(20,26),(24,24),(26,20),(27,13),(26,9),(23,7),(19,7),(17,10),(16,12)],ink)
c.poly([(8,15),(5,12),(4,12),(6,17),(3,15),(5,19),(6,22),(9,24),(13,25),(20,25),(23,23),(25,19),(26,12),(24,9),(20,8),(18,11),(17,14)],cream)
# Body shadow follows the low round belly.
c.poly([(5,19),(8,22),(13,23),(19,23),(23,21),(25,17),(25,21),(23,24),(20,25),(12,25),(8,24),(6,22)],mid)
c.line(10,25,19,25,shade)
c.set(7,23,shade)
c.line(21,24,22,24,shade)
# Soft light over back and forehead.
c.poly([(7,16),(10,14),(16,14),(19,10),(20,9),(23,9),(25,11),(25,14),(23,16),(21,17),(18,16),(13,16),(10,18),(7,18)],light)
c.line(5,13,7,15,light)
# Scalloped folded wing.
c.poly([(10,17),(13,16),(17,17),(20,19),(19,22),(17,23),(12,23),(9,21),(8,19)],shade)
c.poly([(10,17),(13,17),(17,18),(19,19),(18,21),(16,22),(12,22),(10,20),(9,19)],cream)
c.line(11,18,14,18,light)
c.line(11,20,12,21,mid)
c.line(14,20,15,21,mid)
c.set(18,20,mid)
# Three low, rounded comb lobes.
c.poly([(18,9),(17,6),(18,4),(20,4),(21,6),(21,3),(23,3),(24,6),(25,5),(26,6),(26,9),(24,10),(21,9)],rededge)
c.rect(18,5,2,3,red)
c.rect(22,4,2,4,red)
c.rect(24,7,2,2,red)
c.line(19,8,24,8,red)
c.set(18,5,redlight)
c.set(22,4,redlight)
c.set(23,5,redlight)
# Hanging wattle, tucked under the beak.
c.poly([(24,15),(27,15),(27,18),(26,20),(24,19),(23,17)],rededge)
c.rect(24,16,2,3,red)
c.set(24,16,redlight)
# Short golden beak facing right.
c.poly([(26,12),(28,12),(30,14),(28,16),(26,16)],ink)
c.poly([(26,13),(28,13),(29,14),(27,15),(26,15)],gold)
c.set(26,13,light)
c.line(27,15,28,15,foot)
# Bright, quiet eye and a single warm cheek pixel cluster.
c.rect(23,11,2,3,ink)
c.set(24,12,'#3f3830')
c.set(23,11,light)
c.line(22,15,23,15,'#dfb48b')
print(c.stats_text())
print(c.matrix_text())
save('farm_chicken',c)
finish(c)
