result = new_canvas(48,48, name='vintage_sewing_machine')
c = result
ink='#171c27'
dark='#25313a'
mid='#3d5157'
light='#637b79'
shine='#9cb3a6'
gold='#b58b45'
goldhi='#e5c177'
wood='#734635'
# angled wooden plinth
c.poly([(4,33),(36,31),(44,36),(43,41),(10,44),(3,39)],ink)
c.poly([(4,34),(36,32),(43,36),(10,40),(4,38)],'#bd8750')
c.poly([(4,38),(10,40),(43,36),(43,40),(10,43),(4,39)],wood)
c.line(11,41,41,38,'#9e6340')
c.line(6,35,33,33,'#e2b675')
# heavy iron bed
c.poly([(7,31),(34,29),(40,33),(39,36),(12,39),(6,35)],ink)
c.poly([(7,32),(33,30),(39,33),(12,37),(7,35)],mid)
c.line(12,37,38,34,gold)
c.line(13,38,38,35,dark)
# red cloth spread from needle to foreground
c.poly([(9,31),(19,30),(25,34),(26,39),(22,43),(15,42),(14,38),(8,36)],'#691f36')
c.poly([(10,32),(18,31),(23,34),(24,39),(21,42),(17,41),(16,37),(9,35)],'#bd3448')
c.poly([(11,32),(17,32),(20,35),(20,39),(22,41),(18,40),(17,36)],'#ed5960')
c.line(10,34,15,35,'#f47b70')
c.line(24,35,24,39,'#8f283f')
c.line(15,38,16,41,'#df4a53')
# rear column, rises from bed
c.poly([(27,13),(34,13),(35,16),(35,28),(38,31),(36,33),(26,34),(25,31),(28,28),(28,22),(26,19)],ink)
c.poly([(29,16),(33,15),(33,28),(35,31),(28,32),(30,28),(30,21),(28,19)],dark)
c.line(32,19,32,28,mid)
c.line(29,30,33,30,gold)
c.set(30,31,goldhi)
# handwheel behind right shoulder
c.ellipse(37,17,6,9,ink)
c.ellipse(37,17,5,8,light)
c.ellipse(37,17,4,7,dark)
c.ellipse(37,17,3,6,ink)
c.line(37,11,37,23,mid)
c.line(34,13,40,21,light)
c.line(34,21,40,13,mid)
c.ellipse(37,17,2,3,gold)
c.ellipse(37,17,1,2,goldhi)
c.line(41,12,42,15,shine)
c.line(42,17,41,22,mid)
c.rect(39,17,4,2,ink)
c.rect(41,17,3,2,gold)
c.set(43,17,goldhi)
# arm and needle head: stepped vintage silhouette
c.poly([(10,12),(12,9),(18,8),(23,9),(28,10),(31,10),(34,12),(34,19),(31,21),(27,20),(25,17),(18,16),(17,23),(14,25),(9,23),(8,19),(8,14)],ink)
c.poly([(11,12),(14,10),(19,10),(25,12),(30,12),(32,13),(31,17),(27,17),(24,15),(16,14),(15,20),(10,21),(9,18)],mid)
c.poly([(10,16),(15,15),(15,22),(13,23),(10,22)],dark)
c.poly([(17,12),(23,13),(27,14),(31,13),(32,17),(30,19),(27,18),(25,16),(17,15)],dark)
c.line(13,10,19,10,shine)
c.line(20,11,25,12,light)
c.line(10,13,10,17,light)
# gold ornamental pinstriping
c.line(17,13,23,14,gold)
c.line(23,14,27,16,gold)
c.line(28,17,30,17,goldhi)
c.line(11,21,14,21,gold)
c.set(12,20,goldhi)
c.set(29,14,gold)
# face plate
c.poly([(9,14),(11,14),(12,16),(12,20),(10,21),(9,20)],light)
c.line(10,15,10,19,shine)
c.set(10,15,'#d6dfc7')
c.set(10,20,ink)
# needle bar and separate presser rod
c.rect(11,24,2,6,light)
c.line(11,25,11,29,'#d6dfc7')
c.line(12,29,12,33,ink)
c.set(12,31,shine)
c.line(15,23,15,31,ink)
c.line(14,25,14,30,light)
# foot silver on cloth
c.poly([(14,30),(16,30),(18,32),(17,33),(13,33),(13,32)],ink)
c.line(14,31,16,31,shine)
c.line(14,32,17,32,light)
# tension knob on head
c.circle(15,18,2,ink)
c.circle(15,18,1,gold)
c.set(15,17,goldhi)
c.set(15,19,wood)
# spool pin and thread spool on top
c.line(20,4,20,9,ink)
c.rect(17,4,6,1,goldhi)
c.rect(18,5,4,3,'#d5b98b')
c.line(18,6,21,6,'#a4815d')
c.rect(17,8,6,1,gold)
c.set(20,3,shine)
# fine thread via guide to needle
c.line(17,5,13,8,'#d5b98b')
c.line(13,8,12,12,'#d5b98b')
c.set(12,11,goldhi)
# small bed screw
c.set(34,33,shine)
c.set(30,33,ink)
view(result, scale=8)
finish(result)
