output = input_canvas.copy(name='output')
colors={5:'#713a9d',6:'#ad70d1',7:'#ad70d1',8:'#ad70d1',9:'#452052',10:'#ad70d1'}
for y in range(64):
 for x in range(64):
  p=input_canvas.get(x,y)
  if p in colors: output.set(x,y,colors[p])
def block(x,y,w,h,col):
 output.rect(x*2,y*2,w*2,h*2,col)
def bubble(x,y,r=2):
 # stepped bubbles on the same two-pixel grid as the bottle
 if r==2:
  block(x+1,y,2,1,'#69338b');block(x,y+1,1,2,'#69338b');block(x+3,y+1,1,2,'#69338b');block(x+1,y+3,2,1,'#69338b')
  block(x+1,y+1,2,2,'#d89cef');block(x+1,y+1,1,1,'#f7e4ff')
 else:
  block(x+1,y,1,1,'#9053b3');block(x,y+1,3,1,'#9053b3');block(x+1,y+2,1,1,'#9053b3');block(x+1,y+1,1,1,'#f0c7ff')
bubble(12,9)
bubble(19,7,1)
bubble(20,12)
bubble(7,14,1)
bubble(14,16,1)
# small foamy glints on the elliptical liquid surface
block(10,14,4,1,'#ba7cda')
block(6,17,3,1,'#ba7cda')
block(19,18,4,1,'#ba7cda')
# submerged rising bubbles
bubble(10,24,1)
bubble(18,23)
bubble(14,28,1)
view(output)
finish(output)
