import random
random.seed(12)
result = new_canvas(128,128,background='#73cfee',name='summer_seaside')
c=result
# clear sky bands
c.rect(0,0,128,20,'#65c5ed')
c.rect(0,20,128,19,'#79d2f1')
c.rect(0,39,128,11,'#95e0f3')
# sun, squared glints
c.circle(104,17,10,'#ffe89a')
c.circle(104,17,8,'#fff3b1')
c.circle(103,16,6,'#fff8d4')
for x,y in [(103,3),(118,16),(91,6),(116,28)]:
 c.rect(x,y,2,2,'#fff0b3')
# soft cloud clusters with cool lower edge
def cloud(x,y):
 c.rect(x,y+5,29,5,'#d2edf5')
 c.rect(x+3,y+3,23,6,'#edfaff')
 c.rect(x+7,y,10,8,'#f9feff')
 c.rect(x+16,y+2,8,6,'#f9feff')
 c.rect(x-2,y+6,31,2,'#f9feff')
 c.rect(x+4,y+10,20,1,'#bce4f1')
cloud(13,12)
cloud(61,29)
c.rect(0,35,16,3,'#d9f3f8');c.rect(3,32,8,4,'#f3fcff')
# ocean depth bands
c.rect(0,49,128,8,'#247cb6')
c.line(0,49,127,49,'#367fb6')
c.rect(0,57,128,8,'#218fc1')
c.rect(0,65,128,9,'#20a5c6')
c.rect(0,74,128,11,'#29b9c9')
c.rect(0,85,128,16,'#51cfcd')
# slanting shore, bottom right dry beach
c.poly([(0,102),(18,99),(36,97),(54,94),(71,90),(89,84),(107,79),(127,77),(127,128),(0,128)],'#eac17b')
c.poly([(0,108),(20,105),(39,102),(57,99),(78,94),(96,88),(112,85),(127,84),(127,128),(0,128)],'#f6d58f')
c.poly([(0,117),(24,111),(49,108),(73,103),(100,94),(127,90),(127,128),(0,128)],'#ffdf9b')
# broad shallows and white crest
c.path('M 0 98 Q 20 100 37 93 Q 58 93 74 87 Q 92 80 106 78 Q 117 77 127 74 L 127 79 Q 116 81 108 82 Q 92 83 76 91 Q 56 97 38 98 Q 18 104 0 103 Z','#b2eee0')
c.path('M 0 100 Q 19 102 38 95 Q 59 95 75 89 Q 92 81 109 80 Q 119 79 127 76', '#f5ffff',fill=False)
c.path('M 0 101 Q 19 103 38 96 Q 59 96 75 90 Q 92 82 109 81 Q 119 80 127 77', '#f5ffff',fill=False)
# horizontal wavelets, restrained clusters
for y,col,n in [(53,'#74bfde',12),(59,'#51b4d5',13),(66,'#6dd2dd',11),(72,'#71d8df',13),(80,'#8de4df',9),(88,'#91e7dc',8)]:
 for i in range(n):
  x=random.randrange(0,124); length=random.randrange(2,9)
  if c.color_name(c.get(x,y)) in ['#eac17b','#f6d58f','#ffdf9b']:continue
  c.line(x,y,min(127,x+length),y,col)
# a curling incoming wave
c.path('M 2 84 Q 18 87 31 82 Q 43 78 53 81 Q 61 82 70 78', '#d3f7ed',fill=False)
c.line(9,86,20,86,'#ffffff');c.line(29,83,34,82,'#ffffff')
c.line(43,80,50,80,'#ffffff');c.line(78,74,90,74,'#d4f8f0')
c.line(93,73,102,73,'#d4f8f0')
# foam bubbles and wet sand tiny light flecks
for x,y in [(5,105),(8,104),(24,101),(30,100),(45,98),(51,97),(66,94),(81,89),(93,86),(102,84),(114,82),(122,81)]:
 c.rect(x,y,2,1,'#fff9df')
for i in range(70):
 x=random.randrange(128);y=random.randrange(90,128)
 if c.color_name(c.get(x,y)) in ['#f6d58f','#ffdf9b']:
  c.rect(x,y,random.choice([1,2]),1,random.choice(['#efc885','#f4ce86','#ffeab4']))
