result = new_canvas(32, 32, name='microscope')
c=result
ink='#182638'
shade='#34465b'
mid='#688698'
light='#b8d3d9'
white='#edf7ed'
teal='#367e8a'
bright='#64c7ce'
gold='#e5ae58'
# Rear cast-metal arm, with angular perspective and open throat
c.poly([(21,8),(25,10),(27,14),(27,24),(23,27),(18,25),(21,22),(22,15),(19,12)],ink)
c.poly([(23,10),(25,12),(25,23),(22,25),(20,24),(23,21),(24,15),(21,12)],mid)
c.line(25,14,25,22,light)
c.poly([(25,12),(26,14),(26,24),(23,26),(22,25),(25,22)],shade)
# Broad weighted foot, front and right faces
c.poly([(13,24),(22,24),(28,27),(28,29),(24,31),(6,30),(3,28),(4,26)],ink)
c.poly([(13,25),(21,25),(26,27),(22,29),(7,28),(5,27)],light)
c.poly([(6,28),(22,29),(26,27),(27,28),(24,30),(7,29)],mid)
c.line(8,26,16,25,white)
# Illuminator rising off the base
c.poly([(13,23),(17,22),(20,24),(18,27),(12,26)],shade)
c.poly([(13,23),(17,23),(19,24),(16,25),(12,24)],ink)
c.line(14,23,17,23,bright)
c.line(13,24,16,24,light)
# Stage: dark slab with a visible thickness and oblique edges
c.poly([(7,17),(20,16),(25,19),(21,22),(7,21),(4,19)],ink)
c.poly([(8,17),(20,17),(23,19),(19,20),(7,19)],mid)
c.poly([(7,20),(20,21),(23,20),(21,21),(8,20)],shade)
# Glass slide and two retaining clips
c.poly([(10,17),(16,17),(19,18),(13,19),(9,18)],light)
c.line(13,18,16,18,bright)
c.set(9,17,white)
c.line(19,18,21,19,white)
# Tilted head and body tube, shaded left to right
c.poly([(9,5),(13,3),(21,10),(21,12),(17,15),(14,13),(14,11)],ink)
c.poly([(10,6),(13,5),(19,10),(17,12),(15,11)],light)
c.line(11,6,17,11,white)
c.poly([(19,10),(20,11),(17,14),(15,12),(17,12)],mid)
# Rotating nosepiece and two objective lenses
c.poly([(16,12),(20,11),(22,13),(19,15),(15,14)],ink)
c.line(17,13,20,12,mid)
c.poly([(17,14),(19,14),(18,17),(16,17)],ink)
c.line(17,14,17,16,light)
c.set(17,17,gold)
c.poly([(20,14),(22,14),(23,16),(21,17)],ink)
c.line(21,14,22,16,light)
c.set(22,16,gold)
# Focus wheel on the outside of the arm
c.circle(24,14,3,ink)
c.circle(24,14,2,mid)
c.line(23,13,24,12,light)
c.rect(24,14,2,2,shade)
c.set(24,14,bright)
# Eyepiece barrel and dark glass at its upper end
c.poly([(7,3),(10,1),(13,2),(15,5),(11,8),(9,7)],ink)
c.poly([(8,4),(11,2),(12,3),(14,5),(11,7)],shade)
c.line(9,4,11,3,bright)
c.line(11,6,13,5,light)
c.line(8,3,10,2,mid)
view(result)
finish(result)
