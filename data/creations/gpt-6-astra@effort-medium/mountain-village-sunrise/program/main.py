import random
random.seed(8)
c=new_canvas(128,128,background='#efb181',name='mountain-village-sunrise')
# pastel sunrise bands
for y,col in [(0,'#827f9e'),(12,'#a58ba3'),(23,'#c99aa0'),(34,'#e8aa92'),(44,'#f5c28e'),(55,'#f8d69b')]:
 c.rect(0,y,128,16,col)
c.circle(65,39,13,'#ffe9ac')
c.rect(5,24,24,2,'#dba9ad');c.rect(11,22,15,2,'#dba9ad');c.rect(88,17,29,2,'#bca0b2')
# mountain ranges
c.poly([(0,55),(12,43),(23,48),(41,25),(56,42),(68,34),(85,53),(104,31),(127,52),(127,82),(0,82)],'#8c849d')
c.poly([(23,48),(41,25),(56,42),(46,38),(41,33),(36,42),(32,40)],'#e4c2be')
c.poly([(89,46),(104,31),(119,45),(108,40),(103,36),(100,42),(97,40)],'#e4c2be')
c.poly([(0,65),(19,48),(31,56),(49,43),(65,62),(81,46),(100,62),(117,47),(127,55),(127,88),(0,88)],'#666f86')
c.poly([(19,48),(31,56),(24,54),(20,52),(14,56)],'#b8a5ac')
c.poly([(0,72),(17,66),(31,71),(47,64),(70,73),(92,64),(112,69),(127,65),(127,95),(0,95)],'#677f80')
c.poly([(0,83),(28,77),(52,84),(80,76),(106,80),(127,76),(127,128),(0,128)],'#657b60')
c.poly([(0,99),(25,86),(48,92),(71,87),(100,96),(127,91),(127,128),(0,128)],'#849363')
# pines
def pine(x,y,h,dark,light):
 c.rect(x-1,y-h+5,2,h-3,'#635b52')
 for a in [0,5,10]:
  top=y-h+a; half=int(h*.24+a*.16)
  c.poly([(x,top),(x-half,top+int(h*.51)),(x+half,top+int(h*.51))],dark)
  c.poly([(x,top),(x-half,top+int(h*.51)),(x-1,top+int(h*.43))],light)
for x,y,h in [(4,81,22),(16,78,21),(27,80,19),(90,77,23),(100,78,29),(115,76,24),(124,81,28),(37,77,17)]:pine(x,y,h,'#395b5c','#57736b')
# path winding into foreground
c.poly([(61,83),(69,83),(68,96),(78,104),(88,114),(85,128),(51,128),(64,114),(63,106),(56,98)],'#b2a383')
c.poly([(61,84),(64,85),(60,97),(67,106),(68,114),(56,128),(51,128),(64,114),(63,106),(56,98)],'#526b53')
# tiny grasses
for i in range(210):
 x=random.randrange(128);y=random.randrange(85,128)
 if c.color_name(c.get(x,y)) in ['#849363','#657b60']:
  c.line(x,y,x+random.choice([0,1,2]),y-1,random.choice(['#a0a16a','#526f56','#748457']))
# stones fitted to path
for y,xs in [(91,[61,65]),(96,[60,64]),(101,[63,67]),(106,[67,72]),(111,[68,74,79]),(116,[65,72,80]),(122,[61,69,78]),(127,[56,65,75,82])]:
 for x in xs:
  w=random.choice([3,4,5])
  c.poly([(x,y-2),(x+w-1,y-3),(x+w,y),(x+1,y+1)],'#777c70')
  c.line(x,y-2,x+w-2,y-2,'#d1c4a0')
# wooden houses gable face

def house(x,y,w,h):
 # y roof peak
 e=y+int(w*.45);base=e+h
 c.rect(x+2,e,w-3,h,'#684b40')
 c.rect(x+3,e,w-8,h-1,'#b37c4e')
 c.rect(x+w-6,e,4,h,'#80543e')
 c.poly([(x+2,e),(x+w//2,y+2),(x+w-2,e)],'#b57d50')
 for yy in range(e+3,base,4):
  c.line(x+3,yy,x+w-7,yy,'#81563f');c.line(x+4,yy+1,x+w-8,yy+1,'#c38c57')
 # roof chimney behind roof
 c.rect(x+w-10,y-3,4,10,'#755d55');c.rect(x+w-11,y-4,6,2,'#bca087')
 c.poly([(x-3,e+2),(x+w//2,y-3),(x+w+3,e+1),(x+w,e+4),(x+w//2,y+2),(x,e+5)],'#3e4249')
 c.line(x-3,e+1,x+w//2,y-4,'#f0b978');c.line(x+w//2,y-4,x+w+3,e,'#c38b62')
 c.line(x-1,e,x+w//2,y-1,'#956c57')
 c.line(x+w//2+3,y+2,x+w,e+1,'#67606a')
 # foundation
 c.rect(x+1,base,w,3,'#565a53')
 for xx in range(x+2,x+w,5):c.rect(xx,base,3,1,'#a2a08b')
 # door centered
 dx=x+w//2-2
 c.rect(dx-1,base-11,7,11,'#543e36');c.rect(dx,base-10,4,10,'#76533c');c.line(dx,base-10,dx,base-2,'#ba8652');c.set(dx+3,base-5,'#f7cf85')
 # windows
 for wx in [x+5,x+w-10]:
  c.rect(wx-1,e+4,6,7,'#523e39');c.rect(wx,e+5,4,4,'#ffd890');c.line(wx+2,e+5,wx+2,e+8,'#ab784e');c.rect(wx-2,e+10,8,1,'#d9a775')
 c.rect(dx-2,base+3,9,2,'#b9aa8d')
 return x+w-8,y-5
# exactly three houses
chim=[]
chim.append(house(9,65,26,15))
chim.append(house(91,62,25,15))
chim.append(house(45,52,35,23))
# central attic window
c.rect(59,62,7,7,'#654938');c.rect(60,63,5,5,'#ffdc91');c.line(62,63,62,67,'#ac774c')
# chimney smoke, drift up and left
for x,y in chim:
 c.path(f'M {x} {y} C {x+4} {y-5} {x-5} {y-7} {x-4} {y-11} C {x-4} {y-15} {x+1} {y-15} {x-1} {y-19} L {x-4} {y-20} C {x-1} {y-15} {x-8} {y-13} {x-7} {y-9} C {x-6} {y-5} {x} {y-4} {x-2} {y} Z','#cfb8b0')
 c.set(x-3,y-21,'#dbc1b5')
# foreground framing
pine(6,119,38,'#284c48','#3d6655')
pine(119,122,42,'#294c48','#436957')
pine(127,114,29,'#294c48','#436957')
# shrubs and stones
for x,y in [(22,111),(31,119),(96,115),(46,109),(102,102),(40,100)]:
 c.rect(x-2,y,7,3,'#506a4f');c.rect(x,y-2,4,3,'#6e8355');c.set(x+1,y-2,'#b4ac70')
for x,y in [(39,120),(92,125),(25,103),(87,104)]:
 c.poly([(x,y),(x+2,y-3),(x+6,y-2),(x+7,y+1)],'#606e61');c.line(x+2,y-3,x+5,y-3,'#b2b194')
# a small split rail fence
for x,y in [(26,99),(35,102),(43,105)]:
 c.rect(x,y-6,2,8,'#69513c');c.set(x,y-6,'#d1a16b')
c.line(27,95,44,101,'#c49a65');c.line(27,98,44,104,'#8d6e46')
view(c)
save('mountain-village-sunrise',c)
finish(c)
