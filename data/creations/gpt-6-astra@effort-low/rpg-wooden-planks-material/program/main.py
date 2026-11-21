result = new_canvas(16,16,background='#92552e',name='wood_planks')
# Four boards, with grooves continuing over the repeat boundary.
base=['#a86938','#bd8047','#985c32','#b37640']
light=['#c38a4d','#d49755','#b67b41','#ce9050']
shade='#794424'
groove='#50321f'
for i in range(4):
 x=i*4
 result.rect(x,0,1,16,groove)
 result.rect(x+1,0,3,16,base[i])
 result.rect(x+1,0,1,16,light[i])
# Staggered end joints and end-grain shadows.
for i,y in enumerate([3,11,7,15]):
 x=i*4
 result.line(x+1,y,x+3,y,'#603920')
 result.line(x+1,(y+1)%16,x+3,(y+1)%16,light[i])
 result.set(x+3,(y-1)%16,shade)
# Narrow irregular grain runs, naturally wrapping at the tile edge.
for x,ys in [(3,[0,1,5,6,7,11,12,13,14,15]),(7,[0,1,2,6,7,8,13,14,15]),(11,[1,2,3,4,9,10,14]),(15,[0,1,2,3,7,8,9,12,13])]:
 for y in ys: result.set(x,y,shade)
result.set(2,8,'#8a4d28')
result.set(2,9,'#8a4d28')
result.set(6,3,'#a06030')
result.set(6,4,'#a06030')
result.set(10,11,'#7d4727')
result.set(14,5,'#9a5b2d')
# Two tiny elongated knots, with a lit lower rim.
for x,y in [(6,7),(14,11)]:
 result.set(x,y-1,shade)
 result.set(x-1,y,shade)
 result.set(x,y,groove)
 result.set(x+1,y,shade)
 result.set(x,y+1,shade)
 result.set(x,y+2,'#d49755')
view(result)
finish(result)
