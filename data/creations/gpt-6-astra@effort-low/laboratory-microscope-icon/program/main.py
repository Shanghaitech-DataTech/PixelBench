result = new_canvas(32,32)
c=result
ink='#192b3e'
shadow='#3b566b'
mid='#7796a5'
light='#bbd5da'
white='#edf5e9'
teal='#399eaa'
# three-quarter foot
c.poly([(7,25),(20,23),(27,26),(27,29),(11,30),(4,28),(4,26)],ink)
c.poly([(6,25),(20,24),(25,26),(12,28),(5,27)],light)
c.poly([(12,28),(26,26),(26,28),(12,29)],shadow)
c.line(6,26,11,27,white)
# curved supporting arm, behind optical assembly
c.path('M 19 10 L 23 10 Q 27 11 27 16 L 25 23 L 22 26 L 17 26 L 17 23 L 21 22 L 23 17 L 22 14 L 19 14 Z',ink)
c.path('M 21 11 L 23 11 Q 25 12 25 16 L 23 22 L 21 24 L 18 24 L 22 21 L 24 16 L 22 13 L 20 13 Z',mid)
c.line(24,12,25,14,light)
# illuminator
c.poly([(12,23),(16,22),(19,23),(19,25),(15,26),(12,25)],ink)
c.poly([(13,23),(16,23),(18,24),(15,25)],teal)
c.set(15,23,'#9ee8e5')
# stage and its depth
c.poly([(6,18),(17,16),(23,18),(23,20),(11,22),(6,20)],ink)
c.poly([(7,18),(17,17),(21,18),(11,20)],mid)
c.line(11,21,22,19,shadow)
# glass specimen slide
c.poly([(10,18),(16,17),(19,18),(13,19)],'#d6f3eb')
c.line(13,18,15,18,teal)
# tube angled down-right from eyepiece
c.poly([(10,5),(14,3),(20,10),(19,13),(16,14),(9,7)],ink)
c.poly([(11,6),(14,5),(18,10),(16,12)],light)
c.line(11,6,16,11,white)
c.poly([(16,12),(19,10),(19,12),(17,13)],shadow)
# ocular barrel
c.poly([(7,3),(11,1),(15,4),(15,6),(11,8),(7,5)],ink)
c.poly([(8,3),(11,2),(13,4),(10,6)],shadow)
c.line(10,6,13,5,mid)
c.line(8,3,10,2,'#5699ad')
# nosepiece and objectives
c.poly([(15,12),(19,11),(21,13),(18,15),(15,14)],ink)
c.line(16,12,19,12,mid)
c.poly([(16,14),(18,14),(18,17),(16,18),(15,17)],ink)
c.line(16,15,16,16,white)
c.set(17,17,teal)
c.line(20,14,21,16,mid)
c.set(21,17,ink)
# focus knob on the arm
c.circle(24,16,3,ink)
c.circle(24,16,2,shadow)
c.line(23,15,24,14,light)
c.set(24,16,mid)
c.set(25,17,'#283d51')
view(result)
finish(result)
