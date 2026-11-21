# Cozy tavern, 64 x 64
result = new_canvas(64,64,background='#211a22',name='tavern')
c=result
ink='#17151d'; deep='#2c2026'; wooddark='#482b2c'; wood='#704333'; mid='#955b39'; gold='#c18a4b'; light='#ecc779'; cream='#ffdfa0'
# rear wall, wood panelling and pools of lamplight
c.rect(2,3,60,39,'#3c2c2c')
c.rect(5,9,53,29,'#50352c')
c.ellipse(19,22,16,16,'#60402e')
c.ellipse(46,22,12,15,'#67452f')
for x in [6,16,27,38,49,59]:
 c.line(x,9,x,38,'#452e2a')
 c.line(x+1,11,x+1,34,'#775037')
# heavy structural timbers
c.rect(0,0,64,5,ink); c.rect(2,1,60,2,wood)
c.rect(0,5,4,41,ink);c.rect(1,5,2,39,wooddark)
c.rect(59,4,5,43,ink);c.rect(60,4,2,41,wood)
c.line(61,7,61,39,mid)
c.poly([(4,5),(16,5),(4,17)],wooddark)
c.line(5,13,12,6,mid)
c.poly([(48,5),(59,5),(59,16)],wooddark)
c.line(51,6,58,13,mid)
# floor
c.rect(0,42,64,22,'#50332f')
for y in [46,52,59]:
 c.line(0,y,63,y,deep); c.line(1,y+1,62,y+1,'#77503a')
for x,y in [(7,43),(29,43),(49,43),(19,47),(44,47),(8,53),(34,53),(57,53),(22,60),(48,60)]: c.line(x,y,x,min(63,y+4),deep)
for x,y,w in [(2,50,7),(26,49,9),(47,57,8),(11,57,9),(28,62,12),(52,44,6)]: c.line(x,y,x+w,y,'#895a3c')
# framed shelves
c.rect(9,12,45,19,ink)
c.rect(11,13,41,16,'#32282a')
c.rect(12,14,39,1,wood)
c.rect(10,21,43,3,ink); c.rect(10,21,43,1,gold); c.rect(11,22,41,1,wood)
c.rect(10,29,43,3,ink);c.rect(10,29,43,1,gold);c.rect(11,30,41,1,wood)
# tiny glass bottles, with necks, shoulders, glints, labels
def bottle(x,y,h,col,hi,label=False):
 c.rect(x+1,y,2,2,ink);c.set(x+1,y, gold)
 c.rect(x,y+2,4,h-2,ink);c.rect(x+1,y+2,2,h-3,col)
 c.line(x+1,y+2,x+1,y+3,hi)
 if label: c.rect(x+1,y+h-3,2,1,'#dbbc7a')
for args in [(13,15,6,'#416354','#83aa79',True),(19,14,7,'#96713e','#ddad61',False),(25,16,5,'#8a4740','#ce8170',False),(33,14,7,'#436b5f','#99b78b',True),(39,15,6,'#516e66','#99b78b',False),(46,14,7,'#ad783b','#edc773',True),(14,24,5,'#ac793e','#ebbb63',False),(23,23,6,'#517568','#a2bc8a',True),(29,24,5,'#7f4840','#cd8170',False),(36,23,6,'#4e6d58','#9ab179',True),(46,24,5,'#a47743','#f1c879',False)]: bottle(*args)
# overhead hazy smoke in restrained stepped bands
c.path('M 7 11 Q 16 6 28 10 Q 35 12 40 9 L 43 9 Q 36 15 26 12 Q 14 8 7 13 Z','#75614a')
c.path('M 29 6 Q 36 7 42 6 Q 50 5 54 9 L 54 11 Q 47 7 42 8 Q 34 10 29 7 Z','#54463e')
# pendant lamps, dark chains and bright glass
for x,y in [(8,17),(44,12)]:
 c.line(x,4,x,y-4,ink); c.set(x,6,mid)
 c.rect(x-2,y-4,5,2,ink)
 c.poly([(x-3,y-2),(x+3,y-2),(x+5,y+2),(x-5,y+2)],ink)
 c.poly([(x-2,y-2),(x+2,y-2),(x+3,y+1),(x-3,y+1)],gold)
 c.rect(x-2,y,5,3,'#f7be5c');c.rect(x-1,y,3,3,cream)
 c.line(x-4,y+3,x+4,y+3,ink);c.line(x-2,y+4,x+2,y+4,'#bc813d')
