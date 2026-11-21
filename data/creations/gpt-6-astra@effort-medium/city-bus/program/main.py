result = new_canvas(64,32,name='city_bus')
c=result
ink='#182736'
# Main silhouette and roof
c.poly([(4,6),(54,6),(58,8),(60,12),(60,24),(58,26),(3,26),(2,24),(2,9)],ink)
c.rect(5,5,47,1,'#506879')
c.rect(5,7,49,2,'#e5eff0')
c.line(55,8,57,9,'#b0c7cc')
c.rect(3,10,56,13,'#d6e5e6')
c.rect(3,20,56,4,'#22a6ac')
c.rect(3,24,56,1,'#16747f')
# dark continuous glazing strip
c.rect(4,9,51,10,ink)
c.poly([(55,9),(57,10),(59,13),(59,19),(55,19)],ink)
# passenger windows
for x,w in [(5,7),(22,7),(31,7),(40,7)]:
 c.rect(x,10,w,7,'#365568')
 c.rect(x,10,w,1,'#7ea5b2')
 c.line(x,11,x+w-1,11,'#4e7589')
 c.line(x+1,15,x+3,13,'#527c8e')
 c.rect(x,17,w,1,'#243e50')
# rear double door and front double door
for x in [13,48]:
 c.rect(x,9,8,16,ink)
 c.rect(x+1,10,6,13,'#63818d')
 for dx in [1,4]:
  c.rect(x+dx,10,2,8,'#304d60')
  c.rect(x+dx,10,2,1,'#90b3bd')
  c.rect(x+dx,19,2,4,'#acc4c9')
 c.line(x+3,10,x+3,23,ink)
 c.line(x+1,24,x+6,24,'#8aa4ab')
 c.set(x+2,19,'#f1d27a')
 c.set(x+4,19,'#f1d27a')
# windscreen at nose
c.poly([(56,11),(57,12),(58,14),(58,17),(56,17)],'#557e90')
c.line(56,12,56,15,'#9ac4ce')
# side route display above central windows
c.rect(32,9,14,4,'#162b32')
for x,y in [(33,10),(34,10),(34,11),(33,12),(34,12),(37,10),(38,10),(40,10),(41,10),(43,10),(44,10),(37,12),(39,12),(41,12),(43,12)]:
 c.set(x,y,'#ffc15b')
# body trim and service hatch
c.line(22,19,46,19,'#f3f6ee')
c.rect(25,21,12,2,'#16838d')
c.line(26,21,35,21,'#59c3c4')
c.set(36,22,'#b8e2dc')
c.line(5,21,10,21,'#155865')
c.line(5,23,10,23,'#155865')
# wheel arches, tires, hubs
for x in [10,41]:
 c.rect(x-4,24,9,2,ink)
 c.circle(x,25,4,ink)
 c.circle(x,25,3,'#243541')
 c.circle(x,25,2,'#9db0b9')
 c.line(x-1,24,x+1,24,'#e5eded')
 c.set(x,25,'#425968')
 c.set(x,27,'#627b8b')
# lamps, bumpers, mirror
c.rect(3,19,2,3,'#bf5360')
c.set(3,19,'#ff9281')
c.rect(57,20,3,2,'#fff0b3')
c.set(59,20,'#ffffff')
c.rect(57,23,3,2,'#425a68')
c.rect(2,23,3,2,'#425a68')
c.set(24,23,'#ffcb71')
c.line(59,12,61,12,ink)
c.rect(61,12,1,3,'#506c7c')
view(result)
finish(result)
