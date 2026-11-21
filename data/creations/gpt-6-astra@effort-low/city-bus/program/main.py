result = new_canvas(64,32,name='city_bus')
c=result
ink='#182632'; dark='#263b49'; glass='#34566b'; light='#8ec9d6'; body='#e2ece8'; shade='#a1b8bb'; teal='#168e91'; hi='#55c7c1'
# roof and rounded body silhouette
c.poly([(4,7),(7,5),(54,5),(58,7),(60,11),(60,24),(58,26),(4,26),(2,24),(2,10)],ink)
c.rect(5,7,50,2,body)
c.line(8,6,52,6,'#f5f7e8')
c.rect(3,10,56,14,body)
c.rect(5,9,51,2,body)
c.rect(4,23,55,3,shade)
# low continuous teal livery
c.rect(3,19,56,5,teal)
c.line(4,19,58,19,hi)
c.line(4,24,58,24,'#116469')
# window band
c.rect(5,10,50,8,ink)
for x,w in [(6,8),(16,8),(26,8),(36,7)]:
 c.rect(x,11,w,6,glass)
 c.line(x,11,x+w-1,11,light)
 c.line(x,12,x+3,15,'#547f91')
 c.line(x+1,16,x+w-1,16,'#416b7e')
# rear door, double leaf
c.rect(15,10,10,15,ink)
for x in (16,20):
 c.rect(x,11,3,12,shade)
 c.rect(x,11,3,8,glass)
 c.line(x,11,x+2,11,light)
 c.rect(x,20,3,3,teal)
c.line(19,11,19,24,dark)
c.set(18,20,'#e2ece8');c.set(21,20,'#e2ece8')
c.line(16,24,23,24,'#d1ded8')
# front entrance and driver's windshield
c.rect(45,10,10,15,ink)
for x in (46,50):
 c.rect(x,11,3,12,glass)
 c.line(x,11,x+2,11,light)
 c.line(x,12,x+2,15,'#547f91')
 c.rect(x,20,3,3,teal)
c.line(49,11,49,24,dark)
c.set(48,20,body);c.set(50,20,body)
c.line(46,24,53,24,shade)
c.poly([(55,10),(57,10),(58,12),(58,18),(55,18)],glass)
c.line(56,11,57,13,light)
c.line(56,18,58,18,ink)
# simplified dot-matrix route display
c.rect(44,7,12,3,ink)
for x,y in [(45,8),(46,8),(48,8),(50,8),(51,8),(53,8),(54,8)]:c.set(x,y,'#ffc46b')
# body fittings and lamps
c.rect(4,20,2,3,'#b6464d');c.set(4,20,'#ff8b76')
c.rect(57,20,2,2,'#fff2b0');c.set(58,22,'#e9a551')
c.rect(3,24,3,1,dark);c.rect(56,24,4,1,dark)
c.line(29,21,40,21,'#11777e')
c.rect(6,18,5,1,shade)
# two recessed wheel wells and tires
for x in (11,39):
 c.circle(x,25,4,ink)
 c.circle(x,25,3,'#26313b')
 c.circle(x,25,2,'#8ba2ad')
 c.set(x,24,'#e2ece8');c.set(x,25,'#455d6b');c.set(x+1,26,'#566e7d')
 c.line(x-2,28,x+2,28,ink)
# roof equipment and mirror
c.rect(17,4,18,2,shade)
c.line(19,4,32,4,body)
c.line(58,11,61,11,ink);c.rect(61,11,1,4,dark)
view(result)
finish(result)
