result = new_canvas(48,48)
c=result
ink='#20232b'; dark='#303944'; mid='#46535b'; light='#71818a'; steel='#b4c6ca'; shine='#e3e6d5'; gold='#b68a49'; bright='#e2bd70'
# angled cast iron base
c.poly([(4,34),(34,31),(44,35),(43,40),(12,44),(3,39)],ink)
c.poly([(4,34),(34,31),(44,35),(12,40),(3,37)],mid)
c.poly([(5,35),(33,32),(40,35),(12,39)],dark)
c.line(12,40,42,36,light)
c.line(12,42,41,38,'#111b26')
c.line(5,38,10,40,gold)
c.line(14,41,39,37,gold)
# feet
c.rect(7,40,4,3,ink);c.rect(36,39,4,3,ink)
# wheel behind right pillar
c.ellipse(38,18,6,9,ink)
c.ellipse(39,17,5,8,light)
c.ellipse(39,17,4,7,steel)
c.ellipse(39,17,3,6,ink)
c.line(39,11,39,23,light)
c.line(36,14,42,20,light)
c.line(36,20,42,14,light)
c.ellipse(39,17,2,2,gold)
c.set(39,16,shine)
c.rect(42,21,3,3,ink);c.set(44,21,light)
# pillar and curved arm silhouette
c.path('M 27 12 L 33 12 Q 36 13 36 18 L 35 29 Q 35 32 39 33 L 38 35 L 26 37 L 22 35 L 22 32 Q 28 31 28 27 L 28 21 Q 28 18 24 18 L 15 19 L 14 24 L 8 25 L 7 13 Q 7 10 11 10 L 23 10 Z',ink)
c.path('M 10 12 L 23 12 L 28 14 L 32 14 Q 34 14 34 18 L 33 29 L 35 32 L 29 34 L 25 34 Q 30 31 30 27 L 30 20 Q 29 16 24 16 L 14 17 L 13 22 L 10 23 Z',dark)
c.path('M 10 12 L 22 12 L 27 14 L 31 14 L 32 16 L 26 15 L 22 14 L 11 15 Z',mid)
c.line(30,19,31,28,mid)
c.line(32,19,32,26,light)
c.line(25,34,34,32,gold)
c.line(27,35,36,33,bright)
# gold pinstripe and vintage ornament
c.line(15,15,23,15,gold);c.line(24,16,27,17,gold)
c.set(16,13,bright);c.set(19,13,gold)
c.line(31,21,31,25,gold)
c.set(30,23,bright);c.set(32,23,bright)
# front silver faceplate
c.poly([(8,14),(12,13),(13,22),(10,24),(8,23)],light)
c.line(9,15,9,21,steel)
c.line(11,15,12,21,mid)
c.set(10,14,shine);c.set(10,22,ink)
# top spool and spindle
c.line(29,5,29,12,steel)
c.rect(25,6,7,2,ink)
c.rect(26,7,5,4,'#b27145')
c.line(26,7,30,7,'#ecd69b');c.line(26,9,30,9,'#d8ac68')
c.rect(25,11,7,1,gold)
c.line(26,7,14,8,'#d5b47b');c.line(14,8,10,12,'#d5b47b')
# tension knob
c.rect(6,17,3,4,ink);c.rect(5,18,3,2,gold);c.set(5,18,bright)
# needle plate on base
c.poly([(8,34),(17,33),(22,35),(12,37)],light)
c.line(11,35,17,34,steel)
c.line(13,36,18,35,ink)
# red fabric draped over front edge
c.poly([(16,31),(23,31),(26,34),(23,37),(24,41),(20,44),(14,43),(13,38),(11,35)],'#6e2438')
c.poly([(16,32),(22,32),(24,34),(20,37),(21,42),(18,43),(15,42),(15,37),(12,35)],'#ba3549')
c.line(16,33,21,33,'#ee6c65');c.line(14,35,17,37,'#e75056')
c.line(17,38,18,42,'#e75056');c.line(22,37,23,40,'#8e293f')
# needle bar and presser assembly on top of fabric
c.rect(9,24,2,7,mid);c.line(9,24,9,30,steel)
c.line(10,30,10,34,shine)
c.line(13,23,13,31,steel);c.set(13,24,shine)
c.line(13,31,14,33,mid)
c.line(12,34,16,34,ink);c.line(12,33,16,33,steel)
c.set(16,32,shine)
# small pillar fastener
c.set(33,30,steel)
view(c)
finish(result)
