result = new_canvas(64,64,background='#201b25',name='tavern')
c=result
ink='#181720'; wood='#66402f'; light='#ad7140'; gold='#efbc65'
# plaster wall and timber frame
c.rect(3,5,58,37,'#403039')
c.rect(7,8,49,28,'#513a38')
c.rect(0,3,64,4,'#2a2026'); c.line(0,3,63,3,'#80513a')
for x in [3,31,58]:
 c.rect(x,6,3,33,'#2b2329'); c.line(x,7,x,36,'#704733')
c.rect(0,37,64,27,'#34272b')
# floor boards perspective
for y in [42,48,55,63]:
 c.line(0,y,63,y,ink); c.line(0,y+1,63,y+1,'#51372e') if y<63 else None
for x in [-30,-8,16,39,63,86]:
 c.line(32+(x-32)//3,38,x,63,'#231e25')
for x,y,w in [(4,51,6),(27,59,8),(47,51,9),(9,60,5),(36,45,7),(53,59,6)]: c.line(x,y,x+w,y,'#684431')
# bottle shelving cabinet
c.rect(17,10,37,23,ink); c.rect(19,12,33,19,'#30272c')
for y in [20,30]:
 c.rect(17,y,37,3,'#34232a'); c.line(18,y,53,y,'#b07746'); c.line(19,y+1,52,y+1,'#6d4532')
c.line(18,11,53,11,'#865537')
def bottle(x,y,col,h=6):
 c.rect(x+1,y,2,2,ink); c.rect(x,y+2,4,h-2,ink)
 c.rect(x+1,y+1,1,h-2,col); c.rect(x+1,y+3,2,h-3,col)
 c.set(x+1,y,'#b28755'); c.set(x+1,y+2,'#9ba978'); c.rect(x+1,y+h-3,2,1,'#c9b383')
for x,y,col,h in [(20,13,'#4d806c',7),(26,14,'#a16045',6),(32,12,'#65845f',8),(39,14,'#466b67',6),(46,13,'#a77a45',7),(21,24,'#aa7744',6),(28,23,'#52765e',7),(43,23,'#738c67',7),(48,24,'#95604e',6)]: bottle(x,y,col,h)
# small stacked mugs
for x in [35,38]:
 c.rect(x,26,3,4,'#b4a084'); c.line(x,26,x+2,26,'#eed8a4'); c.set(x+2,29,'#746556')
# left small window
c.rect(7,13,8,16,ink); c.rect(8,14,6,13,'#34434e'); c.rect(9,15,4,5,'#435767')
c.line(11,14,11,27,'#211e27'); c.line(8,21,13,21,'#211e27'); c.rect(6,28,10,2,'#8c5b3c')
# smoke in shadow behind counter
c.path('M 7 36 Q 3 32 9 30 Q 13 28 10 24 M 55 32 Q 60 27 55 24 Q 52 21 56 19','#74605a',fill=False)
c.path('M 14 32 Q 18 28 14 26','#65504d',fill=False)
# hanging lamps, stepped glow halos
for x,y in [(12,10),(43,8)]:
 c.ellipse(x,y+5,8,6,'#6c4838'); c.ellipse(x,y+5,6,5,'#97643e'); c.ellipse(x,y+5,4,4,'#bc8b4b')
 c.line(x,0,x,y,ink); c.set(x+1,4,'#926044')
 c.poly([(x-3,y),(x+3,y),(x+5,y+5),(x-5,y+5)],ink)
 c.poly([(x-2,y+1),(x+2,y+1),(x+3,y+4),(x-3,y+4)],'#d59743')
 c.rect(x-3,y+5,7,2,'#ffe4a0'); c.rect(x-2,y+7,5,1,'#d89645'); c.set(x,y+5,'#fff4c5')
# counter silhouette and front
c.rect(9,36,47,13,ink); c.rect(11,39,43,9,wood)
for x in [12,26,40]:
 c.rect(x,40,12,7,'#39282a'); c.rect(x+1,41,10,5,'#875234'); c.line(x+2,41,x+9,41,'#aa6d3e'); c.line(x+2,45,x+8,45,'#613a2d')
c.rect(10,47,45,2,'#2a2024'); c.line(12,47,53,47,'#a06b3e')
c.rect(8,34,49,5,ink); c.rect(9,34,47,3,'#a66b3f'); c.line(10,34,55,34,'#d89c56'); c.line(9,37,55,37,'#5c372b')
c.line(18,35,31,35,'#bd8046'); c.line(40,36,49,36,'#805032')
# barware on top
bottle(29,28,'#58836a',6)
for x,y in [(19,30),(38,30)]:
 c.rect(x,y,4,4,ink); c.rect(x+1,y+1,2,2,'#c48b4b'); c.line(x,y,x+3,y,'#f3deb0'); c.line(x+3,y+1,x+4,y+1,'#b6b6a0'); c.set(x+4,y+2,'#b6b6a0')
c.ellipse(48,33,4,1,'#d6b78a'); c.line(46,32,49,32,'#eee0ae')
# foreground barrel
c.ellipse(6,54,6,3,ink)
c.rect(1,43,11,11,ink); c.ellipse(6,48,6,8,ink)
c.ellipse(6,48,5,7,'#805031')
for x in [3,6,9]: c.line(x,44,x,53,'#422d28'); c.line(x+1,45,x+1,53,'#ac7241')
for y in [44,51]:
 c.rect(1,y,11,2,'#3b3b39'); c.line(2,y,10,y,'#828075'); c.set(3,y+1,'#b2a287'); c.set(9,y+1,'#b2a287')
c.ellipse(6,41,5,2,ink); c.ellipse(6,41,4,1,'#b47d49'); c.line(4,41,8,41,'#734b32')
# stools
for x,y in [(20,48),(36,50),(51,49)]:
 c.ellipse(x,y+10,6,2,'#241e25')
 for dx in [-3,3]:
  c.line(x+dx,y+2,x+dx*2//1,y+10,ink)
  c.line(x+dx,y+3,x+dx+(-1 if dx<0 else 1),y+9,'#9c6840')
 c.line(x-4,y+7,x+4,y+7,'#533a2e'); c.line(x-3,y+6,x+3,y+6,'#ba8350')
 c.ellipse(x,y+1,6,3,ink); c.ellipse(x,y,5,2,'#935735'); c.line(x-3,y-1,x+3,y-1,'#d39854'); c.line(x-3,y+2,x+3,y+2,'#57342b')
# ceiling corner shadows and bracket
c.rect(0,0,64,2,'#17171f'); c.line(0,7,3,10,'#17171f'); c.line(61,7,63,9,'#17171f')
view(c)
finish(result)
