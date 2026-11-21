result = new_canvas(32,32,name='farm_chicken')
c=result
outline='#6c5143'
shadow='#bba17b'
mid='#dfcda1'
cream='#f1e3bc'
light='#fff0cf'
red='#b95749'
redlight='#dc7960'
reddark='#87463e'
feet='#bb7b47'
# Legs tucked beneath the round belly
c.rect(13,24,2,4,outline)
c.rect(22,24,2,4,outline)
c.line(14,25,14,27,feet)
c.line(23,25,23,27,feet)
c.line(11,28,15,28,outline)
c.line(20,28,25,28,outline)
c.line(12,27,15,27,feet)
c.line(21,27,24,27,feet)
# A lifted fan of tail feathers and full silhouette
c.poly([(8,14),(5,12),(3,12),(3,15),(4,17),(3,18),(4,21),(6,23),(9,25),(14,26),(21,26),(25,24),(27,21),(28,16),(27,11),(25,8),(20,8),(17,10),(15,13),(12,14)],outline)
c.poly([(8,16),(5,13),(4,13),(5,17),(4,18),(5,21),(8,23),(12,25),(21,25),(24,23),(26,20),(27,16),(26,11),(24,9),(20,9),(18,11),(16,15),(12,16)],mid)
# Belly shade follows the lower curve
c.poly([(5,19),(8,21),(13,23),(20,23),(24,21),(26,18),(25,22),(23,24),(20,25),(12,25),(8,23),(6,22)],shadow)
c.poly([(6,17),(9,17),(13,16),(17,14),(18,11),(21,9),(24,9),(26,12),(26,16),(24,20),(21,22),(15,23),(10,21),(7,20)],cream)
c.poly([(17,14),(19,11),(21,10),(24,10),(25,12),(25,15),(22,17),(18,18),(15,17)],light)
# Tail feather separations
c.line(5,16,8,19,shadow)
c.line(5,18,7,20,cream)
# Soft folded wing
c.poly([(10,17),(13,16),(17,17),(20,19),(19,22),(17,23),(13,22),(10,20)],shadow)
c.poly([(10,17),(14,17),(17,18),(19,19),(18,21),(16,22),(12,21),(10,19)],mid)
c.line(11,17,14,17,light)
c.line(10,18,11,19,cream)
c.line(13,20,15,21,cream)
c.set(17,20,cream)
# Rounded three-lobed comb
c.poly([(18,9),(18,6),(19,5),(20,5),(21,6),(22,4),(24,4),(25,5),(25,6),(27,6),(28,7),(27,10),(24,10),(22,9)],reddark)
c.poly([(19,8),(19,6),(20,6),(21,8),(22,7),(23,5),(24,5),(24,8),(26,7),(27,7),(26,9),(23,9),(21,8)],red)
c.set(19,6,redlight)
c.line(23,5,23,6,redlight)
c.set(26,7,redlight)
# Wattle below the beak
c.poly([(25,17),(28,16),(28,19),(27,21),(25,20),(24,18)],reddark)
c.poly([(25,17),(27,17),(27,19),(26,20),(25,19)],red)
c.set(25,17,redlight)
# Short ochre beak pointing right
c.poly([(27,13),(29,14),(30,15),(29,16),(27,17),(26,16),(26,14)],outline)
c.poly([(27,14),(29,15),(27,16)],'#d9a354')
c.line(27,14,28,14,'#efc77b')
# Alert but gentle eye
c.rect(23,12,2,2,'#392f2d')
c.set(23,12,light)
c.set(24,14,shadow)
c.set(24,15,'#dfbb91')
view(result,scale=12)
finish(result)