# counter shadow and body
c.rect(5,37,50,12,ink)
c.rect(7,39,46,8,wooddark)
for x in [8,23,38]:
 c.rect(x,39,13,7,wood);c.rect(x+1,40,11,1,mid)
 c.line(x+1,40,x+1,45,gold); c.line(x+2,45,x+11,45,'#4b2c29')
 c.line(x+5,42,x+9,42,mid)
c.rect(6,47,47,2,ink);c.rect(7,47,45,1,mid)
# thick polished bar top
c.poly([(7,32),(52,32),(57,36),(54,39),(4,39),(4,36)],ink)
c.poly([(8,33),(51,33),(54,35),(53,36),(6,36)],mid)
c.line(8,33,50,33,gold);c.line(6,37,54,37,gold);c.line(7,38,53,38,wooddark)
c.line(17,35,29,35,'#d49b56');c.line(38,35,46,35,wood)
# mugs and bottle on bar
bottle(32,27,7,'#416354','#a1b584',True)
def mug(x,y):
 c.rect(x,y,5,6,ink);c.rect(x+4,y+1,3,4,ink);c.rect(x+5,y+2,1,2,gold)
 c.rect(x+1,y+1,3,4,'#b9813e');c.line(x+1,y+1,x+1,y+4,cream)
 c.rect(x,y,5,2,'#ead6a0');c.set(x+3,y,'#fff0bd')
mug(16,29);mug(42,29)
c.rect(24,32,5,1,'#d7ac69');c.rect(25,31,3,1,'#f4d99a')
# foreground barrel on right
c.ellipse(56,59,7,3,deep)
c.poly([(51,43),(59,42),(62,47),(62,57),(59,61),(51,60),(48,55),(48,48)],ink)
c.poly([(51,44),(58,44),(60,48),(60,56),(58,59),(52,58),(50,54),(50,48)],wood)
c.poly([(52,45),(55,44),(55,58),(52,57),(51,53)],mid)
c.line(55,46,55,58,wooddark);c.line(58,46,59,56,wooddark)
c.ellipse(55,44,5,2,ink);c.ellipse(55,44,4,1,gold);c.line(52,44,58,44,mid)
for y in [48,55]:
 c.line(49,y,60,y,ink);c.line(50,y+1,60,y+1,'#7c7964');c.set(51,y+1,'#b0a786');c.set(59,y+1,'#444842')
# two foreground stools, chunky seats and splayed legs
for x,y in [(14,49),(36,51)]:
 c.ellipse(x,y+10,7,2,deep)
 for dx in [-4,3]:
  c.poly([(x+dx,y+1),(x+dx+2,y+1),(x+dx+3 if dx>0 else x+dx,y+10),(x+dx+1 if dx>0 else x+dx-2,y+10)],ink)
  c.line(x+dx+1,y+3,x+dx+2 if dx>0 else x+dx-1,y+9,mid)
 c.line(x-4,y+7,x+4,y+7,ink);c.line(x-3,y+6,x+4,y+6,wood)
 c.ellipse(x,y,7,3,ink);c.ellipse(x,y-1,6,2,mid)
 c.line(x-4,y-2,x+3,y-2,gold);c.line(x-3,y,x+4,y,wood)
 c.line(x-5,y+2,x+5,y+2,wooddark)
# cropped barrel at left and a final floor glint
c.poly([(0,35),(3,36),(4,41),(4,46),(2,50),(0,50)],ink)
c.rect(0,38,2,10,wood);c.line(0,40,3,40,'#92907a');c.line(0,46,3,46,'#92907a')
view(result)
finish(result)
