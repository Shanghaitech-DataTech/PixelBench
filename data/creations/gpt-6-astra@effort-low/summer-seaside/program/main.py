import random
random.seed(23)
c=new_canvas(128,128,'#71cffa',name='summer_seaside')
# clear sky bands
c.rect(0,24,128,20,'#86dafa');c.rect(0,39,128,15,'#a1e5fa')
# sunshine
c.circle(105,16,11,'#ffe69a');c.circle(105,16,8,'#fff2af');c.circle(103,14,5,'#fff8ce')
# soft stepped cloud banks
def cloud(x,y):
 c.rect(x,y+5,30,5,'#d6eff9');c.rect(x+3,y+2,23,7,'#f5fcff');c.rect(x+8,y-1,11,9,'#f5fcff');c.rect(x+11,y-3,6,7,'#f5fcff');c.rect(x-3,y+6,36,2,'#f5fcff')
cloud(14,17);cloud(65,29)
# sea bands
c.rect(0,51,128,10,'#246cb7');c.rect(0,61,128,10,'#218bc6');c.rect(0,71,128,13,'#22a9cd');c.rect(0,84,128,15,'#38c6ce')
c.line(0,51,127,51,'#3886c4')
# beach sweeping diagonal
c.poly([(0,92),(19,95),(39,94),(60,90),(81,86),(104,82),(127,80),(127,128),(0,128)],'#efd08a')
c.poly([(0,97),(21,100),(42,99),(64,95),(86,90),(108,87),(127,86),(127,128),(0,128)],'#f9df9b')
# shallow water and broken white lace surf
c.path('M0 87 Q20 94 39 90 Q72 80 95 79 Q113 75 127 76 L127 81 Q103 81 82 87 Q58 89 40 95 Q17 98 0 92 Z','#89e2da')
c.path('M0 90 Q20 97 40 92 Q61 87 82 84 Q105 77 127 78 L127 81 Q104 81 82 87 Q60 90 40 95 Q18 99 0 93 Z','#f2ffed')
for x,y,w in [(2,88,8),(17,92,7),(33,90,6),(48,88,7),(69,83,8),(90,80,5),(112,76,9)]:c.line(x,y,x+w,y,'#d8fff2')
# horizontal wavelets
for i in range(67):
 x=random.randrange(128); y=random.randrange(55,88)
 # keep sparkles in water
 if y < 85-(x/128)*8:
  col=random.choice(['#74dce4','#51c5dd','#b4f1ee'] if y>70 else ['#419bd0','#64b6dc'])
  c.line(x,y,min(127,x+random.randrange(2,8)),y,col)
c.path('M4 78 Q14 75 25 78 M53 70 Q64 68 75 70 M90 63 L105 63', '#d7f8ef',fill=False)
# distant sailboat
c.line(91,47,91,64,'#f5e8c7')
c.poly([(89,48),(89,61),(78,61)],'#fffdf0')
c.poly([(93,51),(100,61),(93,61)],'#d6edf0')
c.poly([(78,64),(100,64),(96,67),(82,67)],'#fff8df');c.line(83,67,96,67,'#205d9c')
# two flying gulls
for x,y in [(56,17),(74,11)]:
 c.line(x-5,y,x-3,y-1,'#32749c');c.line(x-3,y-1,x,y+2,'#32749c');c.line(x,y+2,x+3,y-1,'#32749c');c.line(x+3,y-1,x+5,y-1,'#32749c')
# sand grain clusters
for i in range(86):
 x=random.randrange(128);y=random.randrange(94,128)
 if y>102-x*.09:
  c.line(x,y,min(x+random.choice([0,1,2]),127),y,random.choice(['#e9c47d','#f3d18b','#ffedb5']))
# towel angled on the sand
c.poly([(69,103),(91,98),(107,118),(83,124)],'#dfbd7a')
c.poly([(68,101),(90,96),(105,116),(82,122)],'#fff4d8')
for pts in [[(70,103),(92,99),(94,102),(72,107)],[(75,110),(97,105),(99,108),(77,113)],[(80,117),(102,112),(104,115),(82,120)]]:c.poly(pts,'#ef7363')
for x,y in [(83,122),(88,121),(93,119),(98,118),(103,117)]: c.line(x,y,x+1,y+2,'#fff4d8')
# flip flops
for x,y in [(110,104),(117,101)]:
 c.ellipse(x,y,3,6,'#cba967');c.ellipse(x,y-1,2,5,'#258e9d');c.line(x-1,y-3,x,y,'#a9eee0');c.line(x+1,y-3,x,y,'#a9eee0');c.line(x,y,x,y+2,'#135a79')
# umbrella shadow, pole
c.ellipse(35,112,23,5,'#daba79');c.ellipse(34,111,17,3,'#c9ad70')
c.line(33,73,33,109,'#9e7756');c.line(34,73,34,110,'#fff0c3');c.line(32,110,35,110,'#9e7756')
# umbrella scalloped canopy, alternating radial panels
c.poly([(9,80),(12,72),(19,65),(30,61),(36,61),(47,65),(55,72),(59,80),(51,78),(43,81),(34,79),(25,82),(17,79)],'#c74749')
c.poly([(10,78),(14,71),(21,65),(32,62),(25,69),(21,78),(17,77)],'#ff655b')
c.poly([(17,77),(21,68),(32,62),(29,70),(26,80)],'#fff8de')
c.poly([(26,80),(29,69),(33,62),(37,70),(42,79),(34,77)],'#f15853')
c.poly([(34,62),(43,66),(48,72),(51,77),(43,79),(39,69)],'#fff8de')
c.poly([(35,62),(47,66),(54,73),(58,78),(51,76),(47,69)],'#f16659')
c.line(13,71,21,65,'#ff9280');c.line(22,65,30,62,'#fffdf0');c.line(33,59,33,62,'#a86c4b')
view(c)
finish(c)
