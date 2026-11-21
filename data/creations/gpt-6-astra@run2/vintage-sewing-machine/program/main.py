result = new_canvas(48,48,name='vintage-sewing-machine')
c=result
ink='#181d27'
dark='#252d35'
mid='#3c4c52'
light='#63777a'
shine='#9caca3'
gold='#b58b4c'
goldhi='#e4c37e'
goldsh='#745333'
steel='#b9c6c4'
white='#e3e2cf'
# wooden base, shown in shallow perspective
c.poly([(3,35),(35,32),(44,36),(44,40),(10,44),(3,40)],ink)
c.poly([(4,35),(35,33),(43,36),(10,40),(4,38)],'#987047')
c.poly([(5,35),(35,34),(40,36),(10,39)],'#c39a62')
c.poly([(4,39),(10,41),(43,37),(43,40),(10,43),(4,40)],'#604535')
c.line(11,41,41,38,'#ad7c4b')
# metal bed
c.poly([(6,33),(33,31),(40,34),(39,37),(11,40),(6,37)],ink)
c.poly([(7,33),(33,32),(38,34),(11,37),(7,36)],mid)
c.poly([(11,37),(39,34),(38,36),(11,39)],dark)
c.line(12,38,36,35,goldsh)
c.line(8,34,30,32,light)
# cloth falling over front left corner
c.poly([(10,32),(20,31),(27,34),(21,36),(21,42),(17,45),(8,42),(9,36)],'#5e2435')
c.poly([(10,33),(19,32),(24,34),(18,36),(19,42),(16,44),(9,41),(10,36)],'#b83d48')
c.poly([(11,33),(18,33),(20,34),(14,36),(14,41),(16,43),(11,41)],'#e15c58')
c.line(18,36,18,41,'#812b3e')
c.line(10,40,15,42,'#f08067')
# pillar / heavy machine casting
c.poly([(28,14),(35,13),(38,18),(36,31),(39,33),(36,35),(26,36),(24,34),(28,31)],ink)
c.poly([(29,17),(34,16),(35,19),(33,30),(35,33),(28,34),(29,30)],dark)
c.poly([(30,18),(33,17),(33,28),(31,31),(31,33),(28,33),(30,29)],mid)
c.line(34,21,33,29,light)
c.line(27,34,35,33,gold)
# rear handwheel axle
c.line(34,17,43,16,ink)
c.rect(36,15,4,4,mid)
# wheel angled narrow oval, rear bevel
c.ellipse(41,17,5,9,ink)
c.ellipse(42,16,4,8,mid)
c.ellipse(41,16,3,7,steel)
c.ellipse(41,16,2,6,dark)
c.line(41,10,41,22,light)
c.line(39,13,43,19,light)
c.line(39,19,43,13,light)
c.ellipse(41,16,1,2,gold)
c.set(41,15,goldhi)
c.line(44,12,44,19,'#7f9293')
c.line(40,8,42,8,white)
# arm silhouette: broad arched neck
c.poly([(10,13),(12,10),(28,10),(33,12),(35,16),(34,22),(29,22),(27,18),(18,17),(17,23),(11,24),(9,21)],ink)
c.poly([(12,12),(27,11),(31,13),(33,16),(32,20),(30,20),(28,16),(17,15),(15,21),(11,21),(11,15)],dark)
c.poly([(12,11),(26,11),(30,13),(31,14),(17,13),(12,15)],light)
c.line(15,11,26,11,shine)
c.poly([(18,14),(27,14),(30,17),(29,18),(26,16),(18,16)],mid)
# gold inlaid trim
c.line(18,12,26,12,gold)
c.line(19,15,26,15,goldsh)
c.set(27,16,gold)
c.set(29,18,goldhi)
c.line(30,23,30,27,goldsh)
c.set(31,24,gold)
# faceplate of needle housing
c.poly([(10,14),(14,13),(17,15),(16,23),(12,25),(10,22)],ink)
c.poly([(11,15),(14,14),(15,16),(14,23),(12,23),(11,21)],mid)
c.line(12,15,12,21,shine)
c.line(14,16,14,21,steel)
c.set(13,16,ink)
c.set(13,21,ink)
# tension control knob
c.rect(8,17,3,3,ink)
c.rect(8,17,2,2,gold)
c.set(8,17,goldhi)
# needle bar and presser bar
c.line(12,24,12,30,steel)
c.line(13,24,13,29,light)
c.line(12,30,12,33,white)
c.line(16,23,16,32,ink)
c.line(15,24,15,31,steel)
c.line(15,31,17,33,light)
c.line(14,33,19,33,ink)
c.line(14,32,18,32,white)
# thread spool above arm
c.line(24,5,24,9,ink)
c.rect(21,5,6,5,goldsh)
c.rect(22,5,4,4,'#d6b88c')
c.line(22,6,25,6,white)
c.line(22,8,25,8,gold)
c.line(21,4,26,4,ink)
c.line(21,9,26,9,ink)
c.line(22,4,25,4,goldhi)
# thread guide and thin cream thread
c.line(14,8,14,10,steel)
c.line(14,8,21,7,'#c6b990')
c.set(14,8,white)
# brass maker emblem, stitch length control
c.rect(21,17,4,2,goldsh)
c.line(22,17,24,17,goldhi)
c.rect(33,25,2,3,ink)
c.set(33,25,steel)
# bed screws and rim glints
c.set(34,34,steel)
c.set(8,35,steel)
c.line(27,35,31,35,light)
view(result,scale=8)
finish(result)
