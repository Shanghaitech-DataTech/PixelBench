result = new_canvas(64,64,background='#201a24',name='tavern')
c=result
ink='#211720'; deep='#30202a'; wood='#684033'; mid='#875039'; light='#af7148'; gold='#dc9e55'; cream='#ffda83'
# shadowed plaster wall and timber frame
c.rect(2,2,60,38,'#443039')
c.rect(5,5,54,30,'#51373b')
c.rect(6,6,51,25,'#5c403f')
c.rect(0,0,64,4,ink); c.rect(1,4,4,38,deep); c.rect(2,4,1,35,wood)
c.rect(59,3,5,40,ink); c.rect(59,4,2,34,wood)
c.rect(4,8,56,3,deep); c.line(5,8,58,8,wood)
# floor boards recede into room
c.rect(0,40,64,24,'#47302c')
for y in [44,50,57,63]:
 c.line(0,y,63,y,ink); c.line(0,y+1 if y<63 else y,63,y+1 if y<63 else y,'#654030')
for x in [-20,0,20,40,60,80]:
 c.line(max(0,min(63,32+(x-32)//2)),41,max(0,min(63,x)),63,'#302229')
for x,y,w in [(3,48,6),(27,61,8),(43,54,9),(13,59,5),(53,47,6),(28,46,4)]: c.line(x,y,x+w,y,'#805039')
# back bar shelving
c.rect(15,12,35,21,ink); c.rect(17,13,31,18,'#32282b')
c.rect(18,14,29,7,'#3c2d2b'); c.rect(18,23,29,7,'#3d2d2c')
for x in [16,48]: c.rect(x,13,1,19,wood)
def bottle(x,y,col,hi):
 c.rect(x+1,y,2,2,ink); c.rect(x,y+2,4,6,ink)
 c.rect(x+1,y+1,1,2,hi); c.rect(x+1,y+3,2,4,col); c.set(x+1,y+3,hi)
 c.rect(x+1,y+5,2,1,'#c3a16a')
for x,y,col,hi in [(19,13,'#47766a','#86a17a'),(25,13,'#945136','#cd8a4a'),(32,13,'#4c6b57','#a1aa6e'),(41,13,'#627b78','#a0b49b'),(19,22,'#7e473b','#b87c53'),(26,22,'#587e65','#9dab75'),(38,22,'#426e64','#83a484'),(43,22,'#8a5741','#c99156')]: bottle(x,y,col,hi)
for y in [21,30]:
 c.rect(15,y,35,3,ink); c.rect(16,y,33,1,light); c.rect(16,y+1,33,1,wood)
# stacked cups on shelf
c.rect(33,26,3,4,'#d4b784'); c.set(33,26,'#fff0b3'); c.line(33,28,35,28,'#866b53')
# wall plaque on left
c.rect(6,17,7,11,ink); c.rect(7,18,5,9,'#946443'); c.rect(8,19,3,7,'#43312d'); c.set(9,20,gold); c.line(8,23,10,23,'#d2a775')
# warm pools around pendant lamps
for x,y in [(10,11),(53,14)]:
 c.ellipse(x,y+3,6,7,'#68473f'); c.ellipse(x,y+3,4,5,'#825941')
 c.line(x,3,x,y-3,ink); c.set(x+1,5,'#8f6746')
 c.rect(x-2,y-3,5,2,ink); c.poly([(x-2,y-2),(x+2,y-2),(x+4,y+2),(x-4,y+2)],ink)
 c.rect(x-2,y-1,5,3,'#e6a951'); c.rect(x-1,y-1,2,3,'#ffe9a0')
 c.line(x-3,y+2,x+3,y+2,'#a8673c'); c.line(x-2,y+3,x+2,y+3,cream); c.set(x,y+4,'#c58b4b')
# bar counter silhouette, raised polished top
c.poly([(7,32),(55,32),(59,36),(59,41),(7,41),(4,37)],ink)
c.poly([(8,33),(54,33),(57,36),(6,36)],'#bb804d')
c.line(9,33,54,33,'#e4ac65'); c.line(7,36,57,36,'#e6ad67')
c.rect(7,37,51,3,wood); c.line(7,37,57,37,'#9c623c'); c.line(8,39,58,39,ink)
# panelled bar front
c.rect(9,40,48,10,'#61362e'); c.rect(10,40,46,1,'#9e603e')
for x in [11,25,40]:
 c.rect(x,42,13,7,ink); c.rect(x+1,42,11,6,'#895036'); c.rect(x+2,43,9,4,'#75432f'); c.line(x+2,43,x+10,43,'#a2633d')
 c.set(x+4,46,'#91553a')
c.rect(8,49,50,3,ink); c.line(9,49,56,49,'#8d5738')
# drinks on counter, glass handles
for x,y in [(16,29),(36,30)]:
 c.rect(x+3,y+1,3,4,ink); c.rect(x+3,y+2,2,2,'#cfab71')
 c.rect(x,y,4,6,ink); c.rect(x+1,y+1,2,4,'#dda052'); c.line(x+1,y+1,x+2,y+1,'#fff0b2'); c.set(x+1,y+2,'#ffe4a0')
bottle(46,26,'#3f7467','#a4b37b')
c.line(25,35,29,35,'#714934'); c.rect(26,31,3,3,'#e9d0a0'); c.set(27,31,'#fff0b2'); c.line(27,34,27,35,'#dcb984')
# foreground barrel left
def barrel(x,y):
 c.ellipse(x+5,y+7,6,9,ink)
 c.rect(x,y+1,11,13,wood); c.ellipse(x+5,y+7,5,8,'#995e3b')
 c.rect(x+2,y+2,2,12,'#b57a46'); c.rect(x+8,y+2,2,12,'#704332')
 for xx in [x+1,x+4,x+7,x+10]: c.line(xx,y+2,xx,y+13,'#69412f')
 c.ellipse(x+5,y+1,5,2,ink); c.ellipse(x+5,y,4,1,'#b78350'); c.line(x+2,y,x+7,y,'#805037')
 for yy in [y+4,y+11]:
  c.rect(x,yy,11,2,'#38373a'); c.line(x+1,yy,x+9,yy,'#8c8270'); c.set(x+2,yy,'#c3b38a')
barrel(1,42)
barrel(52,43)
# stools with splayed legs and rounded leather seats
for x,y in [(23,49),(44,50)]:
 c.ellipse(x,y+10,7,2,'#302128')
 c.line(x-3,y+2,x-5,y+11,ink); c.line(x-2,y+2,x-4,y+10,'#a36b40')
 c.line(x+3,y+2,x+5,y+11,ink); c.line(x+2,y+2,x+4,y+10,'#835135')
 c.line(x-3,y+7,x+3,y+7,ink); c.line(x-3,y+6,x+3,y+6,'#b17746')
 c.ellipse(x,y+1,6,3,ink); c.ellipse(x,y,5,2,'#a35437'); c.line(x-3,y-1,x+3,y-1,'#d5884b'); c.line(x-3,y+2,x+3,y+2,'#65332d')
# wisps in the lamplight; restrained stepped smoke
c.path('M 29 30 Q 24 27 29 25 Q 33 23 30 21', '#938077',fill=False)
c.path('M 30 29 Q 28 27 31 26', '#b3a08a',fill=False)
c.path('M 7 30 Q 4 27 8 24 Q 12 22 9 20', '#887064',fill=False)
c.path('M 49 8 Q 44 6 39 8 Q 35 10 30 8 Q 27 7 25 8', '#77615d',fill=False)
view(result)
finish(result)
