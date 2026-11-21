import math
result = new_canvas(64,64,background='#101720',name='open-pocket-watch')
c=result
# restrained dark backdrop
c.ellipse(32,53,28,7,'#0b1018')
c.ellipse(32,54,22,4,'#080d13')
# chain rising behind the watch
for x,y in [(48,28),(53,26),(57,23),(59,19),(58,15),(54,13),(50,14),(48,17),(49,20)]:
 c.ellipse(x,y,3,2,'#201711')
 c.ellipse(x,y,2,1,'#c18b3c',False)
 c.set(x-1,y-1,'#ffe7a1')
# open lid, tilted above left of body
c.ellipse(23,17,19,14,'#070d13')
c.ellipse(22,16,18,14,'#724523')
c.ellipse(22,15,18,13,'#d39b45')
c.ellipse(22,14,17,12,'#ffe1a0')
c.ellipse(22,15,15,10,'#805127')
c.ellipse(22,15,14,9,'#bc8137')
c.ellipse(22,14,13,8,'#e1b55e')
c.ellipse(22,14,11,6,'#c18d40')
# curved metal gleams
c.path('M 7 12 Q 13 2 27 4', '#fff0bb',False)
c.path('M 9 17 Q 17 25 31 20','#f3d282',False)
c.path('M 12 10 Q 21 4 31 10','#ebc473',False)
c.path('M 15 17 Q 23 21 30 16','#a36a2e',False)
c.line(12,11,18,8,'#f8db91')
c.line(24,19,31,16,'#deb15a')
# hinge
c.rect(19,26,13,5,'#36271c')
c.rect(20,26,11,3,'#d2a34f')
for x in [21,24,28,30]: c.line(x,26,x,29,'#ffde88')
# crown and bow to upper right
c.ellipse(44,26,5,5,'#b37b32',False)
c.ellipse(44,26,4,4,'#ffe0a0',False)
c.rect(41,28,6,6,'#6e4526')
for x in [41,43,45]:c.line(x,28,x,32,'#efbc60')
# main case
c.ellipse(32,43,23,19,'#080c12')
c.ellipse(32,42,23,19,'#754723')
c.ellipse(32,41,23,18,'#b07731')
c.ellipse(32,40,23,18,'#ecc474')
c.ellipse(32,40,22,17,'#ffe5a0')
c.ellipse(32,41,21,16,'#97622f')
c.ellipse(32,40,20,15,'#c6964b')
c.ellipse(32,40,19,14,'#2c2520')
c.ellipse(32,40,18,13,'#57422a')
# deep recesses and movement plate
c.poly([(17,34),(26,28),(37,28),(47,34),(49,44),(40,52),(26,52),(17,46)],'#9b7336')
c.ellipse(23,41,9,8,'#292823')
c.ellipse(38,44,11,8,'#29231d')
c.ellipse(34,32,7,5,'#342b22')
# gears with individual teeth, ring and spokes
def gear(x,y,r,phase=0):
 for i in range(12):
  a=phase+i*math.pi/6
  xx=round(x+math.cos(a)*r); yy=round(y+math.sin(a)*r)
  c.rect(xx-1,yy-1,3,3,'#dfb45a')
 c.circle(x,y,r-1,'#e4b65f')
 c.circle(x,y,r-2,'#705028')
 if r>4:c.circle(x,y,r-3,'#252522')
 for i in range(5):
  a=phase+i*math.tau/5
  c.line(x,y,round(x+math.cos(a)*(r-2)),round(y+math.sin(a)*(r-2)),'#c7923d')
 c.circle(x,y,2,'#eccb79')
 c.set(x,y,'#4c3224');c.set(x-1,y-1,'#fff1ba')
 for i in range(5):
  a=math.pi+i*math.pi/6
  c.set(round(x+math.cos(a)*(r-1)),round(y+math.sin(a)*(r-1)),'#ffdf88')
gear(22,41,6,0.2)
gear(34,45,5,0.1)
gear(42,38,5,0.3)
gear(43,48,3)
# balance wheel lower left
c.circle(24,49,4,'#38291e')
c.circle(24,49,3,'#dfac55',False)
c.line(22,47,26,51,'#f6d186')
c.line(22,51,26,47,'#a97a37')
c.set(24,49,'#fff0b4')
# small ivory dial inset upper left
c.ellipse(29,33,8,7,'#4b321f')
c.ellipse(29,32,8,7,'#d7b76d')
c.ellipse(29,32,7,6,'#f0ddb0')
for i in range(12):
 a=i*math.tau/12
 x=round(29+6*math.sin(a));y=round(32-5*math.cos(a))
 c.set(x,y,'#584735')
c.line(29,32,26,29,'#202b32')
c.line(29,32,33,30,'#202b32')
c.set(29,32,'#a86b2c')
# bridge holding exposed wheel train
c.poly([(29,38),(31,38),(37,48),(36,50),(33,48)],'#5c3d22')
c.line(30,39,36,48,'#e4bf70')
c.line(31,39,37,48,'#b8883f')
# jewel bearings / polished screwheads
for x,y in [(17,35),(38,30),(47,43),(32,51)]:
 c.circle(x,y,1,'#e5c57b');c.line(x-1,y,x+1,y,'#433d32');c.set(x,y-1,'#fff0c2')
c.set(36,47,'#69283a');c.set(36,46,'#e89a7d')
# fine machining marks and cool reflected metal
c.line(15,12,20,9,'#edc77b')
c.line(16,13,21,10,'#d9ac58')
c.line(26,16,30,13,'#edc77b')
c.set(13,16,'#e6bb6b')
c.set(32,12,'#b17b32')
# visible wheel rims and dark cutouts between spokes
c.set(33,42,'#292823');c.set(36,44,'#292823')
c.set(33,47,'#292823');c.set(31,45,'#ffe1a0')
c.set(41,36,'#292823');c.set(44,38,'#292823')
c.set(41,40,'#292823')
c.set(20,39,'#292823');c.set(24,42,'#292823')
c.line(19,39,20,38,'#fff1b0')
c.set(42,35,'#fff1b0')
c.set(43,48,'#3d3330')
c.set(43,47,'#fff1b0')
# case specular arcs
c.path('M 10 37 Q 13 27 21 25','#fff2c3',False)
c.path('M 12 46 Q 18 56 32 57','#ffe09a',False)
c.path('M 33 58 Q 47 57 53 46','#d29c4c',False)
c.path('M 51 34 Q 55 40 52 45','#fff2bd',False)
c.line(17,53,22,55,'#fff4ca')
c.line(24,59,32,60,'#bd8740')
c.set(10,38,'#ffffff');c.set(51,33,'#fff4d1')
view(c)
finish(result)
