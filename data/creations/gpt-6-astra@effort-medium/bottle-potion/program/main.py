result = input_canvas.copy(name='output')
colors={5:'#7136ac',6:'#ac72d8',7:'#ac72d8',8:'#ac72d8',9:'#45205f',10:'#ac72d8'}
for y in range(64):
 for x in range(64):
  p=input_canvas.get(x,y)
  if p in colors: result.set(x,y,colors[p])
# Keep the source's two-pixel block scale for the potion details.
def block(x,y,col): result.rect(x*2,y*2,2,2,col)
def bubble(x,y,r=2):
 if r==2:
  pattern=['.aa.','abca','acda','.aa.']
 else:
  pattern=['.a.','aba','.a.']
 cols={'a':'#d6a1f2','b':'#fff0ff','c':'#9951ce','d':'#7936ad'}
 for j,row in enumerate(pattern):
  for i,k in enumerate(row):
   if k!='.': block(x+i,y+j,cols[k])
bubble(10,8,2)
bubble(19,10,1)
bubble(22,5,1)
bubble(7,14,2)
bubble(17,16,2)
bubble(22,15,1)
# Tiny glowing beads and pale ripples on the surface.
block(14,15,'#edc9ff')
block(12,18,'#c780e9')
result.rect(22,38,10,2,'#aa64d3')
result.rect(24,40,6,2,'#9149bf')
# Suspended bubbles beneath the surface.
bubble(12,24,2)
bubble(19,23,1)
block(10,27,'#d6a1f2')
# A short reflected gleam in the liquid.
result.rect(10,44,2,4,'#e6bcf6')
result.rect(12,48,2,4,'#d6a1f2')
view(result)
finish(result)
