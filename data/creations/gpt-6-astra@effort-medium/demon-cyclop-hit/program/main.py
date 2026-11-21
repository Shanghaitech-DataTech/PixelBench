f1=new_canvas(47,39,name='original')
f1.blit(input_canvas,4,3)
# Edit the expression before articulating the body.
p=input_canvas.copy(name='expression')
ink='#141b1b'; gold='#ffe18d'; skin='#adbc3a'; shade='#74a334'; white='#fce2ca'
p.rect(17,16,3,3,white)
p.rect(19,15,3,3,ink)
p.set(21,17,white)
# Open jaw, rim, tooth and tongue.
p.poly([(15,22),(21,22),(23,24),(22,27),(16,27),(14,25)],shade)
p.rect(16,23,6,3,ink)
p.rect(17,26,4,1,ink)
p.rect(16,23,2,1,white)
p.rect(18,25,3,1,'#bd6460')
f2=new_canvas(47,39,name='recoil')
# The planted right-hand foot anchors the backward tilt.
for y in range(33):
 for x in range(37):
  if y>=26 and x<=14: continue
  idx=p.get(x,y)
  if p.palette()[idx]['rgba'][3]==0: continue
  lean=round(max(0,29-y)*0.19)
  f2.set(x+4+lean,y+3,idx)
# Raised right leg (left side of image): knee out, sole above ground.
def poly(points,col): f2.poly([(x+4,y+3) for x,y in points],col)
poly([(10,25),(14,26),(13,28),(9,29),(5,29),(3,27),(4,25),(7,25),(8,24)],ink)
poly([(9,25),(12,26),(11,27),(8,28),(5,28),(4,27),(5,26),(8,26)],shade)
f2.set(8,30,gold)
f2.set(9,31,gold)
f3=new_canvas(47,39,name='impact')
# Apply the red impact filter to every opaque monster pixel, retaining shading.
colors={}
for y in range(39):
 for x in range(47):
  idx=f2.get(x,y)
  rgba=f2.palette()[idx]['rgba']
  if rgba[3]:
   r,g,b,a=rgba
   colors[idx]=(min(255,round(r*.57+116)),round(g*.34),round(b*.34),a)
   f3.set(x,y,colors[idx])
view(f1,scale=8)
view(f2,scale=8)
view(f3,scale=8)
finish([f1,f2,f3])
