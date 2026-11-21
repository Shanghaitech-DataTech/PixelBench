f1=new_canvas(41,28,name='original')
f1.blit(input_canvas,7,4)
f2=new_canvas(41,28,name='raised_wings')
a='#1d181e'; d='#432f53'; c='#b572b1'; e='#5f5f7b'; h='#5c436f'
# Broad raised wings with a dark silhouette and scalloped trailing edges.
for side in [0,1]:
 def pts(p): return [(40-x if side else x,y) for x,y in p]
 def poly(p,col): f2.poly(pts(p),col)
 def line(x,y,u,v,col):
  p=pts([(x,y),(u,v)]); f2.line(*p[0],*p[1],col)
 poly([(16,10),(13,7),(10,5),(6,3),(1,0),(1,8),(2,13),(4,11),(6,11),(7,16),(9,13),(11,13),(13,17),(14,14),(16,14)],a)
 poly([(15,10),(12,7),(9,5),(6,4),(2,2),(2,8),(3,11),(4,10),(6,10),(8,13),(9,12),(11,12),(13,14),(14,13),(16,13)],d)
 poly([(3,3),(6,5),(9,6),(12,8),(15,11),(13,12),(10,10),(7,9),(4,9)],h)
 poly([(3,4),(5,5),(6,9),(4,9),(3,10)],e)
 poly([(7,6),(10,7),(12,9),(9,9),(8,11)],e)
 line(2,2,6,4,c); line(6,4,10,6,c); line(10,6,13,8,c); line(13,8,15,10,c)
 line(3,3,6,10,d); line(7,5,11,12,d); line(10,7,13,14,d)
 line(2,4,2,8,h)
# Keep the original head, torso and feet pixel-for-pixel.
for y in range(16):
 for x in range(9,18):
  col=input_canvas.get(x,y)
  if col != 0: f2.set(x+7,y+4,col)
view(f1,scale=10)
view(f2,scale=10)
finish([f1,f2])
