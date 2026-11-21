result = new_canvas(64,64, '#172635', name='laundromat')
c=result
# room shell
c.rect(2,2,60,40,'#bacfda')
c.rect(3,3,58,5,'#d7e5e9')
c.rect(3,9,58,25,'#abc1cc')
c.rect(3,26,58,13,'#7999aa')
c.rect(3,26,58,1,'#e0ebed')
c.rect(2,38,60,24,'#718997')
# floor tile perspective
for y in [42,49,59]: c.line(3,y,60,y,'#536f80')
for x in [-20,0,20,40,60,80]:
    c.line(32+(x-32)//2,38,max(2,min(61,x)),61,'#536f80')
c.line(2,61,61,61,'#314e61')
# fluorescent light and cornice
c.rect(4,7,56,1,'#708e9f')
c.rect(10,4,18,3,'#7996a5');c.rect(11,4,16,2,'#f4ffff')
c.rect(38,4,17,3,'#7996a5');c.rect(39,4,15,2,'#f4ffff')
# sign and clock
c.rect(5,9,21,9,'#56788c')
c.text(6,10,'WASH','#e0eeed',font='5x7',spacing=0)
c.circle(32,13,5,'#3d596b');c.circle(32,13,4,'#eef5ef')
c.set(32,10,'#708390');c.set(35,13,'#708390');c.set(32,16,'#708390');c.set(29,13,'#708390')
c.line(32,13,32,11,'#293f51');c.line(32,13,34,14,'#293f51')
c.rect(45,11,12,6,'#d6e4e5');c.rect(46,12,7,1,'#71939e');c.rect(46,14,9,1,'#71939e')
# back row of washers, separated dark gutters
c.rect(3,20,58,20,'#344f60')
def machine(x,y,w=13,h=19):
    c.rect(x,y,w,h,'#253f51')
    c.rect(x+1,y+1,w-2,h-2,'#afc5d0')
    c.rect(x+1,y+1,w-2,3,'#e7f0ef')
    c.line(x+1,y+5,x+w-2,y+5,'#819aaa')
    c.rect(x+2,y+2,3,1,'#536d7d')
    c.set(x+w-3,y+2,'#3a8f9c')
    cx=x+w//2; cy=y+11
    c.circle(cx,cy,5,'#718d9e');c.circle(cx,cy,4,'#e2edef');c.circle(cx,cy,3,'#27485f')
    c.rect(cx-1,cy+1,3,2,'#507b92');c.set(cx+2,cy,'#83a9b6')
    c.line(cx-2,cy-1,cx,cy-2,'#9dc6d4')
    c.set(cx+4,cy,'#536b7c')
    c.line(x+2,y+h-3,x+w-3,y+h-3,'#d6e4e6')
    c.set(x+2,y+h-1,'#182e3e');c.set(x+w-3,y+h-1,'#182e3e')
for x in [4,18,32,46]:machine(x,20)
# second, nearer row left
c.rect(3,44,31,16,'#40596a')
# machine bodies with top surface
for x in [4,19]:
    c.poly([(x,43),(x+3,40),(x+14,40),(x+13,43)],'#e3eef0')
    machine(x,43,14,18)
# folding table on right: cast shadow and legs
c.rect(39,54,20,4,'#587281')
c.rect(40,45,2,11,'#314d60');c.rect(41,46,1,9,'#b2c8d0')
c.rect(57,45,2,11,'#314d60');c.rect(57,46,1,9,'#b2c8d0')
c.poly([(37,44),(41,39),(60,39),(60,46),(37,46)],'#3b596b')
c.poly([(38,43),(41,40),(59,40),(59,44),(38,44)],'#d8e6e7')
c.line(38,45,59,45,'#91aab5')
# folded towels
c.rect(49,39,9,3,'#577e92');c.rect(49,38,8,2,'#a6ced6');c.line(50,38,56,38,'#d7edef')
c.rect(48,36,9,2,'#dce8df');c.line(49,37,56,37,'#a6bdb8')
# basket on floor, warm accent linen
c.ellipse(46,58,8,2,'#496676')
c.poly([(38,50),(53,50),(51,59),(40,59)],'#a56d51')
c.poly([(39,51),(52,51),(50,58),(41,58)],'#dfad76')
for y in [53,56]:
    for x in [41,44,47,50]: c.rect(x,y,2,1,'#93674f')
c.line(39,50,52,50,'#f1cc94')
# laundry protrudes from basket
c.poly([(40,49),(41,46),(45,46),(46,49),(49,47),(51,49),(51,50),(40,50)],'#e9eee7')
c.line(43,47,44,49,'#acc7d0');c.line(48,49,49,49,'#abc5ca')
# wall edge
c.line(61,8,61,37,'#638194')
view(c)
finish(result)
