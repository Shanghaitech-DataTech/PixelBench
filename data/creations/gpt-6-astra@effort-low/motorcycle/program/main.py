import math
result = new_canvas(128,128)
c=result
ink='#101117'; tire='#191b21'; rubber='#272a32'; edge='#3a3f48'; mid='#505762'; silver='#a5afba'; light='#e3e9ed'; white='#f9fbff'; red='#ce263b'; bright='#ff4d56'
# thick tires and rims
for x,y in [(29,88),(101,88)]:
 c.circle(x,y,21,ink).circle(x,y,19,tire)
 c.path(f'M {x-17} {y+5} Q {x-21} {y-11} {x-8} {y-17} Q {x+3} {y-22} {x+13} {y-13}',rubber,False)
 c.circle(x,y,14,edge).circle(x,y,12,silver).circle(x,y,10,'#232833')
 for a in range(0,360,60):
  t=math.radians(a)
  xx=x+round(10*math.cos(t)); yy=y+round(10*math.sin(t))
  c.line(x,y,xx,yy,light)
  c.line(x+1,y,xx+1,yy,silver)
 c.circle(x,y,5,mid).circle(x,y,3,silver).set(x-1,y-1,white)
# rear hugger
c.path('M 10 76 Q 18 62 33 64 L 45 71 L 41 74 Q 26 66 14 78 Z',ink)
c.path('M 14 72 Q 24 65 34 68',mid,False)
# chassis and engine dark mass
c.poly([(33,58),(51,48),(77,51),(88,66),(75,89),(47,91),(35,77)],ink)
# tubular frame
for pts in [(35,61,61,78),(35,61,73,58),(61,78,73,58),(40,62,50,83)]:
 x,y,X,Y=pts
 c.line(x,y,X,Y,edge); c.line(x,y-1,X,Y-1,silver)
c.poly([(42,68),(56,61),(68,68),(68,83),(58,91),(44,85)],'#343942')
# cylinder finning
c.poly([(48,62),(61,60),(66,70),(49,75)],mid)
for y in [64,67,70]: c.line(49,y,62,y-2,silver)
c.circle(56,79,10,ink).circle(56,79,8,silver).circle(56,79,6,'#747f8b')
c.path('M 51 82 Q 48 76 54 73',light,False)
c.circle(56,79,3,mid)
for x,y in [(56,72),(62,81),(51,84)]: c.set(x,y,light)
# swingarm
c.poly([(27,86),(47,79),(54,84),(30,93),(25,91)],ink)
c.poly([(28,87),(46,82),(48,85),(29,90)],'#7c8794')
c.line(31,88,44,84,light)
c.circle(29,88,3,mid).set(29,87,light)
# exhaust below engine and upswept silencer
c.path('M 65 76 L 73 81 L 70 91 L 49 92 L 37 85',edge,False)
c.line(49,90,69,90,silver)
c.poly([(21,73),(25,69),(46,80),(43,87),(37,86)],ink)
c.poly([(23,73),(26,71),(43,81),(41,84),(36,83)],mid)
c.line(27,73,41,80,silver)
c.line(24,72,22,75,light)
# front forks
c.poly([(83,52),(88,51),(106,88),(100,92)],ink)
c.poly([(84,55),(87,54),(101,83),(98,84)],silver)
c.line(84,55,97,81,white)
c.poly([(97,77),(101,77),(106,89),(100,91)],'#747e8a')
c.line(99,79,103,87,light)
c.circle(101,88,3,edge).set(101,87,light)
# front fender
c.path('M 83 76 Q 99 63 113 73 L 117 79 L 111 78 Q 101 70 88 79 Z',ink)
c.path('M 87 74 Q 99 67 110 73',mid,False)
c.line(110,74,114,77,red)
# upswept tail fairing
c.poly([(10,44),(31,46),(46,54),(42,62),(25,58),(16,52)],ink)
c.poly([(12,46),(30,48),(40,53),(27,53),(19,50)],'#555c67')
c.line(13,45,29,47,silver)
c.poly([(12,49),(21,51),(23,54),(16,53)],red).line(14,50,20,52,bright)
# seat
c.poly([(26,45),(36,46),(47,51),(57,51),(56,56),(42,56),(33,51),(24,49)],ink)
c.line(28,46,36,48,edge)
# tank
c.path('M 43 52 L 49 44 Q 57 39 66 41 L 77 47 L 79 57 L 64 63 L 51 60 Z',ink)
c.path('M 46 51 L 51 46 L 60 43 L 67 44 L 74 48 L 73 54 L 61 58 L 52 57 Z','#3a404a')
c.path('M 50 46 L 59 43 L 66 44 L 71 47', '#737c86',False)
c.poly([(49,54),(60,56),(73,51),(72,55),(60,60),(50,57)],red)
c.line(52,54,60,55,bright)
c.line(59,43,63,43,silver)
# windscreen and upper nose
c.poly([(75,40),(72,30),(77,30),(91,41),(94,48),(84,48)],ink)
c.poly([(76,33),(79,34),(89,42),(80,40)],'#303640')
c.line(75,31,86,38,'#59616c')
# mirror
c.line(84,43,86,34,edge)
c.poly([(83,30),(91,31),(93,34),(91,36),(84,34)],ink)
c.line(85,31,90,32,mid)
# wide fairing right side
c.poly([(76,44),(91,42),(100,48),(106,58),(98,65),(88,66),(80,86),(70,91),(64,88),(71,69),(68,61)],ink)
c.poly([(78,47),(91,45),(98,49),(102,56),(95,61),(85,62),(77,81),(70,86),(73,69),(71,61)],'#414752')
c.poly([(78,47),(91,45),(98,49),(98,51),(85,50),(76,57),(73,59)],'#626b76')
c.poly([(84,64),(93,63),(80,88),(69,90),(65,87),(72,85)],'#292e38')
# angular red graphic
c.poly([(74,64),(83,57),(100,55),(97,59),(84,61),(76,70),(70,82)],red)
c.line(84,58,99,56,bright)
c.poly([(75,74),(80,68),(76,82),(70,86)],'#7d1e32')
# intake and lamp
c.poly([(88,50),(99,51),(102,55),(94,55)],ink)
c.line(94,51,99,52,white).line(96,53,100,53,silver)
c.poly([(77,55),(83,52),(81,56),(76,60)],ink)
c.line(77,58,80,55,mid)
# fasteners and controls
for x,y in [(75,63),(80,48),(78,80)]: c.set(x,y,silver)
c.line(73,44,77,41,silver).line(69,41,76,41,ink)
c.line(44,79,40,78,silver).rect(38,77,6,2,edge)
c.line(63,90,76,90,ink)
view(c)
finish(result)