# far sailboat, reflection
c.line(88,64,98,64,'#87d7e2');c.line(91,66,96,66,'#59c3d5')
c.line(94,45,94,60,'#526d84')
c.poly([(92,46),(92,58),(82,58)],'#ffffff')
c.poly([(96,49),(102,58),(96,58)],'#dfedf1')
c.line(91,49,91,56,'#e6f4f6')
c.poly([(81,60),(103,60),(99,63),(86,63)],'#f4f5ec')
c.line(83,60,102,60,'#395d80')
# exactly two gulls, angled wings
c.path('M 48 22 L 51 21 L 55 24 L 58 21 L 61 21','#477c9e',fill=False)
c.path('M 73 12 L 76 12 L 79 14 L 82 11 L 85 11','#477c9e',fill=False)
# umbrella shadow on sand
c.ellipse(40,113,22,5,'#d6ad71')
c.ellipse(37,112,16,3,'#c69f6d')
# towel drop shadow and perspective shape
c.poly([(76,101),(94,98),(111,119),(89,124)],'#d2ac71')
c.poly([(75,98),(92,95),(108,116),(88,121)],'#fffbde')
# towel stripes interpolate
for pts in [[(77,101),(94,98),(96,101),(79,104)],[(81,106),(98,103),(100,106),(83,109)],[(85,112),(102,108),(104,111),(87,115)],[(88,117),(106,113),(108,116),(90,120)]]:
 c.poly(pts,'#2babc1')
c.line(75,98,92,95,'#fffdf0')
for x,y in [(88,121),(92,120),(96,119),(100,118),(104,117)]:c.line(x,y,x+1,y+2,'#fff4ce')
# umbrella pole, diagonal sunlit edge
c.line(33,70,38,111,'#977547')
c.line(34,70,39,110,'#f9edc5')
c.set(39,111,'#826941')
# umbrella silhouette and panels
c.poly([(8,73),(11,65),(17,58),(25,53),(33,51),(42,54),(50,61),(57,70),(59,76),(51,74),(43,77),(35,74),(26,77),(18,73)],'#b7454c')
# panels fan from crown
c.poly([(33,52),(25,55),(19,62),(15,71),(8,73),(12,64),(20,57)],'#f46a61')
c.poly([(33,52),(25,56),(20,64),(18,73),(26,76),(27,63)],'#fff5df')
c.poly([(33,52),(29,61),(27,69),(26,76),(35,73),(37,62)],'#ef5455')
c.poly([(33,52),(39,58),(43,66),(43,76),(35,73),(35,62)],'#fffae8')
c.poly([(33,52),(43,56),(50,63),(51,73),(43,76),(43,66),(39,58)],'#e94d53')
c.poly([(33,52),(43,55),(51,62),(58,73),(59,76),(51,73),(49,64),(42,57)],'#fff0d7')
# scalloped hanging edge
for x,y,w,col in [(8,73,9,'#d74a50'),(18,74,8,'#e7d7c5'),(26,76,9,'#c93947'),(35,74,8,'#eadfcb'),(43,76,8,'#c63946'),(51,74,8,'#e4d2c0')]:
 c.rect(x,y,w,2,col)
c.line(32,51,34,51,'#fff1cd');c.set(33,50,'#be5c4b')
# little flip-flops to the right of towel
for x,y in [(113,103),(120,100)]:
 c.ellipse(x,y+3,3,6,'#d1a66b')
 c.ellipse(x,y+2,2,5,'#285e78')
 c.rect(x-2,y,4,6,'#287e96')
 c.line(x-1,y-1,x,y+2,'#ff8b64')
 c.line(x+1,y-1,x,y+2,'#ffc382')
 c.set(x,y+3,'#ef855e')
# small shell on foreground
c.poly([(60,116),(62,113),(65,112),(68,115),(68,117),(63,118)],'#e8ac7c')
c.line(62,114,64,117,'#fff2ce');c.line(65,113,65,116,'#fff4d9');c.line(67,115,66,117,'#fff4d9')
assert result.stats()['colors_used'] <= 86, result.stats()
view(result)
finish(result)
