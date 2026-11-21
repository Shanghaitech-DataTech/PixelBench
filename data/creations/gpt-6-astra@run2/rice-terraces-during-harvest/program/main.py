import random
result = new_canvas(64,64,background='#727d58',name='harvest_terraces')
c=result
# Muted high slopes and village shelf
c.poly([(0,0),(64,0),(64,17),(49,15),(39,12),(28,13),(14,19),(0,19)],'#7c8963')
c.poly([(0,0),(37,0),(28,4),(17,6),(8,11),(0,12)],'#596e57')
c.poly([(0,0),(23,0),(15,3),(5,5),(0,8)],'#465e4c')
c.path('M 0 15 Q 13 9 26 9 Q 44 6 64 13 L 64 22 L 0 24 Z','#969369')
c.path('M 0 19 Q 16 13 28 13 Q 47 12 64 18', '#b4ae79',fill=False)
# tiny distant trees
for x,y in [(5,9),(9,8),(31,5),(44,7),(55,10),(60,11)]:
 c.rect(x,y,1,4,'#58664b'); c.rect(x-1,y-1,3,3,'#647551'); c.set(x,y-2,'#71825c')
# village homes: walls, shadow sides, tiled roofs
for x,y,w in [(15,7,6),(25,4,7),(37,7,6)]:
 c.rect(x,y+2,w,5,'#d0bc87')
 c.rect(x+w-2,y+2,2,5,'#9b9168')
 c.poly([(x-1,y+2),(x+1,y-1),(x+w-2,y-1),(x+w+1,y+2)],'#665e50')
 c.line(x+1,y-1,x+w-2,y-1,'#92816a')
 c.rect(x+2,y+4,1,3,'#645f4b')
 c.set(x+w-2,y+3,'#e0c997')
# contours: a broad descending amphitheatre with irregular curved shelves
# bands painted from distant pale gold to deep ochre foreground
bands=[
 ('M 0 19 Q 12 23 24 18 Q 39 10 50 16 Q 58 20 64 20 L 64 64 L 0 64 Z','#76754b'),
 ('M 0 21 Q 13 25 25 20 Q 39 13 50 18 Q 58 22 64 22 L 64 64 L 0 64 Z','#d1b760'),
 ('M 0 25 Q 15 30 28 23 Q 39 18 49 23 Q 56 27 64 26 L 64 64 L 0 64 Z','#85804a'),
 ('M 0 27 Q 15 32 28 25 Q 39 20 49 25 Q 56 29 64 28 L 64 64 L 0 64 Z','#e1bf55'),
 ('M 0 33 Q 15 38 29 30 Q 41 24 50 31 Q 58 35 64 33 L 64 64 L 0 64 Z','#77713b'),
 ('M 0 35 Q 15 40 29 32 Q 41 26 50 33 Q 58 37 64 35 L 64 64 L 0 64 Z','#d4a43b'),
 ('M 0 42 Q 15 46 30 39 Q 41 33 50 40 Q 59 44 64 41 L 64 64 L 0 64 Z','#665e32'),
 ('M 0 45 Q 15 49 30 42 Q 41 36 50 43 Q 59 47 64 44 L 64 64 L 0 64 Z','#e0ae3d'),
 ('M 0 53 Q 17 57 31 49 Q 42 43 51 50 Q 58 54 64 51 L 64 64 L 0 64 Z','#58552e'),
 ('M 0 56 Q 17 60 31 52 Q 42 46 51 53 Q 58 57 64 54 L 64 64 L 0 64 Z','#bb842e'),
 ('M 0 64 Q 17 67 32 60 Q 43 54 52 61 Q 59 64 64 62 L 64 64 Z','#494b2c')]
for path,col in bands:c.path(path,col)
# lit grassy lips on narrow terrace paths
for path in ['M 0 19 Q 12 23 24 18 Q 39 10 50 16 Q 58 20 63 20','M 0 25 Q 15 30 28 23 Q 39 18 49 23 Q 56 27 63 26','M 0 33 Q 15 38 29 30 Q 41 24 50 31 Q 58 35 63 33','M 0 42 Q 15 46 30 39 Q 41 33 50 40 Q 59 44 63 41','M 0 53 Q 17 57 31 49 Q 42 43 51 50 Q 58 54 63 51']:
 c.path(path,'#b4a04f',fill=False)
# Sparse clustered rice heads, restricted to each planted shelf
random.seed(21)
fields={'#d1b760':('#e4ce7a','#b39a48'),'#e1bf55':('#f2d36f','#c6a046'),'#d4a43b':('#ebc459','#b78e32'),'#e0ae3d':('#f4cd61','#bd8f30'),'#bb842e':('#dcab45','#9d702d')}
lookup={c.color(k):v for k,v in fields.items()}
for y in range(18,64):
 for x in range(64):
  idx=c.get(x,y)
  if idx in lookup and random.random()<0.21:
   light,shade=lookup[idx]
   if y>0 and c.get(x,y-1)==idx:
    c.set(x,y,shade);c.set(x,y-1,light)
# harvested patches and cut sheaves
for x,y in [(6,39),(11,40),(52,46),(57,47),(23,56)]:
 c.line(x-1,y+1,x+1,y+1,'#9b762e')
 c.line(x,y,x-1,y-2,'#f0c65c');c.line(x,y,x+1,y-2,'#f0c65c');c.set(x,y-1,'#806334')
# Two farmers with straw conical hats; feet planted on terrace ridges
def farmer(x,y,shirt):
 c.line(x,y+3,x+3,y+3,'#57542f')
 c.set(x,y+2,'#403f31');c.set(x+2,y+2,'#403f31')
 c.rect(x,y-1,3,3,shirt)
 c.set(x-1,y,'#d6a371');c.set(x+3,y,'#d6a371')
 c.line(x,y-2,x+2,y-2,'#755a37')
 c.set(x+1,y-2,'#d6a371')
 c.line(x-1,y-3,x+3,y-3,'#f5d68a')
 c.line(x,y-4,x+2,y-4,'#e9bf68')
 c.set(x+1,y-5,'#f5d68a')
 c.set(x+2,y-3,'#bc8a42')
farmer(19,30,'#556b6a')
farmer(44,43,'#964c35')
# sickle and wicker harvest basket beside the nearer farmer
c.line(48,43,49,41,'#6d5131');c.set(50,40,'#d9d2a2')
c.rect(40,44,3,3,'#94612d');c.line(40,44,42,44,'#e1b451');c.set(41,45,'#c59239')
view(result,scale=8,margin=0)
finish(result)
