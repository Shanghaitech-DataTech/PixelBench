import math
result = new_canvas(128,128,name='motorcycle')
c=result
ink='#111319'; tire='#171b22'; edge='#303640'; dark='#252b35'; mid='#414a56'; steel='#8997a3'; light='#c1cbd1'; white='#e8eff0'; red='#d73245'; rlight='#ff6370'
# tires and rims
for x,y in [(29,91),(101,91)]:
 c.circle(x,y,22,ink); c.circle(x,y,20,tire)
 c.path(f'M {x-18} {y+5} Q {x-22} {y-12} {x-7} {y-18}',edge,False)
 c.path(f'M {x+9} {y+17} Q {x+20} {y+10} {x+19} {y-4}',edge,False)
 c.circle(x,y,15,'#59616b'); c.circle(x,y,13,'#10151c')
 for a in range(0,360,60):
  t=math.radians(a); t2=t+0.17
  pts=[(x+int(3*math.cos(t)),y+int(3*math.sin(t))),(x+int(12*math.cos(t2)),y+int(12*math.sin(t2))),(x+int(12*math.cos(t2+.15)),y+int(12*math.sin(t2+.15))),(x+int(4*math.cos(t+.5)),y+int(4*math.sin(t+.5)))]
  c.poly(pts,white)
 c.circle(x,y,7,steel); c.circle(x,y,5,'#58626d')
 for a in range(0,360,60):
  t=math.radians(a); c.set(x+round(6*math.cos(t)),y+round(6*math.sin(t)),ink)
 c.circle(x,y,2,light)
# rear suspension
c.poly([(29,87),(52,75),(65,83),(62,89),(30,95)],ink)
c.poly([(30,88),(52,79),(59,82),(52,85),(30,92)],steel)
c.line(34,88,52,82,light)
c.line(37,89,52,86,mid)
# rear spring
c.line(43,66,53,83,ink)
c.line(46,65,56,82,steel)
for i in range(5):
 c.line(44+i*2,68+i*3,50+i*2,67+i*3,red)
# engine undercarriage
c.poly([(46,64),(67,62),(81,73),(78,92),(66,100),(48,94),(42,82)],ink)
c.poly([(49,67),(62,66),(69,74),(66,89),(47,87)],mid)
for y in [70,73,76]:
 c.line(48,y,61,y,steel)
c.circle(59,84,11,'#1b222b'); c.circle(59,84,9,steel); c.circle(59,84,7,'#64717e')
c.path('M 54 88 Q 49 80 58 78',light,False)
c.circle(59,84,3,'#768591')
for x,y in [(59,76),(66,84),(59,92),(51,84)]: c.set(x,y,light)
# exhaust header and belly
c.path('M 72 77 Q 86 92 71 96 L 55 96',steel,False)
c.path('M 74 77 Q 88 93 72 98 L 55 98',mid,False)
# tubular frame triangular
for pts,col in [([(37,60),(65,61),(78,73),(62,91),(37,60)],ink), ([(39,61),(64,63),(73,73),(61,87),(39,61)],steel)]:
 for a,b in zip(pts,pts[1:]):
  c.line(*a,*b,col)
c.line(40,62,60,82,light); c.line(43,63,66,65,light)
c.line(62,86,72,74,light)
# tail silhouette and seat
c.poly([(8,48),(25,50),(40,54),(48,60),(39,66),(23,60),(13,57)],ink)
c.poly([(9,49),(25,52),(39,57),(33,61),(16,55)],mid)
c.poly([(13,51),(25,53),(34,57),(26,56)],steel)
c.poly([(10,52),(19,54),(17,57),(11,55)],red)
c.line(11,52,17,54,rlight)
c.poly([(23,48),(36,49),(48,55),(43,59),(28,53),(22,52)],'#0b0f15')
c.line(27,48,35,49,'#525b67')
# tank
c.poly([(40,55),(47,46),(57,43),(70,45),(78,53),(72,65),(55,66)],ink)
c.poly([(43,54),(49,48),(58,45),(68,47),(73,53),(67,60),(53,61)],mid)
c.poly([(49,48),(58,45),(67,47),(70,50),(58,48)],'#596471')
c.line(56,45,61,45,steel)
c.poly([(43,56),(53,61),(68,61),(65,65),(53,64)],dark)
# windscreen and nose
c.poly([(75,47),(74,33),(78,32),(90,44),(92,50)],ink)
c.poly([(77,36),(79,37),(87,45),(79,43)],'#2b3440')
c.line(76,33,86,43,'#5c6672')
c.line(70,49,77,44,steel); c.line(69,48,75,48,ink)
# front fork behind cowling
c.poly([(83,61),(88,59),(103,90),(99,94)],ink)
c.poly([(85,63),(88,64),(101,88),(98,89)],light)
c.line(87,65,99,87,white)
c.poly([(95,82),(99,80),(104,91),(100,94)],steel)
c.circle(101,91,3,mid); c.circle(101,91,1,white)
# front fender
c.path('M 80 80 Q 87 65 104 69 Q 114 70 119 80 L 111 77 Q 95 69 84 82 Z',ink)
c.path('M 84 77 Q 97 65 111 74 L 104 73 Q 93 71 84 79 Z',mid)
c.line(90,72,101,70,red)
# wide angular fairing
c.poly([(72,48),(86,46),(99,52),(105,61),(98,65),(87,65),(83,81),(76,95),(59,98),(65,88),(69,74),(63,62)],ink)
c.poly([(74,50),(85,48),(97,54),(101,59),(94,62),(84,62),(79,78),(69,88),(72,72),(66,61)],'#3c4551')
c.poly([(74,50),(85,48),(97,54),(99,56),(86,52),(77,53)],'#626d79')
c.poly([(67,63),(74,67),(84,64),(80,76),(70,87)],dark)
c.poly([(66,90),(78,82),(73,94),(62,96)],mid)
# side red streak
c.poly([(67,58),(77,61),(93,57),(100,58),(94,61),(77,65),(69,62)],red)
c.line(78,61,92,58,rlight)
c.poly([(68,89),(77,84),(74,88),(65,94),(62,94)],red)
# vents
c.poly([(75,68),(81,66),(78,71),(72,75)],'#10161e')
c.line(74,74,78,72,'#59636f')
c.poly([(72,76),(78,73),(75,78),(70,82)],'#10161e')
# headlamp
c.poly([(96,54),(101,57),(102,60),(97,60),(92,57)],ink)
c.line(95,56,100,58,white); c.line(98,59,101,59,steel)
# fasteners
for x,y in [(72,54),(69,64),(80,64),(70,88)]: c.set(x,y,light)
# low exhaust can
c.poly([(29,81),(34,78),(50,89),(48,96),(42,96),(28,86)],ink)
c.poly([(31,81),(34,80),(48,90),(46,94),(42,93),(30,85)],steel)
c.line(33,81,46,90,light)
c.poly([(29,81),(32,82),(31,86),(28,85)],'#3c4650')
c.line(40,85,38,90,mid)
# footpeg
c.line(54,91,49,94,ink); c.rect(47,93,8,2,light)
view(c)
save('motorcycle',c)
finish(result)
