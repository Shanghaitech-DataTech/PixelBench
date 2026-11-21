import random
r=random.Random(24)
c=new_canvas(128,128,background='#70ccef',name='summer-seaside')
# clear sky
c.rect(0,29,128,21,'#8adcf3')
c.rect(0,43,128,8,'#a3e4f3')
# sun
c.circle(102,17,11,'#ffe397')
c.circle(102,17,8,'#fff5bf')
c.rect(98,11,6,2,'#fffbdc')
# soft stepped cloud silhouettes
def cloud(x,y,s):
 c.rect(x,y+4,s,5,'#d9f1f6')
 c.rect(x+3,y+1,s-7,7,'#f8fcf4')
 c.rect(x+7,y-2,8,8,'#f8fcf4')
 c.rect(x+15,y,8,7,'#f8fcf4')
 c.rect(x+2,y+8,s-5,2,'#c1e9f3')
cloud(9,16,32)
cloud(51,30,28)
cloud(111,36,23)
# layered sea
c.rect(0,50,128,8,'#2379b8')
c.rect(0,58,128,10,'#238fc3')
c.rect(0,68,128,12,'#26a9ca')
c.rect(0,80,128,15,'#37c4d0')
c.line(0,50,127,50,'#2875ab')
# sunlight and ripples
for i in range(115):
 y=r.randrange(53,94);x=r.randrange(128);w=r.randrange(2,9)
 col=('#429fce' if y<68 else '#69d9dc')
 if x>84 and x<117: col=('#87dce3' if y>65 else '#6dbbd9')
 c.line(x,y,min(127,x+w),y,col)
# sand shoreline, diagonal curve
shore=[(0,86),(13,88),(24,90),(37,91),(51,90),(66,87),(81,84),(96,81),(112,79),(127,78),(127,128),(0,128)]
c.poly(shore,'#f6d58a')
# wet golden edge
c.path('M0 86 L13 88 L24 90 L37 91 L51 90 L66 87 L81 84 L96 81 L112 79 L127 78 L127 83 L110 84 L96 86 L82 89 L67 92 L51 95 L36 96 L23 95 L11 93 L0 91Z','#dfbc79')
# surf banks
c.path('M0 82 L14 84 L26 87 L39 88 L51 87 L65 84 L80 81 L95 78 L112 76 L127 75 L127 79 L111 80 L97 82 L81 85 L66 88 L51 91 L37 92 L24 91 L12 88 L0 87Z','#dcfbef')
c.path('M0 82 L14 84 L26 87 L39 88 L51 87 L65 84 L80 81 L95 78 L112 76 L127 75','#a1eee5',False)
for x,y,w in [(3,86,7),(18,89,6),(30,90,10),(47,89,7),(60,87,6),(75,84,9),(93,80,5),(108,78,8),(120,77,5)]:
 c.line(x,y,x+w,y,'#ffffff')
# distant curling wave
c.path('M0 73 L13 74 L23 73 L34 74 M48 76 L61 75 L72 73 L89 72 M105 69 L117 69 L127 68','#b7f2e9',False)
c.line(5,74,15,74,'#f4fff5');c.line(61,76,70,74,'#f4fff5')
# beach sand scattered small flecks
for i in range(95):
 x=r.randrange(128);y=r.randrange(96,128)
 c.line(x,y,min(127,x+r.choice([0,1,2])),y,r.choice(['#e8c37c','#ffe5a3','#fbe0a0']))
# sailboat, distant
c.line(82,52,82,67,'#e9e4ce')
c.poly([(80,54),(80,64),(69,64)],'#fffdf0')
c.poly([(84,57),(90,64),(84,64)],'#d1eaf0')
c.line(69,66,91,66,'#fff9df')
c.poly([(70,67),(89,67),(86,70),(74,70)],'#344e70')
c.line(76,72,88,72,'#75d5df')
# exactly two gulls
for x,y in [(40,40),(62,18)]:
 c.line(x-5,y-2,x-2,y-1,'#397b9c');c.line(x-2,y-1,x,y+1,'#397b9c');c.line(x,y+1,x+3,y-2,'#397b9c');c.line(x+3,y-2,x+6,y-2,'#397b9c')
 c.set(x-3,y-2,'#fffdf3');c.set(x+3,y-3,'#fffdf3')
# towel shadow and woven striped towel
c.poly([(73,101),(94,97),(109,119),(85,124)],'#d6b273')
c.poly([(71,99),(93,96),(105,117),(83,122)],'#fff7da')
for a,b in [(2,5),(9,12),(16,19)]:
 c.poly([(71+int(a*.57),99+a),(93+int(a*.57),96+a),(93+int(b*.57),96+b),(71+int(b*.57),99+b)],'#25a9b7')
 c.line(72+int(a*.57),99+a,92+int(a*.57),96+a,'#69d2cb')
for x,y in [(83,122),(87,121),(91,120),(95,120),(99,119),(103,118)]:c.line(x,y,x+1,y+2,'#fff5d7')
# umbrella cast shadow
c.ellipse(36,113,25,7,'#ddba79')
c.ellipse(31,111,20,5,'#d3ad6d')
# pole
c.line(33,77,35,112,'#916c4e');c.line(32,77,34,112,'#fff0bf');c.set(34,113,'#9f8055')
# umbrella dome, segmented scalloped canopy
c.poly([(6,80),(9,74),(15,67),(24,62),(33,60),(43,63),(52,69),(60,79),(62,83),(55,81),(49,83),(41,81),(34,83),(26,80),(19,82),(12,79)],'#d94b48')
c.poly([(8,77),(15,68),(25,63),(33,61),(24,68),(19,79),(13,77)],'#fff6de')
c.poly([(33,61),(42,64),(47,71),(50,80),(42,79),(35,81),(35,70)],'#fff6de')
c.poly([(33,61),(28,68),(26,79),(20,80),(22,72),(27,65)],'#f66557')
c.poly([(34,61),(39,67),(43,77),(42,79),(35,81),(35,70)],'#e7e4d2')
c.poly([(43,64),(52,70),(58,77),(60,81),(54,79),(50,80),(47,71)],'#f76b57')
c.line(8,80,12,79,'#b43f48');c.line(13,80,19,82,'#d9d4bc');c.line(26,80,34,83,'#b43f48');c.line(35,83,41,81,'#b8ceca');c.line(49,83,55,81,'#b43f48')
c.rect(32,58,2,3,'#9f7051')
# flip flops at right
for x,y in [(111,103),(118,108)]:
 c.ellipse(x,y+2,3,7,'#cfab6b')
 c.ellipse(x,y,3,6,'#24576b')
 c.ellipse(x,y-1,2,5,'#388c98')
 c.line(x-2,y-2,x,y+1,'#ff8b65');c.line(x,y+1,x+2,y-3,'#ff8b65');c.set(x,y+2,'#ffd295')
# shell
c.poly([(55,119),(56,116),(59,115),(62,117),(62,119)],'#fff1cf')
c.line(58,116,59,119,'#e5a284');c.set(61,118,'#e5a284')
view(c)
finish(c)
