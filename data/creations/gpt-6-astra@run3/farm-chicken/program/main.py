result = new_canvas(32,32,name='farm_chicken')
c=result
outline='#705344'
shadow='#b59a70'
cream='#ead9a8'
light='#f8ebc7'
mid='#d6bf8e'
# Small ochre legs and splayed toes, behind the body.
c.rect(12,24,2,4,outline)
c.rect(20,24,2,4,outline)
c.line(10,28,14,28,outline)
c.line(18,28,23,28,outline)
c.line(12,25,12,27,'#d39a55')
c.line(20,25,20,27,'#d39a55')
c.line(11,28,13,28,'#d39a55')
c.line(19,28,22,28,'#d39a55')
# Three rounded tail feathers merge into a generous pear-shaped body.
c.poly([(7,19),(4,16),(3,12),(4,10),(6,11),(8,14),(7,10),(8,9),(10,11),(12,15),(15,12),(17,9),(18,6),(21,5),(24,6),(26,9),(26,14),(27,17),(27,21),(25,24),(22,26),(12,26),(8,24),(6,21)],outline)
c.poly([(7,20),(5,16),(4,12),(5,12),(9,17),(9,12),(10,13),(12,17),(15,14),(18,12),(18,8),(20,6),(23,6),(25,9),(25,15),(26,18),(26,21),(24,24),(21,25),(12,25),(9,23)],cream)
# Warm shadow follows the lower silhouette.
c.poly([(7,19),(9,21),(12,23),(19,24),(23,23),(26,20),(25,23),(22,25),(12,25),(9,23)],mid)
c.line(12,25,21,25,shadow)
c.line(8,21,10,23,shadow)
# Soft upper-lit crown and breast.
c.poly([(18,9),(19,7),(22,7),(24,8),(24,11),(23,13),(25,16),(25,19),(23,21),(23,17),(20,15),(17,16),(13,17),(12,16),(16,13),(18,12)],light)
c.line(5,13,7,16,light)
# Comb: three little scallops.
c.poly([(18,7),(17,5),(17,3),(19,3),(20,4),(21,2),(23,2),(23,4),(25,3),(26,4),(26,6),(24,8),(21,7)],'#874f42')
c.poly([(18,5),(18,4),(19,4),(20,6),(22,3),(22,5),(24,5),(25,4),(25,6),(23,7),(20,6)],'#c97863')
c.set(22,3,'#e49a79')
c.set(18,4,'#e49a79')
# Wing with a curved, tucked feather edge.
c.path('M 11 17 Q 15 15 19 17 Q 21 19 19 22 Q 15 24 11 21 L 10 19',shadow,fill=False)
c.poly([(12,17),(15,17),(18,18),(19,20),(17,22),(14,22),(11,20)],mid)
c.line(12,17,15,17,light)
c.line(11,18,11,19,light)
c.line(14,21,16,21,cream)
c.set(18,20,cream)
# Wattle beneath beak.
c.poly([(24,13),(26,13),(27,15),(26,18),(24,18),(23,16)],'#874f42')
c.rect(24,14,2,3,'#c97863')
c.set(24,14,'#e49a79')
# Golden beak points gently right.
c.poly([(25,10),(27,10),(30,12),(27,14),(25,13)],outline)
c.poly([(26,11),(27,11),(29,12),(26,12)],'#ddb16a')
c.line(26,13,27,13,'#bd854c')
# Single glossy eye; restrained expression.
c.rect(22,10,2,2,'#493e36')
c.set(22,10,'#fff3d4')
c.set(23,12,mid)
view(result,scale=12)
finish(result)
