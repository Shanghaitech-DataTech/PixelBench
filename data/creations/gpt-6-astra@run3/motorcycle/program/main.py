import math
result = new_canvas(128,128,name='motorcycle')
c=result
ink='#101218'; black='#181b22'; tire='#20242b'; tread='#30343c'; dark='#292e38'; gray='#3e4651'; mid='#596471'; steel='#82929e'; silver='#b4c3ca'; white='#e5eef0'; red='#c92b3b'; bright='#f54b50'; burg='#6b202f'
# tires and inset rims
for x,y in [(29,91),(101,91)]:
 c.circle(x,y,20,ink)
 c.circle(x,y,18,tire)
 c.path(f'M {x-16} {y+7} Q {x-22} {y-8} {x-8} {y-16} Q {x+4} {y-22} {x+15} {y-11}',tread,False)
 c.circle(x,y,14,black)
 c.circle(x,y,12,steel)
 c.circle(x,y,10,ink)
 # narrow white paired spokes
 for a in range(0,360,60):
  r=math.radians(a-15)
  px=int(round(x+10*math.cos(r))); py=int(round(y+10*math.sin(r)))
  qx=int(round(x+4*math.cos(r+.40))); qy=int(round(y+4*math.sin(r+.40)))
  c.line(qx,qy,px,py,silver)
  c.line(x,y,px,py,white)
 c.circle(x,y,4,gray)
 c.circle(x,y,2,silver)
 c.set(x-1,y-1,white)
# rear sprocket and chain
c.circle(29,91,6,mid,False)
c.line(29,85,56,82,steel); c.line(29,97,59,90,gray)
c.line(31,84,53,82,gray)
# swingarm
c.poly([(27,89),(55,78),(63,81),(61,87),(28,95)],ink)
c.poly([(29,90),(55,81),(60,82),(58,86),(29,93)],gray)
c.line(30,90,54,82,silver)
c.circle(29,91,2,silver)
# under-seat mechanical structure
c.poly([(27,54),(43,52),(68,60),(61,84),(44,82),(36,65)],ink)
c.line(33,57,53,75,steel); c.line(34,57,59,61,silver)
c.line(53,75,59,61,gray)
# red rear shock
c.line(43,62,49,81,ink)
for i in range(5):
 c.line(42+i,65+i*3,47+i,64+i*3,red)
