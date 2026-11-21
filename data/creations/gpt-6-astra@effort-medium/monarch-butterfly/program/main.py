result = new_canvas(32,32,name='monarch')
k='#211c29'
o='#ed802a'
l='#ffb447'
r='#b84c25'
w='#fff0ce'
# The left pair of wings; mirror to keep the silhouette balanced.
a=new_canvas(32,32,name='wings')
a.poly([(14,14),(12,9),(8,4),(3,2),(1,3),(1,9),(3,15),(5,18),(3,20),(3,24),(5,28),(8,29),(11,28),(14,24),(15,19)],k)
a.poly([(13,14),(10,9),(6,5),(3,4),(3,9),(5,14),(8,17),(13,18)],o)
a.poly([(4,5),(7,6),(10,10),(11,12),(7,10),(4,8)],l)
a.poly([(5,11),(8,12),(12,16),(8,16)],'#f59a32')
a.poly([(6,19),(10,19),(13,20),(12,24),(9,27),(6,26),(5,23)],o)
a.poly([(6,20),(10,20),(9,24),(6,24)],l)
a.poly([(10,25),(13,21),(12,25),(9,27),(6,26)],r)
# Wing veins radiate from the thorax.
a.line(14,18,8,9,k)
a.line(10,12,3,9,k)
a.line(11,14,5,14,k)
a.line(14,19,6,18,k)
a.line(13,20,6,25,k)
a.line(10,23,10,27,k)
a.line(9,23,5,22,k)
# Pale marginal spots on the dark scalloped borders.
for x,y in [(2,4),(2,7),(3,11),(4,14),(6,16),(4,20),(4,23),(5,26),(7,28),(10,27),(12,25)]:
 a.set(x,y,w)
a.set(5,3,'#ffd99d')
a.set(8,6,w)
a.set(10,8,w)
result.blit(a,0,0)
a.mirror('h')
result.blit(a,0,0)
# Abdomen, thorax, head, and fine antennae.
result.line(15,11,12,7,k)
result.line(16,11,19,7,k)
result.set(12,6,k).set(19,6,k)
result.rect(15,11,2,14,k)
result.rect(14,14,4,6,k)
result.set(15,12,'#83746a')
result.line(15,15,15,19,'#665354')
result.set(15,22,'#aa8161')
result.set(16,24,'#665354')
view(result)
finish(result)
