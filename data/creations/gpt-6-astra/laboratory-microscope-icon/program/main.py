result = new_canvas(32,32,name='microscope')
c=result
ink='#192735'
dark='#30475b'
shade='#537387'
steel='#89a9b8'
light='#c7dde0'
white='#f0f4e9'
teal='#348f9b'
bright='#65c9c4'
# heavy, angled foot: top plane and thickness
c.poly([(8,25),(21,24),(27,27),(27,29),(24,30),(6,30),(3,28),(3,27)],ink)
c.poly([(8,25),(21,25),(25,27),(23,28),(6,28),(5,27)],steel)
c.poly([(7,26),(19,25),(22,26),(19,27),(7,27)],light)
c.line(6,29,23,29,dark)
c.line(24,28,26,27,shade)
# upright curved arm behind the optical assembly
c.poly([(20,8),(24,9),(26,12),(26,22),(23,27),(18,27),(17,24),(20,22),(21,18),(21,13),(18,12)],ink)
c.poly([(22,10),(24,11),(25,13),(25,21),(22,25),(19,25),(21,22),(23,17),(23,13),(21,12)],shade)
c.line(24,13,24,20,steel)
c.line(22,23,21,24,light)
# substage illuminator
c.poly([(12,23),(16,22),(19,23),(19,25),(15,26),(11,25)],ink)
c.poly([(12,23),(16,23),(18,24),(15,25),(12,24)],teal)
c.line(13,23,16,23,bright)
# stage, horizontal top and front thickness
c.poly([(7,18),(20,17),(24,19),(21,22),(7,22),(4,20)],ink)
c.poly([(8,18),(19,18),(22,19),(19,20),(6,20)],shade)
c.line(7,21,20,21,dark)
# glass slide on stage
c.poly([(10,18),(16,18),(18,19),(11,19)],light)
c.set(14,18,bright)
c.set(8,19,white)
c.set(19,19,steel)
# tilted main body tube, optical axis descends right
c.poly([(9,5),(13,4),(19,11),(19,13),(15,16),(12,13),(8,8)],ink)
c.poly([(10,6),(12,5),(17,11),(14,13),(10,9)],light)
c.poly([(12,6),(13,6),(18,12),(16,14),(14,12)],steel)
c.line(10,7,14,11,white)
c.line(15,13,18,11,shade)
# revolving nosepiece
c.poly([(14,13),(18,12),(21,14),(18,16),(14,16)],ink)
c.line(15,14,18,13,shade)
c.set(19,14,steel)
# two discrete objectives
c.poly([(14,15),(16,15),(16,18),(14,18),(13,17)],ink)
c.line(14,15,15,17,light)
c.poly([(18,15),(20,14),(22,17),(20,19),(19,18)],ink)
c.line(19,15,21,17,steel)
c.set(20,17,bright)
# eyepiece barrel with dark ocular lens
c.poly([(5,4),(8,2),(10,2),(13,5),(9,8),(7,7)],ink)
c.poly([(8,3),(10,3),(12,5),(9,7),(7,5)],shade)
c.line(8,3,10,5,steel)
c.line(6,4,8,6,dark)
c.set(7,4,bright)
# large focus knob on near face
c.circle(23,13,3,ink)
c.circle(23,13,2,steel)
c.line(22,12,23,11,light)
c.line(24,13,23,15,shade)
c.set(23,13,dark)
view(result,scale=12)
finish(result)
