result = new_canvas(64, 32, name='city_bus')
c = result
ink='#192632'
edge='#354b5b'
body='#e0e8df'
white='#f6f5df'
teal='#228b8c'
light='#55b7ad'
dark='#153e51'
glass='#28576b'
shine='#6596a3'
# Silhouette: flat roof, rounded forward corner, low floor.
c.poly([(3,7),(5,5),(55,5),(58,7),(60,12),(60,24),(58,26),(3,26),(2,24),(2,9)],ink)
c.rect(4,7,52,17,body)
c.rect(3,10,2,13,body)
c.poly([(55,7),(57,8),(59,12),(59,23),(55,24)],body)
# Roof cap and upper trim.
c.line(6,6,54,6,white)
c.line(4,7,55,7,'#bacdc8')
c.rect(15,4,15,1,edge)
c.rect(18,3,10,1,'#a1b7b8')
c.rect(36,4,10,1,'#a1b7b8')
# Belt and lower body panels.
c.rect(3,18,56,6,teal)
c.line(4,18,58,18,light)
c.rect(4,23,54,2,'#19656e')
c.line(4,25,58,25,edge)
# Repeated passenger windows; pillars remain as pale bodywork.
for x,w in [(5,7),(14,7),(33,7),(42,7)]:
    c.rect(x,9,w,8,ink)
    c.rect(x+1,10,w-2,6,glass)
    c.line(x+1,10,x+w-2,10,shine)
    c.line(x+1,11,x+1,14,'#3f7386')
    c.line(x+2,15,x+w-2,15,dark)
# Rear double door, recessed all the way to the skirt.
c.rect(23,9,8,16,ink)
c.rect(24,10,6,13,'#819da0')
for x in [24,28]:
    c.rect(x,10,2,10,dark)
    c.line(x,10,x+1,10,shine)
    c.rect(x,11,2,6,glass)
c.line(27,10,27,23,ink)
c.line(24,23,29,23,'#bacdc8')
c.set(26,19,white)
c.set(28,19,white)
# Front door and driver glazing, paired black-framed leaves.
c.rect(50,8,8,17,ink)
c.rect(51,12,6,11,'#91a9a8')
for x in [51,55]:
    c.rect(x,12,2,9,glass)
    c.line(x,12,x+1,12,shine)
    c.line(x,18,x+1,18,dark)
c.line(54,12,54,23,ink)
c.line(51,23,56,23,'#d4dfd6')
c.set(53,20,white)
c.set(55,20,white)
# Windshield sliver on the slanted nose.
c.poly([(58,10),(59,12),(59,18),(58,18)],dark)
c.line(59,13,59,16,shine)
# Small electronic sign above front doors, amber pixel lettering.
c.rect(50,8,8,3,'#10252c')
for x,y in [(51,9),(52,9),(54,9),(56,9)]:
    c.set(x,y,'#f6b74c')
c.set(52,10,'#b87932')
# Body seams and ventilation grille.
c.line(14,20,20,20,'#63b3ac')
c.line(34,20,44,20,'#63b3ac')
for y in [20,22]:
    c.line(5,y,9,y,'#195c65')
c.rect(45,19,3,2,body)
c.set(46,19,white)
# Wheel arches, two tires and metal hubs.
for x in [13,44]:
    c.circle(x,25,5,ink)
    c.circle(x,25,4,'#29333e')
    c.circle(x,25,2,'#9aafb6')
    c.line(x-1,24,x+1,24,'#dce5df')
    c.set(x,25,'#526875')
    c.line(x-1,28,x+1,28,'#111d29')
    c.line(x-2,21,x+2,21,'#a9c4bc')
# Front bumper, lights, rear lamps and side marker.
c.rect(58,22,3,3,edge)
c.rect(58,20,2,2,'#fff1b6')
c.set(59,20,'#fffbe8')
c.rect(2,20,2,3,'#a9454d')
c.set(2,20,'#ff8a64')
c.set(36,23,'#f3bc59')
# Exterior mirror arm and housing.
c.line(59,11,61,11,ink)
c.rect(61,12,2,3,ink)
c.set(61,12,'#718d97')
view(result)
finish(result)
