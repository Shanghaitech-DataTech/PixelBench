result = new_canvas(32, 32, name='farm_chicken')
c=result
outline='#705345'
shadow='#b59a70'
mid='#dfcba0'
cream='#f2e2b8'
light='#fff0ce'
red='#b85e4e'
redlight='#da8063'
# Feet tucked beneath the round body
c.line(12,24,12,28,outline)
c.line(20,24,20,28,outline)
c.line(10,29,14,29,outline)
c.line(18,29,22,29,outline)
c.line(12,26,12,28,'#d59d56')
c.line(20,26,20,28,'#d59d56')
c.set(11,28,'#d59d56'); c.set(19,28,'#d59d56')
# Upturned tail and plump silhouette
c.poly([(8,13),(5,10),(3,10),(3,14),(4,17),(3,19),(4,22),(7,25),(11,26),(20,26),(24,24),(26,21),(27,17),(27,10),(25,7),(21,6),(18,8),(17,11),(14,12)],outline)
c.poly([(8,15),(4,11),(4,14),(6,18),(4,19),(5,22),(8,24),(12,25),(20,25),(24,23),(25,20),(26,16),(26,10),(24,8),(21,7),(19,9),(18,13),(14,13)],mid)
c.poly([(8,16),(6,14),(7,18),(5,19),(6,22),(10,24),(18,24),(22,23),(24,20),(25,16),(25,10),(23,8),(21,8),(19,10),(19,14),(15,14)],cream)
c.poly([(8,17),(10,15),(16,14),(19,13),(20,10),(22,9),(24,10),(24,13),(22,15),(18,16),(12,17)],light)
# Shadow low on belly
c.line(9,24,12,25,shadow); c.line(13,25,20,25,shadow)
c.line(21,24,23,23,shadow)
# Soft scalloped wing
c.poly([(10,17),(14,16),(18,17),(20,19),(19,22),(16,23),(12,22),(9,20)],shadow)
c.poly([(10,17),(14,17),(17,18),(19,19),(18,21),(16,22),(12,21),(10,20)],mid)
c.line(11,17,14,17,light)
c.line(10,18,10,19,cream)
c.set(12,20,cream); c.line(14,20,15,21,cream)
# Comb: three rounded lobes
c.poly([(19,8),(18,6),(18,4),(20,3),(21,4),(22,2),(24,2),(25,4),(26,4),(27,6),(26,9),(23,8)],outline)
c.poly([(20,7),(19,6),(19,4),(20,4),(21,6),(22,5),(23,3),(24,3),(24,6),(26,5),(26,7),(25,8),(23,7)],red)
c.set(19,4,redlight); c.line(23,3,23,4,redlight); c.set(25,5,redlight)
# Small dangling wattle
c.poly([(25,15),(27,14),(28,16),(27,19),(25,19),(24,17)],outline)
c.rect(25,15,2,3,red)
c.set(25,15,redlight)
# Beak projecting to the right
c.poly([(26,12),(28,12),(30,14),(28,16),(26,16)],outline)
c.poly([(27,13),(28,13),(29,14),(27,14)],'#e3b363')
c.line(27,15,28,15,'#bf8549')
# Bright, quiet face
c.set(23,11,outline)
c.rect(23,12,2,2,'#493f37')
c.set(23,12,light)
c.set(22,15,'#e4bc8b')
c.set(23,15,'#e4bc8b')
view(result)
finish(result)
