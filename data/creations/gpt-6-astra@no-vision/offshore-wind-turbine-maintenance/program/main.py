c = new_canvas(64,64,background='#9ebfcd',name='offshore-maintenance')
# A cool maritime sky, with a low pale haze.
c.rect(0,17,64,12,'#aecbd4')
c.rect(0,29,64,9,'#c4d8da')
c.rect(3,10,12,2,'#bed4db'); c.rect(7,8,10,2,'#bed4db')
c.rect(20,16,12,1,'#bed4db'); c.rect(23,15,7,1,'#bed4db')
# Two complete turbines on the far bank of the sea.
far='#83a4b2'; light='#e5e9df'
c.line(12,23,11,39,far); c.line(13,23,13,39,light)
c.poly([(11,22),(12,9),(13,9),(13,21)],light)
c.poly([(12,22),(2,28),(1,28),(9,22)],light)
c.poly([(13,22),(22,28),(22,30),(13,24)],light)
c.rect(10,21,5,2,far); c.rect(10,21,4,1,light); c.set(12,22,light)
c.line(28,28,28,39,far); c.line(29,28,29,39,'#dbe5df')
c.poly([(28,27),(24,19),(25,19),(29,26)],light)
c.poly([(29,27),(37,24),(37,25),(30,28)],light)
c.poly([(28,28),(25,35),(24,35),(27,27)],light)
c.rect(27,26,4,2,far); c.set(28,26,light)
# Ocean: broad bands and deliberate, broken wave crests.
c.rect(0,38,64,26,'#427e92')
c.rect(0,43,64,8,'#316b83')
c.rect(0,51,64,13,'#23576e')
c.line(0,38,63,38,'#689aa6')
for x,y,w in [(1,40,8),(18,40,5),(26,39,7),(3,45,6),(17,44,9),(8,49,10),(22,48,5),(0,54,8),(15,55,7),(23,59,9),(3,61,9),(54,49,7),(57,57,6),(44,61,9)]:
    c.rect(x,y,w,1,'#5e9fa9')
for x,y,w in [(5,44,4),(20,43,4),(10,48,5),(1,53,4),(17,54,3),(26,58,4),(6,60,4),(57,48,4),(59,56,3)]:
    c.rect(x,y,w,1,'#a6cdca')
c.line(0,58,5,58,'#19485e'); c.line(9,57,14,57,'#19485e'); c.line(35,62,42,62,'#19485e')
# Main turbine tower continues above the frame: believable industrial scale.
c.poly([(44,0),(51,0),(54,51),(42,51)],'#6b8792')
c.poly([(44,0),(48,0),(49,48),(42,48)],'#d8e2dd')
c.poly([(44,0),(45,0),(45,37),(43,38)],'#f0eee0')
c.line(51,0,53,38,'#4b6879')
# Ring seams and a restrained reflected blue edge.
c.line(44,14,51,14,'#9aadb2'); c.line(44,15,49,15,'#e9eade')
c.line(43,30,52,30,'#9aadb2')
c.line(43,31,49,31,'#e9eade')
# Foundation beneath the service deck.
c.rect(42,43,12,12,'#354f5c')
c.rect(43,44,5,11,'#607580'); c.rect(43,47,2,6,'#926d55')
c.rect(52,44,2,11,'#203e50')
c.rect(42,54,12,3,'#203e50')
c.line(39,57,55,57,'#72adb4'); c.line(41,58,51,58,'#b2d3cd')
c.line(53,56,58,56,'#72adb4')
# Brackets, platform floor and rear railing.
c.line(32,44,43,51,'#263f50'); c.line(59,44,53,50,'#263f50')
c.line(34,44,43,49,'#75909b'); c.line(58,44,53,48,'#75909b')
c.rect(32,35,29,1,'#c8a552')
for x in [32,40,54,60]: c.rect(x,35,1,6,'#d9b85a')
c.rect(32,38,29,1,'#9d884c')
# Tower access hatch.
c.rect(46,32,5,9,'#52717c'); c.rect(47,33,3,7,'#9baeb0'); c.set(49,37,'#e8ce7c')
c.rect(30,40,32,3,'#263f50'); c.rect(31,40,30,1,'#9fb4b7')
c.rect(30,43,32,2,'#172f42')
c.rect(30,42,32,1,'#e6b950')
for x in [31,40,48,56]: c.line(x,42,x+2,42,'#675e42')
# Front safety rails, leaving a ladder opening at left.
c.line(30,35,30,41,'#f1cd6f'); c.line(30,35,33,35,'#f1cd6f')
c.line(40,35,61,35,'#f1cd6f'); c.line(40,38,61,38,'#d8ae53')
for x in [40,48,55,61]: c.line(x,35,x,41,'#f1cd6f')
# Ladder hung vertically from the platform.
c.line(34,39,34,60,'#172f42'); c.line(39,39,39,60,'#172f42')
c.line(35,38,35,59,'#a9bbba'); c.line(38,38,38,59,'#809eaa')
for y in range(41,60,3): c.line(35,y,38,y,'#c2c9bc')
# A technician in a yellow helmet, orange suit and dark fall-arrest harness.
# Raised glove and arms reach the higher ladder rung.
c.set(38,44,'#f1cb79'); c.line(37,45,37,47,'#ed8c3e')
c.rect(33,46,4,5,'#923e2e')
c.rect(33,46,3,4,'#ef8a3b'); c.set(33,46,'#ffc16a')
c.line(32,48,34,46,'#ef8a3b'); c.set(32,49,'#eed0a0')
c.rect(34,44,2,2,'#d2a177'); c.set(36,44,'#243b4b')
c.rect(33,43,3,2,'#f4cc4d'); c.rect(33,44,4,1,'#ffe18b')
c.line(34,46,35,49,'#273d48'); c.line(33,49,36,49,'#e6d596')
c.set(35,48,'#f4d16d')
c.line(33,50,33,52,'#cc6633'); c.line(36,50,37,51,'#ed8c3e')
c.line(33,53,35,53,'#172f42'); c.line(37,52,38,52,'#172f42')
# Tether leads back to an anchor on the platform rail.
c.line(36,47,40,42,'#d6bb75'); c.set(40,41,'#eee4b4')
print(c.stats_text())
print(c.matrix_text(region=(29,34,42,59)))
save('offshore-maintenance',c)
finish(c)
