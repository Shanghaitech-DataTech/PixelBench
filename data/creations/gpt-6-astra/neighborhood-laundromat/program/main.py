result = new_canvas(64,64,background='#bbcdd6',name='Neighborhood Laundromat')
c=result
ink='#344958'; dark='#263c50'; edge='#6e8999'; wall='#c6d8dd'; white='#edf6f4'; light='#dce9e9'; shade='#9eb5bf'; floor='#a2bac3'
# room shell and ceiling
c.rect(0,0,64,6,'#92abb9')
c.rect(2,6,60,29,wall)
c.poly([(0,3),(3,6),(3,35),(0,39)],'#9db7c2')
c.poly([(61,6),(63,3),(63,39),(61,35)],'#a8c1ca')
c.line(3,6,60,6,'#e7f2ef')
c.rect(3,31,58,5,'#829fab')
c.line(3,31,60,31,'#aec5cd')
# two cool fluorescent fixtures
for x in (9,35):
 c.rect(x,2,20,3,'#637f90'); c.rect(x+1,2,18,2,'#f5fffa'); c.line(x+2,5,x+17,5,'#d9f0ed')
# tiled floor
c.poly([(0,37),(3,35),(61,35),(63,38),(63,63),(0,63)],floor)
for y in (39,46,55): c.line(0,y,63,y,'#89a4af')
for a,b in [(10,0),(24,20),(39,42),(53,63)]: c.line(a,35,b,63,'#89a4af')
c.line(0,63,63,63,'#708d9b')
# wall sign
c.rect(6,10,31,9,'#8ba6b2')
c.rect(6,9,30,9,'#476c80')
c.text(8,10,'WASH',white,spacing=1)
c.line(8,17,33,17,'#79aeb9')
# clock
c.circle(50,13,6,edge); c.circle(50,12,6,ink); c.circle(50,12,5,white)
for x,y in [(50,8),(54,12),(50,16),(46,12)]: c.set(x,y,edge)
c.line(50,12,50,9,ink); c.line(50,12,53,13,ink); c.set(50,12,'#cb7972')
# back plumbing visible between machines
c.line(5,20,59,20,'#829da8')
# each washer an independent outlined appliance
def washer(x,y,w=12,h=16):
 c.rect(x+1,y+h,w,2,'#7f99a6')
 c.rect(x,y,w,h,ink)
 c.rect(x+1,y+1,w-2,h-2,light)
 c.line(x+1,y+1,x+w-2,y+1,white)
 c.line(x+w-2,y+2,x+w-2,y+h-2,shade)
 c.rect(x+1,y+2,w-2,3,'#b4c9d0')
 c.rect(x+2,y+2,3,2,'#546f80')
 c.set(x+2,y+2,'#9fe0de')
 c.set(x+w-3,y+2,ink); c.set(x+w-5,y+2,white)
 cx=x+5; cy=y+10
 c.circle(cx,cy,4,'#829ca9'); c.circle(cx,cy,3,dark)
 c.line(cx-2,cy-2,cx,cy-3,'#bfd5db')
 c.set(cx-3,cy,'#bdd2d9')
 c.poly([(cx-2,cy+1),(cx,cy),(cx+2,cy+1),(cx+1,cy+3),(cx-1,cy+3)],'#467d98')
 c.line(cx-1,cy-1,cx+1,cy-2,'#7eb5c9')
 c.set(cx+2,cy+1,'#6399b0')
 c.rect(x+9,y+9,1,3,ink)
 c.line(x+2,y+h-2,x+8,y+h-2,white)
 c.set(x+2,y+h-1,dark); c.set(x+w-3,y+h-1,dark)
for x in (5,19,33,47): washer(x,21)
# foreground second bank: a little top plane is visible
c.rect(2,60,41,2,'#7d98a5')
for x in (3,16,29):
 c.poly([(x,44),(x+2,41),(x+13,41),(x+11,44)],'#f0f7f5')
 c.line(x+2,41,x+12,41,edge)
 washer(x,44)
# folding table frame and top, separate on the right
c.rect(46,53,16,2,'#8ba5af')
c.rect(47,46,2,10,ink); c.rect(59,46,2,10,ink)
c.line(49,53,58,53,'#6c8795')
c.poly([(44,44),(47,41),(61,41),(62,44)],'#f2f6ee')
c.rect(44,44,18,3,'#6e8c9b'); c.line(45,44,61,44,white)
c.line(45,45,60,45,'#bacbd0')
# neatly folded towels
c.rect(55,39,6,3,'#719b9e'); c.line(55,39,60,39,'#b9d9d0')
c.rect(56,37,5,2,'#e3e7dd'); c.line(56,37,60,37,'#fcf9eb')
# laundry basket on table with pale laundry peeking out
c.poly([(45,37),(46,35),(48,35),(49,36),(51,35),(53,37),(53,39),(45,39)],'#f4f5e9')
c.set(47,36,'#d4ded8'); c.set(51,37,'#b8ccc8')
c.poly([(44,38),(54,38),(53,43),(45,43)],'#b47460')
c.line(44,38,54,38,'#f0bd8d'); c.line(45,39,53,39,'#db9c75')
for x in (46,49,52): c.rect(x,40,1,2,'#795b56')
c.line(46,43,52,43,'#e1ab82')
# little floor mat in front of folding station
c.poly([(46,58),(59,58),(62,61),(45,61)],'#6c8d9e')
c.line(48,59,58,59,'#9db7be')
view(result)
save('neighborhood-laundromat',result)
finish(result)
