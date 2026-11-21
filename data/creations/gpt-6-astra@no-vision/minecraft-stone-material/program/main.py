result = new_canvas(16, 16, background='#858680', name='cracked_stone')
c = result
base='#858680'; mid='#93948e'; light='#a3a49c'; shade='#747670'; deep='#62655f'; crack='#4e514c'; rim='#b1b2aa'
# Broad, irregular mineral clusters keep the texture readable at native size.
c.poly([(0,0),(3,0),(3,3),(2,5),(0,5)],mid)
c.poly([(7,0),(12,0),(12,2),(10,2),(10,4),(7,4)],shade)
c.rect(13,0,3,3,mid)
c.poly([(0,6),(2,5),(4,6),(4,8),(2,9),(0,8)],shade)
c.poly([(8,4),(11,3),(14,4),(15,6),(13,7),(9,7)],mid)
c.rect(10,4,3,2,light)
c.poly([(7,10),(10,11),(13,11),(14,14),(12,15),(8,15),(7,13)],shade)
c.poly([(0,13),(2,12),(3,13),(3,15),(0,15)],mid)
c.rect(0,14,2,2,light)
c.rect(14,13,2,3,mid)
c.rect(8,12,3,2,deep)
c.line(8,14,10,14,base)
c.line(1,1,2,1,light)
c.line(1,7,2,7,deep)
c.line(13,1,14,1,light)
c.line(9,1,10,1,deep)
c.set(13,8,shade)
c.line(6,11,6,13,mid)
# Broken highlights follow just one lip of each fracture.
c.line(6,0,5,3,light)
c.line(5,3,7,5,light)
c.line(7,5,7,7,light)
c.line(8,8,10,8,light)
c.line(10,8,12,8,light)
c.line(13,9,15,10,mid)
c.line(5,10,5,13,light)
c.line(5,13,6,15,light)
c.line(0,12,2,11,light)
# The crack network reconnects across opposite borders.
points=[(5,0),(4,2),(4,3),(6,5),(6,7),(9,9),(12,9),(15,11)]
for a,b in zip(points,points[1:]): c.line(*a,*b,crack)
points=[(6,7),(6,8),(4,10),(4,13),(5,15)]
for a,b in zip(points,points[1:]): c.line(*a,*b,crack)
points=[(0,11),(2,10),(4,10)]
for a,b in zip(points,points[1:]): c.line(*a,*b,crack)
# A few shallow chips vary the depth without adding noisy single-pixel grain.
c.line(1,3,2,3,shade)
c.line(11,6,12,6,base)
c.set(3,9,deep)
c.set(7,6, rim)
c.set(5,12,rim)
print(c.stats_text())
print(c.matrix_text())
save('cracked_stone',result)
finish(result)
