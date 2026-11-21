result = new_canvas(32,32,name='microscope')
c=result
ink='#192b40'
shadow='#35516a'
mid='#66899b'
light='#a9c7ce'
white='#e3f1e9'
teal='#237f90'
cyan='#59c7c5'
darkteal='#225465'
# broad cast base in three-quarter perspective
c.poly([(8,24),(20,23),(27,26),(27,29),(24,30),(7,30),(4,28),(4,26)],ink)
c.poly([(8,24),(20,24),(25,26),(22,28),(6,28),(5,26)],mid)
c.poly([(8,24),(18,24),(21,25),(18,26),(6,26)],light)
c.line(7,29,23,29,shadow)
c.line(25,27,25,28,mid)
# bent support arm, behind optical assembly
c.poly([(20,9),(23,10),(25,14),(25,23),(22,26),(18,26),(17,24),(20,21),(20,16),(17,13)],ink)
c.poly([(21,10),(23,12),(24,15),(24,22),(21,25),(19,25),(21,21),(21,15),(19,12)],teal)
c.line(23,15,23,22,cyan)
c.line(21,24,23,22,mid)
# illuminator on base
c.poly([(12,23),(16,22),(19,24),(16,26),(12,25)],ink)
c.poly([(13,23),(16,23),(17,24),(15,25),(13,24)],light)
c.set(15,23,white)
# stage slab and diagonal top
c.poly([(8,17),(18,16),(23,18),(23,20),(13,22),(7,20),(7,18)],ink)
c.poly([(9,17),(18,17),(21,18),(13,20),(8,19)],shadow)
c.line(8,20,13,21,mid)
c.line(14,21,22,19,shadow)
# glass slide and stage clips
c.poly([(11,18),(16,17),(19,18),(14,19)],cyan)
c.line(12,18,15,18,white)
c.set(10,18,light)
c.set(18,19,light)
# focusing wheel on arm
c.circle(23,14,3,ink)
c.circle(23,14,2,mid)
c.line(22,13,23,12,light)
c.rect(23,14,2,2,shadow)
c.set(23,14,white)
# objective turret and two objective lenses
c.poly([(13,10),(19,11),(20,13),(16,15),(12,13)],ink)
c.poly([(14,11),(18,11),(19,12),(15,14),(13,12)],mid)
c.poly([(17,13),(19,13),(19,16),(17,17),(16,16)],ink)
c.line(18,14,18,15,light)
c.set(17,16,cyan)
c.poly([(13,12),(16,13),(14,17),(11,16)],ink)
c.line(13,13,12,15,white)
c.line(14,14,13,16,mid)
c.set(12,16,cyan)
# sloping body tube
c.poly([(8,5),(12,4),(19,10),(19,12),(15,14),(12,12),(7,7)],ink)
c.poly([(9,6),(12,5),(17,10),(14,12)],light)
c.poly([(9,7),(13,11),(14,11),(12,8)],white)
c.poly([(14,12),(17,10),(18,11),(15,13)],teal)
# dark eyepiece and its rim
c.poly([(7,1),(10,1),(13,4),(13,6),(9,8),(5,4),(5,3)],ink)
c.poly([(7,2),(9,2),(11,4),(8,6),(6,4)],shadow)
c.line(6,3,8,2,mid)
c.line(9,6,12,4,light)
c.line(10,7,12,6,teal)
view(result,scale=12)
finish(result)
