c = new_canvas(32,32,name='monarch')
black='#211d29'
orange='#ef8a24'
light='#ffb641'
red='#cb521d'
cream='#fff0ca'
# mirrored wings, with stepped dark outer margins
for flip in (False,True):
 def p(points,col):
  c.poly([(31-x if flip else x,y) for x,y in points],col)
 def line(a,b,col):
  c.line(31-a[0] if flip else a[0],a[1],31-b[0] if flip else b[0],b[1],col)
 def dot(x,y,col): c.set(31-x if flip else x,y,col)
 p([(14,14),(11,8),(6,3),(2,2),(1,4),(1,11),(3,16),(7,19),(13,19)],black)
 p([(13,18),(7,16),(3,18),(2,22),(3,26),(6,29),(9,29),(12,27),(14,22)],black)
 # forewing cells
 p([(3,5),(6,6),(10,10),(12,14),(8,12),(4,9)],light)
 p([(3,10),(7,13),(11,15),(6,15),(4,14)],orange)
 p([(5,16),(9,16),(13,17),(11,18),(8,18)],red)
 p([(8,7),(11,10),(13,14),(13,15),(11,12)],orange)
 # dark veins separate the long forewing panels
 line((5,6),(12,14),black)
 # hindwing radial cells
 p([(12,19),(9,19),(6,18),(4,20),(8,21)],orange)
 p([(12,20),(8,22),(5,21),(4,23),(5,25),(8,24)],light)
 p([(12,21),(9,25),(6,26),(7,27),(9,27),(11,25)],orange)
 p([(13,21),(12,25),(11,27),(13,25)],red)
 # cream dots on the black edge
 for x,y in [(3,3),(5,4),(2,6),(2,9),(3,12),(4,15),(4,19),(3,22),(4,25),(6,27),(9,28),(12,26)]: dot(x,y,cream)
# body, head and tapered abdomen
c.line(15,12,15,24,black)
c.line(16,12,16,24,black)
c.rect(14,14,4,5,black)
c.rect(15,11,2,3,black)
c.line(15,24,15,26,black)
c.set(15,14,'#786046')
c.line(15,17,15,22,'#554132')
# fine antennae
c.line(15,11,13,8,black)
c.line(16,11,18,8,black)
c.set(12,8,black)
c.set(19,8,black)
view(c)
finish(c)
