result = new_canvas(16,16,background='#858789',name='cracked_stone')
# Interlocking mineral patches wrap around the tile edges.
patches=[([(0,0),(4,0),(4,2),(2,2),(2,4),(0,4)],'#929496'), ([(6,0),(10,0),(10,2),(13,2),(13,4),(9,4),(9,3),(6,3)],'#777a7c'), ([(14,0),(15,0),(15,5),(13,5),(13,3),(14,3)],'#9b9d9e'), ([(3,4),(7,4),(7,6),(9,6),(9,8),(5,8),(5,7),(3,7)],'#96989a'), ([(0,6),(2,6),(2,9),(4,9),(4,11),(0,11)],'#777a7c'), ([(10,5),(12,5),(12,8),(15,8),(15,10),(11,10),(11,8),(10,8)],'#8f9294'), ([(5,10),(8,10),(8,12),(10,12),(10,15),(7,15),(7,14),(5,14)],'#777a7c'), ([(11,11),(15,11),(15,14),(13,14),(13,15),(11,15)],'#949698'), ([(0,13),(3,13),(3,12),(4,12),(4,15),(0,15)],'#929496')]
for p,col in patches: result.poly(p,col)
# Small square mineral flecks.
for x,y,w,col in [(3,1,2,'#9b9d9e'),(7,2,2,'#858789'),(1,7,1,'#858789'),(5,5,2,'#a4a6a7'),(8,9,2,'#777a7c'),(12,6,2,'#777a7c'),(1,14,2,'#a4a6a7'),(12,12,2,'#a4a6a7'),(6,13,1,'#858789'),(14,9,2,'#777a7c')]: result.rect(x,y,w,1,col)
# Continuous fractures; x=0 and x=15 meet at row 5.
cracks=[[(0,5),(2,5),(3,6),(3,8),(5,9),(6,9),(7,10),(10,10),(11,9),(11,7),(13,5),(15,5)],[(6,9),(6,7),(7,6),(7,4),(8,3),(8,0)],[(10,10),(10,12),(9,13),(9,15)]]
# Bottom branch connects to the top with a one-pixel step across the seam.
for chain in cracks:
 for (x,y),(xx,yy) in zip(chain,chain[1:]):
  result.line(x,y+1,xx,yy+1,'#a4a6a7') if max(y,yy)<15 else None
for chain in cracks:
 for a,b in zip(chain,chain[1:]): result.line(*a,*b,'#55595c')
for x,y in [(3,7),(6,9),(7,5),(11,8),(10,11)]: result.set(x,y,'#45494c')
result.set(9,15,'#55595c')
result.set(8,15,'#55595c')
view(result)
finish(result)
