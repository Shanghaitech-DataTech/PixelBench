c = new_canvas(48,48,name='vintage-sewing-machine')
ink='#191c27'
dark='#273340'
mid='#40505a'
light='#697b80'
brass='#ba894b'
gold='#edc97b'
# angled wooden plinth
c.poly([(4,33),(36,31),(44,35),(44,40),(11,44),(3,39)],ink)
c.poly([(4,34),(35,32),(43,35),(11,40)],'#9b613e')
c.poly([(4,36),(11,40),(43,36),(43,39),(11,43),(4,39)],'#613c32')
c.line(12,41,41,37,'#b77c49')
# enamel machine bed
c.poly([(7,32),(34,30),(40,33),(40,36),(12,39),(6,35)],ink)
c.poly([(8,32),(33,31),(38,33),(12,37),(7,35)],mid)
c.line(12,37,38,34,brass)
c.line(9,33,31,31,light)
# cloth draped over front edge
c.poly([(11,31),(22,30),(28,33),(24,36),(26,41),(21,44),(16,42),(15,37),(10,35)],'#702738')
c.poly([(11,31),(21,31),(26,33),(21,36),(23,42),(20,43),(17,41),(16,36),(11,35)],'#bd3c4a')
c.poly([(12,32),(19,32),(22,33),(18,35),(19,40),(17,39),(16,35)],'#ef6463')
c.line(23,36,24,40,'#e65055')
# right pillar and curved upper arm silhouette
c.path('M 9 12 L 13 9 L 30 9 Q 35 9 36 15 L 36 28 L 38 31 L 36 33 L 27 34 L 25 31 L 28 28 L 28 19 Q 28 17 24 17 L 16 17 L 15 23 L 9 23 Z',ink)
c.path('M 10 12 L 14 10 L 29 10 Q 33 10 34 15 L 34 28 L 36 31 L 29 32 L 28 30 L 30 28 L 30 18 Q 29 15 24 15 L 14 15 L 13 21 L 10 21 Z',dark)
c.path('M 11 12 L 15 11 L 28 11 Q 32 11 32 13 L 15 13 L 12 16 Z',mid)
c.line(16,11,28,11,light)
c.line(32,18,32,28,mid)
c.line(30,30,34,30,brass)
# gilt ornament
c.line(17,14,25,14,brass)
c.set(19,13,gold)
c.set(23,13,gold)
c.poly([(31,21),(33,23),(31,25),(30,23)],brass)
c.set(31,23,gold)
# handwheel behind right side, rim and spokes
c.ellipse(37,16,6,8,ink)
c.ellipse(37,16,5,7,light)
c.ellipse(37,16,3,5,ink)
c.line(37,11,37,21,mid)
c.line(34,13,40,19,light)
c.line(34,19,40,13,mid)
c.ellipse(37,16,2,2,'#a2afb0')
c.set(37,15,'#e3e4ce')
c.line(42,13,42,18,'#b6c2bc')
# spool pin and thread spool
c.line(26,4,26,9,'#b8c5c1')
c.rect(22,4,7,2,brass)
c.rect(23,2,5,5,'#dec69a')
c.line(23,3,27,3,'#f2e3bd')
c.line(23,5,27,5,'#a88764')
c.line(22,7,29,7,gold)
c.line(23,8,13,10,'#c8a97a')
# faceplate
c.poly([(9,12),(13,12),(14,15),(13,23),(9,23),(8,19)],'#82918f')
c.line(9,13,9,20,'#d3d6be')
c.line(12,14,12,21,mid)
c.set(10,14,ink)
c.set(10,21,ink)
# tension dial
c.circle(16,19,2,ink)
c.circle(16,19,1,brass)
c.set(16,18,gold)
c.line(15,21,12,25,'#b7a28b')
# needle rod and presser bar
c.line(10,24,10,29,mid)
c.line(11,24,11,30,'#dce2d4')
c.line(14,23,14,29,ink)
c.line(14,24,14,29,'#a9bab8')
c.line(11,30,11,33,'#e8e5cf')
c.line(14,29,15,31,'#a9bab8')
c.line(13,32,17,32,ink)
c.line(13,31,17,31,'#e0e2d2')
# small bed screw
c.set(32,34,'#b5b8a5')
view(c)
finish(c)
