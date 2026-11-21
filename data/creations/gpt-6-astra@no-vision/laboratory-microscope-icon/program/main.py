result = new_canvas(32, 32, name="laboratory_microscope")
c = result
# Small, cool enamel and steel palette, with dark blue outlines.
ink = '#172537'
shadow = '#2d4358'
steel = '#536e82'
mid = '#83a8b8'
light = '#c4dce0'
white = '#f0f6eb'
teal = '#338c9b'
teal_dark = '#246575'
teal_light = '#62bdc5'
glass = '#76d9de'
# Cast-metal base, seen from above and from the front.
c.poly([(5,25),(20,23),(27,26),(27,29),(22,31),(6,30),(3,28)], ink)
c.poly([(5,25),(20,24),(26,26),(22,28),(5,28),(4,27)], mid)
c.poly([(5,28),(22,28),(26,26),(26,28),(22,30),(6,29)], steel)
c.line(7,25,18,24, light)
c.line(7,26,19,25, light)
c.line(7,29,20,30, shadow)
# Curving support arm: a thick rear casting to the right of the optics.
c.poly([(21,8),(25,9),(28,13),(28,20),(25,25),(21,27),(16,26),(16,23),(20,23),(23,19),(23,14),(20,12)], ink)
c.poly([(22,9),(25,11),(27,14),(27,20),(24,24),(21,25),(18,25),(18,24),(21,23),(24,19),(24,14),(21,11)], teal)
c.poly([(25,12),(27,15),(27,20),(24,24),(21,25),(19,25),(22,23),(25,19)], teal_dark)
c.line(22,10,25,13, teal_light)
c.line(26,14,26,18, teal_light)
# Illuminator inset into the foot, pointing up through the stage.
c.poly([(12,24),(16,23),(19,25),(16,27),(12,26)], ink)
c.poly([(13,24),(16,24),(17,25),(15,26),(13,25)], steel)
c.line(14,24,16,24, glass)
# Stage: broad dark horizontal diamond, with a visible front thickness.
c.poly([(6,17),(19,15),(24,18),(24,20),(12,22),(5,19)], ink)
c.poly([(6,17),(18,16),(22,18),(12,20),(6,18)], steel)
c.poly([(6,19),(12,21),(23,19),(23,20),(12,22)], shadow)
c.line(7,17,17,16, mid)
# Slide and silver retaining clips.
c.poly([(10,17),(17,17),(19,18),(12,19)], light)
c.line(12,17,16,17, white)
c.set(14,18,glass)
c.line(8,18,10,19,white)
c.line(19,17,21,18,mid)
# Main sloping optical tube, angled up-left.
c.poly([(9,4),(13,3),(21,10),(21,12),(17,15),(14,13),(8,7)], ink)
c.poly([(10,5),(13,4),(20,10),(17,13),(15,12)], mid)
c.poly([(10,5),(11,5),(18,11),(17,12),(14,10)], light)
c.poly([(19,10),(20,10),(20,12),(17,14),(16,12)], steel)
# Revolving nosepiece and separate objectives.
c.poly([(14,12),(18,11),(21,13),(18,15),(14,15),(12,14)], ink)
c.line(14,13,18,12, light)
c.line(14,14,18,14, steel)
# Left objective is shorter, the central objective descends toward slide.
c.poly([(12,14),(14,14),(15,16),(13,17),(11,15)], ink)
c.line(12,14,13,15, mid)
c.poly([(16,14),(19,14),(19,16),(17,18),(15,17)], ink)
c.line(17,15,17,16, light)
c.set(16,17,teal_light)
c.set(18,15,steel)
# Eyepiece sleeve and dark ocular, clearly distinct from the body.
c.poly([(6,2),(9,1),(14,5),(14,7),(11,9),(8,7),(5,4)], ink)
c.poly([(7,3),(9,2),(12,5),(9,7),(6,4)], steel)
c.line(7,3,9,2, light)
c.line(9,4,11,6, mid)
c.poly([(5,2),(8,1),(10,2),(10,4),(7,6),(4,4)], ink)
c.line(5,2,8,1, mid)
c.line(5,3,7,4, shadow)
c.set(8,2,glass)
# Focus wheel sits proud of the support on its visible right-hand side.
c.circle(25,13,3,ink)
c.circle(25,13,2,steel)
c.line(24,12,25,11,light)
c.line(26,12,26,14,mid)
c.set(25,13,shadow)
c.set(25,16,teal_dark)
# Fine focus screw below the coarse wheel.
c.circle(25,18,1,ink)
c.set(25,18,mid)
print(c.stats_text())
print(c.matrix_text())
finish(result)
