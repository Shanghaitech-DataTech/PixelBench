import random
random.seed(17)
result=input_canvas.copy(name='output')
# Restore the sky and distant vegetation behind the person.
patch=new_canvas(170,170)
patch.poly([(78,69),(86,69),(87,115),(83,124),(79,124),(79,91),(75,87),(73,77)],'#fff')
for y in range(68,125):
 for x in range(72,89):
  if patch.get(x,y)!=0 and patch.to_rgba()[2][(y*170+x)*4+3]:
   result.set(x,y,input_canvas.get(64+(x%7),y))
# Rebuild the vending machine face, keeping its original side and the scooter.
result.poly([(81,60),(85,57),(114,55),(118,59),(118,110),(111,116),(91,117),(81,122)],'#241e46')
result.line(82,62,82,113,'#51446b')
result.poly([(85,61),(114,58),(115,98),(111,104),(85,107)],'#c69bc7')
result.poly([(86,62),(113,60),(113,98),(110,102),(86,104)],'#f6d8c4')
# Lit shelves, with small individually shaded bottles and cans.
for row,y in enumerate([63,76,89]):
 for col,x in enumerate([87,94,101,108]):
  shade=['#c47942','#bf694a','#65a4b4','#a376bf'][(col+row)%4]
  result.rect(x,y+2,4,8,shade)
  result.rect(x+1,y,2,2,'#e9d0b3')
  result.line(x,y+3,x,y+8,'#ffe6cf')
  result.rect(x+1,y+5,3,2,'#ded8cf')
  result.set(x+3,y+9,'#6c687b')
 result.line(86,y+11,113,y+9,'#706570')
 result.line(86,y+12,113,y+10,'#fff0ce')
result.poly([(85,106),(110,104),(110,111),(85,115)],'#352e51')
result.poly([(88,108),(105,106),(105,110),(88,112)],'#121f33')
result.line(89,112,104,110,'#716382')
result.rect(113,105,2,3,'#84c6c5')
result.set(113,105,'#e4edce')
# Clean the last coat pixels along the machine's left edge.
for y in range(109,124):
 for x in range(79,82):
  result.set(x,y,input_canvas.get(70,y))
# Cool storm light over the original scene.
tint=new_canvas(170,170,background='#10294428')
result=flatten([result,tint],name='storm')
# Forked lightning in the open sky.
glow=new_canvas(170,170)
bolts=[[(101,0),(98,9),(104,15),(95,25),(100,24),(91,37),(88,45)],[(101,15),(111,22),(108,27),(115,33)],[(95,25),(86,27),(81,34)]]
for pts in bolts:
 for a,b in zip(pts,pts[1:]):
  for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:glow.line(a[0]+dx,a[1]+dy,b[0]+dx,b[1]+dy,'#94badc40')
result=flatten([result,glow],name='lit_storm')
for i,pts in enumerate(bolts):
 for a,b in zip(pts,pts[1:]):result.line(*a,*b,'#d5eeef' if i==0 else '#86b6cf')
# Wet pavement: broken horizontal reflections, pooling water, splash rings.
wet=new_canvas(170,170)
for i in range(110):
 x=random.randrange(170); y=random.randrange(153,170)
 col=random.choice(['#5594ab65','#8fc1cc65','#233c5470','#a2beca50'])
 wet.line(x,y,min(169,x+random.randrange(2,9)),y,col)
for x,y in [(15,155),(37,161),(67,154),(120,160),(142,157),(157,165),(84,165)]:
 wet.line(x-3,y,x+3,y,'#8ab4c27a');wet.set(x-4,y-1,'#739eae70');wet.set(x+4,y-1,'#739eae70')
 wet.set(x,y-2,'#d0e0dd90')
# Reflected vending light below the bike.
for y in range(161,170,2):
 for j in range(3):
  x=random.randrange(76,107)
  wet.line(x,y,x+random.randrange(2,6),y,'#eac1cc65')
result=flatten([result,wet],name='wet_scene')
# Windblown translucent rain, kept fine enough to retain scene detail.
rain=new_canvas(170,170)
for i in range(180):
 x=random.randrange(2,170);y=random.randrange(0,168)
 length=random.choice([2,3,3,4,5])
 rain.line(x,y,max(0,x-1),min(169,y+length),random.choice(['#9dc6da48','#bddbea65','#7ba6bf50','#d7e9ee80']))
for x,y in [(37,71),(37,93),(134,88),(134,111),(116,72),(116,94),(48,123),(54,137),(109,143),(115,150),(35,138)]:
 rain.line(x,y,x,y+2,'#c2dfebaa');rain.set(x-1,y+2,'#77b2cf90');rain.set(x,y,'#e0f2efba')
result=flatten([result,rain],name='output_final')
view(result,scale=4,margin=0)
finish(result)
