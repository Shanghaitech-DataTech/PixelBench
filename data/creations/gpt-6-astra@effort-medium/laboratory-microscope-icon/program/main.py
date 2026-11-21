c = new_canvas(32,32,name='microscope')
ink='#172636'
dark='#30465b'
mid='#57788b'
light='#9cbdc9'
white='#deedf0'
teal='#3d929e'
# cast metal base, three-quarter footprint
c.poly([(6,24),(19,23),(27,26),(27,28),(22,30),(5,29),(3,27)],ink)
c.poly([(6,24),(19,24),(25,26),(21,28),(5,27)],light)
c.poly([(5,27),(21,28),(26,26),(26,28),(22,29),(5,28)],mid)
c.line(7,25,17,25,white)
# curved rear support
c.poly([(19,9),(23,10),(25,14),(25,23),(22,26),(17,26),(17,23),(20,21),(21,15),(18,13)],ink)
c.poly([(21,11),(23,12),(24,15),(24,22),(21,25),(18,25),(18,24),(22,21),(22,15),(20,13)],mid)
c.line(23,15,23,21,light)
# illuminator on base
c.poly([(11,23),(15,22),(18,23),(18,25),(14,26),(10,25)],dark)
c.poly([(11,23),(15,23),(17,24),(14,25),(11,24)],teal)
c.line(12,23,15,23,white)
# stage with depth
c.poly([(6,17),(18,16),(23,19),(23,21),(10,22),(5,20),(5,18)],ink)
c.poly([(7,17),(18,17),(21,19),(10,20),(6,19)],mid)
c.line(7,18,13,18,light)
c.line(10,21,21,20,dark)
# glass slide and clips
c.line(11,18,17,18,white)
c.set(14,18,teal)
c.set(10,18,dark)
c.set(18,18,dark)
# objective turret
c.poly([(12,10),(18,10),(20,12),(17,14),(12,13)],ink)
c.line(13,12,17,12,light)
# objective barrels
c.poly([(11,12),(14,13),(13,16),(11,16),(10,15)],ink)
c.line(12,13,11,15,white)
c.poly([(16,12),(18,13),(18,16),(16,17),(15,15)],ink)
c.rect(16,13,1,3,light)
c.set(16,16,'#daa65d')
# angled body tube
c.poly([(9,4),(13,3),(20,9),(19,12),(16,13),(9,7)],ink)
c.poly([(10,5),(13,4),(18,9),(16,11),(10,6)],white)
c.poly([(16,11),(18,9),(19,10),(18,12)],mid)
c.line(11,7,15,11,light)
# eyepiece sleeve
c.poly([(7,3),(10,1),(13,3),(13,5),(10,7),(7,5)],ink)
c.line(8,3,10,2,mid)
c.line(9,5,12,3,dark)
c.line(10,6,13,4,teal)
# focus adjustment, visible near-side knob
c.circle(23,13,3,ink)
c.circle(23,13,2,mid)
c.line(22,12,23,11,light)
c.rect(23,13,2,2,dark)
c.set(23,13,light)
view(c)
finish(c)
