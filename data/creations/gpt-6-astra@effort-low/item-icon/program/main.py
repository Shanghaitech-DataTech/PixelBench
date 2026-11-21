result = new_canvas(32,32)
c=result
dark='#241f2b'
shadow='#69402d'
gold='#c58b37'
light='#f8d779'
# suspension loop
c.rect(13,1,6,2,dark)
c.rect(11,3,10,5,dark)
c.rect(13,3,6,4,gold)
c.rect(14,3,4,2,dark)
c.rect(12,4,1,2,light)
# chunky outer casing
c.poly([(10,6),(21,6),(25,8),(28,12),(29,16),(28,23),(24,27),(20,29),(11,29),(6,27),(3,23),(2,17),(3,12),(6,8)],dark)
c.poly([(10,8),(21,8),(25,11),(27,15),(27,21),(24,25),(20,27),(11,27),(7,25),(4,21),(4,14),(7,10)],shadow)
c.poly([(10,7),(21,7),(25,10),(27,14),(27,20),(24,24),(20,26),(11,26),(7,24),(4,20),(4,14),(7,10)],gold)
c.line(10,8,20,8,light)
c.line(6,12,9,9,light)
c.line(5,14,5,19,light)
c.line(11,26,20,26,'#e8ae4b')
c.line(24,23,26,20,'#946030')
# recessed dial
c.circle(16,17,10,dark)
c.circle(16,17,8,'#60513c')
c.circle(16,16,8,'#a77b3b')
c.circle(16,16,7,'#e5bd66')
c.circle(16,16,6,'#ce9f50')
# cardinal engraved tick marks
c.line(16,9,16,11,shadow)
c.line(16,22,16,24,shadow)
c.line(9,16,11,16,shadow)
c.line(22,16,24,16,shadow)
for x,y in [(11,11),(21,11),(11,21),(21,21)]:
 c.set(x,y,shadow)
# compass rose diagonal points
c.poly([(11,12),(16,14),(21,12),(19,17),(21,21),(16,19),(11,21),(13,16)],shadow)
c.line(12,12,20,20,'#f8d779')
c.line(12,20,20,12,'#f8d779')
# elongated crystal compass needle
c.poly([(16,10),(20,16),(16,23),(12,17)],dark)
c.poly([(16,11),(19,16),(16,21),(13,17)],'#146491')
c.poly([(16,11),(16,16),(13,17)],'#7fe4ef')
c.poly([(16,11),(19,16),(16,16)],'#36b4da')
c.poly([(13,17),(16,16),(16,21)],'#258fbd')
c.poly([(16,16),(19,16),(16,21)],'#17496e')
c.set(16,13,'#ddfbf5')
c.set(15,14,'#ddfbf5')
c.set(16,16,'#b4f4f4')
# rim rivets and aged nicks
for x,y in [(7,10),(24,10),(7,23),(24,23)]:
 c.set(x,y,shadow)
 c.set(x,y-1,light)
c.set(20,7,shadow)
c.set(21,8,shadow)
c.set(4,18,shadow)
c.set(12,26,shadow)
c.set(13,26,shadow)
view(result)
finish(result)
