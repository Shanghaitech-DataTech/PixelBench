result = new_canvas(32,32,name='factory')
c=result
ink='#252c38'
shadow='#39424b'
brick='#a65e49'
light='#ce8260'
mortar='#704738'
# foundation
c.poly([(3,24),(21,22),(29,24),(29,28),(10,30),(3,27)],ink)
c.poly([(4,25),(11,27),(28,25),(28,27),(11,29),(4,26)],'#657077')
# walls front and side
c.poly([(4,14),(21,14),(21,27),(4,24)],ink)
c.poly([(5,15),(20,16),(20,26),(5,23)],brick)
c.poly([(21,15),(28,12),(28,24),(21,27)],ink)
c.poly([(22,16),(27,14),(27,23),(22,25)],'#78483d')
# brick courses
for y in [18,21,24]:
 c.line(5,y,19,y+1,mortar)
for x,y in [(8,16),(15,17),(6,19),(12,20),(18,20),(8,22),(15,23)]:
 c.line(x,y,x,y+1,mortar)
c.line(6,16,10,16,light)
c.line(6,22,8,22,light)
c.line(16,22,19,22,light)
for y in [17,20,23]:
 c.line(23,y,26,y-1,'#503b36')
# flat roof parapet
c.poly([(3,13),(11,9),(28,11),(29,13),(21,17),(3,15)],ink)
c.poly([(5,13),(12,10),(26,12),(20,15)],'#8e9d9d')
c.poly([(7,13),(12,11),(24,12),(20,14)],'#596a72')
c.line(4,14,20,16,'#bbc3b0')
c.line(21,16,28,13,'#74848a')
# chimney behind roof fittings
c.poly([(20,11),(20,4),(24,3),(26,4),(26,12),(23,13)],ink)
c.rect(21,4,3,8,'#b46d50')
c.line(24,5,24,11,'#794537')
c.line(25,5,25,11,'#623d36')
for y in [6,9]:
 c.line(21,y,23,y,'#744537')
c.set(22,8,'#e39a6b')
c.poly([(19,3),(22,2),(26,3),(26,5),(23,6),(19,5)],ink)
c.line(20,4,23,5,'#dc9366')
c.line(24,4,25,4,'#925d46')
c.line(21,3,23,3,'#0f202b')
# roof vent box
c.poly([(8,11),(11,10),(16,11),(16,14),(13,15),(8,14)],ink)
c.poly([(9,11),(11,11),(15,12),(13,13),(9,12)],'#b9c4bd')
c.rect(9,13,4,1,'#81969c')
c.line(14,13,15,12,'#4c616c')
# front industrial door
c.poly([(10,19),(16,20),(16,26),(10,25)],ink)
c.poly([(11,20),(15,21),(15,25),(11,24)],'#51646b')
for y in [21,23]:
 c.line(11,y,14,y+1,'#8a9b96')
c.set(14,24,'#d4ad67')
# side ventilation grille
c.poly([(23,17),(26,16),(26,20),(23,21)],ink)
for y in [18,20]:
 c.line(24,y,25,y-1,'#92a7a7')
# tiny warning lamp
c.set(7,18,'#f8c86b')
c.set(7,19,'#7c4939')
view(result)
finish(result)