c.line(46,64,51,79,silver)
# engine casing and cylinder fins
c.poly([(52,64),(66,61),(76,72),(70,89),(54,91),(46,81)],black)
c.poly([(54,64),(64,64),(69,74),(53,76)],gray)
for yy in [66,69,72]: c.line(54,yy,65+(yy-66)//2,yy,steel)
c.circle(59,81,10,ink); c.circle(59,81,8,steel); c.circle(59,82,6,mid)
c.path('M 54 83 Q 51 75 59 74 Q 63 74 65 78',silver,False)
c.circle(59,81,3,gray); c.set(58,80,steel)
for x,y in [(55,75),(65,81),(57,87)]: c.set(x,y,white)
# tubular silver frame over engine
c.line(44,57,75,59,ink); c.line(45,58,60,70,ink)
c.line(45,57,60,68,silver); c.line(46,57,74,60,steel)
c.line(60,68,75,59,silver); c.line(60,69,74,61,gray)
# exhaust downpipes and lower collector
c.path('M 68 73 Q 77 80 72 90 L 54 95',steel,False)
c.path('M 70 73 Q 80 83 74 92 L 55 97',gray,False)
# muffler sweeping up towards rear
c.poly([(20,77),(24,75),(47,89),(52,95),(47,100),(38,95),(20,83)],ink)
c.poly([(23,78),(27,78),(48,91),(48,96),(42,95),(23,82)],gray)
c.line(25,78,46,91,silver); c.line(25,81,43,93,steel)
c.poly([(20,77),(24,78),(24,83),(20,82)],black)
c.line(21,78,21,81,steel)
# body tail: upswept rear
c.poly([(9,45),(26,44),(43,51),(47,57),(34,62),(19,56),(12,52)],ink)
c.poly([(11,46),(26,46),(40,51),(37,56),(20,53)],gray)
c.line(12,46,27,46,steel)
c.poly([(13,51),(27,54),(37,56),(30,59),(18,55)],red)
c.line(17,54,29,58,bright)
# tail lamp
c.line(10,48,15,49,bright); c.line(10,49,14,50,red)
# seat
c.poly([(28,46),(38,47),(48,51),(58,51),(56,57),(40,55)],ink)
c.line(32,47,40,49,mid); c.line(41,50,52,52,dark)
# tank
c.poly([(43,51),(50,42),(60,39),(70,40),(81,48),(79,58),(65,62),(50,58)],ink)
c.poly([(46,50),(52,44),(61,41),(70,43),(77,49),(73,56),(61,58),(51,55)],dark)
c.poly([(51,44),(60,41),(69,42),(73,45),(61,44),(54,47)],gray)
c.line(54,44,61,42,steel)
c.line(60,40,65,40,silver)
c.poly([(48,53),(61,56),(76,51),(73,56),(61,59),(51,56)],black)
c.line(52,54,61,56,red); c.line(61,56,71,53,red)
# front fork behind cowl
c.poly([(85,57),(90,56),(105,91),(100,94)],ink)
c.line(87,60,101,90,steel); c.line(89,61,103,90,white)
c.line(87,60,93,74,gray); c.line(89,60,95,74,silver)
c.circle(101,91,3,mid); c.circle(101,91,1,white)
# front fender
c.path('M 85 79 Q 98 65 113 77 L 115 82 L 109 79 Q 98 72 89 82 Z',ink)
c.path('M 88 78 Q 99 69 110 76 L 111 78 Q 99 72 90 80 Z',gray)
c.line(97,73,104,73,steel)
# tilted screen and cockpit
c.poly([(79,43),(74,30),(79,30),(88,36),(93,46)],ink)
c.poly([(77,32),(81,34),(88,41),(81,39)],dark)
c.line(77,31,82,34,mid)
# handlebars and mirror
c.line(78,44,71,40,steel); c.line(68,40,74,40,ink)
c.line(86,41,92,32,gray)
c.poly([(90,30),(96,30),(98,32),(96,35),(90,34)],ink)
c.line(91,31,95,31,steel)
# wide sculpted front fairing
c.poly([(80,40),(91,43),(103,52),(107,59),(101,65),(91,67),(82,86),(76,96),(58,97),(65,88),(70,73),(68,64),(75,54)],ink)
c.poly([(81,43),(90,45),(101,53),(103,58),(92,60),(80,68),(76,81),(68,90),(65,92),(73,73),(71,64),(78,54)],gray)
c.poly([(80,44),(89,46),(99,53),(90,52),(78,60)],mid)
c.line(82,44,90,46,steel)
c.poly([(91,60),(103,59),(99,64),(89,66),(80,87),(74,93),(66,94),(74,81),(79,68)],dark)
c.poly([(76,71),(81,67),(86,64),(82,75),(77,81)],ink)
c.line(79,71,83,68,mid)
# red stripe that follows fairing
c.poly([(76,61),(88,55),(100,55),(103,58),(89,58),(76,65)],red)
c.line(80,60,89,56,bright)
c.poly([(64,91),(74,89),(80,82),(77,92),(73,95),(61,95)],red)
c.line(65,93,73,93,bright)
# headlight narrow forward eye
c.poly([(98,51),(103,54),(105,58),(101,57),(96,53)],ink)
c.line(99,53,102,55,white); c.set(103,56,silver)
# small fairing fasteners
for x,y in [(77,57),(89,62),(74,87)]: c.set(x,y,silver)
# footpeg bracket
c.poly([(46,78),(52,84),(47,88),(44,86)],silver)
c.poly([(47,81),(50,84),(47,85)],gray)
c.line(43,87,49,87,ink); c.line(43,86,48,86,steel)
view(c)
save('motorcycle',c)
finish(result)
