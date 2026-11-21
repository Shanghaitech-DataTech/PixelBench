result = new_canvas(64,64,background='#222f43',name='laundromat')
c=result
# room shell
c.rect(2,2,60,38,'#b4cbd6')
c.rect(3,3,58,4,'#dcebf0')
c.poly([(2,36),(61,36),(63,62),(0,62)],'#7894aa')
c.rect(2,35,60,3,'#526d86')
# tiled floor perspective
for y in [42,49,58]: c.line(1,y,62,y,'#9fb6c5')
for x in [-20,0,20,40,60,80]:
    c.line(32+(x-32)//2,38,max(0,min(63,x)),62,'#9fb6c5')
c.rect(0,62,64,2,'#263b50')
# ceiling luminaires
for x in [7,39]:
 c.rect(x,4,18,3,'#7f9aaa');c.rect(x+1,4,16,2,'#f3ffff')
# wall clock
c.circle(32,13,5,'#536e86');c.circle(32,13,4,'#ecf5f4')
c.set(32,10,'#768e9c');c.set(29,13,'#768e9c');c.set(35,13,'#768e9c')
c.line(32,13,32,11,'#263b50');c.line(32,13,34,14,'#263b50')
# signage
c.rect(4,9,22,9,'#557a91');c.text(5,10,'WASH','#e6f5f4',spacing=0)
c.rect(43,11,13,4,'#d5e4e6');c.line(45,12,53,12,'#7698aa');c.line(45,14,50,14,'#7698aa')
# stacked two rows of individually outlined front loading machines
# shadow behind the bank
c.rect(3,19,58,31,'#31485c')
def machine(x,y,num):
 c.rect(x,y,13,14,'#425a70')
 c.rect(x+1,y,11,13,'#d4e2e7')
 c.rect(x+1,y,11,1,'#f0f8f7')
 c.rect(x+1,y+1,11,3,'#a8bfcc')
 c.rect(x+2,y+2,3,1,'#eef6f4')
 c.rect(x+7,y+1,3,2,'#38576b');c.set(x+8,y+1,'#78d8d7')
 c.set(x+11,y+2,'#eff8f3')
 c.circle(x+6,y+8,4,'#708c9f')
 c.circle(x+6,y+8,3,'#243e54')
 c.rect(x+4,y+9,4,2,'#4f819d')
 c.set(x+4,y+6,'#b5e5ed');c.set(x+3,y+7,'#81b8ce')
 c.line(x+5,y+11,x+7,y+11,'#a9c7d4')
 c.set(x+10,y+8,'#f5ffff')
 c.line(x+2,y+12,x+10,y+12,'#8ea8b9')
for y in [20,35]:
 for i,x in enumerate([4,18,32,46]): machine(x,y,i)
# folding table right foreground, shadow and legs
c.ellipse(47,58,13,3,'#617d95')
c.rect(38,51,2,9,'#354d65');c.rect(57,51,2,9,'#354d65')
c.rect(40,51,1,7,'#b0c5cf');c.rect(56,51,1,7,'#b0c5cf')
c.poly([(37,47),(58,47),(61,51),(35,51)],'#eef0df')
c.rect(35,51,27,2,'#acb5ae');c.line(36,51,60,51,'#d8ded2')
# folded towels
c.rect(46,46,10,3,'#558d9e');c.rect(46,46,9,1,'#8ac5ca')
c.rect(47,44,8,2,'#e3b9b0');c.line(48,44,54,44,'#f4d6c9')
# basket on floor, overflowing cloth
c.ellipse(16,58,10,2,'#526e87')
c.poly([(8,49),(25,49),(23,58),(10,58)],'#c39365')
c.poly([(10,50),(23,50),(21,57),(12,57)],'#ebc58c')
c.poly([(11,49),(12,46),(16,45),(19,48),(22,47),(24,50)],'#d3e5e8')
c.poly([(12,48),(15,46),(17,48),(16,51),(12,51)],'#799cb8')
c.line(8,50,25,50,'#f9dfa8')
for y in [52,55]:
 for x in [12,16,20]: c.rect(x,y,2,1,'#997c61')
c.line(11,58,22,58,'#f0cc92')
view(c)
finish(result)
