result = new_canvas(64,64, '#a9cbd3', name='offshore')
c=result
sky='#a9cbd3'; cloud='#c8dce0'; pale='#e2e9de'; steel='#d2dedb'; shadow='#78949d'; dark='#354f60'; deep='#244d65'; sea='#38758a'; wave='#71a9b4'; yellow='#e8b84e'; orange='#ea7837'
# sky and distant atmospheric clouds
c.rect(0,27,64,9,'#b9d4d8')
c.line(2,9,14,9,cloud); c.line(5,8,11,8,cloud)
c.line(46,6,61,6,cloud); c.line(50,5,57,5,cloud)
c.line(0,23,10,23,cloud)
# sea distinct horizon
c.rect(0,36,64,28,sea)
c.line(0,36,63,36,'#5b929e')
# distant turbines
for x,y in [(10,24),(52,21)]:
 c.line(x,y,x,37,'#819fa6'); c.line(x+1,y+3,x+1,36,'#cadcda')
 c.line(x,y,x-1,y-10,pale)
 c.line(x,y,x-8,y+5,pale)
 c.line(x,y,x+8,y+4,pale)
 c.set(x,y,'#e9eee3')
 c.line(x-2,38,x+3,38,'#97bec1')
# wave strips
for x,y,w in [(0,41,7),(16,39,6),(42,41,7),(55,44,8),(4,48,9),(18,46,5),(44,49,8),(1,57,7),(12,54,6),(49,57,10),(35,60,7),(20,62,7),(58,52,5)]:
 c.line(x,y,x+w-1,y,wave)
 c.line(x+2,y+1,x+w,y+1,'#2e637d')
# submerged structure and reflections
c.poly([(26,49),(38,49),(41,63),(24,63)],'#2e637d')
c.line(28,58,36,58,'#428397');c.line(26,62,34,62,'#528f9d')
# main turbine tower tapered
c.poly([(30,12),(33,12),(36,48),(28,48)],dark)
c.poly([(30,13),(32,13),(33,47),(29,47)],steel)
c.line(30,18,30,42,pale)
c.poly([(33,18),(34,30),(35,45),(33,45)],shadow)
# yellow transition support below platform
c.rect(28,45,9,10,dark);c.rect(29,46,6,8,'#bd883b');c.rect(29,46,2,8,yellow)
c.rect(28,53,9,2,dark)
# platform braces
c.line(21,45,28,51,dark);c.line(41,45,36,51,dark)
c.line(23,46,28,49,shadow)
# maintenance platform railings
c.line(21,38,42,38,yellow)
for x in [21,26,37,42]:
 c.line(x,38,x,44,dark); c.line(x,38,x,41,yellow)
c.line(21,41,42,41,'#b68d43')
c.rect(20,44,24,3,dark);c.line(20,44,43,44,steel);c.line(21,45,42,45,'#859ca2')
# access ladder hanging on near side
c.line(24,43,24,59,dark);c.line(28,43,28,59,dark)
for y in range(44,60,2): c.line(24,y,28,y,'#b5c5bf')
c.line(24,43,24,58,yellow);c.line(28,43,28,58,'#c6a14b')
# technician 10 px tall incl helmet, gripping ladder
c.line(25,52,24,56,'#233d50');c.line(27,52,27,55,'#233d50')
c.set(23,56,'#142f43');c.line(27,55,28,55,'#142f43')
c.rect(24,48,4,5,orange)
c.line(24,49,22,51,orange);c.set(22,52,'#ead1a4')
c.line(27,49,29,47,orange);c.set(29,46,'#ead1a4')
c.rect(25,47,2,2,'#b98d6b')
c.rect(24,46,3,2,yellow);c.line(24,47,27,47,'#ffe093')
c.line(25,49,25,52,'#f9d879');c.line(24,51,27,51,'#f9d879');c.set(26,52,dark)
# nacelle and main rotor
c.rect(29,10,8,4,shadow);c.rect(29,10,7,3,steel);c.line(30,10,35,10,pale)
# blades sweep distinct from tower
c.poly([(30,11),(28,10),(26,1),(28,1),(31,10)],pale)
c.poly([(30,12),(29,14),(16,23),(18,19),(28,11)],pale)
c.line(17,22,28,13,shadow)
c.poly([(31,11),(34,10),(47,15),(43,15),(32,13)],pale)
c.circle(30,12,2,shadow);c.circle(30,11,1,pale)
# foam around footing
c.line(30,56,37,56,wave);c.line(36,55,40,55,'#a9ccca');c.line(31,57,35,57,'#b9d8d2')
view(result)
finish(result)
