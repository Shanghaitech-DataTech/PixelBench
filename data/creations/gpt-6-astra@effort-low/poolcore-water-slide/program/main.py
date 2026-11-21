import random
random.seed(12)
c=new_canvas(128,128,'#d2e6e8',name='poolcore')
# ceiling perspective
c.poly([(0,0),(127,0),(110,29),(28,29),(0,17)],'#bccfd5')
for x in [-60,-10,40,90,140,190]:
 c.line(65,30,x,0,'#9fbac4')
for y in [8,18,25]: c.line(0,y,127,y,'#aec5cd')
# luminous fixtures
for p in [[(12,3),(21,3),(44,23),(40,23)],[(58,3),(65,3),(69,23),(65,23)],[(105,3),(115,3),(94,23),(89,23)]]:
 c.poly(p,'#e6f7f3')
# rear wall
c.rect(0,29,128,36,'#d3e7e8')
for y in range(30,66,5): c.line(0,y,127,y,'#aecdd4')
for x in range(0,128,5): c.line(x,29,x,65,'#aecdd4')
for x,y in [(7,36),(22,46),(57,31),(82,51),(117,41),(42,56)]:c.rect(x,y,3,4,'#c0dbe1')
# dark empty openings
c.rect(32,36,18,25,'#86aebc');c.rect(35,38,13,23,'#527f91')
c.rect(36,40,11,21,'#648e9f');c.line(36,40,36,60,'#476e83')
c.rect(91,35,21,26,'#a0c3cd');c.rect(94,37,16,24,'#769fae')
for y in range(41,61,5):c.line(94,y,109,y,'#6c96a6')
for x in range(95,111,5):c.line(x,38,x,60,'#6c96a6')
# floor and perspective grid
c.poly([(0,60),(128,60),(128,128),(0,128)],'#e0ece8')
for x in range(-160,300,15):c.line(round(66+(x-66)*12/79),60,x,127,'#a5c7ce')
for y in [63,67,72,79,89,103,121]:c.line(0,y,127,y,'#b3d0d5')
# pool coping and water
c.poly([(24,68),(105,68),(128,88),(128,128),(0,128),(0,90)],'#90b6c1')
c.poly([(26,71),(103,71),(127,93),(127,127),(0,127),(0,95)],'#f2f5e9')
c.poly([(28,75),(101,75),(127,98),(127,127),(0,127),(0,100)],'#83c4d6')
# submerged tiles warped perspective
for y in [78,83,90,99,111,125]: c.line(max(0,28-(y-75)),y,min(127,101+(y-75)),y,'#76b8cd')
for x in range(-80,210,13):c.line(65,75,x,127,'#78bfd1')
# broad pale reflections
c.poly([(33,77),(39,77),(26,94),(29,95),(13,122),(4,125),(19,97)],'#a4dbe3')
c.poly([(70,77),(74,77),(77,90),(75,92),(82,123),(76,126),(72,103),(74,101)],'#a7dee5')
c.poly([(100,80),(104,84),(115,104),(111,105),(121,125),(112,123),(102,101),(106,99)],'#98d4df')
# water glints, horizontal clustered ripples
for i in range(160):
 y=random.randrange(78,128);x=random.randrange(128)
 if x>28-(y-75) and x<101+(y-75):
  col=random.choice(['#b4e6e9','#9dd7e1','#c5ebeb','#6bb3ca'])
  c.line(x,y,min(127,x+random.randrange(1,6)),y,col)
# large tiled structural pillars
def pillar(x,top,bottom,w):
 c.rect(x,top,w,bottom-top,'#e0efeb');c.rect(x+w-4,top,4,bottom-top,'#9ebfc9')
 for yy in range(top,bottom,5):c.line(x,yy,x+w-1,yy,'#b1ccd2')
 for xx in range(x+3,x+w-4,5):c.line(xx,top,xx,bottom-1,'#bfd7d9')
 c.line(x,top,x,bottom-1,'#f3f7eb')
 c.rect(x-1,bottom-2,w+2,3,'#b5d1d4')
pillar(12,21,73,12)
pillar(76,27,66,8)
pillar(119,13,87,14)
# slide ladder at back
c.line(110,37,116,67,'#7397a5');c.line(114,36,121,70,'#b0c8cc')
for y in range(43,67,5):
 x=110+(y-37)//5;c.line(x,y,x+5,y,'#f0f4eb')
# white slide sweeping from upper right to left then curving toward water
c.path('M 114 35 C 98 33 89 37 89 46 C 89 55 108 54 109 63 C 111 72 97 78 91 86 L 79 84 C 82 74 98 68 97 64 C 96 61 76 59 76 48 C 76 34 94 27 112 29 Z','#739ba9')
c.path('M 113 32 C 94 30 80 37 80 46 C 80 58 102 57 103 64 C 104 71 87 78 84 85 L 94 87 C 98 79 113 73 113 63 C 112 52 93 53 92 46 C 90 40 101 37 115 38 Z','#f4f6eb')
c.path('M 112 34 C 96 32 84 38 84 46 C 83 56 106 56 107 64 C 108 73 92 78 90 85','#c8dddd',fill=False)
c.path('M 113 36 C 99 34 87 39 87 46 C 86 55 108 54 110 63 C 112 73 95 80 93 85','#a9cbd2',fill=False)
c.line(84,85,93,87,'#ffffff')
# slide contact ripples
for x,y,w in [(82,89,15),(86,92,13),(79,91,4)]:c.line(x,y,x+w,y,'#d6f4ef')
# girl reflection
c.line(57,107,68,107,'#6bb2c5');c.line(58,109,66,109,'#75bacb')
c.line(61,112,69,112,'#a7d3ce')
# ring shadow
c.ellipse(61,103,11,4,'#5cabc1')
c.ellipse(61,101,11,5,'#ba932d')
c.ellipse(61,100,11,5,'#f3ca49')
c.ellipse(61,99,9,3,'#ffe781')
c.ellipse(61,99,5,2,'#83c4d6')
c.line(53,101,56,102,'#ffe88a');c.line(66,102,69,101,'#ffe88a')
# shoulders and back, viewed from behind
c.poly([(58,91),(64,91),(66,99),(56,99)],'#ce9b83')
c.rect(59,92,5,5,'#e9bea0')
c.line(57,94,53,98,'#efc4a2');c.line(65,94,69,98,'#efc4a2')
c.line(57,98,65,98,'#52768c')
c.rect(59,89,4,4,'#bd896f')
# dark hair silhouette
c.ellipse(61,87,4,5,'#394451')
c.rect(57,87,9,6,'#394451')
c.line(58,85,58,90,'#60616a');c.line(59,83,62,83,'#62616a')
c.line(64,87,64,92,'#293c4d')
c.set(56,99,'#ffe781');c.set(69,99,'#fff0a1')
view(c)
finish(c)
